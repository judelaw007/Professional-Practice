# Chapter 3.3: Stock-Based Compensation Election

## Learning Objective

After completing this chapter, you will be able to evaluate whether the stock-based compensation election is beneficial for each jurisdiction and apply the election mechanics correctly, including recapture provisions.

## Introduction

Stock-based compensation creates one of the most persistent and material book-tax differences in corporate taxation. The accounting profession, following IFRS 2 and similar standards, requires companies to expense share options and equity awards at fair value over the vesting period—a measure designed to reflect economic cost to shareholders. Tax authorities, by contrast, typically defer the deduction until exercise or vesting and measure it at intrinsic value—the actual benefit realised by the employee. In a rising share price environment, this creates a permanent gap: the tax deduction at exercise substantially exceeds the cumulative accounting expense. The GloBE framework must grapple with this divergence, and the Article 3.2.2 election represents its solution.

## 1. The Stock-Based Compensation Problem

Stock-based compensation (SBC) creates a significant book-to-tax difference that can distort the GloBE ETR calculation.

### Why SBC Creates a Problem

| Treatment | Basis | Timing |
|-----------|-------|--------|
| **Accounting (IFRS 2)** | Fair value at grant date | Expensed over vesting period |
| **Tax (many jurisdictions)** | Market value at exercise/vesting | Deducted at exercise/vesting |

**Result:** If share price increases between grant and exercise, the tax deduction exceeds the accounting expense. This difference is **permanent**—it will never reverse.

### Impact on GloBE ETR

Without intervention:

```
GloBE Income = Financial Accounting Net Income + Tax Expense − Other Adjustments

If accounting SBC expense is lower than tax deduction:
→ GloBE Income is higher (smaller expense deducted)
→ Covered Taxes reflect actual tax paid (based on larger deduction)
→ ETR = Covered Taxes ÷ GloBE Income = artificially LOW
```

**Risk:** A jurisdiction could become "low-taxed" purely due to SBC timing differences, triggering Top-Up Tax.

## The Article 3.2.2 Election

### What the Election Does

The election allows an MNE to **substitute** the tax-deductible amount of SBC for the accounting expense when calculating GloBE Income *(Article 3.2.2)*.

| Approach | GloBE Income Impact |
|----------|---------------------|
| **Default (no election)** | Use accounting expense (IFRS 2) |
| **With election** | Use tax deduction amount |

### Effect of the Election

```
Default:                          With Election:
GloBE Income uses               GloBE Income uses
lower accounting expense        higher tax deduction
         ↓                               ↓
Higher GloBE Income             Lower GloBE Income
         ↓                               ↓
Lower ETR                       Higher ETR
         ↓                               ↓
More likely to trigger          Less likely to trigger
Top-Up Tax                      Top-Up Tax
```

**Key insight:** When tax deduction exceeds accounting expense, the election typically **decreases** GloBE Income (larger deduction reduces net income), which **increases** ETR and **reduces** Top-Up Tax risk.

The election exists because the framework's architects recognised that SBC timing differences, if left unaddressed, could trigger Top-Up Tax in situations where no genuine undertaxation exists. Consider a technology company granting options when its share price is low; years later, when options vest at a much higher price, the tax deduction significantly exceeds the original accounting expense. Without the election, the ETR calculation would show Covered Taxes (reflecting the large tax deduction) divided by a GloBE Income base reduced only by the smaller accounting expense—producing an artificially low ETR. The election aligns both numerator and denominator to the same basis, revealing the true effective rate on operating profits.

## Election Mechanics

### Scope

The election applies to compensation paid in the form of:
- Shares/stock
- Stock options
- Stock warrants
- Equivalent instruments

### Jurisdictional Application

| Feature | Requirement |
|---------|-------------|
| **Level** | Per jurisdiction |
| **Coverage** | All Constituent Entities in that jurisdiction |
| **Consistency** | Must apply to **all** SBC in the jurisdiction |

### Five-Year Election

| Characteristic | Detail |
|----------------|--------|
| **Duration** | Remains in force for minimum 5 years |
| **Automatic continuation** | Continues indefinitely until revoked |
| **Early revocation** | Not permitted within first 5 years |
| **Re-election after revocation** | Not permitted within 5 years of revocation |

