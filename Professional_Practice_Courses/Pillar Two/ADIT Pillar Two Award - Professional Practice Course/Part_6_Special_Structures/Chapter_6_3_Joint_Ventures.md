# Chapter 6.3: Joint Ventures

## Learning Objective

After completing this chapter, you will be able to identify when an entity qualifies as a Joint Venture for GloBE purposes, apply the separate ETR calculation requirement, allocate Top-up Tax to the UPE based on ownership share, and distinguish JV treatment from MOCE and regular Constituent Entity treatment.

---

## Key References

**OECD GloBE Model Rules:**
- Article 6.4.1(a) — JV treated as separate MNE Group
- Article 6.4.1(b) — JV Subsidiaries included in separate calculation
- Article 6.4.1(c) — Top-up Tax allocation to parent entities
- Article 10.1 — Definition of Joint Venture

**OECD Commentary:**
- Chapter 6, paragraphs 99-125 — Joint Venture rules

**Administrative Guidance:**
- December 2023: Multiple blending groups in same jurisdiction
- June 2024: JV Safe Harbour considerations

---

## Why Special Rules for Joint Ventures?

Joint Ventures present a unique challenge for Pillar Two:

```
┌─────────────────────────────────────────────────────────────────────┐
│ THE JV PROBLEM                                                      │
│                                                                     │
│ Standard GloBE scope:                                               │
│ → Only entities consolidated on a line-by-line basis are CEs       │
│ → JVs are typically equity-accounted, not consolidated             │
│ → Without special rules, JVs would escape Pillar Two entirely      │
│                                                                     │
│ THE SOLUTION (Article 6.4):                                         │
│ → Bring JVs into scope through special rules                       │
│ → Treat JV + subsidiaries as a SEPARATE MNE Group                  │
│ → Calculate ETR and Top-up Tax separately                          │
│ → Allocate Top-up Tax to UPE based on ownership share              │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Definition: Joint Venture *(Article 10.1)*

A **Joint Venture** for GloBE purposes is an entity that meets ALL of the following criteria:

| Criterion | Requirement |
|-----------|-------------|
| **Accounting treatment** | Financial results reported under the **equity method** in UPE's Consolidated Financial Statements |
| **Ownership threshold** | UPE holds **directly or indirectly at least 50%** of Ownership Interests |
| **Not already in scope** | Entity is not itself the UPE of an MNE Group subject to GloBE |

### What the Equity Method Means

Under equity accounting (IAS 28 / ASC 323):
- The investor records its share of the JV's profit/loss
- The JV's assets, liabilities, income, and expenses are **not** consolidated line-by-line
- The investment is shown as a single line item in the investor's balance sheet

### The 50% Threshold

```
JV Ownership Test:

UPE Ownership ≥ 50%  →  Qualifies as JV for GloBE
                        (if equity-accounted)

UPE Ownership < 50%  →  Does NOT qualify as JV
                        (treated as simple equity investment)
```

**Important:** The ≥50% threshold brings **non-consolidated** entities into GloBE scope. Without this rule, an MNE could shelter income in 50/50 JVs that escape Pillar Two.

---

## Comparison: JV vs MOCE vs Regular CE

| Feature | Joint Venture | MOCE | Regular CE |
|---------|---------------|------|------------|
| **Ownership** | ≥50% | ≤30% | Any |
| **Accounting** | Equity method | Consolidated | Consolidated |
| **GloBE treatment** | Separate MNE Group | Separate ETR (entity level) | Jurisdictional blending |
| **Blending** | Within JV group only | None (entity-level) | With other CEs |
| **Top-up Tax** | Allocated to UPE | UPE bears directly | Via IIR/UTPR |

### Visual Comparison

```
REGULAR CE (100% owned, consolidated):
┌─────────────────┐
│      UPE        │
│   ↓ 100%        │
│   SubCo         │──────► Blended with other CEs in jurisdiction
└─────────────────┘

MOCE (28% owned, consolidated):
┌─────────────────┐
│      UPE        │
│   ↓ 28%         │
│   MOCE          │──────► Separate ETR calculation (Art. 5.6)
└─────────────────┘

