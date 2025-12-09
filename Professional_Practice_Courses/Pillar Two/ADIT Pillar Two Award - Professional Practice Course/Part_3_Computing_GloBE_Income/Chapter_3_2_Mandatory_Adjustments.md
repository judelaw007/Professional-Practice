# Chapter 3.2: Mandatory Adjustments

## Learning Objective

After completing this chapter, you will be able to identify and apply all mandatory adjustments required to convert Financial Accounting Net Income or Loss into GloBE Income or Loss.

---

## Overview of Article 3.2 Adjustments

Article 3.2 requires specific adjustments to Financial Accounting Net Income or Loss. These adjustments eliminate common book-to-tax differences where policy justification exists.

### Complete List of Mandatory Adjustments

| Reference | Adjustment | Direction |
|-----------|------------|-----------|
| Art. 3.2.1(a) | Net Taxes Expense | Add back |
| Art. 3.2.1(b) | Excluded Dividends | Exclude (deduct) |
| Art. 3.2.1(c) | Excluded Equity Gain or Loss | Exclude |
| Art. 3.2.1(d) | Included Revaluation Method Gain or Loss | Include (add) |
| Art. 3.2.1(e) | Gains/losses from dispositions under Article 6.3 | Exclude |
| Art. 3.2.1(f) | Asymmetric Foreign Currency Gains or Losses | Adjust |
| Art. 3.2.1(g) | Policy Disallowed Expenses | Add back |
| Art. 3.2.1(h) | Prior Period Errors and Changes in Accounting Principles | Adjust |
| Art. 3.2.1(i) | Accrued Pension Expense | Adjust |
| Art. 3.2.2 | Stock-Based Compensation (elective) | Substitute |

---

## Adjustment 1: Net Taxes Expense *(Article 3.2.1(a))*

### The Rule

The net tax expense recorded in the financial accounts must be **added back** to Financial Accounting Net Income.

### Why This Adjustment Exists

Financial Accounting Net Income is an "after-tax" figure (below the line). Since GloBE Income feeds into an ETR calculation that divides Adjusted Covered Taxes by GloBE Income, the tax expense must be removed to create a "pre-tax" base.

### What to Add Back

| Include in Add-Back | Exclude from Add-Back |
|--------------------|----------------------|
| Current tax expense | Deferred tax adjustments (separate treatment) |
| Foreign taxes | Non-income taxes (VAT, customs, payroll) |
| Withholding taxes suffered | Property taxes |
| Tax provisions/accruals | |

### Worked Example

**SG Germany GmbH — FY 2025**

| Item | Amount (€) |
|------|------------|
| Financial Accounting Net Income | 4,900,000 |
| Tax expense per accounts | 2,100,000 |
| **Add back:** Net Taxes Expense | +2,100,000 |
| **Adjusted amount** | 7,000,000 |

---

## Adjustment 2: Excluded Dividends *(Article 3.2.1(b))*

### The Rule

Dividends and similar distributions are **excluded** from GloBE Income unless they are from "short-term portfolio shareholdings."

### Definition of Excluded Dividend

A dividend is **excluded** if EITHER:

| Condition | Threshold |
|-----------|-----------|
| **Ownership test** | MNE Group holds ≥10% of profits, capital, reserves, or voting rights |
| **Holding period test** | Ownership held for ≥12 months at dividend date |

### Portfolio Shareholding (Not Excluded)

A **Portfolio Shareholding** exists when:
- Ownership <10%, AND
- Held for <12 months

Dividends from Portfolio Shareholdings remain in GloBE Income.

### Decision Tree: Dividend Treatment

```
Dividend received
        │
        ▼
┌───────────────────────┐
│ Ownership ≥10%?       │
└───────────────────────┘
        │
   ┌────┴────┐
  YES       NO
   │         │
   ▼         ▼
EXCLUDED   ┌───────────────────┐
           │ Held ≥12 months?  │
           └───────────────────┘
                    │
              ┌─────┴─────┐
             YES         NO
              │           │
              ▼           ▼
           EXCLUDED    INCLUDED
           (long-term  (portfolio)
            portfolio)
```