### Tracing Requirement

Only **one** Constituent Entity may deduct SBC in excess of the financial accounting amount, and only if that CE is allowed a tax deduction for such SBC under local tax law.

**Example:** If UK parent grants options to employees of German subsidiary:
- Germany must have a local tax deduction for the SBC
- Only the German CE can claim the excess deduction for GloBE purposes

The five-year lock-in period serves an anti-avoidance function. Without it, groups could opportunistically elect or revoke the election year by year, choosing whichever treatment produces the more favourable ETR in each period. This would undermine the consistency that the GloBE framework requires for meaningful comparisons over time. The lock-in also provides administrative simplicity: once elected, the approach is fixed for a meaningful period, reducing the need for annual re-evaluation. The prohibition on re-election within five years of revocation prevents churning between regimes to cherry-pick favourable outcomes.

## Timing Scenarios

### Scenario 1: Share Price Increases (Most Common)

**Facts:**
- Options granted when share price = €10
- Options exercised when share price = €18
- 100,000 options

| Item | Accounting | Tax |
|------|------------|-----|
| Per-option expense/deduction | €3 (Black-Scholes at grant) | €18 (market value at exercise) |
| Total | €300,000 | €1,800,000 |

**Without election:**
- GloBE Income deduction: €300,000
- Tax deduction: €1,800,000
- Covered Taxes reflect €1,800,000 deduction
- **Result:** ETR depressed

**With election:**
- GloBE Income deduction: €1,800,000
- Tax deduction: €1,800,000
- **Result:** Aligned; ETR not distorted

### Scenario 2: Share Price Decreases (Shortfall)

**Facts:**
- Options granted when share price = €20
- Options exercised when share price = €12
- 100,000 options

| Item | Accounting | Tax |
|------|------------|-----|
| Per-option expense/deduction | €5 (Black-Scholes at grant) | €12 (market value at exercise) |
| Total | €500,000 | €1,200,000 |

**Analysis:** Even with share price decline, the tax deduction (€1.2M) exceeds accounting expense (€500K) in this example because the Black-Scholes value was lower than intrinsic value at exercise.

**Note:** In some cases where accounting expense exceeds tax deduction, the election would **reduce** GloBE Income, potentially **lowering** ETR. This requires careful analysis.

### Scenario 3: Options Expire Unexercised

**Facts:**
- Options granted: accounting expense €400,000
- Election made: tax deduction of €0 taken each year (no exercise yet)
- Options expire unexercised in Year 5

**With election in place:**
- Years 1-4: No tax deduction, so €0 deducted from GloBE Income
- Year 5: Options expire → Must **add back** €400,000 to GloBE Income

**Recapture rule:** If options expire without exercise, the total amount previously deducted under the election must be included in GloBE Income for the fiscal year of expiry *(Article 3.2.2)*.

The recapture rule prevents the election from creating a permanent benefit where none should exist. Under the election, no deduction flows through GloBE Income until options are exercised and a tax deduction crystalises. If options expire worthless—because the share price never exceeded the exercise price, or employees left before vesting—no tax deduction ever materialises. Without recapture, the entity would have benefited from not deducting the accounting expense in prior years while never facing the corresponding tax deduction. Recapture corrects this by adding back an amount equal to the accounting expense that would have been deducted without the election, ensuring symmetric treatment over the full option lifecycle.

## Mid-Stream Election Adjustment

### The Problem

If an MNE makes the SBC election **after** some accounting expense has already been recorded in GloBE Income, an adjustment is required to prevent double-counting.

### The Rule

When making the election mid-stream, include in GloBE Income:

```
Adjustment = Cumulative accounting expense already deducted
           − Cumulative amount that would have been deducted under election
```

### Worked Example

**Facts:**
- SBC program started Year 1
- Election made in Year 3
- Vesting period: 4 years

| Year | Accounting Expense | Tax Deduction | Already in GloBE Income |
|------|-------------------|---------------|------------------------|
| 1 | €250,000 | €0 | €250,000 |
| 2 | €250,000 | €0 | €250,000 |
| 3 | €250,000 | €0 | — (election year) |
| 4 | €250,000 | €1,500,000 | — |

