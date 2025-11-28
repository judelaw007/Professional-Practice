# Section 3: Understanding the GIR Structure

## 3.4 GIR Section 3: GloBE Computations

**Estimated Reading Time:** 40 minutes
**Pages:** 15-18

---

## Learning Objectives for This Section

By the end of this section, you will be able to:

- Calculate GloBE Income or Loss for each jurisdiction
- Determine Adjusted Covered Taxes including deferred tax adjustments
- Compute the jurisdictional Effective Tax Rate (ETR)
- Apply the Substance-Based Income Exclusion (SBIE) correctly
- Calculate Top-up Tax for low-taxed jurisdictions
- Allocate Top-up Tax under IIR, UTPR, and QDMTT mechanisms
- Understand the DTL recapture rule and its exceptions

---

## Overview of GIR Section 3

GIR Section 3 (GloBE Computations) is the **substantive calculation section** of the GloBE Information Return. This is where the actual tax computations are performed to determine whether top-up tax is payable.

**Data Points:** Section 3 contains approximately **400+ data points**, which scale significantly based on:
- Number of jurisdictions (each requires separate computation)
- Number of constituent entities per jurisdiction
- Complexity of deferred tax positions
- Number of elections made

**Key Principle:** Section 3 is only completed for jurisdictions where **no safe harbour applies**. If a jurisdiction qualifies for a safe harbour under Section 2, Section 3 is either not required or significantly reduced.

---

## Section 3 Sub-Components

| Sub-Section | Content | Approximate Data Points |
|-------------|---------|------------------------|
| **3.1** | ETR Computation | ~50 (per jurisdiction) |
| **3.2** | Substance-Based Income Exclusion (SBIE) | ~20-30 (per jurisdiction) |
| **3.3** | Top-Up Tax Computation | ~40 (per jurisdiction) |
| **3.4** | Top-Up Tax Allocation and Attribution | ~20 (total) |

**Additional Sections:**
- Deferred Tax Adjustments: ~50+ data points
- Transitional Provisions: ~20+ data points
- Elections: ~40 data points
- Miscellaneous Adjustments: ~120 data points

---

## 3.4.1 ETR Computation Data

### The Basic ETR Formula

The Effective Tax Rate (ETR) is calculated at the **jurisdictional level**, not the entity level:

```
                    Adjusted Covered Taxes
Jurisdictional ETR = ─────────────────────────────
                    Net GloBE Income (or Loss)
```

**Key Points:**
- ETR is expressed as a percentage rounded to the **fourth decimal place**
- If there is a Net GloBE Loss, no ETR calculation is required
- ETR below 15% triggers Top-up Tax calculation

---

### GloBE Income or Loss Calculation

GloBE Income starts with the Financial Accounting Net Income or Loss (FANIL) and applies specific adjustments.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    GloBE INCOME CALCULATION                                 │
└─────────────────────────────────────────────────────────────────────────────┘

   Financial Accounting Net Income or Loss (FANIL)
                        │
                        ▼
   ┌─────────────────────────────────────────────────────────────────────────┐
   │                    ARTICLE 3.2 ADJUSTMENTS                              │
   ├─────────────────────────────────────────────────────────────────────────┤
   │  (+) Add back: Covered Taxes expense                                    │
   │  (+) Add back: Dividends excluded under Art. 3.2.1(a)                   │
   │  (+) Add back: Excluded Equity Gains excluded under Art. 3.2.1(b)       │
   │  (-) Deduct: Excluded Equity Losses under Art. 3.2.1(b)                 │
   │  (+/-) Adjust: International Shipping Income (Art. 3.3)                 │
   │  (+/-) Adjust: Policy Disallowed Expenses (Art. 3.2.1(c))              │
   │  (+/-) Adjust: Prior Period Errors and Accounting Changes (Art. 3.2.4) │
   │  (+/-) Adjust: Asymmetric Foreign Currency Gains/Losses                 │
   │  (+/-) Adjust: Stock-based compensation (if election made)              │
   │  (+/-) Adjust: Asset revaluation adjustments                            │
   │  (+/-) Adjust: Pension expense adjustments                              │
   │  (+/-) Other adjustments per GloBE Model Rules                          │
   └─────────────────────────────────────────────────────────────────────────┘
                        │
                        ▼
              GloBE Income or Loss (Entity Level)
                        │
                        ▼
   ┌─────────────────────────────────────────────────────────────────────────┐
   │                    JURISDICTIONAL AGGREGATION                           │
   ├─────────────────────────────────────────────────────────────────────────┤
   │  Sum of GloBE Income of all CEs in jurisdiction                         │
   │  LESS: Sum of GloBE Losses of all CEs in jurisdiction                   │
   └─────────────────────────────────────────────────────────────────────────┘
                        │
                        ▼
              Net Jurisdictional GloBE Income (or Loss)
