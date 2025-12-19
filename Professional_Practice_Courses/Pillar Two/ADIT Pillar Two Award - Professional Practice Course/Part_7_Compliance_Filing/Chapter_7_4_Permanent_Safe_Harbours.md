# Chapter 7.4: Permanent Safe Harbours

## Learning Objective

After completing this chapter, you will be able to distinguish between transitional and permanent safe harbours, apply the QDMTT Safe Harbour to eliminate residual IIR liability, understand the framework for the Simplified Calculations Safe Harbour, and identify which jurisdictions qualify for permanent safe harbour relief.

## Introduction

While transitional safe harbours provide temporary relief during Pillar Two's initial years, permanent safe harbours reflect enduring design choices about where simplified compliance is appropriate. The distinction is fundamental: transitional mechanisms acknowledge that groups need time to build capabilities, whereas permanent mechanisms acknowledge that certain situations genuinely warrant streamlined treatment regardless of how mature compliance processes become.

The QDMTT Safe Harbour embodies a core principle of the Pillar Two architecture—where a jurisdiction has implemented a Qualified Domestic Minimum Top-Up Tax that meets specified standards, there should be no residual IIR liability to calculate. This prevents the perverse outcome of dual calculations producing marginally different results and triggering small IIR payments despite the QDMTT having already collected the intended minimum tax. The Simplified Calculations Safe Harbour, still evolving as of 2025, extends this logic to jurisdictions without QDMTT but where simplified data confirms adequate taxation.

Understanding permanent safe harbours is essential for long-term compliance strategy. Unlike transitional mechanisms that expire, these frameworks will shape Pillar Two administration indefinitely. Groups must monitor qualification status, understand the switch-off mechanism, and build permanent safe harbour assessment into their annual compliance cycles.

## 1. Overview: Transitional vs Permanent Safe Harbours

```
┌─────────────────────────────────────────────────────────────────────┐
│ SAFE HARBOUR COMPARISON                                             │
│                                                                     │
│ TRANSITIONAL SAFE HARBOURS:                                         │
│ ├── Transitional CbCR Safe Harbour                                 │
│ │   → Expires: FY ending 30 June 2028                              │
│ │   → Based on CbCR data                                           │
│ │   → Transition rates: 15% → 16% → 17%                            │
│ │                                                                   │
│ └── Transitional UTPR Safe Harbour                                 │
│     → Expires: FY ending 31 Dec 2026                               │
│     → UPE jurisdiction ≥20% CIT only                               │
│                                                                     │
│ PERMANENT SAFE HARBOURS:                                            │
│ ├── QDMTT Safe Harbour                                             │
│ │   → No expiry                                                    │
│ │   → Qualified QDMTT jurisdictions                                │
│ │   → IIR Top-Up Tax = €0                                          │
│ │                                                                   │
│ └── Simplified Calculations Safe Harbour                           │
│     → No expiry (subject to 2028 review)                           │
│     → Based on simplified calculations                              │
│     → ETR threshold: 15% (permanent)                               │
└─────────────────────────────────────────────────────────────────────┘
```

## 2. QDMTT Safe Harbour

### 2.1 Purpose

The QDMTT Safe Harbour **eliminates residual IIR liability** for jurisdictions that have implemented a Qualified Domestic Minimum Top-Up Tax. When the safe harbour applies, the Top-Up Tax under the GloBE Rules is deemed to be **zero**.

### 2.2 How It Works

```
WITHOUT QDMTT SAFE HARBOUR:

Step 1: Calculate QDMTT under local rules
        → Ireland QDMTT = €426,394

Step 2: Calculate GloBE Top-Up Tax
        → GloBE calculation = €432,000 (slightly different methodology)

Step 3: IIR Top-Up Tax = GloBE − QDMTT
        → €432,000 − €426,394 = €5,606 residual IIR

Result: MNE pays QDMTT locally + €5,606 IIR to UPE jurisdiction

WITH QDMTT SAFE HARBOUR:

Step 1: Calculate QDMTT under local rules
        → Ireland QDMTT = €426,394

Step 2: GloBE Top-Up Tax = €0 (Safe Harbour applies)

Step 3: IIR Top-Up Tax = €0

Result: MNE pays QDMTT locally only — no residual IIR
```