**Year 3 adjustment (election year):**

```
Cumulative accounting expense (Years 1-2): €500,000
Cumulative tax deduction (Years 1-2):      €0
Adjustment to add to Year 3 GloBE Income:  €500,000
```

**Effect:** The €500,000 previously deducted is added back; from Year 3 onwards, only tax deductions are used.

## Revocation of the Election

### When Revocation Applies

An MNE may revoke the election after 5 years if circumstances change (e.g., SBC programmes discontinued, jurisdiction becomes high-tax).

### Revocation Adjustment

On revocation, include in GloBE Income:

```
Adjustment = Amount deducted under election
           − Financial accounting expense accrued
           (for SBC where final tax deduction has not yet been determined)
```

### What Revocation Does NOT Affect

- Options already exercised (deduction finalised)
- Prior year GloBE Income calculations

### Worked Example

**Facts:**
- Election revoked in Year 8
- Outstanding unvested options with:
  - Cumulative deduction under election: €0 (no exercise yet)
  - Cumulative accounting expense: €600,000

**Revocation adjustment:**

```
Amount deducted under election: €0
Less: Accounting expense accrued: €600,000
Adjustment: (€600,000)
```

**Effect:** Reduce GloBE Income by €600,000 in revocation year (effectively reverting to accounting treatment).

## Deferred Tax Implications

### GloBE Carrying Value Requirement

When the SBC election is made, deferred tax must be recalculated based on **GloBE carrying values**, not financial accounting values *(Administrative Guidance, July 2023)*.

### What This Means

| Without Election | With Election |
|-----------------|---------------|
| DTA based on accounting expense | DTA based on expected tax deduction |
| Standard IFRS 2 / IAS 12 treatment | Recalculated for GloBE purposes |

### Practical Impact

The deferred tax adjustment amount in Adjusted Covered Taxes must align with the SBC treatment in GloBE Income. This ensures consistency between numerator (Covered Taxes) and denominator (GloBE Income).

## Decision Framework: Should You Elect?

### Step 1: Identify Jurisdictions with Material SBC

| Question | If Yes |
|----------|--------|
| Does the jurisdiction have significant SBC programmes? | Continue to Step 2 |
| Is SBC immaterial in this jurisdiction? | No election needed |

### Step 2: Determine Local Tax Treatment

| Question | If Yes |
|----------|--------|
| Does local tax law allow SBC deduction at exercise/vesting? | Continue to Step 3 |
| Is SBC not deductible for local tax? | Election provides no benefit |

### Step 3: Assess ETR Position

| Jurisdiction ETR | Recommendation |
|-----------------|----------------|
| **Well above 15%** (e.g., 25%+) | Election likely not needed; jurisdiction is high-tax regardless |
| **Near 15%** (e.g., 13-17%) | **Analyse carefully**; election may prevent Top-Up Tax |
| **Well below 15%** (e.g., <10%) | Election may help but won't eliminate Top-Up Tax entirely |

### Step 4: Project Share Price Movement

| Expected Movement | Impact |
|-------------------|--------|
| Share price likely to **increase** significantly | Election beneficial (larger tax deduction) |
| Share price stable or declining | Election may have neutral or mixed impact |
| High employee turnover / forfeitures expected | Consider recapture risk |

### Step 5: Evaluate Administrative Burden

| Consideration | Impact |
|---------------|--------|
| Need to track tax deductions separately | Increased compliance cost |
| Multiple SBC programmes | Complex tracking |
| Options may expire unexercised | Recapture risk |

### Decision Matrix

| ETR Position | Share Price Trend | Recommendation |
|--------------|-------------------|----------------|
| Near 15% | Rising | **Strongly consider election** |
| Near 15% | Stable/Falling | Analyse case-by-case |
| Well above 15% | Any | Election likely unnecessary |
| Well below 15% | Rising | Election helpful but insufficient alone |
| Any | High forfeiture risk | **Caution**: recapture exposure |

## Stratos Worked Example

### Background

Stratos Group plc has a global equity incentive programme granting stock options to employees. The tax team must evaluate the SBC election for each jurisdiction.

### Jurisdiction Analysis

**Singapore (ETR: 12.5%)**

