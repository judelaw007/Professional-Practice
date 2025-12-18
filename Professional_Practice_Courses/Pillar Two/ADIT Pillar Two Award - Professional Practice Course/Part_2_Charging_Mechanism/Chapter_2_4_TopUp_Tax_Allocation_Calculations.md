# Chapter 2.4: Top-Up Tax Allocation Calculations

## Learning Objective

After completing this chapter, you will be able to calculate the complete Top-Up Tax allocation from jurisdictional totals through to individual parent entity liability, handling minority interests and POPE structures.

## Introduction

The preceding chapters explained which rules apply and in what order. This chapter addresses the practical question: how much does each entity actually pay? Top-Up Tax allocation is a multi-stage process that traces from jurisdictional calculations, through entity-level apportionment, to final parent liability. Each stage serves a distinct purpose—jurisdictional calculations determine total undertaxation, entity allocation identifies which specific entities bear that undertaxation, and parent allocation determines which group members must actually remit the tax. Mastering these calculations requires attention to detail, particularly where ownership is split across multiple chains or where loss-making entities affect the allocation pool.

## 1. The Complete Allocation Process

Top-Up Tax allocation involves three distinct levels of calculation:

| Level | What It Does | Reference |
|-------|--------------|-----------|
| **Level 1: Jurisdictional** | Calculate Top-Up Tax for the jurisdiction | Article 5.2 |
| **Level 2: Entity** | Allocate jurisdictional Top-Up Tax to individual CEs | Article 5.2.4 |
| **Level 3: Parent** | Determine each parent's Allocable Share | Article 2.2 |

This chapter provides the calculation mechanics for each level and shows how they connect.

## 2. Level 1: Jurisdictional Top-Up Tax Calculation

### 2.1 The Complete Formula

**Jurisdictional Top-Up Tax = (Top-Up Tax Percentage × Excess Profit) + Additional Current Top-Up Tax − QDMTT**

Where:
- **Top-Up Tax Percentage** = Minimum Rate (15%) − Jurisdictional ETR *(Article 5.2.1)*
- **Excess Profit** = Net GloBE Income − SBIE *(Article 5.2.2)*
- **Additional Current Top-Up Tax** = Recaptured amounts from prior years *(Article 5.2.3)*
- **QDMTT** = Qualified Domestic Minimum Top-Up Tax already collected *(Article 5.2.3)*

### 2.2 Worked Example: Jurisdictional Calculation

**Scenario:** Stratos has operations in Singapore with the following data:

| Item | Value |
|------|-------|
| GloBE Income (all Singapore CEs combined) | €15,000,000 |
| Adjusted Covered Taxes | €1,875,000 |
| Payroll Costs (eligible employees) | €4,500,000 |
| Tangible Assets (net book value) | €8,000,000 |
| SBIE Rate (2026 transition year) | Payroll: 9.6%, Assets: 7.6% |
| QDMTT | Nil (Singapore has no QDMTT) |

**Step 1: Calculate ETR**

```
ETR = Adjusted Covered Taxes ÷ GloBE Income
    = €1,875,000 ÷ €15,000,000
    = 12.50%
```

**Step 2: Calculate Top-Up Tax Percentage**

```
Top-Up Tax % = 15% − ETR
             = 15% − 12.50%
             = 2.50%
```

**Step 3: Calculate SBIE**

```
Payroll Carve-Out = €4,500,000 × 9.6% = €432,000
Tangible Asset Carve-Out = €8,000,000 × 7.6% = €608,000
Total SBIE = €432,000 + €608,000 = €1,040,000
```

**Step 4: Calculate Excess Profit**

```
Excess Profit = GloBE Income − SBIE
              = €15,000,000 − €1,040,000
              = €13,960,000
```

**Step 5: Calculate Jurisdictional Top-Up Tax**

```
Jurisdictional Top-Up Tax = Top-Up Tax % × Excess Profit
                          = 2.50% × €13,960,000
                          = €349,000
```

