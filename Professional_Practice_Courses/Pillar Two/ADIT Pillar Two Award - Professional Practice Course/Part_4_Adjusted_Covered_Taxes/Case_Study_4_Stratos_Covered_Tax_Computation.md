# Case Study 4: Stratos's Covered Tax Computation

## Scenario Context

Following the GloBE Income calculations in Case Study 3, Stratos Group's tax team must now compute Adjusted Covered Taxes for each jurisdiction to determine jurisdictional ETRs. This case study focuses on the complete Covered Tax workpaper for three key jurisdictions: Germany, Singapore, and Ireland.

The CFO has requested a comprehensive analysis covering:
1. Classification of all tax items as Covered or Non-Covered
2. Current tax expense adjustments
3. Deferred tax adjustments (including 15% rate cap)
4. Tax allocation between entities (CFC push-down, WHT allocation)
5. Final Adjusted Covered Taxes for ETR calculation

---

## Data Package

### Entity Overview

| Entity | Jurisdiction | Tax Rate | Role |
|--------|--------------|----------|------|
| Stratos Holdings plc | UK | 25% | Ultimate Parent Entity |
| SG Germany GmbH | Germany | 30% | Operating subsidiary |
| SG Singapore Pte Ltd | Singapore | 17% | IP holding company |
| SG Ireland Ltd | Ireland | 12.5% | European HQ |

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

**GloBE Income (from Case Study 3)**
- GloBE Income: €4,000,000

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

**GloBE Income (from Part 3)**
- GloBE Income: €15,000,000

---

## Task 1: Covered Tax Classification—Germany

**Objective:** Classify each tax line as Covered Tax or Non-Covered Tax using the Article 4.2.1 framework.

### Classification Workpaper

| # | Tax Item | Amount (€) | Category Test | Result |
|---|----------|------------|---------------|--------|
| 1 | Corporate income tax | 8,200,000 | Tax on own income? YES | **COVERED** |
| 2 | Solidarity surcharge | 451,000 | Component of CIT? YES | **COVERED** |
| 3 | Trade tax (Gewerbesteuer) | 3,100,000 | Tax on trading profits? YES | **COVERED** |
| 4 | VAT | 2,400,000 | Indirect tax? YES | **NOT COVERED** |
| 5 | Wage tax (employer) | 890,000 | Payroll tax? YES | **NOT COVERED** |
| 6 | Real property tax | 125,000 | Property tax? YES | **NOT COVERED** |
| 7 | R&D credit | (180,000) | QRTC test—see below | **Special treatment** |

### QRTC Verification: R&D Credit

| Question | Answer | Reference |
|----------|--------|-----------|
| Is the credit refundable as cash? | Yes | German Forschungszulage is refundable |
| Is refund available within 4 years? | Yes | Paid with annual assessment |
| Can it settle non-tax liabilities? | Yes | Cash payment |
| Is refund limited to tax liability? | No | Paid regardless of tax position |

**Conclusion:** R&D credit qualifies as QRTC → Treat as **income**, not reduction of Covered Taxes

### Classification Summary

| Category | Items | Total (€) |
|----------|-------|-----------|
| **Covered Taxes (P&L)** | CIT + Solidarity + Trade Tax | 11,751,000 |
| **Non-Covered Taxes** | VAT, Wage tax, Property tax | 3,415,000 |
| **QRTC (reclassify to income)** | R&D credit | 180,000 |

---

## Task 2: Current Tax Adjustments—Germany

**Objective:** Apply Article 4.1.2 additions and Article 4.1.3 subtractions to the current tax starting point.

### Starting Point

```
Current tax expense (P&L):              €11,751,000
```

### Additions (Article 4.1.2)

| # | Item | Article | Amount (€) | Calculation |
|---|------|---------|------------|-------------|
| 1 | Tax in OCI (pension) | 4.1.2(a) | +45,000 | Direct from data |
| 2 | Tax in OCI (hedging) | 4.1.2(a) | +22,000 | Direct from data |
| 3 | Prior year UTP paid | 4.1.2(c) | +150,000 | Settled in FY 2025 |
| 4 | QRTC reversal | 4.1.2(d) | +180,000 | R&D credit add-back |
| | **Total Additions** | | **+397,000** | |

### Subtractions (Article 4.1.3)

| # | Item | Article | Amount (€) | Calculation |
|---|------|---------|------------|-------------|
| 1 | Tax on excluded dividend | 4.1.3(a) | -0 | No German tax on EU dividend |
| 2 | Current year UTP | 4.1.3(d) | -280,000 | TP reserve not resolved |
| | **Total Subtractions** | | **-280,000** | |

### Adjusted Current Tax

