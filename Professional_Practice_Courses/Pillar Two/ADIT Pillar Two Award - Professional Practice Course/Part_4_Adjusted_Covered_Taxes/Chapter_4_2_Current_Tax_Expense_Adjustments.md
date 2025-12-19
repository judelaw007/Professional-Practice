# Chapter 4.2: Current Tax Expense Adjustments

## Learning Objective

This chapter provides the methodology for adjusting the current tax expense starting point to arrive at Adjusted Covered Taxes. The current tax expense from financial accounts requires modifications to align with GloBE principles—certain items must be added, others subtracted. Mastering these adjustments prevents both overstating and understating the ETR numerator.

## Introduction

Financial accounting captures tax expense using principles designed for investor reporting—emphasising prudence, matching, and fair presentation of obligations. The GloBE framework has different objectives: measuring actual taxation of income to determine whether a jurisdiction meets the 15% minimum. These objectives don't always align. Accounting standards may record taxes in equity rather than profit and loss; they may include uncertain tax provisions that may never be paid; they may exclude taxes that have been paid but relate to prior periods. The adjustment framework in Articles 4.1.2 and 4.1.3 bridges this gap, adding items that represent genuine taxation not captured in current P&L expense, and subtracting items that overstate actual taxation. The result—Adjusted Covered Taxes—represents a more accurate picture of taxes that will actually be paid on current-year income, which is precisely what the minimum tax calculation requires.

## 1. The Adjustment Framework

Article 4.1.1 establishes that Adjusted Covered Taxes begin with the current tax expense from financial accounts. Articles 4.1.2 and 4.1.3 then prescribe specific additions and subtractions.

**Formula:**
```
Adjusted Covered Taxes (Current) =
    Current Tax Expense (from financial accounts)
  + Additions (Article 4.1.2)
  − Subtractions (Article 4.1.3)
```

The deferred tax adjustments (covered in Chapter 4.3) are applied separately.

## 2. Additions to Covered Taxes (Article 4.1.2)

Five categories of additions ensure taxes that belong in the ETR numerator are captured even if not recorded as current tax expense in P&L.

### 2.1 Addition 1: Taxes Recorded Outside P&L (Article 4.1.2(a))

**What it captures:** Covered Taxes expensed in equity or Other Comprehensive Income (OCI) rather than profit before tax.

**Examples:**
| Item | Where Recorded | Treatment |
|------|----------------|-----------|
| Tax on revaluation gains | OCI | Add to Covered Taxes |
| Tax on hedging reserves | OCI | Add to Covered Taxes |
| Tax on actuarial adjustments | OCI | Add to Covered Taxes |
| Tax on foreign currency translation | Equity | Add to Covered Taxes |

**Practical step:** Review the tax charge reconciliation in notes to accounts. Extract any income tax recorded directly in equity or OCI and add to current tax expense.

**Stratos example:** SG Germany GmbH has a €45,000 tax charge on pension actuarial gains recorded in OCI. This is added to Covered Taxes.

### 2.2 Addition 2: GloBE Loss DTA Usage (Article 4.1.2(b))

**What it captures:** When the GloBE Loss Election is made (see Chapter 4.4), a notional DTA is created at 15%. When this GloBE Loss DTA is utilised in subsequent years, the utilisation amount is added to Covered Taxes.

**Mechanics:**
```
Year 1: GloBE Loss of €10M → Create GloBE Loss DTA: €10M × 15% = €1.5M
Year 2: GloBE Income of €8M → Use GloBE Loss DTA: €8M × 15% = €1.2M
        → Add €1.2M to Year 2 Covered Taxes
```

**Why this matters:** Under the GloBE Loss Election, losses generate a deemed tax benefit at 15%. When income is earned in future years, this deemed benefit must flow through the ETR calculation.

### 2.3 Addition 3: UTPs Subsequently Paid (Article 4.1.2(c))

**What it captures:** Tax on uncertain tax positions (UTPs) that was previously excluded from Covered Taxes but is now actually paid.

**The cycle:**
1. **Year 1:** UTP accrued → Excluded from Covered Taxes (Article 4.1.3(d))
2. **Year 3:** UTP resolved, tax paid → Add to Year 3 Covered Taxes

**Important exclusion:** Interest and penalties associated with UTPs are NOT added—only the tax principal amount.

**Example:**
```
FY 2024: SG Ireland Ltd accrues €800,000 UTP provision
         → Excluded from 2024 Covered Taxes

FY 2026: Irish Revenue audit settles; €650,000 tax paid
         → Add €650,000 to 2026 Covered Taxes
         → €150,000 release goes to income (not relevant to Covered Taxes)
```