### 2.3 Three Qualification Standards

For a jurisdiction's QDMTT to qualify for the Safe Harbour, it must meet **three standards**:

| Standard | Description | Assessment |
|----------|-------------|------------|
| **Accounting Standard** | QDMTT computed using an Acceptable Financial Accounting Standard (same as or equivalent to GloBE) | Jurisdictional |
| **Consistency Standard** | QDMTT rules are consistent with the GloBE Model Rules and Commentary | Jurisdictional |
| **Administration Standard** | Jurisdiction applies QDMTT in a manner consistent with Administrative Guidance | Jurisdictional |

The three standards ensure that QDMTT calculations produce results materially equivalent to GloBE calculations. The Accounting Standard prevents jurisdictions from using local GAAP that might understate income or overstate deductions relative to the acceptable financial accounting standards recognised under Pillar Two. The Consistency Standard ensures the jurisdiction has not introduced favourable modifications—such as expanded SBIE or relaxed Covered Tax definitions—that would reduce the QDMTT below what GloBE would produce. The Administration Standard addresses enforcement: even well-drafted legislation fails to qualify if the tax authority applies it inconsistently or grants informal concessions that undermine the minimum tax objective. Together, these standards create confidence that QDMTT genuinely substitutes for GloBE calculation rather than offering a softer alternative.

### 2.4 Jurisdictional vs Entity-Level

The QDMTT Safe Harbour qualification is determined at the **jurisdictional level**, not entity-by-entity:

```
QDMTT SAFE HARBOUR ASSESSMENT

Ireland:
├── Accounting Standard: Uses IFRS → Meets standard
├── Consistency Standard: Irish rules align with GloBE → Meets standard
├── Administration Standard: Revenue applies consistently → Meets standard
└── Result: Ireland QDMTT qualifies for Safe Harbour

ALL Stratos Irish entities benefit:
├── SG Ireland Ltd → QDMTT Safe Harbour applies
└── Atlas Ireland Ltd (MOCE) → QDMTT Safe Harbour applies
```

### Qualifying Jurisdictions

Jurisdictions with Qualified QDMTT that generally meet the three standards include:

| Region | Jurisdictions |
|--------|---------------|
| **EU** | All EU Member States implementing Pillar Two Directive (Ireland, Germany, France, Netherlands, Luxembourg, etc.) |
| **UK** | UK Domestic Minimum Tax |
| **Other** | Various jurisdictions adopting GloBE-aligned QDMTT |

**Note:** The OECD maintains a central record of legislation with transitional qualified status. Check this register for current qualifying jurisdictions.

### Effect on Compliance

```
QDMTT SAFE HARBOUR COMPLIANCE IMPACT

When Safe Harbour applies:
□ Calculate QDMTT under local rules only
□ File local QDMTT return
□ Report Safe Harbour status in GIR
□ No separate GloBE calculation needed for that jurisdiction
□ No residual IIR liability

When Safe Harbour does NOT apply:
□ Calculate QDMTT under local rules
□ Calculate GloBE Top-Up Tax separately
□ Pay difference via IIR (if GloBE > QDMTT)
□ Dual calculation burden
```

The compliance benefit of the QDMTT Safe Harbour extends beyond eliminating small residual IIR payments. When the safe harbour applies, groups need not maintain parallel GloBE calculations for that jurisdiction at all—they can rely entirely on the QDMTT calculation for both local filing and GIR reporting purposes. This represents a substantial administrative simplification for groups with significant operations in QDMTT jurisdictions. The jurisdiction captures its domestic minimum tax, the group avoids dual calculation burdens, and the GIR can simply report the safe harbour claim without detailed ETR backup. The efficiency gains are particularly significant for EU Member States, where consistent implementation of the Pillar Two Directive means the QDMTT Safe Harbour will likely apply across the majority of European operations.

## 3. Simplified Calculations Safe Harbour

### 2.1 Purpose

