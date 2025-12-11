# Chapter 6.2: Acquisitions and Disposals

## Learning Objective

After completing this chapter, you will be able to apply GloBE rules to entity-level acquisitions and disposals, determine when share deals are treated as asset deals, apply the basis step-up election, calculate partial-year adjustments for SBIE, and handle deferred tax attribute transfers correctly.

---

## Key References

**OECD GloBE Model Rules:**
- Article 6.2.1 — General rules for entities joining/leaving an MNE Group
- Article 6.2.1(a) — GloBE Income follows consolidated accounts
- Article 6.2.1(c) — Historical carrying value of assets
- Article 6.2.1(d)-(e) — SBIE adjustments for partial year
- Article 6.2.1(f) — Deferred tax attribute treatment
- Article 6.2.2 — Share deals treated as asset deals
- Article 6.3.4 — Basis step-up election

**OECD Commentary:**
- Chapter 6, paragraphs 46-98 — Acquisitions and disposals

**Administrative Guidance:**
- February 2023: DTL five-year clock reset
- June 2024: Articles 6.2-6.3 only apply from Transition Year

---

## The Steady-State Assumption

The GloBE Rules are generally drafted assuming the MNE Group has the **same Constituent Entities throughout the entire Fiscal Year**. Special rules address what happens when entities **join** or **leave** during the year.

```
┌─────────────────────────────────────────────────────────────────────┐
│ THE KEY PRINCIPLE: Follow the Consolidated Financial Statements     │
│                                                                     │
│ An entity is treated as part of the MNE Group for GloBE purposes   │
│ if ANY portion of its assets, liabilities, income, expenses, or    │
│ cash flows are consolidated on a line-by-line basis in the UPE's   │
│ Consolidated Financial Statements.                                  │
│                                                                     │
│ → Only include amounts actually consolidated                        │
│ → Partial year = partial inclusion                                  │
└─────────────────────────────────────────────────────────────────────┘
```

---

## General Rules: Entity Joining an MNE Group *(Article 6.2.1)*

When an entity becomes a Constituent Entity through an acquisition:

### Article 6.2.1(a): GloBE Income Follows Accounts

The target's GloBE Income or Loss is **limited to the amount consolidated** in the UPE's financial statements.

| Scenario | Treatment |
|----------|-----------|
| Acquisition on 1 July | Include 6 months of target's results |
| Acquisition on 1 October | Include 3 months of target's results |
| Acquisition on 31 December | Include minimal/nil (depends on cut-off) |

### Article 6.2.1(c): Historical Carrying Values

The acquiring MNE Group must determine the target's GloBE Income using the **historical carrying values** of its assets and liabilities—not fair value step-ups from purchase accounting.

```
Purchase Accounting vs GloBE Treatment:

ACCOUNTING:
→ Assets revalued to fair value
→ Goodwill recognized
→ New depreciation/amortisation base

GloBE:
→ Assets remain at HISTORICAL carrying value
→ Goodwill excluded from GloBE calculations
→ Depreciation continues on pre-acquisition basis
```

**Why this matters:** Purchase accounting creates higher depreciation that reduces accounting profit. GloBE uses historical values, so GloBE Income may be **higher** than accounting income for acquired entities.

### Article 6.2.1(d)-(e): SBIE Adjustments

For the Substance-Based Income Exclusion:

| Component | Treatment | Proration Method |
|-----------|-----------|------------------|
| **Payroll** | Prorated | Include only costs in consolidated period |
| **Tangible Assets** | **Special rule** | Value at joining/leaving date, then prorate |

**Tangible Asset Calculation:**

```
SBIE Asset Amount = (Asset Value at Transaction Date) × (Months in Group / 12)
```

**Example:**

Entity joins on 1 September (4 months in group):
- Tangible assets at joining date: €10,000,000
- SBIE asset amount: €10,000,000 × (4/12) = €3,333,333
- Asset carve-out (7.8% for 2025): €3,333,333 × 7.8% = €260,000

---

## Deferred Tax Attribute Transfer *(Article 6.2.1(f))*

### General Rule: Attributes Carry Over

