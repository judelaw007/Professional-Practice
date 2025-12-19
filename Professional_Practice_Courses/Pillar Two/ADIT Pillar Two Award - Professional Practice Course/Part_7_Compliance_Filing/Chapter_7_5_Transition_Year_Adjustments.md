# Chapter 7.5: Transition Year Adjustments

## Learning Objective

After completing this chapter, you will be able to apply the opening balance rules for deferred tax attributes under Article 9.1, calculate SBIE using transition rates under Article 9.2, understand the DTL recapture mechanism and tracking methodologies, and identify key first-year compliance considerations.

## Introduction

Transition rules represent one of the most technically demanding aspects of Pillar Two compliance. When an MNE group first enters GloBE scope, the rules must reconcile two fundamentally different tax systems: the historical financial accounting and tax positions built up over years of operation, and the new GloBE framework that measures everything through its own methodology. Without careful transition provisions, this reconciliation would produce arbitrary and often punitive results—taxing income that has already been taxed, ignoring losses that economically reduce profits, or creating immediate recapture events from timing differences that will naturally reverse.

Article 9 addresses these challenges through interconnected mechanisms. Article 9.1 establishes how existing deferred tax assets and liabilities translate into GloBE terms, ensuring that prior-year losses can reduce future GloBE income and that historical timing differences receive appropriate recognition. Article 9.2 phases in the Substance-Based Income Exclusion rates over ten years, giving groups time to adjust to the permanent 5% thresholds while maintaining meaningful substance benefits during the transition. The DTL recapture rules, which track whether deferred tax liabilities actually reverse, begin their five-year monitoring from the Transition Year.

Understanding these transition mechanics is essential not merely for compliance but for strategic planning. The choices made in the Transition Year—including DTL tracking methodology, FIFO versus LIFO allocation, and identification of excluded DTAs—establish the foundation for ongoing GloBE calculations and cannot easily be revisited once made.

## 1. Overview: Why Transition Rules Matter

When an MNE Group first enters the scope of GloBE Rules, special transition rules prevent distortions:

```
┌─────────────────────────────────────────────────────────────────────┐
│ THE TRANSITION CHALLENGE                                            │
│                                                                     │
│ Without transition rules:                                           │
│ → Historical deferred tax attributes would be ignored               │
│ → Prior-year losses couldn't reduce GloBE income                   │
│ → Opening DTLs would create immediate recapture issues             │
│ → ETR calculations would be distorted                               │
│                                                                     │
│ THE SOLUTION (Article 9):                                           │
│ → Article 9.1: Bring in opening deferred tax balances              │
│ → Article 9.2: Phase-in SBIE rates over 10 years                   │
│ → Recapture rules start from Transition Year                        │
│ → Grace periods for certain pre-existing arrangements               │
└─────────────────────────────────────────────────────────────────────┘
```

The transition challenge reflects a fundamental tension in Pillar Two's design. On one hand, the system seeks to measure effective taxation with precision, which argues for ignoring pre-existing positions and starting fresh. On the other hand, economic reality demands recognition that MNE groups entered the GloBE era with legitimate deferred tax positions—losses incurred in prior years, timing differences that will reverse, and substance already deployed. Article 9 resolves this tension by bringing forward historical positions while preventing abuse: opening balances enter GloBE calculations, but with safeguards against manipulation. The 30 November 2021 cutoff date, in particular, targets arrangements created after Pillar Two became inevitable but before rules took effect.

## 2. Article 9.1: Opening Deferred Tax Adjustments

### 2.1 The Transition Year

The **Transition Year** is the first fiscal year that an MNE Group comes within the scope of the GloBE Rules.

| Scenario | Transition Year |
|----------|-----------------|
| MNE in scope from 1 Jan 2024 | FY 2024 |
| MNE crosses €750M threshold in 2025 | FY 2025 |
| New acquisition joins Group mid-2025 | FY 2025 (for acquired entities) |

### 2.2 Article 9.1.1: General Transition Rule

At the beginning of the Transition Year, MNE Groups may take into account existing deferred tax attributes:

```
OPENING BALANCE RULE

Deferred Tax Assets (DTAs):
→ Can be used to reduce Adjusted Covered Taxes
→ Must be reflected in financial accounts
→ Measured at LOWER of:
   • 15% (minimum rate), OR
   • Domestic tax rate

Deferred Tax Liabilities (DTLs):
→ Opening DTLs included in Adjusted Covered Taxes
→ Subject to 5-year recapture rule from Transition Year
→ Measured at LOWER of 15% or domestic rate
```

### 2.3 Measurement Rule: Lower of 15% or Domestic Rate

| Domestic Rate | Measurement Rate | Impact |
|---------------|------------------|--------|
| 25% (UK) | **15%** | DTA/DTL reduced to 15% equivalent |
| 21% (US) | **15%** | DTA/DTL reduced to 15% equivalent |
| 12.5% (Ireland) | **12.5%** | Full amount (rate already ≤15%) |
| 9% (Hungary) | **9%** | Full amount (rate already ≤15%) |

The "lower of 15% or domestic rate" measurement rule embodies a coherent policy rationale. Deferred tax assets reflect the expectation that temporary differences will generate future tax benefits, but under GloBE the relevant measure is whether those benefits contribute to achieving the 15% minimum rate. A German loss DTA measured at 30% overstates its GloBE value—when that loss is used, it will reduce German taxes at 30%, but the ETR calculation never credits more than 15% of any income. The measurement cap ensures opening balances enter GloBE at appropriate values. For low-tax jurisdictions like Ireland or Hungary, the domestic rate already falls below 15%, so no adjustment is required; the opening DTA will fully contribute to Covered Taxes when it reverses.

### 2.4 Example: Opening DTA Adjustment

**Scenario:** German entity has €1,000,000 DTA at 30% domestic rate (FY 2024 Transition Year).

```
Opening DTA (German books):        €1,000,000 at 30%
Implied timing difference:         €1,000,000 ÷ 30% = €3,333,333

GloBE measurement (lower of 30% or 15%):
GloBE DTA = €3,333,333 × 15% = €500,000

Result: Only €500,000 DTA usable for GloBE purposes
        (€500,000 reduction from accounting DTA)
```

### 2.5 Article 9.1.2: Excluded DTAs

Certain DTAs are **excluded** from the transition rule if they arise from:

| Exclusion | Description | Date Threshold |
|-----------|-------------|----------------|
| **Permanent differences** | DTAs from items included in taxable income but not GloBE Income | Any date |
| **Post-30 Nov 2021 transactions** | DTAs created from transactions after this date (anti-abuse) | After 30 Nov 2021 |
| **Government tax benefits** | Certain DTAs from government-granted tax attributes | After 30 Nov 2021 |

**Purpose:** Prevents MNEs from engineering DTAs to shelter future GloBE income.

The exclusions under Article 9.1.2 represent targeted anti-avoidance measures rather than general restrictions. The 30 November 2021 date corresponds to the period when Pillar Two's architecture became sufficiently clear that sophisticated taxpayers could engineer positions specifically to exploit transition relief. By excluding DTAs created after this date from certain transactions, the rules prevent groups from accelerating losses or arranging intercompany transactions designed to generate opening deferred tax assets for GloBE purposes. The exclusion for permanent differences addresses a different concern: items that affect taxable income but not GloBE Income should not generate deferred tax attributes that reduce GloBE liability, as this would create a mismatch between the income base and the tax recognised against it.

### 2.6 Article 9.1.3: Intragroup Asset Transfers

For assets transferred between Constituent Entities **after 30 November 2021** but **before the Transition Year**:

```
INTRAGROUP TRANSFER RULE

Transfer: SubCo A sells asset to SubCo B (Dec 2022)
Transition Year: FY 2024

Rule:
→ SubCo B's basis = SubCo A's carrying value at transfer
→ NOT the transfer price
→ Deferred tax calculated on original basis

Purpose: Prevents step-up basis from generating additional DTAs
```

### Grace Period (January 2025 Guidance)

