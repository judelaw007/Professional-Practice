# GIR-003: Top-Up Tax Calculator - Tool Specification

**Version:** 1.0
**Last Updated:** 2024-12-07
**Status:** Planned
**Platform:** tools.mojitax.com

---

## 1. Tool Metadata

| Field | Value |
|-------|-------|
| Tool ID | GIR-003 |
| Tool Name | GIR Top-Up Tax Calculator |
| Category | Pillar Two |
| Form Type | Calculator |
| Status | Planned |
| Used By | GloBE Information Return: Complete Filing Implementation |
| Introduced In | Section 2.4 - Top-Up Tax Calculation |
| Related Tools | GIR-001 (ETR Calculator), GIR-002 (SBIE Calculator) |

---

## 2. Purpose & Learning Objective

### 2.1 Purpose
Practice the complete Top-up Tax calculation for a jurisdiction by combining the Effective Tax Rate (ETR) and Substance-Based Income Exclusion (SBIE) to determine the Top-up Tax amount. This tool demonstrates how all GloBE calculation components work together to arrive at the final tax liability.

### 2.2 Learning Objective
After using this tool, learners will be able to:
- Calculate Excess Profit by subtracting SBIE from GloBE Income
- Apply the Top-up Tax Percentage to Excess Profit
- Understand how QDMTT reduces the IIR/UTPR liability
- Follow the complete calculation flow from GloBE Income to Net Top-up Tax
- Recognize how the three calculation tools (GIR-001, GIR-002, GIR-003) connect

### 2.3 Prerequisites
Learners should have completed:
- GIR-001: ETR Calculator (understanding ETR calculation)
- GIR-002: SBIE Calculator (understanding substance exclusion)
- Section 2.4 content on Top-up Tax mechanics

### 2.4 Calculation Flow Context

```
┌─────────────────────┐     ┌─────────────────────┐
│  GIR-001            │     │  GIR-002            │
│  ETR Calculator     │     │  SBIE Calculator    │
│  ─────────────────  │     │  ─────────────────  │
│  Inputs:            │     │  Inputs:            │
│  • GloBE Income     │     │  • Fiscal Year      │
│  • Covered Taxes    │     │  • Payroll          │
│                     │     │  • Assets           │
│  Outputs:           │     │                     │
│  • ETR %            │     │  Outputs:           │
│  • Top-up Tax %     │     │  • Total SBIE       │
└──────────┬──────────┘     └──────────┬──────────┘
           │                           │
           └─────────────┬─────────────┘
                         │
                         ▼
           ┌─────────────────────────┐
           │  GIR-003                │
           │  Top-Up Tax Calculator  │
           │  ───────────────────────│
           │  Inputs:                │
           │  • GloBE Income         │
           │  • Covered Taxes        │
           │  • Total SBIE           │
           │  • QDMTT Amount         │
           │                         │
           │  Outputs:               │
           │  • ETR %                │
           │  • Top-up Tax %         │
           │  • Excess Profit        │
           │  • Gross Top-up Tax     │
           │  • Net Top-up Tax       │
           └─────────────────────────┘
```

---

## 3. Input Fields

### 3.1 GloBE Income

| Property | Value |
|----------|-------|
| Field ID | `globe_income` |
| Label | GloBE Income |
| Data Type | Decimal number |
| Required | **Yes** |
| Precision | 2 decimal places |
| Min Value | 0.01 |
| Max Value | 999,999,999,999.99 |
| Default Value | Empty (no default) |
| UI Element | Currency input field with thousand separators |
| Placeholder Text | "Enter GloBE Income amount" |
| Help Text | "The net GloBE Income for the jurisdiction after all adjustments. Use the same value from GIR-001 ETR Calculator." |

**Validation Rules:**
| Rule | Condition | Error Message |
|------|-----------|---------------|
| Required | Field is empty | "GloBE Income is required" |
| Positive | Value <= 0 | "GloBE Income must be greater than zero" |
| Numeric | Non-numeric input | "Please enter a valid number" |
| Max exceeded | Value > max | "Value exceeds maximum allowed" |

---

### 3.2 Adjusted Covered Taxes

| Property | Value |
|----------|-------|
| Field ID | `covered_taxes` |
| Label | Adjusted Covered Taxes |
| Data Type | Decimal number |
| Required | **Yes** |
| Precision | 2 decimal places |
| Min Value | 0.00 |
| Max Value | 999,999,999,999.99 |
| Default Value | Empty (no default) |
| UI Element | Currency input field with thousand separators |
| Placeholder Text | "Enter Adjusted Covered Taxes" |
| Help Text | "Total Adjusted Covered Taxes for the jurisdiction. Use the same value from GIR-001 ETR Calculator." |

