# Chapter 6.3: Joint Ventures

## Learning Objective

After completing this chapter, you will be able to identify when an entity qualifies as a Joint Venture for GloBE purposes, apply the separate ETR calculation requirement, allocate Top-Up Tax to the UPE based on ownership share, and distinguish JV treatment from MOCE and regular Constituent Entity treatment.

## Introduction

Joint ventures occupy a unique position in corporate group structures. Unlike fully-owned subsidiaries that are consolidated line-by-line in the parent's financial statements, joint ventures are typically equity-accounted—meaning the investor recognises only its share of the JV's profit or loss as a single line item, without consolidating individual assets, liabilities, revenues, and expenses. This accounting treatment reflects the economic reality that the investor shares control with one or more partners and cannot unilaterally direct the JV's activities. For GloBE purposes, however, equity accounting creates a potential gap: entities that escape line-by-line consolidation fall outside the standard definition of Constituent Entity, which could allow MNE Groups to shelter low-taxed income in joint venture structures.

Article 6.4 addresses this gap by bringing joint ventures with at least 50% ownership into GloBE scope through special rules that treat the JV and its subsidiaries as a separate MNE Group. This chapter examines these rules in detail, including the criteria for JV classification, the separate ETR calculation methodology, and the mechanics of Top-Up Tax allocation to joint venture investors. Understanding JV treatment is essential because it differs meaningfully from both regular Constituent Entity treatment (with jurisdictional blending) and MOCE treatment (with entity-level separate calculation)—creating a third category with its own distinct rules.

## 1. Why Special Rules for Joint Ventures?

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
│ → Calculate ETR and Top-Up Tax separately                          │
│ → Allocate Top-Up Tax to UPE based on ownership share              │
└─────────────────────────────────────────────────────────────────────┘
```

## 2. Definition: Joint Venture *(Article 10.1)*

A **Joint Venture** for GloBE purposes is an entity that meets ALL of the following criteria:

| Criterion | Requirement |
|-----------|-------------|
| **Accounting treatment** | Financial results reported under the **equity method** in UPE's Consolidated Financial Statements |
| **Ownership threshold** | UPE holds **directly or indirectly at least 50%** of Ownership Interests |
| **Not already in scope** | Entity is not itself the UPE of an MNE Group subject to GloBE |

### 2.1 What the Equity Method Means

Under equity accounting (IAS 28 / ASC 323):
- The investor records its share of the JV's profit/loss
- The JV's assets, liabilities, income, and expenses are **not** consolidated line-by-line
- The investment is shown as a single line item in the investor's balance sheet

### 2.2 The 50% Threshold

```
JV Ownership Test:

UPE Ownership ≥ 50%  →  Qualifies as JV for GloBE
                        (if equity-accounted)

UPE Ownership < 50%  →  Does NOT qualify as JV
                        (treated as simple equity investment)
```

**Important:** The ≥50% threshold brings **non-consolidated** entities into GloBE scope. Without this rule, an MNE could shelter income in 50/50 JVs that escape Pillar Two.

The 50% ownership threshold represents a deliberate policy choice about where to draw the line for GloBE's extended reach. At 50% or more, the investor has sufficient ownership to benefit materially from the JV's low-taxed profits—and to influence, if not control, the JV's tax planning decisions. Below 50%, the ownership becomes more analogous to a portfolio investment where the investor is a passive recipient of returns rather than an active participant in the enterprise. The threshold also aligns roughly with accounting significance: investments of 20-50% typically receive equity-method treatment under IAS 28, while investments below 20% are often treated as fair value through P&L. By capturing entities at 50% and above, GloBE ensures that meaningful joint venture arrangements cannot be used to circumvent the minimum tax while avoiding extension to passive minority investments that present less policy concern.

## 3. Comparison: JV vs MOCE vs Regular CE

| Feature | Joint Venture | MOCE | Regular CE |
|---------|---------------|------|------------|
| **Ownership** | ≥50% | ≤30% | Any |
| **Accounting** | Equity method | Consolidated | Consolidated |
| **GloBE treatment** | Separate MNE Group | Separate ETR (entity level) | Jurisdictional blending |
| **Blending** | Within JV group only | None (entity-level) | With other CEs |
| **Top-Up Tax** | Allocated to UPE | UPE bears directly | Via IIR/UTPR |

### 3.1 Visual Comparison

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

The distinction between these three categories—Regular CE, MOCE, and JV—reflects the framework's attempt to match GloBE treatment to economic substance. Regular Constituent Entities are fully within the group's control and consolidated; they blend with other entities in their jurisdiction because the UPE bears all the consequences of their combined performance. MOCEs are consolidated despite minority economic ownership, so they require separate calculation to prevent the UPE from benefiting from taxes borne by minority shareholders. JVs present the opposite situation: they are not consolidated despite significant ownership, so they require inclusion through the separate MNE Group mechanism to prevent undertaxed profits from escaping GloBE entirely. Each category receives treatment calibrated to its ownership and accounting characteristics.

## 4. The JV as a Separate MNE Group *(Article 6.4.1(a))*

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

### 4.1 JV Subsidiaries

**JV Subsidiaries** are entities in which the JV holds a controlling interest. They are:
- Included in the JV's separate MNE Group
- Subject to jurisdictional blending within the JV group
- NOT blended with the main MNE Group

## 5. Separate ETR Calculation

### 5.1 No Blending with Main Group

The JV Group's GloBE Income and Covered Taxes are **never blended** with the main MNE Group:

**Example:**

| Jurisdiction | Main Group | JV Group | Combined? |
|--------------|------------|----------|-----------|
| **Germany** | | | |
| GloBE Income | €50,000,000 | €8,000,000 | **NO** |
| Covered Taxes | €11,500,000 | €1,600,000 | **NO** |
| ETR | **23.00%** | **20.00%** | Calculated separately |

Even though both are in Germany, they have separate ETR calculations.

### 5.2 Blending Within JV Group

If the JV has subsidiaries in multiple jurisdictions, **jurisdictional blending applies within the JV group**:

**Example: JV with subsidiaries in two jurisdictions**

```
JV Entity (Germany) ─── 100% ──► JV Sub 1 (Germany)
                   ─── 100% ──► JV Sub 2 (Ireland)

