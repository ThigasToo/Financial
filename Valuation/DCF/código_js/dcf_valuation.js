/*******************************
 * Valuation DCF em JavaScript *
 *******************************/

/**
 * 1. CAPM - Custo de Capital Próprio
 * re = rf + beta * (rm - rf) + riscoPais (opcional)
 */
function calcCAPM(rf, beta, marketRiskPremium, countryRisk = 0) {
  return rf + beta * marketRiskPremium + countryRisk;
}

/**
 * 2. WACC - Custo Médio Ponderado de Capital
 * WACC = (E/V)*re + (D/V)*rd*(1 - t)
 */
function calcWACC(equityValue, debtValue, re, rd, taxRate) {
  const V = equityValue + debtValue;
  const We = equityValue / V;
  const Wd = debtValue / V;
  return We * re + Wd * rd * (1 - taxRate);
}

/**
 * 3. NOPAT - Lucro Operacional após Impostos
 * NOPAT = EBIT * (1 - taxRate)
 */
function calcNOPAT(EBIT, taxRate) {
  return EBIT * (1 - taxRate);
}

/**
 * 4. FCFF - Fluxo de Caixa Livre para a Firma
 * FCFF = NOPAT + D&A - CAPEX - ΔWC
 */
function calcFCFF(NOPAT, depreciation, capex, deltaWC) {
  return NOPAT + depreciation - capex - deltaWC;
}

/**
 * 5. Valuation por DCF
 * - Projeta os fluxos
 * - Calcula o valor presente
 * - Soma com o valor residual (perpetuidade)
 */
function calcDCFValuation(FCFF0, growthRate, WACC, g, years) {
  let FCFFs = [];
  let PVs = [];
  let PVsum = 0;

  // projeção e desconto dos fluxos explícitos
  for (let t = 1; t <= years; t++) {
    let FCFFt = FCFF0 * Math.pow(1 + growthRate, t);
    let PVt = FCFFt / Math.pow(1 + WACC, t);
    FCFFs.push(FCFFt);
    PVs.push(PVt);
    PVsum += PVt;
  }

  // cálculo do valor residual (Gordon Growth)
  let FCFFn1 = FCFFs[years - 1] * (1 + g);
  let Vresidual = FCFFn1 / (WACC - g);
  let PVresidual = Vresidual / Math.pow(1 + WACC, years);

  let enterpriseValue = PVsum + PVresidual;

  return {
    FCFFs,
    PVs,
    PVsum,
    Vresidual,
    PVresidual,
    enterpriseValue
  };
}

/************************************
 * Exemplo com dados Vale S.A. - 2024*
 ************************************/
(function exemplo() {
  // Premissas de entrada
  const rf = 0.15; // taxa livre de risco
  const beta = 1.04; // beta da empresa
  const marketRiskPremium = -0.03; // prêmio de risco de mercado
  const countryRisk = 0.02; // risco país
  const debtValue = 11181000000; // valor da dívida
  const equityValue = 34528000000; // valor do patrimônio líquido
  const rd = 0.09; // custo da dívida 
  const taxRate = 0.27; // alíquota de imposto
  const EBIT = 15400000000; // lucro antes de juros e impostos
  const depreciation = 3057000000; // depreciação e amortização
  const capex = 6100000000; // despesas de capital
  const deltaWC = 3654000000; // variação no capital de giro
  const growthRate = 0.04; // crescimento explícito
  const g = 0.04; // perpetuidade
  const years = 3; // anos de projeção

  // 1. CAPM
  const re = calcCAPM(rf, beta, marketRiskPremium, countryRisk);
  console.log("Custo de Capital Próprio (Re):", (re * 100).toFixed(2), "%");

  // 2. WACC
  const WACC = calcWACC(equityValue, debtValue, re, rd, taxRate);
  console.log("WACC:", (WACC * 100).toFixed(2), "%");

  // 3. NOPAT
  const NOPAT = calcNOPAT(EBIT, taxRate);
  console.log("NOPAT:", NOPAT.toFixed(2));

  // 4. FCFF
  const FCFF0 = calcFCFF(NOPAT, depreciation, capex, deltaWC);
  console.log("FCFF Ano 0:", FCFF0.toFixed(2));

  // 5. DCF Valuation
  const valuation = calcDCFValuation(FCFF0, growthRate, WACC, g, years);
  console.log("Enterprise Value:", valuation.enterpriseValue.toFixed(2));
  console.log("Detalhes:", valuation);
})();