```

### Key GloBE Income Adjustments

| Adjustment | Article | Direction | Description |
|------------|---------|-----------|-------------|
| **Covered Taxes** | 3.2.1(a) | Add back | Tax expense is separately calculated |
| **Excluded Dividends** | 3.2.1(a) | Adjust | Participation exemption dividends |
| **Excluded Equity Gains/Losses** | 3.2.1(b) | Adjust | Equity gains on qualifying shareholdings |
| **Policy Disallowed Expenses** | 3.2.1(c) | Add back | Bribes, fines, penalties |
| **Prior Period Errors** | 3.2.4 | Adjust | Material prior period adjustments |
| **Asymmetric FX** | 3.2.1(d) | Adjust | Foreign currency on ownership interests |
| **International Shipping** | 3.3 | Exclude | Qualifying shipping income exclusion |
| **Stock-Based Compensation** | 3.2.2 | Election | Optional adjustment to deductible amount |
| **Asset Disposals** | 3.2.1(c) | Adjust | Arm's length gain/loss on intra-group transfers |

---

### Covered Taxes Calculation

Covered Taxes are the taxes included in the ETR numerator. The calculation starts with the **Current Tax Expense** from financial statements.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    ADJUSTED COVERED TAXES CALCULATION                       │
└─────────────────────────────────────────────────────────────────────────────┘

   Current Tax Expense (per Financial Statements)
                        │
                        ▼
   ┌─────────────────────────────────────────────────────────────────────────┐
   │                    ARTICLE 4.1 ADJUSTMENTS                              │
   ├─────────────────────────────────────────────────────────────────────────┤
   │  (-) Taxes not relating to GloBE Income                                 │
   │  (-) Uncertain Tax Position accruals                                    │
   │  (-) Taxes relating to Excluded Dividends                               │
   │  (-) Taxes relating to Excluded Equity Gains/Losses                     │
   │  (+) Covered Taxes paid in respect of prior periods                     │
   │  (+/-) Other adjustments per Art. 4.1.2 - 4.1.5                         │
   └─────────────────────────────────────────────────────────────────────────┘
                        │
                        ▼
   ┌─────────────────────────────────────────────────────────────────────────┐
   │                    DEFERRED TAX ADJUSTMENT (Art. 4.4)                   │
   ├─────────────────────────────────────────────────────────────────────────┤
   │  (+) Deferred Tax Expense (credit for DTL increase)                     │
   │  (-) Deferred Tax Benefit (debit for DTL decrease)                      │
   │  Cap: DTL credit capped at 15% of timing difference                     │
   │  Subject to: 5-year recapture rule                                      │
   └─────────────────────────────────────────────────────────────────────────┘
                        │
                        ▼
              Adjusted Covered Taxes
```

### Deferred Tax Adjustments (Article 4.4)

Deferred Tax Liabilities (DTLs) can increase Adjusted Covered Taxes, subject to important limitations:

| Rule | Description |
|------|-------------|
| **15% Cap** | DTL credit is capped at 15% of the timing difference |
| **5-Year Recapture** | DTL must reverse within 5 years or be recaptured |
| **Recapture Exception Accruals** | Certain DTLs exempt from recapture (see below) |
| **Unclaimed Accrual Option** | Can elect to exclude DTLs expected not to reverse |

**Recapture Exception Accruals (REAs):**

These DTLs do NOT require 5-year monitoring:

| Category | Examples |
|----------|----------|
| **Cost Recovery Allowances** | Depreciation on tangible assets |
| **R&D Expenses** | Capitalized development costs |
| **Decommissioning/Remediation** | Environmental provisions |
| **Fair Value Accounting** | Unrealized gains/losses |
| **Foreign Exchange** | FX gains/losses on monetary items |
| **Insurance Reserves** | Policy reserves and DAC |

---

### Negative ETR Scenarios

If Adjusted Covered Taxes are negative (tax credit or refund position), the ETR can be negative:

