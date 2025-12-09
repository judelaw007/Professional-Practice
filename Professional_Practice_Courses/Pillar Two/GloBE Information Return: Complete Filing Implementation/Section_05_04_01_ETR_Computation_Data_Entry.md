# Section 5.4: Completing GIR Section 3: GloBE Computations

## 5.4.1 ETR Computation Data Entry

### Introduction

GIR Section 3 represents the computational heart of the GloBE Information Return. With approximately 400+ data points that scale with each jurisdiction and Constituent Entity, this section captures the detailed calculations underlying each jurisdiction's Effective Tax Rate (ETR) and any resulting Top-up Tax liability.

This section provides step-by-step guidance for completing the ETR computation portion of Section 3, covering GloBE Income/Loss determination, Covered Taxes allocation, and the jurisdictional ETR calculation.

**Learning Objectives:**
- Calculate GloBE Income/Loss from financial accounting starting points
- Apply required GloBE adjustments systematically
- Determine Covered Taxes with current and deferred tax components
- Compute the jurisdictional ETR and validate results

---

### 5.4.1.1 Section 3 Architecture Overview

#### Understanding the Three-Part Structure

GIR Section 3: GloBE Computations comprises three integrated sub-sections:

| Sub-Section | Description | Data Points (Approximate) |
|-------------|-------------|---------------------------|
| **3.1 ETR Computation** | GloBE Income, Covered Taxes, ETR calculation | ~100 data points |
| **3.2 SBIE Computation** | Payroll and tangible asset carve-outs | ~30 data points |
| **3.3 Top-Up Tax Computation** | Excess profit, Top-up Tax, allocation | ~40 data points |

**Additional Data Categories within Section 3:**

| Category | Description | Data Points |
|----------|-------------|-------------|
| Deferred Tax Adjustments | DTL recapture, loss carrybacks | ~50+ data points |
| Transitional Provisions | Article 9.1 elections, transition rules | ~20+ data points |
| Elections | Jurisdictional and entity-level elections | ~40 data points |
| Miscellaneous Adjustments | Cross-border allocations, special cases | ~120 data points |
| International Shipping | Excluded income calculations | ~20 data points |

**Calculator Tab:** `Section 3 - ETR Computation`

---

### 5.4.1.2 The ETR Calculation Formula

#### Core Formula

The fundamental ETR calculation under the GloBE Rules is:

```
                    Jurisdictional Adjusted Covered Taxes
Jurisdictional ETR = ─────────────────────────────────────────
                    Jurisdictional Net GloBE Income

Result: Expressed as percentage, rounded to fourth decimal place (e.g., 14.2356%)
```

**Key Components:**

| Component | Definition | GIR Data Source |
|-----------|------------|-----------------|
| **Adjusted Covered Taxes** | Current tax expense + Adjusted deferred tax expense | Section 3.1.2 |
| **Net GloBE Income** | Financial accounting income ± GloBE adjustments | Section 3.1.1 |
| **Minimum Rate** | 15% (global standard) | Fixed reference |

**Critical Rule: GloBE Loss Scenario**

If a jurisdiction has Net GloBE Loss (negative income), the ETR is not calculated. The GIR requires disclosure of the reason ETR was not computed in such cases.

---

### 5.4.1.3 GloBE Income/Loss Calculation

#### Starting Point: Financial Accounting Net Income or Loss

Under Article 3.1 of the GloBE Model Rules, the calculation starts with each Constituent Entity's **Financial Accounting Net Income or Loss (FANIL)**.

**Key Principles:**

```
FANIL Determination:
├── Source: Information used to prepare consolidated financial statements
├── Basis: Net income/loss "below the line" (after tax)
├── Standard: UPE's accounting framework (IFRS, US GAAP, or Authorised)
├── Adjustments: Consolidation eliminations are EXCLUDED for GloBE purposes
└── Note: Uses individual CE accounts adjusted to consolidated standard
```

**Calculator Data Entry - Financial Accounting Starting Point:**

