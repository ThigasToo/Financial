# 📊 Valuation DCF em JavaScript

Este projeto implementa, em **JavaScript**, o cálculo de **valuation de empresas pelo método de Fluxo de Caixa Descontado (DCF - Discounted Cash Flow)**.  
O código segue as etapas clássicas: cálculo do custo de capital próprio (CAPM), do custo médio ponderado de capital (WACC), do NOPAT, do fluxo de caixa livre para a firma (FCFF) e finalmente do valor da empresa (Enterprise Value).

---

## 🚀 Funcionalidades

1. **CAPM - Custo de Capital Próprio**  
```
Re = Rf + β * (Rm - Rf) + Risco País (opcional)
```

2. **WACC - Custo Médio Ponderado de Capital**  
```
WACC = (E/V) * Re + (D/V) * Rd * (1 - t)
```

3. **NOPAT - Lucro Operacional após Impostos**  
```
NOPAT = EBIT * (1 - t)
```

4. **FCFF - Fluxo de Caixa Livre para a Firma**  
```
FCFF = NOPAT + D&A - CAPEX - ΔWC
```

5. **Valuation por DCF**  
- Projeta os fluxos de caixa futuros  
- Desconta ao valor presente  
- Calcula o valor residual (perpetuidade, modelo de Gordon Growth)  
- Obtém o **Enterprise Value**  

---

## 📂 Estrutura do Código

- `calcCAPM()` → Calcula o custo de capital próprio.  
- `calcWACC()` → Calcula o custo médio ponderado de capital.  
- `calcNOPAT()` → Calcula o NOPAT.  
- `calcFCFF()` → Calcula o fluxo de caixa livre para a firma.  
- `calcDCFValuation()` → Realiza o valuation via DCF, retornando os fluxos projetados, valores presentes, valor residual e o Enterprise Value.  
- `exemplo()` → Executa um caso prático com dados da **Vale S.A. (2024)**.

---

## 📊 Premissas do Exemplo (Vale S.A. - 2024)
- Taxa livre de risco (Rf): 15%
- Beta: 1,04
- Prêmio de risco de mercado (Rm - Rf): -3%
- Risco país: 2%
- Dívida: R$ 11,18 bi
- Patrimônio líquido: R$ 34,52 bi
- Custo da dívida (Rd): 9%
- Alíquota de imposto: 27%
- EBIT: R$ 15,4 bi
- Depreciação e Amortização: R$ 3,06 bi
- CAPEX: R$ 6,1 bi
- Δ Capital de Giro: R$ 3,65 bi
- Crescimento explícito: 4%
- Crescimento na perpetuidade (g): 4%
- Horizonte de projeção: 3 anos

Exemplo de saída: 

<img width="638" height="281" alt="Captura de tela 2025-09-18 142601" src="https://github.com/user-attachments/assets/981a7121-d879-49b4-9a87-7965584dd6d1" />

## 📌 Observações
- O exemplo utiliza valores da Vale S.A. (2024) apenas para fins educacionais.
- O código pode ser adaptado para qualquer empresa, bastando alterar as premissas de entrada.
- Não substitui análises financeiras profissionais.
