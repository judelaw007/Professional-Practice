# Chapter 7.3: Transitional Safe Harbours

## Learning Objective

After completing this chapter, you will be able to identify which safe harbours are available during the Pillar Two transition period, apply the three tests for the Transitional CbCR Safe Harbour, understand the QDMTT Safe Harbour requirements, and determine which jurisdictions qualify for safe harbour relief in your MNE Group.

---

## Key References

**OECD Guidance:**
- Safe Harbours and Penalty Relief (December 2022)
- Administrative Guidance (July 2023, December 2023)

**Key Concepts:**
- Transitional CbCR Safe Harbour
- QDMTT Safe Harbour (Permanent)
- Transitional UTPR Safe Harbour
- Simplified Calculations Safe Harbour (Permanent)

---

## Overview of Safe Harbours

Safe harbours provide compliance relief by allowing MNEs to avoid detailed GloBE calculations in certain jurisdictions:

```
┌─────────────────────────────────────────────────────────────────────┐
│ PILLAR TWO SAFE HARBOURS                                            │
│                                                                     │
│ TRANSITIONAL (Time-limited):                                        │
│ ├── Transitional CbCR Safe Harbour                                 │
│ │   → FY beginning ≤ 31 Dec 2026, ending before 30 June 2028       │
│ │   → Based on CbCR data                                           │
│ │                                                                   │
│ └── Transitional UTPR Safe Harbour                                 │
│     → FY beginning ≤ 31 Dec 2025, ending before 31 Dec 2026        │
│     → UPE jurisdiction with ≥20% nominal CIT rate                  │
│                                                                     │
│ PERMANENT:                                                          │
│ ├── QDMTT Safe Harbour                                             │
│ │   → Qualified QDMTT jurisdictions                                │
│ │   → Top-up Tax = zero                                            │
│ │                                                                   │
│ └── Simplified Calculations Safe Harbour                           │
│     → Permanent simplified methodology                              │
│     → Subject to 2028 review                                        │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Transitional CbCR Safe Harbour

### Purpose

The Transitional CbCR Safe Harbour allows MNEs to exclude lower-risk jurisdictions from detailed GloBE calculations during the initial implementation years. If a jurisdiction qualifies, the **Top-up Tax is deemed to be zero**.

### Transition Period

| Criterion | Requirement |
|-----------|-------------|
| **Start** | Fiscal years beginning on or before **31 December 2026** |
| **End** | Fiscal years ending before **30 June 2028** |
| **Typical coverage** | FY 2024, 2025, 2026 (for Dec year-ends) |

### The Three Tests

A jurisdiction qualifies for the Transitional CbCR Safe Harbour if it meets **ANY ONE** of three tests:

```
TRANSITIONAL CbCR SAFE HARBOUR TESTS

Test 1: DE MINIMIS TEST
├── CbCR Revenue < €10 million, AND
└── CbCR Profit (Loss) < €1 million

Test 2: SIMPLIFIED ETR TEST
├── Simplified Covered Taxes ÷ CbCR Profit ≥ Transition Rate
└── Transition Rates:
    ├── 2023-2024: 15%
    ├── 2025: 16%
    └── 2026: 17%

Test 3: ROUTINE PROFITS TEST
└── CbCR Profit ≤ Substance-Based Income Exclusion (SBIE)

Pass ANY ONE test → Safe Harbour applies → Top-up Tax = €0
```

---

## Test 1: De Minimis Test

### Requirements

| Metric | Threshold |
|--------|-----------|
| **CbCR Revenue** | < €10 million |
| **CbCR Profit (Loss)** | < €1 million (including losses) |

### Data Source

Data comes from the **Qualified Country-by-Country Report** for the jurisdiction.

### Example: Luxembourg

| Metric | FY 2025 CbCR Data | Threshold | Meets? |
|--------|-------------------|-----------|--------|
| Revenue | €9,200,000 | < €10M | ✓ |
| Profit | €630,000 | < €1M | ✓ |

**Result:** Luxembourg passes the De Minimis Test → Safe Harbour applies.

### Important Notes

- Both thresholds must be met
- Losses count as meeting the profit threshold (loss < €1M)
- No averaging — tested annually

---

## Test 2: Simplified ETR Test

### Requirements

Calculate a Simplified ETR and compare to the Transition Rate:

```
Simplified ETR = Simplified Covered Taxes ÷ CbCR Profit (Loss)