| Field | Cell Reference | Format | Source | Example |
|-------|---------------|--------|--------|---------|
| Jurisdiction Code | B5 | ISO 3166-1 alpha-2 | Section 1 | DE |
| Constituent Entity Name | C5 | Text | Section 1 | GlobalCo GmbH |
| Entity Identifier | D5 | Alphanumeric | System-generated | CE-DE-001 |
| Fiscal Year End | E5 | Date | Group standard | 31/12/2024 |
| **FANIL per CE Accounts** | F5 | Currency (€) | Local accounts | €12,500,000 |
| FANIL Consolidation Adjustment | G5 | Currency (€) | Consolidation | (€500,000) |
| **FANIL for GloBE** | H5 | Currency (€) | F5-G5 | €12,000,000 |

---

#### GloBE Adjustments: Article 3.2 Requirements

The Financial Accounting Net Income/Loss must be adjusted to arrive at GloBE Income/Loss. These adjustments create a "substituted, standardized measure of taxable income."

**Categories of GloBE Adjustments:**

```
GloBE Adjustments Framework:
│
├── ADDITIONS to FANIL
│   ├── Net Taxes Expense (add back if deducted)
│   ├── Excluded Dividends add-back
│   ├── Excluded Equity Gains add-back
│   ├── Asymmetric Foreign Currency Gains (add back losses)
│   ├── Policy Disallowed Expenses
│   ├── Prior Period Errors and Changes in Accounting Principles
│   └── Pension Fund Accrual Adjustments
│
├── DEDUCTIONS from FANIL
│   ├── Excluded Dividends
│   ├── Excluded Equity Gains/Losses
│   ├── Asymmetric Foreign Currency Gains (deduct gains)
│   ├── Arm's Length adjustments (transfer pricing)
│   ├── Qualified Refundable Tax Credits (treated as income)
│   ├── International Shipping Income exclusion
│   └── Intra-group financing adjustments
│
└── ENTITY-SPECIFIC Adjustments
    ├── Insurance Company adjustments
    ├── Flow-Through Entity allocations
    ├── Permanent Establishment allocations
    ├── Joint Venture / Investment Entity treatment
    └── Hybrid Entity adjustments
```

---

#### Calculator Data Entry - GloBE Adjustments

**Tab:** `Section 3.1.1 - GloBE Income`

**Step 1: Excluded Dividends (Article 3.2.1(a))**

| Field | Cell Reference | Format | Guidance |
|-------|---------------|--------|----------|
| Portfolio Dividends Received | I5 | Currency | Dividends from <10% holdings |
| Qualifying Dividends Excluded | J5 | Currency | Dividends from ≥10% holdings held >12 months |
| **Total Excluded Dividends** | K5 | Currency | =SUM(I5:J5) |
| Dividend Adjustment Direction | L5 | +/- | Typically negative (deduction) |

**Step 2: Excluded Equity Gains/Losses (Article 3.2.1(b))**

| Field | Cell Reference | Format | Guidance |
|-------|---------------|--------|----------|
| Portfolio Equity Gains | M5 | Currency | Gains on <10% holdings |
| Qualifying Equity Gains Excluded | N5 | Currency | Gains on ≥10% holdings |
| Portfolio Equity Losses | O5 | Currency | Losses on <10% holdings |
| Qualifying Equity Losses Excluded | P5 | Currency | Losses on ≥10% holdings |
| **Net Equity Adjustment** | Q5 | Currency | Complex formula |

**Step 3: Asymmetric Foreign Currency Adjustments (Article 3.2.1(c))**

| Field | Cell Reference | Format | Guidance |
|-------|---------------|--------|----------|
| FX Gains in FANIL | R5 | Currency | Already included in FANIL |
| FX Losses in FANIL | S5 | Currency | Already included in FANIL |
| Asymmetric FX Treatment Applied | T5 | Y/N | Election required |
| **FX Adjustment Amount** | U5 | Currency | If elected, remove asymmetry |

**Step 4: Policy Disallowed Expenses (Article 3.2.1(d))**

| Field | Cell Reference | Format | Guidance |
|-------|---------------|--------|----------|
| Bribes and Corrupt Payments | V5 | Currency | Always disallowed |
| Fines and Penalties | W5 | Currency | Non-deductible amounts |
| Other Policy Disallowed | X5 | Currency | Per Article 3.2.1(d) |
| **Total Policy Disallowed** | Y5 | Currency | =SUM(V5:X5) |

**Step 5: Intra-Group Transactions (Article 3.2.3)**