```
Current tax expense (P&L):              €11,751,000
Additions:                              +€397,000
Subtractions:                           -€280,000
                                        ───────────
Adjusted Current Tax:                   €11,868,000
```

### Corresponding GloBE Income Adjustment

The QRTC must also be added to GloBE Income:

```
GloBE Income (from Case Study 3):       €53,700,000
Add: QRTC (Article 3.2.4):             +€180,000
                                        ───────────
Adjusted GloBE Income:                  €53,880,000
```

---

## Task 3: Deferred Tax Adjustments—Germany

**Objective:** Calculate the Total Deferred Tax Adjustment Amount (DTAA) applying the 15% rate cap and exclusions.

### Starting Point

```
Deferred tax expense (P&L):             €980,000
```

### Step 1: Apply 15% Rate Cap

German combined rate (30%) exceeds 15%. All deferred tax movements must be recast.

| Item | At 30% | At 15% | Adjustment |
|------|--------|--------|------------|
| DTL intangibles | €900,000 | €450,000 | -€450,000 |
| DTL PP&E | €400,000 | €200,000 | -€200,000 |
| DTA provisions | (€250,000) | (€125,000) | +€125,000 |
| **Rate cap adjustment** | | | **-€525,000** |

### Step 2: Apply Exclusions (Article 4.4.1)

| Item | Amount | Article | Treatment |
|------|--------|---------|-----------|
| Valuation allowance release | €150,000 | 4.4.1(c) | Exclude |
| Rate change impact | €80,000 | 4.4.1(d) | Exclude |

**Exclusion calculation:**
- VA release was a credit (negative expense): Excluding it means adding back
- Rate change was a debit (positive expense): Excluding it means subtracting

```
Valuation allowance exclusion:          -€150,000 (remove credit)
Rate change exclusion:                  -€80,000 (remove debit)
                                        ───────────
Total exclusions:                       -€230,000
```

Wait—let me reconsider the sign conventions:
- VA release of €150,000 reduced deferred tax expense → Excluding means we ADD it back to DTAA
- Rate change of €80,000 increased deferred tax expense → Excluding means we SUBTRACT it from DTAA

```
Net exclusion impact on DTAA:
  VA release (was -€150K in DT expense, exclude): +€150,000
  Rate change (was +€80K in DT expense, exclude): -€80,000
  Net:                                             +€70,000
```

Actually, let me think about this more carefully:

The P&L deferred tax expense of €980,000 includes:
- DTL intangibles: +€900,000
- DTL PP&E: +€400,000
- DTA provisions: -€250,000
- VA release: -€150,000
- Rate change: +€80,000
- Total: €980,000

For DTAA, we:
1. Recast at 15% cap
2. Exclude VA movements
3. Exclude rate change effects

Let me recalculate from scratch:

**Items to include in DTAA (at 15%):**
| Item | Original (30%) | Recast (15%) |
|------|----------------|--------------|
| DTL intangibles | €900,000 | €450,000 |
| DTL PP&E | €400,000 | €200,000 |
| DTA provisions | (€250,000) | (€125,000) |
| **Subtotal** | **€1,050,000** | **€525,000** |

**Items excluded:**
- VA release: €150,000 → Excluded (not included above)
- Rate change: €80,000 → Excluded (not included above)

**DTAA Calculation:**

```
DTAA = €525,000 (recast items only)
```

### Step 3: REA Classification for DTL Tracking

| DTL | Amount (at 15%) | REA? | Tracking Required? |
|-----|-----------------|------|-------------------|
| Intangibles | €450,000 | No | Yes—monitor 5 years |
| PP&E | €200,000 | Yes (tangible assets) | No |

### DTAA Summary

```
Total Deferred Tax Adjustment Amount:    €525,000
```

---

## Task 4: Tax Allocation—Germany

**Objective:** Apply Article 4.3 allocations for any taxes requiring push-down or reallocation.

### CFC Tax Push-Down from UK

**Data:** UK parent has no CFC charge on German income (Germany is high-tax)

```
CFC tax push-down to Germany:           €0
```

### Withholding Tax Allocation

**Data:** No WHT on dividend received from SG France SAS (EU exemption)

```
WHT reallocation:                       €0
```

### Allocation Summary—Germany

```
No tax allocation adjustments required for Germany
```

---

## Task 5: Total Adjusted Covered Taxes—Germany

### Final Calculation

| Component | Reference | Amount (€) |
|-----------|-----------|------------|
| Adjusted Current Tax | Task 2 | 11,868,000 |
| Deferred Tax Adjustment (DTAA) | Task 3 | 525,000 |
| Tax Allocations | Task 4 | 0 |
| **Total Adjusted Covered Taxes** | | **12,393,000** |

