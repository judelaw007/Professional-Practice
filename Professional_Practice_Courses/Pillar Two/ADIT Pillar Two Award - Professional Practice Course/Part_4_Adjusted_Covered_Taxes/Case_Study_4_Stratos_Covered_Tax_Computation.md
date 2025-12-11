# Case Study 4: Stratos's Covered Tax Computation

## Introduction

This case study brings together the concepts from Chapters 4.1 to 4.6. You will compute Adjusted Covered Taxes for Stratos's key jurisdictions, applying tax classification, current and deferred tax adjustments, and tax allocation rules to determine jurisdictional ETRs.

**Important:** Work through each task systematically using the Covered Tax Workpaper. Complete each jurisdiction fully before moving to the next. Do not skip steps.

**Time estimate:** 90-120 minutes

---

## Background: Stratos Group — FY 2025 Covered Tax Computation

Following the GloBE Income calculations in Case Study 3, Stratos Group's tax team must now compute Adjusted Covered Taxes for each jurisdiction to determine jurisdictional ETRs. The CFO has requested a comprehensive analysis for three key jurisdictions: Germany, Singapore, and Ireland.

### Entity Overview

| Entity | Jurisdiction | Statutory Rate | Role |
|--------|--------------|----------------|------|
| Stratos Holdings plc | UK | 25% | Ultimate Parent Entity |
| SG Germany GmbH | Germany | 30% | Operating subsidiary |
| SG Singapore Pte Ltd | Singapore | 17% | IP holding company |
| SG Ireland Ltd | Ireland | 12.5% | European HQ |

### Ownership Structure

```
Stratos Holdings plc (UK)
    │
    ├── SG Germany GmbH (Germany) — 100%
    │       │
    │       └── SG France SAS (France) — 100%
    │
    ├── SG Singapore Pte Ltd (Singapore) — 100%
    │
    └── SG Ireland Ltd (Ireland) — 100%
```

---

## Data Package

### Tax Data: SG Germany GmbH

**Current Tax Expense (from P&L)**

| Line Item | Amount (€) | Notes |
|-----------|------------|-------|
| Corporate income tax (Körperschaftsteuer) | 8,200,000 | 15% federal CIT |
| Solidarity surcharge | 451,000 | 5.5% of CIT |
| Trade tax (Gewerbesteuer) | 3,100,000 | ~14% effective |
| **Subtotal Current Tax (P&L)** | **11,751,000** | |

**Taxes Outside P&L**

| Line Item | Amount (€) | Location |
|-----------|------------|----------|
| Tax on pension actuarial adjustment | 45,000 | OCI |
| Tax on hedging reserve movement | 22,000 | OCI |

**Tax Credits**

| Credit Type | Amount (€) | Refundable? | Within 4 Years? |
|-------------|------------|-------------|-----------------|
| R&D tax credit (Forschungszulage) | 180,000 | Yes | Yes |

**Non-Income Taxes (for classification)**

| Tax Type | Amount (€) | Classification |
|----------|------------|----------------|
| VAT (net payable) | 2,400,000 | ? |
| Wage tax (employer) | 890,000 | ? |
| Real property tax | 125,000 | ? |

**Deferred Tax Expense**

| Item | Movement (€) | Rate | Nature |
|------|--------------|------|--------|
| DTL on intangibles (IP amortisation) | +900,000 | 30% | Non-REA |
| DTL on PP&E (accelerated depreciation) | +400,000 | 30% | REA |
| DTA on provisions (accrued expenses) | -250,000 | 30% | |
| Valuation allowance release | -150,000 | — | On Irish sub DTA |
| Rate change impact | +80,000 | — | Country X rate reduction |
| **Net Deferred Tax Expense** | **+980,000** | | |

**Uncertain Tax Positions**

| UTP Item | Amount (€) | Status |
|----------|------------|--------|
| Transfer pricing reserve (current year) | 280,000 | Not yet resolved |
| Prior year UTP (settled and paid in FY 2025) | 150,000 | Paid |

**Excluded Income**

| Item | Amount (€) | Tax Impact |
|------|------------|------------|
| Dividend from SG France SAS (100% sub) | 3,100,000 | WHT: €0 (EU exemption) |

**GloBE Income (from Case Study 3):** €53,700,000

---

### Tax Data: SG Singapore Pte Ltd