| Field | Cell Reference | Format | Guidance |
|-------|---------------|--------|----------|
| Transfer Pricing Adjustment Required | Z5 | Y/N | Arm's length test |
| TP Adjustment Amount | AA5 | Currency | Increase or decrease |
| Intra-Group Financing Adjustment | AB5 | Currency | Per Article 3.2.4 |
| **Net Intra-Group Adjustment** | AC5 | Currency | =SUM(Z5:AB5) |

**Step 6: Other Adjustments**

| Field | Cell Reference | Format | Guidance |
|-------|---------------|--------|----------|
| Stock-Based Compensation (Art. 3.2.2) | AD5 | Currency | Election available |
| Pension Fund Accruals | AE5 | Currency | Article 3.2.1(j) |
| Prior Period Errors/Changes | AF5 | Currency | Article 3.2.1(f) |
| Insurance Company Adjustments | AG5 | Currency | If applicable |
| Qualified Refundable Tax Credits | AH5 | Currency | Treated as income |
| International Shipping Exclusion | AI5 | Currency | Article 3.3 |
| **Total Other Adjustments** | AJ5 | Currency | =SUM(AD5:AI5) |

---

#### Arriving at GloBE Income/Loss

**Final GloBE Income Calculation:**

| Field | Cell Reference | Formula | Example |
|-------|---------------|---------|---------|
| FANIL for GloBE | H5 | Starting point | €12,000,000 |
| Excluded Dividends | K5 | (Deduction) | (€500,000) |
| Net Equity Adjustment | Q5 | +/- | (€200,000) |
| FX Adjustment | U5 | +/- | €0 |
| Policy Disallowed | Y5 | Addition | €50,000 |
| Intra-Group Adjustments | AC5 | +/- | (€100,000) |
| Other Adjustments | AJ5 | +/- | €150,000 |
| **GloBE Income (Entity)** | AK5 | =H5+K5+Q5+U5+Y5+AC5+AJ5 | **€11,400,000** |

**Jurisdictional Aggregation:**

```
Jurisdictional Net GloBE Income:
├── Sum of all CE GloBE Income in jurisdiction
├── Less: Sum of all CE GloBE Losses in jurisdiction
├── Result: Net GloBE Income (or Loss) for jurisdiction
└── If negative: GloBE Loss - ETR not calculated
```

**Calculator Summary Row:**

| Field | Cell Reference | Formula | Example |
|-------|---------------|---------|---------|
| **Total GloBE Income - Germany** | AK20 | =SUMIF(B:B,"DE",AK:AK) | €45,600,000 |
| Total GloBE Losses - Germany | AK21 | =SUMIF(B:B,"DE",IF(AK:AK<0,AK:AK,0)) | (€2,100,000) |
| **Net GloBE Income - Germany** | AK22 | =AK20+AK21 | **€43,500,000** |

---

### 5.4.1.4 Covered Taxes Calculation

#### Understanding Covered Taxes

Covered Taxes represent the taxes that count towards meeting the 15% minimum rate. They comprise two components:

```
Adjusted Covered Taxes:
│
├── Current Tax Expense
│   ├── Corporate income tax accrued for the fiscal year
│   ├── In lieu of income taxes
│   ├── Tax on retained earnings / undistributed profits
│   └── Withholding taxes (on dividends, interest, royalties)
│
└── Adjusted Deferred Tax Expense
    ├── Deferred tax expense per accounts
    ├── Capped at minimum rate (15%) on timing differences
    ├── DTL recapture adjustments
    └── Transition year adjustments
```

---

#### Calculator Data Entry - Current Tax Expense

**Tab:** `Section 3.1.2 - Covered Taxes`

**Step 1: Record Current Tax Expense by Entity**

| Field | Cell Reference | Format | Source | Example |
|-------|---------------|--------|--------|---------|
| Entity Identifier | B5 | Alphanumeric | Section 3.1.1 | CE-DE-001 |
| Current Corporate Income Tax | C5 | Currency | Tax accounts | €3,200,000 |
| In Lieu of Income Tax | D5 | Currency | Tax accounts | €0 |
| Taxes on Undistributed Profits | E5 | Currency | Tax accounts | €0 |
| Withholding Tax (borne) | F5 | Currency | Tax accounts | €150,000 |
| CFC Tax Inclusion (allocated) | G5 | Currency | Parent allocation | €0 |
| **Total Current Tax Expense** | H5 | Currency | =SUM(C5:G5) | €3,350,000 |

