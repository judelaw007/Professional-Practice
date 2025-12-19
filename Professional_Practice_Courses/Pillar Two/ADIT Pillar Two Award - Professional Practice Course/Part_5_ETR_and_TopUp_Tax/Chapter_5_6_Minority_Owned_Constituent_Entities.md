# Chapter 5.6: Minority-Owned Constituent Entities

## Learning Objective

After completing this chapter, you will be able to identify Minority-Owned Constituent Entities (MOCEs), apply the separate ETR calculation requirement, compute Top-Up Tax for MOCEs and Minority-Owned Sub-Groups, and allocate Top-Up Tax liability between the main MNE Group and minority interests.

## Introduction

The standard jurisdictional blending approach works well when an MNE Group wholly owns its Constituent Entities—the group benefits from the income and bears the tax burden in proportionate measure. However, corporate structures frequently include entities where the Ultimate Parent Entity holds control but minority shareholders retain significant economic interests. Joint ventures, partially-owned subsidiaries consolidated under variable interest arrangements, and entities controlled through voting agreements all present situations where the economic ownership diverges from accounting consolidation. The MOCE rules address this divergence by carving out entities with 30% or less ownership from standard jurisdictional blending.

This chapter examines how Minority-Owned Constituent Entities receive separate treatment under Article 5.6. Understanding these rules is essential because failing to identify and correctly process MOCEs can lead to material errors in ETR calculations—either by inappropriately blending MOCE results with the main group or by miscalculating the Top-Up Tax allocation. The complexity increases when MOCEs form their own sub-groups with tiered ownership structures. Practitioners must develop systematic processes for identifying MOCEs at the outset of GloBE compliance work and applying the separate calculation methodology correctly.

## 1. Why Separate Treatment for MOCEs?

The standard jurisdictional blending rule combines all Constituent Entities in a jurisdiction for ETR calculation. This creates a problem for minority-owned entities:

```
┌─────────────────────────────────────────────────────────────────────┐
│ THE PROBLEM WITHOUT SEPARATE TREATMENT                              │
│                                                                     │
│ If UPE owns only 25% of Entity X:                                  │
│ → 75% of Entity X's income belongs to OTHER shareholders           │
│ → But jurisdictional blending includes 100% of Entity X            │
│ → This could trigger Top-Up Tax that minority shareholders         │
│   shouldn't bear                                                    │
│                                                                     │
│ OR                                                                  │
│                                                                     │
│ → Entity X's high ETR could shield OTHER entities from Top-Up Tax  │
│ → The UPE benefits from taxes paid by minority shareholders        │
└─────────────────────────────────────────────────────────────────────┘
```

**Solution:** MOCEs are **excluded** from standard jurisdictional blending and have their own separate ETR calculation.

The separate treatment reflects a fundamental principle of equity within the GloBE framework. When minority shareholders hold 70% or more of an entity's economic interest, it would be inappropriate for the UPE to benefit from that entity's taxes shielding other group income from Top-Up Tax—taxes that minority shareholders effectively bore. Equally, minority shareholders should not be indirectly burdened by Top-Up Tax triggered because the MOCE's low rate dragged down a jurisdictional ETR calculated across entities they have no stake in. By requiring separate calculation, the rules ensure that each MOCE stands on its own merits, with its ETR determined independently and any Top-Up Tax attributable specifically to its undertaxed profits.

## 2. Definition: Minority-Owned Constituent Entity (Article 10.1)

A **Minority-Owned Constituent Entity (MOCE)** is a Constituent Entity where:

1. The UPE holds **directly or indirectly 30% or less** of the Ownership Interests, **AND**
2. The entity is **consolidated** in the MNE Group's financial statements (i.e., UPE has control)

```
┌─────────────────────────────────────────────────────────────────────┐
│                     MOCE QUALIFICATION                              │
│                                                                     │
│  Ownership Interest ≤ 30%  +  Consolidation (Control)  =  MOCE     │
│                                                                     │
│  If ownership > 30%: NOT a MOCE (standard blending applies)        │
│  If no control: NOT a Constituent Entity at all                    │
└─────────────────────────────────────────────────────────────────────┘
```

### 2.1 Calculating Indirect Ownership

The 30% test considers **both direct and indirect** ownership:

