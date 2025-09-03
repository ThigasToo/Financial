# Projeto de Valuation por FCD (Fluxo de Caixa Descontado) para ITUB4

Este projeto contém um notebook Python (`DCF_ITUB4.ipynb`) que realiza uma análise de valuation para as ações do Itaú Unibanco (ITUB4) utilizando o método de Fluxo de Caixa Descontado para o Acionista (FCFE - Free Cash Flow to Equity).

O objetivo é calcular o valor intrínseco de uma ação e compará-lo com o preço de mercado atual, fornecendo uma base quantitativa para uma tese de investimento.

---

## ⚠️ AVISO IMPORTANTE: A Necessidade de uma Arquitetura de Dados

O notebook **não funciona de forma isolada**. Ele foi projetado para consumir um arquivo de dados específico chamado `Itau IRFS.csv`, que **não é gerado automaticamente**.

Antes de executar o código de valuation, é fundamental que você construa um processo para coletar, tratar e, o mais importante, **projetar** os dados financeiros da empresa. O valuation é tão bom quanto as premissas e os dados que o alimentam.

Abaixo estão os passos essenciais para construir a base de dados necessária para este projeto.

### Passos para Obtenção e Modelagem dos Dados

#### Passo 1: Identificação dos Dados Necessários
O modelo utiliza o **Fluxo de Caixa para o Acionista (FCFE)**. A fórmula básica para o FCFE é:

`FCFE = Lucro Líquido - (CAPEX - Depreciação) - Variação do Capital de Giro + Novas Dívidas - Amortização de Dívidas`

Para instituições financeiras, como o Itaú, o cálculo pode ser simplificado ou adaptado. No contexto da planilha de origem, o FCFE foi obtido a partir do **Reinvestimento**:

`FCFE = Lucro Líquido - Reinvestimento`

Onde `Reinvestimento` é o valor que a empresa retém para crescer, ou seja, o Lucro Líquido que não é distribuído como dividendos.

#### Passo 2: Fonte dos Dados Históricos
A fonte primária e mais confiável para dados financeiros são os documentos oficiais da empresa, disponíveis no site de **Relações com Investidores (RI)**.

1.  Acesse o site de RI do Itaú Unibanco.
2.  Procure por "Central de Resultados".
3.  Baixe os **Demonstrativos Financeiros (DFP / ITR)** e os **Releases de Resultados** dos últimos trimestres e anos. Neles você encontrará o Lucro Líquido e o Patrimônio Líquido.

#### Passo 3: Extração e Tratamento
Você pode extrair os dados de forma:
* **Manual:** Copiar os valores dos relatórios (geralmente em PDF) para uma planilha (Excel, Google Sheets). É um método mais simples, porém mais lento e suscetível a erros.
* **Automatizada:** Desenvolver scripts (usando Python com bibliotecas como `BeautifulSoup`, `Selenium` ou `Tabula-py`) para extrair dados de páginas web ou tabelas em PDFs. Isso exige conhecimento de programação, mas cria um processo mais robusto e escalável.

#### Passo 4: Modelagem Financeira e Projeções (O Passo Crucial)
Os dados históricos são apenas o ponto de partida. O valuation por FCD depende de **previsões futuras**. Você precisará construir um modelo financeiro (em uma planilha, por exemplo) para projetar o FCFE para os próximos anos (no caso do notebook, até 2028).

Para criar suas projeções, considere:
* **Guidance da Empresa:** O que a própria gestão espera para o futuro (crescimento da carteira de crédito, margens, etc.).
* **Cenário Macroeconômico:** Projeções para a taxa de juros (Selic), inflação (IPCA) e crescimento do PIB, que impactam diretamente o setor bancário.
* **Análise de Tendências:** Estude o crescimento histórico do Lucro Líquido, a rentabilidade (ROE) e a política de dividendos (Payout) da empresa.
* **Definição de Premissas:** Com base na sua análise, defina premissas realistas para o crescimento futuro dos lucros e da taxa de reinvestimento.

#### Passo 5: Estruturação do Arquivo CSV
Após criar suas projeções, organize os dados no formato exato que o script espera:

1.  **Nome do Arquivo:** `Itau IRFS.csv`
2.  **Formato:** CSV (Valores Separados por Vírgula).
3.  **Separador:** Ponto e vírgula (`;`). O script usa `sep=';'`.
4.  **Codificação:** `latin1`. O script usa `encoding='latin1'`.
5.  **Estrutura:**
    * As **colunas** devem ser as datas dos trimestres (`31/12/2022`, `31/03/2023`, etc.).
    * As **linhas** devem ser as métricas financeiras. O script atual está programado para ler o **FCFE** da **quarta linha** do arquivo (`dados.iloc[3]`). Certifique-se de que seus valores projetados de FCFE estejam nesta linha.

---

## Como Executar o Código

1.  **Clone ou baixe** este repositório.
2.  **Instale as bibliotecas necessárias:**
    ```bash
    pip install pandas numpy yfinance
    ```
3.  **Crie e popule** o arquivo `Itau IRFS.csv` seguindo os passos da seção anterior. Ele deve estar no mesmo diretório do notebook.
4.  **Ajuste as Premissas:** Abra o notebook `DCF_ITUB4.ipynb` e navegue até a **"Seção 2: PREMISSAS DO VALUATION"**. Altere as seguintes variáveis com base na sua própria análise:
    * `taxa_livre_risco`: Taxa de juros de um título público brasileiro de longo prazo.
    * `beta`: Beta da ITUB4.
    * `premio_risco_mercado`: Prêmio de risco esperado para o mercado de ações brasileiro.
    * `taxa_crescimento_perpetuo`: Taxa de crescimento sustentável da empresa no longo prazo (geralmente próxima ao crescimento nominal do PIB).
5.  **Execute todas as células** do notebook para ver o resultado do valuation.

---

## Disclaimer

Este projeto é destinado a fins educacionais e de estudo. A análise de valuation apresentada é baseada em um modelo com dados e premissas que podem não refletir a realidade. **Isto não é uma recomendação de compra ou venda de ativos.** Sempre conduza sua própria pesquisa e análise antes de tomar qualquer decisão de investimento.
