# Chapter 2.2: Undertaxed Profits Rule Application

## Learning Objective

After completing this chapter, you will be able to determine when the UTPR applies, calculate the UTPR Top-Up Tax Amount, and allocate it across jurisdictions using the substance-based formula.

## Introduction

If the Income Inclusion Rule is Pillar Two's primary enforcement mechanism, the Undertaxed Profits Rule is its safety net. The UTPR exists because the architects of the global minimum tax recognised that the IIR alone would leave gaps—minority interests not captured by parent entities, groups headquartered in non-implementing jurisdictions, and other scenarios where Top-Up Tax would otherwise go uncollected. The UTPR addresses these gaps through an entirely different mechanism: rather than charging the parent, it denies deductions in jurisdictions where the MNE group has real economic presence. This creates a distributed collection system that, while more complex, ensures the global minimum tax cannot be avoided simply by locating the ultimate parent in a non-cooperating jurisdiction.

## 1. How the UTPR Works

The **Undertaxed Profits Rule (UTPR)** is the backstop mechanism under GloBE. It applies when Top-Up Tax on low-taxed income is **not fully collected** through the Income Inclusion Rule.

The UTPR operates differently from the IIR:
- **IIR:** Parent entity includes Top-Up Tax in its own jurisdiction
- **UTPR:** Top-Up Tax is collected in **other jurisdictions** where the MNE group has operations, through deduction denial or equivalent adjustment

## 2. When Does UTPR Apply?

### 2.1 UTPR Triggers

The UTPR applies when there is **residual Top-Up Tax** not collected under the IIR *(Article 2.5)*. This occurs in three main scenarios:

| Scenario | Why UTPR Applies |
|----------|------------------|
| **No Qualified IIR at UPE level** | UPE jurisdiction has not implemented a Qualified IIR |
| **Low-taxed UPE jurisdiction** | UPE jurisdiction itself is a low-taxed jurisdiction (ETR below 15%) |
| **Split ownership** | Minority interests mean IIR does not capture 100% of Top-Up Tax |

### 2.2 UTPR Priority

The IIR always has priority over the UTPR. The UTPR only applies to the **residual amount** not already taxed under the IIR.

The IIR-first principle reflects both policy and pragmatism. Conceptually, taxing the parent on its subsidiaries' undertaxed income makes intuitive sense—the parent controls and benefits from those subsidiaries. Practically, collecting tax at a single point (the parent entity's jurisdiction) is simpler than distributing collection across multiple jurisdictions. The UTPR's role as residual collector means it operates only at the margins of most groups' Pillar Two calculations, though for groups with UPEs in non-implementing jurisdictions or significant minority interests, it becomes the primary collection mechanism.