**Result:** Singapore jurisdictional Top-Up Tax is **€349,000**.

## 3. SBIE Transition Rates Reference

The Substance-Based Income Exclusion uses transition rates that decline annually *(Article 9.1)*:

| Fiscal Year | Payroll Rate | Tangible Asset Rate |
|-------------|--------------|---------------------|
| 2024 | 10.0% | 8.0% |
| 2025 | 9.8% | 7.8% |
| 2026 | 9.6% | 7.6% |
| 2027 | 9.4% | 7.4% |
| 2028 | 9.2% | 7.2% |
| 2029 | 8.4% | 6.6% |
| 2030 | 7.6% | 6.0% |
| 2031 | 6.8% | 5.4% |
| 2032 | 6.0% | 5.2% |
| 2033+ | 5.0% | 5.0% |

**Note:** These are the permanent rates after the transition period. For years 2024-2028, rates decline by 0.2 percentage points annually. For years 2029-2032, the decline accelerates (0.8 percentage points for payroll, 0.4 for assets).

The SBIE transition schedule reflects the political compromise needed to secure agreement from jurisdictions with different economic characteristics. Countries with substantial manufacturing or employee-intensive service operations benefit from higher carve-out rates, as these reduce the "Excess Profit" base subject to Top-Up Tax. Starting at 10%/8% and declining to 5%/5% over a decade gives these jurisdictions time to adjust, while the declining trajectory ensures the carve-out does not permanently shield income from the minimum tax. For practitioners, the key implication is that SBIE calculations must use the correct year's rates—an error of one percentage point on a €50 million payroll changes the carve-out by €500,000.

## 4. Level 2: Entity Allocation Within a Jurisdiction

Once the jurisdictional Top-Up Tax is calculated, it must be **allocated to individual Constituent Entities** in that jurisdiction *(Article 5.2.4)*.

### 4.1 The Entity Allocation Rule

**Entity's Top-Up Tax = Jurisdictional Top-Up Tax × (Entity's GloBE Income ÷ Total Positive GloBE Income in Jurisdiction)**

**Key points:**
- Only CEs with **positive GloBE Income** receive an allocation
- CEs with GloBE losses receive **no allocation**
- Allocations are proportional to each CE's share of positive income

### 4.2 Worked Example: Multi-Entity Jurisdiction

**Scenario:** Stratos has three entities in Singapore with the following GloBE Income:

| Entity | GloBE Income | Allocation? |
|--------|--------------|-------------|
| SG Tech Pte Ltd | €10,000,000 | Yes |
| SG Services Pte Ltd | €6,000,000 | Yes |
| SG Holdings Pte Ltd | €(1,000,000) | No (loss) |
| **Total Positive** | **€16,000,000** | |

**Note:** Total positive GloBE Income (€16M) differs from Net GloBE Income (€15M) because the €1M loss reduces the jurisdictional total but the loss-making entity receives no allocation.

**Entity Allocations (assuming €349,000 jurisdictional Top-Up Tax):**

| Entity | GloBE Income | Share of Positive | Allocated Top-Up Tax |
|--------|--------------|-------------------|---------------------|
| SG Tech Pte Ltd | €10,000,000 | 62.5% | €349,000 × 62.5% = **€218,125** |
| SG Services Pte Ltd | €6,000,000 | 37.5% | €349,000 × 37.5% = **€130,875** |
| SG Holdings Pte Ltd | €(1,000,000) | 0% | **€0** |
| **Total** | | **100%** | **€349,000** |

The exclusion of loss-making entities from the allocation may seem counterintuitive—why should an entity with a loss not share the burden of Top-Up Tax? The answer lies in the purpose of entity-level allocation: to identify which specific entities gave rise to the undertaxed income. An entity with a GloBE loss did not contribute to the jurisdiction's positive net income and therefore bears no responsibility for the resulting Top-Up Tax. This creates an asymmetry—the loss-making entity reduces jurisdictional Net GloBE Income (lowering the Top-Up Tax base) but does not receive an allocation of the remaining Top-Up Tax. Groups should be aware that this asymmetry affects how Top-Up Tax "attaches" to specific entities for purposes such as IIR allocation and financial statement presentation.