JOINT VENTURE (50% owned, equity-accounted):
┌─────────────────┐
│      UPE        │
│   ↓ 50%         │
│   JV Entity     │──────► Treated as SEPARATE MNE Group (Art. 6.4)
│   ↓ 100%        │
│   JV Sub        │
└─────────────────┘
```

---

## The JV as a Separate MNE Group *(Article 6.4.1(a))*

When an entity qualifies as a JV:

```
┌─────────────────────────────────────────────────────────────────────┐
│ JV TREATMENT (Article 6.4.1)                                        │
│                                                                     │
│ The JV and its subsidiaries are treated AS IF they were:           │
│                                                                     │
│ → A SEPARATE MNE Group                                              │
│ → With the JV as the Ultimate Parent Entity                        │
│ → Subject to their own ETR calculation                             │
│ → With their own jurisdictional blending (within JV group only)    │
│                                                                     │
│ The main MNE Group's calculations EXCLUDE the JV's results.        │
└─────────────────────────────────────────────────────────────────────┘
```

### JV Subsidiaries

**JV Subsidiaries** are entities in which the JV holds a controlling interest. They are:
- Included in the JV's separate MNE Group
- Subject to jurisdictional blending within the JV group
- NOT blended with the main MNE Group

---

## Separate ETR Calculation

### No Blending with Main Group

The JV Group's GloBE Income and Covered Taxes are **never blended** with the main MNE Group:

**Example:**

| Jurisdiction | Main Group | JV Group | Combined? |
|--------------|------------|----------|-----------|
| **Germany** | | | |
| GloBE Income | €50,000,000 | €8,000,000 | **NO** |
| Covered Taxes | €11,500,000 | €1,600,000 | **NO** |
| ETR | **23.00%** | **20.00%** | Calculated separately |

Even though both are in Germany, they have separate ETR calculations.

### Blending Within JV Group

If the JV has subsidiaries in multiple jurisdictions, **jurisdictional blending applies within the JV group**:

**Example: JV with subsidiaries in two jurisdictions**

```
JV Entity (Germany) ─── 100% ──► JV Sub 1 (Germany)
                   ─── 100% ──► JV Sub 2 (Ireland)

JV Group Germany calculation:
→ Blend JV Entity + JV Sub 1 (both in Germany)
→ JV Sub 2 (Ireland) calculated separately within JV Group
```

---

## Top-Up Tax Allocation *(Article 6.4.1(c))*

### Who Pays the Top-Up Tax?

The **UPE of the main MNE Group** (or intermediate parent with IIR) pays Top-up Tax on its **allocable share** of the JV's Top-up Tax.

```
Top-up Tax Allocation = JV Group Top-up Tax × UPE's Ownership %
```

### Example: 50/50 JV

**Scenario:** Alpha Group and Beta Group each own 50% of JV Co.

```
JV Co (Germany)
├── GloBE Income: €10,000,000
├── Covered Taxes: €1,200,000
├── ETR: 12.00%
├── Top-up Tax %: 3.00%
├── SBIE: €500,000
├── Excess Profit: €9,500,000
└── JV Top-up Tax: €285,000

Allocation:
├── Alpha Group (50%): €142,500
└── Beta Group (50%): €142,500
```

**Each UPE pays its 50% share via IIR** (if in an IIR jurisdiction).

### Direct and Indirect Holdings

The allocable share includes **both direct and indirect** holdings:

```
UPE owns 60% of HoldCo
HoldCo owns 80% of JV

UPE's ownership in JV = 60% × 80% = 48%

Wait — 48% < 50%, so is this a JV?

Answer: Check total ownership through ALL paths.
If UPE also holds 5% directly in JV:
Total = 48% + 5% = 53% → Qualifies as JV