### Worked Example

**SG Netherlands BV — Dividend Analysis**

| Dividend Source | Ownership | Holding Period | Treatment |
|-----------------|-----------|----------------|-----------|
| SG Ireland Ltd | 60% | >12 months | **Excluded** |
| Listed Co. A | 2% | 3 years | **Excluded** (long-term portfolio) |
| Listed Co. B | 5% | 6 months | **Included** (short-term portfolio) |
| Listed Co. C | 12% | 2 months | **Excluded** (≥10% ownership) |

**Calculation:**

| Item | Amount (€) |
|------|------------|
| Total dividends received | 3,500,000 |
| Less: Excluded dividends (Ireland) | (2,800,000) |
| Less: Excluded dividends (Listed Co. A) | (400,000) |
| Less: Excluded dividends (Listed Co. C) | (150,000) |
| **Dividends remaining in GloBE Income** | **150,000** |

### Portfolio Shareholding Election

An MNE Group may elect to **include** all Portfolio Shareholding dividends in GloBE Income *(Administrative Guidance, Article 3.5)*. This is a **Five-Year Election** that simplifies compliance by avoiding the need to track holding periods.

**When to consider this election:**
- High volume of portfolio investments
- Administrative burden of tracking holding periods exceeds tax benefit
- Portfolio dividends are minimal relative to total income

---

## Adjustment 3: Excluded Equity Gain or Loss *(Article 3.2.1(c))*

### The Rule

Certain gains and losses related to equity investments are **excluded** from GloBE Income.

### Three Types of Excluded Equity Items

| Type | Description | Reference |
|------|-------------|-----------|
| **Fair value changes** | Gains/losses from changes in fair value of Ownership Interests (except Portfolio Shareholdings) | Art. 3.2.1(c)(i) |
| **Equity method P&L** | Profit or loss from Ownership Interests accounted for under equity method | Art. 3.2.1(c)(ii) |
| **Disposal gains/losses** | Gains/losses from disposition of Ownership Interests (except Portfolio Shareholdings) | Art. 3.2.1(c)(iii) |

### Portfolio Shareholding Exception

For **Portfolio Shareholdings** (<10% ownership AND held <12 months):
- Fair value changes: **Included** in GloBE Income
- Disposal gains/losses: **Included** in GloBE Income

### Worked Example

**SG Holdings Ltd — Equity Items**

| Item | Amount (€) | Treatment |
|------|------------|-----------|
| Fair value gain on SG Netherlands shares | 1,200,000 | **Excluded** (subsidiary) |
| Share of SG Japan profit (equity method) | 850,000 | **Excluded** (equity method) |
| Gain on sale of 5% stake in TechCo (held 8 months) | 320,000 | **Included** (portfolio) |
| Loss on sale of 15% stake in StartupCo | (180,000) | **Excluded** (≥10%) |

**Net adjustment:**

| Item | Amount (€) |
|------|------------|
| Total equity items per accounts | 2,190,000 |
| Less: Excluded fair value gain | (1,200,000) |
| Less: Excluded equity method profit | (850,000) |
| Add back: Excluded disposal loss | 180,000 |
| **Net equity items in GloBE Income** | **320,000** |

### Equity Investment Inclusion Election

An MNE Group may elect to **include** all excluded equity gains/losses in GloBE Income. This is a **Five-Year Election** available on a per-jurisdiction basis.

**When to consider:**
- Simplifies tracking when equity items are immaterial
- May be beneficial if losses exceed gains

---

## Adjustment 4: Included Revaluation Method Gain or Loss *(Article 3.2.1(d))*

### The Rule

Gains and losses from revaluation of property, plant and equipment (PPE) that are recognised in **Other Comprehensive Income (OCI)** under the revaluation model must be **included** in GloBE Income.