**Step 2: Current Tax Adjustments**

| Field | Cell Reference | Format | Guidance |
|-------|---------------|--------|----------|
| Uncertain Tax Positions | I5 | Currency | Add back if reserved |
| Non-Covered Tax Deductions | J5 | Currency | Taxes not qualifying |
| Tax Credits (non-qualified) | K5 | Currency | Reduce if not qualified |
| Cross-Border Allocations | L5 | Currency | PE, FTE allocations |
| **Adjusted Current Tax** | M5 | Currency | =H5+I5-J5-K5+L5 |

---

#### Calculator Data Entry - Deferred Tax Expense

**Step 3: Record Deferred Tax Expense**

| Field | Cell Reference | Format | Source | Example |
|-------|---------------|--------|--------|---------|
| Deferred Tax Expense per Accounts | N5 | Currency | Financial statements | €800,000 |
| DTE from Consolidated Accounts | O5 | Currency | If different from CE | €850,000 |
| **Starting DTE** | P5 | Currency | =MAX(N5,O5) | €850,000 |

**Step 4: Deferred Tax Adjustments (Article 4.4)**

| Field | Cell Reference | Format | Guidance |
|-------|---------------|--------|----------|
| DTE Capped at Minimum Rate | Q5 | Currency | Cap DTAs at 15% |
| Excluded Deferred Tax Items | R5 | Currency | Per Article 4.4.1(e) |
| DTL Subject to Recapture | S5 | Currency | Track separately |
| DTL Recapture Adjustment | T5 | Currency | Year 6 recapture |
| Transition Year DTAs | U5 | Currency | Article 9.1 |
| Loss Carryback Adjustment | V5 | Currency | If applicable |
| **Adjusted Deferred Tax** | W5 | Currency | Complex formula |

**Minimum Rate Cap on Deferred Tax Assets:**

```
DTA Minimum Rate Cap:
├── If DTA recorded at > 15%, cap at 15%
├── Example: DTA at €1,000 @ 25% rate = €250
│            Cap: €1,000 × 15% = €150
│            Reduction: €100
└── This prevents "tax planning" through high DTAs
```

---

#### DTL Recapture Tracking

**Critical Compliance Requirement:**

Under Article 4.4.4, certain Deferred Tax Liabilities are subject to recapture if they do not reverse within five years.

**Recapture Exception Accruals (NOT subject to recapture):**

| Category | Example Items | Tracking Required |
|----------|---------------|-------------------|
| Cost Recovery Allowances | Depreciation, amortization (tangibles) | No |
| R&D Expenses | Capitalized development costs | No |
| Decommissioning Costs | Environmental remediation | No |
| Fair Value Accounting | Unrealized gains on financial instruments | No |
| Foreign Exchange | Currency translation adjustments | No |
| Insurance Reserves | Policy liabilities | No |
| Reinvestment Gains | Deferred gain on asset replacement | No |

**DTLs Subject to Recapture:**

| Category | Example Items | Tracking Required |
|----------|---------------|-------------------|
| Intangible Assets | Goodwill, patents, trademarks | **YES** |
| Inventory | LIFO reserve differences | **YES** |
| Other Timing Differences | Non-exception categories | **YES** |

**Calculator DTL Recapture Tracker:**

**Tab:** `DTL Recapture Tracking`

| Field | Cell Reference | Format | Purpose |
|-------|---------------|--------|---------|
| DTL Category | B5 | Text | Aggregated or GL basis |
| Tracking Method | C5 | Dropdown: LIFO/FIFO/Item | June 2024 guidance |
| Year 1 DTL Added | D5 | Currency | Opening balance |
| Year 1 DTL Reversed | E5 | Currency | Reversals in Y1 |
| Year 2 DTL Added | F5 | Currency | New in Y2 |
| Year 2 DTL Reversed | G5 | Currency | Reversals in Y2 |
| [Continue Y3-Y5] | H5-M5 | Currency | Track each year |
| **5-Year Recapture Check** | N5 | Currency | Unreversed balance |
| Recapture Required | O5 | Y/N | =IF(N5>0,"YES","NO") |

**Tracking Methods (per June 2024 Administrative Guidance):**