### ETR Calculation

```
GloBE Income (adjusted):                €53,880,000
Adjusted Covered Taxes:                 €12,393,000

ETR = €12,393,000 ÷ €53,880,000 = 23.0%

Since 23.0% > 15%: NO TOP-UP TAX for Germany
```

---

## Task 6: Covered Tax Computation—Singapore

### Current Tax Adjustments

**Starting point:**
```
Current tax expense (P&L):              €150,000
```

**CFC Tax Push-Down (Article 4.3.2(c))**

UK parent has CFC charge of €320,000 on Singapore passive income (€1,800,000).

**Apply Passive Income Limitation (Article 4.3.3):**

```
Step 1: Singapore pre-push ETR
  Local tax: €150,000
  GloBE Income: €4,000,000
  ETR = 3.75%

Step 2: Top-up Tax %
  15% - 3.75% = 11.25%

Step 3: Cap calculation
  €1,800,000 × 11.25% = €202,500

Step 4: Push-down amount
  MIN(€320,000, €202,500) = €202,500
```

**Adjusted Current Tax:**
```
Current tax expense:                    €150,000
CFC tax push-down:                     +€202,500
                                        ─────────
Adjusted Current Tax:                   €352,500
```

### Deferred Tax Adjustments

Singapore rate (17%) > 15%, so cap applies:

| Item | At 17% | At 15% | Adjustment |
|------|--------|--------|------------|
| DTL on IP | €85,000 | €75,000 | -€10,000 |
| DTA on losses | (€40,000) | (€35,294) | +€4,706 |
| **DTAA** | **€45,000** | **€39,706** | |

Actually, let me recalculate properly:

For DTL at 17% of €85,000, the underlying timing difference = €85,000 ÷ 17% = €500,000
Recast at 15%: €500,000 × 15% = €75,000

For DTA at 17% of €40,000, the underlying timing difference = €40,000 ÷ 17% = €235,294
Recast at 15%: €235,294 × 15% = €35,294

```
DTAA = €75,000 - €35,294 = €39,706
```

### Total Adjusted Covered Taxes—Singapore

| Component | Amount (€) |
|-----------|------------|
| Adjusted Current Tax | 352,500 |
| DTAA | 39,706 |
| **Total Adjusted Covered Taxes** | **392,206** |

### ETR Calculation—Singapore

```
GloBE Income:                           €4,000,000
Adjusted Covered Taxes:                 €392,206

ETR = €392,206 ÷ €4,000,000 = 9.8%

Top-up Tax % = 15% - 9.8% = 5.2%
Top-up Tax = 5.2% × (€4,000,000 - SBIE) = [to be calculated in Part 5]
```

---

## Task 7: Covered Tax Computation—Ireland

### Current Tax Adjustments

**Starting point:**
```
Current tax expense (P&L):              €1,875,000
Less: R&D credit                        (€225,000)
Net per accounts:                       €1,650,000
```

**QRTC Analysis:**

Irish Knowledge Development Box credit:
- Is it refundable? → Check: KDB is a reduced rate, not a refundable credit
- **Conclusion:** NOT a QRTC—remains as reduction to Covered Taxes

```
Adjusted Current Tax:                   €1,650,000
```

### WHT Allocation (Article 4.3.2(e))

Ireland paid dividend to UK parent. Any UK WHT on receipt would be allocated back to Ireland.

**Data:** No UK WHT (treaty exemption)

```
WHT allocation:                         €0
```

### Deferred Tax Adjustments

Irish rate (12.5%) < 15%:
- DTAs can be recast UP to 15% if from GloBE Losses (Article 4.4.3)
- DTLs remain at 12.5% (lower of rate or 15%)

| Item | At 12.5% | At 15% | Treatment |
|------|----------|--------|-----------|
| DTL on R&D assets | €120,000 | €120,000 | No change (12.5% < 15%) |

```
DTAA = €120,000
```

### Total Adjusted Covered Taxes—Ireland

| Component | Amount (€) |
|-----------|------------|
| Adjusted Current Tax | 1,650,000 |
| DTAA | 120,000 |
| **Total Adjusted Covered Taxes** | **1,770,000** |

### ETR Calculation—Ireland

```
GloBE Income:                           €15,000,000
Adjusted Covered Taxes:                 €1,770,000

ETR = €1,770,000 ÷ €15,000,000 = 11.8%

Top-up Tax % = 15% - 11.8% = 3.2%
Top-up Tax = 3.2% × (€15,000,000 - SBIE) = [to be calculated in Part 5]
```

---

## Task 8: Consolidated Covered Tax Summary

### Jurisdiction Summary Table

