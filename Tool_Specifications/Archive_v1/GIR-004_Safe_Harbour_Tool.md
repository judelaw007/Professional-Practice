# GIR-004: Safe Harbour Qualification Tool - Tool Specification

**Version:** 1.0
**Last Updated:** 2024-12-07
**Status:** Planned
**Platform:** tools.mojitax.com

---

## 1. Tool Metadata

| Field | Value |
|-------|-------|
| Tool ID | GIR-004 |
| Tool Name | GIR Safe Harbour Qualification Tool |
| Category | Pillar Two |
| Form Type | Assessment |
| Status | Planned |
| Used By | GloBE Information Return: Complete Filing Implementation |
| Introduced In | Section 1.4 - Transition Rules and Safe Harbours |

---

## 2. Purpose & Learning Objective

### 2.1 Purpose
Practice assessing whether a jurisdiction qualifies for the Transitional CbCR Safe Harbour. This tool helps learners understand the three qualifying tests and determine which jurisdictions require full GloBE calculations versus those that can rely on simplified Country-by-Country Report (CbCR) data.

### 2.2 Learning Objective
After using this tool, learners will be able to:
- Apply the De Minimis Test thresholds correctly
- Calculate and apply the Simplified ETR Test with year-specific thresholds
- Understand the Routine Profits Test and its relationship to SBIE
- Determine overall safe harbour qualification status
- Recognize which jurisdictions require full GloBE calculations vs. safe harbour treatment
- Understand the strategic value of safe harbour elections in reducing compliance burden

### 2.3 Prerequisites
Learners should understand:
- The concept of Country-by-Country Reporting (CbCR)
- The difference between CbCR data and GloBE-adjusted data
- The transitional nature of the safe harbour (available 2024-2026)
- Basic SBIE concepts (for Routine Profits Test)

### 2.4 Safe Harbour Overview

The Transitional CbCR Safe Harbour allows MNE groups to use existing CbCR data instead of performing full GloBE calculations for certain jurisdictions. A jurisdiction qualifies if it meets **ANY ONE** of three tests:

```
┌─────────────────────────────────────────────────────────────────┐
│           TRANSITIONAL CbCR SAFE HARBOUR                        │
│                   (FY 2024-2026 only)                           │
└─────────────────────────────────────────────────────────────────┘
                              │
        ┌─────────────────────┼─────────────────────┐
        │                     │                     │
        ▼                     ▼                     ▼
┌───────────────┐   ┌───────────────┐   ┌───────────────┐
│  DE MINIMIS   │   │ SIMPLIFIED    │   │   ROUTINE     │
│     TEST      │   │  ETR TEST     │   │ PROFITS TEST  │
├───────────────┤   ├───────────────┤   ├───────────────┤
│ Revenue <€10M │   │ ETR >= 15%    │   │ Profit <= SBIE│
│     AND       │   │ (2024)        │   │               │
│ Profit <€1M   │   │ ETR >= 16%    │   │               │
│               │   │ (2025)        │   │               │
│               │   │ ETR >= 17%    │   │               │
│               │   │ (2026)        │   │               │
└───────┬───────┘   └───────┬───────┘   └───────┬───────┘
        │                   │                   │
        └─────────────────────┼─────────────────────┘
                              │
                              ▼
                    ┌─────────────────┐
                    │  PASS ANY ONE   │
                    │       =         │
                    │  SAFE HARBOUR   │
                    │    APPLIES      │
                    └─────────────────┘
```

---

## 3. Input Fields

### 3.1 Fiscal Year

| Property | Value |
|----------|-------|
| Field ID | `fiscal_year` |
| Label | Fiscal Year |
| Data Type | Integer (year selection) |
| Required | **Yes** |
| UI Element | Dropdown select |
| Default Value | 2024 |
| Help Text | "Select the fiscal year. The Simplified ETR threshold varies by year. Safe harbour is only available for FY 2024-2026." |

**Dropdown Options:**

| Value | Display Text | ETR Threshold |
|-------|--------------|---------------|
| 2024 | FY 2024 | 15% |
| 2025 | FY 2025 | 16% |
| 2026 | FY 2026 | 17% |

**Important Note:** After FY 2026, the Transitional CbCR Safe Harbour expires. Display warning if future enhancement adds later years.

**Validation Rules:**
| Rule | Condition | Error Message |
|------|-----------|---------------|
| Required | No selection made | "Please select a fiscal year" |
| Valid range | Year not in 2024-2026 | "Safe harbour is only available for FY 2024-2026" |

---

### 3.2 Jurisdiction Name

| Property | Value |
|----------|-------|
| Field ID | `jurisdiction_name` |
| Label | Jurisdiction |
| Data Type | String |
| Required | **Yes** |
| Max Length | 100 characters |
| UI Element | Text input or searchable dropdown |
| Placeholder Text | "e.g., United Kingdom, Germany" |
| Help Text | "Enter the jurisdiction you are testing for safe harbour qualification" |