**Example: Indirect Ownership Calculation**

```
        UPE (100%)
         │
         ▼
      HoldCo (60% owned by UPE)
         │
         ▼
      SubCo (40% owned by HoldCo)

UPE's indirect ownership in SubCo = 60% × 40% = 24%

Since 24% ≤ 30% and SubCo is consolidated → SubCo is a MOCE
```

### 2.2 Control Without Majority Ownership

MOCEs arise when accounting standards require consolidation despite ≤30% ownership. Common scenarios:

| Scenario | Ownership | Why Consolidated? |
|----------|-----------|-------------------|
| Voting control | 25% equity | UPE controls board through voting agreements |
| Variable interest entity | 20% equity | UPE is primary beneficiary under IFRS 10/ASC 810 |
| De facto control | 28% equity | Remaining ownership widely dispersed |
| Contractual arrangements | 15% equity | Management contracts give effective control |

The scenarios where MOCE status arises highlight the tension between accounting consolidation and economic ownership. Modern financial reporting standards—IFRS 10 and ASC 810—focus on control rather than majority ownership when determining consolidation. A company might consolidate an entity in which it holds only 20% of the equity because it serves as the primary beneficiary of a variable interest entity, controls the entity through contractual arrangements, or exercises de facto control due to dispersed minority holdings. While such consolidation makes sense for financial reporting purposes—presenting a complete picture of the economic activities the parent controls—it creates mismatches for tax purposes where economic ownership traditionally determines who bears the tax burden. The MOCE rules bridge this gap by requiring separate calculation for entities where consolidation exists but majority economic ownership does not.

## 3. Related Definitions

### 3.1 Minority-Owned Parent Entity (MOPE)

A **Minority-Owned Parent Entity** is a MOCE that:
- Holds **ownership interests** in other MOCEs, **AND**
- Is **not** owned (directly or indirectly) by another MOCE

### 3.2 Minority-Owned Sub-Group

A **Minority-Owned Sub-Group** consists of:
- A Minority-Owned Parent Entity (MOPE), **AND**
- All MOCEs in which the MOPE holds (directly or indirectly) ownership interests

```
                    UPE (100%)
                     │
                     ▼ (owns 25%)
              ┌─────────────┐
              │    MOPE     │  ← Minority-Owned Parent Entity
              │ (Ireland)   │     (25% owned by UPE)
              └─────────────┘
                     │
           ┌─────────┴─────────┐
           ▼ (100%)            ▼ (100%)
    ┌──────────────┐    ┌──────────────┐
    │  MOCE Sub 1  │    │  MOCE Sub 2  │  ← Minority-Owned Subsidiaries
    │  (Ireland)   │    │  (Germany)   │
    └──────────────┘    └──────────────┘

    └──────────────────────────────────┘
              Minority-Owned Sub-Group
```

The distinction between MOPEs and stand-alone MOCEs matters for determining the calculation methodology. A stand-alone MOCE—one without any subsidiaries—has its ETR calculated on an individual entity basis. A MOPE, by contrast, heads a Minority-Owned Sub-Group that is treated as if it were a separate MNE Group for GloBE purposes. This means jurisdictional blending applies within the sub-group: if the MOPE in Ireland has a wholly-owned subsidiary also in Ireland, those two entities blend their results for the sub-group's Ireland ETR calculation—but entirely separately from any main group entities that might also be located in Ireland. The sub-group effectively operates as a parallel GloBE calculation track.

## 4. Separate ETR Calculation (Article 5.6)

### 4.1 Two Categories of MOCEs

| Category | Treatment | Article |
|----------|-----------|---------|
| **MOCE in a Minority-Owned Sub-Group** | Sub-Group treated as separate MNE Group | 5.6.1 |
| **Stand-alone MOCE** (not in a Sub-Group) | Entity-level separate ETR | 5.6.2 |

### 4.2 Article 5.6.1: Minority-Owned Sub-Groups

When a Minority-Owned Sub-Group exists:

```
┌─────────────────────────────────────────────────────────────────────┐
│ MINORITY-OWNED SUB-GROUP TREATMENT                                  │
│                                                                     │
│ The Minority-Owned Sub-Group is treated as if it were a            │
│ SEPARATE MNE GROUP for purposes of:                                 │
│                                                                     │
│ → Jurisdictional blending (within the sub-group only)              │
│ → ETR calculation                                                   │
│ → SBIE calculation                                                  │
│ → Top-Up Tax calculation                                           │
│                                                                     │
│ The Sub-Group's income and taxes are EXCLUDED from the             │
│ main MNE Group's jurisdictional calculations.                      │
└─────────────────────────────────────────────────────────────────────┘
```

### 4.3 Article 5.6.2: Stand-Alone MOCEs

If a MOCE is **not** part of a Minority-Owned Sub-Group:

```
┌─────────────────────────────────────────────────────────────────────┐
│ STAND-ALONE MOCE TREATMENT                                          │
│                                                                     │
│ The MOCE's Adjusted Covered Taxes and GloBE Income or Loss are:    │
│                                                                     │
│ → EXCLUDED from the main group's jurisdictional ETR                │
│ → Calculated SEPARATELY on an entity-by-entity basis               │
│                                                                     │
│ Each stand-alone MOCE has its own individual ETR calculation.      │
└─────────────────────────────────────────────────────────────────────┘
```

## 5. Multiple ETR Calculations Per Jurisdiction

MOCE rules can result in **multiple ETR calculations** for the same jurisdiction:

**Example: Ireland with Three ETR Calculations**

```
Ireland Jurisdiction
├── Main MNE Group entities (standard blending)
│   ├── Ireland OpCo 1
│   └── Ireland OpCo 2
│   └── ETR Calculation #1: Main Group Ireland
│
├── Minority-Owned Sub-Group
│   ├── MOPE Ireland
│   └── MOCE Sub Ireland
│   └── ETR Calculation #2: MO Sub-Group Ireland
│
└── Stand-alone MOCE
    └── Ireland JV Co (25% owned, no subsidiaries)
    └── ETR Calculation #3: Stand-alone MOCE
```

The possibility of multiple ETR calculations for a single jurisdiction represents one of the more complex aspects of GloBE compliance. Practitioners accustomed to thinking in terms of "the Ireland ETR" must adjust their mental model to recognise that there may be several Ireland ETRs within the same MNE Group. Documentation and calculation systems need to track which entities fall into which calculation pool. Errors at this stage—misclassifying an entity as main group when it should be MOCE, or vice versa—propagate through all subsequent calculations. Robust entity classification at the start of the GloBE process, with clear documentation of ownership percentages and consolidation bases, becomes essential for managing this complexity.

## 6. Worked Example: MOCE ETR Computation

### 6.1 Scenario

**Stratos Group** has a 28% ownership interest in **Atlas Ireland Ltd**, a consolidated entity providing shared services. Atlas Ireland Ltd is a stand-alone MOCE (no subsidiaries).

### 6.2 Step 1: Identify MOCE Status

| Test | Assessment |
|------|------------|
| UPE ownership interest | 28% (direct) |
| Is ≤ 30%? | Yes |
| Is entity consolidated? | Yes (control through management contract) |
| Part of Minority-Owned Sub-Group? | No (no MOCE subsidiaries) |
| **Classification** | **Stand-alone MOCE** |

### 6.3 Step 2: Calculate Separate ETR

**Atlas Ireland Ltd Data:**

| Item | Amount |
|------|--------|
| GloBE Income | €2,400,000 |
| Adjusted Covered Taxes | €288,000 |

**ETR Calculation:**

```
ETR = Adjusted Covered Taxes / GloBE Income
ETR = €288,000 / €2,400,000
ETR = 12.00%
```

### 6.4 Step 3: Apply SBIE (Separately)

**Atlas Ireland Ltd Substance:**

| Item | Amount | Rate (2025) | Carve-out |
|------|--------|-------------|-----------|
| Eligible Payroll | €1,200,000 | 9.8% | €117,600 |
| Tangible Assets (NBV) | €800,000 | 7.8% | €62,400 |
| **Total SBIE** | | | **€180,000** |

**Excess Profit:**

```
Excess Profit = GloBE Income − SBIE
Excess Profit = €2,400,000 − €180,000
Excess Profit = €2,220,000
```

### 6.5 Step 4: Calculate Top-Up Tax

```
Top-Up Tax % = 15% − 12% = 3%

Top-Up Tax = 3% × €2,220,000 = €66,600
```