### Why This Adjustment Exists

Under IAS 16, entities may choose the revaluation model for PPE, with gains going to OCI (not P&L). Without this adjustment, such gains would escape the GloBE Income calculation entirely.

### What Gets Included

| Item | In P&L? | In OCI? | GloBE Treatment |
|------|---------|---------|-----------------|
| Revaluation gain on PPE | No | Yes | **Include** in GloBE Income |
| Revaluation loss on PPE | Sometimes | Sometimes | **Include** if in OCI |
| Associated deferred tax | — | — | Included in Covered Taxes |

### Worked Example

**SG Australia Pty Ltd — PPE Revaluation**

| Item | Amount (A$) |
|------|-------------|
| Revaluation surplus on factory (in OCI) | 2,500,000 |
| Deferred tax liability recognised | 750,000 |

**GloBE adjustment:**
- Include revaluation gain of A$2,500,000 in GloBE Income
- Include deferred tax of A$750,000 in Adjusted Covered Taxes

### Realization Method Election *(Article 3.2.5)*

An MNE may elect to use the **realization method** instead of fair value accounting for GloBE purposes. Under this election:

- Fair value gains/losses are **excluded** until asset disposal
- Gain/loss crystallises only on actual disposition

This is a **Five-Year Election** applicable to:
- All assets and liabilities, OR
- Only tangible assets, OR
- Only Investment Entities

**Benefit:** Reduces ETR volatility from unrealised gains/losses.

---

## Adjustment 5: Gains/Losses from Article 6.3 Dispositions *(Article 3.2.1(e))*

### The Rule

Gains and losses from **intra-group asset dispositions** covered by Article 6.3 are **excluded** from GloBE Income.

### What Article 6.3 Covers

Article 6.3 provides rules for reorganisations and asset transfers within an MNE Group, including:

- Asset transfers at book value (no gain/loss recognition)
- Carryover of tax attributes
- Certain corporate reorganisations

### Practical Application

For most practitioners, this adjustment applies when:

| Transaction | Treatment |
|-------------|-----------|
| Intra-group asset sale at arm's length price | Gain/loss recognised normally (not Art. 6.3) |
| Intra-group asset transfer at book value (qualifying reorganisation) | Gain/loss **excluded** under Art. 3.2.1(e) |

---

## Adjustment 6: Asymmetric Foreign Currency Gains or Losses *(Article 3.2.1(f))*

### The Rule

Adjustments are required when **accounting functional currency** differs from **tax functional currency**, creating asymmetric foreign exchange gains or losses.

### When Asymmetric FX Arises

| Scenario | Example |
|----------|---------|
| Accounting in USD, tax returns in EUR | Transaction in GBP creates FX gain in USD accounts but different (or no) FX gain for tax |
| Functional currency mismatch | US subsidiary of UK parent with EUR tax filings |

### Three Scenarios

| Situation | GloBE Treatment |
|-----------|-----------------|
| Transaction in **accounting currency** creates taxable FX gain (tax currency different) | **Include** the FX gain in GloBE Income |
| Transaction in **tax currency** creates accounting FX gain | **Exclude** the accounting FX gain |
| Transaction in **third currency** creates accounting FX gain | **Exclude** the accounting FX gain |

### Worked Example

**SG Singapore Pte Ltd**
- Accounting functional currency: SGD
- Tax functional currency: SGD (no mismatch)
- **Result:** No asymmetric FX adjustment required

**TechStart US Inc**
- Accounting functional currency: USD (follows US parent)
- Tax functional currency: USD
- **Result:** No asymmetric FX adjustment required

**Note:** Asymmetric FX adjustments are uncommon for entities where accounting and tax functional currencies align.

---

## Adjustment 7: Policy Disallowed Expenses *(Article 3.2.1(g))*

### The Rule

Certain expenses are **added back** to GloBE Income because they are disallowed on policy grounds.

### What Gets Added Back