### 2.4 Addition 4: QRTC Recorded as Tax Reduction (Article 4.1.2(d))

**What it captures:** Qualified Refundable Tax Credits that were recorded as a reduction to current tax expense must be reversed out and treated as income instead.

**The mechanics:**
| Step | Action | Effect |
|------|--------|--------|
| 1 | Identify QRTC in tax expense | Credit reduces tax expense |
| 2 | Add QRTC amount back to Covered Taxes | Reverses accounting treatment |
| 3 | Add QRTC to GloBE Income | Treats as income (Article 3.2.10) |

**Example:**
```
Financial accounts show:
  Pre-credit tax expense:     €5,000,000
  R&D tax credit (QRTC):     (€200,000)
  Net tax expense:            €4,800,000

GloBE adjustment:
  Current tax expense:        €4,800,000
  Add back QRTC:             +€200,000
  Adjusted Covered Taxes:     €5,000,000

Corresponding GloBE Income adjustment:
  Financial accounting income: €30,000,000
  Add QRTC:                   +€200,000
  Adjusted GloBE Income:      €30,200,000
```

**Critical point:** The QRTC adjustment is dual—add to Covered Taxes AND add to GloBE Income. Both adjustments must be made together.

### 2.5 Addition 5: Taxes on Distributed Profits Under EDTS (Article 4.1.2(e))

**What it captures:** For entities in Eligible Distribution Tax System jurisdictions (e.g., Estonia, Latvia), deemed distribution taxes expected to be paid within four years are added.

**Application:** Only relevant for entities in EDTS jurisdictions. See Chapter 4.1 for EDTS mechanics.

The additions framework reflects a fundamental principle: taxes should be counted in the year they relate to the underlying income, not necessarily the year they appear in the P&L line for current tax expense. Taxes recorded in OCI relate to income items that bypass P&L—recording them elsewhere doesn't make them any less real. GloBE Loss DTA utilisation represents the realisation of previously accumulated tax benefits—the loss reduced future taxes, and that reduction must flow through Covered Taxes when realised. UTP settlements represent taxes that were previously uncertain but are now paid—reality has replaced estimation. QRTC reversals ensure that refundable credits are treated as income rather than tax reductions, producing the favourable ETR treatment that policy intends. Each addition corrects for an accounting presentation that would otherwise understate the taxes actually paid.

## 3. Subtractions from Covered Taxes (Article 4.1.3)

Five categories of subtractions ensure taxes are not counted when they relate to income excluded from GloBE or when payment is uncertain.

### 3.1 Subtraction 1: Taxes on Excluded Income (Article 4.1.3(a))

**Principle:** If income is excluded from GloBE Income, the tax on that income must also be excluded from Covered Taxes. Otherwise, the ETR would be artificially inflated.

**Categories of excluded income requiring tax subtraction:**
| Excluded Income | GloBE Article | Tax Treatment |
|-----------------|---------------|---------------|
| Excluded Dividends | Article 3.2.1(b) | Subtract related tax |
| Excluded Equity Gains | Article 3.2.1(c) | Subtract related tax |
| International Shipping Income | Article 3.3 | Subtract related tax |
| Policy Disallowed Expenses | Article 3.2.1(f) | Complex—see below |

**Calculation method for excluded income tax:**
```
Tax on Excluded Income = (Excluded Income ÷ Total Income) × Total Tax Expense
```

**Worked example:**
```
Total GloBE Income:           €10,000,000
Excluded Dividend:             €2,000,000
Total Tax Expense:             €1,500,000

Tax on Excluded Dividend:
  (€2,000,000 ÷ €10,000,000) × €1,500,000 = €300,000

Adjusted Covered Taxes:
  €1,500,000 − €300,000 = €1,200,000
```

**Documentation required:** Maintain workpaper showing allocation methodology between included and excluded income.

### 3.2 Subtraction 2: Non-QRTC Recorded as Income (Article 4.1.3(b))

**What it captures:** If a non-qualified refundable tax credit was recorded as income (rather than as a reduction of tax expense), it must be subtracted from Covered Taxes.

**Contrast with Article 4.1.2(d):**
| Credit Type | Accounting Treatment | GloBE Adjustment |
|-------------|---------------------|------------------|
| QRTC recorded as tax reduction | Add to Covered Taxes | Article 4.1.2(d) |
| QRTC recorded as income | No adjustment needed | — |
| Non-QRTC recorded as income | Subtract from Covered Taxes | Article 4.1.3(b) |
| Non-QRTC recorded as tax reduction | No adjustment needed | — |