JV Group Germany calculation:
→ Blend JV Entity + JV Sub 1 (both in Germany)
→ JV Sub 2 (Ireland) calculated separately within JV Group
```

The "separate MNE Group" treatment for JVs creates a parallel calculation universe that operates independently from the main group. This has significant practical implications. The JV Group must maintain its own GloBE data collection, perform its own adjustments to arrive at GloBE Income and Adjusted Covered Taxes, and apply SBIE based on its own payroll and tangible assets. Where the JV has multiple subsidiaries, jurisdictional blending applies within the JV Group—but always separately from any main group entities in the same jurisdiction. This segregation ensures that a high-taxed JV cannot shield low-taxed main group entities (or vice versa) simply because they happen to operate in the same country. The complexity increases when multiple MNE Groups each have significant stakes in the same JV, as each must perform its own GloBE analysis from its own perspective as an investor.

## 6. Top-Up Tax Allocation *(Article 6.4.1(c))*

### 6.1 Who Pays the Top-Up Tax?

The **UPE of the main MNE Group** (or intermediate parent with IIR) pays Top-Up Tax on its **allocable share** of the JV's Top-Up Tax.

```
Top-Up Tax Allocation = JV Group Top-Up Tax × UPE's Ownership %
```

### 6.2 Example: 50/50 JV

**Scenario:** Alpha Group and Beta Group each own 50% of JV Co.

```
JV Co (Germany)
├── GloBE Income: €10,000,000
├── Covered Taxes: €1,200,000
├── ETR: 12.00%
├── Top-Up Tax %: 3.00%
├── SBIE: €500,000
├── Excess Profit: €9,500,000
└── JV Top-Up Tax: €285,000

Allocation:
├── Alpha Group (50%): €142,500
└── Beta Group (50%): €142,500
```

**Each UPE pays its 50% share via IIR** (if in an IIR jurisdiction).

### 6.3 Direct and Indirect Holdings

The allocable share includes **both direct and indirect** holdings:

```
UPE owns 60% of HoldCo
HoldCo owns 80% of JV

UPE's ownership in JV = 60% × 80% = 48%

Wait — 48% < 50%, so is this a JV?

Answer: Check total ownership through ALL paths.
If UPE also holds 5% directly in JV:
Total = 48% + 5% = 53% → Qualifies as JV

