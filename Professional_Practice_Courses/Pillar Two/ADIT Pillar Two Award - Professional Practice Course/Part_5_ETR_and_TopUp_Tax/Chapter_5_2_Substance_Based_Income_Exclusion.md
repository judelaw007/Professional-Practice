# Chapter 5.2: Substance-Based Income Exclusion (SBIE)

## Learning Objective

After completing this chapter, you will be able to calculate the Substance-Based Income Exclusion (SBIE) using the payroll and tangible asset carve-outs, apply the correct transition rates for each fiscal year, and determine the Excess Profit subject to Top-Up Tax.

## Key References

**OECD GloBE Model Rules:**
- Article 5.3.1 — SBIE amount definition
- Article 5.3.2 — Exclusion calculation (sum of carve-outs)
- Article 5.3.3 — Payroll carve-out
- Article 5.3.4 — Tangible asset carve-out
- Article 5.3.5 — Location rules (50% threshold)
- Article 9.2.1 — Transition payroll rates
- Article 9.2.2 — Transition tangible asset rates
- Article 10.1 — Definitions (Eligible Payroll Costs, Eligible Tangible Assets, Eligible Employees)

**Administrative Guidance:**
- June 2024: SBIE uses accounting carrying value, not GloBE carrying value
- February 2023: Mobile employee allocation clarification

**OECD Commentary:**
- Chapter 5, paragraphs 52-95 — SBIE calculation methodology

## 1. What SBIE Does

The Substance-Based Income Exclusion reduces the amount of income subject to Top-Up Tax by recognising that genuine economic substance (employees and physical assets) represents real business activity deserving a fixed return.

### 1.1 The Concept

```
                                              SBIE
                                               ↓
┌─────────────────────────────────────────────────────────────────┐
│                    Net GloBE Income                             │
│  ┌───────────────────────────────────────────┬────────────────┐ │
│  │        Substance-Based                    │    Excess      │ │
│  │        Income Exclusion                   │    Profit      │ │
│  │        (SBIE)                             │                │ │
│  │                                           │    ← Subject   │ │
│  │        ← Excluded from                    │      to        │ │
│  │          Top-Up Tax                       │      Top-up    │ │
│  │                                           │      Tax       │ │
│  └───────────────────────────────────────────┴────────────────┘ │
└─────────────────────────────────────────────────────────────────┘
```

### 1.2 The Formula

```
Excess Profit = Net GloBE Income − SBIE

Top-Up Tax = Top-Up Tax % × Excess Profit
```

**Key insight:** SBIE reduces the **base** on which Top-Up Tax is calculated, not the rate. Higher substance = lower Top-Up Tax.

## 2. SBIE Components

Article 5.3.2 defines the SBIE amount as the sum of two carve-outs for each Constituent Entity in the jurisdiction:

```
SBIE = Payroll Carve-out + Tangible Asset Carve-out
```

### 2.1 Component 1: Payroll Carve-out (Article 5.3.3)

```
Payroll Carve-out = Eligible Payroll Costs × Payroll Rate
```

### 2.2 Component 2: Tangible Asset Carve-out (Article 5.3.4)

```
Tangible Asset Carve-out = Carrying Value of Eligible Tangible Assets × Asset Rate
```

## 3. Transition Rates (Article 9.2)

The SBIE percentages are **higher** in early years and **reduce** over a 10-year transition period to the permanent rates of 5%.

### 3.1 SBIE Transition Rate Table

| Fiscal Year (beginning in) | Payroll Rate | Tangible Asset Rate |
|----------------------------|--------------|---------------------|
| 2024 | 10.0% | 8.0% |
| 2025 | 9.8% | 7.8% |
| 2026 | 9.6% | 7.6% |
| 2027 | 9.4% | 7.4% |
| 2028 | 9.2% | 7.2% |
| 2029 | 8.4% | 6.6% |
| 2030 | 7.6% | 6.0% |
| 2031 | 6.8% | 5.4% |
| 2032 | 6.0% | 4.8% |
| 2033 | 5.2% | 4.4% |
| **2034+** | **5.0%** | **5.0%** |

