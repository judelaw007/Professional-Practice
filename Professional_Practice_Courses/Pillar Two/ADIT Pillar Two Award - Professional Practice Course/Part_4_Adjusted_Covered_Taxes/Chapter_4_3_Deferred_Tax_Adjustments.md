# Chapter 4.3: Deferred Tax Adjustments

## Learning Objective

This chapter provides the methodology for calculating the Total Deferred Tax Adjustment Amount (DTAA) that modifies the current tax expense to produce total Adjusted Covered Taxes. Deferred tax accounting creates timing differences between financial accounting and tax—the DTAA ensures GloBE captures the economic reality of when taxes will ultimately be paid.

## 1. The Deferred Tax Adjustment Framework

The GloBE approach to deferred taxes differs significantly from financial accounting. Three key principles govern:

1. **15% Rate Cap:** All DTAs and DTLs are valued at the lower of 15% or the applicable domestic rate
2. **Exclusions:** Several categories of deferred tax movements are ignored
3. **Recapture:** DTLs claimed in Covered Taxes must reverse within five years or be recaptured

**Formula:**
```
Total Deferred Tax Adjustment Amount (DTAA) =
    Deferred Tax Expense (from financial accounts)
  ± Adjustments for 15% rate cap
  − Excluded deferred tax items
  + DTL recapture adjustments (if applicable)
```

## 2. The 15% Rate Cap (Article 4.4.1)

### 2.1 The Rule

All deferred tax assets and liabilities must be valued at the **lower of:**
- The 15% minimum rate, OR
- The applicable domestic tax rate

### 2.2 Why This Matters

Without the cap, a high-tax jurisdiction could create excess deferred tax benefits that inflate Covered Taxes beyond what will actually be paid.

**Example:**
```
Jurisdiction with 25% tax rate:
  DTL in financial accounts:    €1,000,000 (at 25%)

For GloBE purposes:
  DTL recast to 15%:           €600,000 (€1M × 15/25)

Difference:                    €400,000 reduction in DTAA
```

### 2.3 Practical Application

**Step 1:** Extract deferred tax expense from financial accounts

**Step 2:** Identify the applicable domestic tax rate

**Step 3:** If domestic rate > 15%, recast deferred tax balances at 15%

**Step 4:** Calculate the adjusted deferred tax movement

### 2.4 Rate Cap Calculation Template

| Item | Accounts Rate | GloBE Rate | Accounts Value | GloBE Value | Adjustment |
|------|---------------|------------|----------------|-------------|------------|
| DTL on intangibles | 30% | 15% | €2,000,000 | €1,000,000 | −€1,000,000 |
| DTA on provisions | 25% | 15% | €500,000 | €300,000 | −€200,000 |
| DTA on losses | 20% | 15% | €800,000 | €600,000 | −€200,000 |

**Key point:** DTAs in low-tax jurisdictions (rate < 15%) can be **recast upward** to 15% if attributable to a GloBE Loss (Article 4.4.3).

## 3. GloBE Loss DTA Recasting (Article 4.4.3)

### 3.1 The Exception

While the general rule caps deferred tax at 15%, loss-related DTAs in low-tax jurisdictions can be increased to 15% if:
1. The DTA arose from a loss, AND
2. The loss would have been a GloBE Loss

### 3.2 Why This Exists

Without this provision, losses in zero-tax or low-tax jurisdictions would provide no GloBE benefit, creating an asymmetry with profits.

### 3.3 Example

```
Jurisdiction: Singapore (17% rate)
Entity: SG Singapore Pte Ltd

Year 1 (Loss):
  GloBE Loss: €5,000,000
  Accounting DTA: €5M × 17% = €850,000
  GloBE DTA: €5M × 17% = €850,000 (rate < 15%, no recast needed)

Jurisdiction: Cayman Islands (0% rate)
Entity: SG Cayman Ltd

Year 1 (Loss):
  GloBE Loss: €3,000,000
  Accounting DTA: €0 (no tax rate)
  GloBE DTA (recast): €3M × 15% = €450,000 ← Benefit created at 15%
```

## 4. Excluded Deferred Tax Items (Article 4.4.1(b)-(e))

Several categories of deferred tax movements are **excluded** from the DTAA to prevent distortions.