```
DTL Tracking Approaches:
├── Aggregate DTL Category Basis
│   └── Two or more GL accounts grouped as single category
├── GL Account Basis
│   └── All DTLs in single GL tracked together
├── Item-by-Item Basis
│   └── Individual asset/liability tracking
│
Default Method: LIFO (Last-In, First-Out)
Alternative: FIFO (First-In, First-Out) if elected
```

---

#### Arriving at Adjusted Covered Taxes

**Final Covered Taxes Calculation:**

| Field | Cell Reference | Formula | Example |
|-------|---------------|---------|---------|
| Adjusted Current Tax | M5 | From Step 2 | €3,350,000 |
| Adjusted Deferred Tax | W5 | From Step 4 | €650,000 |
| **Adjusted Covered Taxes (Entity)** | X5 | =M5+W5 | €4,000,000 |

**Jurisdictional Aggregation:**

| Field | Cell Reference | Formula | Example |
|-------|---------------|---------|---------|
| **Total Adjusted Covered Taxes - Germany** | X20 | =SUMIF(A:A,"DE",X:X) | €12,875,000 |

---

### 5.4.1.5 Computing the Jurisdictional ETR

#### Final ETR Calculation

**Calculator Summary - ETR Computation:**

**Tab:** `Section 3 - ETR Summary`

| Field | Cell Reference | Formula | Germany Example |
|-------|---------------|---------|-----------------|
| Jurisdiction | B5 | | DE |
| Net GloBE Income | C5 | From Section 3.1.1 | €43,500,000 |
| Total Adjusted Covered Taxes | D5 | From Section 3.1.2 | €12,875,000 |
| **Jurisdictional ETR** | E5 | =IF(C5>0,D5/C5,"N/A") | **29.5977%** |
| ETR Rounded | F5 | =ROUND(E5,4) | **29.60%** |
| Above Minimum Rate? | G5 | =IF(F5>=0.15,"YES","NO") | YES |
| Top-up Tax Required? | H5 | =IF(G5="YES","NO","YES") | NO |

**ETR Validation Checks:**

| Validation | Formula | Expected Result |
|------------|---------|-----------------|
| ETR Reasonableness | =IF(AND(E5>0,E5<0.5),"PASS","REVIEW") | PASS |
| Statutory Rate Comparison | =IF(E5<StatutoryRate×0.8,"FLAG","OK") | OK |
| Prior Year Comparison | =IF(ABS(E5-PriorYearETR)>0.1,"REVIEW","OK") | OK |
| GloBE Income Sign | =IF(C5<0,"LOSS - NO ETR","INCOME") | INCOME |

---

### 5.4.1.6 Worked Example: 15-Jurisdiction ETR Calculation

**Scenario: GlobalCo Holdings plc - FY 2024**

GlobalCo Holdings plc is a UK-headquartered MNE Group with operations across 15 jurisdictions. Below is the summarized ETR computation for each jurisdiction.

**Step 1: Jurisdictional Summary Input**

| Jurisdiction | # of CEs | Net GloBE Income (€M) | Adj. Covered Taxes (€M) |
|--------------|----------|----------------------|------------------------|
| United Kingdom | 8 | 125.5 | 31.4 |
| Germany | 4 | 43.5 | 12.9 |
| France | 3 | 28.7 | 7.5 |
| Netherlands | 2 | 15.2 | 2.3 |
| Ireland | 5 | 67.3 | 8.4 |
| United States | 12 | 210.6 | 44.2 |
| Singapore | 3 | 35.8 | 6.1 |
| Hong Kong | 2 | 22.4 | 3.7 |
| Switzerland | 2 | 18.9 | 2.5 |
| Luxembourg | 1 | 8.5 | 0.9 |
| Australia | 2 | 31.2 | 9.4 |
| Japan | 3 | 45.6 | 13.7 |
| South Korea | 2 | 19.8 | 5.0 |
| Canada | 2 | 24.3 | 5.8 |
| Brazil | 1 | (2.1) | N/A |

**Step 2: ETR Calculation Results**