Deferred tax assets and liabilities of the target are treated as if the acquiring MNE Group had **controlled the target when they arose**.

```
┌─────────────────────────────────────────────────────────────────────┐
│ DEFERRED TAX ATTRIBUTE TRANSFER                                     │
│                                                                     │
│ ✓ Accounting DTAs → Carry over to acquiring group                  │
│ ✓ Accounting DTLs → Carry over to acquiring group                  │
│ ✓ Tax loss carryforwards → Subject to local law limitations        │
│ ✗ GloBE Loss Election DTA → Does NOT transfer (jurisdictional)     │
│                                                                     │
│ DTLs subject to 5-year recapture:                                   │
│ → Clock RESETS on acquisition                                       │
│ → New 5-year period starts in acquiring group                       │
└─────────────────────────────────────────────────────────────────────┘
```

### DTL Five-Year Clock Reset

When a target with existing DTLs joins an MNE Group:

1. The DTLs are treated as **arising** in the acquiring MNE Group
2. A **new 5-year period** begins for recapture purposes
3. The acquiring group does not inherit the selling group's clock

**Example:**

| Timeline | Selling Group | Acquiring Group |
|----------|---------------|-----------------|
| Year 1 | DTL arises: €500,000 | — |
| Year 2 | DTL outstanding | — |
| Year 3 | **Acquisition occurs** | DTL transferred; new Year 1 |
| Year 4 | — | DTL Year 2 in acquirer |
| Year 5 | — | DTL Year 3 in acquirer |
| Year 6 | — | DTL Year 4 in acquirer |
| Year 7 | — | DTL Year 5 in acquirer |
| Year 8 | — | **Recapture if not reversed** |

The acquiring group has a full 5 years from acquisition to reverse the DTL.

---

## Share Deals vs Asset Deals

### Standard Treatment: Share Deal

In a typical share acquisition:

```
SHARE DEAL

Buyer purchases shares of Target from Seller

                    Seller Jurisdiction
                    ┌─────────────────┐
                    │     SELLER      │
                    │   Recognizes    │
                    │   gain on       │◄─── Gain taxed HERE
                    │   share sale    │
                    └────────┬────────┘
                             │ Shares
                             ▼
                    ┌─────────────────┐
                    │     TARGET      │
                    │   No gain       │
                    │   recognized    │◄─── No tax event
                    │   (assets      │
                    │   unchanged)    │
                    └─────────────────┘
                    Target Jurisdiction
```

- Gain is in **seller's jurisdiction** (where shares are held)
- Target's asset basis **unchanged**
- Target continues with historical carrying values

### Article 6.2.2: Share Deal Treated as Asset Deal

Some jurisdictions treat certain share acquisitions as **deemed asset disposals** for tax purposes. Article 6.2.2 aligns GloBE treatment with this local tax treatment.

```
SHARE DEAL TREATED AS ASSET DEAL (Article 6.2.2)

Where local tax law treats share deal as asset deal:

                    Seller Jurisdiction
                    ┌─────────────────┐
                    │     SELLER      │
                    │   No gain       │
                    │   (shares)      │
                    └────────┬────────┘
                             │ Shares
                             ▼
                    ┌─────────────────┐
                    │     TARGET      │
                    │   DEEMED gain   │
                    │   on assets     │◄─── Gain taxed HERE
                    │   for tax       │      (local law)
                    │   purposes      │
                    └─────────────────┘
                    Target Jurisdiction
```

**When Article 6.2.2 applies:**

| Condition | Required |
|-----------|----------|
| Controlling interest acquired/disposed | Yes |
| Local tax law treats as asset deal | Yes |
| Covered Tax levied on deemed disposal | Yes |

**Impact on GloBE:**
- Target recognizes gain/loss in its GloBE Income
- Covered Taxes include the tax on deemed disposal
- Acquiring group uses fair value basis for future GloBE calculations

---

## Basis Step-Up Election *(Article 6.3.4)*

### When the Election Applies

If local tax law **requires or permits** an entity to adjust the basis of its assets to fair value, the MNE Group can elect for GloBE treatment to follow this domestic tax treatment.