```
EXAMPLE: Negative ETR
─────────────────────────────────────────────────────────────────────────────

Jurisdiction: Country X
GloBE Income:           €100,000,000
Adjusted Covered Taxes: -€5,000,000 (net refund position)

ETR Calculation:
  -€5,000,000 ÷ €100,000,000 = -5%

Top-up Tax Percentage:
  15% - (-5%) = 20%

Result: 20% Top-up Tax Percentage applies to Excess Profit
```

---

### GIR Section 3.1 Data Elements

| Field | Description | Source |
|-------|-------------|--------|
| **Jurisdiction** | 2-character country code | ISO 3166-1 Alpha-2 |
| **FANIL** | Financial Accounting Net Income or Loss | Consolidated accounts |
| **Covered Taxes (Current)** | Current tax expense | Financial statements |
| **Covered Taxes (Deferred)** | Deferred tax adjustment | Tax provision |
| **GloBE Adjustments** | Net adjustments under Article 3.2 | GloBE calculations |
| **Net GloBE Income** | Jurisdictional total | Aggregation |
| **Adjusted Covered Taxes** | Jurisdictional total | Aggregation |
| **ETR** | Calculated rate | Formula |

---

## 3.4.2 Substance-Based Income Exclusion (SBIE)

The SBIE is a **carve-out** that reduces the amount of GloBE Income subject to Top-up Tax. It recognizes that MNEs with substantial payroll and tangible assets in a jurisdiction have genuine economic substance.

### SBIE Formula

```
SBIE = Payroll Carve-Out + Tangible Asset Carve-Out

Where:
  Payroll Carve-Out    = Eligible Payroll Costs × Payroll Rate
  Tangible Asset Carve-Out = Eligible Tangible Assets × Asset Rate
```

### SBIE Phase-In Rates

The carve-out rates are transitional for the first 10 years:

| Fiscal Year | Payroll Rate | Tangible Asset Rate |
|------------|--------------|---------------------|
| **2024** | 9.8% | 7.8% |
| **2025** | 9.6% | 7.6% |
| **2026** | 9.4% | 7.4% |
| **2027** | 9.2% | 7.2% |
| **2028** | 9.0% | 7.0% |
| **2029** | 8.2% | 6.6% |
| **2030** | 7.4% | 6.2% |
| **2031** | 6.6% | 5.8% |
| **2032** | 5.8% | 5.4% |
| **2033+** | 5.0% | 5.0% |

### Eligible Payroll Costs

| Included | Excluded |
|----------|----------|
| Salaries and wages | Costs for Excluded Entities |
| Employee benefits | Stock-based compensation (unless election) |
| Payroll taxes (employer portion) | Independent contractor fees |
| Pension contributions | Amounts capitalized to assets |
| Other compensation costs | Intercompany recharges (unless eligible) |

### Eligible Tangible Assets

| Included | Excluded |
|----------|----------|
| Property, plant and equipment | Intangible assets |
| Natural resources | Goodwill |
| Right-of-use assets (leases) | Financial assets |
| Inventory (at cost) | Assets held for sale |
| Land and buildings | Investment property (at fair value) |

**Carrying Value:** Use the average of the opening and closing carrying values for the fiscal year.

### SBIE Calculation Example

```
EXAMPLE: SBIE Calculation for Fiscal Year 2024
─────────────────────────────────────────────────────────────────────────────

Jurisdiction: Germany

Payroll Data:
  Total Eligible Payroll Costs:        €50,000,000
  Payroll Rate (2024):                 9.8%
  Payroll Carve-Out:                   €50,000,000 × 9.8% = €4,900,000

Tangible Asset Data:
  Opening Carrying Value:              €180,000,000
  Closing Carrying Value:              €220,000,000
  Average Carrying Value:              €200,000,000
  Asset Rate (2024):                   7.8%
  Asset Carve-Out:                     €200,000,000 × 7.8% = €15,600,000

Total SBIE:
  €4,900,000 + €15,600,000 = €20,500,000

Effect: €20,500,000 is excluded from Excess Profit calculation
```

### GIR Section 3.2 Data Elements