| Jurisdiction | ETR Calculated | ETR (Rounded) | vs. 15% Minimum | Status |
|--------------|---------------|---------------|-----------------|--------|
| United Kingdom | 25.02% | 25.02% | +10.02% | No Top-up |
| Germany | 29.66% | 29.66% | +14.66% | No Top-up |
| France | 26.13% | 26.13% | +11.13% | No Top-up |
| Netherlands | 15.13% | 15.13% | +0.13% | No Top-up |
| Ireland | 12.48% | 12.48% | -2.52% | **TOP-UP DUE** |
| United States | 20.99% | 20.99% | +5.99% | No Top-up |
| Singapore | 17.04% | 17.04% | +2.04% | No Top-up |
| Hong Kong | 16.52% | 16.52% | +1.52% | No Top-up |
| Switzerland | 13.23% | 13.23% | -1.77% | **TOP-UP DUE** |
| Luxembourg | 10.59% | 10.59% | -4.41% | **TOP-UP DUE** |
| Australia | 30.13% | 30.13% | +15.13% | No Top-up |
| Japan | 30.04% | 30.04% | +15.04% | No Top-up |
| South Korea | 25.25% | 25.25% | +10.25% | No Top-up |
| Canada | 23.87% | 23.87% | +8.87% | No Top-up |
| Brazil | N/A | N/A | N/A | GloBE Loss |

**Step 3: Identify Jurisdictions Requiring Top-Up Tax Computation**

```
Jurisdictions with ETR < 15%:
├── Ireland: ETR 12.48% → Top-up Tax Percentage: 2.52%
├── Switzerland: ETR 13.23% → Top-up Tax Percentage: 1.77%
└── Luxembourg: ETR 10.59% → Top-up Tax Percentage: 4.41%

Jurisdictions with GloBE Loss:
└── Brazil: No ETR calculation; no Top-up Tax (unless loss offset rules apply)
```

---

### 5.4.1.7 GIR Section 3.1 Data Entry Fields Reference

#### Complete Field List for ETR Computation

**GloBE Income Fields (Section 3.1.1):**

| Field # | Description | Data Type | Mandatory |
|---------|-------------|-----------|-----------|
| 3.1.1.1 | Financial Accounting Net Income/Loss | Currency | Yes |
| 3.1.1.2 | Net Taxes Expense | Currency | Yes |
| 3.1.1.3 | Excluded Dividends | Currency | Conditional |
| 3.1.1.4 | Excluded Equity Gains/Losses | Currency | Conditional |
| 3.1.1.5 | Asymmetric Foreign Currency Adjustment | Currency | If elected |
| 3.1.1.6 | Policy Disallowed Expenses | Currency | If applicable |
| 3.1.1.7 | Prior Period Errors/Changes | Currency | If applicable |
| 3.1.1.8 | Intra-Group Financing Adjustments | Currency | If applicable |
| 3.1.1.9 | Stock-Based Compensation Adjustment | Currency | If elected |
| 3.1.1.10 | Qualified Refundable Tax Credits | Currency | If applicable |
| 3.1.1.11 | International Shipping Income Exclusion | Currency | If applicable |
| 3.1.1.12 | Flow-Through Entity Allocation | Currency | If applicable |
| 3.1.1.13 | PE Income Allocation | Currency | If applicable |
| 3.1.1.14 | Other GloBE Adjustments | Currency | If applicable |
| **3.1.1.15** | **GloBE Income/Loss (Entity)** | **Currency** | **Calculated** |

**Covered Taxes Fields (Section 3.1.2):**

| Field # | Description | Data Type | Mandatory |
|---------|-------------|-----------|-----------|
| 3.1.2.1 | Current Tax Expense | Currency | Yes |
| 3.1.2.2 | Deferred Tax Expense | Currency | Yes |
| 3.1.2.3 | Current Tax Adjustments | Currency | If applicable |
| 3.1.2.4 | Deferred Tax Adjustments | Currency | If applicable |
| 3.1.2.5 | DTA Minimum Rate Cap Adjustment | Currency | If applicable |
| 3.1.2.6 | DTL Recapture Adjustment | Currency | If applicable |
| 3.1.2.7 | Transition Year DTA Adjustment | Currency | Year 1 only |
| 3.1.2.8 | Cross-Border Tax Allocation | Currency | If applicable |
| 3.1.2.9 | Tax Credits Adjustment | Currency | If applicable |
| **3.1.2.10** | **Adjusted Covered Taxes (Entity)** | **Currency** | **Calculated** |

**ETR Summary Fields (Section 3.1.3):**