**Current Tax Expense**

| Line Item | Amount (€) | Notes |
|-----------|------------|-------|
| Singapore corporate tax | 680,000 | 17% rate |
| Foreign tax credits utilised | (530,000) | On royalty income |
| **Net Current Tax** | **150,000** | |

**CFC Tax Exposure (in UK parent accounts)**

| Item | Amount (€) | Income Type |
|------|------------|-------------|
| UK CFC charge on Singapore passive income | 320,000 | IP royalties |
| Singapore passive income under UK CFC | 1,800,000 | |

**Deferred Tax**

| Item | Movement (€) | Rate |
|------|--------------|------|
| DTL on IP capitalisation | +85,000 | 17% |
| DTA on tax losses | -40,000 | 17% |
| **Net Deferred Tax** | **+45,000** | |

**GloBE Income (from Case Study 3):** €4,000,000

---

### Tax Data: SG Ireland Ltd

**Current Tax Expense**

| Line Item | Amount (€) | Notes |
|-----------|------------|-------|
| Irish corporation tax | 1,875,000 | 12.5% rate |
| R&D tax credit | (225,000) | Knowledge Development Box |

**Dividend to UK Parent**

| Item | Amount (€) |
|------|------------|
| Dividend paid to Stratos Holdings plc | 500,000 |
| Irish dividend WHT | 0 | EU Parent-Sub exemption |
| UK WHT on receipt | 0 | Treaty exemption |

**Deferred Tax**

| Item | Movement (€) | Rate |
|------|--------------|------|
| DTL on R&D assets | +120,000 | 12.5% |
| **Net Deferred Tax** | **+120,000** | |

**GloBE Income (from Case Study 3):** €15,000,000

---

## Task 1: Covered Tax Classification—Germany

### Your Task

Classify each tax line item as Covered Tax or Non-Covered Tax using the Article 4.2.1 framework. For the R&D credit, apply the QRTC test from Article 10.1.

### Expected Deliverable

**Classification Workpaper**

| # | Tax Item | Amount (€) | Category Test | Result |
|---|----------|------------|---------------|--------|
| 1 | Corporate income tax | 8,200,000 | | |
| 2 | Solidarity surcharge | 451,000 | | |
| 3 | Trade tax (Gewerbesteuer) | 3,100,000 | | |
| 4 | VAT | 2,400,000 | | |
| 5 | Wage tax (employer) | 890,000 | | |
| 6 | Real property tax | 125,000 | | |
| 7 | R&D credit | (180,000) | | |

**QRTC Verification (R&D Credit)**

| Question | Answer | Reference |
|----------|--------|-----------|
| Is the credit refundable as cash? | | |
| Is refund available within 4 years? | | |
| Can it settle non-tax liabilities? | | |
| Is refund limited to tax liability? | | |

**Conclusion:** _______________________________________________

**Classification Summary**

| Category | Items | Total (€) |
|----------|-------|-----------|
| **Covered Taxes (P&L)** | | |
| **Non-Covered Taxes** | | |
| **QRTC (reclassify to income)** | | |

---

## Task 2: Current Tax Adjustments—Germany

### Your Task

Apply Article 4.1.2 additions and Article 4.1.3 subtractions to the current tax starting point. Remember to consider the QRTC treatment and UTP adjustments.

### Expected Deliverable

**Starting Point**

```
Current tax expense (P&L):              €_______________
```

**Additions (Article 4.1.2)**

| # | Item | Article | Amount (€) | Calculation |
|---|------|---------|------------|-------------|
| 1 | Tax in OCI (pension) | 4.1.2(a) | | |
| 2 | Tax in OCI (hedging) | 4.1.2(a) | | |
| 3 | Prior year UTP paid | 4.1.2(c) | | |
| 4 | QRTC reversal | 4.1.2(d) | | |
| | **Total Additions** | | | |

**Subtractions (Article 4.1.3)**

| # | Item | Article | Amount (€) | Calculation |
|---|------|---------|------------|-------------|
| 1 | Tax on excluded dividend | 4.1.3(a) | | |
| 2 | Current year UTP | 4.1.3(d) | | |
| | **Total Subtractions** | | | |

**Adjusted Current Tax**

```
Current tax expense (P&L):              €_______________
Additions:                              €_______________
Subtractions:                           €_______________
                                        ───────────────
Adjusted Current Tax:                   €_______________
```