The Simplified Calculations Safe Harbour is a **permanent** framework allowing MNEs to use simplified calculations instead of full GloBE computations for qualifying jurisdictions.

### Framework Status

As of 2025, the Simplified Calculations Safe Harbour framework has been agreed in principle, with detailed methodology subject to ongoing refinement and a **2028 review**.

### The Three Tests (Simplified)

Like the Transitional CbCR Safe Harbour, the Simplified Calculations Safe Harbour uses three tests, but with **simplified calculation methodologies**:

```
SIMPLIFIED CALCULATIONS SAFE HARBOUR TESTS

Test 1: SIMPLIFIED DE MINIMIS TEST
├── Simplified Revenue < €10 million, AND
└── Simplified Income < €1 million

Test 2: SIMPLIFIED ETR TEST
├── Simplified Covered Taxes ÷ Simplified Income ≥ 15%
└── Note: Permanent 15% rate (not transitional rates)

Test 3: SIMPLIFIED ROUTINE PROFITS TEST
└── Simplified Income ≤ SBIE

Pass ANY ONE test → Safe Harbour applies → Top-Up Tax = €0
```

### Simplified Calculations Defined

| Calculation | Description |
|-------------|-------------|
| **Simplified Income** | Alternative to GloBE Income, using financial accounting data with limited adjustments |
| **Simplified Revenue** | Alternative to GloBE Revenue, based on CbCR or financial statements |
| **Simplified Tax** | Alternative to Adjusted Covered Taxes, using financial statement tax expense with limited adjustments |

### Key Differences from Transitional CbCR Safe Harbour

| Aspect | Transitional CbCR | Simplified Calculations |
|--------|-------------------|------------------------|
| **Time limit** | Expires 30 June 2028 | **Permanent** |
| **ETR threshold** | 15% → 16% → 17% | **15%** (fixed) |
| **Data source** | CbCR Report | Financial statements with adjustments |
| **"Once out" rule** | Yes | TBD |
| **Methodology** | Fixed | Subject to 2028 review |

### 2028 Methodology Review

The Inclusive Framework has committed to reviewing the Simplified Calculations methodology **no later than 2028** to evaluate:
- Whether the integrity of the GloBE Rules is undermined
- Potential adjustments to simplified calculation definitions
- Ongoing suitability of the safe harbour approach

The commitment to a 2028 review reflects the inherent tension between simplification and precision. Simplified calculations are, by definition, approximations—they use readily available data and accept some deviation from theoretically correct GloBE results in exchange for compliance efficiency. The review will assess whether this trade-off remains appropriate as Pillar Two matures. If evidence emerges that simplified calculations systematically understate ETR or that the safe harbour is being exploited to shelter genuinely undertaxed income, the Inclusive Framework may tighten the methodology. Conversely, if the approach proves robust, the framework may be expanded. Groups should monitor developments closely, as changes to the Simplified Calculations methodology will directly affect compliance planning for jurisdictions without QDMTT.

## Interaction Between Safe Harbours

### Decision Tree

```
SAFE HARBOUR DECISION TREE

For each jurisdiction:
                                    │
                    ┌───────────────┴───────────────┐
                    │                               │
            Does jurisdiction             Does jurisdiction
            have Qualified QDMTT?         qualify for CbCR
                    │                     Safe Harbour?
                    │                               │
               ┌────┴────┐                    ┌────┴────┐
               │         │                    │         │
              YES        NO                  YES        NO
               │         │                    │         │
               ▼         │                    ▼         ▼
         QDMTT Safe      │              CbCR Safe    Full GloBE
         Harbour         │              Harbour      Calculation
         applies         │              applies      Required
               │         │                    │
               ▼         ▼                    ▼
         IIR = €0   Continue to          Top-Up Tax
                    next test            = €0
```

### Priority and Stacking