The January 2025 Administrative Guidance provides a **Grace Period** for certain pre-existing tax benefits:

| Type | Grace Period | Cap |
|------|--------------|-----|
| Government-granted DTAs (pre-transition) | 2-3 years | Subject to limits |
| Certain tax incentive arrangements | 2-3 years | Subject to limits |

During the Grace Period, affected deferred tax expenses can be included in:
- Total Deferred Tax Adjustment Amount (Article 4.4), OR
- Simplified Covered Taxes (Transitional CbCR Safe Harbour)

## 3. Article 9.2: SBIE Transition Rates

### 10-Year Phase-In Period

The Substance-Based Income Exclusion (SBIE) uses **transition rates** that phase down over 10 years:

```
SBIE TRANSITION RATES

Year        Payroll Rate    Asset Rate    Notes
─────────────────────────────────────────────────────
2024        10.0%           8.0%          Initial rates
2025        9.8%            7.8%
2026        9.6%            7.6%
2027        9.4%            7.4%
2028        9.2%            7.2%
2029        9.0%            7.0%          First 6 years
─────────────────────────────────────────────────────
2030        8.2%            6.6%
2031        6.4%            5.6%          Last 4 years: steeper decline
2032        5.2%            5.2%
2033+       5.0%            5.0%          Permanent rates
```

The ten-year phase-in schedule reflects a deliberate policy choice about how quickly to reduce substance-based relief. During the initial transition period (2024-2029), rates decline gradually—0.2 percentage points per year—giving groups time to adjust their compliance processes and model the increasing Top-Up Tax exposure. The steeper decline from 2030 onwards accelerates convergence toward the permanent 5% rates. This structure acknowledges that MNE groups built operational models under the assumption that economic substance would continue to shelter profits from taxation. Abrupt elimination of this shelter would create significant disruption; phased reduction allows groups to adapt their structures, increase local taxation, or adjust profit allocation while maintaining predictability about future liabilities.

### Impact of Declining Rates

As SBIE rates decline, **Excess Profit increases**, leading to higher potential Top-Up Tax:

**Example: Singapore (€4M GloBE Income, Payroll €1.2M, Assets €850K, ETR 10%)**

| Year | Payroll Carve-out | Asset Carve-out | Total SBIE | Excess Profit | Top-Up Tax (5%) |
|------|-------------------|-----------------|------------|---------------|-----------------|
| 2024 | €120,000 (10.0%) | €68,000 (8.0%) | €188,000 | €3,812,000 | €190,600 |
| 2025 | €117,600 (9.8%) | €66,300 (7.8%) | €183,900 | €3,816,100 | €190,805 |
| 2033 | €60,000 (5.0%) | €42,500 (5.0%) | €102,500 | €3,897,500 | €194,875 |

**Trend:** Top-Up Tax increases by ~€4,000 over transition period due to declining SBIE.

### Planning Consideration

MNEs with significant substance should:
- Maximise SBIE claims during early transition years
- Track payroll and asset data rigorously
- Model future Top-Up Tax exposure as rates decline

## 4. DTL Recapture Rules (Article 4.4.4)

### The 5-Year Recapture Mechanism

DTLs included in Adjusted Covered Taxes are subject to **recapture** if they don't reverse within 5 years:

```
DTL RECAPTURE RULE

Year 1: Book DTL of €100,000 → Included in Adjusted Covered Taxes
        → ETR calculation benefits from this DTL

Year 2-5: DTL should reverse (timing difference unwinds)
          → If it reverses: No recapture
          → If it doesn't reverse: Recapture in Year 6

Year 6 (if not reversed):
→ Re-compute Year 1 ETR WITHOUT the €100,000 DTL
→ If ETR falls below 15%: Additional Top-Up Tax due
→ "Recapture amount" = Additional Top-Up Tax
```

