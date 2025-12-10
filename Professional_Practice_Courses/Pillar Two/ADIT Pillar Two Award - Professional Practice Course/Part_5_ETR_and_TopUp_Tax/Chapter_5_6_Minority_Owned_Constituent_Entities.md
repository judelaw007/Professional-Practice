# Chapter 5.6: Minority-Owned Constituent Entities

## Learning Objective

After completing this chapter, you will be able to identify Minority-Owned Constituent Entities (MOCEs), apply the separate ETR calculation requirement, compute Top-up Tax for MOCEs and Minority-Owned Sub-Groups, and allocate Top-up Tax liability between the main MNE Group and minority interests.

---

## Key References

**OECD GloBE Model Rules:**
- Article 5.6.1 — Treatment of Minority-Owned Sub-Groups
- Article 5.6.2 — Treatment of stand-alone MOCEs
- Article 10.1 — Definition of Minority-Owned Constituent Entity
- Article 10.1 — Definition of Minority-Owned Parent Entity (MOPE)
- Article 10.1 — Definition of Minority-Owned Sub-Group

**OECD Commentary:**
- Chapter 5, paragraphs 163-182 — Minority-Owned Entity rules
- Chapter 10 — Definitions (MOCE, MOPE, Minority-Owned Sub-Group)

**Administrative Guidance:**
- February 2023: MOCE indirect ownership calculation clarifications

---

## Why Separate Treatment for MOCEs?

The standard jurisdictional blending rule combines all Constituent Entities in a jurisdiction for ETR calculation. This creates a problem for minority-owned entities:

```
┌─────────────────────────────────────────────────────────────────────┐
│ THE PROBLEM WITHOUT SEPARATE TREATMENT                              │
│                                                                     │
│ If UPE owns only 25% of Entity X:                                  │
│ → 75% of Entity X's income belongs to OTHER shareholders           │
│ → But jurisdictional blending includes 100% of Entity X            │
│ → This could trigger Top-up Tax that minority shareholders         │
│   shouldn't bear                                                    │
│                                                                     │
│ OR                                                                  │
│                                                                     │
│ → Entity X's high ETR could shield OTHER entities from Top-up Tax  │
│ → The UPE benefits from taxes paid by minority shareholders        │
└─────────────────────────────────────────────────────────────────────┘
```

**Solution:** MOCEs are **excluded** from standard jurisdictional blending and have their own separate ETR calculation.

---

## Definition: Minority-Owned Constituent Entity *(Article 10.1)*

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

### Calculating Indirect Ownership

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

### Control Without Majority Ownership

MOCEs arise when accounting standards require consolidation despite ≤30% ownership. Common scenarios:

| Scenario | Ownership | Why Consolidated? |
|----------|-----------|-------------------|
| Voting control | 25% equity | UPE controls board through voting agreements |
| Variable interest entity | 20% equity | UPE is primary beneficiary under IFRS 10/ASC 810 |
| De facto control | 28% equity | Remaining ownership widely dispersed |
| Contractual arrangements | 15% equity | Management contracts give effective control |

---

## Related Definitions

### Minority-Owned Parent Entity (MOPE)

A **Minority-Owned Parent Entity** is a MOCE that:
- Holds **ownership interests** in other MOCEs, **AND**
- Is **not** owned (directly or indirectly) by another MOCE

### Minority-Owned Sub-Group

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

---

## Separate ETR Calculation *(Article 5.6)*

### Two Categories of MOCEs

| Category | Treatment | Article |
|----------|-----------|---------|
| **MOCE in a Minority-Owned Sub-Group** | Sub-Group treated as separate MNE Group | 5.6.1 |
| **Stand-alone MOCE** (not in a Sub-Group) | Entity-level separate ETR | 5.6.2 |