Top-Up Tax allocation = 53% of JV Top-Up Tax
```

## 7. JV as Partially-Owned Parent Entity (POPE)

If the JV itself qualifies as a **POPE** (owned less than 80% by the main UPE), the charging mechanism shifts:

### 7.1 Standard JV (≥80% owned by main UPE):
- Main UPE pays all Top-Up Tax on JV group via IIR

### 7.2 JV as POPE (<80% owned by main UPE):
- Main UPE pays Top-Up Tax on **JV entity itself** (based on ownership %)
- **JV (as POPE) pays** Top-Up Tax on its **subsidiaries**

```
┌─────────────────────────────────────────────────────────────────────┐
│ JV AS POPE EXAMPLE                                                  │
│                                                                     │
│ Main UPE owns 60% of JV Entity                                      │
│ JV Entity owns 100% of JV Sub (low-taxed)                          │
│                                                                     │
│ Top-Up Tax on JV Entity:                                            │
│ → Allocated to Main UPE (60%)                                       │
│ → Allocated to other JV investors (40%)                            │
│                                                                     │
│ Top-Up Tax on JV Sub:                                               │
│ → Paid by JV Entity (as POPE) — 100%                               │
│ → NOT allocated to Main UPE                                         │
└─────────────────────────────────────────────────────────────────────┘
```

The POPE rules add another layer of complexity to JV treatment, shifting the charging mechanism when the main UPE's ownership falls below the 80% threshold. The policy rationale is consistency with the broader IIR architecture: POPEs with significant minority shareholders should collect Top-Up Tax on their subsidiaries directly, rather than having that tax liability flow up to a UPE that owns less than 80% of the intermediate parent. For JVs, this means distinguishing between Top-Up Tax on the JV entity itself (allocated to investors based on ownership percentage) and Top-Up Tax on JV subsidiaries (borne by the JV as POPE if ownership is below 80%). In practice, most 50/50 joint ventures will trigger POPE treatment, meaning each investor is only directly responsible for its share of the JV entity's own Top-Up Tax, with the JV itself bearing responsibility for subsidiary-level Top-Up Tax.

## 8. QDMTT Interaction

### 8.1 QDMTT Priority

If the JV's jurisdiction has a QDMTT:
1. The jurisdiction collects QDMTT first
2. QDMTT reduces the IIR liability
3. Credit given to the main UPE for QDMTT paid

### 8.2 Example: JV in Ireland (with QDMTT)

| Item | Amount |
|------|--------|
| JV Ireland GloBE Income | €6,000,000 |
| JV Ireland Covered Taxes | €600,000 |
| JV Ireland ETR | 10.00% |
| Top-Up Tax % | 5.00% |
| SBIE | €300,000 |
| Excess Profit | €5,700,000 |
| JV Top-Up Tax | €285,000 |

**QDMTT Treatment:**
- Ireland collects €285,000 via QDMTT
- Main UPE's IIR liability: €0 (offset by QDMTT)
- JV investors indirectly bear QDMTT through reduced JV distributions

## 9. Stratos Worked Example: JV with TechPartner

### 9.1 Background

Stratos Holdings plc has a 55% interest in **EuroTech JV GmbH**, a joint venture with TechPartner AG (45%). EuroTech JV is equity-accounted in Stratos's consolidated financial statements.

### 9.2 JV Structure

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

### 9.3 Step 1: Confirm JV Status

| Criterion | Assessment |
|-----------|------------|
| Equity method? | Yes — not consolidated in Stratos accounts |
| UPE ownership ≥50%? | Yes — 55% |
| Not UPE of another in-scope MNE? | Confirmed |
| **Classification** | **Joint Venture for GloBE** |

### 9.4 Step 2: Identify JV Group

The JV Group consists of:
- EuroTech JV GmbH (Germany) — the JV entity
- EuroTech France SAS (France) — JV Subsidiary

### 9.5 Step 3: Calculate ETR for JV Group

**EuroTech JV GmbH (Germany):**

| Item | Amount |
|------|--------|
| GloBE Income | €8,000,000 |
| Adjusted Covered Taxes | €1,840,000 |
| ETR | **23.00%** |

**Result:** Germany ETR ≥ 15% → No Top-Up Tax for Germany.

**EuroTech France SAS (France):**

| Item | Amount |
|------|--------|
| GloBE Income | €3,500,000 |
| Adjusted Covered Taxes | €385,000 |
| ETR | **11.00%** |

**Result:** France ETR < 15% → Top-Up Tax applies.

### 9.6 Step 4: Calculate SBIE and Top-Up Tax for France

**France SBIE (FY 2025 rates):**

| Component | Amount | Rate | Carve-out |
|-----------|--------|------|-----------|
| Payroll | €1,800,000 | 9.8% | €176,400 |
| Tangible Assets | €2,200,000 | 7.8% | €171,600 |
| **Total SBIE** | | | **€348,000** |

**France Top-Up Tax:**

```
Excess Profit = €3,500,000 − €348,000 = €3,152,000
Top-Up Tax % = 15% − 11% = 4%
Top-Up Tax = €3,152,000 × 4% = €126,080
```

### Step 5: Allocate Top-Up Tax

**JV Group Top-Up Tax:** €126,080 (France only)

**Allocation:**

| Investor | Ownership | Allocated Top-Up Tax |
|----------|-----------|---------------------|
| Stratos Holdings plc | 55% | **€69,344** |
| TechPartner AG | 45% | €56,736 |
| **Total** | 100% | **€126,080** |

### 9.8 Step 6: Determine Collection Mechanism

**France QDMTT Status:** France has implemented QDMTT.

| Item | Amount |
|------|--------|
| JV France Top-Up Tax | €126,080 |
| QDMTT paid by EuroTech France | (€126,080) |
| Net IIR liability | **€0** |

**Result:** France retains the €126,080 via QDMTT. Stratos's IIR liability is €0 (QDMTT offset).

### 9.9 Summary: Stratos JV Position

| JV Jurisdiction | ETR | Top-Up Tax | Stratos Share | QDMTT? | Net IIR |
|-----------------|-----|------------|---------------|--------|---------|
| Germany | 23.00% | €0 | €0 | N/A | €0 |
| France | 11.00% | €126,080 | €69,344 | Yes | **€0** |

## 10. Common Pitfalls

### 10.1 Pitfall 1: Treating <50% Equity Investments as JVs

**Error:** Applying JV rules to an associate with only 30% ownership.

**Correct approach:** The ≥50% threshold must be met. Associates with <50% ownership are **not** JVs for GloBE purposes and are outside Pillar Two scope (unless they are consolidated for some other reason).

### 10.2 Pitfall 2: Blending JV with Main Group

**Error:** Including JV's GloBE Income and Covered Taxes in the main MNE Group's jurisdictional ETR calculation.

**Correct approach:** JV and its subsidiaries are a **separate MNE Group**. Never blend with main group CEs.

### 10.3 Pitfall 3: Ignoring JV Subsidiaries

**Error:** Calculating ETR only for the JV entity and forgetting JV subsidiaries.

**Correct approach:** JV Subsidiaries are part of the JV Group. Include all subsidiaries in the separate ETR calculation with appropriate jurisdictional blending.

### 10.4 Pitfall 4: Incorrect POPE Treatment

**Error:** Allocating all JV Group Top-Up Tax to the main UPE when the JV is a POPE.

**Correct approach:** If the JV is a POPE (<80% owned by main UPE), the JV itself pays Top-Up Tax on its subsidiaries. Only Top-Up Tax on the JV entity is allocated to the main UPE.

### 10.5 Pitfall 5: Double-Counting with QDMTT

**Error:** Reporting IIR liability without offsetting QDMTT paid by JV entities.

**Correct approach:** QDMTT has priority. Credit QDMTT paid against IIR liability.

## 11. Joint Venture Assessment Checklist

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

   If ETR ≥ 15%: No Top-Up Tax. Move to next jurisdiction.

□ SBIE Calculation:
   □ Payroll carve-out (9.8%):                   €__________________
   □ Asset carve-out (7.8%):                     €__________________
   □ Total SBIE:                                 €__________________

□ Excess Profit:                                 €__________________
□ Top-Up Tax %:                                  __________________%
□ JV Jurisdictional Top-Up Tax:                  €__________________

(Repeat for each JV Group jurisdiction)

═══════════════════════════════════════════════════════════════════════
SECTION D: TOP-UP TAX ALLOCATION
═══════════════════════════════════════════════════════════════════════

□ Total JV Group Top-Up Tax:                     €__________________

□ Is JV a POPE (<80% owned by main UPE)?         YES / NO

   If NO: All Top-Up Tax allocated to investors

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

□ JV Group Total Top-Up Tax:                     €__________________
□ UPE's Allocated Share:                         €__________________
□ QDMTT Offset:                                 (€__________________)
□ **Net IIR Liability for UPE:**                 €__________________

□ Documentation complete?                        YES / NO
```

