from decouple import config
from docling.document_converter import DocumentConverter
from langchain_anthropic import ChatAnthropic
from langchain_core.output_parsers.string import StrOutputParser
from langchain_core.prompts import PromptTemplate

from core.models import UploadedFile


def process_file(uploaded_file_id: int):
    converter = DocumentConverter()
    uploaded_file = UploadedFile.objects.get(id=uploaded_file_id)
    result = converter.convert(uploaded_file.file.path)
    uploaded_file.processed_data = result.document.export_to_markdown()
    uploaded_file.save()
    return uploaded_file.processed_data


def process_markdown_with_llm(markdown_text: str, file_id: int):
    template = """
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

    # Build a prompt and LLM chain
    prompt = PromptTemplate.from_template(template)
    llm = ChatAnthropic(
        model='claude-3-opus-20240229',
        api_key=config('ANTHROPIC_API_KEY'),
        max_tokens_to_sample=4096,
    )
    chain = prompt | llm | StrOutputParser()
    # Invoke chain with markdown_text as positional argument
    result = chain.invoke(markdown_text)
    uploaded_file = UploadedFile.objects.get(id=file_id)
    uploaded_file.processed_data_json = result
    uploaded_file.save()
    return result