The five-year recapture mechanism addresses a fundamental concern about deferred tax liabilities: they represent anticipated future tax payments, but the anticipation may prove wrong. When a group includes a DTL in Adjusted Covered Taxes, it receives current-year ETR credit for taxes that have not yet been paid. If those taxes are never paid—because the timing difference is indefinitely deferred or the liability otherwise evaporates—the original ETR credit was unjustified. The recapture mechanism corrects this by requiring re-computation of the original year's ETR as if the DTL had never existed. The five-year window provides a reasonable period for legitimate timing differences to reverse while preventing indefinite deferral from generating permanent ETR benefits. The exceptions for accelerated depreciation and fair value accounting recognise that certain DTLs will reverse, but over periods exceeding five years—penalising these through recapture would be economically inappropriate.

### Visual: DTL Recapture Timeline

```
DTL RECAPTURE TIMELINE

Year 1          Year 2      Year 3      Year 4      Year 5      Year 6
│               │           │           │           │           │
├── DTL booked  │           │           │           │           │
│   €100,000    │           │           │           │           │
│               │           │           │           │           │
│◄──────────── 5-year monitoring period ──────────────────────►│
│                                                               │
│   If DTL reverses during Years 2-5:                          │
│   → No recapture                                              │
│                                                               │
│   If DTL does NOT reverse by end of Year 5:                  │
│   → Recapture in Year 6                                       │
│   → Additional Top-Up Tax due                                 │
```

### Recapture Exception Accruals

Certain DTLs are **exempt** from the recapture rule:

| Exception | Description |
|-----------|-------------|
| **Accelerated depreciation** | DTLs on tangible assets (depreciation timing differences) |
| **Cost recovery allowances** | Similar to accelerated depreciation |
| **Fair value accounting** | DTLs on unrealised gains (mark-to-market) |
| **Certain pension liabilities** | As specified in guidance |

These DTLs are expected to reverse over extended periods and are excluded from recapture.

### 3.3 DTL Tracking Methodologies

The June 2024 Administrative Guidance provides three tracking approaches:

| Method | Description | Best For |
|--------|-------------|----------|
| **Item-by-item** | Track each DTL individually | Small number of DTLs |
| **GL account basis** | Track by general ledger account | Medium complexity |
| **Aggregate DTL category** | Track by DTL type category | Large volume of DTLs |

### FIFO vs LIFO Methodology

For DTL reversals, MNEs may use:

| Method | Assumption | Effect |
|--------|------------|--------|
| **FIFO** | Reversals relate to oldest accruals | Earlier recapture trigger |
| **LIFO** | Reversals relate to newest accruals | Later recapture trigger |

**Choice depends on:** DTL characteristics and administrative preference.

The tracking methodology and FIFO/LIFO election represent important administrative decisions with long-term consequences. Item-by-item tracking offers precision but becomes unwieldy for groups with numerous timing differences; aggregate tracking by category sacrifices some accuracy but provides practical manageability. The FIFO versus LIFO choice affects when the five-year clock runs on particular DTL accruals. LIFO, by attributing reversals to the newest accruals first, preserves older accruals on the books longer—potentially deferring recapture triggers but also extending the period over which those accruals must be monitored. Groups should select methodologies based on their DTL profiles, system capabilities, and risk tolerance regarding recapture timing, then apply these choices consistently across fiscal years.

## 5. Stratos Worked Example: Transition Year Adjustments

### 5.1 Background

Stratos Holdings plc enters GloBE scope in FY 2024 (Transition Year). Analyse transition adjustments for Irish operations.

### Opening Deferred Tax Position (SG Ireland Ltd)

| Item | Amount (€) | Tax Rate | DTA/DTL |
|------|------------|----------|---------|
| Tax losses carried forward | 2,000,000 | 12.5% | DTA €250,000 |
| Accelerated depreciation | (500,000) | 12.5% | DTL €62,500 |
| Provisions (timing) | 300,000 | 12.5% | DTA €37,500 |
| **Net DTA** | | | **€225,000** |

### Step 1: Apply Article 9.1.1 Measurement Rule

Irish domestic rate (12.5%) is **below** 15%, so full amounts are used:

| Item | Accounting Amount | GloBE Amount | Adjustment |
|------|-------------------|--------------|------------|
| Loss DTA | €250,000 | €250,000 | None (12.5% < 15%) |
| Depreciation DTL | €62,500 | €62,500 | None |
| Provisions DTA | €37,500 | €37,500 | None |
| **Net** | **€225,000** | **€225,000** | None |

**Result:** Full opening deferred tax balances carried into GloBE.

### Step 2: Check Article 9.1.2 Exclusions

| DTA | Created | Post-30 Nov 2021? | Excluded? |
|-----|---------|-------------------|-----------|
| Loss DTA | FY 2019-2022 | Partially | Check each year |
| Provisions DTA | Ongoing | Mixed | Review |

**Assumption:** All DTAs arose from normal business operations, not excluded arrangements.

### Step 3: SBIE Calculation Using Transition Rates (FY 2025)

| Component | Amount (€) | Rate (2025) | Carve-out (€) |
|-----------|------------|-------------|---------------|
| Payroll | 8,400,000 | 9.8% | 823,200 |
| Tangible Assets | 12,000,000 | 7.8% | 936,000 |
| **Total SBIE** | | | **1,759,200** |

### Step 4: DTL Recapture Setup

Opening DTL (accelerated depreciation): €62,500

| Year | DTL Booked | Reversal | Cumulative |
|------|------------|----------|------------|
| 2024 (Transition) | €62,500 | — | €62,500 |
| 2025 | — | €12,500 | €50,000 |
| 2026 | — | €12,500 | €37,500 |
| 2027 | — | €12,500 | €25,000 |
| 2028 | — | €12,500 | €12,500 |
| 2029 | — | €12,500 | €0 |

**Result:** DTL fully reverses within 5 years → No recapture.

### Step 5: Compare with Higher-Rate Jurisdiction (Germany)

**SG Germany GmbH Opening Position:**

| Item | Amount (€) | Tax Rate | Accounting DTA |
|------|------------|----------|----------------|
| Tax losses carried forward | 5,000,000 | 30% | DTA €1,500,000 |

**GloBE Adjustment:**

```
Accounting DTA: €1,500,000 at 30%
Implied timing difference: €1,500,000 ÷ 30% = €5,000,000

GloBE measurement (lower of 30% or 15%):
GloBE DTA = €5,000,000 × 15% = €750,000

Reduction: €1,500,000 - €750,000 = €750,000 (50% reduction)
```

**Impact:** German loss DTA is halved for GloBE purposes due to rate cap.

## 6. First-Year Compliance Considerations

### Transition Year Checklist

```
TRANSITION YEAR CHECKLIST
MNE Group: _________________________
Transition Year: _________________________

═══════════════════════════════════════════════════════════════════════
SECTION A: OPENING DEFERRED TAX BALANCES
═══════════════════════════════════════════════════════════════════════

For each jurisdiction:

Jurisdiction: _________________________

□ Identify all opening DTAs and DTLs:
   □ Loss carryforwards:                           €__________________
   □ Depreciation timing differences:              €__________________
   □ Provisions timing differences:                €__________________
   □ Other DTAs:                                   €__________________
   □ Other DTLs:                                  (€__________________)
   □ **Net DTA / (DTL):**                          €__________________

□ Apply measurement rule (lower of 15% or domestic rate):
   □ Domestic tax rate:                            ___________________%
   □ Measurement rate (lower of above or 15%):     ___________________%
   □ GloBE-adjusted DTA/DTL:                       €__________________

□ Check Article 9.1.2 exclusions:
   □ Any DTAs from post-30 Nov 2021 transactions?       YES / NO
   □ Any DTAs from government tax benefits?             YES / NO
   □ Excluded amount:                              €__________________

□ **Net GloBE opening deferred tax:**              €__________________

(Repeat for each jurisdiction)

═══════════════════════════════════════════════════════════════════════
SECTION B: SBIE TRANSITION RATES
═══════════════════════════════════════════════════════════════════════

□ Transition Year: _________________________

□ Applicable rates:
   □ Payroll carve-out rate:                       ___________________%
   □ Asset carve-out rate:                         ___________________%

□ SBIE calculations prepared for all jurisdictions?     YES / NO

═══════════════════════════════════════════════════════════════════════
SECTION C: DTL RECAPTURE TRACKING
═══════════════════════════════════════════════════════════════════════

□ DTL tracking methodology selected:
   □ Item-by-item
   □ GL account basis
   □ Aggregate DTL category

□ FIFO or LIFO methodology selected:
   □ FIFO
   □ LIFO

□ Opening DTLs documented and tracking established?     YES / NO

□ Recapture exception accruals identified:
   □ Accelerated depreciation DTLs:                €__________________
   □ Fair value DTLs:                              €__________________
   □ Other exempt DTLs:                            €__________________

═══════════════════════════════════════════════════════════════════════
SECTION D: DOCUMENTATION
═══════════════════════════════════════════════════════════════════════

□ Opening balance reconciliation prepared?              YES / NO
□ Article 9.1.2 exclusion analysis documented?          YES / NO
□ DTL tracking system implemented?                      YES / NO
□ SBIE data collection process established?             YES / NO
```