### Article 5.6.1: Minority-Owned Sub-Groups

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
│ → Top-up Tax calculation                                           │
│                                                                     │
│ The Sub-Group's income and taxes are EXCLUDED from the             │
│ main MNE Group's jurisdictional calculations.                      │
└─────────────────────────────────────────────────────────────────────┘
```

### Article 5.6.2: Stand-Alone MOCEs

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

---

## Multiple ETR Calculations Per Jurisdiction

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

---

## Worked Example: MOCE ETR Computation

### Scenario

**Stratos Group** has a 28% ownership interest in **Atlas Ireland Ltd**, a consolidated entity providing shared services. Atlas Ireland Ltd is a stand-alone MOCE (no subsidiaries).

### Step 1: Identify MOCE Status

| Test | Assessment |
|------|------------|
| UPE ownership interest | 28% (direct) |
| Is ≤ 30%? | Yes |
| Is entity consolidated? | Yes (control through management contract) |
| Part of Minority-Owned Sub-Group? | No (no MOCE subsidiaries) |
| **Classification** | **Stand-alone MOCE** |

### Step 2: Calculate Separate ETR

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

### Step 3: Apply SBIE (Separately)

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

### Step 4: Calculate Top-Up Tax

```
Top-up Tax % = 15% − 12% = 3%

Top-up Tax = 3% × €2,220,000 = €66,600
```

### Step 5: Apply QDMTT Offset (If Applicable)

Ireland has QDMTT. Assume Ireland collects the full Top-up Tax domestically:

```
QDMTT Paid:         €66,600
Net Top-up Tax:     €0
```

**Result:** Ireland retains the €66,600 through its QDMTT.

### Comparison: Main Group vs MOCE

| Calculation | Main Group Ireland | Stand-alone MOCE |
|-------------|-------------------|------------------|
| Entities included | Ireland OpCo 1, OpCo 2 | Atlas Ireland Ltd only |
| GloBE Income | €15,000,000 | €2,400,000 |
| ETR | 11.80% | 12.00% |
| Top-up Tax % | 3.20% | 3.00% |
| Jurisdictional Top-up Tax | €426,394 | €66,600 |
| QDMTT offset | (€426,394) | (€66,600) |
| Net Top-up Tax | €0 | €0 |

**Key insight:** Without MOCE separation, Atlas Ireland's 12% ETR would have been blended with the main group's 11.80%, potentially affecting both calculations unfairly.

---

## Minority-Owned Sub-Group Example

### Scenario

**Stratos Group** owns 22% of **Nexus Holdings BV** (Netherlands), which owns 100% of **Nexus Germany GmbH**. Nexus Holdings BV is consolidated due to Stratos's board control.

### Structure

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

### Calculation: Sub-Group as Separate MNE

**Step 1: Netherlands ETR (MOPE)**

| Item | Amount |
|------|--------|
| GloBE Income (MOPE) | €1,800,000 |
| Adjusted Covered Taxes | €450,000 |
| ETR | 25.00% |

**Result:** ETR ≥ 15% → No Top-up Tax for Netherlands within Sub-Group.

**Step 2: Germany ETR (Sub-Group Member)**

| Item | Amount |
|------|--------|
| GloBE Income (Nexus Germany) | €3,500,000 |
| Adjusted Covered Taxes | €980,000 |
| ETR | 28.00% |

**Result:** ETR ≥ 15% → No Top-up Tax for Germany within Sub-Group.

### Main Group Germany (Separate Calculation)

Stratos's main group also has entities in Germany (SG Germany GmbH):

| Calculation | Main Group Germany | Sub-Group Germany |
|-------------|-------------------|-------------------|
| Entities | SG Germany GmbH | Nexus Germany GmbH |
| GloBE Income | €50,000,000 | €3,500,000 |
| ETR | 23.00% | 28.00% |
| Top-up Tax | €0 | €0 |

**Important:** Nexus Germany GmbH is **excluded** from Main Group Germany's blending.

---

## Top-Up Tax Allocation for MOCEs

### Who Pays the Top-Up Tax?

| Entity Type | Who Bears Top-Up Tax? | Mechanism |
|-------------|----------------------|-----------|
| **Stand-alone MOCE** | UPE of main MNE Group | IIR |
| **MOPE (Sub-Group parent)** | UPE of main MNE Group | IIR |
| **Minority-Owned Subsidiary** | MOPE (Sub-Group parent) | IIR within Sub-Group |

### Allocation Logic

```
                      UPE (Stratos Holdings plc)
                            │
         ┌──────────────────┼──────────────────┐
         │                  │                  │
         ▼                  ▼                  ▼
    Main Group         Stand-alone          MOPE
    Subsidiaries         MOCE             (Sub-Group)
                                              │
    Top-up Tax:       Top-up Tax:            │
    UPE pays          UPE pays               ▼
    via IIR           via IIR           Sub-Group
                                         Subsidiaries
                                              │
                                         Top-up Tax:
                                         MOPE pays (as POPE)
                                         via IIR within Sub-Group