| Scenario | Safe Harbour Applied | Result |
|----------|---------------------|--------|
| QDMTT jurisdiction + CbCR qualifies | QDMTT Safe Harbour (primary) | IIR = €0; QDMTT paid locally |
| QDMTT jurisdiction + CbCR fails | QDMTT Safe Harbour | IIR = €0; QDMTT paid locally |
| No QDMTT + CbCR qualifies | CbCR Safe Harbour | Top-Up Tax = €0 |
| No QDMTT + CbCR fails | None | Full GloBE calculation |

The priority structure reflects a coherent policy logic. QDMTT Safe Harbour takes precedence because where a jurisdiction has implemented a qualified domestic minimum tax, that jurisdiction has effectively claimed the right to collect any shortfall from 15%—the IIR becomes irrelevant regardless of whether CbCR tests would also pass. For non-QDMTT jurisdictions, the CbCR Safe Harbour provides relief where simplified data confirms adequate taxation, preventing compliance burden for jurisdictions that clearly exceed the minimum rate. Only where both mechanisms fail—typically low-tax jurisdictions without QDMTT where profits exceed substance-based thresholds—must groups perform full GloBE calculations. This layered approach ensures compliance effort concentrates where genuine undertaxation risk exists.

## Stratos Worked Example: Permanent Safe Harbour Analysis

### 4.1 Background

Stratos Holdings plc analyses permanent safe harbour eligibility for FY 2025.

### QDMTT Status by Jurisdiction

| Jurisdiction | Has QDMTT? | Meets 3 Standards? | QDMTT Safe Harbour? |
|--------------|------------|-------------------|-------------------|
| UK | Yes | Yes | **Yes** |
| Germany | Yes | Yes | **Yes** |
| Ireland | Yes | Yes | **Yes** |
| Luxembourg | Yes | Yes | **Yes** |
| Singapore | No | N/A | No |
| USA | No | N/A | No |
| Cayman | No | N/A | No |

### Safe Harbour Strategy

| Jurisdiction | QDMTT SH? | CbCR SH? | Result |
|--------------|-----------|----------|--------|
| UK | **Yes** | (Not needed) | IIR = €0; UK DMT applies |
| Germany | **Yes** | (Not needed) | IIR = €0; German QDMTT applies |
| Ireland | **Yes** | (Not needed) | IIR = €0; Irish QDMTT applies |
| Luxembourg | **Yes** | (Yes - De Minimis) | IIR = €0; Lux QDMTT applies |
| Singapore | No | No (failed tests) | **Full GloBE calculation** |
| USA | No | Yes (Simplified ETR) | **Top-Up Tax = €0** |
| Cayman | No | No (failed tests) | **Full GloBE calculation** |

### Compliance Impact

| Jurisdiction | Safe Harbour | Full GloBE Calc? | Top-Up Tax Outcome |
|--------------|--------------|------------------|-------------------|
| UK | QDMTT | No | IIR = €0 |
| Germany | QDMTT | No | IIR = €0 |
| Ireland | QDMTT | No | IIR = €0 (QDMTT €426,394 local) |
| Luxembourg | QDMTT + CbCR | No | IIR = €0 |
| Singapore | None | **Yes** | €197,498 IIR |
| USA | CbCR | No | Top-Up Tax = €0 |
| Cayman | None | **Yes** | €280,480 IIR |

**Result:** Only 2 jurisdictions require full GloBE calculation (Singapore, Cayman).

### Ireland Deep Dive: QDMTT Safe Harbour

| Item | QDMTT Calculation | GloBE Calculation (if done) |
|------|-------------------|----------------------------|
| GloBE Income | €15,000,000 | €15,000,000 |
| Covered Taxes | €1,770,000 | €1,770,000 |
| ETR | 11.80% | 11.80% |
| SBIE | €1,675,200 | €1,675,200 |
| Excess Profit | €13,324,800 | €13,324,800 |
| Top-Up Tax | €426,394 | €426,394 |

**With QDMTT Safe Harbour:**
- Ireland collects €426,394 via QDMTT
- GloBE Top-Up Tax = €0 (Safe Harbour)
- IIR to UK = €0

**Without QDMTT Safe Harbour (hypothetical):**
- If GloBE calculation differed (e.g., €432,000 due to methodology differences)
- IIR to UK = €432,000 − €426,394 = €5,606 residual