### 6.6 Step 5: Apply QDMTT Offset (If Applicable)

Ireland has QDMTT. Assume Ireland collects the full Top-Up Tax domestically:

```
QDMTT Paid:         €66,600
Net Top-Up Tax:     €0
```

**Result:** Ireland retains the €66,600 through its QDMTT.

### 6.7 Comparison: Main Group vs MOCE

| Calculation | Main Group Ireland | Stand-alone MOCE |
|-------------|-------------------|------------------|
| Entities included | Ireland OpCo 1, OpCo 2 | Atlas Ireland Ltd only |
| GloBE Income | €15,000,000 | €2,400,000 |
| ETR | 11.80% | 12.00% |
| Top-Up Tax % | 3.20% | 3.00% |
| Jurisdictional Top-Up Tax | €426,394 | €66,600 |
| QDMTT offset | (€426,394) | (€66,600) |
| Net Top-Up Tax | €0 | €0 |

**Key insight:** Without MOCE separation, Atlas Ireland's 12% ETR would have been blended with the main group's 11.80%, potentially affecting both calculations unfairly.

The Atlas Ireland example illustrates both the mechanics and the policy rationale of MOCE treatment. If Atlas Ireland's 12% ETR were blended with the main group's 11.80% Ireland ETR, the combined result would be a weighted average somewhere between these figures—slightly higher than 11.80%. This would marginally reduce the main group's Top-Up Tax liability, with the benefit flowing to Stratos despite the fact that 72% of Atlas Ireland's taxes were economically borne by minority shareholders who have no stake in the main group's Ireland operations. The separate calculation prevents this cross-subsidisation. Importantly, Ireland's QDMTT captures both Top-Up Tax amounts (€426,394 for main group, €66,600 for the MOCE), meaning the revenue stays in Ireland regardless of the separate calculation requirement—but the separate calculation ensures accurate attribution of the minimum tax burden.

## 7. Minority-Owned Sub-Group Example

### 6.1 Scenario

**Stratos Group** owns 22% of **Nexus Holdings BV** (Netherlands), which owns 100% of **Nexus Germany GmbH**. Nexus Holdings BV is consolidated due to Stratos's board control.

### 7.2 Structure

```
Stratos Holdings plc (UPE)
         │
         ▼ (22% ownership, board control)
┌─────────────────────────┐
│   Nexus Holdings BV     │  ← MOPE (Netherlands)
│   (Netherlands)         │
└─────────────────────────┘
         │
         ▼ (100% owned by MOPE)
┌─────────────────────────┐
│   Nexus Germany GmbH    │  ← Minority-Owned Subsidiary
│   (Germany)             │
└─────────────────────────┘

Minority-Owned Sub-Group: Nexus Holdings BV + Nexus Germany GmbH
```

### 7.3 Calculation: Sub-Group as Separate MNE

**Step 1: Netherlands ETR (MOPE)**

| Item | Amount |
|------|--------|
| GloBE Income (MOPE) | €1,800,000 |
| Adjusted Covered Taxes | €450,000 |
| ETR | 25.00% |

**Result:** ETR ≥ 15% → No Top-Up Tax for Netherlands within Sub-Group.

**Step 2: Germany ETR (Sub-Group Member)**

| Item | Amount |
|------|--------|
| GloBE Income (Nexus Germany) | €3,500,000 |
| Adjusted Covered Taxes | €980,000 |
| ETR | 28.00% |

**Result:** ETR ≥ 15% → No Top-Up Tax for Germany within Sub-Group.

### 7.4 Main Group Germany (Separate Calculation)

Stratos's main group also has entities in Germany (SG Germany GmbH):

| Calculation | Main Group Germany | Sub-Group Germany |
|-------------|-------------------|-------------------|
| Entities | SG Germany GmbH | Nexus Germany GmbH |
| GloBE Income | €50,000,000 | €3,500,000 |
| ETR | 23.00% | 28.00% |
| Top-Up Tax | €0 | €0 |

**Important:** Nexus Germany GmbH is **excluded** from Main Group Germany's blending.

