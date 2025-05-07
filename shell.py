from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers.string import StrOutputParser
from dotenv import load_dotenv, find_dotenv

from docling.document_converter import DocumentConverter
# from core.models import UploadedFile


def process_file(uploaded_file: str):
    converter = DocumentConverter()
    result = converter.convert(uploaded_file)
    return result.document.export_to_markdown()
    # uploaded_file.processed_data = result.document.export_to_markdown()
    # uploaded_file.save()
    # return uploaded_file.processed_data


texto = """
[2025-05-04 01:58:39,082: WARNING/ForkPoolWorker-8] <!-- image -->

## OlÆ Joel!

## Extrato de conta corrente

Cliente:

CPF:

AgŒncia:

Conta:

Período do extrato:

077.192.704-52

20

574436-3

01/02/2025 a 28/02/2025

Joel De Farias Mendonca Junior

## Lançamentos:

R$ 1.299,26

Saldo final

| Data e hora      | Categoria       | Transaçªo                     | Descriçªo                                | Valor       |
|------------------|-----------------|-------------------------------|------------------------------------------|-------------|
| 01/02/2025 07h17 | Alimentaçªo     | Compra no dØbito autorizada   | Restaurante Rota                         | -R$ 15,46   |
| 01/02/2025 15h59 | Supermercado    | Compra no dØbito autorizada   | Supermercado Nordestªo                   | -R$ 43,71   |
| 01/02/2025 20h31 | Transporte      | Compra no dØbito autorizada   | Uber                                     | -R$ 21,90   |
| 01/02/2025 22h21 | Alimentaçªo     | Compra no dØbito autorizada   | Mangai                                   | -R$ 153,13  |
| 01/02/2025 22h24 | Transporte      | Compra no dØbito autorizada   | Uber                                     | -R$ 22,93   |
| 01/02/2025 23h59 |                 |                               | Saldo DiÆrio                             | R$ 2.382,52 |
| 02/02/2025 10h02 | Supermercado    | Compra no dØbito autorizada   | Mercatto Comercio De A                   | -R$ 86,64   |
| 02/02/2025 11h07 | Outra Categoria | Pix enviado                   | Shpp Brasil Instituicao De Pagamento E S | -R$ 98,81   |
| 02/02/2025 16h34 | TransferŒncia   | Pix enviado                   | Joyce Maria Pereira De Oliveira          | -R$ 25,00   |
| 02/02/2025 20h00 | Alimentaçªo     | Compra no dØbito autorizada   | Levu Drinks                              | -R$ 140,80  |
| 02/02/2025 21h28 | TransferŒncia   | Pix recebido                  | Luma Vitória Alves Magno                 | R$ 16,00    |
| 02/02/2025 22h10 | Alimentaçªo     | Compra no dØbito autorizada   | Ddburger                                 | -R$ 75,90   |
| 02/02/2025 23h59 |                 |                               | Saldo DiÆrio                             | R$ 1.971,38 |
| 03/02/2025 09h43 | Tarifas         | Pix enviado                   | Ministerio Da Fazenda                    | -R$ 87,85   |
| 03/02/2025 09h44 | Tarifas         | Pix enviado                   | Ministerio Da Fazenda                    | -R$ 79,85   |
| 03/02/2025 12h30 | Saœde           | Pix enviado                   | Clínica Do Shopping Serviços De Saœde    | -R$ 97,20   |
| 03/02/2025 19h58 | Compras         | Pix enviado                   | Fashion Business Comercio De Roupas      | -R$ 127,84  |
| 03/02/2025 21h01 | Viagem          | Pix enviado                   | Martins Comercio De Joias Em Prata       | -R$ 229,90  |
| 03/02/2025 21h05 | Transporte      | Compra no dØbito autorizada   | Uber                                     | -R$ 9,90    |
| 03/02/2025 22h25 | Alimentaçªo     | Compra no dØbito autorizada   | Ddburger                                 | -R$ 68,40   |
| 03/02/2025 23h59 |                 |                               | Saldo DiÆrio                             | R$ 1.270,47 |
| 04/02/2025 17h37 | Alimentaçªo     | Compra no dØbito autorizada   | Chimarrao Vl                             | -R$ 25,00   |
| 04/02/2025 23h59 |                 |                               | Saldo DiÆrio                             | R$ 1.245,48 |
| 05/02/2025 10h10 | Contas          | Pix enviado                   | Brisanet                                 | -R$ 4,99    |
| 05/02/2025 10h17 | TransferŒncia   | Pix enviado                   | Ezio De Araujo Alves                     | -R$ 420,00  |
| 05/02/2025 14h13 | TransferŒncia   | Pix enviado                   | Tales Moises Barbosa Do Rego             | -R$ 165,66  |
| 05/02/2025 14h23 | Contas          | Pagamento de fatura do cartªo | Fatura do cartªo BTG Pactual             | -R$ 300,00  |
| 05/02/2025 15h42 | TransferŒncia   | Pix recebido                  | Tales Moises Barbosa Do Rego             | R$ 165,66   |
| 05/02/2025 20h37 | TransferŒncia   | Pix enviado                   | Antonia Lenilda Pereira                  | -R$ 200,00  |
| 05/02/2025 23h59 |                 |                               | Saldo DiÆrio                             | R$ 320,51   |
| 06/02/2025 16h18 | TransferŒncia   | Pix enviado                   | Sebastiao Henrique Da Cunha              | -R$ 119,00  |
| 06/02/2025 23h59 |                 |                               | Saldo DiÆrio                             | R$ 201,50   |
| 08/02/2025 11h07 | TransferŒncia   | Pix enviado                   | Jose Nildecio Fernandes Pereira          | -R$ 25,00   |
| 08/02/2025 23h59 |                 |                               | Saldo DiÆrio                             | R$ 176,50   |

03/05/2025 20h05

<!-- image -->

## OlÆ Joel!

Este Ø o extrato da sua conta corrente BTG Pactual

## Extrato de conta corrente

Cliente:

CPF:

AgŒncia:

Conta:

Período do extrato:

077.192.704-52

20

574436-3

01/02/2025 a 28/02/2025

Joel De Farias Mendonca Junior

## Lançamentos:

R$ 1.299,26

Saldo final

| Data e hora      | Categoria               | Transaçªo                     | Descriçªo                             | Valor        |
|------------------|-------------------------|-------------------------------|---------------------------------------|--------------|
| 10/02/2025 15h32 | TransferŒncia           | Pix recebido                  | Nova Data Tecnologia Ltda             | R$ 200,00    |
| 10/02/2025 16h42 | TransferŒncia           | Pix recebido                  | Nova Data Tecnologia Ltda             | R$ 4.000,00  |
| 10/02/2025 17h01 | Contas                  | Pagamento de fatura do cartªo | Fatura do cartªo BTG Pactual          | -R$ 1.112,84 |
| 10/02/2025 20h17 | TransferŒncia           | Pix enviado                   | Mariana Macena Da Silva               | -R$ 11,00    |
| 10/02/2025 23h59 |                         |                               | Saldo DiÆrio                          | R$ 3.252,66  |
| 11/02/2025 09h35 | Outra Categoria         | Pix enviado                   | Jose Everton Aquino De Queiroz        | -R$ 16,00    |
| 11/02/2025 23h59 |                         |                               | Saldo DiÆrio                          | R$ 3.236,66  |
| 12/02/2025 13h35 | TransferŒncia           | Pix enviado                   | Leticia Amaro Vieira                  | -R$ 20,00    |
| 12/02/2025 23h59 |                         |                               | Saldo DiÆrio                          | R$ 3.216,66  |
| 13/02/2025 09h54 | Outra Categoria         | Pix enviado                   | Serasa                                | -R$ 4,90     |
| 13/02/2025 10h31 | TransferŒncia           | Pix enviado                   | Ezio De Araujo Alves                  | -R$ 9,40     |
| 13/02/2025 12h03 | TransferŒncia           | Pix enviado                   | Joel De Farias Mendonca Junior        | -R$ 64,99    |
| 13/02/2025 13h12 | TransferŒncia           | Pix enviado                   | Joel De Farias Mendonca Junior        | -R$ 50,00    |
| 13/02/2025 13h46 | TransferŒncia           | Pix enviado                   | Joel De Farias Mendonca Junior        | -R$ 10,00    |
| 13/02/2025 23h59 |                         |                               | Saldo DiÆrio                          | R$ 3.077,37  |
| 14/02/2025 08h23 | CrØdito e Financiamento | Pagamento de boleto           | Luizacred                             | -R$ 64,79    |
| 14/02/2025 09h38 | TransferŒncia           | Pix enviado                   | Jeezias Bastos Da Costa Junior        | -R$ 400,00   |
| 14/02/2025 11h29 | TransferŒncia           | Pix recebido                  | Joel De Farias Mendonca Junior        | R$ 79,35     |
| 14/02/2025 21h15 | TransferŒncia           | Pix enviado                   | Francisco Clecio De Lima              | -R$ 13,00    |
| 14/02/2025 23h59 |                         |                               | Saldo DiÆrio                          | R$ 2.678,93  |
| 15/02/2025 07h41 | TransferŒncia           | Pix enviado                   | Leticia Amaro Vieira                  | -R$ 50,00    |
| 15/02/2025 23h59 |                         |                               | Saldo DiÆrio                          | R$ 2.628,94  |
| 16/02/2025 19h43 | TransferŒncia           | Pix enviado                   | Hilton Charles Pereira                | -R$ 22,92    |
| 16/02/2025 23h59 |                         |                               | Saldo DiÆrio                          | R$ 2.606,02  |
| 17/02/2025 06h01 | Casa                    | DØbito AutomÆtico             | Pagamento para Cosern                 | -R$ 158,24   |
| 17/02/2025 09h58 | TransferŒncia           | Pix enviado                   | Ezio De Araujo Alves                  | -R$ 65,24    |
| 17/02/2025 10h08 | TransferŒncia           | Pix enviado                   | Ezio De Araujo Alves                  | -R$ 36,25    |
| 17/02/2025 14h23 | Supermercado            | Compra no dØbito autorizada   | Mercadinho Sao Vicente                | -R$ 33,91    |
| 17/02/2025 23h59 |                         |                               | Saldo DiÆrio                          | R$ 2.312,39  |
| 18/02/2025 11h47 | TransferŒncia           | Pix enviado                   | Francisco Halison Pereira De Oliveira | -R$ 85,00    |
| 18/02/2025 14h39 | Supermercado            | Pix enviado                   | Nosso Atacarejo                       | -R$ 102,56   |
| 18/02/2025 21h39 | Alimentaçªo             | Compra no dØbito autorizada   | Marily Bar                            | -R$ 68,00    |
| 18/02/2025 23h59 |                         |                               | Saldo DiÆrio                          | R$ 2.056,84  |

03/05/2025 20h05

<!-- image -->

## Extrato de conta corrente

Cliente:

CPF:

AgŒncia:

Conta:

Período do extrato:

077.192.704-52

20

574436-3

01/02/2025 a 28/02/2025

Joel De Farias Mendonca Junior

## Lançamentos:

R$ 1.299,26

Saldo final

| Data e hora      | Categoria       | Transaçªo                   | Descriçªo                                | Valor       |
|------------------|-----------------|-----------------------------|------------------------------------------|-------------|
| 19/02/2025 19h30 | TransferŒncia   | Pix recebido                | Leticia Amaro Vieira                     | R$ 78,50    |
| 19/02/2025 23h59 |                 |                             | Saldo DiÆrio                             | R$ 2.135,34 |
| 20/02/2025 12h09 | TransferŒncia   | Pix recebido                | Ezio De Araujo Alves                     | R$ 34,00    |
| 20/02/2025 12h19 | TransferŒncia   | Pix recebido                | Ezio De Araujo Alves                     | R$ 17,00    |
| 20/02/2025 14h54 | Compras         | Pix enviado                 | J D Artigos Esportivos                   | -R$ 125,00  |
| 20/02/2025 18h45 | TransferŒncia   | Pix recebido                | Ezio De Araujo Alves                     | R$ 8,49     |
| 20/02/2025 18h45 | Supermercado    | Pix enviado                 | Queiroz Distribuidora Ltda               | -R$ 16,98   |
| 20/02/2025 23h59 |                 |                             | Saldo DiÆrio                             | R$ 2.052,87 |
| 21/02/2025 18h26 | Supermercado    | Pagamento de boleto         | Midway                                   | -R$ 33,32   |
| 21/02/2025 23h59 |                 |                             | Saldo DiÆrio                             | R$ 2.019,56 |
| 22/02/2025 12h48 | TransferŒncia   | Pix enviado                 | Ezio De Araujo Alves                     | -R$ 65,53   |
| 22/02/2025 19h48 | TransferŒncia   | Pix enviado                 | Leticia Amaro Vieira                     | -R$ 28,00   |
| 22/02/2025 21h53 | Alimentaçªo     | Compra no dØbito autorizada | Rota Empório Da Carne                    | -R$ 39,00   |
| 22/02/2025 23h59 |                 |                             | Saldo DiÆrio                             | R$ 1.887,04 |
| 23/02/2025 19h23 | TransferŒncia   | Pix enviado                 | ValØria Queiroz Dias De Araœjo           | -R$ 36,00   |
| 23/02/2025 23h59 |                 |                             | Saldo DiÆrio                             | R$ 1.851,04 |
| 24/02/2025 00h45 | Outra Categoria | Pix enviado                 | Shpp Brasil Instituicao De Pagamento E S | -R$ 135,67  |
| 24/02/2025 01h11 | Compras         | Pix enviado                 | A M C Davanso                            | -R$ 218,80  |
| 24/02/2025 23h59 |                 |                             | Saldo DiÆrio                             | R$ 1.496,58 |
| 26/02/2025 17h42 | Supermercado    | Pix enviado                 | Nosso Atacarejo                          | -R$ 143,54  |
| 26/02/2025 20h44 | TransferŒncia   | Pix recebido                | Ezio De Araujo Alves                     | R$ 69,35    |
| 26/02/2025 23h59 |                 |                             | Saldo DiÆrio                             | R$ 1.422,42 |
| 27/02/2025 11h48 | TransferŒncia   | Pix recebido                | 55.200.918 Daniel Vitor Silva Oliveira   | R$ 100,00   |
| 27/02/2025 23h59 |                 |                             | Saldo DiÆrio                             | R$ 1.522,43 |
| 28/02/2025 15h05 | TransferŒncia   | Pix enviado                 | Anny Suzy Araœjo Ferreira                | -R$ 2,00    |
| 28/02/2025 19h43 | Supermercado    | Compra no dØbito autorizada | Queiroz Distribuidora                    | -R$ 221,18  |
| 28/02/2025 23h59 |                 |                             | Saldo DiÆrio                             | R$ 1.299,26 |

"""