```

### Attribution Based on Ownership

Even though the UPE bears Top-up Tax for a MOCE, the **amount** reflects only the UPE's ownership share in the GloBE Income:

```
UPE's Top-up Tax Attribution = Top-up Tax × UPE's Ownership %

Example: Atlas Ireland Ltd
- Total MOCE Top-up Tax: €66,600
- UPE ownership: 28%
- UPE's attributed Top-up Tax: €66,600 × 28% = €18,648

Note: The full €66,600 is still computed and potentially collected
      via QDMTT, but the UPE's economic exposure is 28%.
```

---

## MOCE Interaction with Other Rules

### De Minimis Exclusion

MOCEs **are included** in the De Minimis calculation:

| Rule | Treatment of MOCE |
|------|-------------------|
| **De Minimis thresholds** | MOCE revenue and income **included** in jurisdiction totals |
| **ETR calculation** | MOCE **excluded** from standard blending |

**Practical effect:** A jurisdiction might qualify for De Minimis including MOCE amounts, but MOCEs would still have separate calculations if De Minimis doesn't apply.

### QDMTT

For a QDMTT to be **Qualified**, it must:
- Apply separate calculations for MOCEs
- Not blend MOCE income with main group

If a jurisdiction's domestic minimum tax doesn't follow MOCE separation, it **does not qualify** as a QDMTT.

### Investment Entities

If a MOCE is an **Investment Entity**:
- MOCE rules do **not** apply
- Investment Entity rules (Articles 7.4/7.5) take **priority**

| Entity Type | Applicable Rules |
|-------------|------------------|
| MOCE (not Investment Entity) | Article 5.6 |
| MOCE that is Investment Entity | Articles 7.4/7.5 (priority) |

---

## Decision Flowchart: MOCE Identification and Treatment

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

---

## Common Pitfalls

### Pitfall 1: Including MOCEs in Standard Blending

**Error:** Including MOCE's Covered Taxes and GloBE Income in the main group's jurisdictional ETR.

**Correct approach:** Always exclude MOCEs from standard blending; calculate separately.

### Pitfall 2: Forgetting Indirect Ownership

**Error:** Only considering direct ownership when applying the 30% test.

**Correct approach:** Calculate ownership through all tiers:
```
Indirect ownership = Product of ownership at each tier
Example: 60% × 40% = 24% indirect ownership
```

### Pitfall 3: Treating Investment Entity MOCEs Under Article 5.6

**Error:** Applying MOCE separate calculation to an entity that is both a MOCE and an Investment Entity.

**Correct approach:** Investment Entity rules (Articles 7.4/7.5) take priority over MOCE rules.

### Pitfall 4: Excluding MOCEs from De Minimis Calculation

**Error:** Not including MOCE revenue and income when calculating De Minimis thresholds.

**Correct approach:** Include MOCEs in De Minimis calculation (different from ETR blending treatment).

### Pitfall 5: Allocating Wrong Top-Up Tax Amount

**Error:** Allocating 100% of MOCE Top-up Tax to the UPE without considering ownership percentage.

**Correct approach:** While the UPE bears the tax obligation, attribution for economic purposes is based on ownership share.

---

## MOCE Assessment Checklist

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

   If ETR ≥ 15%: No Top-up Tax. STOP.

□ SBIE Calculation (separate):
   □ Eligible Payroll:              €__________________
   □ Payroll Carve-out (@9.8%):     €__________________
   □ Tangible Assets (NBV):         €__________________
   □ Asset Carve-out (@7.8%):       €__________________
   □ Total SBIE:                    €__________________

□ Excess Profit (Income − SBIE):    €__________________
□ Top-up Tax % (15% − ETR):         __________________%
□ MOCE Top-up Tax:                  €__________________

□ QDMTT Offset (if applicable):    (€__________________)
□ Net Top-up Tax:                   €__________________

PART C: SUB-GROUP CALCULATION (If MOPE)

□ List all entities in Minority-Owned Sub-Group:
   1. MOPE: _________________________
   2. Subsidiary: _________________________
   3. Subsidiary: _________________________

□ Apply full GloBE calculations as if Sub-Group were separate MNE:
   □ Jurisdictional blending within Sub-Group
   □ Separate SBIE for Sub-Group
   □ Separate Top-up Tax for Sub-Group

PART D: TOP-UP TAX ATTRIBUTION

□ Total MOCE/Sub-Group Top-up Tax:  €__________________
□ UPE Ownership %:                  __________________%
□ UPE Attributed Share:             €__________________
□ Mechanism: IIR / QDMTT offset
```