### 3.3 Subtraction 3: Refund of Non-QRTC (Article 4.1.3(c))

**What it captures:** Refunds of non-qualified tax credits that are recorded as a reduction to current tax expense.

**Example:** Entity receives refund of previously claimed investment tax credit (non-QRTC). The refund reduced current tax expense. Subtract this amount from Covered Taxes.

### 3.4 Subtraction 4: Uncertain Tax Positions (Article 4.1.3(d))

**Principle:** Tax expense related to UTPs is excluded from Covered Taxes because payment is not sufficiently certain.

**Definition:** A UTP exists when the entity takes a filing position that is **not more likely than not** to be sustained upon examination (i.e., less than 50% probability of being upheld).

**Impact:**
```
Current tax expense per accounts:  €8,000,000
UTP provision included:           (€500,000)
Covered Taxes:                     €7,500,000
```

**Subsequent treatment:** When the UTP is resolved and tax is paid, add to Covered Taxes per Article 4.1.2(c).

### 3.5 Subtraction 5: Tax Not Expected to Be Paid Within 3 Years (Article 4.1.3(e))

**Principle:** Current tax expense that is not expected to be paid within three years of the fiscal year-end is excluded from Covered Taxes.

**Rationale:** GloBE requires a degree of certainty that taxes will actually be paid. If payment is delayed beyond three years, it should not count until paid.

**When this applies:**
- Contested tax assessments under appeal
- Tax payment deferrals granted by authorities
- Instalment arrangements extending beyond three years

**Example:**
```
FY 2024 current tax expense:    €6,000,000
Tax under appeal (payment suspended):  €1,200,000

If resolution expected beyond FY 2027:
  Covered Taxes for 2024: €6,000,000 − €1,200,000 = €4,800,000
```

The subtractions share a common logic: they prevent overstating the taxes that genuinely count toward the 15% minimum. Taxes on excluded income must be removed because the income itself is excluded—including only the tax would artificially inflate the ETR. Uncertain tax positions represent contingencies, not settled liabilities—counting them would credit taxes that may never be paid. Taxes not expected to be paid within three years are too speculative to rely upon. Each subtraction ensures that Covered Taxes reflects economic reality rather than accounting constructs. The matching principle that underlies these rules is symmetrical: just as GloBE Income excludes certain items, Covered Taxes must exclude the taxes on those items. The result is an ETR that accurately measures the taxation of included income.

## 4. CFC Tax Push-Down (Article 4.3.2(c))

When a parent entity pays CFC tax on the undistributed income of a foreign subsidiary, that tax must be **pushed down** to the subsidiary for Covered Tax purposes.

### 4.1 Why Push-Down Is Required

Without push-down:
- Parent's ETR is inflated (tax without corresponding income)
- Subsidiary's ETR is understated (income without corresponding tax)

Push-down ensures taxes are matched with the income that generated them.

### 4.2 The Push-Down Mechanism

**Step 1:** Identify CFC tax in parent's current tax expense

**Step 2:** Determine the subsidiary to which the CFC income relates

**Step 3:** Remove CFC tax from parent's Covered Taxes

**Step 4:** Add CFC tax to subsidiary's Covered Taxes

**Diagram:**
```
BEFORE PUSH-DOWN:
┌─────────────────────────────┐
│ Parent Co (UK)              │
│ CFC Tax Paid: €300,000      │ ← Tax here
│ Income: €20,000,000         │
└─────────────────────────────┘
              │
              ▼
┌─────────────────────────────┐
│ Sub Co (Low-Tax Country)    │
│ Tax Paid: €50,000           │
│ Income: €5,000,000          │ ← Income here
│ ETR: 1.0%                   │
└─────────────────────────────┘

AFTER PUSH-DOWN:
┌─────────────────────────────┐
│ Parent Co (UK)              │
│ CFC Tax: €300,000 → REMOVED │
│ Income: €20,000,000         │
└─────────────────────────────┘
              │
              ▼
┌─────────────────────────────┐
│ Sub Co (Low-Tax Country)    │
│ Tax: €50,000 + €300,000     │ ← CFC tax pushed down
│ Income: €5,000,000          │
│ ETR: 7.0%                   │ ← Higher ETR
└─────────────────────────────┘
```

### 4.3 Passive Income Limitation (Article 4.3.3)

For passive income (interest, royalties, dividends), the push-down amount is capped. The cap prevents excessive push-down from artificially eliminating top-up tax.