| Expense Type | Threshold | Treatment |
|--------------|-----------|-----------|
| **Bribes and illegal payments** | Any amount | **Add back** |
| **Fines and penalties** | ≥€50,000 | **Add back** |
| **Fines and penalties** | <€50,000 | No adjustment |

### What Is NOT a Fine or Penalty

| Item | Treatment |
|------|-----------|
| Interest on late tax payment | **Not** a fine—no add-back |
| Compensatory damages | **Not** a penalty—no add-back |
| Contractual penalties (e.g., late delivery) | **Not** policy disallowed—no add-back |

### Worked Example

**SG Germany GmbH — Policy Disallowed Expenses**

| Item | Amount (€) | Treatment |
|------|------------|-----------|
| Environmental fine (regulatory) | 180,000 | **Add back** (≥€50K) |
| Late filing penalty | 25,000 | No adjustment (<€50K) |
| Interest on late tax payment | 45,000 | No adjustment (not a fine) |
| Contractual penalty to customer | 120,000 | No adjustment (commercial) |

**Net adjustment:** Add back €180,000

---

## Adjustment 8: Prior Period Errors and Changes in Accounting Principles *(Article 3.2.1(h))*

### The Rule

Adjustments are required for:
- **Prior period errors** affecting current year opening balances
- **Changes in accounting principles** with retrospective application

### Treatment of Prior Period Errors

| Situation | GloBE Treatment |
|-----------|-----------------|
| Error in prior year GloBE Income | Recalculate prior year ETR and Top-Up Tax |
| Error affects only current year accounts | Adjust current year GloBE Income |
| Error creates Additional Top-Up Tax | Include in current year per Art. 5.4.1 |

### Treatment of Accounting Policy Changes

| Change Type | Treatment |
|-------------|-----------|
| Retrospective restatement | Apply same change to GloBE Income |
| Prospective application | No adjustment to prior periods |

### Worked Example

**SG France SAS — Prior Period Error**

In FY 2025, Stratos discovered that SG France SAS had overstated revenue by €500,000 in FY 2024 due to a cut-off error.

**Step 1:** Restate FY 2024 GloBE Income
- Original GloBE Income: €8,200,000
- Corrected GloBE Income: €7,700,000

**Step 2:** Recalculate FY 2024 ETR
- Original ETR: 14.2%
- Corrected ETR: 15.1%

**Step 3:** Determine impact
- Original Top-Up Tax: €48,000
- Corrected Top-Up Tax: €0 (ETR now above 15%)

**Step 4:** Adjustment in FY 2025
- Reduce GloBE Income by €500,000 (remove overstatement)
- No additional Top-Up Tax from FY 2024 correction

---

## Adjustment 9: Accrued Pension Expense *(Article 3.2.1(i))*

### The Rule

Adjust Financial Accounting Net Income for the difference between:
- **Pension expense** recorded in accounts (accrual basis), and
- **Contributions** actually paid to the pension fund

### Formula

```
Accrued Pension Expense Adjustment = Pension Expense (Accounts) − Contributions Paid
```

If positive (accrual > contribution): **Deduct** from GloBE Income
If negative (contribution > accrual): **Add** to GloBE Income

### Why This Adjustment Exists

- Aligns GloBE Income timing with tax deduction timing
- Most jurisdictions allow deduction when contributions are **paid**, not when expense is **accrued**
- Defined benefit accounting (IAS 19) can create significant accruals not reflecting cash

### Worked Example

**SG UK Holdings Ltd — Pension Adjustment**

| Item | Amount (£) |
|------|------------|
| Defined benefit pension expense (per IAS 19) | 2,400,000 |
| Cash contributions paid to pension scheme | 1,800,000 |
| **Accrued Pension Expense** | **600,000** |

**GloBE adjustment:** Deduct £600,000 from GloBE Income

**Effect:** GloBE Income reflects the £1,800,000 actually contributed, not the £2,400,000 accounting expense.