## 7. Common Pitfalls

### Pitfall 1: Ignoring the 15% Measurement Cap

**Error:** Using full accounting DTAs at domestic rates above 15%.

**Consequence:** Overstated DTAs for GloBE purposes.

**Correct approach:** Apply the lower of 15% or domestic rate to all opening deferred tax balances.

### Pitfall 2: Missing Article 9.1.2 Exclusions

**Error:** Including DTAs from post-30 November 2021 transactions.

**Consequence:** Invalid DTAs inflate Adjusted Covered Taxes.

**Correct approach:** Review DTA creation dates; exclude those from specified post-2021 transactions.

### Pitfall 3: Forgetting DTL Tracking from Day One

**Error:** Not establishing DTL tracking in the Transition Year.

**Consequence:** Unable to demonstrate reversals; unexpected recapture.

**Correct approach:** Implement DTL tracking system from the Transition Year. Select methodology (FIFO/LIFO) and document consistently.

### Pitfall 4: Using Wrong SBIE Rates

**Error:** Using permanent 5% rates instead of transition rates.

**Consequence:** Understated SBIE; overstated Top-Up Tax.

**Correct approach:** Apply transition rates based on fiscal year (9.8%/7.8% for 2025, etc.).

### Pitfall 5: Overlooking Grace Period Benefits

**Error:** Not claiming Grace Period relief for qualifying pre-existing arrangements.

**Consequence:** Missed opportunity to include certain deferred tax expenses.

**Correct approach:** Review January 2025 guidance; identify qualifying arrangements and apply Grace Period rules.

## Concluding Discussion

Transition year adjustments establish the foundation for all subsequent GloBE compliance. The decisions made when an MNE group first enters scope—how to measure opening deferred tax balances, which DTL tracking methodology to adopt, whether to apply FIFO or LIFO for reversal attribution—create frameworks that persist across future fiscal years. Changing these elections mid-stream is difficult or impossible, making careful initial analysis essential.

The economic significance of transition rules should not be underestimated. Opening DTAs can provide substantial ETR relief in the first years of GloBE application, potentially eliminating Top-Up Tax entirely for entities with accumulated losses or significant timing differences. The measurement cap at 15% prevents groups in high-tax jurisdictions from overstating these benefits, but for low-tax jurisdictions the full opening balance translates into GloBE. Similarly, the SBIE transition rates provide materially higher substance carve-outs during the initial decade—groups with significant payroll and tangible assets receive meaningfully more relief under 2024-2025 rates than they will under permanent 5% rates from 2033 onwards.

The DTL recapture mechanism creates ongoing monitoring obligations that extend well beyond the Transition Year. Groups must track DTL accruals and reversals for at least five years, maintaining documentation sufficient to demonstrate that timing differences actually reversed or qualify for recapture exceptions. This tracking requirement underscores the importance of robust systems and processes: failure to demonstrate reversal can trigger recapture and additional Top-Up Tax even for DTLs that genuinely reflected legitimate timing differences but whose documentation proves inadequate.