### 4.1 Exclusion 1: Deferred Tax on Excluded Income (Article 4.4.1(b))

Deferred tax relating to income excluded from GloBE Income is excluded from DTAA.

**Examples:**
- Deferred tax on excluded dividends
- Deferred tax on excluded equity gains
- Deferred tax on international shipping income

**Rationale:** If the income isn't in GloBE Income, the tax shouldn't be in Covered Taxes.

### 4.2 Exclusion 2: Valuation Allowances (Article 4.4.1(c))

Movements in deferred tax arising from valuation adjustments or recognition criteria are excluded.

**What this covers:**
- US GAAP valuation allowances on DTAs
- IFRS recognition adjustments (probability of future profits)
- Write-downs of DTAs due to uncertainty

**Rationale:** These are accounting judgments, not actual tax payments or deferrals.

**Example:**
```
Year 1: DTA of €1M recorded; no valuation allowance
Year 2: Entity reassesses; records €300,000 valuation allowance
        Deferred tax expense in P&L: €300,000

For GloBE:
  Exclude the €300,000 from DTAA
```

### 4.3 Exclusion 3: Rate Change Effects (Article 4.4.1(d))

Deferred tax expense arising from changes in domestic tax rates is excluded.

**What this covers:**
- Remeasurement of DTAs when rate decreases
- Remeasurement of DTLs when rate increases
- One-time charges/credits from enacted rate changes

**Rationale:** These reflect future tax rates, not current-year income taxation.

**Example:**
```
Country X announces rate reduction: 25% → 21%

Financial accounting impact:
  DTL revaluation: €2M × (25% − 21%) = €80,000 credit to P&L

For GloBE:
  Exclude the €80,000 from DTAA
```

### 4.4 Exclusion 4: Tax Credit Effects (Article 4.4.1(e))

Deferred tax arising from the generation and use of tax credits is excluded.

**What this covers:**
- Creation of deferred tax assets for unused credits
- Utilisation of credit-related DTAs
- Changes in credit carryforward balances

**Rationale:** Tax credits receive separate treatment (QRTC vs non-QRTC); deferred tax on credits would double-count.

**Important exception:** This exclusion does NOT apply in the Transition Year under Article 9.1—credit-related deferred tax is included in opening balances.

### 4.5 Exclusion 5: Uncertain Tax Positions (Article 4.4.1(b))

Deferred tax movements related to UTPs are excluded (consistent with current tax treatment).

### 4.6 Exclusion Summary Checklist

| Exclusion | Article | Exclude from DTAA? |
|-----------|---------|-------------------|
| DT on excluded dividends | 4.4.1(b) | Yes |
| DT on excluded equity gains | 4.4.1(b) | Yes |
| Valuation allowance movements | 4.4.1(c) | Yes |
| Rate change remeasurement | 4.4.1(d) | Yes |
| Tax credit generation/use | 4.4.1(e) | Yes |
| UTP-related deferred tax | 4.4.1(b) | Yes |

## 5. DTL Recapture Rule (Article 4.4.4)

### 5.1 The Five-Year Reversal Requirement

Deferred tax liabilities claimed in Covered Taxes must reverse (i.e., the underlying tax must be paid) within **five fiscal years**. If not, the DTL is **recaptured**.

### 5.2 How Recapture Works

**Year 1:** DTL of €500,000 included in DTAA (increases Covered Taxes)

**Year 6 (end):** DTL has not fully reversed; €300,000 still outstanding

**Recapture:** Year 1 ETR and Top-Up Tax are recomputed excluding the €300,000 DTL

### 5.3 Tracking Requirement

MNE Groups must track DTLs by fiscal year of origination and monitor reversal. Two methods are permitted:

| Method | Description | Use When |
|--------|-------------|----------|
| **FIFO** | First DTLs in are first to reverse | Homogeneous DTL categories |
| **LIFO** | Last DTLs in are first to reverse | Default method |

### 5.4 The Unjustified Balance

The recapture amount is determined by the "Unjustified Balance"—the portion of the DTL that has not reversed by the end of the five-year testing period.

```
Year 1: DTL accrued        +€1,000,000
Year 2: DTL reversal       −€200,000
Year 3: DTL reversal       −€300,000
Year 4: DTL reversal       −€100,000
Year 5: DTL reversal       −€150,000
Year 6 (end):
  Unjustified Balance:     €250,000 ← Recapture this amount
```