Top-up Tax allocation = 53% of JV Top-up Tax
```

---

## JV as Partially-Owned Parent Entity (POPE)

If the JV itself qualifies as a **POPE** (owned less than 80% by the main UPE), the charging mechanism shifts:

### Standard JV (≥80% owned by main UPE):
- Main UPE pays all Top-up Tax on JV group via IIR

### JV as POPE (<80% owned by main UPE):
- Main UPE pays Top-up Tax on **JV entity itself** (based on ownership %)
- **JV (as POPE) pays** Top-up Tax on its **subsidiaries**

```
┌─────────────────────────────────────────────────────────────────────┐
│ JV AS POPE EXAMPLE                                                  │
│                                                                     │
│ Main UPE owns 60% of JV Entity                                      │
│ JV Entity owns 100% of JV Sub (low-taxed)                          │
│                                                                     │
│ Top-up Tax on JV Entity:                                            │
│ → Allocated to Main UPE (60%)                                       │
│ → Allocated to other JV investors (40%)                            │
│                                                                     │
│ Top-up Tax on JV Sub:                                               │
│ → Paid by JV Entity (as POPE) — 100%                               │
│ → NOT allocated to Main UPE                                         │
└─────────────────────────────────────────────────────────────────────┘
```

---

## QDMTT Interaction

### QDMTT Priority

If the JV's jurisdiction has a QDMTT:
1. The jurisdiction collects QDMTT first
2. QDMTT reduces the IIR liability
3. Credit given to the main UPE for QDMTT paid

### Example: JV in Ireland (with QDMTT)

| Item | Amount |
|------|--------|
| JV Ireland GloBE Income | €6,000,000 |
| JV Ireland Covered Taxes | €600,000 |
| JV Ireland ETR | 10.00% |
| Top-up Tax % | 5.00% |
| SBIE | €300,000 |
| Excess Profit | €5,700,000 |
| JV Top-up Tax | €285,000 |

**QDMTT Treatment:**
- Ireland collects €285,000 via QDMTT
- Main UPE's IIR liability: €0 (offset by QDMTT)
- JV investors indirectly bear QDMTT through reduced JV distributions

---

## Stratos Worked Example: JV with TechPartner

### Background

Stratos Holdings plc has a 55% interest in **EuroTech JV GmbH**, a joint venture with TechPartner AG (45%). EuroTech JV is equity-accounted in Stratos's consolidated financial statements.

### JV Structure

```
Stratos Holdings plc ──── 55% ────┐
                                  ▼
                         EuroTech JV GmbH (Germany)
                                  │
TechPartner AG ──────── 45% ──────┘
                                  │
                            100%  │
                                  ▼
                         EuroTech France SAS