**Validation Rules:**
| Rule | Condition | Error Message |
|------|-----------|---------------|
| Required | Field is empty | "Jurisdiction is required" |
| Max length | Length > 100 | "Jurisdiction name cannot exceed 100 characters" |

---

### 3.3 CbCR Revenue

| Property | Value |
|----------|-------|
| Field ID | `cbcr_revenue` |
| Label | CbCR Revenue |
| Data Type | Decimal number |
| Required | **Yes** |
| Precision | 2 decimal places |
| Min Value | 0.00 |
| Max Value | 999,999,999,999.99 |
| Default Value | Empty |
| UI Element | Currency input field with thousand separators |
| Placeholder Text | "Enter total CbCR revenue for jurisdiction" |
| Help Text | "Total revenue reported in the CbCR for this jurisdiction. Use CbCR values, not GloBE-adjusted values." |

**Validation Rules:**
| Rule | Condition | Error Message |
|------|-----------|---------------|
| Required | Field is empty | "CbCR Revenue is required" |
| Non-negative | Value < 0 | "CbCR Revenue cannot be negative" |
| Numeric | Non-numeric input | "Please enter a valid number" |

**Data Source Note:** This value comes from the MNE group's Country-by-Country Report (Table 1, Column 1: Revenues - Total).

---

### 3.4 CbCR Profit Before Tax

| Property | Value |
|----------|-------|
| Field ID | `cbcr_profit` |
| Label | CbCR Profit Before Tax |
| Data Type | Decimal number |
| Required | **Yes** |
| Precision | 2 decimal places |
| Min Value | -999,999,999,999.99 (can be negative - loss) |
| Max Value | 999,999,999,999.99 |
| Default Value | Empty |
| UI Element | Currency input field with thousand separators |
| Placeholder Text | "Enter CbCR profit (or loss) before tax" |
| Help Text | "Profit before tax from CbCR. Can be negative if the jurisdiction has a loss. Use CbCR values, not GloBE-adjusted values." |

**Validation Rules:**
| Rule | Condition | Error Message |
|------|-----------|---------------|
| Required | Field is empty | "CbCR Profit Before Tax is required" |
| Numeric | Non-numeric input | "Please enter a valid number" |

**Special Handling for Losses:**
- Negative values are valid (jurisdiction has a loss)
- If profit is negative or zero, Simplified ETR Test is not applicable
- If profit is negative, Routine Profits Test is automatically PASS (no positive profit to compare)

**Data Source Note:** This value comes from CbCR Table 1, Column 2: Profit (Loss) Before Income Tax.

---

### 3.5 Simplified Covered Taxes

| Property | Value |
|----------|-------|
| Field ID | `simplified_taxes` |
| Label | Simplified Covered Taxes |
| Data Type | Decimal number |
| Required | **Yes** |
| Precision | 2 decimal places |
| Min Value | 0.00 |
| Max Value | 999,999,999,999.99 |
| Default Value | Empty |
| UI Element | Currency input field with thousand separators |
| Placeholder Text | "Enter simplified covered taxes" |
| Help Text | "Income Tax Accrued from CbCR, adjusted per safe harbour guidance. Generally equals CbCR Income Tax Paid/Accrued with minor adjustments." |

**Validation Rules:**
| Rule | Condition | Error Message |
|------|-----------|---------------|
| Required | Field is empty | "Simplified Covered Taxes is required" |
| Non-negative | Value < 0 | "Simplified Covered Taxes cannot be negative" |
| Numeric | Non-numeric input | "Please enter a valid number" |

**Data Source Note:** Based on CbCR Table 1, Column 4: Income Tax Accrued - Current Year, with adjustments per OECD Administrative Guidance.

---

### 3.6 SBIE Amount

| Property | Value |
|----------|-------|
| Field ID | `sbie_amount` |
| Label | SBIE Amount |
| Data Type | Decimal number |
| Required | **Yes** |
| Precision | 2 decimal places |
| Min Value | 0.00 |
| Max Value | 999,999,999,999.99 |
| Default Value | Empty |
| UI Element | Currency input field with thousand separators |
| Placeholder Text | "Enter SBIE amount for jurisdiction" |
| Help Text | "The Substance-Based Income Exclusion for the jurisdiction. You can calculate this using GIR-002 SBIE Calculator, or use a simplified estimate for safe harbour testing." |

**Validation Rules:**
| Rule | Condition | Error Message |
|------|-----------|---------------|
| Required | Field is empty | "SBIE Amount is required" |
| Non-negative | Value < 0 | "SBIE Amount cannot be negative" |
| Numeric | Non-numeric input | "Please enter a valid number" |