## 6. Recapture Exception Accruals (Article 4.4.5)

Certain DTLs are **exempt** from the five-year recapture rule. These "Recapture Exception Accruals" (REAs) do not need tracking.

### 6.1 Qualifying Categories

| REA Category | Description |
|--------------|-------------|
| **Cost recovery on tangible assets** | Depreciation timing differences on PP&E |
| **Leased tangible assets** | DTLs on right-of-use assets (per June 2024 guidance) |
| **R&D expenditure** | DTLs from capitalised R&D amortisation |
| **Decommissioning/remediation** | DTLs on environmental provisions |
| **Fair value accounting** | DTLs on unrealised gains from fair value |
| **Foreign exchange** | DTLs on unrealised FX gains |
| **Insurance reserves** | DTLs on insurance technical provisions |
| **Deferred acquisition costs** | Insurance DAC-related DTLs |
| **Reinvestment gains** | DTLs on deferred gains from asset reinvestment |

### 6.2 Practical Benefit

If a DTL falls within an REA category, no tracking is required—the DTL can be included in DTAA without monitoring for reversal.

**Example:**
```
SG Germany GmbH has:
  DTL on accelerated depreciation (tangible assets): €800,000
  DTL on intangible amortisation: €400,000

REA Analysis:
  Tangible asset DTL: REA (cost recovery) → No tracking required
  Intangible DTL: NOT an REA → Track for 5-year recapture
```

## 7. Unclaimed Accrual Election (Article 4.4.7)

### 7.1 The Election

If a DTL is **not expected to reverse** within five years, the entity can elect to treat it as an "Unclaimed Accrual."

### 7.2 Effect of Election

- The DTL is **excluded** from DTAA in the year of origination
- No recapture tracking is required
- When the DTL eventually reverses, it is added to DTAA in that year

### 7.3 When to Use

| Scenario | Election Recommended? |
|----------|----------------------|
| DTL will clearly reverse within 5 years | No—include normally |
| DTL may or may not reverse within 5 years | Consider—avoids recapture risk |
| DTL expected to be long-term (>5 years) | Yes—prevents recapture complexity |

### 3.3 Example

```
Year 1: DTL of €600,000 on indefinite-life intangible
        Expected reversal: 10+ years (asset unlikely to be sold/impaired)

Without election:
  Include €600,000 in DTAA → Track for 5 years → Recapture in Year 6

With Unclaimed Accrual election:
  Exclude €600,000 from DTAA → No tracking needed
  When asset eventually sold (Year 12): Include €600,000 in Year 12 DTAA
```

## 8. The GloBE Loss Election (Article 4.5)

### 8.1 Overview

The GloBE Loss Election provides an **alternative** to standard deferred tax accounting. When elected, Article 4.4 rules are replaced by a simplified loss carryforward mechanism.

### 8.2 When to Consider

| Situation | GloBE Loss Election Beneficial? |
|-----------|--------------------------------|
| Zero/low-tax jurisdiction with losses | **Yes**—creates 15% DTA where none exists |
| High-tax jurisdiction with complex DT | **Maybe**—simplifies but ignores other timing differences |
| Jurisdiction with EDTS | **No**—election not available |

### 8.3 How It Works

**Step 1:** Calculate Net GloBE Loss for the jurisdiction

**Step 2:** Create GloBE Loss DTA = Net GloBE Loss × 15%

**Step 3:** Carry forward GloBE Loss DTA to future years

**Step 4:** In profit years, use GloBE Loss DTA = MIN(GloBE Income × 15%, Available DTA)

**Step 5:** Add usage amount to Covered Taxes (Article 4.1.2(b))

### 8.4 Worked Example

```
SG Cayman Ltd (0% tax jurisdiction):

Year 1: GloBE Loss €10,000,000
        Accounting DTA: €0 (no tax)
        GloBE Loss DTA: €10M × 15% = €1,500,000

Year 2: GloBE Loss €5,000,000
        Accounting DTA: €0
        GloBE Loss DTA addition: €5M × 15% = €750,000
        Cumulative GloBE Loss DTA: €2,250,000

Year 3: GloBE Income €8,000,000
        GloBE Loss DTA usage: MIN(€8M × 15%, €2,250,000) = €1,200,000
        Add to Covered Taxes: +€1,200,000
        ETR: €1,200,000 ÷ €8,000,000 = 15.0% ← No Top-Up Tax!
        Remaining GloBE Loss DTA: €2,250,000 − €1,200,000 = €1,050,000
```