**Corresponding GloBE Income Adjustment (if QRTC applies)**

```
GloBE Income (from Case Study 3):       €_______________
Add: QRTC (Article 3.2.4):              €_______________
                                        ───────────────
Adjusted GloBE Income:                  €_______________
```

---

## Task 3: Deferred Tax Adjustments—Germany

### Your Task

Calculate the Total Deferred Tax Adjustment Amount (DTAA) by:
1. Applying the 15% rate cap (Germany's rate exceeds 15%)
2. Excluding valuation allowance movements (Article 4.4.1(c))
3. Excluding rate change impacts (Article 4.4.1(d))
4. Identifying REA vs non-REA items for tracking

### Expected Deliverable

**Starting Point**

```
Deferred tax expense (P&L):             €_______________
```

**Step 1: Apply 15% Rate Cap**

| Item | Original (30%) | Recast (15%) | Adjustment |
|------|----------------|--------------|------------|
| DTL intangibles | | | |
| DTL PP&E | | | |
| DTA provisions | | | |
| **Rate cap adjustment** | | | |

**Step 2: Items to Exclude (Article 4.4.1)**

| Item | Amount | Article | Treatment |
|------|--------|---------|-----------|
| Valuation allowance release | | 4.4.1(c) | |
| Rate change impact | | 4.4.1(d) | |

**Step 3: DTAA Calculation**

| Item | Amount (€) |
|------|------------|
| Items included at 15% cap | |
| Less: Items excluded | |
| **Total DTAA** | |

**Step 4: REA Classification for DTL Tracking**

| DTL | Amount (at 15%) | REA? | 5-Year Tracking Required? |
|-----|-----------------|------|---------------------------|
| | | | |
| | | | |

---

## Task 4: Tax Allocation—Germany

### Your Task

Determine whether any tax allocation adjustments are required for Germany under Article 4.3. Consider:
- CFC tax push-down from UK parent
- WHT allocation on dividends received

### Expected Deliverable

**CFC Tax Push-Down Analysis**

| Question | Answer |
|----------|--------|
| Does UK have CFC charge on German income? | |
| Is Germany a low-tax jurisdiction? | |
| CFC tax push-down to Germany | €_______________ |

**WHT Allocation Analysis**

| Question | Answer |
|----------|--------|
| Was WHT paid on dividend from SG France? | |
| WHT reallocation amount | €_______________ |

**Allocation Summary—Germany**

```
Total tax allocation adjustments:       €_______________
```

---

## Task 5: Total Adjusted Covered Taxes—Germany

### Your Task

Combine your results from Tasks 2-4 to calculate Total Adjusted Covered Taxes and the ETR for Germany.

### Expected Deliverable

**Final Calculation**

| Component | Reference | Amount (€) |
|-----------|-----------|------------|
| Adjusted Current Tax | Task 2 | |
| Deferred Tax Adjustment (DTAA) | Task 3 | |
| Tax Allocations | Task 4 | |
| **Total Adjusted Covered Taxes** | | |

**ETR Calculation**

```
GloBE Income (adjusted):                €_______________
Adjusted Covered Taxes:                 €_______________

ETR = _______________ ÷ _______________ = ___________%

Top-Up Tax assessment: _______________________________________________
```

---

## Task 6: Covered Tax Computation—Singapore

### Your Task

Complete the full Covered Tax computation for Singapore, including:
1. Current tax adjustments
2. CFC tax push-down from UK (with passive income limitation)
3. Deferred tax adjustments (15% cap)
4. ETR calculation

### Expected Deliverable

**Current Tax Starting Point**

```
Current tax expense (P&L):              €_______________
```

**CFC Tax Push-Down (Article 4.3.2(c))**

| Step | Calculation | Result |
|------|-------------|--------|
| Step 1: Singapore pre-push ETR | Local tax ÷ GloBE Income | |
| Step 2: Top-Up Tax % | 15% − Pre-push ETR | |
| Step 3: Passive income cap | Passive income × Top-Up Tax % | |
| Step 4: Push-down amount | MIN(CFC tax, Cap) | |

**Adjusted Current Tax**

```
Current tax expense:                    €_______________
CFC tax push-down:                      €_______________
                                        ───────────────
Adjusted Current Tax:                   €_______________
```

**Deferred Tax Adjustments (15% cap applies)**

| Item | At 17% | At 15% | DTAA |
|------|--------|--------|------|
| DTL on IP | | | |
| DTA on losses | | | |
| **Total DTAA** | | | |

**Total Adjusted Covered Taxes—Singapore**

| Component | Amount (€) |
|-----------|------------|
| Adjusted Current Tax | |
| DTAA | |
| **Total Adjusted Covered Taxes** | |

**ETR Calculation—Singapore**

```
GloBE Income:                           €_______________
Adjusted Covered Taxes:                 €_______________

ETR = _______________ ÷ _______________ = ___________%

Top-Up Tax % = 15% − ___________% = ___________%
```

---

## Task 7: Covered Tax Computation—Ireland

### Your Task

Complete the full Covered Tax computation for Ireland, including:
1. Current tax adjustments (analyse whether the R&D credit is a QRTC)
2. WHT allocation analysis
3. Deferred tax adjustments (note: Irish rate 12.5% is below 15%)
4. ETR calculation

### Expected Deliverable

**Current Tax Starting Point**

```
Irish corporation tax:                  €_______________
Less: R&D credit:                       €_______________
Net per accounts:                       €_______________
```

**QRTC Analysis—Irish R&D Credit**

| Question | Answer |
|----------|--------|
| Is the Knowledge Development Box a refundable credit? | |
| **Conclusion: Is this a QRTC?** | |

**Adjusted Current Tax**

```
Adjusted Current Tax:                   €_______________
```

**WHT Allocation (Article 4.3.2(e))**

| Question | Answer |
|----------|--------|
| Was WHT paid on dividend to UK parent? | |
| WHT allocation from UK to Ireland | €_______________ |

**Deferred Tax Adjustments**

| Item | At 12.5% | At 15% | Treatment |
|------|----------|--------|-----------|
| DTL on R&D assets | | | Rate < 15%, no change |

```
DTAA:                                   €_______________
```

**Total Adjusted Covered Taxes—Ireland**

| Component | Amount (€) |
|-----------|------------|
| Adjusted Current Tax | |
| DTAA | |
| **Total Adjusted Covered Taxes** | |

**ETR Calculation—Ireland**

```
GloBE Income:                           €_______________
Adjusted Covered Taxes:                 €_______________

ETR = _______________ ÷ _______________ = ___________%

Top-Up Tax % = 15% − ___________% = ___________%
```

---

## Task 8: Consolidated Summary and UK Parent Position

### Your Task

Prepare a consolidated summary of all jurisdictions and show the UK parent position after tax allocations.

### Expected Deliverable

**Jurisdiction Summary Table**

| Jurisdiction | GloBE Income (€) | Adj. Covered Taxes (€) | ETR | Top-Up Tax Exposure |
|--------------|------------------|------------------------|-----|---------------------|
| Germany | | | | |
| Singapore | | | | |
| Ireland | | | | |

**UK Parent Position (Post-Allocations)**

| Item | Original (€) | Allocated Out (€) | Remaining (€) |
|------|--------------|-------------------|---------------|
| UK corporate tax | 5,000,000 | — | |
| CFC tax (Singapore) | 320,000 | | |
| WHT on Irish dividend | 0 | — | |
| **UK Covered Taxes** | | | |

**Notes:** _______________________________________________

---

## Model Answers

### Answer 1: Germany Covered Tax Classification

**Classification Workpaper**

| # | Tax Item | Amount (€) | Category Test | Result |
|---|----------|------------|---------------|--------|
| 1 | Corporate income tax | 8,200,000 | Tax on own income? YES | **COVERED** |
| 2 | Solidarity surcharge | 451,000 | Component of CIT? YES | **COVERED** |
| 3 | Trade tax (Gewerbesteuer) | 3,100,000 | Tax on trading profits? YES | **COVERED** |
| 4 | VAT | 2,400,000 | Indirect tax? YES | **NOT COVERED** |
| 5 | Wage tax (employer) | 890,000 | Payroll tax? YES | **NOT COVERED** |
| 6 | Real property tax | 125,000 | Property tax? YES | **NOT COVERED** |
| 7 | R&D credit | (180,000) | QRTC test—see below | **Special treatment** |

**QRTC Verification (R&D Credit)**

| Question | Answer | Reference |
|----------|--------|-----------|
| Is the credit refundable as cash? | **Yes** | German Forschungszulage is refundable |
| Is refund available within 4 years? | **Yes** | Paid with annual assessment |
| Can it settle non-tax liabilities? | **Yes** | Cash payment |
| Is refund limited to tax liability? | **No** | Paid regardless of tax position |

**Conclusion:** R&D credit qualifies as QRTC → Treat as **income**, not reduction of Covered Taxes

**Classification Summary**

| Category | Items | Total (€) |
|----------|-------|-----------|
| **Covered Taxes (P&L)** | CIT + Solidarity + Trade Tax | 11,751,000 |
| **Non-Covered Taxes** | VAT, Wage tax, Property tax | 3,415,000 |
| **QRTC (reclassify to income)** | R&D credit | 180,000 |

---

### Answer 2: Germany Current Tax Adjustments

**Starting Point**

```
Current tax expense (P&L):              €11,751,000
```

**Additions (Article 4.1.2)**

| # | Item | Article | Amount (€) | Calculation |
|---|------|---------|------------|-------------|
| 1 | Tax in OCI (pension) | 4.1.2(a) | +45,000 | Direct from data |
| 2 | Tax in OCI (hedging) | 4.1.2(a) | +22,000 | Direct from data |
| 3 | Prior year UTP paid | 4.1.2(c) | +150,000 | Settled in FY 2025 |
| 4 | QRTC reversal | 4.1.2(d) | +180,000 | R&D credit add-back |
| | **Total Additions** | | **+397,000** | |

**Subtractions (Article 4.1.3)**

| # | Item | Article | Amount (€) | Calculation |
|---|------|---------|------------|-------------|
| 1 | Tax on excluded dividend | 4.1.3(a) | -0 | No German tax on EU dividend |
| 2 | Current year UTP | 4.1.3(d) | -280,000 | TP reserve not resolved |
| | **Total Subtractions** | | **-280,000** | |

**Adjusted Current Tax**

```
Current tax expense (P&L):              €11,751,000
Additions:                              +€397,000
Subtractions:                           -€280,000
                                        ───────────
Adjusted Current Tax:                   €11,868,000
```

**Corresponding GloBE Income Adjustment**

```
GloBE Income (from Case Study 3):       €53,700,000
Add: QRTC (Article 3.2.4):             +€180,000
                                        ───────────
Adjusted GloBE Income:                  €53,880,000
```

---

### Answer 3: Germany Deferred Tax Adjustments

**Starting Point**

```
Deferred tax expense (P&L):             €980,000
```

**Step 1: Apply 15% Rate Cap**

German combined rate (30%) exceeds 15%. All deferred tax movements must be recast.

| Item | Original (30%) | Recast (15%) | Adjustment |
|------|----------------|--------------|------------|
| DTL intangibles | €900,000 | €450,000 | -€450,000 |
| DTL PP&E | €400,000 | €200,000 | -€200,000 |
| DTA provisions | (€250,000) | (€125,000) | +€125,000 |
| **Rate cap adjustment** | | | **-€525,000** |

**Step 2: Items to Exclude**

| Item | Amount | Article | Treatment |
|------|--------|---------|-----------|
| Valuation allowance release | €150,000 | 4.4.1(c) | Exclude from DTAA |
| Rate change impact | €80,000 | 4.4.1(d) | Exclude from DTAA |

**Step 3: DTAA Calculation**

Items to include at 15% cap: DTL intangibles (€450,000) + DTL PP&E (€200,000) − DTA provisions (€125,000) = **€525,000**

Excluded items (VA release and rate change) were not included above.

```
Total DTAA:                             €525,000
```

**Step 4: REA Classification**

| DTL | Amount (at 15%) | REA? | 5-Year Tracking Required? |
|-----|-----------------|------|---------------------------|
| Intangibles | €450,000 | No | Yes—monitor 5 years |
| PP&E | €200,000 | Yes (tangible assets) | No |

---

### Answer 4: Germany Tax Allocation

**CFC Tax Push-Down Analysis**

| Question | Answer |
|----------|--------|
| Does UK have CFC charge on German income? | **No** — Germany is high-tax |
| Is Germany a low-tax jurisdiction? | **No** — ~30% rate |
| CFC tax push-down to Germany | **€0** |

**WHT Allocation Analysis**

| Question | Answer |
|----------|--------|
| Was WHT paid on dividend from SG France? | **No** — EU exemption |
| WHT reallocation amount | **€0** |

**Allocation Summary—Germany**

```
Total tax allocation adjustments:       €0
```

---

### Answer 5: Germany Total Adjusted Covered Taxes

**Final Calculation**

| Component | Reference | Amount (€) |
|-----------|-----------|------------|
| Adjusted Current Tax | Task 2 | 11,868,000 |
| Deferred Tax Adjustment (DTAA) | Task 3 | 525,000 |
| Tax Allocations | Task 4 | 0 |
| **Total Adjusted Covered Taxes** | | **12,393,000** |

**ETR Calculation**

```
GloBE Income (adjusted):                €53,880,000
Adjusted Covered Taxes:                 €12,393,000

ETR = €12,393,000 ÷ €53,880,000 = 23.0%

Since 23.0% > 15%: NO TOP-UP TAX for Germany
```

---

### Answer 6: Singapore Covered Tax Computation

**Current Tax Starting Point**

```
Current tax expense (P&L):              €150,000
```

**CFC Tax Push-Down (Article 4.3.2(c))**

UK parent has CFC charge of €320,000 on Singapore passive income (€1,800,000).

**Apply Passive Income Limitation (Article 4.3.3):**

| Step | Calculation | Result |
|------|-------------|--------|
| Step 1: Singapore pre-push ETR | €150,000 ÷ €4,000,000 | **3.75%** |
| Step 2: Top-Up Tax % | 15% − 3.75% | **11.25%** |
| Step 3: Passive income cap | €1,800,000 × 11.25% | **€202,500** |
| Step 4: Push-down amount | MIN(€320,000, €202,500) | **€202,500** |

**Adjusted Current Tax**

```
Current tax expense:                    €150,000
CFC tax push-down:                     +€202,500
                                        ─────────
Adjusted Current Tax:                   €352,500
```

**Deferred Tax Adjustments**

Singapore rate (17%) > 15%, so cap applies:

| Item | At 17% | At 15% | DTAA |
|------|--------|--------|------|
| DTL on IP | €85,000 | €75,000 | €75,000 |
| DTA on losses | (€40,000) | (€35,294) | (€35,294) |
| **Total DTAA** | **€45,000** | | **€39,706** |

*Calculation: Underlying timing differences recast at 15%*

**Total Adjusted Covered Taxes—Singapore**

| Component | Amount (€) |
|-----------|------------|
| Adjusted Current Tax | 352,500 |
| DTAA | 39,706 |
| **Total Adjusted Covered Taxes** | **392,206** |

**ETR Calculation—Singapore**

```
GloBE Income:                           €4,000,000
Adjusted Covered Taxes:                 €392,206

ETR = €392,206 ÷ €4,000,000 = 9.8%

Top-Up Tax % = 15% − 9.8% = 5.2%
```

---

### Answer 7: Ireland Covered Tax Computation

**Current Tax Starting Point**

```
Irish corporation tax:                  €1,875,000
Less: R&D credit:                       (€225,000)
Net per accounts:                       €1,650,000
```

**QRTC Analysis—Irish R&D Credit**

| Question | Answer |
|----------|--------|
| Is the Knowledge Development Box a refundable credit? | **No** — KDB is a reduced tax rate (6.25%), not a refundable credit |
| **Conclusion: Is this a QRTC?** | **No** — remains as reduction to Covered Taxes |

**Adjusted Current Tax**

```
Adjusted Current Tax:                   €1,650,000
```

**WHT Allocation (Article 4.3.2(e))**

| Question | Answer |
|----------|--------|
| Was WHT paid on dividend to UK parent? | **No** — EU Parent-Sub exemption + Treaty |
| WHT allocation from UK to Ireland | **€0** |

**Deferred Tax Adjustments**

| Item | At 12.5% | At 15% | Treatment |
|------|----------|--------|-----------|
| DTL on R&D assets | €120,000 | €120,000 | No change (12.5% < 15%) |

```
DTAA:                                   €120,000
```

*Note: Irish rate (12.5%) is below 15%, so DTLs remain at accounting rate.*

**Total Adjusted Covered Taxes—Ireland**

| Component | Amount (€) |
|-----------|------------|
| Adjusted Current Tax | 1,650,000 |
| DTAA | 120,000 |
| **Total Adjusted Covered Taxes** | **1,770,000** |

**ETR Calculation—Ireland**

```
GloBE Income:                           €15,000,000
Adjusted Covered Taxes:                 €1,770,000

ETR = €1,770,000 ÷ €15,000,000 = 11.8%

Top-Up Tax % = 15% − 11.8% = 3.2%
```

---

### Answer 8: Consolidated Summary

**Jurisdiction Summary Table**

| Jurisdiction | GloBE Income (€) | Adj. Covered Taxes (€) | ETR | Top-Up Tax Exposure |
|--------------|------------------|------------------------|-----|---------------------|
| Germany | 53,880,000 | 12,393,000 | 23.0% | None |
| Singapore | 4,000,000 | 392,206 | 9.8% | Yes (5.2%) |
| Ireland | 15,000,000 | 1,770,000 | 11.8% | Yes (3.2%) |

**UK Parent Position (Post-Allocations)**

| Item | Original (€) | Allocated Out (€) | Remaining (€) |
|------|--------------|-------------------|---------------|
| UK corporate tax | 5,000,000 | — | 5,000,000 |
| CFC tax (Singapore) | 320,000 | (202,500) | 117,500 |
| WHT on Irish dividend | 0 | — | 0 |
| **UK Covered Taxes** | **5,320,000** | **(202,500)** | **5,117,500** |

**Note:** €117,500 of CFC tax remains in UK (passive income limitation applied)

---

## Covered Tax Workpaper Template

Use this template for each jurisdiction:

```
COVERED TAX COMPUTATION WORKPAPER
Entity: _________________________
Jurisdiction: ___________________
Fiscal Year: ____________________

SECTION A: CURRENT TAX
A1  Current tax expense (P&L)                    ____________
A2  Add: Tax in OCI/Equity (Art. 4.1.2(a))      ____________
A3  Add: Prior year UTP paid (Art. 4.1.2(c))    ____________
A4  Add: QRTC reversal (Art. 4.1.2(d))          ____________
A5  Less: Tax on excluded income (Art. 4.1.3(a)) ____________
A6  Less: Current year UTP (Art. 4.1.3(d))      ____________
A7  ADJUSTED CURRENT TAX                         ============

SECTION B: DEFERRED TAX (DTAA)
B1  DT expense per P&L                           ____________
B2  Rate cap adjustment (if rate > 15%)          ____________
B3  Exclude: Valuation allowance (Art. 4.4.1(c)) ____________
B4  Exclude: Rate change (Art. 4.4.1(d))        ____________
B5  Exclude: Tax credits (Art. 4.4.1(e))        ____________
B6  TOTAL DTAA                                   ============

SECTION C: TAX ALLOCATIONS
C1  CFC tax push-down received                   ____________
C2  WHT allocated to this entity                 ____________
C3  PE tax allocated                             ____________
C4  TOTAL ALLOCATIONS                            ============

SECTION D: TOTAL ADJUSTED COVERED TAXES
D1  Adjusted Current Tax (A7)                    ____________
D2  DTAA (B6)                                    ____________
D3  Tax Allocations (C4)                         ____________
D4  TOTAL ADJUSTED COVERED TAXES                 ============

SECTION E: ETR CALCULATION
E1  GloBE Income                                 ____________
E2  Adjusted Covered Taxes (D4)                  ____________
E3  ETR (E2 ÷ E1)                               ____________
E4  Top-Up Tax % (15% - E3, if positive)        ____________
```

---

## Learning Points

### Point 1: QRTC Dual Adjustment

The German R&D credit is a QRTC and requires adjustments to BOTH:
- **Covered Taxes:** Add back €180,000 (reverse accounting treatment)
- **GloBE Income:** Add €180,000 (treat as income)

Forgetting either adjustment distorts the ETR calculation.

### Point 2: Passive Income Limitation Prevents Full Push-Down

The UK CFC charge of €320,000 on Singapore could only be pushed down to the extent of €202,500 due to the passive income limitation. The remaining €117,500 stays in UK Covered Taxes.

Without this limitation, Singapore's ETR would be:
- (€150,000 + €320,000) ÷ €4,000,000 = 11.75%

With limitation:
- (€150,000 + €202,500) ÷ €4,000,000 = 8.8%

The limitation ensures the CFC push-down doesn't artificially eliminate Singapore's Top-Up Tax exposure.

### Point 3: Rate Cap Creates Significant Adjustment

Germany's 30% rate means all deferred tax movements are recast at 15%—halving their GloBE impact. The €525,000 rate cap adjustment represents a material reduction from the €1,050,000 that would have been included at accounting rates.

### Point 4: Irish KDB Is Not a QRTC

Unlike Germany's R&D credit, Ireland's Knowledge Development Box is a reduced tax rate (6.25% on qualifying IP income), not a refundable credit. It therefore reduces Covered Taxes directly rather than being treated as income.

### Point 5: Document Classification Decisions

Each tax item requires explicit classification with reference to Article 4.2.1. The classification workpaper provides audit defence and ensures consistency across fiscal years.

---

## Alternative Scenario: What If CFC Push-Down Were Unlimited?

For additional practice, consider this alternative scenario:

**Assume:** The passive income limitation under Article 4.3.3 did not exist.

**Questions:**
1. What would be Singapore's Adjusted Covered Taxes?
2. What would be Singapore's ETR?
3. What would be the impact on UK parent's Covered Taxes?

**Analysis:**

Without passive income limitation:

```
Singapore Adjusted Current Tax:
  Local tax:                €150,000
  Full CFC push-down:      +€320,000
  Total:                    €470,000

Singapore DTAA:             €39,706

Singapore Total Covered Taxes: €509,706

Singapore ETR:
  €509,706 ÷ €4,000,000 = 12.7%

Top-Up Tax % = 15% − 12.7% = 2.3%
```

**Impact comparison:**

| Scenario | Singapore ETR | Singapore Top-Up Tax % | UK CFC Tax Remaining |
|----------|---------------|------------------------|----------------------|
| With limitation | 9.8% | 5.2% | €117,500 |
| Without limitation | 12.7% | 2.3% | €0 |

**Key insight:** The passive income limitation preserves approximately 2.9% additional Top-Up Tax exposure in Singapore, preventing a high-tax parent from sheltering a low-tax subsidiary's income through CFC taxes.

---

## Integration with GIR Filing

The Adjusted Covered Taxes calculated in this case study feed directly into **GIR-001 GloBE Calculator**:

| GIR-001 Input | Data From This Case Study |
|---------------|--------------------------|
| Jurisdiction | Germany / Singapore / Ireland |
| GloBE Income | From Case Study 3 (adjusted for QRTC) |
| Adjusted Covered Taxes | €12,393,000 / €392,206 / €1,770,000 |

**Tool Workflow:**

1. Enter GloBE Income and Adjusted Covered Taxes into **GIR-001 GloBE Calculator**
2. GIR-001 Step 1 calculates the ETR automatically
3. GIR-001 Step 2 calculates SBIE (Substance-Based Income Exclusion)
4. GIR-001 Step 3 calculates Top-Up Tax

Use **GIR-001 GloBE Calculator** at tools.mojitax.com to verify your calculations and practice the complete ETR → SBIE → Top-Up Tax workflow.

---

## Key References

**OECD GloBE Model Rules:**
- Article 4.1.1 — Current tax starting point
- Article 4.1.2 — Additions to Covered Taxes
- Article 4.1.3 — Subtractions from Covered Taxes
- Article 4.2.1 — Covered Tax definition (four categories)
- Article 4.3.2(c) — CFC tax push-down
- Article 4.3.3 — Passive income limitation
- Article 4.4.1 — DTAA and 15% rate cap
- Article 4.4.1(c) — Valuation allowance exclusion
- Article 4.4.1(d) — Rate change exclusion
- Article 3.2.4 — QRTC treatment as income
- Article 10.1 — QRTC definition

**Administrative Guidance:**
- February 2023: CFC push-down allocation rules
- July 2023: Passive income limitation clarification
- December 2023: QRTC verification guidance

**OECD Commentary:**
- Chapter 4, paragraphs 1-68 — Covered Tax computation guidance

---

## Next Step

You have completed Part 4: Adjusted Covered Taxes. With GloBE Income (Part 3) and Adjusted Covered Taxes (Part 4) calculated, you now have both components needed for the ETR calculation. Proceed to **Part 5: Top-Up Tax Calculation** to learn how to compute SBIE, the Top-Up Tax Percentage, and allocate Top-Up Tax under the IIR and UTPR charging mechanisms.