**The formula:**
```
Push-Down Limit = MIN(
    Actual CFC tax on passive income,
    Top-Up Tax % × Passive income taxed under CFC
)
```

**Where:**
- Top-Up Tax % = 15% − Subsidiary's ETR (before push-down)

**Example:**
```
Sub Co (Singapore):
  Passive income taxed under UK CFC: €2,000,000
  Sub's ETR before push-down: 8%
  UK CFC tax on passive income: €500,000

Push-Down Limit:
  Top-Up Tax % = 15% − 8% = 7%
  Limit = 7% × €2,000,000 = €140,000

Push-Down Amount:
  MIN(€500,000, €140,000) = €140,000

Result:
  Only €140,000 pushed to Singapore, not €500,000
  Remaining €360,000 stays in UK parent's Covered Taxes
```

**Purpose:** This prevents a high-tax parent from fully shielding a low-tax subsidiary through CFC tax push-down.

## 5. Blended CFC Regime Rules (GILTI)

The US GILTI regime presents a unique challenge because it applies on a **blended** basis across all CFCs, not entity-by-entity.

### 5.1 The Issue

GILTI calculates tax on aggregate CFC income, making entity-level allocation difficult.

### 5.2 Temporary Allocation Rule (February 2023 Administrative Guidance)

For Blended CFC Tax Regimes:
1. Allocate GILTI tax to each CFC based on its share of total tested income
2. Apply passive income limitation separately to each CFC
3. Push down allocated amount to each CFC

**Note:** The June 2024 Administrative Guidance formula for regular CFC regimes does not apply to GILTI. The temporary rule continues.

## 6. The Three-Year Recapture Rule (Article 4.6.4)

Taxes included in Covered Taxes must be **actually paid** within three years. If not, they are recaptured.

### 6.1 Application Threshold

Only applies if unpaid taxes exceed **€1 million**.

### 6.2 Mechanics

**Year 1:** Include €2M current tax in Covered Taxes

**Year 4 (end):** Only €800,000 paid; €1.2M unpaid

**Recapture:** Recompute Year 1 ETR and Top-Up Tax excluding €1.2M

### 6.3 Practical Steps

1. Track current tax accruals by fiscal year
2. Monitor actual payment dates
3. At end of Year 3, assess unpaid amounts exceeding €1M
4. If threshold exceeded, trigger recapture calculation under Article 5.4.1

### 6.4 Documentation

Maintain a tracking schedule:

| Fiscal Year | Tax Accrued | Paid Y1 | Paid Y2 | Paid Y3 | Unpaid Y3 End | Recapture? |
|-------------|-------------|---------|---------|---------|---------------|------------|
| 2024 | €5,000,000 | €4,000,000 | €800,000 | €100,000 | €100,000 | No (<€1M) |
| 2025 | €6,500,000 | €3,000,000 | €2,000,000 | €200,000 | €1,300,000 | **Yes** |

## 7. Current Tax Adjustment Checklist

Use this checklist when calculating Adjusted Covered Taxes (current portion):

### 7.1 Step 1: Starting Point
- [ ] Extract current tax expense from P&L
- [ ] Confirm same financial accounts as used for GloBE Income

### 7.2 Step 2: Additions (Article 4.1.2)
- [ ] Tax recorded in equity/OCI on GloBE items
- [ ] GloBE Loss DTA utilised (if election made)
- [ ] UTP taxes paid this year (previously excluded)
- [ ] QRTCs recorded as tax reduction (reverse to income)
- [ ] EDTS deemed distribution taxes (if applicable)

### 7.3 Step 3: Subtractions (Article 4.1.3)
- [ ] Tax on excluded dividends
- [ ] Tax on excluded equity gains/losses
- [ ] Tax on international shipping income
- [ ] Non-QRTC recorded as income
- [ ] UTP provisions (not yet paid)
- [ ] Tax not expected to be paid within 3 years

### 7.4 Step 4: Allocations (Article 4.3)
- [ ] Identify CFC taxes in parent accounts
- [ ] Push down CFC taxes to subsidiaries
- [ ] Apply passive income limitation
- [ ] Document GILTI allocation if applicable

### 7.5 Step 5: Recapture Monitoring
- [ ] Track current tax payments by fiscal year
- [ ] Assess unpaid amounts at Year 3 end
- [ ] Trigger recapture if unpaid exceeds €1M

## 8. Stratos Worked Example: Current Tax Adjustments

**Scenario:** SG Germany GmbH's FY 2025 current tax adjustment workpaper

### 8.1 Starting Data

