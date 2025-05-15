import json

import pendulum
from decouple import config
from docling.document_converter import DocumentConverter
from langchain_anthropic import ChatAnthropic
from langchain_core.output_parsers.string import StrOutputParser
from langchain_core.prompts import PromptTemplate

from core.models import Transaction, UploadedFile


class FileProcessor:
    """Domain service for converting & categorizing an uploaded file."""

    LLM_PROMPT = """
    Você é um analista de dados responsável por categorizar lançamentos financeiros.  
    Receberá um bloco de texto em Markdown contendo diversos lançamentos;
    ignore todo o resto e opere apenas sobre as linhas de transação.  

    Regras:
    1. Não recategorize lançamentos que já tenham uma categoria.
    2. Use sempre o valor absoluto (sem sinais).
    3. Defina transaction_type como:
    - DEBIT, se for gasto (débito).
    - CREDIT, se for receita (crédito).
    4. Trabalhe apenas com pessoas físicas.

    Escolha uma dentre as seguintes categorias:
    - Alimentação
    - Receitas
    - Mercado
    - Saúde
    - Educação
    - Compras
    - Transporte
    - Investimento
    - Transferências para terceiros
    - Telefone
    - Moradia

    filtre e categorize estes lançamentos:
    {text}

    responda APENAS com um dicionário que contem a chave context, cujo valor é uma lista de dicionários com os seguintes campos:
    - category: categoria da transação
    - amount: valor da transação
    - date: data da transação
    - description: descrição da transação
    - transaction_type: tipo de transação (CREDIT ou DEBIT)
    """

    def __init__(self, uploaded_file: UploadedFile):
        self.uploaded_file = uploaded_file
        self.converter = DocumentConverter()
        self.llm = ChatAnthropic(
            model='claude-3-5-sonnet-latest',
            api_key=config('ANTHROPIC_API_KEY'),
            max_tokens_to_sample=4096,
        )
        self.prompt = PromptTemplate.from_template(self.LLM_PROMPT)

    def convert_to_markdown(self) -> str:
        result = self.converter.convert(self.uploaded_file.file.path)
        md = result.document.export_to_markdown()
        self.uploaded_file.markdown_data = md
        self.uploaded_file.save(update_fields=['markdown_data'])
        return md

    def categorize_transactions(self, markdown_text: str) -> dict:
        chain = self.prompt | self.llm | StrOutputParser()
        raw = chain.invoke(markdown_text)
        data = json.loads(raw)
        self.uploaded_file.json_data = raw
        self.uploaded_file.save(update_fields=['json_data'])
        return data

    def persist_transactions(self, context: list[dict]):
        transactions = []
        for transaction in context:
            transaction['date'] = pendulum.from_format(transaction['date'], 'DD/MM/YYYY').date()
            transaction['source_file'] = self.uploaded_file
            transactions.append(Transaction(**transaction))
        Transaction.objects.bulk_create(transactions)

        return {'success': True, 'file_id': self.uploaded_file.id}

    def run(self):
        md = self.convert_to_markdown()
        data = self.categorize_transactions(md)
        result = self.persist_transactions(data['context'])
        return result
