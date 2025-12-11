# Chapter 6.4: Multi-Parented Groups

## Learning Objective

After completing this chapter, you will be able to identify when two or more parent entities form a Multi-Parented MNE Group, distinguish between Stapled Structures and Dual-Listed Arrangements, determine how Top-Up Tax is allocated across multiple UPEs, and ensure correct GIR filing obligations for combined groups.

---

## Key References

**OECD GloBE Model Rules:**
- Article 6.5.1 — Multi-Parented MNE Group definition
- Article 6.5.2 — Combined treatment as single MNE Group
- Article 6.5.3 — Top-Up Tax allocation between UPEs
- Article 10.1 — Definition of Stapled Structure and Dual-Listed Arrangement

**OECD Commentary:**
- Chapter 6, paragraphs 126-150 — Multi-Parented MNE Group rules

**Administrative Guidance:**
- December 2023: Combined GIR filing for Multi-Parented Groups
- February 2024: Top-Up Tax allocation clarifications

---

## Why Special Rules for Multi-Parented Groups?

Multi-Parented MNE Groups present unique challenges because there is no single Ultimate Parent Entity:

```
┌─────────────────────────────────────────────────────────────────────┐
│ THE MULTI-PARENTED PROBLEM                                          │
│                                                                     │
│ Standard GloBE structure:                                           │
│ → ONE UPE at top of ownership chain                                │
│ → All Constituent Entities trace back to single parent             │
│ → Top-Up Tax charged to that UPE via IIR                           │
│                                                                     │
│ Multi-Parented reality:                                             │
│ → TWO OR MORE parent entities operate as unified group             │
│ → Entities share economic ownership but not legal ownership        │
│ → No single UPE to bear IIR liability                              │
│                                                                     │
│ THE SOLUTION (Article 6.5):                                         │
│ → Treat the combined structure as a SINGLE MNE Group               │
│ → Each parent entity becomes a "Joint UPE"                         │
│ → Allocate Top-Up Tax proportionally to each UPE                   │
│ → Coordinate GIR filing obligations                                 │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Definition: Multi-Parented MNE Group *(Article 6.5.1)*

A **Multi-Parented MNE Group** exists when two or more entities (that would otherwise be separate UPEs) enter into an arrangement that creates a combined group. There are two qualifying arrangements:

### 1. Stapled Structure *(Article 10.1)*

A **Stapled Structure** arises when:

| Criterion | Requirement |
|-----------|-------------|
| **Ownership stapling** | 50% or more of the ownership interests in each entity are **stapled together** |
| **Trading restriction** | Stapled interests cannot be transferred independently — must be traded as a unit |
| **Exchange listing** | Typically listed as a combined instrument on a securities exchange |

**What "stapling" means:**

```
STAPLED STRUCTURE VISUAL

Before Stapling:
┌──────────────┐     ┌──────────────┐
│   Alpha Co   │     │   Beta Co    │
│    Shares    │     │    Shares    │
│              │     │              │
│  (Trade      │     │  (Trade      │
│   separately)│     │   separately)│
└──────────────┘     └──────────────┘

After Stapling:
┌─────────────────────────────────────┐
│   STAPLED UNIT (Alpha + Beta)       │
│                                     │
│   1 share Alpha + 1 share Beta      │
│   = 1 Stapled Unit                  │
│                                     │
│   Traded together on exchange       │
│   Cannot be separated               │
└─────────────────────────────────────┘
```

**Common examples:**
- Property trusts paired with operating companies
- Infrastructure groups with trust and company components

### 2. Dual-Listed Arrangement (DLA) *(Article 10.1)*

A **Dual-Listed Arrangement** arises when:

| Criterion | Requirement |
|-----------|-------------|
| **Separate listings** | Each parent entity is **separately listed** on a securities exchange (often in different countries) |
| **Equalisation agreement** | Parents enter into an agreement to **equalise** economic interests (dividends, voting, liquidation) |
| **Combined management** | The entities operate as a **single economic enterprise** with shared management |
| **No ownership consolidation** | One parent does NOT own a controlling stake in the other |

**DLA Structure:**

```
DUAL-LISTED ARRANGEMENT VISUAL