**Practical implication:** In early transition years, the higher rates provide greater SBIE—reducing Top-Up Tax exposure. As rates decline, more income becomes subject to Top-Up Tax.

### 3.2 Which Year's Rate Applies?

Use the rate for the **fiscal year** being calculated based on when the fiscal year **begins**:
- FY beginning 2025: Use 2025 rates (9.8% / 7.8%)
- FY beginning 2024: Use 2024 rates (10.0% / 8.0%)

**Note:** Consult domestic implementing legislation for the specific rule applicable in each jurisdiction.

## 4. Eligible Payroll Costs (Article 10.1)

### 4.1 What Qualifies

| Category | Examples | Included? |
|----------|----------|-----------|
| **Salaries and wages** | Base salary, hourly wages | ✅ Yes |
| **Bonuses and allowances** | Performance bonuses, housing allowance | ✅ Yes |
| **Stock-based compensation** | Share options, RSUs (expensed amount) | ✅ Yes |
| **Employee benefits** | Medical insurance, pension contributions | ✅ Yes |
| **Payroll taxes** | Employer social security, fringe benefits tax | ✅ Yes |
| **Retirement benefits** | Employer pension fund contributions | ✅ Yes |

### 4.2 What Does NOT Qualify

| Category | Why Excluded |
|----------|--------------|
| **Capitalised payroll** | Already in tangible asset carve-out (avoid double-counting) |
| **Contractor payments** | Not "employees" under Article 10.1 |
| **International shipping payroll** | Excluded income under Article 3.3 |
| **Payroll for excluded entities** | Investment Entities excluded from SBIE |

### 4.3 Eligible Employees Definition

An **Eligible Employee** is an employee (including part-time) of a Constituent Entity who performs activities for the MNE Group in the jurisdiction.

**Critical test:** Where does the employee **perform activities**?

| Scenario | Treatment |
|----------|-----------|
| Employee works 100% in Jurisdiction A | 100% of payroll costs → Jurisdiction A |
| Employee works 70% in Jurisdiction A, 30% in Jurisdiction B | 70% → A, 30% → B |
| Employee works less than 50% in any single jurisdiction | Proportionate allocation required |

## 5. Eligible Tangible Assets (Article 10.1)

### 4.1 What Qualifies

| Asset Type | Examples | Included? |
|------------|----------|-----------|
| **Property, plant and equipment** | Buildings, machinery, vehicles | ✅ Yes |
| **Natural resources** | Mining rights, oil and gas assets | ✅ Yes |
| **Leased assets (ROU)** | Right-of-use assets under IFRS 16 | ✅ Yes |
| **Licensed assets** | Government licences on land | ✅ Yes |

### 4.2 What Does NOT Qualify

| Asset Type | Why Excluded |
|------------|--------------|
| **Intangible assets** | IP, goodwill, software (not "tangible") |
| **Financial assets** | Investments, receivables |
| **Cash and equivalents** | Not tangible productive assets |
| **Inventory** | Current asset, not long-term productive asset |
| **Assets under construction** | Not yet in use (until capitalised) |

### 5.3 Carrying Value

Use the **accounting carrying value** (net book value) from financial statements:

```
Carrying Value = Cost − Accumulated Depreciation − Impairment
```

**June 2024 Administrative Guidance clarification:** Use the **accounting** carrying value, not GloBE-adjusted carrying value. Any adjustments to derive GloBE Income do not affect SBIE calculation.

### 5.4 Average Carrying Value

Article 5.3.4 requires using the **average** of opening and closing carrying values:

```
                    Opening Carrying Value + Closing Carrying Value
Average Carrying Value = ─────────────────────────────────────────────────
                                            2
```

**Example:**