**Common triggers:**
- Tax residence migration
- Exit from tax consolidation
- Deemed disposal rules
- Voluntary re-basing elections

### Election Mechanics

```
┌─────────────────────────────────────────────────────────────────────┐
│ BASIS STEP-UP ELECTION (Article 6.3.4)                              │
│                                                                     │
│ Step 1: Calculate net gain/loss on deemed disposal                  │
│         (Fair Value − Tax Basis for all assets/liabilities)        │
│                                                                     │
│ Step 2: Choose recognition timing:                                  │
│                                                                     │
│         OPTION A: Recognize 100% in triggering year                 │
│                                                                     │
│         OPTION B: Spread over 5 years (20% per year)               │
│                   Year 1: 20%                                       │
│                   Year 2: 20%                                       │
│                   Year 3: 20%                                       │
│                   Year 4: 20%                                       │
│                   Year 5: 20%                                       │
│                                                                     │
│ Step 3: Adjust carrying values for future GloBE calculations       │
└─────────────────────────────────────────────────────────────────────┘
```

### Example: Basis Step-Up Election

**Scenario:** TechStart Ireland has assets with:
- Tax basis: €20,000,000
- Fair market value: €35,000,000
- Net step-up: €15,000,000 (gain)

Upon acquisition by Stratos, Irish tax law permits a basis step-up with immediate tax charge.

**Option A: Immediate Recognition**

| Year | GloBE Income Impact |
|------|---------------------|
| Year 1 (acquisition year) | +€15,000,000 |
| Years 2-5 | €0 |

**Option B: 5-Year Spread**

| Year | GloBE Income Impact |
|------|---------------------|
| Year 1 | +€3,000,000 |
| Year 2 | +€3,000,000 |
| Year 3 | +€3,000,000 |
| Year 4 | +€3,000,000 |
| Year 5 | +€3,000,000 |

### Early Exit Acceleration

If the entity leaves the MNE Group before the 5-year period ends, the **remaining amount is accelerated** into the leaving year.

**Example:** Entity leaves in Year 3:
- Year 1: €3,000,000 recognized
- Year 2: €3,000,000 recognized
- Year 3: €9,000,000 recognized (remaining €9M accelerated)

---

## Comparison: Asset Deal vs Share Deal vs Step-Up Election

| Aspect | Asset Deal | Share Deal (Standard) | Share Deal (Art. 6.2.2) | Step-Up Election |
|--------|------------|----------------------|-------------------------|------------------|
| **Gain location** | Target jurisdiction | Seller jurisdiction | Target jurisdiction | Target jurisdiction |
| **Target basis** | Fair value | Historical | Fair value | Fair value |
| **GloBE Income** | Target includes gain | No gain in target | Target includes gain | Target includes gain (can spread) |
| **Future depreciation** | On fair value | On historical value | On fair value | On fair value |
| **Covered Taxes** | Tax on asset sale | No tax in target | Tax on deemed disposal | Tax on step-up |

---

## Disposal by an MNE Group

When a Constituent Entity **leaves** an MNE Group:

### Income Recognition

Include in GloBE Income only the target's results **up to the disposal date**:

| Item | Treatment |
|------|-----------|
| GloBE Income | Include to disposal date |
| Covered Taxes | Include to disposal date |
| Gain on disposal | Recognized in seller's jurisdiction |

### SBIE for Leaving Entities

| Component | Treatment |
|-----------|-----------|
| Payroll | Include costs to disposal date |
| Tangible Assets | Value at disposal date × (months in group / 12) |

### Deferred Tax Treatment

DTLs that were previously taken into account in the disposing MNE Group are:
- Treated as **reversed** in the disposing group
- Treated as **arising** in the acquiring group

This prevents double-counting or gaps in the 5-year tracking.

---

## Decision Flowchart: Acquisition/Disposal Treatment