If Simplified ETR ≥ Transition Rate → Test passed
```

### Transition Rates

| Fiscal Year Beginning | Transition Rate |
|----------------------|-----------------|
| 2023 | 15% |
| 2024 | 15% |
| 2025 | **16%** |
| 2026 | **17%** |

### Simplified Covered Taxes

Simplified Covered Taxes are calculated as:

```
Income Tax Expense (per Qualified Financial Statements)
LESS: Taxes that are not Covered Taxes
LESS: Uncertain Tax Position adjustments
─────────────────────────────────────────────────
= Simplified Covered Taxes
```

**Key simplification:** No GloBE adjustments required (no CFC tax allocation, no deferred tax recalculation).

### Example: Germany

| Item | Amount (€) |
|------|------------|
| CbCR Profit | 65,000,000 |
| Income Tax Expense (per QFS) | 15,000,000 |
| Less: Non-Covered Taxes | (200,000) |
| Less: UTP adjustments | (100,000) |
| **Simplified Covered Taxes** | **14,700,000** |

```
Simplified ETR = €14,700,000 ÷ €65,000,000 = 22.62%

Transition Rate (FY 2025): 16%

22.62% ≥ 16% → Test passed → Safe Harbour applies
```

### Loss Jurisdictions

If CbCR Profit is zero or negative, the Simplified ETR test cannot be applied. Consider:
- De Minimis Test (if revenue < €10M)
- Routine Profits Test

---

## Test 3: Routine Profits Test

### Requirements

The jurisdiction's CbCR Profit must be **equal to or less than** the Substance-Based Income Exclusion (SBIE):

```
If CbCR Profit ≤ SBIE → Test passed
```

### SBIE Calculation

Full SBIE calculation using Pillar Two transition rates:

| Year | Payroll Rate | Asset Rate |
|------|--------------|------------|
| 2024 | 9.8% | 7.8% |
| 2025 | 9.0% | 7.0% |
| 2026 | 8.2% | 6.2% |

### Example: Singapore

| Item | Amount (€) |
|------|------------|
| CbCR Profit | €1,500,000 |
| Eligible Payroll | €8,000,000 |
| Tangible Assets (NBV) | €12,000,000 |

**SBIE Calculation (FY 2025):**

```
Payroll carve-out: €8,000,000 × 9.0% = €720,000
Asset carve-out: €12,000,000 × 7.0% = €840,000
Total SBIE: €1,560,000

CbCR Profit (€1,500,000) ≤ SBIE (€1,560,000) → Test passed
```

### When Routine Profits Test Is Useful

- High-substance jurisdictions with moderate profits
- Manufacturing operations with significant assets
- Service centres with significant payroll

---

## "Once Out, Always Out" Rule

### Critical Rule

If an MNE Group **does not apply** the Transitional CbCR Safe Harbour for a jurisdiction in a fiscal year when the GloBE Rules apply, it **cannot qualify** for the safe harbour in that jurisdiction in any subsequent year.

```
"ONCE OUT, ALWAYS OUT" EXAMPLE

FY 2024: Germany qualifies for Safe Harbour
         MNE elects to apply Safe Harbour → ✓ Can continue in future

FY 2024: Singapore qualifies for Safe Harbour
         MNE does NOT apply Safe Harbour (full GloBE calculation done)
         → Singapore is OUT for all future years

FY 2025: Singapore cannot use Safe Harbour (even if it would qualify)
         Full GloBE calculation required
```

### Implications

- **Evaluate all jurisdictions in Year 1** — don't miss the opportunity
- **Document Safe Harbour elections** for compliance records
- **Consider future years** — if a jurisdiction is borderline, applying Safe Harbour in Year 1 preserves the option

---

## QDMTT Safe Harbour (Permanent)

### Purpose

The QDMTT Safe Harbour sets the **Top-up Tax to zero** for jurisdictions where a Qualified Domestic Minimum Top-up Tax applies, eliminating the need for a second calculation under GloBE Rules.

### Requirements

For a QDMTT to qualify for the Safe Harbour, it must meet **three standards**:

| Standard | Description |
|----------|-------------|
| **Accounting Standard** | QDMTT computed using same accounting standard as GloBE (or with acceptable adjustments) |
| **Consistency Standard** | QDMTT rules consistent with GloBE Model Rules |
| **Administration Standard** | Jurisdiction applies QDMTT in consistent manner |

### Effect

```
QDMTT SAFE HARBOUR EFFECT

Without Safe Harbour:
Step 1: Calculate QDMTT under local rules → €500,000
Step 2: Calculate GloBE Top-up Tax → €520,000
Step 3: IIR Top-up Tax = €520,000 - €500,000 = €20,000

