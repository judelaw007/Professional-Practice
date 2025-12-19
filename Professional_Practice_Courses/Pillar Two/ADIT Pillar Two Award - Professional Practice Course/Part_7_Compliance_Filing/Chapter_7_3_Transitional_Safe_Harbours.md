# Chapter 7.3: Transitional Safe Harbours

## Learning Objective

After completing this chapter, you will be able to identify which safe harbours are available during the Pillar Two transition period, apply the three tests for the Transitional CbCR Safe Harbour, understand the QDMTT Safe Harbour requirements, and determine which jurisdictions qualify for safe harbour relief in your MNE Group.

## Introduction

Safe harbours represent one of the most significant practical concessions within the Pillar Two framework. Recognising that the full GloBE calculation machinery demands substantial resources—and that many jurisdictions will clearly exceed the 15% minimum rate—the Inclusive Framework developed a series of safe harbour mechanisms that allow groups to bypass detailed calculations where the outcome is predictable. This proportionality principle is essential: without safe harbours, groups would invest heavily in calculating Top-Up Tax of zero for dozens of jurisdictions, with no benefit to tax administrations or the framework's objectives.

The transitional safe harbours, in particular, acknowledge that groups need time to build Pillar Two compliance capabilities. The Transitional CbCR Safe Harbour leverages existing Country-by-Country Reporting data—which groups already prepare under BEPS Action 13—to provide a simplified compliance pathway during the initial implementation years. If CbCR data demonstrates that a jurisdiction is clearly adequately taxed, why require the full GloBE calculation? The answer, from a policy perspective, is that you should not—and the safe harbour framework reflects this pragmatic approach.

Understanding safe harbour mechanics is not optional for Pillar Two practitioners. Strategic use of safe harbours can reduce compliance costs by 50% or more for some groups, while failing to apply an available safe harbour wastes resources on unnecessary calculations. Equally important is understanding the constraints—particularly the "once out, always out" rule that makes first-year elections irrevocable. Groups must analyse all jurisdictions comprehensively in Year 1 to preserve future flexibility.

## 1. Overview of Safe Harbours

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
│ │   → Top-Up Tax = zero                                            │
│ │                                                                   │
│ └── Simplified Calculations Safe Harbour                           │
│     → Permanent simplified methodology                              │
│     → Subject to 2028 review                                        │
└─────────────────────────────────────────────────────────────────────┘
```

## 2. Transitional CbCR Safe Harbour

### 2.1 Purpose

The Transitional CbCR Safe Harbour allows MNEs to exclude lower-risk jurisdictions from detailed GloBE calculations during the initial implementation years. If a jurisdiction qualifies, the **Top-Up Tax is deemed to be zero**.

### 2.2 Transition Period

| Criterion | Requirement |
|-----------|-------------|
| **Start** | Fiscal years beginning on or before **31 December 2026** |
| **End** | Fiscal years ending before **30 June 2028** |
| **Typical coverage** | FY 2024, 2025, 2026 (for Dec year-ends) |

### 2.3 The Three Tests

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

Pass ANY ONE test → Safe Harbour applies → Top-Up Tax = €0
```

The three-test structure provides multiple pathways to safe harbour qualification, recognising that different jurisdictions present different profiles. Small jurisdictions with limited operations qualify through De Minimis. High-tax jurisdictions qualify through Simplified ETR. High-substance jurisdictions with modest profits qualify through Routine Profits. This flexibility ensures that safe harbour relief reaches its intended beneficiaries—jurisdictions where Top-Up Tax is genuinely unlikely—rather than creating arbitrary barriers based on a single metric. The transition rates increasing from 15% to 17% over the safe harbour period reflect the Inclusive Framework's intent to gradually tighten eligibility as groups build full calculation capabilities.

## 3. Test 1: De Minimis Test

### 3.1 Requirements

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

## 4. Test 2: Simplified ETR Test

### 3.1 Requirements

Calculate a Simplified ETR and compare to the Transition Rate:

```
Simplified ETR = Simplified Covered Taxes ÷ CbCR Profit (Loss)

If Simplified ETR ≥ Transition Rate → Test passed
```

### 4.2 Transition Rates

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

## 5. Test 3: Routine Profits Test

### 3.1 Requirements

The jurisdiction's CbCR Profit must be **equal to or less than** the Substance-Based Income Exclusion (SBIE):

```
If CbCR Profit ≤ SBIE → Test passed
```

### SBIE Calculation

Full SBIE calculation using Pillar Two transition rates:

| Year | Payroll Rate | Asset Rate |
|------|--------------|------------|
| 2024 | 10.0% | 8.0% |
| 2025 | 9.8% | 7.8% |
| 2026 | 9.6% | 7.6% |

### Example: Singapore

| Item | Amount (€) |
|------|------------|
| CbCR Profit | €1,500,000 |
| Eligible Payroll | €8,000,000 |
| Tangible Assets (NBV) | €12,000,000 |

**SBIE Calculation (FY 2025):**

```
Payroll carve-out: €8,000,000 × 9.8% = €784,000
Asset carve-out: €12,000,000 × 7.8% = €936,000
Total SBIE: €1,720,000

CbCR Profit (€1,500,000) ≤ SBIE (€1,720,000) → Test passed
```

### When Routine Profits Test Is Useful

- High-substance jurisdictions with moderate profits
- Manufacturing operations with significant assets
- Service centres with significant payroll

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

The "once out, always out" rule creates powerful incentives for comprehensive Year 1 analysis. A group that performs full GloBE calculations for a jurisdiction in 2024—perhaps because they were uncertain about safe harbour qualification—permanently forfeits safe harbour eligibility for that jurisdiction, even if subsequent years clearly qualify. This is not a policy accident but a deliberate design choice: the Inclusive Framework wants groups to invest in understanding safe harbour eligibility upfront rather than opportunistically switching between approaches. For borderline jurisdictions, the implication is clear—if there is any reasonable prospect of qualification, applying the safe harbour in Year 1 preserves optionality that cannot be recovered once lost.

## QDMTT Safe Harbour (Permanent)

### 2.1 Purpose

The QDMTT Safe Harbour sets the **Top-Up Tax to zero** for jurisdictions where a Qualified Domestic Minimum Top-Up Tax applies, eliminating the need for a second calculation under GloBE Rules.

### 3.1 Requirements

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
Step 2: Calculate GloBE Top-Up Tax → €520,000
Step 3: IIR Top-Up Tax = €520,000 - €500,000 = €20,000

With Safe Harbour:
Step 1: Calculate QDMTT under local rules → €500,000
Step 2: GloBE Top-Up Tax = €0 (Safe Harbour)
Step 3: IIR Top-Up Tax = €0

Result: No residual IIR liability; QDMTT covers everything
```

### Qualifying Jurisdictions

Jurisdictions with Qualified QDMTT that meets the three standards include:
- Ireland
- UK
- Most EU Member States implementing the Pillar Two Directive

The QDMTT Safe Harbour represents a fundamental shift in how Pillar Two interacts with domestic implementation. Without this safe harbour, groups would face a perverse situation: calculating QDMTT under domestic rules, then recalculating under pure GloBE Rules to check for any residual IIR liability. Minor computational differences—arising from accounting standard variations or timing adjustments—could produce IIR Top-Up Tax even where the QDMTT had already collected the economically intended minimum tax. The safe harbour eliminates this redundancy by treating a Qualified QDMTT as fully satisfying GloBE obligations. For groups with significant operations in QDMTT jurisdictions like Ireland or the UK, this dramatically simplifies compliance by allowing them to focus on the domestic QDMTT calculation without parallel GloBE work.

## 6. Transitional UTPR Safe Harbour

### 2.1 Purpose

Provides relief from UTPR Top-Up Tax in respect of the **UPE jurisdiction only** during the transition period.

### 3.1 Requirements

| Criterion | Requirement |
|-----------|-------------|
| **UPE jurisdiction** | Must have nominal corporate income tax rate **≥ 20%** |
| **Period** | FY beginning on or before **31 Dec 2025**, ending before **31 Dec 2026** |

### Effect

If the UPE jurisdiction has ≥20% nominal CIT rate, the UTPR Top-Up Tax amount attributable to that jurisdiction is reduced to **zero**.

### Example

```
UPE: US Corporation (21% CIT rate)
Period: FY 2025