| Field | Description | Source |
|-------|-------------|--------|
| **Eligible Payroll Costs** | Total qualifying payroll | HR/Payroll systems |
| **Payroll Rate Applied** | Rate for fiscal year | SBIE schedule |
| **Payroll Carve-Out** | Calculated amount | Formula |
| **Tangible Assets (Opening)** | Opening carrying value | Fixed asset register |
| **Tangible Assets (Closing)** | Closing carrying value | Fixed asset register |
| **Average Tangible Assets** | Average of opening/closing | Calculation |
| **Asset Rate Applied** | Rate for fiscal year | SBIE schedule |
| **Asset Carve-Out** | Calculated amount | Formula |
| **Total SBIE** | Sum of carve-outs | Aggregation |

---

## 3.4.3 Top-Up Tax Computation

If the jurisdictional ETR is below 15%, Top-up Tax is calculated.

### Top-Up Tax Calculation Flow

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                       TOP-UP TAX CALCULATION                                │
└─────────────────────────────────────────────────────────────────────────────┘

Step 1: Calculate Top-Up Tax Percentage
─────────────────────────────────────────
   Top-Up Tax % = 15% - Jurisdictional ETR

   Example: ETR = 10%
            Top-Up Tax % = 15% - 10% = 5%

Step 2: Calculate Excess Profit
────────────────────────────────
   Excess Profit = Net GloBE Income - SBIE

   Example: GloBE Income = €100,000,000
            SBIE         = €20,500,000
            Excess Profit = €79,500,000

Step 3: Calculate Top-Up Tax
────────────────────────────
   Top-Up Tax = Excess Profit × Top-Up Tax %

   Example: Top-Up Tax = €79,500,000 × 5% = €3,975,000

Step 4: Apply Additional Adjustments
─────────────────────────────────────
   (-) QDMTT paid (if any)
   (+) Additional Current Top-Up Tax (Art. 5.2.3)
   (-) Domestic Top-Up Tax offset

   Final Top-Up Tax = Adjusted amount
```

### Top-Up Tax Percentage

| Jurisdictional ETR | Top-Up Tax % | Notes |
|--------------------|--------------|-------|
| 15% or above | 0% | No Top-up Tax |
| 14% | 1% | Low top-up |
| 10% | 5% | Moderate top-up |
| 5% | 10% | Higher top-up |
| 0% | 15% | Maximum normal |
| -5% (negative) | 20% | Negative ETR scenario |

### Additional Current Top-Up Tax (Article 5.2.3)

Additional Current Top-Up Tax arises from:
- DTL recapture (5-year rule violation)
- Prior period adjustments
- Corrections to prior GloBE calculations

```
EXAMPLE: DTL Recapture Triggering Additional Top-Up Tax
─────────────────────────────────────────────────────────────────────────────

Year 1 (2024): DTL of €5,000,000 claimed in Adjusted Covered Taxes
               ETR calculated as 16% (no Top-up Tax)

Year 6 (2029): DTL has not reversed

Recapture Required:
  Remove €5,000,000 from Year 1 Adjusted Covered Taxes
  Recalculate Year 1 ETR → Now 13%
  Calculate Top-up Tax that would have been due
  Report as Additional Current Top-Up Tax in Year 6 GIR
```

### GIR Section 3.3 Data Elements

| Field | Description | Source |
|-------|-------------|--------|
| **Net GloBE Income** | Jurisdictional total | Section 3.1 |
| **SBIE** | Substance exclusion amount | Section 3.2 |
| **Excess Profit** | GloBE Income minus SBIE | Calculation |
| **Top-Up Tax Percentage** | 15% minus ETR | Calculation |
| **Jurisdictional Top-Up Tax** | Excess Profit × Top-Up % | Calculation |
| **QDMTT Amount** | QDMTT paid in jurisdiction | Local filing |
| **Additional Current Top-Up Tax** | Adjustments from prior periods | Recapture calculation |
| **Net Top-Up Tax** | Final amount due | Aggregation |

---

## 3.4.4 Top-Up Tax Allocation and Attribution

Once Top-up Tax is calculated for a low-taxed jurisdiction, it must be **allocated** to the appropriate charging mechanism and **attributed** to specific entities.

### Charging Mechanism Priority

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    TOP-UP TAX CHARGING PRIORITY                             │
└─────────────────────────────────────────────────────────────────────────────┘

Priority 1: QDMTT (Qualified Domestic Minimum Top-Up Tax)
───────────────────────────────────────────────────────────
   • Low-taxed jurisdiction collects Top-up Tax domestically
   • Reduces IIR/UTPR liability pound-for-pound
   • Must be "Qualified" per OECD standards

Priority 2: IIR (Income Inclusion Rule)
────────────────────────────────────────
   • UPE includes proportionate Top-up Tax in its income
   • "Top-down" approach: UPE first, then intermediate parents
   • Based on ownership percentage in low-taxed CE

Priority 3: UTPR (Undertaxed Profits Rule)
──────────────────────────────────────────
   • Backstop mechanism for residual Top-up Tax
   • Applies when IIR does not fully collect
   • Allocated by payroll and tangible asset formula
```