## 5. Level 3: Parent Entity Allocable Share

After entity-level allocation, the Top-Up Tax is charged to **parent entities** under the IIR or UTPR based on their **Allocable Share** *(Article 2.2)*.

### 5.1 IIR Allocable Share Calculation

**Allocable Share = Top-Up Tax of LTCE × Inclusion Ratio** *(Article 2.2.1)*

**Inclusion Ratio = (GloBE Income of LTCE − Amount attributable to other owners) ÷ GloBE Income of LTCE** *(Article 2.2.2)*

### 5.2 Simple Ownership Example

**Scenario:** Stratos Group plc owns 100% of SG Tech Pte Ltd (Low-Taxed CE).

| Item | Value |
|------|-------|
| SG Tech Pte Ltd Top-Up Tax | €218,125 |
| Stratos's ownership | 100% |
| Stratos's Inclusion Ratio | 100% |
| **Stratos's Allocable Share** | **€218,125** |

### 5.3 Split Ownership Example

**Scenario:** SG Services Pte Ltd is owned:
- 70% by Stratos Group plc (through SG Holdings Ltd)
- 30% by External Investor A

| Item | Value |
|------|-------|
| SG Services Pte Ltd GloBE Income | €6,000,000 |
| SG Services Pte Ltd Top-Up Tax | €130,875 |
| GloBE Income attributable to External Investor | €6,000,000 × 30% = €1,800,000 |

**Stratos's Inclusion Ratio:**

```
Inclusion Ratio = (€6,000,000 − €1,800,000) ÷ €6,000,000
                = €4,200,000 ÷ €6,000,000
                = 70%
```

**Stratos's Allocable Share:**

```
Allocable Share = €130,875 × 70%
                = €91,613
```

**Result:** Stratos pays €91,613 under IIR. The €39,262 attributable to the external investor is not collected under IIR (subject to UTPR if applicable).

## 6. POPE Allocation Adjustments

When a **Partially-Owned Parent Entity (POPE)** is in the ownership chain, allocations require special handling *(Article 2.1.4)*.

### 6.1 POPE Definition Recap

A POPE is a Constituent Entity that:
1. Owns an Ownership Interest in another CE, AND
2. Has more than 20% of its profits held by third parties *(Article 10.1)*

### 6.2 POPE Allocation Mechanics

When a POPE exists, both the POPE and the UPE may apply the IIR. The **IIR offset** prevents double taxation *(Article 2.3)*.

### 6.3 Worked Example: POPE Allocation

**Scenario:**
- Stratos Group plc (UK UPE) owns 60% of SG Holdings BV (Netherlands)
- SG Holdings BV qualifies as a POPE (40% third-party ownership)
- SG Holdings BV owns 100% of SG Singapore Tech Pte Ltd (LTCE)
- SG Singapore Tech Top-Up Tax: €300,000

**Step 1: POPE Applies IIR First**

SG Holdings BV (POPE) applies IIR under Article 2.1.4:

| Item | Value |
|------|-------|
| POPE's ownership of LTCE | 100% |
| POPE's Inclusion Ratio | 100% |
| **POPE's Allocable Share** | **€300,000** |

SG Holdings BV pays €300,000 under Netherlands IIR.

**Step 2: UPE Calculates Initial Allocable Share**

Stratos Group plc calculates its share:

| Item | Value |
|------|-------|
| Stratos's ownership of POPE | 60% |
| Stratos's indirect Inclusion Ratio in LTCE | 60% |
| Initial Allocable Share | €300,000 × 60% = €180,000 |

**Step 3: Apply IIR Offset**

Stratos reduces its Allocable Share by the amount already taxed at POPE level:

| Item | Calculation |
|------|-------------|
| Top-Up Tax charged at POPE | €300,000 |
| Stratos's share of POPE charge | 60% × €300,000 = €180,000 |
| **Offset amount** | **€180,000** |