**Validation Rules:**
| Rule | Condition | Error Message |
|------|-----------|---------------|
| Required | Field is empty | "Adjusted Covered Taxes is required" |
| Non-negative | Value < 0 | "Adjusted Covered Taxes cannot be negative" |
| Numeric | Non-numeric input | "Please enter a valid number" |
| Max exceeded | Value > max | "Value exceeds maximum allowed" |

---

### 3.3 Total SBIE

| Property | Value |
|----------|-------|
| Field ID | `total_sbie` |
| Label | Total SBIE |
| Data Type | Decimal number |
| Required | **Yes** |
| Precision | 2 decimal places |
| Min Value | 0.00 |
| Max Value | 999,999,999,999.99 |
| Default Value | Empty (no default) |
| UI Element | Currency input field with thousand separators |
| Placeholder Text | "Enter Total SBIE from GIR-002" |
| Help Text | "The Total Substance-Based Income Exclusion calculated using GIR-002 SBIE Calculator (Payroll SBIE + Asset SBIE)." |

**Validation Rules:**
| Rule | Condition | Error Message |
|------|-----------|---------------|
| Required | Field is empty | "Total SBIE is required" |
| Non-negative | Value < 0 | "Total SBIE cannot be negative" |
| Numeric | Non-numeric input | "Please enter a valid number" |
| Max exceeded | Value > max | "Value exceeds maximum allowed" |

**Cross-Validation:**
| Rule | Condition | Warning Message |
|------|-----------|-----------------|
| SBIE > GloBE Income | total_sbie > globe_income | "Warning: SBIE exceeds GloBE Income. Excess Profit will be zero." |

---

### 3.4 QDMTT Amount

| Property | Value |
|----------|-------|
| Field ID | `qdmtt_amount` |
| Label | QDMTT Amount |
| Data Type | Decimal number |
| Required | **No** (Optional) |
| Precision | 2 decimal places |
| Min Value | 0.00 |
| Max Value | 999,999,999,999.99 |
| Default Value | 0 |
| UI Element | Currency input field with thousand separators |
| Placeholder Text | "Enter QDMTT amount (if applicable)" |
| Help Text | "Enter the Qualified Domestic Minimum Top-up Tax amount if the jurisdiction has enacted a QDMTT. Leave blank or enter 0 if not applicable." |

**Validation Rules:**
| Rule | Condition | Error Message |
|------|-----------|---------------|
| Non-negative | Value < 0 | "QDMTT Amount cannot be negative" |
| Numeric | Non-numeric input | "Please enter a valid number" |
| Max exceeded | Value > max | "Value exceeds maximum allowed" |

**Cross-Validation:**
| Rule | Condition | Warning Message |
|------|-----------|-----------------|
| QDMTT > Gross Top-up | qdmtt > gross_topup | "Warning: QDMTT exceeds Gross Top-up Tax. Check your inputs." |

**QDMTT Explanation (for tooltip):**
A Qualified Domestic Minimum Top-up Tax (QDMTT) is a domestic minimum tax enacted by a jurisdiction that meets GloBE requirements. When a jurisdiction has a QDMTT, the QDMTT amount offsets the IIR/UTPR liability, as the jurisdiction has already collected the top-up tax domestically.

---

### 3.5 Currency

| Property | Value |
|----------|-------|
| Field ID | `currency` |
| Label | Currency |
| Data Type | String (dropdown selection) |
| Required | **Yes** |
| Default Value | EUR |
| UI Element | Dropdown select |
| Help Text | "Select the currency for display purposes. All inputs must be in the same currency." |

**Dropdown Options:**
| Code | Display | Symbol |
|------|---------|--------|
| EUR | Euro (EUR) | € |
| USD | US Dollar (USD) | $ |
| GBP | British Pound (GBP) | £ |
| CHF | Swiss Franc (CHF) | CHF |

---

### 3.6 Jurisdiction Name (Optional)

| Property | Value |
|----------|-------|
| Field ID | `jurisdiction_name` |
| Label | Jurisdiction Name |
| Data Type | String |
| Required | **No** |
| Max Length | 100 characters |
| Default Value | Empty |
| UI Element | Text input field |
| Placeholder Text | "e.g., Ireland, Switzerland" |
| Help Text | "Optional: Enter jurisdiction name for reference in results" |