The Nexus Sub-Group example demonstrates how the MOCE rules create entirely parallel calculation tracks within a single MNE Group. Stratos effectively runs two complete GloBE calculations: one for its main group (which includes its wholly-owned subsidiaries across various jurisdictions) and one for the Nexus Sub-Group (comprising Nexus Holdings BV and Nexus Germany GmbH, treated as if they were a separate MNE). The sub-group's high ETRs (25% in Netherlands, 28% in Germany) result in no Top-Up Tax for either jurisdiction within the sub-group. Meanwhile, the main group's Germany calculation covers only SG Germany GmbH. If Nexus Germany's 28% ETR were incorrectly included in the main group's Germany blending, it would artificially inflate the main group's Germany ETR—potentially shielding any German entities that might otherwise be low-taxed.

## 8. Top-Up Tax Allocation for MOCEs

### 8.1 Who Pays the Top-Up Tax?

| Entity Type | Who Bears Top-Up Tax? | Mechanism |
|-------------|----------------------|-----------|
| **Stand-alone MOCE** | UPE of main MNE Group | IIR |
| **MOPE (Sub-Group parent)** | UPE of main MNE Group | IIR |
| **Minority-Owned Subsidiary** | MOPE (Sub-Group parent) | IIR within Sub-Group |

### 8.2 Allocation Logic

```
                      UPE (Stratos Holdings plc)
                            │
         ┌──────────────────┼──────────────────┐
         │                  │                  │
         ▼                  ▼                  ▼
    Main Group         Stand-alone          MOPE
    Subsidiaries         MOCE             (Sub-Group)
                                              │
    Top-Up Tax:       Top-Up Tax:            │
    UPE pays          UPE pays               ▼
    via IIR           via IIR           Sub-Group
                                         Subsidiaries
                                              │
                                         Top-Up Tax:
                                         MOPE pays (as POPE)
                                         via IIR within Sub-Group
```

### 8.3 Attribution Based on Ownership

Even though the UPE bears Top-Up Tax for a MOCE, the **amount** reflects only the UPE's ownership share in the GloBE Income:

```
UPE's Top-Up Tax Attribution = Top-Up Tax × UPE's Ownership %

Example: Atlas Ireland Ltd
- Total MOCE Top-Up Tax: €66,600
- UPE ownership: 28%
- UPE's attributed Top-Up Tax: €66,600 × 28% = €18,648

Note: The full €66,600 is still computed and potentially collected
      via QDMTT, but the UPE's economic exposure is 28%.
```

The allocation mechanics reveal an important nuance: while the UPE bears the legal obligation to pay Top-Up Tax on MOCEs through IIR, the economic burden should be understood in proportion to ownership. The full €66,600 Top-Up Tax exists because Atlas Ireland's overall operations generated undertaxed excess profits. Where Ireland collects this through QDMTT, the tax is paid locally by Atlas Ireland itself (reducing returns available to all shareholders proportionally). Where IIR applies instead (in jurisdictions without QDMTT), the UPE pays but its economic exposure is limited to its ownership share. In practice, joint venture agreements and shareholder arrangements may need to address how GloBE Top-Up Tax obligations are shared among the various parties with interests in the MOCE.

## 9. MOCE Interaction with Other Rules

### 9.1 De Minimis Exclusion

MOCEs **are included** in the De Minimis calculation:

| Rule | Treatment of MOCE |
|------|-------------------|
| **De Minimis thresholds** | MOCE revenue and income **included** in jurisdiction totals |
| **ETR calculation** | MOCE **excluded** from standard blending |

**Practical effect:** A jurisdiction might qualify for De Minimis including MOCE amounts, but MOCEs would still have separate calculations if De Minimis doesn't apply.

### 9.2 QDMTT

For a QDMTT to be **Qualified**, it must:
- Apply separate calculations for MOCEs
- Not blend MOCE income with main group

If a jurisdiction's domestic minimum tax doesn't follow MOCE separation, it **does not qualify** as a QDMTT.

### 9.3 Investment Entities

If a MOCE is an **Investment Entity**:
- MOCE rules do **not** apply
- Investment Entity rules (Articles 7.4/7.5) take **priority**

| Entity Type | Applicable Rules |
|-------------|------------------|
| MOCE (not Investment Entity) | Article 5.6 |
| MOCE that is Investment Entity | Articles 7.4/7.5 (priority) |