**Step 4: Final UPE Allocable Share**

```
Final Allocable Share = Initial Share − Offset
                      = €180,000 − €180,000
                      = €0
```

**Result:** The IIR offset eliminates Stratos's Top-Up Tax liability. The full €300,000 is collected at the POPE level.

## 7. Multi-Tier Ownership Chain Calculations

For complex structures with multiple ownership levels, calculate the **cumulative Inclusion Ratio** by multiplying through the chain.

### 7.1 Worked Example: Three-Tier Structure

**Stratos Group Structure:**

```
Stratos Group plc (UK) — 100% ownership
    │
    └── SG Holdings Ltd (UK) — 100% ownership
            │
            └── SG Netherlands BV — 80% ownership
                    │
                    └── SG Ireland Ltd (LTCE)
                        Top-Up Tax: €200,000
```

**Cumulative Inclusion Ratio:**

```
Stratos → SG Holdings = 100%
SG Holdings → SG Netherlands = 100%
SG Netherlands → SG Ireland = 80%

Cumulative Ratio = 100% × 100% × 80% = 80%
```

**Allocable Share:**

```
Stratos's Allocable Share = €200,000 × 80% = €160,000
```

**Note:** The remaining €40,000 (20% minority interest at Netherlands level) would be subject to UTPR if not collected under IIR through another chain.

Multi-tier structures require careful tracing of ownership percentages through each level. The cumulative Inclusion Ratio compounds at each step—if each link in the chain is 80%, a four-tier structure yields a cumulative ratio of just 41% (0.8^4). For groups with complex holding structures, the practical implication is that significant portions of Low-Taxed Constituent Entity income may fall outside the IIR's reach, triggering UTPR for the remainder. Groups should map their ownership chains early in the Pillar Two compliance process and identify where cumulative ratios fall below 100%, as these gaps will require UTPR calculations.

## 8. UTPR Allocation Calculation

When UTPR applies to residual Top-Up Tax, the allocation uses a **substance-based formula** *(Article 2.6)*.

### 8.1 UTPR Percentage Formula

**UTPR Percentage = (Employee Factor × 50%) + (Tangible Asset Factor × 50%)**

Where:
- **Employee Factor** = Employees in jurisdiction ÷ Total employees in all UTPR jurisdictions
- **Tangible Asset Factor** = Tangible assets in jurisdiction ÷ Total tangible assets in all UTPR jurisdictions

### 8.2 Worked Example: UTPR Allocation

**Scenario:** €40,000 of Top-Up Tax is not collected under IIR (minority interest). Stratos has operations in three jurisdictions with Qualified UTPR:

| Jurisdiction | Employees | Tangible Assets (€M) |
|--------------|-----------|---------------------|
| UK | 300 | 50.0 |
| Germany | 150 | 30.0 |
| France | 50 | 20.0 |
| **Total** | **500** | **100.0** |

**Step 1: Calculate Employee Factor**

| Jurisdiction | Employees | Employee Factor |
|--------------|-----------|-----------------|
| UK | 300 | 300 ÷ 500 = 60.0% |
| Germany | 150 | 150 ÷ 500 = 30.0% |
| France | 50 | 50 ÷ 500 = 10.0% |

**Step 2: Calculate Tangible Asset Factor**

| Jurisdiction | Tangible Assets | Asset Factor |
|--------------|-----------------|--------------|
| UK | €50.0M | 50 ÷ 100 = 50.0% |
| Germany | €30.0M | 30 ÷ 100 = 30.0% |
| France | €20.0M | 20 ÷ 100 = 20.0% |

**Step 3: Calculate UTPR Percentage**

| Jurisdiction | Employee × 50% | Asset × 50% | **UTPR %** |
|--------------|----------------|-------------|------------|
| UK | 60% × 50% = 30.0% | 50% × 50% = 25.0% | **55.0%** |
| Germany | 30% × 50% = 15.0% | 30% × 50% = 15.0% | **30.0%** |
| France | 10% × 50% = 5.0% | 20% × 50% = 10.0% | **15.0%** |
| **Total** | | | **100.0%** |