With Safe Harbour:
Step 1: Calculate QDMTT under local rules → €500,000
Step 2: GloBE Top-up Tax = €0 (Safe Harbour)
Step 3: IIR Top-up Tax = €0

Result: No residual IIR liability; QDMTT covers everything
```

### Qualifying Jurisdictions

Jurisdictions with Qualified QDMTT that meets the three standards include:
- Ireland
- UK
- Most EU Member States implementing the Pillar Two Directive

---

## Transitional UTPR Safe Harbour

### Purpose

Provides relief from UTPR Top-up Tax in respect of the **UPE jurisdiction only** during the transition period.

### Requirements

| Criterion | Requirement |
|-----------|-------------|
| **UPE jurisdiction** | Must have nominal corporate income tax rate **≥ 20%** |
| **Period** | FY beginning on or before **31 Dec 2025**, ending before **31 Dec 2026** |

### Effect

If the UPE jurisdiction has ≥20% nominal CIT rate, the UTPR Top-up Tax amount attributable to that jurisdiction is reduced to **zero**.

### Example

```
UPE: US Corporation (21% CIT rate)
Period: FY 2025

Without UTPR Safe Harbour:
→ UTPR jurisdictions could collect Top-up Tax on US operations
   if US has not implemented IIR

With UTPR Safe Harbour:
→ UTPR Top-up Tax for US (UPE jurisdiction) = €0
→ Other low-taxed jurisdictions still subject to UTPR
```

### Rationale

Provides transition relief for UPE jurisdictions that have high tax rates but have not yet implemented Pillar Two (e.g., US).

---

## Stratos Worked Example: Safe Harbour Analysis

### Background

Stratos Holdings plc analyses Safe Harbour eligibility for FY 2025 (year ending 31 December 2025).

### Jurisdictional Data

| Jurisdiction | CbCR Revenue (€) | CbCR Profit (€) | Income Tax Expense (€) | Payroll (€) | Assets (€) |
|--------------|------------------|-----------------|------------------------|-------------|------------|
| UK | 85,000,000 | 8,500,000 | 2,200,000 | 4,200,000 | 2,800,000 |
| Germany | 520,000,000 | 53,880,000 | 12,800,000 | 12,500,000 | 18,000,000 |
| Singapore | 42,000,000 | 4,000,000 | 420,000 | 1,200,000 | 850,000 |
| Ireland | 160,000,000 | 15,000,000 | 1,850,000 | 8,400,000 | 12,000,000 |
| Luxembourg | 9,200,000 | 630,000 | 60,000 | 320,000 | 180,000 |
| USA | 140,000,000 | 12,300,000 | 2,000,000 | 8,000,000 | 3,000,000 |
| Cayman | 25,000,000 | 2,016,000 | 25,000 | 200,000 | 50,000 |

### Test Application

**Transition Rate for FY 2025: 16%**

#### UK

| Test | Calculation | Result |
|------|-------------|--------|
| De Minimis | Revenue €85M > €10M | ✗ |
| Simplified ETR | €2,200,000 ÷ €8,500,000 = 25.88% ≥ 16% | **✓ Pass** |
| Routine Profits | Not needed | — |

**UK Result:** Safe Harbour applies (Simplified ETR Test)

#### Germany

| Test | Calculation | Result |
|------|-------------|--------|
| De Minimis | Revenue €520M > €10M | ✗ |
| Simplified ETR | €12,800,000 ÷ €53,880,000 = 23.75% ≥ 16% | **✓ Pass** |
| Routine Profits | Not needed | — |

**Germany Result:** Safe Harbour applies (Simplified ETR Test)

#### Singapore

| Test | Calculation | Result |
|------|-------------|--------|
| De Minimis | Revenue €42M > €10M | ✗ |
| Simplified ETR | €420,000 ÷ €4,000,000 = 10.50% < 16% | ✗ |
| Routine Profits | SBIE = (€1.2M × 9%) + (€0.85M × 7%) = €167,500; Profit €4M > €167,500 | ✗ |

**Singapore Result:** Safe Harbour does NOT apply → Full GloBE calculation required

#### Ireland

| Test | Calculation | Result |
|------|-------------|--------|
| De Minimis | Revenue €160M > €10M | ✗ |
| Simplified ETR | €1,850,000 ÷ €15,000,000 = 12.33% < 16% | ✗ |
| Routine Profits | SBIE = (€8.4M × 9%) + (€12M × 7%) = €1,596,000; Profit €15M > €1.6M | ✗ |

**Ireland Result:** Safe Harbour does NOT apply

**However:** Ireland has QDMTT → **QDMTT Safe Harbour** applies instead

#### Luxembourg

| Test | Calculation | Result |
|------|-------------|--------|
| De Minimis | Revenue €9.2M < €10M; Profit €630K < €1M | **✓ Pass** |
| Simplified ETR | Not needed | — |
| Routine Profits | Not needed | — |

**Luxembourg Result:** Safe Harbour applies (De Minimis Test)

#### USA

| Test | Calculation | Result |
|------|-------------|--------|
| De Minimis | Revenue €140M > €10M | ✗ |
| Simplified ETR | €2,000,000 ÷ €12,300,000 = 16.26% ≥ 16% | **✓ Pass** |
| Routine Profits | Not needed | — |

**USA Result:** Safe Harbour applies (Simplified ETR Test)

#### Cayman

| Test | Calculation | Result |
|------|-------------|--------|
| De Minimis | Revenue €25M > €10M | ✗ |
| Simplified ETR | €25,000 ÷ €2,016,000 = 1.24% < 16% | ✗ |
| Routine Profits | SBIE = (€200K × 9%) + (€50K × 7%) = €21,500; Profit €2M > €21.5K | ✗ |

**Cayman Result:** Safe Harbour does NOT apply → Full GloBE calculation required

### Summary: Stratos Safe Harbour Status FY 2025

| Jurisdiction | Safe Harbour | Basis | Full GloBE Calc? |
|--------------|--------------|-------|------------------|
| UK | **Yes** | Simplified ETR (25.88%) | No |
| Germany | **Yes** | Simplified ETR (23.75%) | No |
| Singapore | **No** | All tests failed | **Yes** |
| Ireland | **QDMTT SH** | QDMTT Safe Harbour | QDMTT only |
| Luxembourg | **Yes** | De Minimis | No |
| USA | **Yes** | Simplified ETR (16.26%) | No |
| Cayman | **No** | All tests failed | **Yes** |

### Compliance Impact

| Scenario | Jurisdictions Requiring Full GloBE Calc |
|----------|----------------------------------------|
| Without Safe Harbours | 7 jurisdictions |
| With Safe Harbours | **2 jurisdictions** (Singapore, Cayman) + QDMTT (Ireland) |

**Result:** Safe Harbours reduce detailed GloBE calculations by ~60%.

---

## Common Pitfalls

### Pitfall 1: Missing the "Once Out, Always Out" Rule

**Error:** Not applying Safe Harbour in Year 1 for a qualifying jurisdiction, then trying to apply it in Year 2.

**Consequence:** Jurisdiction permanently excluded from Safe Harbour.

**Solution:** Analyse all jurisdictions in the first year and elect Safe Harbour where beneficial.

### Pitfall 2: Using Wrong Transition Rate

**Error:** Using 15% rate for FY 2025 (should be 16%).

**Consequence:** Incorrect Safe Harbour determination.

**Solution:** Verify Transition Rate based on fiscal year **start** date.

### Pitfall 3: Confusing CbCR Data with GloBE Data

**Error:** Using GloBE-adjusted income for Safe Harbour tests.

**Consequence:** Incorrect test results.

**Solution:** Safe Harbour tests use **CbCR data** and **Qualified Financial Statement** tax expense — not GloBE-adjusted figures.

### Pitfall 4: Ignoring QDMTT Safe Harbour

**Error:** Performing full GloBE calculation for jurisdiction with Qualified QDMTT.

**Consequence:** Unnecessary compliance burden.

**Solution:** Check QDMTT Safe Harbour eligibility first — if met, no residual IIR calculation needed.

### Pitfall 5: Not Documenting Safe Harbour Elections

**Error:** Failing to maintain records of Safe Harbour application.

**Consequence:** Audit risk; inability to demonstrate compliance.

**Solution:** Document Safe Harbour analysis annually; retain workings.

---

## Safe Harbour Assessment Checklist

```
TRANSITIONAL SAFE HARBOUR CHECKLIST
MNE Group: _________________________
Fiscal Year: _________________________

