# Valuation da ITSA4 com Modelo de Múltiplos Estágios (DDM Avançado)

Este repositório contém uma versão **avançada** do script de valuation para a ação **ITSA4 (Itaúsa S.A.)**. O projeto evoluiu do simples Modelo de Gordon para um **Modelo de Desconto de Dividendos de 2 Estágios**, que oferece uma análise mais detalhada e realista.

O objetivo continua sendo educacional: demonstrar a aplicação prática de modelos de valuation, mostrando como a adição de complexidade pode gerar resultados mais robustos.

## 🚀 Por que esta versão é melhor?

A principal melhoria deste script é a substituição de premissas excessivamente simplistas por cálculos mais dinâmicos e uma estrutura de modelo que reflete melhor o ciclo de vida de uma empresa.

| Característica | Versão Anterior (Gordon Simples) | **Versão Atualizada (2 Estágios)** |
| :--- | :--- | :--- |
| **Modelo de Crescimento** | Crescimento **único e perpétuo**. Assumia que a empresa cresceria à mesma taxa para sempre. | **Dois estágios** (alto crescimento + perpétuo). Mais realista, modela um período de expansão seguido por uma fase de maturidade. |
| **Cálculo do Risco (Beta)** | Beta **estático**, pego pronto do Yahoo Finance. | Beta **dinâmico**, calculado com base em 5 anos de dados históricos da ITSA4 vs. Ibovespa. **Mais rigoroso e específico.** |
| **Projeção de Dividendos** | Usava a **média histórica** dos dividendos, olhando apenas para o passado. | Projeta os dividendos a partir do **último dividendo anual**, com foco no crescimento futuro. |
| **Robustez do Código** | Vulnerável a falhas se não encontrasse dados de preço para o dia. | **Código robusto**, que verifica se os dados de mercado foram recebidos antes de executar os cálculos, evitando erros. |

Em resumo, esta versão troca suposições estáticas por cálculos dinâmicos e adota um modelo que se alinha melhor à forma como as empresas realmente operam.

## Como Funciona o Código Atualizado?

O script executa um processo de valuation mais sofisticado, dividido em duas grandes fases:

#### Estágio 1: Período de Alto Crescimento
1.  **Cálculo de Inputs Dinâmicos:** Primeiramente, o script calcula o **Beta** da ação, medindo sua volatilidade em relação ao Ibovespa nos últimos 5 anos.
2.  **Definição das Premissas:** Define-se um período de alto crescimento (ex: 5 anos) e as taxas de crescimento para este período (`g_alto`) e para a perpetuidade (`g_perpetuo`).
3.  **Projeção dos Dividendos:** Para cada ano do período de alto crescimento, o script projeta o dividendo e o **traz a valor presente**, usando o Custo do Capital (`k`) como taxa de desconto.

#### Estágio 2: Período de Crescimento Perpétuo
1.  **Cálculo do Valor Terminal:** Ao final do Estágio 1, o script calcula o **Valor Terminal**, que representa o valor presente de todos os dividendos futuros da empresa a partir daquele ponto, usando a fórmula de Gordon com uma taxa de crescimento perpétua e conservadora.
2.  **Desconto do Valor Terminal:** Este valor futuro também é **trazido a valor presente**.

#### Valor Justo Final
O valor intrínseco final da ação é a **soma do valor presente dos dividendos do Estágio 1 com o valor presente do Valor Terminal**.

## Limitações (Mesmo Nesta Versão Melhorada)

Apesar de ser mais robusto, este modelo ainda possui limitações que justificam discrepâncias em relação ao preço de mercado:

* **Sensibilidade às Premissas:** O resultado final ainda é muito sensível às premissas definidas, como o número de anos no período de alto crescimento, o prêmio de risco de mercado e as taxas de crescimento (`g_alto` e `g_perpetuo`).
* **Subjetividade Persiste:** A escolha desses parâmetros é uma decisão do analista, o que introduz subjetividade no resultado. O modelo é uma ferramenta de análise, não um oráculo.
* **Fatores Qualitativos Ignorados:** O modelo continua sendo puramente quantitativo, ignorando fatores como a qualidade da gestão, governança corporativa, inovações e o cenário competitivo, que são precificados pelo mercado.

## Como Executar o Código

### Pré-requisitos
* Python 3.x instalado.

### Instale as bibliotecas necessárias
```bash
pip install yfinance numpy pandas
```

### Execute o script
```bash
python itsa4_2.py
```

## ⚖️ Aviso Legal
Este projeto foi desenvolvido para fins estritamente educacionais e de estudo. As informações e os resultados gerados pelo script não constituem recomendação de compra, venda ou manutenção de qualquer ativo financeiro. Realize sempre sua própria análise ou consulte um profissional de investimentos certificado antes de tomar qualquer decisão financeira.