def process_markdown_with_llm(markdown_text: str):
    template = """
    Você é um analista de dados, trabalhando em um projeto de limpeza de dados.
    Seu trabalho é escolher uma categoria adequada para cada lançamento financeiro
    que vou te enviar. Os lançamentos estão em markdown, junto a outras informações
    do documento, então foque em analisar apenas os lançamentos financeiros.
    Não categorize lançamentos que já estejam categorizados.

    Todos são transações financeiras de uma pessoa física.

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
    [2025-05-04 01:58:39,082: WARNING/ForkPoolWorker-8] <!-- image -->

## OlÆ Joel!

## Extrato de conta corrente

Cliente:

CPF:

AgŒncia:

Conta:

Período do extrato:

077.192.704-52

20

574436-3

01/02/2025 a 28/02/2025

Joel De Farias Mendonca Junior

## Lançamentos:

R$ 1.299,26

Saldo final

| Data e hora      | Categoria       | Transaçªo                     | Descriçªo                                | Valor       |
|------------------|-----------------|-------------------------------|------------------------------------------|-------------|
| 01/02/2025 07h17 | Alimentaçªo     | Compra no dØbito autorizada   | Restaurante Rota                         | -R$ 15,46   |
| 01/02/2025 15h59 | Supermercado    | Compra no dØbito autorizada   | Supermercado Nordestªo                   | -R$ 43,71   |
| 01/02/2025 20h31 | Transporte      | Compra no dØbito autorizada   | Uber                                     | -R$ 21,90   |
| 01/02/2025 22h21 | Alimentaçªo     | Compra no dØbito autorizada   | Mangai                                   | -R$ 153,13  |
| 01/02/2025 22h24 | Transporte      | Compra no dØbito autorizada   | Uber                                     | -R$ 22,93   |
| 01/02/2025 23h59 |                 |                               | Saldo DiÆrio                             | R$ 2.382,52 |
| 02/02/2025 10h02 | Supermercado    | Compra no dØbito autorizada   | Mercatto Comercio De A                   | -R$ 86,64   |
| 02/02/2025 11h07 | Outra Categoria | Pix enviado                   | Shpp Brasil Instituicao De Pagamento E S | -R$ 98,81   |
| 02/02/2025 16h34 | TransferŒncia   | Pix enviado                   | Joyce Maria Pereira De Oliveira          | -R$ 25,00   |
| 02/02/2025 20h00 | Alimentaçªo     | Compra no dØbito autorizada   | Levu Drinks                              | -R$ 140,80  |
| 02/02/2025 21h28 | TransferŒncia   | Pix recebido                  | Luma Vitória Alves Magno                 | R$ 16,00    |
| 02/02/2025 22h10 | Alimentaçªo     | Compra no dØbito autorizada   | Ddburger                                 | -R$ 75,90   |
| 02/02/2025 23h59 |                 |                               | Saldo DiÆrio                             | R$ 1.971,38 |
| 03/02/2025 09h43 | Tarifas         | Pix enviado                   | Ministerio Da Fazenda                    | -R$ 87,85   |
| 03/02/2025 09h44 | Tarifas         | Pix enviado                   | Ministerio Da Fazenda                    | -R$ 79,85   |
| 03/02/2025 12h30 | Saœde           | Pix enviado                   | Clínica Do Shopping Serviços De Saœde    | -R$ 97,20   |
| 03/02/2025 19h58 | Compras         | Pix enviado                   | Fashion Business Comercio De Roupas      | -R$ 127,84  |
| 03/02/2025 21h01 | Viagem          | Pix enviado                   | Martins Comercio De Joias Em Prata       | -R$ 229,90  |
| 03/02/2025 21h05 | Transporte      | Compra no dØbito autorizada   | Uber                                     | -R$ 9,90    |
| 03/02/2025 22h25 | Alimentaçªo     | Compra no dØbito autorizada   | Ddburger                                 | -R$ 68,40   |
| 03/02/2025 23h59 |                 |                               | Saldo DiÆrio                             | R$ 1.270,47 |
| 04/02/2025 17h37 | Alimentaçªo     | Compra no dØbito autorizada   | Chimarrao Vl                             | -R$ 25,00   |
| 04/02/2025 23h59 |                 |                               | Saldo DiÆrio                             | R$ 1.245,48 |
| 05/02/2025 10h10 | Contas          | Pix enviado                   | Brisanet                                 | -R$ 4,99    |
| 05/02/2025 10h17 | TransferŒncia   | Pix enviado                   | Ezio De Araujo Alves                     | -R$ 420,00  |
| 05/02/2025 14h13 | TransferŒncia   | Pix enviado                   | Tales Moises Barbosa Do Rego             | -R$ 165,66  |
| 05/02/2025 14h23 | Contas          | Pagamento de fatura do cartªo | Fatura do cartªo BTG Pactual             | -R$ 300,00  |
| 05/02/2025 15h42 | TransferŒncia   | Pix recebido                  | Tales Moises Barbosa Do Rego             | R$ 165,66   |
| 05/02/2025 20h37 | TransferŒncia   | Pix enviado                   | Antonia Lenilda Pereira                  | -R$ 200,00  |
| 05/02/2025 23h59 |                 |                               | Saldo DiÆrio                             | R$ 320,51   |
| 06/02/2025 16h18 | TransferŒncia   | Pix enviado                   | Sebastiao Henrique Da Cunha              | -R$ 119,00  |
| 06/02/2025 23h59 |                 |                               | Saldo DiÆrio                             | R$ 201,50   |
| 08/02/2025 11h07 | TransferŒncia   | Pix enviado                   | Jose Nildecio Fernandes Pereira          | -R$ 25,00   |
| 08/02/2025 23h59 |                 |                               | Saldo DiÆrio                             | R$ 176,50   |

03/05/2025 20h05

<!-- image -->

## OlÆ Joel!

Este Ø o extrato da sua conta corrente BTG Pactual

## Extrato de conta corrente

Cliente:

CPF:

AgŒncia:

Conta:

Período do extrato:

077.192.704-52

20

574436-3

01/02/2025 a 28/02/2025

Joel De Farias Mendonca Junior

## Lançamentos:

R$ 1.299,26

Saldo final

| Data e hora      | Categoria               | Transaçªo                     | Descriçªo                             | Valor        |
|------------------|-------------------------|-------------------------------|---------------------------------------|--------------|
| 10/02/2025 15h32 | TransferŒncia           | Pix recebido                  | Nova Data Tecnologia Ltda             | R$ 200,00    |
| 10/02/2025 16h42 | TransferŒncia           | Pix recebido                  | Nova Data Tecnologia Ltda             | R$ 4.000,00  |
| 10/02/2025 17h01 | Contas                  | Pagamento de fatura do cartªo | Fatura do cartªo BTG Pactual          | -R$ 1.112,84 |
| 10/02/2025 20h17 | TransferŒncia           | Pix enviado                   | Mariana Macena Da Silva               | -R$ 11,00    |
| 10/02/2025 23h59 |                         |                               | Saldo DiÆrio                          | R$ 3.252,66  |
| 11/02/2025 09h35 | Outra Categoria         | Pix enviado                   | Jose Everton Aquino De Queiroz        | -R$ 16,00    |
| 11/02/2025 23h59 |                         |                               | Saldo DiÆrio                          | R$ 3.236,66  |
| 12/02/2025 13h35 | TransferŒncia           | Pix enviado                   | Leticia Amaro Vieira                  | -R$ 20,00    |
| 12/02/2025 23h59 |                         |                               | Saldo DiÆrio                          | R$ 3.216,66  |
| 13/02/2025 09h54 | Outra Categoria         | Pix enviado                   | Serasa                                | -R$ 4,90     |
| 13/02/2025 10h31 | TransferŒncia           | Pix enviado                   | Ezio De Araujo Alves                  | -R$ 9,40     |
| 13/02/2025 12h03 | TransferŒncia           | Pix enviado                   | Joel De Farias Mendonca Junior        | -R$ 64,99    |
| 13/02/2025 13h12 | TransferŒncia           | Pix enviado                   | Joel De Farias Mendonca Junior        | -R$ 50,00    |
| 13/02/2025 13h46 | TransferŒncia           | Pix enviado                   | Joel De Farias Mendonca Junior        | -R$ 10,00    |
| 13/02/2025 23h59 |                         |                               | Saldo DiÆrio                          | R$ 3.077,37  |
| 14/02/2025 08h23 | CrØdito e Financiamento | Pagamento de boleto           | Luizacred                             | -R$ 64,79    |
| 14/02/2025 09h38 | TransferŒncia           | Pix enviado                   | Jeezias Bastos Da Costa Junior        | -R$ 400,00   |
| 14/02/2025 11h29 | TransferŒncia           | Pix recebido                  | Joel De Farias Mendonca Junior        | R$ 79,35     |
| 14/02/2025 21h15 | TransferŒncia           | Pix enviado                   | Francisco Clecio De Lima              | -R$ 13,00    |
| 14/02/2025 23h59 |                         |                               | Saldo DiÆrio                          | R$ 2.678,93  |
| 15/02/2025 07h41 | TransferŒncia           | Pix enviado                   | Leticia Amaro Vieira                  | -R$ 50,00    |
| 15/02/2025 23h59 |                         |                               | Saldo DiÆrio                          | R$ 2.628,94  |
| 16/02/2025 19h43 | TransferŒncia           | Pix enviado                   | Hilton Charles Pereira                | -R$ 22,92    |
| 16/02/2025 23h59 |                         |                               | Saldo DiÆrio                          | R$ 2.606,02  |
| 17/02/2025 06h01 | Casa                    | DØbito AutomÆtico             | Pagamento para Cosern                 | -R$ 158,24   |
| 17/02/2025 09h58 | TransferŒncia           | Pix enviado                   | Ezio De Araujo Alves                  | -R$ 65,24    |
| 17/02/2025 10h08 | TransferŒncia           | Pix enviado                   | Ezio De Araujo Alves                  | -R$ 36,25    |
| 17/02/2025 14h23 | Supermercado            | Compra no dØbito autorizada   | Mercadinho Sao Vicente                | -R$ 33,91    |
| 17/02/2025 23h59 |                         |                               | Saldo DiÆrio                          | R$ 2.312,39  |
| 18/02/2025 11h47 | TransferŒncia           | Pix enviado                   | Francisco Halison Pereira De Oliveira | -R$ 85,00    |
| 18/02/2025 14h39 | Supermercado            | Pix enviado                   | Nosso Atacarejo                       | -R$ 102,56   |
| 18/02/2025 21h39 | Alimentaçªo             | Compra no dØbito autorizada   | Marily Bar                            | -R$ 68,00    |
| 18/02/2025 23h59 |                         |                               | Saldo DiÆrio                          | R$ 2.056,84  |

03/05/2025 20h05

<!-- image -->

## Extrato de conta corrente

Cliente:

CPF:

AgŒncia:

Conta:

Período do extrato:

077.192.704-52

20

574436-3

01/02/2025 a 28/02/2025

Joel De Farias Mendonca Junior

## Lançamentos:

R$ 1.299,26

Saldo final

| Data e hora      | Categoria       | Transaçªo                   | Descriçªo                                | Valor       |
|------------------|-----------------|-----------------------------|------------------------------------------|-------------|
| 19/02/2025 19h30 | TransferŒncia   | Pix recebido                | Leticia Amaro Vieira                     | R$ 78,50    |
| 19/02/2025 23h59 |                 |                             | Saldo DiÆrio                             | R$ 2.135,34 |
| 20/02/2025 12h09 | TransferŒncia   | Pix recebido                | Ezio De Araujo Alves                     | R$ 34,00    |
| 20/02/2025 12h19 | TransferŒncia   | Pix recebido                | Ezio De Araujo Alves                     | R$ 17,00    |
| 20/02/2025 14h54 | Compras         | Pix enviado                 | J D Artigos Esportivos                   | -R$ 125,00  |
| 20/02/2025 18h45 | TransferŒncia   | Pix recebido                | Ezio De Araujo Alves                     | R$ 8,49     |
| 20/02/2025 18h45 | Supermercado    | Pix enviado                 | Queiroz Distribuidora Ltda               | -R$ 16,98   |
| 20/02/2025 23h59 |                 |                             | Saldo DiÆrio                             | R$ 2.052,87 |
| 21/02/2025 18h26 | Supermercado    | Pagamento de boleto         | Midway                                   | -R$ 33,32   |
| 21/02/2025 23h59 |                 |                             | Saldo DiÆrio                             | R$ 2.019,56 |
| 22/02/2025 12h48 | TransferŒncia   | Pix enviado                 | Ezio De Araujo Alves                     | -R$ 65,53   |
| 22/02/2025 19h48 | TransferŒncia   | Pix enviado                 | Leticia Amaro Vieira                     | -R$ 28,00   |
| 22/02/2025 21h53 | Alimentaçªo     | Compra no dØbito autorizada | Rota Empório Da Carne                    | -R$ 39,00   |
| 22/02/2025 23h59 |                 |                             | Saldo DiÆrio                             | R$ 1.887,04 |
| 23/02/2025 19h23 | TransferŒncia   | Pix enviado                 | ValØria Queiroz Dias De Araœjo           | -R$ 36,00   |
| 23/02/2025 23h59 |                 |                             | Saldo DiÆrio                             | R$ 1.851,04 |
| 24/02/2025 00h45 | Outra Categoria | Pix enviado                 | Shpp Brasil Instituicao De Pagamento E S | -R$ 135,67  |
| 24/02/2025 01h11 | Compras         | Pix enviado                 | A M C Davanso                            | -R$ 218,80  |
| 24/02/2025 23h59 |                 |                             | Saldo DiÆrio                             | R$ 1.496,58 |
| 26/02/2025 17h42 | Supermercado    | Pix enviado                 | Nosso Atacarejo                          | -R$ 143,54  |
| 26/02/2025 20h44 | TransferŒncia   | Pix recebido                | Ezio De Araujo Alves                     | R$ 69,35    |
| 26/02/2025 23h59 |                 |                             | Saldo DiÆrio                             | R$ 1.422,42 |
| 27/02/2025 11h48 | TransferŒncia   | Pix recebido                | 55.200.918 Daniel Vitor Silva Oliveira   | R$ 100,00   |
| 27/02/2025 23h59 |                 |                             | Saldo DiÆrio                             | R$ 1.522,43 |
| 28/02/2025 15h05 | TransferŒncia   | Pix enviado                 | Anny Suzy Araœjo Ferreira                | -R$ 2,00    |
| 28/02/2025 19h43 | Supermercado    | Compra no dØbito autorizada | Queiroz Distribuidora                    | -R$ 221,18  |
| 28/02/2025 23h59 |                 |                             | Saldo DiÆrio                             | R$ 1.299,26 |

    Responda apenas com uma lista de transações, com o seguinte formato:
    [
        {
            'descrição': 'descrição da transação',
            'categoria': 'categoria da transação',
            'valor': 'valor da transação',
            'data': 'data da transação',
        },        
    ]
    """
    # Build a prompt and LLM chain
    prompt = PromptTemplate.from_template(template)
    llm = ChatOllama(model="gemma3:4b", format="json")
    chain = prompt | llm | StrOutputParser()
    # Invoke chain with markdown_text as positional argument
    return chain.invoke(markdown_text)

if __name__ == "__main__":
    result = process_markdown_with_llm(texto)
    ...
    print(result)


import json
import pendulum
from core.models import *

file = UploadedFile.objects.first()
transactions = json.loads(file.processed_data_json)

for transaction in transactions.get('context', {}):
    data = transaction.get('date', '01/01/2025')
    transaction['date'] = (pendulum.from_format(data, 'DD/MM/YY')).date()
    Transaction.objects.create(**transaction, source_file=file)