| Item | Value |
|------|-------|
| SBC accounting expense (FY 2025) | €850,000 |
| SBC tax deduction (FY 2025) | €620,000 |
| Share price trend | Declining |

**Analysis:**
- Tax deduction < Accounting expense
- Election would **increase** GloBE Income (using smaller €620K deduction instead of €850K)
- Higher GloBE Income → Lower ETR → **Worse** outcome

**Recommendation:** Do **NOT** elect for Singapore

**Germany (ETR: 28%)**

| Item | Value |
|------|-------|
| SBC accounting expense (FY 2025) | €1,200,000 |
| SBC tax deduction (FY 2025) | €1,850,000 |
| Share price trend | Rising |

**Analysis:**
- Tax deduction > Accounting expense
- Election would increase GloBE Income (€1.85M vs €1.2M)
- Higher GloBE Income → Minimal ETR impact (already high-tax)

**Recommendation:** Election is **neutral**; may elect for consistency or skip

**Ireland (ETR: 12.5% before QDMTT)**

| Item | Value |
|------|-------|
| SBC accounting expense (FY 2025) | €450,000 |
| SBC tax deduction (FY 2025) | €720,000 |
| Share price trend | Rising |
| QDMTT status | Ireland has QDMTT |

**Analysis:**
- Tax deduction > Accounting expense
- Election would increase GloBE Income
- However, Ireland's QDMTT already collects Top-Up Tax domestically

**Recommendation:** Election is **neutral** given QDMTT; consider for future planning

**United Kingdom (ETR: 24%)**

| Item | Value |
|------|-------|
| SBC accounting expense (FY 2025) | €2,400,000 |
| SBC tax deduction (FY 2025) | €3,100,000 |
| Share price trend | Rising |

**Analysis:**
- UK is high-tax jurisdiction
- Election increases GloBE Income but ETR remains above 15%

**Recommendation:** Election is **optional**; may elect for consistency across group

### Stratos SBC Election Summary

| Jurisdiction | ETR | Elect? | Rationale |
|--------------|-----|--------|-----------|
| Singapore | 12.5% | **No** | Tax deduction < accounting; election worsens ETR |
| Germany | 28% | Optional | High-tax; minimal impact |
| Ireland | 12.5% | Optional | QDMTT applies |
| UK | 24% | Optional | High-tax; minimal impact |

## 7. Common Pitfalls

### Pitfall 1: Assuming Election Always Helps

**Error:** Making the election in all jurisdictions without analysis.

**Problem:** If tax deduction < accounting expense, the election **lowers** GloBE Income, reducing ETR and potentially triggering Top-Up Tax.

### Pitfall 2: Forgetting the Recapture Rule

**Error:** Not tracking options that may expire unexercised.

**Problem:** Full recapture to GloBE Income in expiry year can cause unexpected ETR volatility.

### Pitfall 3: Missing the 5-Year Lock-In

**Error:** Planning to revoke the election after 2 years when circumstances change.

**Problem:** Revocation is not permitted within the first 5 years.

### Pitfall 4: Inconsistent Application Within Jurisdiction

**Error:** Applying election to some SBC programmes but not others in the same jurisdiction.

**Problem:** Election must apply to **all** SBC in the jurisdiction.

### Pitfall 5: Ignoring Deferred Tax Recalculation

**Error:** Using standard accounting deferred tax figures when election is made.

**Problem:** Deferred tax must be recalculated using GloBE carrying values.

The SBC election exemplifies a broader theme in the GloBE framework: the tension between following financial accounting as the starting point and adjusting for known book-tax differences that would otherwise distort the minimum tax calculation. Unlike the mandatory adjustments in Article 3.2, the SBC election is discretionary—groups can choose to live with the default treatment if it suits their circumstances. This optionality requires careful analysis: the election that benefits a high-growth technology company with appreciating share prices may disadvantage a mature company with stable or declining equity values. The decision framework outlined in this chapter provides a structured approach to that analysis, but ultimately each group must evaluate its own SBC programmes, share price trajectory, and jurisdictional ETR positions to determine whether the election serves its interests.

## Documentation Requirements

When making or analysing the SBC election, document:

| Item | Purpose |