---

## Summary

Minority-Owned Constituent Entities require special treatment to prevent unfair blending of minority shareholders' income and taxes:

| Aspect | Key Point |
|--------|-----------|
| **Definition** | UPE owns ≤ 30% (direct + indirect) but entity is consolidated |
| **Stand-alone MOCE** | Entity-level separate ETR (Article 5.6.2) |
| **Minority-Owned Sub-Group** | Sub-Group treated as separate MNE (Article 5.6.1) |
| **Multiple ETRs** | Same jurisdiction may have multiple ETR calculations |
| **Top-up Tax** | UPE bears obligation; MOPE bears for its subsidiaries |
| **De Minimis** | MOCEs included in threshold calculation |
| **Investment Entities** | Investment Entity rules take priority |
| **QDMTT** | Must follow MOCE separation to qualify |

For Stratos, any MOCE (such as Atlas Ireland Ltd at 28% ownership) must be calculated separately, preventing inappropriate blending with main group entities.

---

## Integration with GIR Tools

MOCE calculations require **separate runs** through the GIR-001 GloBE Calculator:

| Calculation | GIR-001 Run | Data Input |
|-------------|-------------|------------|
| Main Group (per jurisdiction) | Run 1 | Exclude all MOCEs |
| Minority-Owned Sub-Group | Run 2 | Sub-Group entities only |
| Stand-alone MOCE | Run 3 | Single entity data |

**Workflow:**

```
Step 1: Identify all MOCEs in the MNE Group
        │
        ▼
Step 2: For each jurisdiction:
        ├── Run GIR-001 for Main Group (excluding MOCEs)
        ├── Run GIR-001 for each Minority-Owned Sub-Group
        └── Run GIR-001 for each Stand-alone MOCE
        │
        ▼
Step 3: Aggregate Top-up Tax results
        ├── Main Group Top-up Tax
        ├── Sub-Group Top-up Tax
        └── Stand-alone MOCE Top-up Tax
        │
        ▼
Step 4: Apply QDMTT offsets (separately for each calculation)
        │
        ▼
Step 5: Report on GIR with separate disclosures for MOCEs
```

**GIR Filing Note:** The GloBE Information Return requires separate disclosure of MOCE calculations. Ensure data is segregated appropriately.

---

## Next Step

You have completed Part 5: ETR Calculation and Top-Up Tax Determination. Proceed to **Case Study 5: Stratos's Complete ETR and Top-Up Tax Calculation** to apply all concepts from Chapters 5.1-5.6 in an integrated, hands-on exercise.