**Safe Harbour benefit:** Eliminates €5,606 residual and avoids dual calculation.

## Central Record of Qualified Status

### OECD Central Register

The OECD maintains a **Central Record of Legislation with Transitional Qualified Status**, which identifies:
- Jurisdictions with Qualified QDMTT
- Jurisdictions with transitional qualified status
- Implementation dates and scope

### How to Use the Register

```
CHECKING QDMTT SAFE HARBOUR ELIGIBILITY

Step 1: Access OECD Central Record
        → www.oecd.org/tax/beps/

Step 2: Identify jurisdiction
        → Check if QDMTT is listed

Step 3: Verify standards met
        → Accounting Standard
        → Consistency Standard
        → Administration Standard

Step 4: Confirm effective dates
        → QDMTT must be in force for relevant fiscal year

Step 5: Apply Safe Harbour
        → Report in GIR
```

### Switch-Off Mechanism

The QDMTT Safe Harbour includes a **switch-off mechanism**:
- If a jurisdiction's QDMTT no longer meets the three standards
- The Safe Harbour is "switched off" for that jurisdiction
- MNEs must then perform full GloBE calculations

## 5. GIR Reporting for Safe Harbours

### Safe Harbour Disclosure

Even when safe harbours apply, the GIR must be filed with appropriate disclosures:

| Safe Harbour | GIR Disclosure Required |
|--------------|------------------------|
| **QDMTT Safe Harbour** | Identify jurisdiction; confirm QDMTT paid |
| **CbCR Safe Harbour** | Identify jurisdiction; identify test passed |
| **Simplified Calculations** | Identify jurisdiction; simplified calculation details |

### Reduced Reporting Burden

When Safe Harbours apply, certain GIR sections are **simplified**:

```
GIR REPORTING WITH SAFE HARBOURS

Jurisdiction with QDMTT Safe Harbour:
├── Report Safe Harbour claim: YES
├── ETR Computation section: Simplified (QDMTT data)
├── Top-Up Tax section: Top-Up Tax = €0
└── Full GloBE adjustments: NOT required

Jurisdiction with CbCR Safe Harbour:
├── Report Safe Harbour claim: YES
├── ETR Computation section: NOT required
├── Top-Up Tax section: Top-Up Tax = €0
└── Test passed: Identify which test (De Minimis / ETR / Routine)
```

## 6. Common Pitfalls

### Pitfall 1: Assuming All QDMTT Jurisdictions Qualify

**Error:** Assuming any jurisdiction with a domestic minimum tax qualifies for QDMTT Safe Harbour.

**Correct approach:** Verify the jurisdiction's QDMTT meets all three standards (Accounting, Consistency, Administration). Check the OECD Central Record.

### Pitfall 2: Confusing CbCR and QDMTT Safe Harbours

**Error:** Applying CbCR Safe Harbour to a QDMTT jurisdiction and missing the QDMTT benefit.

**Correct approach:** QDMTT Safe Harbour is the primary relief for QDMTT jurisdictions. CbCR Safe Harbour is for non-QDMTT jurisdictions.

### Pitfall 3: Ignoring the Switch-Off Mechanism

**Error:** Continuing to apply QDMTT Safe Harbour after a jurisdiction's QDMTT is disqualified.

**Correct approach:** Monitor OECD updates for any switch-off announcements. Adjust calculations accordingly.

### Pitfall 4: Omitting Safe Harbour Disclosure in GIR

**Error:** Not reporting Safe Harbour elections in the GIR.

**Correct approach:** Always disclose Safe Harbour claims in the GIR Summary section, even though detailed calculations are not required.

### Pitfall 5: Assuming No GIR Filing When Safe Harbours Apply

**Error:** Believing that Safe Harbour eligibility eliminates the GIR filing requirement.

**Correct approach:** GIR must still be filed. Safe Harbours reduce the content/complexity of the GIR, not the filing obligation itself.

## 7. Permanent Safe Harbour Checklist