---

## 4. Output Fields

### 4.1 Jurisdictional ETR

| Property | Value |
|----------|-------|
| Field ID | `etr_percentage` |
| Label | Jurisdictional ETR |
| Data Type | Percentage |
| Precision | 2 decimal places |
| Display Format | "XX.XX%" |
| UI Element | Read-only text |

---

### 4.2 Top-up Tax Percentage

| Property | Value |
|----------|-------|
| Field ID | `topup_percentage` |
| Label | Top-up Tax Percentage |
| Data Type | Percentage |
| Precision | 2 decimal places |
| Display Format | "X.XX%" |
| UI Element | Read-only text |

---

### 4.3 Status Indicator

| Property | Value |
|----------|-------|
| Field ID | `status` |
| Label | Status |
| Data Type | String (enumerated) |
| UI Element | Badge/pill with background color |

**Status Values:**
| Status | Condition | Display Text | Background Color |
|--------|-----------|--------------|------------------|
| LOW_TAXED | ETR < 15% AND Net Top-up > 0 | "Top-up Tax Applies" | Red (#DC3545) |
| COMPLIANT | ETR >= 15% | "Compliant - No Top-up Tax" | Green (#28A745) |
| QDMTT_OFFSET | ETR < 15% AND Net Top-up = 0 (due to QDMTT) | "Offset by QDMTT" | Blue (#007BFF) |
| NO_EXCESS | ETR < 15% AND Excess Profit <= 0 | "No Excess Profit" | Grey (#6C757D) |

---

### 4.4 Excess Profit

| Property | Value |
|----------|-------|
| Field ID | `excess_profit` |
| Label | Excess Profit |
| Data Type | Currency |
| Precision | 0 decimal places |
| Display Format | Currency symbol + formatted number |
| UI Element | Read-only text |

**Display Note:** If Excess Profit is zero or negative, display "€0" with explanatory note.

---

### 4.5 Gross Top-up Tax

| Property | Value |
|----------|-------|
| Field ID | `gross_topup_tax` |
| Label | Gross Top-up Tax |
| Data Type | Currency |
| Precision | 0 decimal places |
| Display Format | Currency symbol + formatted number |
| UI Element | Read-only text |

---

### 4.6 QDMTT Offset

| Property | Value |
|----------|-------|
| Field ID | `qdmtt_offset` |
| Label | QDMTT Offset |
| Data Type | Currency |
| Precision | 0 decimal places |
| Display Format | "(" + Currency symbol + formatted number + ")" |
| UI Element | Read-only text (shown in parentheses to indicate reduction) |

**Display Note:** Only displayed if QDMTT > 0. Shows as negative/offset value.

---

### 4.7 Net Top-up Tax (IIR/UTPR)

| Property | Value |
|----------|-------|
| Field ID | `net_topup_tax` |
| Label | Net Top-up Tax (IIR/UTPR) |
| Data Type | Currency |
| Precision | 0 decimal places |
| Display Format | Currency symbol + formatted number |
| UI Element | Read-only text with large font, highlighted/emphasized |

**Display Note:** This is the amount subject to IIR or UTPR collection by the parent jurisdiction. Cannot be negative (minimum is 0).

---

### 4.8 Calculation Breakdown

| Property | Value |
|----------|-------|
| Field ID | `calculation_breakdown` |
| Label | Calculation Breakdown |
| Data Type | Formatted text block |
| UI Element | Card/panel with monospace font |

**Display Format:**
```
TOP-UP TAX CALCULATION FOR {jurisdiction_name}
═══════════════════════════════════════════════════════════

STEP 1: CALCULATE ETR
─────────────────────────────────────
Adjusted Covered Taxes:     {covered_taxes}
GloBE Income:               {globe_income}
ETR = {covered_taxes} ÷ {globe_income} × 100
ETR = {etr_percentage}%

STEP 2: DETERMINE TOP-UP TAX PERCENTAGE
─────────────────────────────────────
Minimum Rate:               15.00%
Jurisdictional ETR:         {etr_percentage}%
Top-up Tax % = 15.00% - {etr_percentage}%
Top-up Tax % = {topup_percentage}%

STEP 3: CALCULATE EXCESS PROFIT
─────────────────────────────────────
GloBE Income:               {globe_income}
Less: Total SBIE:           ({total_sbie})
                            ─────────────
Excess Profit:              {excess_profit}

STEP 4: CALCULATE GROSS TOP-UP TAX
─────────────────────────────────────
Excess Profit:              {excess_profit}
Top-up Tax %:               {topup_percentage}%
Gross Top-up Tax = {excess_profit} × {topup_percentage}%
Gross Top-up Tax = {gross_topup_tax}

STEP 5: APPLY QDMTT OFFSET
─────────────────────────────────────
Gross Top-up Tax:           {gross_topup_tax}
Less: QDMTT Amount:         ({qdmtt_offset})
                            ─────────────
Net Top-up Tax (IIR/UTPR):  {net_topup_tax}
```

---

## 5. Calculation Logic

### 5.1 Primary Calculation

```
FUNCTION CalculateTopUpTax(globe_income, covered_taxes, total_sbie, qdmtt_amount):

    // Validate inputs
    IF globe_income <= 0 THEN
        RETURN Error("GloBE Income must be greater than zero")
    END IF

    IF covered_taxes < 0 THEN
        RETURN Error("Adjusted Covered Taxes cannot be negative")
    END IF

    IF total_sbie < 0 THEN
        RETURN Error("Total SBIE cannot be negative")
    END IF

    IF qdmtt_amount < 0 THEN
        RETURN Error("QDMTT Amount cannot be negative")
    END IF

    // Default QDMTT to 0 if not provided
    IF qdmtt_amount IS NULL THEN
        qdmtt_amount = 0
    END IF

    // STEP 1: Calculate ETR
    etr_decimal = covered_taxes / globe_income
    etr_percentage = ROUND(etr_decimal × 100, 2)

    // STEP 2: Calculate Top-up Tax Percentage
    IF etr_percentage >= 15.00 THEN
        topup_percentage = 0.00
        status = "COMPLIANT"
    ELSE
        topup_percentage = ROUND(15.00 - etr_percentage, 2)
    END IF

    // STEP 3: Calculate Excess Profit
    excess_profit = globe_income - total_sbie
    IF excess_profit < 0 THEN
        excess_profit = 0
    END IF
    excess_profit = ROUND(excess_profit, 0)

    // STEP 4: Calculate Gross Top-up Tax
    gross_topup_tax = excess_profit × (topup_percentage / 100)
    gross_topup_tax = ROUND(gross_topup_tax, 0)

    // STEP 5: Apply QDMTT Offset
    qdmtt_offset = MIN(qdmtt_amount, gross_topup_tax)
    qdmtt_offset = ROUND(qdmtt_offset, 0)

    net_topup_tax = gross_topup_tax - qdmtt_offset
    IF net_topup_tax < 0 THEN
        net_topup_tax = 0
    END IF

    // Determine final status
    IF etr_percentage >= 15.00 THEN
        status = "COMPLIANT"
    ELSE IF excess_profit <= 0 THEN
        status = "NO_EXCESS"
    ELSE IF net_topup_tax = 0 AND qdmtt_offset > 0 THEN
        status = "QDMTT_OFFSET"
    ELSE
        status = "LOW_TAXED"
    END IF

    RETURN {
        etr_percentage: etr_percentage,
        topup_percentage: topup_percentage,
        excess_profit: excess_profit,
        gross_topup_tax: gross_topup_tax,
        qdmtt_offset: qdmtt_offset,
        net_topup_tax: net_topup_tax,
        status: status
    }

END FUNCTION
```

### 5.2 Rounding Rules

| Calculation | Rounding Method | Precision |
|-------------|-----------------|-----------|
| ETR Percentage | Standard (half-up) | 2 decimal places |
| Top-up Tax Percentage | Standard (half-up) | 2 decimal places |
| Excess Profit | Standard (half-up) | 0 decimal places (whole currency) |
| Gross Top-up Tax | Standard (half-up) | 0 decimal places (whole currency) |
| QDMTT Offset | Standard (half-up) | 0 decimal places (whole currency) |
| Net Top-up Tax | Standard (half-up) | 0 decimal places (whole currency) |

### 5.3 Formula Reference

| Formula | Article Reference |
|---------|-------------------|
| ETR = Adjusted Covered Taxes ÷ GloBE Income | GloBE Model Rules Article 5.1 |
| Top-up Tax % = 15% - ETR | GloBE Model Rules Article 5.2.1 |
| Excess Profit = GloBE Income - SBIE | GloBE Model Rules Article 5.2.3 |
| Top-up Tax = Excess Profit × Top-up Tax % | GloBE Model Rules Article 5.2.4 |
| QDMTT Offset | GloBE Model Rules Article 5.2.3(d) |

---

## 6. User Interface Specifications

### 6.1 Layout Structure

```
┌─────────────────────────────────────────────────────────────┐
│  GIR Top-Up Tax Calculator                             [?]  │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │ INPUT SECTION                                        │   │
│  ├─────────────────────────────────────────────────────┤   │
│  │                                                      │   │
│  │  Currency:        [EUR ▼]                           │   │
│  │                                                      │   │
│  │  GloBE Income:    [________________] €              │   │
│  │                   (Required - same as GIR-001)       │   │
│  │                                                      │   │
│  │  Adjusted Covered [________________] €              │   │
│  │  Taxes:           (Required - same as GIR-001)       │   │
│  │                                                      │   │
│  │  Total SBIE:      [________________] €              │   │
│  │                   (Required - from GIR-002)          │   │
│  │                                                      │   │
│  │  QDMTT Amount:    [________________] €              │   │
│  │                   (Optional - if jurisdiction has    │   │
│  │                    enacted QDMTT)                    │   │
│  │                                                      │   │
│  │  Jurisdiction:    [________________]                │   │
│  │                   (Optional - for reference)         │   │
│  │                                                      │   │
│  │  [  Calculate Top-Up Tax  ]    [  Clear  ]          │   │
│  │                                                      │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │ RESULTS SECTION                                      │   │
│  ├─────────────────────────────────────────────────────┤   │
│  │                                                      │   │
│  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐  │   │
│  │  │ ETR         │  │ Top-up %    │  │ Status      │  │   │
│  │  │  11.59%     │  │   3.41%     │  │ TOP-UP TAX  │  │   │
│  │  │             │  │             │  │  APPLIES    │  │   │
│  │  └─────────────┘  └─────────────┘  └─────────────┘  │   │
│  │                                                      │   │
│  │  CALCULATION SUMMARY                                │   │
│  │  ┌─────────────────────────────────────────────┐    │   │
│  │  │ GloBE Income              €32,800,000       │    │   │
│  │  │ Less: SBIE                (€3,188,000)      │    │   │
│  │  │                           ───────────       │    │   │
│  │  │ Excess Profit             €29,612,000       │    │   │
│  │  │                                             │    │   │
│  │  │ × Top-up Tax %            3.41%             │    │   │
│  │  │                           ───────────       │    │   │
│  │  │ Gross Top-up Tax          €1,009,769        │    │   │
│  │  │ Less: QDMTT Offset        (€0)              │    │   │
│  │  │                           ───────────       │    │   │
│  │  │ NET TOP-UP TAX (IIR)      €1,009,769        │    │   │
│  │  └─────────────────────────────────────────────┘    │   │
│  │                                                      │   │
│  │  [▼ Show detailed calculation breakdown]            │   │
│  │                                                      │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### 6.2 Summary Display vs Full Breakdown

**Default View:** Condensed calculation summary (as shown above)

**Expanded View:** Full 5-step calculation breakdown (Section 4.8)

### 6.3 Button Specifications

**Calculate Top-Up Tax Button:**
| Property | Value |
|----------|-------|
| Label | "Calculate Top-Up Tax" |
| Type | Primary |
| Color | Blue (#007BFF) |
| Behavior | Validates inputs, runs calculation, displays results |
| Disabled State | Greyed out if required fields empty |

**Clear Button:**
| Property | Value |
|----------|-------|
| Label | "Clear" |
| Type | Secondary |
| Color | Grey (#6C757D) |
| Behavior | Clears all input fields and results |

### 6.4 Visual Hierarchy

The results should emphasize:
1. **Primary:** Net Top-up Tax (IIR/UTPR) - largest font, highlighted
2. **Secondary:** ETR, Top-up %, Status - medium prominence
3. **Tertiary:** Calculation steps - standard font in breakdown panel

### 6.5 Responsive Behavior

| Viewport | Layout |
|----------|--------|
| Desktop (>992px) | Side-by-side input/results panels |
| Tablet (768-992px) | Stacked panels, full width |
| Mobile (<768px) | Single column, summary collapsed by default |

---

## 7. User Flow

### 7.1 Happy Path Flow

```
Step 1: User navigates to GIR Top-Up Tax Calculator
        → Page loads with empty input fields
        → Help text indicates relationship to GIR-001 and GIR-002
        → Results section shows placeholder

Step 2: User enters GloBE Income
        → Same value used in GIR-001

Step 3: User enters Adjusted Covered Taxes
        → Same value used in GIR-001

Step 4: User enters Total SBIE
        → Value from GIR-002 results

Step 5: User enters QDMTT Amount (if applicable)
        → Defaults to 0 if left empty
        → User enters amount if jurisdiction has QDMTT

Step 6: User clicks "Calculate Top-Up Tax"
        → System validates all inputs
        → IF validation passes:
            → Full calculation runs through all 5 steps
            → Summary displays with key metrics
            → Status badge shows appropriate color
            → Detailed breakdown available via toggle
        → IF validation fails:
            → Error messages display

Step 7: User reviews results
        → Can expand detailed breakdown
        → Can modify inputs and recalculate
        → Can click "Clear" to start over
```

### 7.2 Integrated Workflow (Recommended)

```
Complete Workflow:
1. Use GIR-001 to calculate ETR
   → Note: GloBE Income = €32,800,000
   → Note: Covered Taxes = €3,800,000
   → Result: ETR = 11.59%

2. Use GIR-002 to calculate SBIE
   → Input payroll and assets
   → Result: Total SBIE = €3,188,000

3. Use GIR-003 to calculate Top-up Tax
   → Enter GloBE Income from step 1
   → Enter Covered Taxes from step 1
   → Enter Total SBIE from step 2
   → Enter QDMTT if applicable
   → Result: Net Top-up Tax = €1,009,769
```

---

## 8. Edge Cases & Error Handling

### 8.1 Edge Cases

| Scenario | Inputs | Expected Behavior |
|----------|--------|-------------------|
| ETR exactly 15% | ETR = 15.00% | Top-up % = 0, Status = COMPLIANT, Net Tax = 0 |
| ETR above 15% | ETR = 25.00% | Top-up % = 0, Status = COMPLIANT, Net Tax = 0 |
| SBIE exceeds GloBE Income | SBIE > GloBE Income | Excess Profit = 0, Warning displayed, Status = NO_EXCESS |
| Zero SBIE | SBIE = 0 | Excess Profit = GloBE Income, calculate normally |
| QDMTT equals Gross Top-up | QDMTT = Gross | Net Tax = 0, Status = QDMTT_OFFSET |
| QDMTT exceeds Gross Top-up | QDMTT > Gross | Net Tax = 0, Warning displayed |
| Zero Covered Taxes | Taxes = 0 | ETR = 0%, Top-up % = 15%, calculate normally |
| Very small Top-up % | ETR = 14.99% | Top-up % = 0.01%, calculate normally |

### 8.2 Warning Messages (Non-blocking)

| Condition | Warning Message |
|-----------|-----------------|
| SBIE > GloBE Income | "SBIE exceeds GloBE Income. Excess Profit has been set to zero." |
| QDMTT > Gross Top-up | "QDMTT exceeds Gross Top-up Tax. Only the Gross Top-up amount will be offset." |
| ETR > 100% | "ETR exceeds 100%. Please verify your input values." |

### 8.3 Error Messages

| Error Code | Trigger | User Message |
|------------|---------|--------------|
| ERR_001 | GloBE Income empty | "GloBE Income is required" |
| ERR_002 | GloBE Income <= 0 | "GloBE Income must be greater than zero" |
| ERR_003 | GloBE Income non-numeric | "Please enter a valid number for GloBE Income" |
| ERR_004 | Covered Taxes empty | "Adjusted Covered Taxes is required" |
| ERR_005 | Covered Taxes < 0 | "Adjusted Covered Taxes cannot be negative" |
| ERR_006 | Covered Taxes non-numeric | "Please enter a valid number for Adjusted Covered Taxes" |
| ERR_007 | SBIE empty | "Total SBIE is required" |
| ERR_008 | SBIE < 0 | "Total SBIE cannot be negative" |
| ERR_009 | SBIE non-numeric | "Please enter a valid number for Total SBIE" |
| ERR_010 | QDMTT < 0 | "QDMTT Amount cannot be negative" |
| ERR_011 | QDMTT non-numeric | "Please enter a valid number for QDMTT Amount" |

---

## 9. Test Cases

### 9.1 Functional Test Cases

| Test ID | Description | Inputs | Expected Output | Source |
|---------|-------------|--------|-----------------|--------|
| TC-001 | Ireland - Full calculation | GloBE: 32,800,000, Taxes: 3,800,000, SBIE: 3,188,000, QDMTT: 0 | ETR: 11.59%, Top-up: 3.41%, Excess: 29,612,000, Gross: 1,009,769, Net: 1,009,769 | Case Study 1 |
| TC-002 | Switzerland - Full calculation | GloBE: 18,000,000, Taxes: 2,520,000, SBIE: 1,160,600, QDMTT: 0 | ETR: 14.00%, Top-up: 1.00%, Excess: 16,839,400, Gross: 168,394, Net: 168,394 | Case Study 1 |
| TC-003 | UK Compliant - No top-up | GloBE: 120,000,000, Taxes: 30,000,000, SBIE: any, QDMTT: 0 | ETR: 25.00%, Top-up: 0.00%, Net: 0, Status: COMPLIANT | Case Study 4 |
| TC-004 | With QDMTT offset | GloBE: 25,000,000, Taxes: 3,090,000, SBIE: 587,000, QDMTT: 500,000 | Gross: ~886,000, QDMTT Offset: 500,000, Net: ~386,000 | Case Study 4 |
| TC-005 | Full QDMTT offset | GloBE: 10,000,000, Taxes: 1,000,000, SBIE: 1,000,000, QDMTT: 1,000,000 | Gross: 450,000, QDMTT Offset: 450,000, Net: 0, Status: QDMTT_OFFSET | Edge case |
| TC-006 | SBIE exceeds income | GloBE: 10,000,000, Taxes: 1,000,000, SBIE: 15,000,000, QDMTT: 0 | Excess: 0, Gross: 0, Net: 0, Status: NO_EXCESS | Edge case |
| TC-007 | Zero SBIE | GloBE: 10,000,000, Taxes: 1,000,000, SBIE: 0, QDMTT: 0 | Excess: 10,000,000, calculate top-up on full amount | Edge case |
| TC-008 | Exactly 15% ETR | GloBE: 10,000,000, Taxes: 1,500,000, SBIE: 1,000,000, QDMTT: 0 | ETR: 15.00%, Top-up: 0.00%, Net: 0, Status: COMPLIANT | Boundary |

### 9.2 Calculation Verification Test Cases

| Test ID | Step | Calculation | Expected |
|---------|------|-------------|----------|
| CV-001 | ETR | 3,800,000 ÷ 32,800,000 × 100 | 11.59% |
| CV-002 | Top-up % | 15.00% - 11.59% | 3.41% |
| CV-003 | Excess Profit | 32,800,000 - 3,188,000 | 29,612,000 |
| CV-004 | Gross Top-up | 29,612,000 × 3.41% | 1,009,769 |
| CV-005 | Net Top-up | 1,009,769 - 0 | 1,009,769 |

### 9.3 Validation Test Cases

| Test ID | Description | Input | Expected Result |
|---------|-------------|-------|-----------------|
| VT-001 | Empty GloBE Income | globe_income = "" | ERR_001 displayed |
| VT-002 | Negative GloBE Income | globe_income = -1000 | ERR_002 displayed |
| VT-003 | Empty SBIE | total_sbie = "" | ERR_007 displayed |
| VT-004 | Negative QDMTT | qdmtt = -500 | ERR_010 displayed |
| VT-005 | All valid inputs | All positive values | Calculation runs |

### 9.4 UI/UX Test Cases

| Test ID | Description | Action | Expected Result |
|---------|-------------|--------|-----------------|
| UX-001 | Clear button | Click Clear after calculation | All fields cleared |
| UX-002 | Breakdown toggle | Click "Show detailed breakdown" | Full 5-step breakdown expands |
| UX-003 | Status badge - Low-taxed | ETR = 10% | Red badge "Top-up Tax Applies" |
| UX-004 | Status badge - Compliant | ETR = 20% | Green badge "Compliant" |
| UX-005 | Status badge - QDMTT | Net = 0 due to QDMTT | Blue badge "Offset by QDMTT" |

---

## 10. Accessibility Requirements

| Requirement | Implementation |
|-------------|----------------|
| Keyboard navigation | All inputs accessible via Tab key |
| Screen reader | ARIA labels on all form fields |
| Color contrast | Minimum 4.5:1 for text |
| Status colors | Status also communicated via text, not color alone |
| Error announcement | Errors announced to screen readers |
| Focus indicator | Visible focus ring on all interactive elements |

---

## 11. Technical Notes

### 11.1 Dependencies
- No external APIs required
- All calculations performed client-side
- No data persistence required
- Related tools: GIR-001, GIR-002 (values can be copied from those tools)

### 11.2 Performance
- Calculation should complete in <100ms
- No network requests during calculation

### 11.3 Browser Support
- Chrome (latest 2 versions)
- Firefox (latest 2 versions)
- Safari (latest 2 versions)
- Edge (latest 2 versions)

### 11.4 Potential Enhancement: Auto-population
Future enhancement could allow linking to GIR-001 and GIR-002 results to auto-populate shared fields. Not in scope for initial version.

---

## 12. Limitations & Scope

This demo tool does **NOT**:
- Calculate GloBE Income adjustments (user must input pre-calculated amount)
- Calculate Adjusted Covered Taxes from components
- Calculate SBIE (use GIR-002 for that)
- Handle allocation of Top-up Tax between parent entities (IIR allocation rules)
- Handle split between IIR and UTPR collection
- Process Additional Current Top-up Tax
- Handle prior period adjustments
- Handle recast or recapture scenarios
- Connect to any tax authority system
- Store or persist calculation history
- Generate actual GIR filings or XML

This tool is for **learning purposes only** to understand the complete Top-up Tax calculation flow.

---

## 13. Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2024-12-07 | Initial specification |

---

## 14. Appendix: Case Study Alignment

### Case Study 1: GlobalTech Manufacturing

**Ireland Scenario:**
- Sample Data Location: `Appendices/Case_Study_1_GlobalTech_First_Filing/Sample_Data.md`
- Inputs:
  - GloBE Income: €32,800,000
  - Adjusted Covered Taxes: €3,800,000
  - Total SBIE: €3,188,000 (from GIR-002)
  - QDMTT: €0
- Expected Outputs:
  - ETR: 11.59%
  - Top-up Tax %: 3.41%
  - Excess Profit: €29,612,000
  - Gross Top-up Tax: €1,009,769
  - Net Top-up Tax: €1,009,769
  - Status: Low-Taxed (RED)

**Switzerland Scenario:**
- Sample Data Location: `Appendices/Case_Study_1_GlobalTech_First_Filing/Sample_Data.md`
- Inputs:
  - GloBE Income: €18,000,000
  - Adjusted Covered Taxes: €2,520,000
  - Total SBIE: €1,160,600 (from GIR-002)
  - QDMTT: €0
- Expected Outputs:
  - ETR: 14.00%
  - Top-up Tax %: 1.00%
  - Excess Profit: €16,839,400
  - Gross Top-up Tax: €168,394
  - Net Top-up Tax: €168,394

### Case Study 4: Atlantic Manufacturing Group

**Netherlands Scenario (with QDMTT):**
- This case study demonstrates QDMTT offset scenarios
- Netherlands, Switzerland, and Ireland all have QDMTT regimes
- Use this case study to practice QDMTT offset calculations

---

## 15. Appendix: Calculation Flow Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│                     TOP-UP TAX CALCULATION                       │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│ STEP 1: Calculate ETR                                           │
│ ─────────────────────────────────────────────────────────────── │
│ ETR = Adjusted Covered Taxes ÷ GloBE Income × 100               │
│                                                                  │
│ IF ETR ≥ 15% → STOP: Jurisdiction is COMPLIANT                  │
│ IF ETR < 15% → CONTINUE to Step 2                               │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│ STEP 2: Calculate Top-up Tax Percentage                         │
│ ─────────────────────────────────────────────────────────────── │
│ Top-up Tax % = 15% - ETR                                        │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│ STEP 3: Calculate Excess Profit                                  │
│ ─────────────────────────────────────────────────────────────── │
│ Excess Profit = GloBE Income - SBIE                             │
│                                                                  │
│ IF Excess Profit ≤ 0 → STOP: No Top-up Tax (NO_EXCESS)          │
│ IF Excess Profit > 0 → CONTINUE to Step 4                       │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│ STEP 4: Calculate Gross Top-up Tax                               │
│ ─────────────────────────────────────────────────────────────── │
│ Gross Top-up Tax = Excess Profit × Top-up Tax %                 │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│ STEP 5: Apply QDMTT Offset                                       │
│ ─────────────────────────────────────────────────────────────── │
│ QDMTT Offset = MIN(QDMTT Amount, Gross Top-up Tax)              │
│ Net Top-up Tax = Gross Top-up Tax - QDMTT Offset                │
│                                                                  │
│ IF Net Top-up Tax = 0 AND QDMTT > 0 → Status: QDMTT_OFFSET     │
│ IF Net Top-up Tax > 0 → Status: LOW_TAXED (IIR/UTPR applies)   │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                         FINAL OUTPUT                             │
│ ─────────────────────────────────────────────────────────────── │
│ Net Top-up Tax = Amount subject to IIR or UTPR collection       │
└─────────────────────────────────────────────────────────────────┘
```