### Scope Clarification

| Payment Type | In Scope? |
|--------------|-----------|
| Contributions to external pension fund | **Yes** |
| Contributions to in-house pension fund | **Yes** |
| Direct payments to employees/retirees | **No** (not within Art. 3.2.1(i)) |

---

## Adjustment 10: Stock-Based Compensation *(Article 3.2.2)* — Elective

### The Rule

An MNE may **elect** to substitute the tax-deductible amount of stock-based compensation (SBC) for the accounting expense.

### Default vs Elected Treatment

| Approach | Amount Used for GloBE Income |
|----------|------------------------------|
| **Default** (no election) | Accounting expense (e.g., IFRS 2) |
| **Elected** | Tax-deductible amount |

### Why This Election Exists

SBC often creates book-to-tax timing differences:
- **Accounting:** Expense recognised over vesting period
- **Tax:** Deduction at exercise/vesting (often larger due to share price increase)

Without the election, these timing differences could create artificial Top-Up Tax.

### Election Mechanics

- **Irrevocable** election
- Applies to **all** SBC for the Constituent Entity
- If options expire unexercised: previously deducted amounts must be added back to GloBE Income

### Worked Example

**SG Singapore Tech Pte Ltd — SBC Election Analysis**

| Item | Without Election | With Election |
|------|------------------|---------------|
| SBC accounting expense (IFRS 2) | €850,000 | — |
| SBC tax deduction (local tax) | — | €620,000 |
| **GloBE Income impact** | Expense €850,000 | Expense €620,000 |

**Analysis:**
- Without election: Higher SBC expense reduces GloBE Income
- With election: Lower tax deduction increases GloBE Income

**Decision:** If the jurisdiction is low-taxed, a **higher** GloBE Income increases Top-Up Tax. Therefore:
- In **low-tax jurisdictions**: Consider NOT electing (keep higher accounting expense)
- In **high-tax jurisdictions**: Election may be neutral or beneficial

---

## Complete Adjustment Checklist

Use this checklist for each Constituent Entity:

### Mandatory Adjustments

| # | Adjustment | Add/Deduct | Amount (€) | Done? |
|---|------------|------------|------------|-------|
| 1 | Net Taxes Expense | Add back | | ☐ |
| 2 | Excluded Dividends (≥10% or ≥12 months) | Deduct | | ☐ |
| 3a | Fair value gains on ownership interests (excl. portfolio) | Deduct | | ☐ |
| 3b | Equity method profit/loss | Deduct | | ☐ |
| 3c | Disposal gains/losses on ownership interests (excl. portfolio) | Deduct | | ☐ |
| 4 | Revaluation gains/losses in OCI (PPE) | Add | | ☐ |
| 5 | Gains/losses from Article 6.3 dispositions | Deduct | | ☐ |
| 6 | Asymmetric FX gains/losses | Adjust | | ☐ |
| 7a | Bribes/illegal payments | Add back | | ☐ |
| 7b | Fines/penalties ≥€50,000 | Add back | | ☐ |
| 8 | Prior period errors/accounting changes | Adjust | | ☐ |
| 9 | Accrued pension expense | Adjust | | ☐ |

### Elective Adjustments (Document if Applied)

| # | Election | Applied? | Amount (€) |
|---|----------|----------|------------|
| A | Stock-based compensation (Art. 3.2.2) | Yes/No | |
| B | Portfolio shareholding inclusion (AG 3.5) | Yes/No | |
| C | Equity investment inclusion | Yes/No | |
| D | Realization method (Art. 3.2.5) | Yes/No | |

---

## Stratos Worked Example: Complete Adjustment Calculation

**SG Germany GmbH — FY 2025 GloBE Income Calculation**

### Starting Point

| Item | Reference | Amount (€) |
|------|-----------|------------|
| **Financial Accounting Net Income** | Chapter 3.1 | **4,900,000** |

### Adjustments