| Asset | Opening NBV | Closing NBV | Average |
|-------|-------------|-------------|---------|
| Factory | €10,000,000 | €9,500,000 | €9,750,000 |
| Equipment | €2,000,000 | €1,800,000 | €1,900,000 |
| **Total** | **€12,000,000** | **€11,300,000** | **€11,650,000** |

## 6. Location Rules (Article 5.3.5)

### 6.1 The 50% Threshold

If an employee or tangible asset is located in a jurisdiction for **50% or less** of the time, only the proportionate share of the carve-out applies.

### 6.2 Mobile Employees

**Scenario:** An employee is based in the UK but travels extensively.

| Jurisdiction | Days Worked | % of Year | Treatment |
|--------------|-------------|-----------|-----------|
| UK (home base) | 150 | 60% | 60% of payroll → UK |
| Germany | 60 | 24% | 24% of payroll → Germany |
| France | 40 | 16% | 16% of payroll → France |

**Total = 100%** — Full payroll cost is allocated across jurisdictions.

### 6.3 Mobile Assets

**Scenario:** A shipping container travels between jurisdictions.

| Jurisdiction | Days Located | % of Year | Treatment |
|--------------|--------------|-----------|-----------|
| Netherlands | 200 | 55% | 55% of carrying value → Netherlands |
| Belgium | 165 | 45% | 45% of carrying value → Belgium |

## 7. SBIE Cannot Create a Loss

**Critical rule:** The SBIE cannot reduce Excess Profit below zero.

```
Excess Profit = MAX(0, Net GloBE Income − SBIE)
```

If SBIE exceeds Net GloBE Income, the excess is **lost**—it cannot be carried forward or used to offset other jurisdictions.

### 7.1 Example: High-Substance, Low-Profit Jurisdiction

| Item | Amount |
|------|--------|
| Net GloBE Income | €2,000,000 |
| Payroll Carve-out | €1,800,000 |
| Tangible Asset Carve-out | €1,500,000 |
| **Total SBIE** | **€3,300,000** |
| Excess Profit | MAX(0, €2M − €3.3M) = **€0** |

**Result:** No Top-Up Tax, but €1,300,000 of "wasted" SBIE cannot be used elsewhere.

## 8. Stratos Worked Example: Complete SBIE Calculation

### 8.1 Data for FY 2025

Stratos has identified two low-taxed jurisdictions from Chapter 5.1:
- **Singapore** (ETR 9.81%)
- **Ireland** (ETR 11.80%)

Germany (ETR 23.00%) is not low-taxed, so no SBIE calculation is required.

### 8.2 Singapore SBIE Calculation

**Step 1: Gather payroll data**

| Entity | Eligible Payroll Costs |
|--------|------------------------|
| SG Singapore Pte Ltd | €850,000 |

**Step 2: Gather tangible asset data**

| Asset | Opening NBV | Closing NBV | Average |
|-------|-------------|-------------|---------|
| Office building | €1,200,000 | €1,150,000 | €1,175,000 |
| IT equipment | €180,000 | €150,000 | €165,000 |
| Leased vehicles (ROU) | €95,000 | €80,000 | €87,500 |
| **Total** | | | **€1,427,500** |

**Step 3: Apply FY 2025 transition rates**

| Component | Base | Rate | Carve-out |
|-----------|------|------|-----------|
| Payroll | €850,000 | 9.8% | €83,300 |
| Tangible Assets | €1,427,500 | 7.8% | €111,345 |
| **Total SBIE** | | | **€194,645** |

**Step 4: Calculate Excess Profit**

```
Net GloBE Income:                   €4,000,000
Less: SBIE:                         (€194,645)
                                    ───────────
Excess Profit:                      €3,805,355
```

### 8.3 Ireland SBIE Calculation

**Step 1: Gather payroll data**

| Entity | Eligible Payroll Costs |
|--------|------------------------|
| SG Ireland Ltd | €4,200,000 |

**Step 2: Gather tangible asset data**

