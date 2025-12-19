# Chapter 4.1: Defining Covered Taxes

## Learning Objective

This chapter provides a practical framework for identifying which taxes qualify as "Covered Taxes" for GloBE purposes. The correct classification of taxes directly impacts the ETR numerator—include a non-qualifying tax and you overstate coverage; exclude a qualifying tax and you understate it. Both errors lead to incorrect top-up tax calculations.

## Introduction

The effective tax rate calculation that lies at the heart of Pillar Two requires two inputs: GloBE Income in the denominator and Covered Taxes in the numerator. While Part 3 addressed how to compute GloBE Income, this chapter tackles the equally important question of which taxes count toward meeting the 15% minimum. The answer is not as straightforward as it might seem. Countries impose a bewildering variety of levies—corporate income taxes, withholding taxes, turnover taxes, property taxes, digital services taxes, tonnage taxes, and countless others. Some clearly measure the taxation of corporate profits; others do not. Some substitute for income taxes; others exist alongside them. The GloBE framework must draw principled lines, crediting taxes that genuinely represent taxation of corporate income while excluding levies that serve other purposes. The four-category structure of Article 4.2.1 provides this architecture, distinguishing taxes on income, distribution taxes under special regimes, taxes imposed in lieu of corporate income tax, and taxes on retained earnings. Understanding these categories—and the exclusions that accompany them—is essential for accurate ETR computation.

## 1. The Starting Point: Current Tax Expense

The Covered Taxes analysis begins with the current tax expense recorded in financial accounts (Article 4.1.1). This is the same financial accounting starting point used for GloBE Income under Article 3.1.

**Practical implication:** Use the same set of accounts for both GloBE Income and Covered Taxes. If you use IFRS consolidated accounts to derive GloBE Income, use the same IFRS accounts for the current tax expense figure.

## 2. The Four Categories of Covered Taxes

Article 4.2.1 defines four categories of taxes that qualify as Covered Taxes. Each serves a specific purpose in ensuring the ETR calculation captures genuine income taxation.

### 2.1 Category 1: Taxes on Income or Profits (Article 4.2.1(a))

The primary category—taxes recorded in financial accounts with respect to:
- The Constituent Entity's own income or profits
- Its share of income or profits of entities in which it holds an Ownership Interest

**What this captures:**
| Tax Type | Example | Treatment |
|----------|---------|-----------|
| Corporate income tax | German CIT at 15% | Covered Tax |
| Trade tax on income | German Gewerbesteuer | Covered Tax |
| Federal/state income taxes | US federal + state CIT | Covered Tax |
| CFC inclusions | UK CFC charge | Covered Tax (allocated to CE) |
| Partnership allocations | Share of partnership tax | Covered Tax |

**Classification test:**
```
Step 1: Is the tax recorded in financial accounts?
        → If NO: Not a Covered Tax (unless adjustment applies under Article 4.1.2)

Step 2: Is it levied on income, profits, or a share thereof?
        → If YES: Category 1 Covered Tax
        → If NO: Proceed to Categories 2-4
```

### 2.2 Category 2: Eligible Distribution Tax System (Article 4.2.1(b))

Taxes on distributed profits, deemed profit distributions, and non-business expenses under an Eligible Distribution Tax System (EDTS).

**What qualifies as an EDTS:** A corporate tax system that:
- Imposes no (or minimal) tax on retained profits
- Taxes profits only upon distribution to shareholders

**Jurisdictions using EDTS:**
- Estonia (20% on distributions, 0% on retained)
- Latvia (similar structure)

**Special treatment under Article 7.3:** EDTS jurisdictions receive deemed distribution recognition—tax expected to be paid within four years can be counted toward current-year Covered Taxes.

**Stratos implication:** Stratos has no entities in EDTS jurisdictions. If it established an Estonian subsidiary, it would need to:
1. Project distributions over the four-year window
2. Calculate deemed covered taxes based on expected distribution timing
3. Track actual distributions against projections

### 2.3 Category 3: Taxes Imposed in Lieu of CIT (Article 4.2.1(c))

Taxes substituting for a generally applicable corporate income tax—typically levied on gross amounts where a net income tax would otherwise apply.

**Common examples:**
| Tax | Jurisdiction | Why It Qualifies |
|-----|--------------|------------------|
| Withholding tax on interest | Various | Substitutes for taxing net interest income |
| Withholding tax on royalties | Various | Substitutes for taxing net royalty income |
| Withholding tax on rent | Various | Substitutes for taxing net rental income |
| State premium taxes | US states | Imposed on insurers in lieu of state CIT |