═══════════════════════════════════════════════════════════════════════
SECTION A: TRANSITION PERIOD CONFIRMATION
═══════════════════════════════════════════════════════════════════════

□ Fiscal year start date:                            ___________________
□ Fiscal year end date:                              ___________________

□ Is FY start on or before 31 Dec 2026?                   YES / NO
□ Is FY end before 30 June 2028?                          YES / NO

   If both YES: Transitional CbCR Safe Harbour available

□ Transition Rate for this FY:                       ___________________%
   (15% for 2023-24, 16% for 2025, 17% for 2026)

═══════════════════════════════════════════════════════════════════════
SECTION B: JURISDICTIONAL ANALYSIS
═══════════════════════════════════════════════════════════════════════

Jurisdiction: _________________________

□ Has Safe Harbour been applied in prior year?            YES / NO / N/A

   If NO (and GloBE Rules applied): "Once out, always out" —
   Safe Harbour NOT available

TEST 1: DE MINIMIS
□ CbCR Revenue:                                      €__________________
□ CbCR Profit (Loss):                                €__________________
□ Revenue < €10M AND Profit < €1M?                        YES / NO

   If YES: Safe Harbour applies (De Minimis)

TEST 2: SIMPLIFIED ETR
□ Income Tax Expense (per QFS):                      €__________________
□ Less: Non-Covered Taxes:                          (€__________________)
□ Less: UTP adjustments:                            (€__________________)
□ Simplified Covered Taxes:                          €__________________
□ CbCR Profit:                                       €__________________
□ Simplified ETR:                                    ___________________%
□ Simplified ETR ≥ Transition Rate?                       YES / NO

   If YES: Safe Harbour applies (Simplified ETR)