┌────────────────────────────────────────────────────────────────┐
│                    EQUALISATION AGREEMENT                       │
│                                                                 │
│ ┌──────────────┐                        ┌──────────────┐       │
│ │   UK Co plc  │◄──────────────────────►│  AU Co Ltd   │       │
│ │              │    "Single economic    │              │       │
│ │  Listed on   │     enterprise"        │  Listed on   │       │
│ │  London SE   │                        │  Sydney ASX  │       │
│ └──────────────┘                        └──────────────┘       │
│        │                                       │                │
│        │ owns                                  │ owns           │
│        ▼                                       ▼                │
│  ┌───────────┐                          ┌───────────┐          │
│  │ UK Subs   │                          │ AU Subs   │          │
│  └───────────┘                          └───────────┘          │
│                                                                 │
│  COMBINED GROUP treated as SINGLE MNE Group for GloBE          │
└────────────────────────────────────────────────────────────────┘
```

**Key features of DLAs:**
- Shareholders in each parent effectively share equally in the combined group
- Dividend policies aligned across both parents
- Often structured to access capital markets in multiple jurisdictions
- Well-known historical examples: BHP Group (UK/Australia), Rio Tinto (UK/Australia), Unilever (UK/Netherlands)

---

## The 50% Ownership Threshold

For both structures, the **50% or more** threshold is critical:

```
STAPLED STRUCTURE TEST

If ≥50% of ownership interests are stapled:
→ Multi-Parented MNE Group exists
→ Combined treatment applies

If <50% of ownership interests are stapled:
→ No Multi-Parented MNE Group
→ Each parent treated as separate UPE of its own group
```

**Example: Partial Stapling**

| Scenario | Stapled % | Treatment |
|----------|-----------|-----------|
| Alpha and Beta 100% stapled | 100% | Multi-Parented MNE Group |
| Alpha and Beta 60% stapled; 40% trade freely | 60% | Multi-Parented MNE Group |
| Alpha and Beta 45% stapled; 55% trade freely | 45% | **No** Multi-Parented Group — separate UPEs |

---

## Combined Treatment as Single MNE Group *(Article 6.5.2)*

When entities form a Multi-Parented MNE Group:

```
┌─────────────────────────────────────────────────────────────────────┐
│ COMBINED TREATMENT (Article 6.5.2)                                  │
│                                                                     │
│ All Constituent Entities of ALL parent entities are treated as:    │
│                                                                     │
│ → Members of a SINGLE MNE Group                                    │
│ → Subject to jurisdictional blending across the combined group     │
│ → Assessed against single €750M revenue threshold                  │
│ → Each parent = "Joint UPE" with IIR obligations                   │
│                                                                     │
│ NO duplication:                                                     │
│ → Revenue counted ONCE (not doubled for each parent)               │
│ → GloBE Income calculated ONCE per jurisdiction                    │
│ → Top-Up Tax calculated ONCE, then ALLOCATED                       │
└─────────────────────────────────────────────────────────────────────┘
```

### Revenue Threshold Test

The €750M threshold is applied to the **combined group**:

**Example:**

| Parent | Standalone Revenue | Combined Group Revenue |
|--------|-------------------|----------------------|
| Alpha plc | €500,000,000 | — |
| Beta Ltd | €400,000,000 | — |
| **Combined** | — | **€900,000,000** |

- Combined revenue exceeds €750M
- **Both** Alpha and Beta are within GloBE scope
- Even if neither alone exceeds €750M, the combined test brings them in scope

---

## Top-Up Tax Allocation *(Article 6.5.3)*

### The Allocation Principle

When a Multi-Parented MNE Group has Top-Up Tax liability, it must be **allocated** between the Joint UPEs:

```
Top-Up Tax Allocation = Group Top-Up Tax × Allocable Share
```

### Determining Allocable Share

The **Allocable Share** for each UPE is based on its relative economic interest in the combined group:

| Method | Application |
|--------|-------------|
| **Ownership interest ratio** | Proportion of combined ownership interests held through each parent |
| **Agreement terms** | Equalisation agreement may specify allocation percentages |
| **Default: 50/50** | If no clear basis, equal allocation applies |

### Example: Stapled Structure Allocation

**Scenario:** Alpha plc and Beta plc are 100% stapled. Combined group has €400,000 Top-Up Tax.

```
Alpha shareholders: 60% of stapled units
Beta shareholders: 40% of stapled units