| Field # | Description | Data Type | Mandatory |
|---------|-------------|-----------|-----------|
| 3.1.3.1 | Jurisdictional Net GloBE Income | Currency | Yes |
| 3.1.3.2 | Jurisdictional Adjusted Covered Taxes | Currency | Yes |
| 3.1.3.3 | Jurisdictional ETR | Percentage | Calculated |
| 3.1.3.4 | Reason ETR Not Calculated | Text | If N/A |
| 3.1.3.5 | Top-up Tax Percentage | Percentage | If <15% |

---

### 5.4.1.8 Common ETR Computation Errors

#### Error 1: Incorrect FANIL Starting Point

**Problem:** Using standalone entity accounts instead of consolidation-adjusted figures.

**Solution:**
```
Correct Approach:
├── Start with CE accounts prepared for consolidation
├── Apply UPE's accounting policies consistently
├── Exclude consolidation elimination entries
└── Verify currency translation to EUR (GIR currency)
```

#### Error 2: Missing GloBE Adjustments

**Problem:** Failing to make required adjustments for excluded dividends or equity gains.

**Solution:**
```
Adjustment Checklist:
☐ Dividends from portfolio holdings (<10%) excluded?
☐ Dividends from qualifying holdings (≥10%, >12 months) excluded?
☐ Equity gains/losses on qualifying holdings excluded?
☐ Policy disallowed expenses added back?
☐ Intra-group transaction adjustments made?
```

#### Error 3: Deferred Tax Cap Not Applied

**Problem:** Recording DTAs at statutory rate instead of capping at 15%.

**Solution:**
```
DTA Cap Calculation:
├── Identify all DTAs in Covered Taxes
├── Calculate implied tax rate for each DTA
├── If rate > 15%, recalculate at 15%
├── Reduce Adjusted Covered Taxes by the difference
└── Document cap adjustment in GIR notes
```

#### Error 4: DTL Recapture Not Tracked

**Problem:** Failing to monitor DTLs for 5-year recapture.

**Solution:**
```
Recapture Tracking Setup:
├── Identify all DTLs not qualifying for exceptions
├── Choose tracking method (Aggregate/GL/Item)
├── Establish Year 1 baseline
├── Track additions and reversals annually
├── Flag unreversed balances approaching Year 5
└── Calculate recapture adjustment if triggered
```

#### Error 5: GloBE Loss Mishandled

**Problem:** Attempting to calculate ETR when jurisdiction has net loss.

**Solution:**
```
GloBE Loss Handling:
├── If Net GloBE Income < 0, stop ETR calculation
├── Record reason in GIR field 3.1.3.4
├── Track loss for potential carryforward
├── No Top-up Tax due (generally)
└── Consider QDMTT rules for loss utilization
```

---

### 5.4.1.9 ETR Computation Checklist

Use this checklist to ensure complete and accurate ETR computation:

**GloBE Income (Section 3.1.1):**

| # | Check Item | Status |
|---|------------|--------|
| 1 | FANIL obtained from consolidation package for each CE | ☐ |
| 2 | FANIL excludes consolidation elimination entries | ☐ |
| 3 | Excluded dividends identified and removed | ☐ |
| 4 | Excluded equity gains/losses identified and removed | ☐ |
| 5 | Policy disallowed expenses added back | ☐ |
| 6 | Asymmetric FX election documented (if made) | ☐ |
| 7 | Intra-group transaction adjustments applied | ☐ |
| 8 | Stock-based compensation election documented (if made) | ☐ |
| 9 | Qualified refundable tax credits treated as income | ☐ |
| 10 | International shipping exclusion calculated (if applicable) | ☐ |
| 11 | Entity-level GloBE Income calculated and validated | ☐ |
| 12 | Jurisdictional aggregation completed | ☐ |

**Covered Taxes (Section 3.1.2):**

| # | Check Item | Status |
|---|------------|--------|
| 13 | Current tax expense recorded per CE | ☐ |
| 14 | Deferred tax expense obtained (consolidated basis) | ☐ |
| 15 | DTA minimum rate cap applied | ☐ |
| 16 | DTL recapture tracking established | ☐ |
| 17 | DTL recapture adjustments calculated (if Year 6+) | ☐ |
| 18 | Transition year DTA adjustments applied | ☐ |
| 19 | Cross-border tax allocations made (CFC, PE) | ☐ |
| 20 | Tax credits correctly classified (qualified vs. non-qualified) | ☐ |
| 21 | Entity-level Adjusted Covered Taxes calculated | ☐ |
| 22 | Jurisdictional aggregation completed | ☐ |