**Classification test:**
```
Is the gross-basis tax imposed INSTEAD OF a net income tax?
→ If YES: Covered Tax (Category 3)
→ If NO: Not a Covered Tax (likely indirect tax)
```

**What does NOT qualify:**
- Digital services taxes (not imposed "in lieu" of CIT)
- Turnover taxes (not substituting for income tax)
- Transaction taxes (capital transfer, stamp duty)

### 2.4 Category 4: Taxes on Retained Earnings and Equity (Article 4.2.1(d))

Taxes levied by reference to retained earnings or corporate equity, including multi-component taxes based on income and equity.

**Examples:**
- Swiss cantonal capital taxes (where income is a component)
- Certain net worth taxes with income elements
- Minimum taxes calculated on equity where alternative to income tax

**Classification criteria:**
- Must have income or retained earnings as a measurement component
- Pure property or wealth taxes on assets (not equity) do not qualify

The four-category structure reflects a deliberate policy choice to credit taxes that genuinely measure the taxation of corporate profits—whether imposed directly on net income, upon distribution of profits, as a substitute for net income taxation, or on accumulated earnings that represent undistributed profits. The common thread is that each category captures a levy whose base relates to what the company earns, not what it owns, sells, or consumes. This distinction matters because the 15% minimum rate is conceived as a floor on income taxation specifically. Crediting unrelated levies—however substantial—would undermine the framework's coherence. A company paying heavy property taxes but minimal income taxes is not meeting the policy objective, even if its total tax burden is significant.

## 3. What is NOT a Covered Tax

Equally important is knowing what to exclude. The following are explicitly non-qualifying:

### 3.1 Excluded by Nature

| Tax Type | Why Excluded |
|----------|--------------|
| **VAT/GST** | Indirect tax on consumption, not income |
| **Customs duties** | Indirect tax on imports |
| **Payroll taxes** | Tax on employment, not corporate income |
| **Property taxes** | Tax on real estate ownership |
| **Stamp duties** | Transaction tax |
| **Excise duties** | Tax on specific goods |
| **Environmental levies** | Behaviour-based tax |
| **Digital services taxes** | Turnover-based, not "in lieu" of CIT |

### 3.2 Excluded by Article 4.2.2

Two specific exclusions regardless of nature:

1. **Top-Up Tax under Qualified IIR** (Article 4.2.2(a))
   - A parent's IIR liability on low-taxed subsidiaries is NOT a Covered Tax
   - Reason: Including it would create circular calculation

2. **Top-Up Tax under Qualified DMTT** (Article 4.2.2(b))
   - A CE's domestic minimum top-up tax is NOT a Covered Tax
   - Reason: QDMTT eliminates IIR/UTPR liability directly; it's not part of ETR calculation

**Practical consequence:**
If a jurisdiction imposes a *non-qualifying* domestic minimum tax (NDMTT), that tax IS included as a Covered Tax. However, this only increases the ETR numerator—it does not provide the QDMTT "switch-off" benefit.

## 4. Qualified Refundable Tax Credits: Special Treatment

Qualified Refundable Tax Credits (QRTCs) receive preferential treatment under GloBE—they are treated as **income** rather than as a reduction of Covered Taxes (Article 3.2.10).

### 4.1 Definition (Article 10.1)

A QRTC is a refundable tax credit that:
1. Is payable as cash or cash equivalent within **four years** of satisfying conditions
2. Is not limited to reducing Covered Tax liability only

### 4.2 Why This Matters: ETR Impact

The classification dramatically affects ETR:

**Example: CE with €1,000 GloBE Income, €200 pre-credit tax, €100 tax credit**

| Credit Type | Calculation | ETR |
|-------------|-------------|-----|
| **QRTC** (treated as income) | €200 ÷ (€1,000 + €100) = 200/1,100 | **18.2%** |
| **Non-QRTC** (reduces Covered Taxes) | (€200 - €100) ÷ €1,000 = 100/1,000 | **10.0%** |

The QRTC treatment results in **8.2 percentage points higher ETR**—potentially eliminating top-up tax exposure entirely.

### 4.3 Verification Checklist: Does Credit Qualify as QRTC?

| Question | Required Answer |
|----------|-----------------|
| Is the credit refundable as cash? | Yes |
| Is refund available within 4 years? | Yes |
| Can it be used to settle non-tax liabilities? | Yes |
| Is the refund amount limited to tax liability? | No |

If all conditions are met → QRTC → Treat as GloBE Income, not reduction of Covered Taxes