### IIR Allocation

The IIR is the **primary** charging mechanism and follows a "top-down" approach:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                       IIR ALLOCATION EXAMPLE                                │
└─────────────────────────────────────────────────────────────────────────────┘

Structure:
   GlobalCo plc (UK - UPE) ──100%──▶ UK Holdings Ltd ──80%──▶ Ireland Sub Ltd

Low-Taxed Jurisdiction: Ireland (ETR = 10%)
Top-Up Tax for Ireland: €1,000,000

IIR Allocation:
   UPE (GlobalCo plc) applies IIR
   Allocable Share = 100% × 80% = 80%
   IIR Top-Up Tax = €1,000,000 × 80% = €800,000

Result: GlobalCo plc includes €800,000 in UK tax base
```

### UTPR Allocation Formula

When UTPR applies, the Top-up Tax is allocated among UTPR jurisdictions using a **two-factor formula**:

```
                     (Employees in UTPR Jurisdiction / Total Employees)
UTPR Allocation = ─────────────────────────────────────────────────────── × 0.5
Key                        Total across all UTPR Jurisdictions

                     (Tangible Assets in UTPR Jurisdiction / Total Assets)
                 + ───────────────────────────────────────────────────── × 0.5
                         Total across all UTPR Jurisdictions
```

**UTPR Allocation Example:**

```
EXAMPLE: UTPR Allocation Across Three Jurisdictions
─────────────────────────────────────────────────────────────────────────────

UTPR Top-Up Tax to Allocate: €5,000,000

Jurisdiction Data:
                    Employees    Tangible Assets
   Germany:         1,000        €100,000,000
   France:          600          €60,000,000
   Netherlands:     400          €40,000,000
   ─────────────────────────────────────────────
   Total:           2,000        €200,000,000

UTPR Allocation Key:
   Germany:    (1,000/2,000 × 0.5) + (€100M/€200M × 0.5) = 0.25 + 0.25 = 0.50
   France:     (600/2,000 × 0.5) + (€60M/€200M × 0.5) = 0.15 + 0.15 = 0.30
   Netherlands:(400/2,000 × 0.5) + (€40M/€200M × 0.5) = 0.10 + 0.10 = 0.20

UTPR Allocation:
   Germany:     €5,000,000 × 0.50 = €2,500,000
   France:      €5,000,000 × 0.30 = €1,500,000
   Netherlands: €5,000,000 × 0.20 = €1,000,000
```

### QDMTT Credit Against IIR/UTPR

QDMTT reduces IIR and UTPR liability on a **pound-for-pound** basis:

```
EXAMPLE: QDMTT Credit
─────────────────────────────────────────────────────────────────────────────

Jurisdiction: Ireland
GloBE Top-Up Tax Calculated: €1,000,000
QDMTT Paid in Ireland:       €1,000,000

Effect:
   IIR Top-Up Tax = €1,000,000 - €1,000,000 = €0
   UTPR Top-Up Tax = €0