## Concluding Discussion

Joint ventures represent one of the more complex areas of GloBE compliance, combining the challenges of non-consolidated entities, shared ownership, and multi-party coordination. The Article 6.4 rules bring JVs into scope through the "separate MNE Group" mechanism, but this creates significant practical hurdles. Each JV investor must independently gather the data needed to compute the JV Group's GloBE position, apply adjustments from the investor's own perspective, and determine its allocable share of any Top-Up Tax. Where multiple investors have GloBE obligations, coordination becomes essential—particularly for consistent treatment of elections and accounting policies within the JV.

The interaction between JV rules and other GloBE provisions adds further complexity. QDMTT priority means that JV jurisdictions with domestic minimum taxes may collect Top-Up Tax locally, offsetting investors' IIR obligations. The POPE rules shift responsibility for subsidiary-level Top-Up Tax to the JV itself when ownership falls below 80%. The distinction between JVs (≥50% ownership, equity-accounted) and MOCEs (≤30% ownership, consolidated) requires careful attention to both ownership thresholds and accounting treatment.

For groups with significant JV investments, building JV-specific GloBE processes is essential. This includes establishing data-sharing arrangements with JV partners, agreeing on methodologies for computing JV Group GloBE amounts, and developing systems to track the investor's allocable share of Top-Up Tax across potentially numerous JV investments. The compliance burden scales with the number and complexity of JV arrangements. Groups that historically treated JVs as "off-balance sheet" investments must now integrate them fully into their Pillar Two compliance infrastructure, recognising that significant JV ownership carries with it significant GloBE obligations.