The QRTC distinction illustrates a nuanced policy choice within the GloBE framework. Refundable credits that can be converted to cash within four years are economically equivalent to government grants—the company receives value regardless of its tax liability. Treating such credits as income rather than as reductions in tax ensures they increase the ETR denominator rather than decrease the numerator, producing a higher ETR and reducing top-up tax exposure. This favourable treatment reflects recognition that refundable credits represent genuine support for activities like R&D, not tax gaming. By contrast, non-refundable credits merely reduce taxes otherwise payable—they provide no benefit if the company has insufficient tax liability. Treating them as reductions in Covered Taxes accurately reflects their economic effect. The four-year refundability window prevents jurisdictions from structuring credits to technically qualify as refundable while making actual refunds practically unavailable.

## 5. CFC Regime Taxes and Attribution

Taxes paid under CFC regimes by a parent entity require special allocation treatment.

### 5.1 The Issue

When Country A imposes CFC tax on Parent Co for the undistributed profits of Sub Co in Country B:
- Parent Co records the CFC tax in its financial accounts
- But the income generating the tax is Sub Co's income

### 5.2 The Solution: Push-Down (Article 4.3.2(c))

CFC taxes are **pushed down** from the parent to the subsidiary:

```
Parent Co (Country A)
├── Pays CFC tax: €300,000
├── CFC tax in Parent's accounts: €300,000
│
└── Sub Co (Country B)
    ├── Income triggering CFC: €2,000,000
    ├── Sub's own tax: €50,000
    └── PUSH-DOWN CFC tax: +€300,000
        → Sub's Adjusted Covered Taxes: €350,000
```

**Result:** The €300,000 CFC tax is:
- **Removed** from Parent Co's Covered Taxes
- **Added** to Sub Co's Covered Taxes

This ensures the tax is counted against the income that generated it.

## 6. Covered Tax Classification Checklist

Use this checklist for each tax line in financial accounts:

### 6.1 Step 1: Identify All Tax Lines

Extract from financial accounts:
- [ ] Current income tax expense (P&L)
- [ ] Taxes recorded in equity
- [ ] Taxes recorded in OCI
- [ ] Withholding taxes suffered
- [ ] CFC charges paid
- [ ] Uncertain tax position provisions

### 6.2 Step 2: Apply Four-Category Test

For each tax line:

| # | Question | If YES → |
|---|----------|----------|
| 1 | Tax on own income/profits? | Category 1 ✓ |
| 2 | Tax on share of CE's income (CFC, partnership)? | Category 1 ✓ |
| 3 | Distribution tax under EDTS? | Category 2 ✓ |
| 4 | Gross-basis tax in lieu of CIT? | Category 3 ✓ |
| 5 | Tax on retained earnings/equity? | Category 4 ✓ |
| 6 | None of the above? | **NOT Covered Tax** |

### 6.3 Step 3: Apply Exclusions

| # | Check | If YES → |
|---|-------|----------|
| 1 | Is it IIR Top-Up Tax? | Exclude |
| 2 | Is it QDMTT? | Exclude |
| 3 | Is it indirect tax (VAT, GST)? | Exclude |
| 4 | Is it payroll tax? | Exclude |
| 5 | Is it property tax? | Exclude |

### 6.4 Step 4: Special Classifications

| # | Item | Treatment |
|---|------|-----------|
| 1 | QRTC recorded as tax reduction? | Reverse—treat credit as income |
| 2 | CFC tax in parent accounts? | Push down to subsidiary |
| 3 | Withholding tax on inbound payments? | Covered Tax (Category 1 or 3) |

## 7. Stratos Worked Example: Classifying German Taxes

**Scenario:** SG Germany GmbH's tax accounts show the following for FY 2025:

| Line Item | Amount (€) | Classification |
|-----------|------------|----------------|
| Corporate income tax (Körperschaftsteuer) | 8,200,000 | ? |
| Solidarity surcharge (5.5% of CIT) | 451,000 | ? |
| Trade tax (Gewerbesteuer) | 3,100,000 | ? |
| VAT paid on supplies | 2,400,000 | ? |
| Wage tax (employer portion) | 890,000 | ? |
| Real property tax (Grundsteuer) | 125,000 | ? |
| R&D tax credit received | (180,000) | ? |

### 7.1 Classification Analysis

**1. Corporate Income Tax: €8,200,000**
- Question: Tax on entity's own income? → YES
- Category: Article 4.2.1(a)
- **Result: COVERED TAX**

**2. Solidarity Surcharge: €451,000**
- Question: Tax on entity's own income (surcharge on CIT)? → YES
- Category: Article 4.2.1(a) (component of income tax)
- **Result: COVERED TAX**