Result: No additional Top-up Tax due under IIR or UTPR
```

### GIR Section 3.4 Data Elements

| Field | Description | Source |
|-------|-------------|--------|
| **Jurisdiction with Taxing Rights** | Which jurisdiction collects | GloBE analysis |
| **QDMTT Amount** | Amount paid domestically | Local filing |
| **IIR Allocable Share** | Ownership-based allocation | Corporate structure |
| **IIR Top-Up Tax** | Amount allocated under IIR | Calculation |
| **UTPR Jurisdiction** | UTPR collecting jurisdictions | GloBE analysis |
| **UTPR Allocation Key** | Employee/asset formula | Calculation |
| **UTPR Top-Up Tax** | Amount allocated under UTPR | Calculation |

---

## January 2025 Updates to Section 3

The January 2025 OECD guidance provides several clarifications for Section 3:

| Update | Description |
|--------|-------------|
| **Restricted Tier 1 Capital** | New disclosures for banking sector |
| **GloBE Carrying Value Differences** | Additional disclosure for asset basis differences |
| **Investment Entities** | CE-by-CE reporting for investment entities |
| **Insurance Investment Entities** | Separate ETR computation required |
| **Sections 3.1.5-3.1.10** | Not required if only one taxing rights jurisdiction or QDMTT Safe Harbour applies |

---

## Complete ETR Computation Flowchart

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    COMPLETE GIR SECTION 3 WORKFLOW                          │
└─────────────────────────────────────────────────────────────────────────────┘

For Each Jurisdiction (Where Safe Harbour Does NOT Apply):
──────────────────────────────────────────────────────────

Step 1: Gather Entity-Level Data
─────────────────────────────────
    ├── FANIL for each CE
    ├── Current Tax Expense for each CE
    ├── Deferred Tax movements for each CE
    └── GloBE adjustment data for each CE
              │
              ▼
Step 2: Calculate GloBE Income per CE
─────────────────────────────────────
    ├── Apply Article 3.2 adjustments
    └── Calculate GloBE Income/Loss per CE
              │
              ▼
Step 3: Calculate Adjusted Covered Taxes per CE
───────────────────────────────────────────────
    ├── Apply Article 4.1 adjustments
    ├── Apply Article 4.4 deferred tax adjustments
    └── Apply 15% cap and recapture rules
              │
              ▼
Step 4: Aggregate to Jurisdictional Level
─────────────────────────────────────────
    ├── Sum GloBE Income of all CEs
    ├── Less: GloBE Losses of all CEs
    └── Sum Adjusted Covered Taxes of all CEs
              │
              ▼
Step 5: Calculate Jurisdictional ETR
────────────────────────────────────
    ├── ETR = Adjusted Covered Taxes / Net GloBE Income
    └── If Net GloBE Loss → STOP (no Top-up Tax)
              │
              ▼
Step 6: If ETR < 15%, Calculate SBIE
────────────────────────────────────
    ├── Calculate Payroll Carve-Out
    ├── Calculate Tangible Asset Carve-Out
    └── Total SBIE
              │
              ▼
Step 7: Calculate Top-Up Tax
────────────────────────────
    ├── Top-Up Tax % = 15% - ETR
    ├── Excess Profit = GloBE Income - SBIE
    ├── Top-Up Tax = Excess Profit × Top-Up Tax %
    └── Adjust for Additional Current Top-Up Tax
              │
              ▼
Step 8: Apply QDMTT Credit
─────────────────────────
    ├── Reduce Top-up Tax by QDMTT paid
    └── Remaining amount subject to IIR/UTPR
              │
              ▼
Step 9: Allocate Under IIR
─────────────────────────
    ├── Calculate allocable share per ownership
    └── Allocate to UPE (or intermediate parent)
              │
              ▼
Step 10: Allocate Residual Under UTPR
─────────────────────────────────────
    ├── Apply two-factor allocation key
    └── Allocate to UTPR jurisdictions
```

---

## Section 3 Completion Checklist

### Pre-Computation Verification

- [ ] Confirmed no safe harbour applies (Section 2 complete)
- [ ] All CEs in jurisdiction identified
- [ ] Financial data available for all CEs
- [ ] Tax provision data available for all CEs

### ETR Computation

- [ ] FANIL extracted from financial statements
- [ ] All Article 3.2 adjustments identified and applied
- [ ] Current tax expense extracted
- [ ] Deferred tax adjustments calculated
- [ ] 15% cap on DTL credits applied
- [ ] DTL recapture checked (5-year rule)
- [ ] Adjusted Covered Taxes aggregated at jurisdictional level
- [ ] Net GloBE Income calculated at jurisdictional level
- [ ] ETR calculated (rounded to 4 decimal places)

### SBIE Calculation

- [ ] Eligible payroll costs identified
- [ ] Correct payroll rate applied for fiscal year
- [ ] Tangible assets valued (average of opening/closing)
- [ ] Correct asset rate applied for fiscal year
- [ ] Total SBIE calculated

### Top-Up Tax Computation

- [ ] Top-up Tax percentage calculated (if ETR < 15%)
- [ ] Excess Profit calculated (GloBE Income - SBIE)
- [ ] Jurisdictional Top-up Tax calculated
- [ ] Additional Current Top-up Tax identified (if any)
- [ ] QDMTT credit applied (if applicable)

### Allocation