```
PERMANENT SAFE HARBOUR CHECKLIST
MNE Group: _________________________
Fiscal Year: _________________________

═══════════════════════════════════════════════════════════════════════
SECTION A: QDMTT SAFE HARBOUR ASSESSMENT
═══════════════════════════════════════════════════════════════════════

Jurisdiction: _________________________

□ Does jurisdiction have QDMTT?                           YES / NO

   If NO: QDMTT Safe Harbour not available.
          Check CbCR / Simplified Calculations Safe Harbour.

□ Check OECD Central Record:
   □ Jurisdiction listed?                                 YES / NO
   □ Transitional qualified status?                       YES / NO
   □ Full qualified status?                               YES / NO

□ Three Standards Assessment:
   □ Accounting Standard met?                             YES / NO
   □ Consistency Standard met?                            YES / NO
   □ Administration Standard met?                         YES / NO

□ **QDMTT Safe Harbour applies?**                         YES / NO

   If YES:
   □ GloBE Top-Up Tax = €0
   □ IIR liability = €0
   □ QDMTT paid locally: €__________________
   □ Report in GIR: Safe Harbour claimed

(Repeat for each jurisdiction with QDMTT)

═══════════════════════════════════════════════════════════════════════
SECTION B: SIMPLIFIED CALCULATIONS SAFE HARBOUR (POST-TRANSITION)
═══════════════════════════════════════════════════════════════════════

Note: Framework subject to 2028 review. Apply transitional CbCR Safe
Harbour during transition period; monitor for finalised permanent rules.

Jurisdiction: _________________________

□ Does CbCR Safe Harbour apply (if within transition period)?  YES / NO

   If transition period ended:
   □ Apply Simplified De Minimis Test                     PASS / FAIL
   □ Apply Simplified ETR Test (15% threshold)            PASS / FAIL
   □ Apply Simplified Routine Profits Test                PASS / FAIL

□ **Simplified Calculations Safe Harbour applies?**       YES / NO

(Repeat for each non-QDMTT jurisdiction)

═══════════════════════════════════════════════════════════════════════
SECTION C: SUMMARY
═══════════════════════════════════════════════════════════════════════

| Jurisdiction | QDMTT SH? | CbCR/Simplified SH? | Full GloBE? |
|--------------|-----------|---------------------|-------------|
| | YES/NO | YES/NO | YES/NO |
| | YES/NO | YES/NO | YES/NO |
| | YES/NO | YES/NO | YES/NO |

□ Total jurisdictions with Safe Harbour relief:          __________
□ Total jurisdictions requiring full GloBE:              __________

□ GIR filing required?                                        YES
□ Safe Harbour disclosures prepared?                      YES / NO
```

## Concluding Discussion

Permanent safe harbours represent Pillar Two's acknowledgment that not every jurisdiction requires full GloBE calculation. The architecture embeds a hierarchy of trust: QDMTT jurisdictions receive the highest confidence because they have legislated and administered a qualified domestic minimum tax, while simplified calculations offer relief where readily available data confirms adequate taxation without domestic top-up mechanisms. This graduated approach ensures compliance effort flows to where undertaxation risk is genuine rather than theoretical.

The practical significance for MNE groups is substantial. Where QDMTT Safe Harbour applies—as it will across EU Member States, the UK, and other implementing jurisdictions—groups eliminate both residual IIR calculations and the risk of paying marginal top-up amounts driven by methodology differences rather than genuine tax shortfalls. The Simplified Calculations Safe Harbour extends similar relief to non-QDMTT jurisdictions meeting threshold tests. Together, these mechanisms concentrate full GloBE calculations on a minority of jurisdictions: typically low-tax locations without QDMTT where economic substance cannot shelter profits.

The ongoing refinement of these frameworks, particularly the 2028 review of Simplified Calculations methodology, underscores that Pillar Two remains a dynamic system. Groups building compliance infrastructure should design flexibility into their processes, anticipating that safe harbour thresholds, qualification standards, and switch-off mechanisms may evolve. Monitoring the OECD Central Record is not a one-time exercise but an annual compliance requirement, as changes to jurisdictional qualification status directly affect which calculations groups must perform and which they may forego.