**Step 4: Allocate UTPR Top-Up Tax**

| Jurisdiction | UTPR % | Allocated Amount |
|--------------|--------|-----------------|
| UK | 55.0% | €40,000 × 55% = **€22,000** |
| Germany | 30.0% | €40,000 × 30% = **€12,000** |
| France | 15.0% | €40,000 × 15% = **€6,000** |
| **Total** | **100%** | **€40,000** |

## 9. Complete Allocation Workbook Template

### 9.1 Step 1: Jurisdictional Top-Up Tax

| Item | Formula | Amount |
|------|---------|--------|
| A. GloBE Income (net) | Sum of all CE GloBE Income in jurisdiction | € |
| B. Adjusted Covered Taxes | Sum of all CE Covered Taxes | € |
| C. ETR | B ÷ A | % |
| D. Top-Up Tax Percentage | 15% − C (if C < 15%) | % |
| E. Payroll Costs (eligible) | | € |
| F. Tangible Assets (NBV) | | € |
| G. Payroll Carve-Out | E × transition rate | € |
| H. Asset Carve-Out | F × transition rate | € |
| I. Total SBIE | G + H | € |
| J. Excess Profit | A − I | € |
| K. Jurisdictional Top-Up Tax | D × J | € |
| L. Less: QDMTT | | (€) |
| **M. Net Jurisdictional Top-Up Tax** | **K − L** | **€** |

### 9.2 Step 2: Entity Allocation

| Entity | GloBE Income | Share of Positive | Allocated Top-Up Tax |
|--------|--------------|-------------------|---------------------|
| Entity 1 | € | % | € |
| Entity 2 | € | % | € |
| Entity 3 | € | % | € |
| **Total (Positive Only)** | **€** | **100%** | **€** |

### 9.3 Step 3: Parent Allocable Share (IIR)

| Entity | Top-Up Tax | Ownership Chain | Inclusion Ratio | Allocable Share |
|--------|------------|-----------------|-----------------|-----------------|
| Entity 1 | € | UPE → ... → CE | % | € |
| Entity 2 | € | UPE → ... → CE | % | € |
| **Total IIR** | | | | **€** |

### 9.4 Step 4: Residual for UTPR

| Item | Amount |
|------|--------|
| Total Entity Top-Up Tax | € |
| Less: IIR Allocable Shares | (€) |
| **UTPR Top-Up Tax Amount** | **€** |

### 9.5 Step 5: UTPR Allocation

| Jurisdiction | Employees | Assets (€M) | Emp % | Asset % | UTPR % | Allocated |
|--------------|-----------|-------------|-------|---------|--------|-----------|
| Jurisdiction 1 | | € | % | % | % | € |
| Jurisdiction 2 | | € | % | % | % | € |
| **Total** | | **€** | **100%** | **100%** | **100%** | **€** |

## 10. Stratos Example: Complete Allocation

**Scenario:** Stratos has completed its FY 2025 Pillar Two calculations and identified the following:

| Jurisdiction | ETR | Status | Top-Up Tax |
|--------------|-----|--------|------------|
| Singapore | 12.3% | Low-taxed | €2,100,000 |
| Ireland | 14.1% | Low-taxed | €800,000 |
| UK | 23.5% | Above minimum | Nil |
| Germany | 28.2% | Above minimum | Nil |

### 10.1 Singapore Allocation

**Ownership:** Stratos Group plc → SG Holdings Ltd → SG Singapore Pte Ltd (100% throughout)

| Step | Calculation | Result |
|------|-------------|--------|
| Singapore Top-Up Tax | Given | €2,100,000 |
| Entities with positive GloBE Income | SG Singapore Pte Ltd only | 100% |
| Entity allocation | €2,100,000 × 100% | €2,100,000 |
| Stratos's Inclusion Ratio | 100% × 100% | 100% |
| **IIR Allocable Share** | €2,100,000 × 100% | **€2,100,000** |
| UTPR Residual | €2,100,000 − €2,100,000 | €0 |