**Example:**
- LTCE Top-Up Tax: €1,000,000
- Amount collected under IIR (80% ownership): €800,000
- **UTPR Top-Up Tax Amount: €200,000** (the minority's share)

## 3. Decision Flowchart: Does UTPR Apply?

```
                    ┌─────────────────────────────────┐
                    │ Is there Top-Up Tax for any     │
                    │ Low-Taxed Constituent Entity?   │
                    └───────────────┬─────────────────┘
                                    │
                        ┌───────────┴───────────┐
                        │                       │
                       YES                      NO
                        │                       │
                        ▼                       ▼
            ┌───────────────────────┐   ┌─────────────────┐
            │ Is 100% of the Top-Up │   │ NO UTPR         │
            │ Tax collected under   │   │ (no Top-Up Tax) │
            │ a Qualified IIR?      │   └─────────────────┘
            └───────────┬───────────┘
                        │
            ┌───────────┴───────────┐
            │                       │
           YES                      NO
            │                       │
            ▼                       ▼
    ┌─────────────────┐   ┌─────────────────────────────┐
    │ NO UTPR         │   │ UTPR applies to residual    │
    │ (IIR is         │   │ amount not captured by IIR  │
    │ sufficient)     │   │ (Article 2.5)               │
    └─────────────────┘   └─────────────────────────────┘
```

## 4. Step 1: Calculate the UTPR Top-Up Tax Amount

The **UTPR Top-Up Tax Amount** is the total Top-Up Tax **not collected** under the IIR *(Article 2.5.1)*.

### 4.1 Formula

**UTPR Top-Up Tax Amount = Total Top-Up Tax of all LTCEs − Top-Up Tax collected under IIR**

### 4.2 Worked Example: UTPR Amount Calculation

**Scenario:** Stratos Group has a low-taxed subsidiary in Country X. The UPE jurisdiction (UK) has a Qualified IIR, but Stratos owns only 75% of the subsidiary.

| Item | Amount |
|------|--------|
| Country X Subsidiary Top-Up Tax | €400,000 |
| Stratos's Inclusion Ratio | 75% |
| Top-Up Tax collected under IIR | €400,000 × 75% = €300,000 |
| **UTPR Top-Up Tax Amount** | €400,000 − €300,000 = **€100,000** |

The €100,000 attributable to the 25% minority interest is not collected under the IIR and becomes subject to UTPR.

## 5. Step 2: Identify UTPR Jurisdictions

The UTPR Top-Up Tax Amount is allocated to jurisdictions where:
1. The MNE group has Constituent Entities, AND
2. The jurisdiction has implemented a **Qualified UTPR**

### 5.1 Jurisdictions with Qualified UTPR (as at 2025)

| Jurisdiction | UTPR Status |
|--------------|-------------|
| United Kingdom | Qualified UTPR effective 2025 |
| EU Member States | Qualified UTPR effective 2025 |
| Australia | Qualified UTPR effective 2025 |
| Japan | Qualified UTPR effective 2025 |
| South Korea | Qualified UTPR effective 2025 |
| Canada | Qualified UTPR effective 2025 |

**Note:** UTPR generally takes effect one year after IIR in most implementing jurisdictions. Verify current status through the OECD's published list of qualified jurisdictions.

## 6. Step 3: Calculate UTPR Percentage for Each Jurisdiction

The UTPR Top-Up Tax Amount is allocated using a **substance-based formula** with two equally weighted factors *(Article 2.6)*:

### 6.1 The UTPR Percentage Formula

**UTPR Percentage = (Employee Factor × 50%) + (Tangible Asset Factor × 50%)**

Where:
- **Employee Factor** = Employees in jurisdiction ÷ Total employees in all UTPR jurisdictions
- **Tangible Asset Factor** = Tangible assets in jurisdiction ÷ Total tangible assets in all UTPR jurisdictions

### 6.2 Key Definitions

| Term | Definition |
|------|------------|
| **Employees** | Number of employees (headcount) in the jurisdiction |
| **Tangible Assets** | Net book value of tangible assets (property, plant, equipment) |

**Excluded from tangible assets:** Intangible assets, financial assets, goodwill

The substance-based allocation formula represents a deliberate policy choice about where UTPR collections should flow. By weighting employees and tangible assets equally, the formula directs Top-Up Tax to jurisdictions where the MNE group has genuine economic presence—factories, offices, and workforces—rather than to holding company jurisdictions with minimal real activity. This design serves multiple objectives: it rewards jurisdictions that host substantive operations, it makes UTPR difficult to avoid through paper transactions, and it creates rough proportionality between a jurisdiction's contribution to group value creation and its share of the collected tax. The exclusion of intangibles prevents intellectual property holding jurisdictions from capturing UTPR allocations—a deliberate choice given that IP-heavy structures are often at the heart of the profit-shifting arrangements Pillar Two seeks to address.

## 7. Worked Example: UTPR Allocation Across Jurisdictions

**Scenario:** Stratos Group has a UTPR Top-Up Tax Amount of €100,000 to allocate. The group has Constituent Entities in four jurisdictions with Qualified UTPR.

### 7.1 Step 1: Gather Substance Data

| Jurisdiction | Employees | Tangible Assets (€M) |
|--------------|-----------|---------------------|
| Germany | 200 | 25.0 |
| France | 150 | 20.0 |
| Netherlands | 50 | 10.0 |
| Ireland | 100 | 5.0 |
| **Total** | **500** | **60.0** |

### 7.2 Step 2: Calculate Employee Factor

| Jurisdiction | Employees | Employee Factor |
|--------------|-----------|-----------------|
| Germany | 200 | 200 ÷ 500 = 40.0% |
| France | 150 | 150 ÷ 500 = 30.0% |
| Netherlands | 50 | 50 ÷ 500 = 10.0% |
| Ireland | 100 | 100 ÷ 500 = 20.0% |

### 7.3 Step 3: Calculate Tangible Asset Factor

| Jurisdiction | Tangible Assets | Asset Factor |
|--------------|-----------------|--------------|
| Germany | €25.0M | 25 ÷ 60 = 41.7% |
| France | €20.0M | 20 ÷ 60 = 33.3% |
| Netherlands | €10.0M | 10 ÷ 60 = 16.7% |
| Ireland | €5.0M | 5 ÷ 60 = 8.3% |

### 7.4 Step 4: Calculate UTPR Percentage

| Jurisdiction | Employee Factor × 50% | Asset Factor × 50% | **UTPR %** |
|--------------|----------------------|-------------------|------------|
| Germany | 40.0% × 50% = 20.0% | 41.7% × 50% = 20.8% | **40.8%** |
| France | 30.0% × 50% = 15.0% | 33.3% × 50% = 16.7% | **31.7%** |
| Netherlands | 10.0% × 50% = 5.0% | 16.7% × 50% = 8.3% | **13.3%** |
| Ireland | 20.0% × 50% = 10.0% | 8.3% × 50% = 4.2% | **14.2%** |
| **Total** | | | **100.0%** |

### 7.5 Step 5: Allocate UTPR Top-Up Tax

| Jurisdiction | UTPR % | UTPR Top-Up Tax Allocated |
|--------------|--------|--------------------------|
| Germany | 40.8% | €100,000 × 40.8% = **€40,800** |
| France | 31.7% | €100,000 × 31.7% = **€31,700** |
| Netherlands | 13.3% | €100,000 × 13.3% = **€13,300** |
| Ireland | 14.2% | €100,000 × 14.2% = **€14,200** |
| **Total** | **100%** | **€100,000** |

## 8. Step 4: How UTPR Is Collected

Each jurisdiction collects its allocated UTPR Top-Up Tax through one of two methods *(Article 2.4)*:

### 8.1 Method 1: Denial of Deduction (Most Common)

The jurisdiction denies a tax deduction to the local Constituent Entity, increasing taxable income and generating additional tax equal to the UTPR amount.

**Calculation:**

```
Deduction denied = UTPR allocation ÷ Local tax rate
```

**Example for Germany (30% tax rate):**
- UTPR allocation: €40,800
- Deduction denied: €40,800 ÷ 30% = €136,000
- Additional taxable income: €136,000
- Additional tax: €136,000 × 30% = €40,800 ✓

### 8.2 Method 2: Equivalent Adjustment

The jurisdiction applies an adjustment that achieves the same result as deduction denial (e.g., direct tax charge, deemed income inclusion).

The mechanics of UTPR collection illustrate why this rule is considered more intrusive than the IIR. Rather than simply adding an amount to the parent's tax bill, the UTPR reaches into the local entity's tax computation and alters it—denying deductions that would otherwise be legitimate. This intervention in domestic tax calculations requires careful legislative drafting and can create practical challenges, particularly when determining which specific deductions to deny. The "equivalent adjustment" alternative gives jurisdictions flexibility in implementation, but the end result must be identical: additional tax equal to the UTPR allocation.

## 9. UTPR Carve-Out Rule

A jurisdiction is **excluded** from the UTPR allocation if, in the **prior year**, the UTPR Top-Up Tax allocated to that jurisdiction did not result in an actual cash tax expense *(Article 2.6.3)*.

### 9.1 How the Carve-Out Works

| Prior Year | Current Year Treatment |
|------------|----------------------|
| UTPR allocation resulted in cash tax expense | Jurisdiction remains in UTPR pool |
| UTPR allocation did NOT result in cash tax expense | UTPR Percentage = 0% for next year |

**Exception:** The carve-out does not apply if **all** UTPR jurisdictions would have a UTPR Percentage of zero (i.e., at least one jurisdiction must remain in the pool).

### 9.2 Why This Matters

Some jurisdictions may not be able to collect UTPR through their domestic law mechanisms. The carve-out ensures UTPR is reallocated to jurisdictions that can actually collect it.

## 10. Transitional UTPR Safe Harbour

### 10.1 Overview

During the transition period, the UTPR **does not apply** to the UPE jurisdiction if that jurisdiction has a corporate tax rate of **at least 20%** *(Transitional Safe Harbour)*.

### 10.2 Transition Period

- Fiscal years beginning on or before **31 December 2025**
- Fiscal years ending before **31 December 2026**

### 10.3 Practical Effect

For most MNE groups with UPEs in major developed economies (UK, US, most EU countries, Japan, etc.), **no UTPR applies to the UPE jurisdiction** during the transition period.

**Example:** Stratos Group plc has its UPE in the UK (25% corporate tax rate). During the transition period, even if the UK were a low-taxed jurisdiction (hypothetically), the UTPR would not apply to collect Top-Up Tax from UK-based Constituent Entities in respect of UK-parented low-taxed income.

### 10.4 After Transition Period

From 2026 onwards, the safe harbour no longer applies. UTPR may apply to UPE jurisdictions regardless of their statutory tax rate.

The transitional safe harbour reflects diplomatic sensitivity around the UTPR's potential reach. Without it, the UTPR could—in the early years of Pillar Two—impose additional tax on groups headquartered in countries that have not yet implemented domestic legislation, effectively allowing implementing countries to tax income connected to non-implementing jurisdictions. This raised sovereignty concerns, particularly in the United States, which has been slower to adopt Pillar Two than the EU or other major economies. The safe harbour provides breathing room for countries to implement, while the 20% threshold ensures it benefits only jurisdictions with genuinely substantive tax systems. After the transition period, the full UTPR applies—creating pressure for remaining holdouts to join the framework or see their groups' undertaxed income subject to UTPR collection elsewhere.

## 11. UTPR and QDMTT Interaction

### 11.1 QDMTT Priority

If a low-taxed jurisdiction has implemented a **Qualified Domestic Minimum Top-Up Tax (QDMTT)**, the QDMTT is collected **first**. The UTPR only applies to the residual amount not collected by the QDMTT.

**Order of application:**
1. QDMTT (collected in the low-taxed jurisdiction)
2. IIR (collected at parent level)
3. UTPR (collected in other jurisdictions—only if residual remains)

### 11.2 Worked Example: QDMTT Reduces UTPR

**Scenario:**
- Low-taxed jurisdiction Top-Up Tax: €500,000
- QDMTT collected locally: €500,000
- IIR Allocable Share: €0 (QDMTT already collected full amount)
- **UTPR Top-Up Tax Amount: €0**

The QDMTT fully addresses the undertaxation, leaving nothing for IIR or UTPR.

## 12. Stratos Example: Complete UTPR Analysis

**Scenario:** Stratos has identified a UTPR Top-Up Tax Amount of €200,000 arising from a low-taxed entity where Stratos has only 60% ownership (minority interest not subject to IIR).

### 12.1 Stratos's UTPR Jurisdictions

| Jurisdiction | Employees | Tangible Assets (€M) | Qualified UTPR? |
|--------------|-----------|---------------------|-----------------|
| UK | 450 | 85.0 | Yes |
| Germany | 200 | 25.0 | Yes |
| France | 150 | 20.0 | Yes |
| Singapore | 180 | 30.0 | No |
| Ireland | 100 | 5.0 | Yes |

**Note:** Singapore is excluded as it has not implemented a Qualified UTPR.

### 12.2 UTPR Calculation (Excluding Singapore)

| Jurisdiction | Employees | Assets (€M) | Employee % | Asset % | UTPR % |
|--------------|-----------|-------------|-----------|---------|--------|
| UK | 450 | 85.0 | 50.0% | 63.0% | 56.5% |
| Germany | 200 | 25.0 | 22.2% | 18.5% | 20.4% |
| France | 150 | 20.0 | 16.7% | 14.8% | 15.8% |
| Ireland | 100 | 5.0 | 11.1% | 3.7% | 7.4% |
| **Total** | **900** | **135.0** | **100%** | **100%** | **100%** |

### 12.3 UTPR Allocation

| Jurisdiction | UTPR % | Allocated Amount |
|--------------|--------|-----------------|
| UK | 56.5% | €113,000 |
| Germany | 20.4% | €40,800 |
| France | 15.8% | €31,600 |
| Ireland | 7.4% | €14,800 |
| **Total** | **100%** | **€200,200*** |

*Rounding difference

### 12.4 Impact on Stratos's UK Subsidiary

SG Holdings Ltd (UK) will have a deduction denied:
- UTPR allocation: €113,000
- UK tax rate: 25%
- Deduction denied: €113,000 ÷ 25% = €452,000

This increases SG Holdings Ltd's UK taxable income by €452,000, generating €113,000 additional UK corporation tax.

## 13. Common Pitfalls

### 13.1 Pitfall 1: Including Non-UTPR Jurisdictions

Only jurisdictions with a **Qualified UTPR** are included in the allocation. Exclude entities in jurisdictions without UTPR legislation.

### 13.2 Pitfall 2: Using Wrong Asset Base

Tangible assets means **net book value** of property, plant, and equipment only. Do not include intangibles, financial assets, or goodwill.

### 13.3 Pitfall 3: Forgetting the Carve-Out

If a jurisdiction did not collect its UTPR allocation in the prior year (no cash tax expense), exclude it from the current year calculation.

### 13.4 Pitfall 4: Ignoring QDMTT Priority

Always check if the low-taxed jurisdiction has a QDMTT. If so, calculate UTPR only on the residual after QDMTT.

### 13.5 Pitfall 5: Applying UTPR During Transition Period

During the transition period (through 2025/2026), the UTPR safe harbour applies to UPE jurisdictions with ≥20% tax rate. Don't calculate UTPR for the UPE jurisdiction in these years.

The UTPR represents perhaps the most innovative—and controversial—element of the Pillar Two architecture. Its substance-based allocation formula, deduction denial mechanics, and distributed collection across multiple jurisdictions mark a significant departure from traditional international tax principles, which generally respect the primacy of residence and source taxation. For practitioners, the UTPR demands careful attention to which jurisdictions have implemented qualified rules, to the annual updating of employee and asset data, and to the interplay with QDMTT and IIR. For MNE groups, it underscores the importance of the IIR capturing as much Top-Up Tax as possible at the parent level—avoiding the fragmentation and complexity that UTPR collection entails.