Allocation:
├── Alpha plc: €400,000 × 60% = €240,000
└── Beta plc:  €400,000 × 40% = €160,000

Each pays via IIR based on allocable share.
```

### Example: DLA Allocation

**Scenario:** UK Co plc and AU Co Ltd have a DLA with 50/50 equalisation. Combined Top-Up Tax is €600,000.

```
Equalisation agreement: 50/50

Allocation:
├── UK Co plc: €600,000 × 50% = €300,000
└── AU Co Ltd: €600,000 × 50% = €300,000

Each bears IIR based on equalisation terms.
```

---

## Jurisdictional Blending in Multi-Parented Groups

### All CEs Blend Together

Under combined treatment, Constituent Entities blend **across the entire Multi-Parented Group**:

```
JURISDICTIONAL BLENDING EXAMPLE

Alpha plc (UK)              Beta Ltd (Australia)
    │                              │
    ├── Alpha Germany Sub          ├── Beta Germany GmbH
    │   GloBE Income: €30M         │   GloBE Income: €20M
    │   Covered Taxes: €6.9M       │   Covered Taxes: €4.2M
    │                              │
    └── Alpha Ireland Ltd          └── Beta Singapore Pte
        GloBE Income: €15M             GloBE Income: €25M
        Covered Taxes: €1.8M           Covered Taxes: €2.5M

COMBINED GERMANY:
├── Total GloBE Income: €30M + €20M = €50M
├── Total Covered Taxes: €6.9M + €4.2M = €11.1M
└── Combined ETR: 22.20% ✓ (≥15%, no Top-Up Tax)

COMBINED IRELAND:
├── Total GloBE Income: €15M
├── Total Covered Taxes: €1.8M
└── Combined ETR: 12.00% (Top-Up Tax applies)

COMBINED SINGAPORE:
├── Total GloBE Income: €25M
├── Total Covered Taxes: €2.5M
└── Combined ETR: 10.00% (Top-Up Tax applies)
```

**Key point:** Germany entities blend together even though owned by different parents. The combined 22.20% ETR means no Top-Up Tax for Germany.

---

## GIR Filing Obligations

### Both UPEs Have Filing Obligations

Each Joint UPE has obligations under GloBE:

```
┌─────────────────────────────────────────────────────────────────────┐
│ GIR FILING FOR MULTI-PARENTED GROUPS                                │
│                                                                     │
│ Option 1: SEPARATE FILING                                           │
│ → Each UPE files its own GIR                                        │
│ → Both report the SAME combined group data                          │
│ → Must coordinate to ensure consistency                             │
│                                                                     │
│ Option 2: SINGLE DESIGNATED FILING ENTITY (DFE)                     │
│ → One UPE appointed as DFE                                          │
│ → DFE files GIR on behalf of both                                   │
│ → Other UPE notifies its tax authority of DFE arrangement           │
│                                                                     │
│ RECOMMENDED: Appoint single DFE to avoid duplication and errors.    │
└─────────────────────────────────────────────────────────────────────┘
```

### IIR Application

Both UPEs apply IIR to their allocable share:

| UPE | Jurisdiction | IIR Status | Obligation |
|-----|--------------|------------|------------|
| UK Co plc | UK | IIR implemented | Pays IIR on UK Co's allocable share |
| AU Co Ltd | Australia | IIR implemented | Pays IIR on AU Co's allocable share |

**If one UPE is in non-IIR jurisdiction:**
- That UPE does not pay IIR
- UTPR may apply in other jurisdictions to collect the allocable share
- The IIR-jurisdiction UPE pays only its share, not the other's

---

## Stratos Worked Example: Potential DLA Analysis

### Background

Stratos Holdings plc is exploring a potential Dual-Listed Arrangement with **NordicTech ASA** (Norway) to access Scandinavian capital markets. The combined entity would operate as a single enterprise.

### Proposed Structure

```
PROPOSED DLA STRUCTURE