### 10.2 Ireland Allocation

**Ownership:**
- Stratos Group plc → SG Holdings Ltd → SG Netherlands BV → SG Ireland Ltd (60% at NL level)
- External Investor → SG Ireland Ltd (40%)

| Step | Calculation | Result |
|------|-------------|--------|
| Ireland Top-Up Tax | Given | €800,000 |
| Entity allocation | SG Ireland Ltd only | €800,000 |
| Stratos's cumulative ownership | 100% × 100% × 60% | 60% |
| **IIR Allocable Share** | €800,000 × 60% | **€480,000** |
| External investor share | €800,000 × 40% | €320,000 |
| **UTPR Residual** | | **€320,000** |

### 10.3 UTPR Allocation (Ireland Residual)

| Jurisdiction | Employees | Assets (€M) | Emp % | Asset % | UTPR % | Allocated |
|--------------|-----------|-------------|-------|---------|--------|-----------|
| UK | 450 | 85.0 | 50.0% | 62.5% | 56.3% | €180,160 |
| Germany | 200 | 20.0 | 22.2% | 14.7% | 18.5% | €59,200 |
| France | 150 | 15.0 | 16.7% | 11.0% | 13.9% | €44,480 |
| Netherlands | 100 | 16.0 | 11.1% | 11.8% | 11.5% | €36,800 |
| **Total** | **900** | **136.0** | **100%** | **100%** | **100%** | **€320,640*** |

*Rounding difference

### 10.4 Summary: Stratos FY 2025 Top-Up Tax Liability

| Mechanism | Jurisdiction | Entity Collecting | Amount |
|-----------|--------------|-------------------|--------|
| IIR | UK | Stratos Group plc | €2,580,000 |
| UTPR | UK | SG Holdings Ltd | €180,160 |
| UTPR | Germany | SG Germany GmbH | €59,200 |
| UTPR | France | SG France SAS | €44,480 |
| UTPR | Netherlands | SG Netherlands BV | €36,800 |
| **Total** | | | **€2,900,640** |

## 11. Common Pitfalls

### 11.1 Pitfall 1: Forgetting Loss-Making Entities in Entity Allocation

Loss-making CEs receive **no allocation** of jurisdictional Top-Up Tax. Only CEs with positive GloBE Income participate in the allocation.

### 11.2 Pitfall 2: Using Ownership Percentage as Inclusion Ratio

The Inclusion Ratio is based on **GloBE Income attribution**, not legal ownership percentage. In straightforward structures these align, but with special allocations or profit-sharing arrangements they may differ.

### 11.3 Pitfall 3: Double-Counting POPE Charges

When both UPE and POPE apply IIR, always apply the **IIR offset** to prevent double taxation. The offset equals the UPE's share of the charge already paid at POPE level.

### 11.4 Pitfall 4: Including Non-UTPR Jurisdictions

Only jurisdictions with a **Qualified UTPR** are included in the UTPR allocation. Exclude employees and assets in jurisdictions without UTPR implementation.

### 11.5 Pitfall 5: Mixing Allocation Formulas

IIR uses **ownership-based** allocation (Inclusion Ratio).
UTPR uses **substance-based** allocation (50% employees + 50% tangible assets).
Never mix these formulas.

The allocation calculations in this chapter represent the mechanical heart of Pillar Two compliance. While earlier chapters addressed policy and structure, this chapter provides the numerical workings that determine actual cash tax obligations. For tax departments, these calculations must be repeatable, auditable, and consistent year over year. Developing robust allocation models—whether in spreadsheets, specialised software, or ERP systems—is essential for groups expecting ongoing Pillar Two obligations. The allocation template provided in this chapter offers a starting framework, but each group will need to adapt it to their specific ownership structures, jurisdictional presence, and the particular complexities of their fact patterns.