```

### Step 1: Confirm JV Status

| Criterion | Assessment |
|-----------|------------|
| Equity method? | Yes — not consolidated in Stratos accounts |
| UPE ownership ≥50%? | Yes — 55% |
| Not UPE of another in-scope MNE? | Confirmed |
| **Classification** | **Joint Venture for GloBE** |

### Step 2: Identify JV Group

The JV Group consists of:
- EuroTech JV GmbH (Germany) — the JV entity
- EuroTech France SAS (France) — JV Subsidiary

### Step 3: Calculate ETR for JV Group

**EuroTech JV GmbH (Germany):**

| Item | Amount |
|------|--------|
| GloBE Income | €8,000,000 |
| Adjusted Covered Taxes | €1,840,000 |
| ETR | **23.00%** |

**Result:** Germany ETR ≥ 15% → No Top-up Tax for Germany.

**EuroTech France SAS (France):**

| Item | Amount |
|------|--------|
| GloBE Income | €3,500,000 |
| Adjusted Covered Taxes | €385,000 |
| ETR | **11.00%** |

**Result:** France ETR < 15% → Top-up Tax applies.

### Step 4: Calculate SBIE and Top-up Tax for France

**France SBIE (FY 2025 rates):**

| Component | Amount | Rate | Carve-out |
|-----------|--------|------|-----------|
| Payroll | €1,800,000 | 9.8% | €176,400 |
| Tangible Assets | €2,200,000 | 7.8% | €171,600 |
| **Total SBIE** | | | **€348,000** |

**France Top-up Tax:**

```
Excess Profit = €3,500,000 − €348,000 = €3,152,000
Top-up Tax % = 15% − 11% = 4%
Top-up Tax = €3,152,000 × 4% = €126,080
```

### Step 5: Allocate Top-up Tax

**JV Group Top-up Tax:** €126,080 (France only)

**Allocation:**

| Investor | Ownership | Allocated Top-up Tax |
|----------|-----------|---------------------|
| Stratos Holdings plc | 55% | **€69,344** |
| TechPartner AG | 45% | €56,736 |
| **Total** | 100% | **€126,080** |

### Step 6: Determine Collection Mechanism

**France QDMTT Status:** France has implemented QDMTT.

| Item | Amount |
|------|--------|
| JV France Top-up Tax | €126,080 |
| QDMTT paid by EuroTech France | (€126,080) |
| Net IIR liability | **€0** |

**Result:** France retains the €126,080 via QDMTT. Stratos's IIR liability is €0 (QDMTT offset).

### Summary: Stratos JV Position

| JV Jurisdiction | ETR | Top-up Tax | Stratos Share | QDMTT? | Net IIR |
|-----------------|-----|------------|---------------|--------|---------|
| Germany | 23.00% | €0 | €0 | N/A | €0 |
| France | 11.00% | €126,080 | €69,344 | Yes | **€0** |

---

## Common Pitfalls

### Pitfall 1: Treating <50% Equity Investments as JVs

**Error:** Applying JV rules to an associate with only 30% ownership.

**Correct approach:** The ≥50% threshold must be met. Associates with <50% ownership are **not** JVs for GloBE purposes and are outside Pillar Two scope (unless they are consolidated for some other reason).

### Pitfall 2: Blending JV with Main Group

**Error:** Including JV's GloBE Income and Covered Taxes in the main MNE Group's jurisdictional ETR calculation.

**Correct approach:** JV and its subsidiaries are a **separate MNE Group**. Never blend with main group CEs.

### Pitfall 3: Ignoring JV Subsidiaries

**Error:** Calculating ETR only for the JV entity and forgetting JV subsidiaries.

**Correct approach:** JV Subsidiaries are part of the JV Group. Include all subsidiaries in the separate ETR calculation with appropriate jurisdictional blending.

### Pitfall 4: Incorrect POPE Treatment

**Error:** Allocating all JV Group Top-up Tax to the main UPE when the JV is a POPE.

**Correct approach:** If the JV is a POPE (<80% owned by main UPE), the JV itself pays Top-up Tax on its subsidiaries. Only Top-up Tax on the JV entity is allocated to the main UPE.

### Pitfall 5: Double-Counting with QDMTT

**Error:** Reporting IIR liability without offsetting QDMTT paid by JV entities.

**Correct approach:** QDMTT has priority. Credit QDMTT paid against IIR liability.

---

## Joint Venture Assessment Checklist

Use this checklist when an entity may be a JV:

```
JOINT VENTURE ASSESSMENT CHECKLIST
Entity: _________________________
Jurisdiction: _________________________
Fiscal Year: _________________________

═══════════════════════════════════════════════════════════════════════
SECTION A: JV QUALIFICATION
═══════════════════════════════════════════════════════════════════════

□ Is entity reported under equity method in UPE's accounts?   YES / NO

   If NO: Not a JV. Check if consolidated (CE) or below threshold.

□ Does UPE hold ≥50% ownership (direct + indirect)?           YES / NO
   □ Direct ownership:                                        ________%
   □ Indirect ownership (calculate):                          ________%
   □ Total ownership:                                         ________%

   If <50%: Not a JV. Entity is outside GloBE scope (unless consolidated).

□ Is entity itself UPE of an in-scope MNE Group?              YES / NO

   If YES: Not a JV. Subject to GloBE in its own right.

□ **CONCLUSION: Is entity a Joint Venture?**                  YES / NO

═══════════════════════════════════════════════════════════════════════
SECTION B: JV GROUP IDENTIFICATION
═══════════════════════════════════════════════════════════════════════

□ List JV Subsidiaries (entities controlled by JV):
   1. ___________________________ (Jurisdiction: ___________)
   2. ___________________________ (Jurisdiction: ___________)
   3. ___________________________ (Jurisdiction: ___________)