TEST 3: ROUTINE PROFITS
□ Eligible Payroll:                                  €__________________
□ Tangible Assets (NBV):                             €__________________
□ Payroll carve-out (× rate):                        €__________________
□ Asset carve-out (× rate):                          €__________________
□ Total SBIE:                                        €__________________
□ CbCR Profit ≤ SBIE?                                     YES / NO

   If YES: Safe Harbour applies (Routine Profits)

□ **CONCLUSION: Does jurisdiction qualify?**              YES / NO

(Repeat for each jurisdiction)

═══════════════════════════════════════════════════════════════════════
SECTION C: QDMTT SAFE HARBOUR
═══════════════════════════════════════════════════════════════════════

□ Does jurisdiction have Qualified QDMTT?                 YES / NO

   If YES:
   □ Meets Accounting Standard?                           YES / NO
   □ Meets Consistency Standard?                          YES / NO
   □ Meets Administration Standard?                       YES / NO

   If all YES: QDMTT Safe Harbour applies → IIR Top-up Tax = €0

═══════════════════════════════════════════════════════════════════════
SECTION D: SUMMARY
═══════════════════════════════════════════════════════════════════════

| Jurisdiction | CbCR SH? | Test Passed | QDMTT SH? | Full GloBE? |
|--------------|----------|-------------|-----------|-------------|
| | YES/NO | | YES/NO | YES/NO |
| | YES/NO | | YES/NO | YES/NO |
| | YES/NO | | YES/NO | YES/NO |

□ Documentation complete?                                 YES / NO
□ Elections filed/recorded?                               YES / NO
```

---

## Summary

Transitional Safe Harbours provide significant compliance relief:

| Safe Harbour | Availability | Benefit |
|--------------|--------------|---------|
| **Transitional CbCR** | FY start ≤ 31 Dec 2026, end < 30 June 2028 | Top-up Tax = €0 if any test passed |
| **QDMTT Safe Harbour** | Permanent (Qualified QDMTT jurisdictions) | IIR Top-up Tax = €0 |
| **Transitional UTPR** | FY start ≤ 31 Dec 2025, end < 31 Dec 2026 | UTPR for UPE jurisdiction = €0 (if CIT ≥20%) |

**Key rules:**
- Three tests for CbCR Safe Harbour: De Minimis, Simplified ETR, Routine Profits
- "Once out, always out" — apply in Year 1 or lose the option
- Transition Rates increase: 15% (2024) → 16% (2025) → 17% (2026)

---

## Integration with GIR Tools

Safe Harbour analysis should precede GIR-001 detailed calculations:

```
WORKFLOW

Step 1: Extract CbCR data for all jurisdictions
Step 2: Apply Safe Harbour tests (this chapter)
Step 3: For qualifying jurisdictions → Report Safe Harbour in GIR
Step 4: For non-qualifying jurisdictions → Run GIR-001 calculations
Step 5: Apply QDMTT Safe Harbour where applicable
Step 6: Consolidate into GIR filing
```

**GIR Reporting:** Safe Harbour elections must be disclosed in the GIR Summary section.

---

## Next Step

You have learned how to apply Transitional Safe Harbours to reduce compliance burden. Proceed to **Chapter 7.4: Penalties and Compliance** for guidance on penalty relief provisions and ongoing compliance obligations.