| Asset | Opening NBV | Closing NBV | Average |
|-------|-------------|-------------|---------|
| Office building | €8,500,000 | €8,200,000 | €8,350,000 |
| R&D equipment | €2,100,000 | €1,900,000 | €2,000,000 |
| Data centre | €5,400,000 | €5,100,000 | €5,250,000 |
| Leased assets (ROU) | €620,000 | €580,000 | €600,000 |
| **Total** | | | **€16,200,000** |

**Step 3: Apply FY 2025 transition rates**

| Component | Base | Rate | Carve-out |
|-----------|------|------|-----------|
| Payroll | €4,200,000 | 9.8% | €411,600 |
| Tangible Assets | €16,200,000 | 7.8% | €1,263,600 |
| **Total SBIE** | | | **€1,675,200** |

**Step 4: Calculate Excess Profit**

```
Net GloBE Income:                   €15,000,000
Less: SBIE:                         (€1,675,200)
                                    ────────────
Excess Profit:                      €13,324,800
```

### 8.4 SBIE Summary

| Jurisdiction | Net GloBE Income | SBIE | Excess Profit |
|--------------|------------------|------|---------------|
| Singapore | €4,000,000 | €194,645 | €3,805,355 |
| Ireland | €15,000,000 | €1,675,200 | €13,324,800 |

**Key observation:** Ireland has significant substance (high payroll and tangible assets), which reduces its Excess Profit by over €1.6M. Singapore has less substance relative to income.

## 9. Multi-Entity Jurisdictions

When a jurisdiction has multiple Constituent Entities, calculate SBIE for **each entity** and aggregate:

### 9.1 Example: Ireland with Two Entities

| Entity | Payroll Costs | Tangible Assets (Avg) |
|--------|---------------|-----------------------|
| SG Ireland Ltd | €4,200,000 | €16,200,000 |
| SG Dublin Services Ltd | €1,800,000 | €3,400,000 |
| **Jurisdiction Total** | **€6,000,000** | **€19,600,000** |

**SBIE Calculation (FY 2025):**

| Component | Base | Rate | Carve-out |
|-----------|------|------|-----------|
| Payroll | €6,000,000 | 9.8% | €588,000 |
| Tangible Assets | €19,600,000 | 7.8% | €1,528,800 |
| **Total SBIE** | | | **€2,116,800** |

**Jurisdictional blending applies:** The combined SBIE reduces the combined Net GloBE Income.

## 10. Election Not to Apply SBIE (Article 5.3.1)

An MNE may elect **not** to apply SBIE for a jurisdiction in any fiscal year.

### 10.1 When to Consider This Election

| Scenario | Recommendation |
|----------|----------------|
| SBIE exceeds Net GloBE Income (wasted SBIE) | Election irrelevant—no Top-Up Tax either way |
| Minimal payroll/assets relative to income | May simplify compliance if SBIE is immaterial |
| QDMTT applies and covers liability | May skip SBIE if QDMTT already collects full Top-Up Tax |

**Practical note:** This election is rarely beneficial. SBIE always reduces or eliminates Top-Up Tax liability.

## 11. Common Pitfalls

### 11.1 Pitfall 1: Using Gross Rather Than Net Book Value

**Error:** Including accumulated depreciation in tangible asset value.

**Correct approach:** Use **net book value** (carrying value after depreciation).

### 11.2 Pitfall 2: Including Intangible Assets

**Error:** Adding software or patents to the tangible asset carve-out.

**Correct approach:** Only tangible assets qualify. Intangibles are excluded.

### 11.3 Pitfall 3: Double-Counting Capitalised Payroll

**Error:** Including payroll costs that were capitalised into an asset (e.g., construction labour) in both carve-outs.

**Correct approach:** Capitalised payroll is excluded from the payroll carve-out—it's already in the tangible asset base.

### 11.4 Pitfall 4: Forgetting the Average Calculation

**Error:** Using only closing NBV for tangible assets.

**Correct approach:** Use the **average** of opening and closing carrying values.

### 11.5 Pitfall 5: Applying Wrong Year's Transition Rate