┌────────────────────────────────────────────────────────────────┐
│                    EQUALISATION AGREEMENT                       │
│                       (60% / 40%)                               │
│                                                                 │
│ ┌───────────────────┐                ┌───────────────────┐     │
│ │ Stratos Holdings  │◄──────────────►│   NordicTech ASA  │     │
│ │      plc (UK)     │                │    (Norway)       │     │
│ │                   │                │                   │     │
│ │  Listed on LSE    │                │  Listed on Oslo   │     │
│ └───────────────────┘                └───────────────────┘     │
│        │                                    │                   │
│        │                                    │                   │
│        ▼                                    ▼                   │
│  ┌────────────┐                      ┌────────────┐            │
│  │  Stratos   │                      │ NordicTech │            │
│  │  Existing  │                      │   Subs     │            │
│  │  CEs       │                      │            │            │
│  └────────────┘                      └────────────┘            │
└────────────────────────────────────────────────────────────────┘
```

### Step 1: Confirm Multi-Parented MNE Group Status

| Criterion | Assessment |
|-----------|------------|
| Separate listings? | Yes — LSE and Oslo Børs |
| Equalisation agreement? | Yes — 60/40 split proposed |
| Combined management? | Yes — unified board proposed |
| Control by one parent? | No — neither controls the other |
| **Classification** | **Dual-Listed Arrangement for GloBE** |

### Step 2: Apply Combined Revenue Test

| Entity | Current Revenue |
|--------|-----------------|
| Stratos Group | €1,850,000,000 |
| NordicTech Group | €650,000,000 |
| **Combined** | **€2,500,000,000** |

**Result:** Combined revenue exceeds €750M threshold (both groups already exceed independently, so this merely confirms).

### Step 3: Identify Combined Group Jurisdictions

**Stratos existing jurisdictions:**
- UK (Stratos Holdings plc)
- Germany (Stratos GmbH)
- Singapore (Stratos Asia Pte Ltd)
- Ireland (Stratos Ireland Ltd)
- Luxembourg (Stratos Finance S.à r.l.)

**NordicTech jurisdictions:**
- Norway (NordicTech ASA)
- Sweden (NordicTech AB)
- Germany (NordicTech GmbH)

**Overlap:** Germany — entities from both groups must blend.

### Step 4: Calculate Combined ETR (Germany Example)

**Germany Blending:**

| Entity | GloBE Income | Covered Taxes |
|--------|--------------|---------------|
| Stratos GmbH | €50,000,000 | €11,500,000 |
| NordicTech GmbH | €18,000,000 | €3,960,000 |
| **Combined Germany** | **€68,000,000** | **€15,460,000** |

```
Combined Germany ETR = €15,460,000 ÷ €68,000,000 = 22.74%

