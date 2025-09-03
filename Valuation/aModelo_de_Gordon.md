# Valuation da ITSA4 com Modelo de Gordon (DDM)

Este repositório contém um script em Python para calcular o valor intrínseco da ação **ITSA4 (Itaúsa S.A.)** utilizando o **Modelo de Crescimento de Gordon**, também conhecido como Modelo de Desconto de Dividendos (MDD) com crescimento constante.

O objetivo deste projeto é puramente educacional, servindo como um estudo prático de um dos modelos clássicos de valuation de empresas.

## 🚀 Como Funciona o Código?

O script `itsa4.py` automatiza o cálculo do valor justo de uma ação seguindo 4 passos principais:

1.  **Coleta de Dados:** Utiliza bibliotecas Python para buscar dados financeiros em tempo real:
    * `yfinance`: Coleta informações da ação no Yahoo Finance, como o Beta (medida de risco), ROE (Retorno sobre o Patrimônio Líquido) e a política de Payout (percentual do lucro distribuído como dividendos).
    * `ipeadatapy`: Busca a taxa de juros de longo prazo (Swap DI 360) diretamente da base de dados do IPEA, usada como aproximação para a Taxa Livre de Risco (`Rf`).

2.  **Cálculo da Taxa de Crescimento (g):** Estima a taxa de crescimento sustentável dos dividendos através da fórmula:
    `g = ROE * (1 - Payout Ratio)`
    Esta taxa representa o quanto a empresa pode crescer usando apenas os lucros que ela reinveste na própria operação.

3.  **Cálculo do Custo do Capital (k):** Calcula a taxa de retorno mínima exigida pelos investidores usando o modelo **CAPM (Capital Asset Pricing Model)**:
    `k = Rf + β * (Rm - Rf)`
    Onde `Rf` é a taxa livre de risco, `β` é o beta da ação e `(Rm - Rf)` é o prêmio de risco do mercado.

4.  **Cálculo do Valor Justo (V₀):** Com as variáveis `k` e `g` definidas, o script projeta o dividendo do próximo ano (`D1`) com base na média histórica e, finalmente, aplica a fórmula do Modelo de Gordon para encontrar o valor presente da ação.

## O Modelo de Valuation Utilizado: Modelo de Crescimento de Gordon

O coração deste projeto é o Modelo de Crescimento de Gordon. Ele determina o valor justo de uma ação hoje (`V0`) como o valor presente de todos os seus dividendos futuros, assumindo que eles crescerão a uma taxa constante para sempre.

A fórmula central é:

$$V_0 = \frac{D_1}{k - g}$$

Onde:
* `V0` = Valor justo da ação hoje.
* `D1` = Dividendo esperado por ação no próximo ano.
* `k` = Custo do capital (taxa de retorno exigida pelo investidor).
* `g` = Taxa de crescimento constante e perpétua dos dividendos.

## Principais Fragilidades e a Causa das Discrepâncias

É muito comum que o resultado obtido por este modelo seja significativamente diferente do preço da ação negociado na bolsa de valores. Isso **não significa que o mercado está errado**, mas sim que o modelo possui limitações e fragilidades importantes:

1.  **A Grande Sensibilidade às Premissas (`k` e `g`):** O modelo é extremamente sensível a pequenas alterações nas taxas de custo de capital (`k`) e crescimento (`g`). Como o denominador da fórmula é a diferença `(k - g)`, uma mudança de 0,5% em qualquer uma dessas variáveis pode causar uma variação de 20%, 30% ou mais no preço final.

2.  **A Premissa de Crescimento Perpétuo e Constante:** A suposição de que uma empresa crescerá a uma taxa única e constante para sempre é a maior fragilidade teórica do modelo. Na realidade, as empresas passam por ciclos: fases de alto crescimento, maturidade e, eventualmente, declínio.

3.  **Subjetividade na Definição dos Inputs:** Várias entradas do modelo são baseadas em estimativas subjetivas:
    * **Prêmio de Risco de Mercado:** O retorno esperado do mercado (`Rm`) é uma estimativa. O script usa um valor fixo, mas diferentes analistas usarão diferentes valores, alterando drasticamente o custo do capital `k`.
    * **Projeção de Dividendos (`D1`):** O script usa a média de dividendos passados para prever o futuro. Essa é uma abordagem simplista que ignora mudanças na política da empresa ou na sua lucratividade futura.

4.  **O Modelo Ignora Fatores Não Quantificáveis:** O preço de mercado de uma ação reflete uma gama muito maior de informações, incluindo sentimento do mercado, notícias macroeconômicas, qualidade da gestão e vantagens competitivas.

## Como Executar o Código

- Pré-requisitos:

Python 3.x instalado.

- Instale as bibliotecas necessárias
```bash
pip install yfinance ipeadatapy pandas matplotlib
```

- Execute o código:
```bash
python modelo_de_gordon.py
````

## ⚖️ Aviso Legal
Este projeto foi desenvolvido para fins estritamente educacionais e de estudo. As informações e os resultados gerados pelo script não constituem recomendação de compra, venda ou manutenção de qualquer ativo financeiro. Realize sempre sua própria análise ou consulte um profissional de investimentos certificado antes de tomar qualquer decisão financeira.