**3. Trade Tax (Gewerbesteuer): €3,100,000**
- Question: Tax on income/profits? → YES (levied on trading profit)
- Category: Article 4.2.1(a)
- **Result: COVERED TAX**

**4. VAT Paid: €2,400,000**
- Question: Tax on own income? → NO (indirect consumption tax)
- **Result: NOT A COVERED TAX** (exclude from ETR numerator)

**5. Wage Tax (Employer): €890,000**
- Question: Tax on own income? → NO (payroll tax)
- **Result: NOT A COVERED TAX**

**6. Real Property Tax: €125,000**
- Question: Tax on income? → NO (property ownership tax)
- **Result: NOT A COVERED TAX**

**7. R&D Tax Credit: €(180,000)**
- Question: Is this a QRTC?
  - Is it refundable as cash? → YES (German R&D credit is refundable)
  - Within 4 years? → YES
  - Not limited to tax liability? → YES
- **Result: QRTC—treat as INCOME, not tax reduction**

### 7.2 Summary for SG Germany GmbH

| Item | Treatment | Amount (€) |
|------|-----------|------------|
| **Covered Taxes** | | |
| Corporate income tax | Include | 8,200,000 |
| Solidarity surcharge | Include | 451,000 |
| Trade tax | Include | 3,100,000 |
| **Subtotal Covered Taxes** | | **11,751,000** |
| | | |
| **Excluded** | | |
| VAT | Exclude | — |
| Wage tax | Exclude | — |
| Property tax | Exclude | — |
| R&D credit | Treat as income | — |
| | | |
| **GloBE Income Adjustment** | | |
| R&D credit (QRTC) | Add to GloBE Income | +180,000 |

**Impact on ETR Calculation:**

Without QRTC adjustment:
- If R&D credit reduced taxes: Covered Taxes = €11,751,000 - €180,000 = €11,571,000
- ETR would be lower

With QRTC adjustment:
- Covered Taxes = €11,751,000 (credit reversed out of tax line)
- GloBE Income increased by €180,000
- ETR numerator AND denominator both increase—more favourable outcome

## 8. Common Classification Challenges

### 8.1 Challenge 1: Minimum Taxes

**Issue:** Many jurisdictions impose minimum taxes—how do they classify?

| Minimum Tax Type | Classification |
|------------------|----------------|
| Corporate minimum tax on income | Covered Tax (Category 1) |
| Alternative minimum tax | Covered Tax (Category 1) |
| Minimum tax on equity/assets only | NOT Covered Tax |
| QDMTT | Exclude (Article 4.2.2(b)) |
| Non-qualifying DMT | Covered Tax (Category 1) |

### 8.2 Challenge 2: Digital Services Taxes

**Issue:** Are DSTs "taxes imposed in lieu" of CIT?

**Analysis:**
- DSTs are typically imposed on gross revenues
- They are NOT imposed "in lieu" of CIT—they apply in addition to or regardless of CIT
- They are not substitutes for net income taxation

**Result:** DSTs are generally **NOT Covered Taxes**

### 8.3 Challenge 3: Tonnage Taxes

**Issue:** Shipping companies often pay tonnage tax instead of CIT.

**Analysis:**
- Tonnage tax replaces CIT for qualifying shipping income
- It is explicitly imposed "in lieu" of corporate income tax

**Result:** Tonnage tax is a **Covered Tax** (Category 3)

Note: This interacts with the International Shipping Exclusion (Article 3.3)—if shipping income is excluded from GloBE Income, the related tonnage tax should also be excluded from Covered Taxes.

### 8.4 Challenge 4: Branch Profits Tax

**Issue:** Some jurisdictions impose a second-tier tax on profits remitted by a branch to its foreign head office.

**Analysis:**
- Branch profits tax is imposed on the repatriation of profits, not on the earning of profits
- It is economically similar to withholding tax on dividends
- Generally levied on gross remittances

**Result:** Branch profits tax is generally a **Covered Tax** (Category 1 or 3, depending on structure)

These classification challenges highlight a recurring theme in Covered Tax analysis: the need to look beyond a tax's label to understand its economic substance. A "digital services tax" may sound like a modern income tax but operates as a turnover levy. A "tonnage tax" may seem unrelated to income but functions as a substitute for corporate income tax. The GloBE framework demands substance-over-form analysis, examining whether each levy genuinely represents taxation of corporate profits. Groups with diverse operations across multiple jurisdictions must develop systematic approaches to classification, documenting the analysis for each tax type and jurisdiction. The stakes are significant—miscategorising a substantial tax can swing the ETR by several percentage points, potentially transforming a compliant jurisdiction into one triggering top-up tax.