```
START: Acquisition or disposal of entity
        │
        ▼
┌───────────────────────────────────────────────────┐
│ Is this a share deal or asset deal?               │
└───────────────────────────────────────────────────┘
        │
   ┌────┴────────────────┐
 SHARE              ASSET
 DEAL               DEAL
   │                   │
   ▼                   ▼
┌──────────────────┐  ┌──────────────────────────────┐
│ Does local tax   │  │ Follow standard asset        │
│ law treat share  │  │ treatment:                   │
│ deal as asset    │  │ → Gain in target jurisdiction│
│ deal?            │  │ → Target takes FMV basis     │
└──────────────────┘  └──────────────────────────────┘
        │
   ┌────┴────┐
   NO       YES
   │         │
   ▼         ▼
┌────────────────┐  ┌────────────────────────────────┐
│ Standard share │  │ Apply Article 6.2.2:           │
│ deal:          │  │ → Gain in target jurisdiction  │
│ → Gain in      │  │ → Target takes FMV basis       │
│   seller's     │  │ → Include deemed disposal      │
│   jurisdiction │  │   gain in target's GloBE      │
│ → Target keeps │  │   Income                       │
│   historical   │  └────────────────────────────────┘
│   basis        │
└────────────────┘
        │
        ▼
┌───────────────────────────────────────────────────┐
│ Does local tax law permit/require basis step-up?  │
└───────────────────────────────────────────────────┘
        │
   ┌────┴────┐
   NO       YES
   │         │
   ▼         ▼
┌────────┐  ┌────────────────────────────────────────┐
│No      │  │ Consider Article 6.3.4 election:       │
│election│  │ → Recognize gain/loss in GloBE Income  │
│needed  │  │ → Choose immediate or 5-year spread    │
└────────┘  │ → Adjust carrying values going forward │
            └────────────────────────────────────────┘
```

---

## Stratos Worked Example: TechStart Acquisition

### Background

Stratos Holdings plc acquires 100% of TechStart Ireland Ltd on 1 July 2025.

**TechStart Data:**

| Item | Pre-Acquisition Value |
|------|----------------------|
| Tax basis of assets | €8,000,000 |
| Fair market value of assets | €12,000,000 |
| Full-year GloBE Income | €8,500,000 |
| Full-year Covered Taxes | €1,062,500 |
| Eligible payroll (full year) | €2,400,000 |
| Tangible assets (at 1 July) | €5,000,000 |
| DTL on accelerated depreciation | €300,000 |

### Step 1: Determine Deal Structure

Irish tax law treats the acquisition as a **share deal**. The shares are sold by TechStart's former parent (a US company).

**Result:** Standard share deal treatment under Article 6.2.1.
- Gain recognized in seller's jurisdiction (US)
- TechStart retains historical carrying values

### Step 2: Calculate Partial-Year GloBE Amounts

| Item | Full Year | Consolidated (6 months) |
|------|-----------|-------------------------|
| GloBE Income | €8,500,000 | €4,250,000 |
| Covered Taxes | €1,062,500 | €531,250 |
| Payroll | €2,400,000 | €1,200,000 |

### Step 3: Calculate SBIE for Partial Year

**Tangible Assets:**
```
Asset value at joining date: €5,000,000
Months in group: 6 out of 12
Prorated amount: €5,000,000 × (6/12) = €2,500,000
Asset carve-out (7.8%): €2,500,000 × 7.8% = €195,000
```

**Payroll:**
```
Payroll in consolidated period: €1,200,000
Payroll carve-out (9.8%): €1,200,000 × 9.8% = €117,600
```

**Total SBIE for TechStart (partial year):** €195,000 + €117,600 = **€312,600**

### Step 4: Handle Deferred Tax Attributes

TechStart has a DTL of €300,000 from accelerated depreciation.

| Treatment | Action |
|-----------|--------|
| DTL transfers to Stratos Group | Yes |
| 5-year clock resets | Yes — new Year 1 starts 1 July 2025 |
| Subject to 15% cap | Yes — recast at MIN(12.5%, 15%) = 12.5% |

The DTL will be tracked for 5 years from 1 July 2025. If not reversed by 30 June 2030, recapture will be triggered.

### Step 5: Consider Basis Step-Up Election