### 8.5 Key Trade-Off

| Aspect | Standard DT (Art. 4.4) | GloBE Loss Election (Art. 4.5) |
|--------|------------------------|-------------------------------|
| Loss recognition | Per accounting DTA | At 15% rate |
| Other timing differences | Included | **Ignored** |
| DTL recapture tracking | Required | Not applicable |
| Complexity | Higher | Lower |

**Warning:** Once elected, all other deferred tax attributes in the jurisdiction are ignored. Only the GloBE Loss DTA is tracked.

### 8.6 Election Mechanics

- **When:** File with first GIR including the jurisdiction
- **Scope:** Applies to entire jurisdiction, not individual entities
- **Revocation:** Permitted, but GloBE Loss DTA balance is reduced to zero

## 9. Transition Year Rules (Article 9.1)

### 9.1 Opening Balance Recognition

In the first year the MNE Group is subject to GloBE (the "Transition Year"), existing deferred tax balances are brought into the GloBE system.

**Rule:** Recognise DTAs and DTLs at the **lower of 15% or the domestic rate**

### 9.2 Loss DTA Recasting

Pre-existing DTAs from losses can be **recast upward** to 15% if:
1. The DTA arose from losses
2. The losses would have been GloBE Losses

**Example:**
```
Transition Year opening balance:
  DTA from losses at 10% rate: €500,000 (losses of €5M)

Recast to 15%:
  GloBE DTA: €5M × 15% = €750,000

Increase to DTAA: +€250,000
```

### 9.3 Pre-Transition DTL Treatment

DTLs imported into GloBE in the Transition Year are **not subject to the five-year recapture rule**.

**Practical benefit:** No need to track pre-existing DTLs for recapture.

### 9.4 Excluded Items

The following cannot be brought into the GloBE system:
- DTAs arising from excluded income transactions after 30 November 2021
- DTAs from government tax benefits created after 30 November 2021
- Basis step-ups from intra-group transfers after 30 November 2021

## 10. Deferred Tax Adjustment Process Flowchart

```
┌─────────────────────────────────────────────────────────────────┐
│                  STEP 1: STARTING POINT                         │
│  Extract Deferred Tax Expense from P&L                          │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                  STEP 2: RATE CAP                               │
│  If domestic rate > 15%: Recast all DTAs/DTLs at 15%            │
│  If domestic rate < 15%: Loss DTAs may be recast UP to 15%      │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                  STEP 3: EXCLUSIONS                             │
│  Remove deferred tax related to:                                │
│  • Excluded income (dividends, equity gains)                    │
│  • Valuation allowance movements                                │
│  • Rate change remeasurements                                   │
│  • Tax credit generation/use                                    │
│  • UTPs                                                         │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                  STEP 4: DTL ANALYSIS                           │
│  For each DTL:                                                  │
│  • Is it an REA? → No tracking required                         │
│  • Will it reverse in 5 years? → Include in DTAA                │
│  • Not expected to reverse? → Unclaimed Accrual election        │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                  STEP 5: RECAPTURE CHECK                        │
│  For non-REA DTLs claimed in prior years:                       │
│  • Has 5-year period ended?                                     │
│  • Calculate Unjustified Balance                                │
│  • Trigger recapture adjustment if required                     │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                  STEP 6: CALCULATE DTAA                         │
│  Total Deferred Tax Adjustment Amount =                         │
│    Adjusted Deferred Tax Expense after all modifications        │
└─────────────────────────────────────────────────────────────────┘
```

## 11. Stratos Worked Example: Deferred Tax Adjustments

**Scenario:** SG Germany GmbH's FY 2025 deferred tax adjustment workpaper

### 11.1 Starting Data