ETR ≥ 15% → No Top-Up Tax for Germany
```

**NordicTech GmbH has 22% standalone ETR**, but blending with Stratos GmbH still results in no Top-Up Tax (both are adequately taxed).

### Step 5: Calculate Top-Up Tax for Low-Tax Jurisdictions

**Singapore (Stratos only):**

| Item | Amount |
|------|--------|
| GloBE Income | €32,000,000 |
| Covered Taxes | €3,136,000 |
| ETR | **9.80%** |
| Top-Up Tax % | 5.20% |
| SBIE | €1,892,000 |
| Excess Profit | €30,108,000 |
| Top-Up Tax | **€1,565,616** |

**Sweden (NordicTech only — assumed undertaxed):**

| Item | Amount |
|------|--------|
| GloBE Income | €12,000,000 |
| Covered Taxes | €1,320,000 |
| ETR | **11.00%** |
| Top-Up Tax % | 4.00% |
| SBIE | €800,000 |
| Excess Profit | €11,200,000 |
| Top-Up Tax | **€448,000** |

### Step 6: Allocate Top-Up Tax Between Joint UPEs

**Total Combined Group Top-Up Tax:**

| Jurisdiction | Top-Up Tax |
|--------------|------------|
| Singapore | €1,565,616 |
| Sweden | €448,000 |
| **Total** | **€2,013,616** |

**Allocation per Equalisation Agreement (60/40):**

| UPE | Allocation % | Allocated Top-Up Tax |
|-----|--------------|---------------------|
| Stratos Holdings plc | 60% | **€1,208,170** |
| NordicTech ASA | 40% | **€805,446** |
| **Total** | 100% | **€2,013,616** |

### Step 7: Determine Payment Mechanism

| UPE | Jurisdiction | IIR Status | Payment |
|-----|--------------|------------|---------|
| Stratos Holdings plc | UK | IIR implemented | Pays €1,208,170 via UK IIR |
| NordicTech ASA | Norway | IIR implemented | Pays €805,446 via Norway IIR |

**Result:** Both UPEs pay their allocable share via IIR in their respective jurisdictions.

### Summary: DLA Impact on Stratos

| Metric | Stratos Standalone | Combined DLA |
|--------|-------------------|--------------|
| **Total Top-Up Tax** | €198,907 (current) | €2,013,616 (combined) |
| **Stratos's Share** | €198,907 | €1,208,170 |
| **Increase** | — | +€1,009,263 |

**Observation:** The DLA brings NordicTech's Swedish undertaxation into Stratos's allocable share. Stratos would bear 60% of the combined group's Top-Up Tax, including tax on jurisdictions it doesn't directly operate in.

---

## Planning Considerations for Multi-Parented Groups

### Pre-Formation Analysis

Before entering a Stapled Structure or DLA:

```
PRE-FORMATION CHECKLIST

□ What is each parent's current GloBE position?
   - Low-tax jurisdictions that will blend
   - Existing QDMTT coverage
   - Current Top-Up Tax exposure

□ How will combined thresholds affect scope?
   - Revenue threshold (€750M) on combined basis
   - De Minimis Exclusion may be lost for some jurisdictions

□ What is the proposed allocation methodology?
   - Equalisation terms
   - Impact on IIR liability distribution
   - Tax cashflow implications

□ Which jurisdiction will be primary GIR filer?
   - Designate DFE early
   - Coordinate data collection processes
```

### Post-Formation Monitoring

```
ONGOING COMPLIANCE

□ Annual reconciliation of allocation percentages
   - Changes in equalisation terms
   - Shifts in shareholder composition

□ Coordinated GIR preparation
   - Single data collection process
   - Consistent methodology across both UPE tax teams

□ Monitor for structural changes
   - Unstapling events (trigger exit)
   - DLA termination provisions