| Jurisdiction | GloBE Income (€) | Adj. Covered Taxes (€) | ETR | Top-up Tax Exposure |
|--------------|------------------|------------------------|-----|---------------------|
| Germany | 53,880,000 | 12,393,000 | 23.0% | None |
| Singapore | 4,000,000 | 392,206 | 9.8% | Yes (5.2%) |
| Ireland | 15,000,000 | 1,770,000 | 11.8% | Yes (3.2%) |

### UK Parent Position (Post-Allocations)

| Item | Original (€) | Allocated Out (€) | Remaining (€) |
|------|--------------|-------------------|---------------|
| UK corporate tax | 5,000,000 | — | 5,000,000 |
| CFC tax (Singapore) | 320,000 | (202,500) | 117,500 |
| WHT on Irish dividend | 0 | — | 0 |
| **UK Covered Taxes** | **5,320,000** | **(202,500)** | **5,117,500** |

**Note:** €117,500 of CFC tax remains in UK (passive income limitation applied)

---

## Model Answers

### Answer 1: Germany Covered Tax Classification

**Covered Taxes:**
- Corporate income tax: €8,200,000
- Solidarity surcharge: €451,000
- Trade tax: €3,100,000
- **Total: €11,751,000**

**Non-Covered Taxes (excluded):**
- VAT, wage tax, property tax

**QRTC:** R&D credit €180,000 → Treat as income

---

### Answer 2: Germany Current Tax Adjustments

| Line | Description | Amount (€) |
|------|-------------|------------|
| A | Current tax expense (P&L) | 11,751,000 |
| B | Add: Tax in OCI | 67,000 |
| C | Add: Prior year UTP paid | 150,000 |
| D | Add: QRTC reversal | 180,000 |
| E | Less: Current year UTP | (280,000) |
| **F** | **Adjusted Current Tax** | **11,868,000** |

---

### Answer 3: Germany Deferred Tax Adjustments

| Line | Description | Amount (€) |
|------|-------------|------------|
| A | DT expense per P&L | 980,000 |
| B | Rate cap adjustment (30% → 15%) | (525,000) |
| C | Exclude: VA movement | 150,000 |
| D | Exclude: Rate change | (80,000) |
| **E** | **DTAA** | **525,000** |

---

### Answer 4: Singapore CFC Push-Down

| Step | Calculation | Result |
|------|-------------|--------|
| Pre-push ETR | €150,000 ÷ €4,000,000 | 3.75% |
| Top-up Tax % | 15% - 3.75% | 11.25% |
| Passive income cap | €1,800,000 × 11.25% | €202,500 |
| Push-down amount | MIN(€320,000, €202,500) | **€202,500** |

---

### Answer 5: Final Adjusted Covered Taxes

| Jurisdiction | Amount (€) | ETR |
|--------------|------------|-----|
| Germany | 12,393,000 | 23.0% |
| Singapore | 392,206 | 9.8% |
| Ireland | 1,770,000 | 11.8% |

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
E4  Top-up Tax % (15% - E3, if positive)        ____________
```

---

## Learning Points

### Point 1: QRTC Dual Adjustment

The German R&D credit is a QRTC and requires adjustments to BOTH:
- Covered Taxes: Add back €180,000 (reverse accounting treatment)
- GloBE Income: Add €180,000 (treat as income)

Forgetting either adjustment distorts the ETR calculation.

### Point 2: Passive Income Limitation Prevents Full Push-Down

The UK CFC charge of €320,000 on Singapore could only be pushed down to the extent of €202,500 due to the passive income limitation. The remaining €117,500 stays in UK Covered Taxes.

Without this limitation, Singapore's ETR would be:
- (€150,000 + €320,000) ÷ €4,000,000 = 11.75%

With limitation:
- (€150,000 + €202,500) ÷ €4,000,000 = 8.8%

The limitation ensures the CFC push-down doesn't artificially eliminate Singapore's Top-up Tax exposure.

### Point 3: Rate Cap Creates Significant Adjustment

Germany's 30% rate means all deferred tax movements are recast at 15%—halving their GloBE impact. The €525,000 rate cap adjustment represents a material reduction from the €1,050,000 that would have been included at accounting rates.

### Point 4: Irish KDB Is Not a QRTC

Unlike Germany's R&D credit, Ireland's Knowledge Development Box is a reduced tax rate (6.25% on qualifying IP income), not a refundable credit. It therefore reduces Covered Taxes directly rather than being treated as income.

### Point 5: Document Classification Decisions

Each tax item requires explicit classification with reference to Article 4.2.1. The classification workpaper provides audit defence and ensures consistency across fiscal years.

---

## Key References

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