Without UTPR Safe Harbour:
→ UTPR jurisdictions could collect Top-Up Tax on US operations
   if US has not implemented IIR

With UTPR Safe Harbour:
→ UTPR Top-Up Tax for US (UPE jurisdiction) = €0
→ Other low-taxed jurisdictions still subject to UTPR
```

### Rationale

Provides transition relief for UPE jurisdictions that have high tax rates but have not yet implemented Pillar Two (e.g., US).

The Transitional UTPR Safe Harbour addresses a specific political reality: the United States, home to many of the world's largest multinationals, has not implemented Pillar Two. Without this safe harbour, US-parented groups would face UTPR charges from implementing jurisdictions seeking to collect Top-Up Tax on undertaxed US income—even though the US has a 21% federal corporate rate clearly exceeding the 15% minimum. The 20% nominal rate threshold provides a bright-line test that shields high-tax UPE jurisdictions from UTPR exposure during the transition, giving the US and similarly situated countries time to implement their own measures. Once the transition period ends, this protection expires, and groups must rely on actual US tax rates meeting the 15% threshold.

## 7. Stratos Worked Example: Safe Harbour Analysis

### 7.1 Background

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
| Routine Profits | SBIE = (€1.2M × 9.8%) + (€0.85M × 7.8%) = €183,900; Profit €4M > €183,900 | ✗ |

**Singapore Result:** Safe Harbour does NOT apply → Full GloBE calculation required

#### Ireland

| Test | Calculation | Result |
|------|-------------|--------|
| De Minimis | Revenue €160M > €10M | ✗ |
| Simplified ETR | €1,850,000 ÷ €15,000,000 = 12.33% < 16% | ✗ |
| Routine Profits | SBIE = (€8.4M × 9.8%) + (€12M × 7.8%) = €1,759,200; Profit €15M > €1.76M | ✗ |

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
| Routine Profits | SBIE = (€200K × 9.8%) + (€50K × 7.8%) = €23,500; Profit €2M > €23.5K | ✗ |

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

## 8. Common Pitfalls

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

## 9. Safe Harbour Assessment Checklist

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

   If all YES: QDMTT Safe Harbour applies → IIR Top-Up Tax = €0

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

## Concluding Discussion

Safe harbours represent the Inclusive Framework's acknowledgment that proportionality matters in tax administration. A framework requiring full GloBE calculations for every jurisdiction—including those clearly above the minimum rate—would impose costs grossly disproportionate to any policy benefit. The transitional safe harbours, in particular, provide essential breathing room during initial implementation, allowing groups to build capabilities progressively rather than requiring full sophistication from Day 1.

For practitioners, safe harbour analysis should be among the first steps in any Pillar Two compliance engagement. The Stratos example demonstrates typical outcomes: four of seven jurisdictions qualify for transitional safe harbour relief, Ireland qualifies for QDMTT Safe Harbour, and only two jurisdictions require full GloBE calculations. This 60% reduction in detailed calculation work translates directly to reduced compliance costs—but only if the analysis is performed correctly and elections are properly documented.

The strategic implications of the "once out, always out" rule deserve final emphasis. Groups must treat Year 1 safe harbour analysis with the same seriousness as substantive tax planning. A jurisdiction excluded from safe harbour treatment in 2024 cannot recover eligibility in subsequent years, even if circumstances change dramatically. This creates asymmetric risk: applying a safe harbour to a marginally qualifying jurisdiction preserves optionality, while foregoing a safe harbour forecloses it permanently. Conservative compliance strategies favour safe harbour election where qualification is reasonably arguable.