```

---

## Termination of Multi-Parented Status

### When Does Multi-Parented Status End?

| Event | Effect |
|-------|--------|
| **Unstapling** | If stapled interests fall below 50%, Multi-Parented status ends |
| **DLA termination** | Cancellation of equalisation agreement ends combined treatment |
| **Merger** | If one parent acquires the other, standard single-UPE structure applies |

### Year of Termination

In the fiscal year of termination:
- Prorate combined treatment to date of termination
- Separate treatment applies from termination date forward
- Complex transition calculations may be required

---

## Common Pitfalls

### Pitfall 1: Double-Counting Top-Up Tax

**Error:** Each UPE calculates and reports 100% of the combined group's Top-Up Tax.

**Correct approach:** Each UPE reports and pays only its **allocable share**. Total paid by both UPEs should equal combined group Top-Up Tax (no more, no less).

### Pitfall 2: Failing to Blend Cross-Parent Jurisdictions

**Error:** Treating Alpha's Germany sub and Beta's Germany sub as separate jurisdictions.

**Correct approach:** Under combined treatment, **all** Constituent Entities in a jurisdiction blend together regardless of which parent owns them.

### Pitfall 3: Ignoring Revenue Threshold Impact

**Error:** Assuming each parent tests €750M threshold independently.

**Correct approach:** Combined group revenue is used for the threshold test. A parent below €750M individually may still be in scope through the combined test.

### Pitfall 4: Inconsistent GIR Filings

**Error:** Each UPE files different data in their respective GIRs.

**Correct approach:** Both UPEs must report the **same** combined group data. Appoint a DFE to ensure consistency.

### Pitfall 5: Misallocating Based on Ownership Rather Than Agreement

**Error:** Allocating based on actual ownership percentages when an equalisation agreement specifies different terms.

**Correct approach:** Allocation follows the **equalisation agreement** terms for DLAs, not underlying ownership ratios.

---

## Multi-Parented Group Assessment Checklist

Use this checklist when evaluating a potential Multi-Parented MNE Group:

```
MULTI-PARENTED GROUP ASSESSMENT CHECKLIST
Structure: _________________________
Parties: _________________________
Fiscal Year: _________________________

═══════════════════════════════════════════════════════════════════════
SECTION A: STRUCTURE QUALIFICATION
═══════════════════════════════════════════════════════════════════════

□ TYPE OF ARRANGEMENT:
   □ Stapled Structure
   □ Dual-Listed Arrangement
   □ Other (describe): _________________________

STAPLED STRUCTURE CRITERIA:
□ Are ownership interests stapled together?             YES / NO
□ Percentage of interests stapled:                      ________%
□ Are stapled interests traded as a unit?               YES / NO

   If <50% stapled: NOT a Multi-Parented MNE Group.

DLA CRITERIA:
□ Are both entities separately listed?                  YES / NO
   □ Entity 1 exchange: _________________________
   □ Entity 2 exchange: _________________________
□ Is there an equalisation agreement?                   YES / NO
□ Do entities operate as single enterprise?             YES / NO
□ Does one parent control the other?                    YES / NO

   If one controls other: NOT a DLA — standard parent-sub structure.

□ **CONCLUSION: Is this a Multi-Parented MNE Group?**   YES / NO

═══════════════════════════════════════════════════════════════════════
SECTION B: COMBINED GROUP IDENTIFICATION
═══════════════════════════════════════════════════════════════════════

PARENT ENTITY 1:
□ Name: _________________________
□ Jurisdiction: _________________________
□ IIR status: _________________________
□ Number of CEs: _________________________

PARENT ENTITY 2:
□ Name: _________________________
□ Jurisdiction: _________________________
□ IIR status: _________________________
□ Number of CEs: _________________________

□ Combined Group revenue:                           €__________________
□ Exceeds €750M threshold?                              YES / NO

□ Jurisdictions with CEs from BOTH parents (will blend):
   1. _________________________
   2. _________________________
   3. _________________________

═══════════════════════════════════════════════════════════════════════
SECTION C: ALLOCATION DETERMINATION
═══════════════════════════════════════════════════════════════════════

□ Allocation method:
   □ Stapled unit ownership ratio
   □ Equalisation agreement terms
   □ Other (specify): _________________________

□ Parent Entity 1 allocable share:                      ________%
□ Parent Entity 2 allocable share:                      ________%
□ Total (must equal 100%):                              ________%

═══════════════════════════════════════════════════════════════════════
SECTION D: ETR CALCULATION (Combined Jurisdictions)
═══════════════════════════════════════════════════════════════════════