□ JV Group jurisdictions requiring ETR calculation:
   1. ___________________________
   2. ___________________________
   3. ___________________________

═══════════════════════════════════════════════════════════════════════
SECTION C: ETR CALCULATION (By Jurisdiction within JV Group)
═══════════════════════════════════════════════════════════════════════

Jurisdiction: ___________________________

□ JV entities in this jurisdiction: ___________________________
□ Blended GloBE Income:                          €__________________
□ Blended Adjusted Covered Taxes:                €__________________
□ ETR:                                           __________________%

   If ETR ≥ 15%: No Top-up Tax. Move to next jurisdiction.

□ SBIE Calculation:
   □ Payroll carve-out (9.8%):                   €__________________
   □ Asset carve-out (7.8%):                     €__________________
   □ Total SBIE:                                 €__________________

□ Excess Profit:                                 €__________________
□ Top-up Tax %:                                  __________________%
□ JV Jurisdictional Top-up Tax:                  €__________________

(Repeat for each JV Group jurisdiction)

═══════════════════════════════════════════════════════════════════════
SECTION D: TOP-UP TAX ALLOCATION
═══════════════════════════════════════════════════════════════════════

□ Total JV Group Top-up Tax:                     €__________________

□ Is JV a POPE (<80% owned by main UPE)?         YES / NO

   If NO: All Top-up Tax allocated to investors

□ Allocation to main UPE:
   □ UPE ownership %:                            __________________%
   □ UPE's allocated share:                      €__________________

□ Allocation to other JV investors:              €__________________

═══════════════════════════════════════════════════════════════════════
SECTION E: QDMTT OFFSET
═══════════════════════════════════════════════════════════════════════

□ Does JV jurisdiction have QDMTT?               YES / NO

   If NO: Full IIR liability applies.

□ QDMTT paid by JV entities:                     €__________________
□ Net IIR liability (after QDMTT offset):        €__________________

═══════════════════════════════════════════════════════════════════════
SECTION F: SUMMARY
═══════════════════════════════════════════════════════════════════════

□ JV Group Total Top-up Tax:                     €__________________
□ UPE's Allocated Share:                         €__________________
□ QDMTT Offset:                                 (€__________________)
□ **Net IIR Liability for UPE:**                 €__________________

□ Documentation complete?                        YES / NO
```

---

## Summary

Joint Ventures require special treatment under Pillar Two to bring equity-accounted investments into scope:

| Aspect | Key Rule |
|--------|----------|
| **Definition** | Equity method + ≥50% UPE ownership |
| **Treatment** | Separate MNE Group (JV as UPE) |
| **ETR calculation** | Separate from main group; blending within JV group only |
| **Top-up Tax** | Allocated to main UPE based on ownership % |
| **POPE complication** | If JV <80% owned, JV pays on its subsidiaries |
| **QDMTT** | Offsets IIR liability; credit to investors |

**Key distinction:** JVs (≥50%, equity method) are brought into scope through Article 6.4. Associates (<50%) remain outside GloBE scope.

---

## Integration with GIR Tools

JV calculations require **separate runs** through GIR-001:

| Run | Scope | Data Input |
|-----|-------|------------|
| Run 1 | Main MNE Group | Exclude JV and JV Subsidiaries |
| Run 2 | JV Group | JV entity + JV Subsidiaries only |

**GIR Reporting:**
- JVs are reported separately in the GloBE Information Return
- Ownership percentages must be disclosed
- Top-up Tax allocation documented

**GIR-001 Workflow for JVs:**

```
Step 1: Identify JV Group entities
Step 2: Run GIR-001 for JV Group (separate from main group)
Step 3: Calculate JV Group Top-up Tax
Step 4: Allocate to investors based on ownership %
Step 5: Apply QDMTT offset if applicable
Step 6: Report UPE's allocated share in main group GIR
```

---

## Next Step

You have learned how to identify and calculate Top-up Tax for Joint Ventures. Proceed to **Chapter 6.4: Multi-Parented Groups** for guidance on stapled structures, dual-listed companies, and combined group treatment.