**Note:** For safe harbour purposes, SBIE can be calculated using simplified methods if full GloBE SBIE data is not yet available.

---

### 3.7 Currency

| Property | Value |
|----------|-------|
| Field ID | `currency` |
| Label | Currency |
| Data Type | String (dropdown selection) |
| Required | **Yes** |
| Default Value | EUR |
| UI Element | Dropdown select |
| Help Text | "Select the currency. All inputs must be in the same currency." |

**Dropdown Options:**
| Code | Display | Symbol |
|------|---------|--------|
| EUR | Euro (EUR) | € |
| USD | US Dollar (USD) | $ |
| GBP | British Pound (GBP) | £ |
| CHF | Swiss Franc (CHF) | CHF |

**De Minimis Thresholds:** The €10M revenue and €1M profit thresholds are EUR-denominated. If user selects different currency, display note that thresholds are EUR-equivalent.

---

## 4. Output Fields

### 4.1 De Minimis Test Result

| Property | Value |
|----------|-------|
| Field ID | `de_minimis_result` |
| Label | De Minimis Test |
| Data Type | Object with status and details |
| UI Element | Result card with PASS/FAIL badge |

**Display Components:**
| Component | Description |
|-----------|-------------|
| Status | PASS (green) or FAIL (red) |
| Revenue Check | "Revenue €X < €10M" or "Revenue €X ≥ €10M" |
| Profit Check | "Profit €X < €1M" or "Profit €X ≥ €1M" |
| Explanation | Why test passed or failed |

---

### 4.2 Simplified ETR Test Result

| Property | Value |
|----------|-------|
| Field ID | `simplified_etr_result` |
| Label | Simplified ETR Test |
| Data Type | Object with status, ETR, threshold, and details |
| UI Element | Result card with PASS/FAIL badge |

**Display Components:**
| Component | Description |
|-----------|-------------|
| Status | PASS (green) or FAIL (red) or N/A (grey) |
| Calculated ETR | "Simplified ETR: XX.XX%" |
| Threshold | "FY{year} Threshold: XX%" |
| Comparison | "XX.XX% ≥ XX%" (pass) or "XX.XX% < XX%" (fail) |

**N/A Condition:** If CbCR Profit ≤ 0, ETR cannot be calculated. Display: "N/A - No positive profit"

---

### 4.3 Routine Profits Test Result

| Property | Value |
|----------|-------|
| Field ID | `routine_profits_result` |
| Label | Routine Profits Test |
| Data Type | Object with status and details |
| UI Element | Result card with PASS/FAIL badge |

**Display Components:**
| Component | Description |
|-----------|-------------|
| Status | PASS (green) or FAIL (red) |
| Profit | "CbCR Profit: €X" |
| SBIE | "SBIE Amount: €X" |
| Comparison | "Profit ≤ SBIE" (pass) or "Profit > SBIE" (fail) |

**Special Case:** If profit is negative or zero, test automatically PASSES (no excess profit possible).

---

### 4.4 Overall Safe Harbour Status

| Property | Value |
|----------|-------|
| Field ID | `overall_status` |
| Label | Safe Harbour Status |
| Data Type | String (enumerated) |
| UI Element | Large status banner |