Jurisdiction: ___________________________

□ CEs from Parent 1 in this jurisdiction: _________________________
□ CEs from Parent 2 in this jurisdiction: _________________________

□ Combined GloBE Income:                            €__________________
□ Combined Adjusted Covered Taxes:                  €__________________
□ Combined ETR:                                     __________________%

   If ETR ≥ 15%: No Top-Up Tax. Move to next jurisdiction.

□ Combined SBIE:                                    €__________________
□ Combined Excess Profit:                           €__________________
□ Top-Up Tax %:                                     __________________%
□ Jurisdictional Top-Up Tax:                        €__________________

(Repeat for each jurisdiction)

═══════════════════════════════════════════════════════════════════════
SECTION E: TOP-UP TAX ALLOCATION
═══════════════════════════════════════════════════════════════════════

□ Total Combined Group Top-Up Tax:                  €__________________

□ Allocation:
   □ Parent Entity 1 (_______%):                    €__________________
   □ Parent Entity 2 (_______%):                    €__________________

□ IIR payment responsibility:
   □ Parent 1 jurisdiction: _____________ IIR? YES / NO
   □ Parent 2 jurisdiction: _____________ IIR? YES / NO

═══════════════════════════════════════════════════════════════════════
SECTION F: GIR FILING
═══════════════════════════════════════════════════════════════════════

□ Filing approach:
   □ Each UPE files separately (coordinate data)
   □ Single DFE appointed

□ If DFE appointed:
   □ DFE name: _________________________
   □ DFE jurisdiction: _________________________
   □ Notification filed by other UPE?                   YES / NO

═══════════════════════════════════════════════════════════════════════
SECTION G: SUMMARY
═══════════════════════════════════════════════════════════════════════

□ Combined Group Total Top-Up Tax:                  €__________________
□ Parent Entity 1 Allocable Share:                  €__________________
□ Parent Entity 2 Allocable Share:                  €__________________

□ Documentation complete?                               YES / NO
□ GIR coordination process established?                 YES / NO
```

---

## Summary

Multi-Parented MNE Groups require combined treatment under Article 6.5:

| Aspect | Key Rule |
|--------|----------|
| **Structures** | Stapled (≥50% stapled) or DLA (equalisation agreement) |
| **Treatment** | Combined as single MNE Group |
| **Revenue test** | Combined group revenue for €750M threshold |
| **Blending** | All CEs blend by jurisdiction (regardless of parent) |
| **Allocation** | Top-Up Tax split per ownership ratio or agreement |
| **Filing** | Both UPEs obligated; DFE recommended |
| **IIR** | Each UPE pays on its allocable share |

**Key distinction:** Multi-Parented Groups differ from standard structures because there is no single UPE — both parents share GloBE obligations proportionally.

---

## Integration with GIR Tools

Multi-Parented Group calculations require **combined data** in GIR-001:

| Consideration | Action |
|---------------|--------|
| **Input data** | Combine all CEs from both parent structures |
| **Jurisdictional grouping** | Blend CEs from both parents in same jurisdiction |
| **Output allocation** | Apply allocable share to Top-Up Tax results |

**GIR-001 Workflow for Multi-Parented Groups:**

```
Step 1: Identify all CEs from both parent entities
Step 2: Confirm Multi-Parented status (≥50% stapled or valid DLA)
Step 3: Input combined group data into GIR-001
Step 4: Run standard ETR calculations with combined blending
Step 5: Extract total Top-Up Tax
Step 6: Allocate per ownership ratio or equalisation agreement
Step 7: Each UPE reports allocated share in respective GIR
```

**GIR Reporting Note:** The GIR must identify the structure as Multi-Parented and disclose the other Joint UPE(s). Allocation methodology must be consistently applied year-on-year.

---

## Next Step

You have learned how to identify and handle Multi-Parented MNE Groups. Proceed to **Chapter 6.5: Flow-Through UPEs** for guidance on transparent entities at the top of MNE Group structures.