The interaction between MOCE rules and other GloBE provisions requires careful attention to ordering. For De Minimis purposes, MOCE revenue and income count toward the jurisdictional thresholds—this ensures that the De Minimis exclusion reflects the full scope of group activity in a jurisdiction, not artificially reduced figures that exclude MOCEs. However, if the jurisdiction does not qualify for De Minimis, the MOCE then receives separate ETR treatment. The Investment Entity priority rule addresses situations where an entity might technically meet both definitions: if it is both a MOCE (≤30% ownership, consolidated) and an Investment Entity (meeting the Article 7.4 criteria), the Investment Entity rules take precedence because they provide specialised treatment designed for the particular circumstances of investment funds and similar vehicles.

## 10. Decision Flowchart: MOCE Identification and Treatment

```
START: Constituent Entity identified
        │
        ▼
┌───────────────────────────────────────────────────┐
│ Does UPE hold ≤ 30% ownership interest            │
│ (direct + indirect)?                              │
└───────────────────────────────────────────────────┘
        │
   ┌────┴────┐
   NO       YES
   │         │
   ▼         ▼
┌────────┐  ┌───────────────────────────────────────┐
│Standard│  │ Is entity consolidated in MNE Group   │
│blending│  │ financial statements?                 │
│applies │  └───────────────────────────────────────┘
└────────┘          │
               ┌────┴────┐
               NO       YES
               │         │
               ▼         ▼
        ┌────────┐  ┌───────────────────────────────┐
        │Not a   │  │ Is entity an Investment Entity?│
        │CE      │  └───────────────────────────────┘
        └────────┘          │
                       ┌────┴────┐
                      YES       NO
                       │         │
                       ▼         ▼
                ┌────────┐  ┌───────────────────────┐
                │Apply   │  │ MOCE IDENTIFIED       │
                │Inv.    │  │                       │
                │Entity  │  │ Does MOCE have        │
                │rules   │  │ ownership in other    │
                │(7.4/   │  │ MOCEs?                │
                │7.5)    │  └───────────────────────┘
                └────────┘          │
                               ┌────┴────┐
                               NO       YES
                               │         │
                               ▼         ▼
                   ┌──────────────┐  ┌──────────────┐
                   │Stand-alone   │  │MOPE          │
                   │MOCE          │  │(Sub-Group)   │
                   │              │  │              │
                   │Entity-level  │  │Sub-Group     │
                   │separate ETR  │  │as separate   │
                   │(Art. 5.6.2)  │  │MNE Group     │
                   └──────────────┘  │(Art. 5.6.1)  │
                                     └──────────────┘
```

## 11. Common Pitfalls

### 11.1 Pitfall 1: Including MOCEs in Standard Blending

**Error:** Including MOCE's Covered Taxes and GloBE Income in the main group's jurisdictional ETR.

**Correct approach:** Always exclude MOCEs from standard blending; calculate separately.

### 11.2 Pitfall 2: Forgetting Indirect Ownership

**Error:** Only considering direct ownership when applying the 30% test.

**Correct approach:** Calculate ownership through all tiers:
```
Indirect ownership = Product of ownership at each tier
Example: 60% × 40% = 24% indirect ownership
```

### 11.3 Pitfall 3: Treating Investment Entity MOCEs Under Article 5.6

**Error:** Applying MOCE separate calculation to an entity that is both a MOCE and an Investment Entity.

**Correct approach:** Investment Entity rules (Articles 7.4/7.5) take priority over MOCE rules.

### 11.4 Pitfall 4: Excluding MOCEs from De Minimis Calculation

**Error:** Not including MOCE revenue and income when calculating De Minimis thresholds.

**Correct approach:** Include MOCEs in De Minimis calculation (different from ETR blending treatment).

### 11.5 Pitfall 5: Allocating Wrong Top-Up Tax Amount

**Error:** Allocating 100% of MOCE Top-Up Tax to the UPE without considering ownership percentage.

**Correct approach:** While the UPE bears the tax obligation, attribution for economic purposes is based on ownership share.

## 12. MOCE Assessment Checklist

Use this checklist to identify and process MOCEs:

```
MOCE IDENTIFICATION AND CALCULATION CHECKLIST
Entity: _________________________
Jurisdiction: _________________________
Fiscal Year: _________________________

PART A: MOCE IDENTIFICATION

□ Step 1: Calculate UPE Ownership
   □ Direct ownership: __________%
   □ Indirect ownership calculation:
     Tier 1: _____% × Tier 2: _____% × Tier 3: _____% = _____%
   □ Total (direct + indirect): __________%
   □ Is total ≤ 30%? YES / NO

   If NO → Standard blending applies. STOP.

□ Step 2: Confirm Consolidation
   □ Is entity consolidated in MNE Group financials? YES / NO
   □ Basis for consolidation: _________________________

   If NO → Not a Constituent Entity. STOP.

□ Step 3: Check Investment Entity Status
   □ Is entity an Investment Entity? YES / NO

   If YES → Apply Investment Entity rules (Articles 7.4/7.5). STOP.

□ Step 4: Determine MOCE Type
   □ Does entity own interests in other MOCEs? YES / NO

   If YES → Entity is a MOPE; apply Sub-Group treatment (Article 5.6.1)
   If NO  → Entity is a Stand-alone MOCE (Article 5.6.2)

PART B: SEPARATE CALCULATION (Stand-alone MOCE)

□ GloBE Income:                     €__________________
□ Adjusted Covered Taxes:           €__________________
□ ETR (Taxes ÷ Income):             __________________%

   If ETR ≥ 15%: No Top-Up Tax. STOP.

□ SBIE Calculation (separate):
   □ Eligible Payroll:              €__________________
   □ Payroll Carve-out (@9.8%):     €__________________
   □ Tangible Assets (NBV):         €__________________
   □ Asset Carve-out (@7.8%):       €__________________
   □ Total SBIE:                    €__________________

□ Excess Profit (Income − SBIE):    €__________________
□ Top-Up Tax % (15% − ETR):         __________________%
□ MOCE Top-Up Tax:                  €__________________

□ QDMTT Offset (if applicable):    (€__________________)
□ Net Top-Up Tax:                   €__________________

PART C: SUB-GROUP CALCULATION (If MOPE)

□ List all entities in Minority-Owned Sub-Group:
   1. MOPE: _________________________
   2. Subsidiary: _________________________
   3. Subsidiary: _________________________

□ Apply full GloBE calculations as if Sub-Group were separate MNE:
   □ Jurisdictional blending within Sub-Group
   □ Separate SBIE for Sub-Group
   □ Separate Top-Up Tax for Sub-Group

PART D: TOP-UP TAX ATTRIBUTION

□ Total MOCE/Sub-Group Top-Up Tax:  €__________________
□ UPE Ownership %:                  __________________%
□ UPE Attributed Share:             €__________________
□ Mechanism: IIR / QDMTT offset
```

## Concluding Discussion

The MOCE rules represent one of the more technically demanding aspects of GloBE compliance, requiring careful analysis of ownership structures and consolidation bases that may not be immediately apparent from standard tax documentation. Many MNE Groups include entities consolidated under control principles that result in minority economic ownership—joint ventures, variable interest entities, and arrangements where voting control differs from equity ownership. Each such entity must be evaluated against the MOCE criteria, with separate calculation tracks established where the 30% threshold is met.

For practitioners, the MOCE rules demand integration between tax and accounting functions. The determination of whether an entity is consolidated—and on what basis—typically resides with the financial reporting team. The calculation of direct and indirect ownership percentages requires tracing through potentially complex ownership chains. Once MOCEs are identified, the GloBE calculation effectively bifurcates into main group and MOCE/sub-group tracks, each requiring its own jurisdictional blending, ETR computation, SBIE calculation, and Top-Up Tax determination. Documentation must clearly identify which entities fall into which calculation pool and demonstrate that the separate calculations were performed correctly.

Looking forward, the MOCE rules may become increasingly relevant as MNE Groups adapt their structures to the Pillar Two environment. Joint ventures and minority investments have traditionally offered flexibility in structuring, but the GloBE implications of such arrangements now require explicit consideration. An entity that qualifies as a MOCE cannot benefit from blending with higher-taxed main group entities in the same jurisdiction—its low-tax status stands alone. Conversely, high-taxed MOCEs cannot shield main group entities from Top-Up Tax exposure. Understanding these dynamics becomes essential for both compliance accuracy and strategic structuring decisions in the post-GloBE landscape.