**Status Values:**
| Status | Condition | Display Text | Background Color |
|--------|-----------|--------------|------------------|
| QUALIFIES | Any test PASS | "SAFE HARBOUR APPLIES" | Green (#28A745) |
| NOT_QUALIFIED | All tests FAIL | "FULL GloBE CALCULATION REQUIRED" | Red (#DC3545) |

---

### 4.5 Recommendation

| Property | Value |
|----------|-------|
| Field ID | `recommendation` |
| Label | Recommendation |
| Data Type | Formatted text |
| UI Element | Recommendation panel |

**Recommendation Text:**

If QUALIFIES:
```
This jurisdiction qualifies for the Transitional CbCR Safe Harbour.

Action: You may elect to apply the safe harbour for this jurisdiction.
Result: Top-up Tax for this jurisdiction is deemed to be ZERO.
Benefit: No full GloBE calculations required for this jurisdiction.

Note: Safe harbour election is made on a jurisdiction-by-jurisdiction,
year-by-year basis. Document your safe harbour elections in the GIR.
```

If NOT_QUALIFIED:
```
This jurisdiction does NOT qualify for the Transitional CbCR Safe Harbour.

Action: Full GloBE calculations are required for this jurisdiction.
Next Steps:
1. Calculate GloBE Income using GIR-001 ETR Calculator
2. Calculate SBIE using GIR-002 SBIE Calculator
3. Calculate Top-up Tax using GIR-003 Top-Up Tax Calculator

The jurisdiction may still have no Top-up Tax liability if ETR ≥ 15%
after full GloBE calculations.
```

---

### 4.6 Test Summary Table

| Property | Value |
|----------|-------|
| Field ID | `test_summary` |
| Label | Test Summary |
| Data Type | Table |
| UI Element | Summary table |

**Table Format:**
```
┌─────────────────────┬────────┬─────────────────────────────┐
│ Test                │ Result │ Details                     │
├─────────────────────┼────────┼─────────────────────────────┤
│ De Minimis Test     │ FAIL   │ Revenue €320M ≥ €10M        │
│ Simplified ETR Test │ PASS   │ 23.00% ≥ 15% threshold      │
│ Routine Profits Test│ PASS   │ Profit €48M ≤ SBIE €15M: NO │
├─────────────────────┼────────┼─────────────────────────────┤
│ OVERALL             │ PASS   │ Safe Harbour APPLIES        │
└─────────────────────┴────────┴─────────────────────────────┘
```

---

## 5. Calculation Logic

### 5.1 ETR Threshold Lookup

```
CONSTANT ETR_THRESHOLDS = {
    2024: 15.00,
    2025: 16.00,
    2026: 17.00
}
```

### 5.2 De Minimis Threshold Constants

```
CONSTANT DE_MINIMIS_REVENUE = 10,000,000    // €10 million
CONSTANT DE_MINIMIS_PROFIT = 1,000,000      // €1 million
```

### 5.3 Primary Calculation

```
FUNCTION AssessSafeHarbour(fiscal_year, jurisdiction, cbcr_revenue,
                           cbcr_profit, simplified_taxes, sbie_amount):

    // Initialize results
    results = {
        de_minimis: { status: null, details: {} },
        simplified_etr: { status: null, etr: null, threshold: null, details: {} },
        routine_profits: { status: null, details: {} },
        overall_status: null,
        qualifies: false
    }

    // ═══════════════════════════════════════════════════════════
    // TEST 1: DE MINIMIS TEST
    // ═══════════════════════════════════════════════════════════

    revenue_pass = cbcr_revenue < DE_MINIMIS_REVENUE
    profit_pass = cbcr_profit < DE_MINIMIS_PROFIT

    // Must pass BOTH conditions
    de_minimis_pass = revenue_pass AND profit_pass

    results.de_minimis = {
        status: de_minimis_pass ? "PASS" : "FAIL",
        revenue_check: revenue_pass,
        profit_check: profit_pass,
        revenue_value: cbcr_revenue,
        profit_value: cbcr_profit,
        revenue_threshold: DE_MINIMIS_REVENUE,
        profit_threshold: DE_MINIMIS_PROFIT
    }

    // ═══════════════════════════════════════════════════════════
    // TEST 2: SIMPLIFIED ETR TEST
    // ═══════════════════════════════════════════════════════════

    etr_threshold = ETR_THRESHOLDS[fiscal_year]

    IF cbcr_profit <= 0 THEN
        // Cannot calculate ETR with zero or negative profit
        results.simplified_etr = {
            status: "N/A",
            etr: null,
            threshold: etr_threshold,
            reason: "No positive profit - ETR cannot be calculated"
        }
        simplified_etr_pass = false
    ELSE
        simplified_etr = (simplified_taxes / cbcr_profit) × 100
        simplified_etr = ROUND(simplified_etr, 2)

        simplified_etr_pass = simplified_etr >= etr_threshold

        results.simplified_etr = {
            status: simplified_etr_pass ? "PASS" : "FAIL",
            etr: simplified_etr,
            threshold: etr_threshold,
            comparison: simplified_etr + "% vs " + etr_threshold + "% threshold"
        }
    END IF

    // ═══════════════════════════════════════════════════════════
    // TEST 3: ROUTINE PROFITS TEST
    // ═══════════════════════════════════════════════════════════

    IF cbcr_profit <= 0 THEN
        // No positive profit, so no excess profit possible
        routine_profits_pass = true
        results.routine_profits = {
            status: "PASS",
            reason: "No positive profit - automatically qualifies",
            profit_value: cbcr_profit,
            sbie_value: sbie_amount
        }
    ELSE
        routine_profits_pass = cbcr_profit <= sbie_amount

        results.routine_profits = {
            status: routine_profits_pass ? "PASS" : "FAIL",
            profit_value: cbcr_profit,
            sbie_value: sbie_amount,
            comparison: routine_profits_pass ?
                "Profit ≤ SBIE" : "Profit > SBIE"
        }
    END IF

    // ═══════════════════════════════════════════════════════════
    // OVERALL DETERMINATION
    // ═══════════════════════════════════════════════════════════

    // Qualifies if ANY test passes
    qualifies = de_minimis_pass OR simplified_etr_pass OR routine_profits_pass

    results.qualifies = qualifies
    results.overall_status = qualifies ? "QUALIFIES" : "NOT_QUALIFIED"
    results.qualifying_test =
        de_minimis_pass ? "De Minimis" :
        simplified_etr_pass ? "Simplified ETR" :
        routine_profits_pass ? "Routine Profits" : null

    RETURN results

END FUNCTION
```

### 5.4 Rounding Rules

| Calculation | Rounding Method | Precision |
|-------------|-----------------|-----------|
| Simplified ETR | Standard (half-up) | 2 decimal places |
| Comparisons | Use exact values before rounding for threshold tests |

### 5.5 Formula Reference

| Test | Formula | Source |
|------|---------|--------|
| De Minimis | Revenue < €10M AND Profit < €1M | OECD AG December 2023, Para 2.2 |
| Simplified ETR | Simplified Taxes ÷ CbCR Profit ≥ Threshold | OECD AG December 2023, Para 2.3 |
| Routine Profits | CbCR Profit ≤ SBIE | OECD AG December 2023, Para 2.4 |

---

## 6. User Interface Specifications

### 6.1 Layout Structure

```
┌─────────────────────────────────────────────────────────────┐
│  GIR Safe Harbour Qualification Tool                   [?]  │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │ INPUT SECTION                                        │   │
│  ├─────────────────────────────────────────────────────┤   │
│  │                                                      │   │
│  │  Fiscal Year:     [FY 2024           ▼]             │   │
│  │                   (ETR Threshold: 15%)               │   │
│  │                                                      │   │
│  │  Jurisdiction:    [United Kingdom        ]          │   │
│  │                                                      │   │
│  │  Currency:        [EUR ▼]                           │   │
│  │                                                      │   │
│  │  CbCR Revenue:    [________________] €              │   │
│  │                   (From CbCR Table 1)                │   │
│  │                                                      │   │
│  │  CbCR Profit      [________________] €              │   │
│  │  Before Tax:      (Can be negative for losses)       │   │
│  │                                                      │   │
│  │  Simplified       [________________] €              │   │
│  │  Covered Taxes:   (From CbCR, adjusted)              │   │
│  │                                                      │   │
│  │  SBIE Amount:     [________________] €              │   │
│  │                   (For Routine Profits test)         │   │
│  │                                                      │   │
│  │  [  Check Safe Harbour  ]    [  Clear  ]            │   │
│  │                                                      │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │ RESULTS SECTION                                      │   │
│  ├─────────────────────────────────────────────────────┤   │
│  │                                                      │   │
│  │  ┌─────────────────────────────────────────────┐    │   │
│  │  │          SAFE HARBOUR APPLIES               │    │   │
│  │  │     ✓ Jurisdiction qualifies via            │    │   │
│  │  │       Simplified ETR Test                   │    │   │
│  │  └─────────────────────────────────────────────┘    │   │
│  │                                                      │   │
│  │  TEST RESULTS                                       │   │
│  │  ┌─────────────────────────────────────────────┐    │   │
│  │  │                                             │    │   │
│  │  │  ┌─────────┐ DE MINIMIS TEST               │    │   │
│  │  │  │  FAIL   │ Revenue €320M ≥ €10M          │    │   │
│  │  │  └─────────┘ Profit €48M ≥ €1M             │    │   │
│  │  │                                             │    │   │
│  │  │  ┌─────────┐ SIMPLIFIED ETR TEST           │    │   │
│  │  │  │  PASS   │ ETR: 23.00%                   │    │   │
│  │  │  └─────────┘ Threshold: 15% (FY2024)       │    │   │
│  │  │              23.00% ≥ 15% ✓                │    │   │
│  │  │                                             │    │   │
│  │  │  ┌─────────┐ ROUTINE PROFITS TEST          │    │   │
│  │  │  │  FAIL   │ Profit: €48M                  │    │   │
│  │  │  └─────────┘ SBIE: €15M                    │    │   │
│  │  │              €48M > €15M ✗                 │    │   │
│  │  │                                             │    │   │
│  │  └─────────────────────────────────────────────┘    │   │
│  │                                                      │   │
│  │  RECOMMENDATION                                     │   │
│  │  ┌─────────────────────────────────────────────┐    │   │
│  │  │ This jurisdiction qualifies for the         │    │   │
│  │  │ Transitional CbCR Safe Harbour.             │    │   │
│  │  │                                             │    │   │
│  │  │ Action: Elect safe harbour treatment.       │    │   │
│  │  │ Result: Top-up Tax = ZERO                   │    │   │
│  │  └─────────────────────────────────────────────┘    │   │
│  │                                                      │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### 6.2 Dynamic Threshold Display

When user selects fiscal year, immediately display the applicable ETR threshold:

| Year Selected | Display Text |
|---------------|--------------|
| FY 2024 | "ETR Threshold: 15%" |
| FY 2025 | "ETR Threshold: 16%" |
| FY 2026 | "ETR Threshold: 17%" |

### 6.3 Visual Status Indicators

**Test Result Badges:**
| Result | Color | Icon |
|--------|-------|------|
| PASS | Green (#28A745) | ✓ |
| FAIL | Red (#DC3545) | ✗ |
| N/A | Grey (#6C757D) | — |

**Overall Status Banner:**
| Status | Color | Size |
|--------|-------|------|
| QUALIFIES | Green (#28A745) | Large, prominent |
| NOT_QUALIFIED | Red (#DC3545) | Large, prominent |

### 6.4 Button Specifications

**Check Safe Harbour Button:**
| Property | Value |
|----------|-------|
| Label | "Check Safe Harbour" |
| Type | Primary |
| Color | Blue (#007BFF) |
| Behavior | Validates inputs, runs all three tests, displays results |

**Clear Button:**
| Property | Value |
|----------|-------|
| Label | "Clear" |
| Type | Secondary |
| Color | Grey (#6C757D) |
| Behavior | Clears all inputs and results |

### 6.5 Responsive Behavior

| Viewport | Layout |
|----------|--------|
| Desktop (>992px) | Side-by-side input/results |
| Tablet (768-992px) | Stacked panels |
| Mobile (<768px) | Single column, tests collapsed |

---

## 7. User Flow

### 7.1 Happy Path Flow

```
Step 1: User navigates to Safe Harbour Qualification Tool
        → Page loads with FY 2024 selected (threshold 15%)
        → Empty input fields displayed

Step 2: User selects Fiscal Year (if different)
        → ETR threshold display updates

Step 3: User enters Jurisdiction Name
        → e.g., "United Kingdom"

Step 4: User enters CbCR data
        → CbCR Revenue (from CbCR report)
        → CbCR Profit Before Tax
        → Simplified Covered Taxes

Step 5: User enters SBIE Amount
        → From GIR-002 or estimated

Step 6: User clicks "Check Safe Harbour"
        → System validates all inputs
        → All three tests are evaluated
        → Results display with PASS/FAIL for each
        → Overall status banner shows
        → Recommendation panel appears

Step 7: User reviews results
        → Understands which test(s) passed/failed
        → Notes recommendation for filing
```

### 7.2 Qualification Scenarios

```
Scenario A: Large profitable jurisdiction with high ETR
─────────────────────────────────────────────────────
Revenue: €500M, Profit: €80M, Taxes: €20M, SBIE: €5M

De Minimis:      FAIL (revenue and profit too high)
Simplified ETR:  PASS (25% ≥ 15%)
Routine Profits: FAIL (profit > SBIE)

Result: QUALIFIES via Simplified ETR Test


Scenario B: Small loss-making jurisdiction
─────────────────────────────────────────────────────
Revenue: €5M, Profit: -€1M, Taxes: €0, SBIE: €0.5M

De Minimis:      PASS (revenue < €10M, loss < €1M)
Simplified ETR:  N/A (no positive profit)
Routine Profits: PASS (no positive profit)

Result: QUALIFIES via De Minimis Test (and Routine Profits)


Scenario C: Low-taxed jurisdiction
─────────────────────────────────────────────────────
Revenue: €100M, Profit: €30M, Taxes: €3M, SBIE: €5M

De Minimis:      FAIL (revenue too high)
Simplified ETR:  FAIL (10% < 15%)
Routine Profits: FAIL (€30M > €5M)

Result: NOT QUALIFIED - Full GloBE calculation required
```

---

## 8. Edge Cases & Error Handling

### 8.1 Edge Cases

| Scenario | Inputs | Expected Behavior |
|----------|--------|-------------------|
| Zero revenue and profit | Revenue=0, Profit=0 | De Minimis: PASS, ETR: N/A, Routine: PASS → QUALIFIES |
| Negative profit (loss) | Profit < 0 | ETR: N/A, Routine: PASS (auto), De Minimis: check revenue |
| ETR exactly at threshold | ETR = 15.00% (FY2024) | PASS (≥ threshold includes equals) |
| ETR just below threshold | ETR = 14.99% | FAIL |
| Profit equals SBIE exactly | Profit = SBIE | Routine Profits: PASS (≤ includes equals) |
| Zero taxes, positive profit | Taxes=0, Profit>0 | ETR = 0%, FAIL Simplified ETR |
| Very large numbers | Revenue = €500B | Calculate normally, no overflow |
| All tests fail | All conditions fail | NOT_QUALIFIED, show recommendation |

### 8.2 Special Display Cases

| Scenario | Display Behavior |
|----------|------------------|
| Multiple tests pass | Highlight all passing tests, note primary qualifier |
| Negative profit | Show N/A for ETR with explanation |
| Exactly at threshold | Show "≥" symbol to clarify equals case |

### 8.3 Error Messages

| Error Code | Trigger | User Message |
|------------|---------|--------------|
| ERR_001 | Fiscal year not selected | "Please select a fiscal year" |
| ERR_002 | Jurisdiction empty | "Jurisdiction is required" |
| ERR_003 | Revenue empty | "CbCR Revenue is required" |
| ERR_004 | Revenue negative | "CbCR Revenue cannot be negative" |
| ERR_005 | Profit empty | "CbCR Profit Before Tax is required" |
| ERR_006 | Taxes empty | "Simplified Covered Taxes is required" |
| ERR_007 | Taxes negative | "Simplified Covered Taxes cannot be negative" |
| ERR_008 | SBIE empty | "SBIE Amount is required" |
| ERR_009 | SBIE negative | "SBIE Amount cannot be negative" |

---

## 9. Test Cases

### 9.1 Functional Test Cases

| Test ID | Description | Inputs | Expected Output | Source |
|---------|-------------|--------|-----------------|--------|
| TC-001 | UK qualifies via ETR | FY:2024, Rev:320M, Profit:48M, Taxes:11.04M, SBIE:15M | De Minimis:FAIL, ETR:PASS(23%), Routine:FAIL, Overall:QUALIFIES | Case Study 1 |
| TC-002 | Small jurisdiction - De Minimis | FY:2024, Rev:5M, Profit:0.5M, Taxes:0.1M, SBIE:0.2M | De Minimis:PASS, Overall:QUALIFIES | Edge case |
| TC-003 | Loss jurisdiction | FY:2024, Rev:50M, Profit:-5M, Taxes:0, SBIE:1M | De Minimis:FAIL, ETR:N/A, Routine:PASS, Overall:QUALIFIES | Edge case |
| TC-004 | Low-tax fails all | FY:2024, Rev:100M, Profit:30M, Taxes:3M, SBIE:5M | All FAIL, Overall:NOT_QUALIFIED | Edge case |
| TC-005 | Routine profits pass | FY:2024, Rev:50M, Profit:3M, Taxes:0.3M, SBIE:5M | De Minimis:FAIL, ETR:FAIL(10%), Routine:PASS, Overall:QUALIFIES | Edge case |
| TC-006 | FY2025 threshold | FY:2025, Rev:100M, Profit:50M, Taxes:8M, SBIE:10M | ETR:16%, Threshold:16%, PASS | Rate test |
| TC-007 | FY2026 threshold | FY:2026, Rev:100M, Profit:50M, Taxes:8M, SBIE:10M | ETR:16%, Threshold:17%, FAIL | Rate test |
| TC-008 | Boundary: ETR exactly 15% | FY:2024, Rev:100M, Profit:20M, Taxes:3M, SBIE:5M | ETR:15.00%, PASS (equals threshold) | Boundary |

### 9.2 Threshold Test Cases

| Test ID | Fiscal Year | ETR | Threshold | Expected Result |
|---------|-------------|-----|-----------|-----------------|
| TH-001 | 2024 | 14.99% | 15% | FAIL |
| TH-002 | 2024 | 15.00% | 15% | PASS |
| TH-003 | 2024 | 15.01% | 15% | PASS |
| TH-004 | 2025 | 15.99% | 16% | FAIL |
| TH-005 | 2025 | 16.00% | 16% | PASS |
| TH-006 | 2026 | 16.99% | 17% | FAIL |
| TH-007 | 2026 | 17.00% | 17% | PASS |

### 9.3 De Minimis Boundary Tests

| Test ID | Revenue | Profit | Expected |
|---------|---------|--------|----------|
| DM-001 | €9,999,999 | €999,999 | PASS |
| DM-002 | €10,000,000 | €999,999 | FAIL (revenue at threshold) |
| DM-003 | €9,999,999 | €1,000,000 | FAIL (profit at threshold) |
| DM-004 | €10,000,000 | €1,000,000 | FAIL (both at threshold) |

### 9.4 Validation Test Cases

| Test ID | Description | Input | Expected Result |
|---------|-------------|-------|-----------------|
| VT-001 | Empty jurisdiction | jurisdiction = "" | ERR_002 displayed |
| VT-002 | Negative revenue | revenue = -1000 | ERR_004 displayed |
| VT-003 | Empty taxes | taxes = "" | ERR_006 displayed |
| VT-004 | Negative SBIE | sbie = -500 | ERR_009 displayed |
| VT-005 | Valid negative profit | profit = -5000000 | Accepted, ETR shows N/A |

---

## 10. Accessibility Requirements

| Requirement | Implementation |
|-------------|----------------|
| Keyboard navigation | All inputs accessible via Tab key |
| Screen reader | ARIA labels on all fields, test results announced |
| Color contrast | Minimum 4.5:1 for text |
| Status communication | Pass/Fail communicated via text AND color |
| Focus indicator | Visible focus ring on all elements |

---

## 11. Technical Notes

### 11.1 Dependencies
- No external APIs required
- All calculations performed client-side
- No data persistence required

### 11.2 Performance
- All three tests run in <100ms
- No network requests during calculation

### 11.3 Browser Support
- Chrome (latest 2 versions)
- Firefox (latest 2 versions)
- Safari (latest 2 versions)
- Edge (latest 2 versions)

### 11.4 Currency Considerations
- De Minimis thresholds are EUR-denominated
- If different currency selected, note that thresholds are EUR-equivalent
- No automatic currency conversion (user responsibility)

---

## 12. Limitations & Scope

This demo tool does **NOT**:
- Validate that CbCR data comes from a "Qualified CbCR" per guidance
- Check CbCR filing status or availability
- Handle Permanent CbCR Safe Harbour (different from Transitional)
- Handle QDMTT Safe Harbour (separate concept)
- Validate jurisdiction-specific requirements
- Consider group-level elections or consolidation
- Connect to any tax authority or CbCR database
- Store election records
- Generate GIR filing documentation

This tool is for **learning purposes only** to understand safe harbour qualification assessment.

---

## 13. Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2024-12-07 | Initial specification |

---

## 14. Appendix: Case Study Alignment

### Case Study 1: GlobalTech Manufacturing

**UK Safe Harbour Test:**
- Sample Data Location: `Appendices/Case_Study_1_GlobalTech_First_Filing/Sample_Data.md`
- Inputs:
  - Fiscal Year: 2024
  - Jurisdiction: United Kingdom
  - CbCR Revenue: €320,000,000
  - CbCR Profit Before Tax: €48,000,000
  - Simplified Covered Taxes: €11,040,000
  - SBIE Amount: €15,000,000
- Expected Outputs:
  - De Minimis Test: FAIL (revenue and profit exceed thresholds)
  - Simplified ETR Test: PASS (€11,040,000 ÷ €48,000,000 = 23% ≥ 15%)
  - Routine Profits Test: FAIL (€48M > €15M)
  - Overall: QUALIFIES (via Simplified ETR Test)
  - Recommendation: Full GloBE calculation NOT required for UK

---

## 15. Appendix: ETR Threshold Transition Schedule

Per OECD Administrative Guidance (December 2023):

| Fiscal Year | Simplified ETR Threshold | Notes |
|-------------|-------------------------|-------|
| FY beginning on/after 31 Dec 2023 (2024) | 15% | First year of safe harbour |
| FY beginning on/after 31 Dec 2024 (2025) | 16% | Threshold increases |
| FY beginning on/after 31 Dec 2025 (2026) | 17% | Final year of transitional safe harbour |
| FY beginning on/after 31 Dec 2026 (2027+) | N/A | Transitional safe harbour expires |

**Note:** After FY 2026, the Transitional CbCR Safe Harbour is no longer available. MNE groups must perform full GloBE calculations or rely on other relief mechanisms (e.g., QDMTT Safe Harbour, Permanent Safe Harbour when implemented).

---

## 16. Appendix: Safe Harbour Decision Tree

```
START: Assess jurisdiction for Safe Harbour
              │
              ▼
    ┌─────────────────────┐
    │ Is FY 2024-2026?    │
    └─────────────────────┘
              │
       ┌──────┴──────┐
       │ NO          │ YES
       ▼             ▼
  ┌─────────┐   ┌─────────────────────────────────┐
  │ Safe    │   │ Check De Minimis Test           │
  │ Harbour │   │ Revenue <€10M AND Profit <€1M?  │
  │ NOT     │   └─────────────────────────────────┘
  │ Available│            │
  └─────────┘      ┌──────┴──────┐
                   │ YES         │ NO
                   ▼             ▼
              ┌─────────┐   ┌─────────────────────────────────┐
              │ PASS    │   │ Check Simplified ETR Test       │
              │ Safe    │   │ Simplified ETR ≥ Threshold?     │
              │ Harbour │   └─────────────────────────────────┘
              │ APPLIES │            │
              └─────────┘     ┌──────┴──────┐
                              │ YES         │ NO
                              ▼             ▼
                         ┌─────────┐   ┌─────────────────────────────────┐
                         │ PASS    │   │ Check Routine Profits Test      │
                         │ Safe    │   │ Profit ≤ SBIE?                  │
                         │ Harbour │   └─────────────────────────────────┘
                         │ APPLIES │            │
                         └─────────┘     ┌──────┴──────┐
                                         │ YES         │ NO
                                         ▼             ▼
                                    ┌─────────┐   ┌─────────────┐
                                    │ PASS    │   │ FAIL        │
                                    │ Safe    │   │ Full GloBE  │
                                    │ Harbour │   │ Calculation │
                                    │ APPLIES │   │ Required    │
                                    └─────────┘   └─────────────┘
```