**Question:** Should Stratos make a basis step-up election for TechStart?

**Analysis:**

| Factor | Consideration |
|--------|---------------|
| Step-up amount | €12M − €8M = €4M gain |
| Irish tax on step-up | €4M × 12.5% = €500,000 |
| Impact on GloBE Income | +€4M (or +€800K per year if spread) |
| Ireland ETR before | 11.80% |
| Ireland ETR with step-up (Year 1) | Higher (increased income + tax) |

**Decision framework:**
- If Ireland's ETR is below 15%, adding €4M income and €500K tax may **increase** ETR
- Future depreciation on stepped-up basis reduces future GloBE Income
- Election is **irrevocable**—analyse carefully

**Calculation if election made:**

Without step-up election:
```
Ireland GloBE Income: €15,000,000 + €4,250,000 = €19,250,000
Ireland Covered Taxes: €1,770,000 + €531,250 = €2,301,250
Ireland ETR: 11.95%
```

With step-up election (immediate):
```
Ireland GloBE Income: €19,250,000 + €4,000,000 = €23,250,000
Ireland Covered Taxes: €2,301,250 + €500,000 = €2,801,250
Ireland ETR: €2,801,250 ÷ €23,250,000 = 12.05%
```

**Result:** Step-up election marginally improves ETR (12.05% vs 11.95%). However, the Top-Up Tax base increases. Analysis of multi-year impact needed before deciding.

---

## Common Pitfalls

### Pitfall 1: Using Fair Value for Acquired Entity

**Error:** Using purchase accounting fair values for the target's GloBE Income calculation.

**Correct approach:** Use the target's **historical carrying values** per Article 6.2.1(c). Only use fair value if Article 6.2.2 applies or a step-up election is made.

### Pitfall 2: Not Prorating Tangible Assets

**Error:** Including full-year tangible asset value in SBIE for a mid-year acquisition.

**Correct approach:** Take asset value at joining date, then prorate: Asset × (months in group / 12).

### Pitfall 3: Forgetting DTL Clock Reset

**Error:** Continuing the selling group's 5-year DTL tracking in the acquiring group.

**Correct approach:** Reset the clock. A new 5-year period begins when the DTL transfers to the acquiring MNE Group.

### Pitfall 4: Assuming GloBE Loss Election Transfers

**Error:** Continuing the selling group's GloBE Loss Election for a jurisdiction.

**Correct approach:** GloBE Loss Election does NOT transfer. The acquiring group must make its own election decision.

### Pitfall 5: Ignoring Article 6.2.2 Applicability

**Error:** Applying standard share deal treatment when local law treats the transaction as an asset deal.

**Correct approach:** Check local tax treatment. If the jurisdiction taxes a deemed asset disposal, apply Article 6.2.2.

---

## Acquisition/Disposal Checklist

Use this checklist when an entity joins or leaves the MNE Group:

```
ACQUISITION/DISPOSAL CHECKLIST
Entity: _________________________
Transaction Type: ACQUISITION / DISPOSAL
Transaction Date: _________________________
Months in MNE Group this FY: _____ / 12

═══════════════════════════════════════════════════════════════════════
SECTION A: DEAL STRUCTURE
═══════════════════════════════════════════════════════════════════════

□ Deal type: SHARE DEAL / ASSET DEAL

□ If SHARE DEAL:
   □ Does local tax law treat as asset deal?          YES / NO
   □ If YES: Apply Article 6.2.2
     □ Include deemed disposal gain in target's GloBE Income
     □ Target takes fair value basis going forward
   □ If NO: Apply standard Article 6.2.1
     □ Gain recognized in seller's jurisdiction
     □ Target keeps historical carrying values

═══════════════════════════════════════════════════════════════════════
SECTION B: PARTIAL YEAR CALCULATIONS
═══════════════════════════════════════════════════════════════════════

□ GloBE Income (consolidated period):           €__________________
□ Covered Taxes (consolidated period):          €__________________

□ SBIE Components:
   □ Payroll (consolidated period):             €__________________
   □ Payroll carve-out (×9.8%):                 €__________________

   □ Tangible assets at transaction date:       €__________________
   □ Prorated amount (× months/12):             €__________________
   □ Asset carve-out (×7.8%):                   €__________________

   □ Total SBIE:                                €__________________

═══════════════════════════════════════════════════════════════════════
SECTION C: DEFERRED TAX ATTRIBUTES
═══════════════════════════════════════════════════════════════════════

□ Does target have DTAs?                         YES / NO
   □ Amount: €__________________
   □ Nature: _________________________
   □ Transfer to acquiring group? YES (standard) / NO (GloBE Loss Election)

□ Does target have DTLs?                         YES / NO
   □ Amount: €__________________
   □ Nature: _________________________
   □ 5-year clock reset date: _________________________
   □ Recapture deadline: _________________________

□ Did target have GloBE Loss Election?           YES / NO
   □ If YES: Does NOT transfer
   □ Acquiring group election decision: MAKE NEW ELECTION / USE DTA APPROACH

═══════════════════════════════════════════════════════════════════════
SECTION D: BASIS STEP-UP ELECTION (Article 6.3.4)
═══════════════════════════════════════════════════════════════════════

□ Does local tax permit/require basis step-up?   YES / NO

   If NO: Skip to Section E

□ Step-up analysis:
   □ Tax basis of assets:                        €__________________
   □ Fair market value:                          €__________________
   □ Net step-up gain/(loss):                    €__________________
   □ Tax on step-up:                             €__________________

□ Election decision:
   □ Make step-up election?                      YES / NO
   □ If YES, recognition timing:
     □ Option A: 100% in Year 1                  €__________________
     □ Option B: 20% per year × 5 years          €__________ per year

□ Impact analysis:
   □ ETR without election: ___________%
   □ ETR with election (Year 1): ___________%
   □ Multi-year NPV impact considered?           YES / NO

═══════════════════════════════════════════════════════════════════════
SECTION E: SUMMARY
═══════════════════════════════════════════════════════════════════════

□ Article applied: 6.2.1 / 6.2.2 / 6.3.4
□ GloBE Income impact (this FY):                 €__________________
□ Covered Taxes impact (this FY):                €__________________
□ SBIE impact (this FY):                         €__________________
□ DTL tracking required?                         YES / NO
□ Elections made: _________________________
□ Documentation complete?                        YES / NO
```

---

## Summary

Acquisitions and disposals require careful analysis of deal structure and applicable GloBE rules:

| Scenario | Key Article | Treatment |
|----------|-------------|-----------|
| **Standard share deal** | 6.2.1 | Historical values; gain in seller jurisdiction |
| **Share deal = asset deal** | 6.2.2 | Fair value; gain in target jurisdiction |
| **Asset deal** | 6.3.1 | Fair value; gain in target jurisdiction |
| **Basis step-up** | 6.3.4 | Election for immediate or 5-year spread |

**Key points to remember:**
- GloBE follows **historical carrying values** unless specific rules apply
- Payroll is prorated; tangible assets use transaction date value then prorate
- DTL 5-year clock **resets** on acquisition
- GloBE Loss Election does **not** transfer
- Step-up election is **irrevocable**—analyse carefully before electing

---

## Integration with GIR Tools

| Step | Tool | Action |
|------|------|--------|
| **Partial year data** | GIR-001 GloBE Calculator | Enter prorated GloBE Income and Covered Taxes |
| **SBIE adjustment** | GIR-001 Step 2 | Enter prorated payroll; prorated tangible assets |
| **DTL tracking** | Manual tracking | Set up new 5-year schedule from transaction date |
| **Step-up election** | Manual analysis | Model ETR impact before deciding |

**GIR Reporting:** The GloBE Information Return requires:
- Transaction date for entities joining/leaving
- Indication of Article 6.2.2 or 6.3.4 elections made
- Partial-year calculation methodology

---

## Next Step

You have learned how to handle entity-level acquisitions and disposals under GloBE. Proceed to **Chapter 6.3: Joint Ventures** for guidance on the special rules applying to JV investments where the UPE holds more than 50% ownership but less than full control.