| # | Adjustment | Calculation | Amount (€) |
|---|------------|-------------|------------|
| 1 | Net Taxes Expense | Current tax + deferred tax | +2,100,000 |
| 2 | Excluded Dividends | Dividend from SG France (100% sub) | (450,000) |
| 3a | Fair value gains | None | — |
| 3b | Equity method | None | — |
| 3c | Disposal gains | None | — |
| 4 | Revaluation OCI | None | — |
| 5 | Article 6.3 | None | — |
| 6 | Asymmetric FX | Functional currencies aligned | — |
| 7a | Bribes | None | — |
| 7b | Fines ≥€50K | Environmental fine | +180,000 |
| 8 | Prior period | None | — |
| 9 | Pension | Accrual €320K, contribution €280K | (40,000) |

### Subtotal Before Elections

| Item | Amount (€) |
|------|------------|
| Financial Accounting Net Income | 4,900,000 |
| Add: Net Taxes Expense | 2,100,000 |
| Less: Excluded Dividends | (450,000) |
| Add: Policy Disallowed (fine) | 180,000 |
| Less: Pension Adjustment | (40,000) |
| **GloBE Income (before elections)** | **6,690,000** |

### Election Analysis

**Stock-Based Compensation:**
- Accounting expense: €95,000
- Tax deduction: €110,000
- Germany ETR expected: ~28% (above minimum)
- **Decision:** No election needed (jurisdiction is high-tax)

### Final GloBE Income

| Item | Amount (€) |
|------|------------|
| **GloBE Income** | **6,690,000** |

---

## Common Pitfalls

### Pitfall 1: Forgetting to Add Back Tax Expense

**Error:** Using Financial Accounting Net Income directly without adding back tax expense.

**Impact:** GloBE Income is understated, artificially inflating ETR.

### Pitfall 2: Excluding All Dividends

**Error:** Excluding dividends from a 5% shareholding held for 6 months.

**Correct:** This is a Portfolio Shareholding—dividends are **included** in GloBE Income.

### Pitfall 3: Missing the €50,000 Threshold for Fines

**Error:** Adding back a €30,000 regulatory fine.

**Correct:** Fines below €50,000 are **not** added back.

### Pitfall 4: Ignoring Pension Adjustment Direction

**Error:** Always deducting the pension adjustment.

**Correct:** If contributions **exceed** accrual, the adjustment **increases** GloBE Income.

### Pitfall 5: Applying SBC Election Without Analysis

**Error:** Automatically electing SBC substitution.

**Correct:** In low-tax jurisdictions, the higher accounting expense may be preferable to reduce Top-Up Tax.

---

## Key References

**OECD GloBE Model Rules:**
- Article 3.2.1(a)-(i) — Mandatory adjustments
- Article 3.2.2 — Stock-based compensation election
- Article 3.2.5 — Realization method election

**Administrative Guidance:**
- February 2023: Pension expense clarification
- July 2023: Asymmetric FX guidance
- December 2023: Portfolio shareholding election

**OECD Commentary:**
- Chapter 3, paragraphs 26-120 — Detailed adjustment guidance

---

## Summary

Article 3.2 requires nine mandatory adjustments to Financial Accounting Net Income:

| Category | Adjustments |
|----------|-------------|
| **Add back** | Net taxes, policy disallowed expenses |
| **Exclude** | Dividends (qualifying), equity gains/losses, Art. 6.3 dispositions |
| **Include** | Revaluation gains in OCI |
| **Adjust** | Asymmetric FX, prior period errors, pension accruals |

Plus optional elections for:
- Stock-based compensation
- Portfolio shareholding inclusion
- Equity investment inclusion
- Realization method

The adjustment checklist ensures systematic application across all Constituent Entities.

---

## Next Step

You have learned the mandatory adjustments to Financial Accounting Net Income. Proceed to **Chapter 3.3: Stock-Based Compensation Election** for detailed guidance on when and how to make this important election.