**Error:** Using 2024 rates for a FY 2026 calculation.

**Correct approach:** Apply the transition rate for the **fiscal year** being calculated.

### 11.6 Pitfall 6: Ignoring Location Rules for Mobile Employees

**Error:** Allocating 100% of a travelling employee's payroll to their home jurisdiction.

**Correct approach:** Allocate based on **time spent** performing activities in each jurisdiction.

## 12. SBIE Calculation Worksheet

Use this worksheet for each low-taxed jurisdiction:

```
SBIE CALCULATION WORKSHEET
Jurisdiction: _________________________
Fiscal Year: _________________________
Transition Rates: Payroll ______% | Tangible Assets ______%

SECTION A: CONSTITUENT ENTITIES
List all CEs in this jurisdiction (excluding Investment Entities):

| # | Entity Name |
|---|-------------|
| 1 | ___________ |
| 2 | ___________ |
| 3 | ___________ |

SECTION B: PAYROLL CARVE-OUT
B1  Eligible Payroll Costs (all CEs)           €__________________
B2  Less: Capitalised payroll                  (€__________________)
B3  Less: International shipping payroll       (€__________________)
B4  Net Eligible Payroll Costs (B1-B2-B3)      €__________________
B5  Payroll Transition Rate                    __________________%
B6  PAYROLL CARVE-OUT (B4 × B5)                €__________________

SECTION C: TANGIBLE ASSET CARVE-OUT
C1  Opening carrying value (all CEs)           €__________________
C2  Closing carrying value (all CEs)           €__________________
C3  Average carrying value ((C1+C2)÷2)         €__________________
C4  Less: Assets under construction            (€__________________)
C5  Net Eligible Tangible Assets (C3-C4)       €__________________
C6  Tangible Asset Transition Rate             __________________%
C7  TANGIBLE ASSET CARVE-OUT (C5 × C6)         €__________________

SECTION D: TOTAL SBIE
D1  Payroll Carve-out (B6)                     €__________________
D2  Tangible Asset Carve-out (C7)              €__________________
D3  TOTAL SBIE (D1 + D2)                       €__________________

SECTION E: EXCESS PROFIT
E1  Net GloBE Income (from Chapter 5.1)        €__________________
E2  SBIE (D3)                                  €__________________
E3  EXCESS PROFIT (MAX(0, E1 - E2))            €__________________

    If E3 = 0: No Top-Up Tax for this jurisdiction.

SECTION F: VERIFICATION CHECKLIST
☐ Correct transition rates applied for fiscal year
☐ Average carrying value used (not just closing)
☐ Capitalised payroll excluded
☐ Intangible assets excluded
☐ Location rules applied for mobile employees/assets
☐ Investment Entities excluded
```

## 13. Policy Rationale

Why does SBIE exist?

### 13.1 The Theory

GloBE targets **excess profits**—income beyond what genuine business operations would generate. The SBIE recognises that:

1. **Employees** represent real economic activity
2. **Tangible assets** represent physical investment
3. A **fixed return** on these factors should be excluded from minimum taxation

### 13.2 The Formula Logic

| Factor | Rate | Justification |
|--------|------|---------------|
| Payroll | 5-10% | Return on human capital investment |
| Tangible Assets | 5-8% | Return on physical capital investment |

The rates approximate a "normal" return on these investments, excluding it from the minimum tax calculation.

### 13.3 Who Benefits Most?

| Business Type | Payroll | Tangible Assets | SBIE Benefit |
|---------------|---------|-----------------|--------------|
| Manufacturing | Medium | High | **High** |
| Distribution | High | Medium | **Medium-High** |
| Retail | High | Medium | **Medium-High** |
| IP Holding | Low | Low | **Low** |
| Financial Services | High | Low | **Medium** |
| Tech (asset-light) | Medium | Low | **Low-Medium** |

**Practical implication:** MNEs with significant manufacturing or distribution operations in low-tax jurisdictions benefit most from SBIE.