| Item | Amount (€) | Reference |
|------|------------|-----------|
| Current tax expense (P&L) | 11,200,000 | Chapter 4.1 |
| Tax in OCI (pension actuarial) | 45,000 | Note 12 |
| R&D credit (QRTC) | (180,000) | Recorded as tax reduction |
| Tax on excluded dividend | — | €3.1M dividend × 0% WHT |
| UTP provision | 280,000 | Transfer pricing reserve |
| Prior year UTP settled | 150,000 | Paid in 2025 |

### 8.2 Adjustment Calculation

**Step 1: Starting Point**
```
Current tax expense (P&L):          €11,200,000
```

**Step 2: Additions**
```
Tax in OCI (Art. 4.1.2(a)):         +€45,000
Prior UTP paid (Art. 4.1.2(c)):     +€150,000
QRTC add-back (Art. 4.1.2(d)):      +€180,000
                                    ─────────
Subtotal Additions:                 +€375,000
```

**Step 3: Subtractions**
```
Tax on excluded dividend:            −€0
  (Dividend from 100% subsidiary; no German WHT)

UTP provision (Art. 4.1.3(d)):      −€280,000
                                    ─────────
Subtotal Subtractions:              −€280,000
```

**Step 4: CFC Tax Push-Down**
```
UK parent CFC charge on SG Germany: €0
  (Germany is high-tax; no UK CFC exposure)

Push-down from parent:              €0
```

**Step 5: Adjusted Covered Taxes (Current)**
```
Starting point:                     €11,200,000
Additions:                          +€375,000
Subtractions:                       −€280,000
Push-down:                          +€0
                                    ───────────
Adjusted Covered Taxes (Current):   €11,295,000
```

### 8.3 Corresponding GloBE Income Adjustment

The QRTC add-back requires a matching GloBE Income adjustment:
```
GloBE Income (from Chapter 3.2):    €53,700,000
Add: QRTC (Art. 3.2.10):           +€180,000
                                    ───────────
Adjusted GloBE Income:              €53,880,000
```

### 8.4 Summary Workpaper

| Line | Description | Addition | Subtraction | Net Adjustment |
|------|-------------|----------|-------------|----------------|
| 1 | Current tax expense (starting) | | | €11,200,000 |
| 2 | Tax in OCI | €45,000 | | +€45,000 |
| 3 | Prior year UTP paid | €150,000 | | +€150,000 |
| 4 | QRTC reversal | €180,000 | | +€180,000 |
| 5 | Current year UTP | | €280,000 | −€280,000 |
| 6 | Tax on excluded income | | €0 | €0 |
| 7 | CFC push-down | €0 | | €0 |
| **8** | **Adjusted Covered Taxes (Current)** | | | **€11,295,000** |

## 9. Common Pitfalls

### 9.1 Pitfall 1: Forgetting the Dual QRTC Adjustment

**Issue:** Adding QRTC to Covered Taxes but forgetting to add to GloBE Income

**Impact:** ETR is incorrectly calculated

**Solution:** Always pair QRTC adjustments—Covered Taxes AND GloBE Income

### 9.2 Pitfall 2: Including UTP Penalties and Interest

**Issue:** Adding full UTP settlement (including penalties and interest) to Covered Taxes

**Impact:** Overstates Covered Taxes

**Solution:** Only include the tax principal; exclude interest and penalties

### 9.3 Pitfall 3: Ignoring Passive Income Limitation

**Issue:** Pushing down full CFC tax without applying Article 4.3.3 cap

**Impact:** Artificially inflates subsidiary's ETR

**Solution:** Always calculate and apply the passive income limitation

### 9.4 Pitfall 4: Missing Taxes in OCI/Equity

**Issue:** Only extracting current tax expense from P&L

**Impact:** Understates Covered Taxes

**Solution:** Review full tax reconciliation in notes; include taxes in equity/OCI

The current tax adjustment process ultimately serves the goal of ensuring that Covered Taxes accurately reflects the taxes that will actually be paid on current-year income. This requires looking beyond the P&L tax line to capture taxes recorded elsewhere, while simultaneously excluding items that represent uncertainty or relate to excluded income. Groups developing GloBE compliance processes should establish systematic workpapers that address each adjustment category, with clear documentation of the analysis performed. The CFC push-down rules add particular complexity for groups with extensive CFC exposure, requiring coordination between the parent entity's analysis and subsidiary-level calculations. The three-year recapture monitoring obligation creates an ongoing compliance burden that extends well beyond the initial filing year. Building robust tracking systems from the outset is essential to avoid recapture surprises in future periods.