- [ ] QDMTT amount verified
- [ ] IIR allocable share calculated
- [ ] IIR Top-up Tax allocated to parent entity
- [ ] UTPR allocation key calculated (if applicable)
- [ ] UTPR amounts allocated to UTPR jurisdictions

---

## Common Errors in Section 3

| Error | Consequence | Prevention |
|-------|-------------|------------|
| **Wrong FANIL** | Incorrect GloBE Income | Reconcile to audited accounts |
| **Missing GloBE adjustments** | ETR incorrect | Use comprehensive adjustment checklist |
| **DTL recapture missed** | Understated Top-up Tax | Track DTL vintage by category |
| **Wrong SBIE rates** | Incorrect exclusion | Verify rates against fiscal year |
| **SBIE applied to losses** | Invalid calculation | Only apply SBIE to positive GloBE Income |
| **Wrong allocation ownership** | IIR misallocation | Verify ownership chain |
| **UTPR formula error** | Misallocation | Verify employee/asset data |
| **Double-counting QDMTT** | Understated liability | Reconcile QDMTT to local filings |

---

## Next Steps

Continue to the next sections:
- **Section 4:** Data Gathering and Extraction
- **Section 5:** GIR Completion Calculator - Sections 1-3

**Template References for This Section:**
- ETR Calculation Worksheet (Excel)
- SBIE Calculator (Excel)
- Top-Up Tax Calculator (Excel)
- Top-Up Tax Allocation Tool (Excel)

---

## Sources and References

This section incorporates information from:

- [oecdpillars.com - ETR Calculation and Top-Up Tax](https://oecdpillars.com/pillar-tab/etr-calculation-and-top-up-tax-2/)
- [oecdpillars.com - Substance-Based Income Exclusion](https://oecdpillars.com/pillar-tab/substance-based-income-exclusion/)
- [oecdpillars.com - Deferred Tax Recapture Rule](https://oecdpillars.com/pillar-tab/deferred-tax-recapture-rule/)
- [oecdpillars.com - Qualifying Domestic Minimum Top-Up Tax](https://oecdpillars.com/pillar-tab/qualifying-domestic-minimum-top-up-tax/)
- [oecdpillars.com - Pillar Two GloBE Adjustments](https://oecdpillars.com/pillar-tab/pillar-two-globe-adjustments/)
- [oecdpillars.com - A Review of Changes in the OECD's Updated January 2025 GloBE Information Return](https://oecdpillars.com/a-review-of-changes-in-the-oecds-updated-january-2025-globe-information-return/)
- [OECD - Pillar Two GloBE Rules Fact Sheets](https://www.oecd.org/content/dam/oecd/en/topics/policy-sub-issues/global-minimum-tax/pillar-two-globe-rules-fact-sheets.pdf)
- [OECD - FAQs on Model GloBE Rules](https://www.oecd.org/content/dam/oecd/en/topics/policy-sub-issues/global-minimum-tax/faqs-on-model-globe-rules.pdf)
- [KPMG - Pillar Two: GloBE Information Return](https://assets.kpmg.com/content/dam/kpmg/xx/pdf/2023/07/pillar-two-globe-information-return.pdf)
- [EY - OECD/G20 Inclusive Framework releases document on Pillar Two GloBE Information Return](https://www.ey.com/en_gl/technical/tax-alerts/oecd-g20-inclusive-framework-releases-document-on-pillar-two-glo)
- [Forvis Mazars - Computation of GloBE Adjustments](https://www.forvismazars.us/getattachment/aa97a12a-cd63-4758-8cac-6df9e744f32b/P2TS_5_Computation-of-GloBE-Adjustments.pdf)
- [McDermott Will & Emery - An Overview of OECD Pillar 2](https://www.mwe.com/insights/an-overview-of-oecd-pillar-2/)
- [BDO UK - Pillar Two: How it works](https://www.bdo.co.uk/en-gb/insights/tax/corporate-international-tax/pillar-two-how-it-will-work)
- [MHA - GloBE Model Rules (Pillar 2) – Deferred Tax Requirements](https://www.mha.co.uk/insights/globe-model-rules-pillar-2-deferred-tax-requirements)
- [Wolters Kluwer - Overcoming challenges in preparing GloBE Information Return](https://www.wolterskluwer.com/en-au/expert-insights/overcoming-challenges-in-preparing-for-beps-pillar-two)

---

*End of Section 3.4*