**ETR Calculation (Section 3.1.3):**

| # | Check Item | Status |
|---|------------|--------|
| 23 | ETR calculated for all profit jurisdictions | ☐ |
| 24 | ETR rounded to fourth decimal place | ☐ |
| 25 | GloBE Loss jurisdictions marked with reason | ☐ |
| 26 | Top-up Tax percentage calculated where ETR < 15% | ☐ |
| 27 | Validation checks performed (reasonableness) | ☐ |
| 28 | Prior year comparison completed | ☐ |
| 29 | Statutory rate comparison documented | ☐ |
| 30 | Tax director sign-off obtained | ☐ |

---

### 5.4.1.10 Key Takeaways

#### Strategic Considerations for ETR Computation

1. **Data Quality is Critical**
   - ETR computation requires high-quality financial and tax data
   - Invest in reconciliation between consolidation packages and tax accounts
   - Establish clear data ownership between finance and tax teams

2. **Adjustment Tracking is Complex**
   - Maintain detailed schedules for each GloBE adjustment category
   - Document election decisions and their rationale
   - Build audit trail for all adjustments made

3. **Deferred Tax Requires Ongoing Monitoring**
   - DTL recapture tracking is a multi-year commitment
   - Establish systems for Year 1 to avoid Year 6 surprises
   - Consider voluntary DTL exclusion election for long-term items

4. **Near-Threshold Jurisdictions Need Attention**
   - Jurisdictions with ETR 15-17% should be monitored closely
   - Small changes in GloBE Income or Covered Taxes can flip status
   - Model sensitivity to key assumptions

5. **Documentation Supports Defence**
   - Maintain detailed workpapers for all calculations
   - Document judgment calls and methodology choices
   - Prepare for tax authority inquiry from Year 1

---

## Practice This Skill: GIR ETR Calculator

Now that you understand the ETR calculation methodology, you can practice using the **GIR ETR Calculator (GIR-001)** on tools.mojitax.com.

| Tool | Tool ID | Purpose |
|------|---------|---------|
| GIR ETR Calculator | GIR-001 | Calculate jurisdictional ETR from GloBE Income and Adjusted Covered Taxes |

**Demo Tool vs Professional Tool**

This is a demo tool for learning purposes. In professional practice, you would use enterprise Pillar Two software with full audit trails, multi-entity processing, and compliance features. The demo tool helps you understand the mechanics without the complexity of production systems.

**To Practice:**

1. Go to tools.mojitax.com and find **GIR ETR Calculator**
2. Use the GlobalTech data from **Case Study 1** in the Appendices:
   - Ireland: GloBE Income €45,000,000 | Adjusted Covered Taxes €5,625,000
   - Switzerland: GloBE Income €28,000,000 | Adjusted Covered Taxes €3,640,000
3. Enter the values and calculate
4. **Expected Results:**
   - Ireland ETR: 12.5000% (below 15% minimum)
   - Switzerland ETR: 13.0000% (below 15% minimum)

If your results differ, review Section 5.4.1.2 (The ETR Calculation Formula) to check your understanding.

---

## Section Summary

Section 3.1 of the GIR captures the detailed ETR computation for each jurisdiction. Key requirements include:

- **GloBE Income/Loss:** Starting from FANIL and applying required adjustments
- **Adjusted Covered Taxes:** Current tax + Adjusted deferred tax with caps and recapture
- **ETR Calculation:** Covered Taxes ÷ GloBE Income, rounded to four decimal places
- **Validation:** Reasonableness checks and prior year comparisons

The GIR Completion Calculator automates calculations while maintaining audit trail and validation checks to ensure accurate and defensible ETR computation.

---

## Navigation

**Previous:** [Section 5.3: Completing GIR Section 2: Safe Harbours and Exclusions](Section_05_03_Completing_GIR_Section_2.md)

You have completed the ETR computation. Continue with the remaining GloBE computation components in the subsequent subsections.

**Return to:** [Table of Contents](00_Table_of_Contents.md)