| Item | Amount (€) | Rate | Notes |
|------|------------|------|-------|
| Deferred tax expense (P&L) | 1,600,000 | 30% | German combined rate |
| DTL on intangibles (FY 2025 increase) | 900,000 | 30% | Goodwill amortisation |
| DTL on PP&E (FY 2025 increase) | 400,000 | 30% | Accelerated depreciation |
| DTA on provisions (FY 2025 increase) | (250,000) | 30% | Accrued expenses |
| Valuation allowance movement | 150,000 | — | Write-down of Irish DTA |
| Rate change impact | (80,000) | — | German rate adjustment |
| DT on excluded dividend | 50,000 | 30% | Tax on €167K dividend |

### 11.2 Step-by-Step Calculation

**Step 1: Starting Point**
```
Deferred tax expense (P&L):      €1,600,000
```

**Step 2: 15% Rate Cap**

German rate (30%) > 15%, so recast all movements:

| Item | At 30% | At 15% | Adjustment |
|------|--------|--------|------------|
| DTL intangibles | €900,000 | €450,000 | −€450,000 |
| DTL PP&E | €400,000 | €200,000 | −€200,000 |
| DTA provisions | (€250,000) | (€125,000) | +€125,000 |

```
Rate cap adjustment:             −€525,000
```

**Step 3: Exclusions**
```
Valuation allowance movement:    −€150,000 (exclude)
Rate change impact:              +€80,000 (exclude, was negative)
DT on excluded dividend:         −€50,000 (exclude)
                                 ─────────
Exclusions adjustment:           −€120,000
```

**Step 4: DTL Analysis**

| DTL | Amount (at 15%) | REA? | Treatment |
|-----|-----------------|------|-----------|
| Intangibles | €450,000 | No | Track for recapture |
| PP&E | €200,000 | Yes (tangible asset) | No tracking needed |

**Step 5: Recapture Check**

No prior-year DTLs have reached five-year anniversary in FY 2025. No recapture required.

**Step 6: Calculate DTAA**
```
Starting deferred tax expense:    €1,600,000
Rate cap adjustment:             −€525,000
Exclusions:                      −€120,000
Recapture:                        €0
                                 ──────────
Total DTAA:                       €955,000
```

### 11.3 Summary Workpaper

| Line | Description | Original | Adjustment | GloBE Value |
|------|-------------|----------|------------|-------------|
| 1 | DT expense (P&L) | €1,600,000 | | |
| 2 | Rate cap (30% → 15%) | | −€525,000 | |
| 3 | Valuation allowance | | −€150,000 | Excluded |
| 4 | Rate change | | +€80,000 | Excluded |
| 5 | DT on excluded dividend | | −€50,000 | Excluded |
| 6 | DTL recapture | | €0 | None required |
| **7** | **Total DTAA** | | | **€955,000** |

## 12. Total Adjusted Covered Taxes Calculation

Combining Chapter 4.2 (current) and Chapter 4.3 (deferred):

| Component | Reference | Amount (€) |
|-----------|-----------|------------|
| Adjusted Covered Taxes (Current) | Chapter 4.2 | 11,295,000 |
| Total Deferred Tax Adjustment (DTAA) | Chapter 4.3 | 955,000 |
| **Total Adjusted Covered Taxes** | | **12,250,000** |

### 12.1 ETR Calculation Preview

```
GloBE Income (from Part 3, adjusted for QRTC): €53,880,000
Adjusted Covered Taxes:                        €12,250,000

Jurisdictional ETR = €12,250,000 ÷ €53,880,000 = 22.7%

Since 22.7% > 15%, no Top-Up Tax for Germany.
```

## 13. DTL Recapture Tracking Template

For non-REA DTLs, maintain a tracking schedule:

| DTL Category | FY Originated | Original Amount | Y1 Reversal | Y2 Reversal | Y3 Reversal | Y4 Reversal | Y5 Reversal | Y6 Recapture |
|--------------|---------------|-----------------|-------------|-------------|-------------|-------------|-------------|--------------|
| Intangibles | 2024 | €450,000 | | | | | | |
| Intangibles | 2025 | €450,000 | | | | | | |

Update annually with actual reversals. If balance remains at Y5 end, calculate Unjustified Balance for recapture.

## 14. Common Pitfalls

### 14.1 Pitfall 1: Forgetting Rate Cap on High-Tax Jurisdictions

**Issue:** Including DTAs/DTLs at domestic rates above 15%

**Impact:** Overstates DTAA and Covered Taxes

**Solution:** Always recast to MIN(15%, domestic rate)
