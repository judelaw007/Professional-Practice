# GIR-002: SBIE Calculator - Tool Specification

**Version:** 1.0
**Last Updated:** 2024-12-07
**Status:** Planned
**Platform:** tools.mojitax.com

---

## 1. Tool Metadata

| Field | Value |
|-------|-------|
| Tool ID | GIR-002 |
| Tool Name | GIR SBIE Calculator |
| Category | Pillar Two |
| Form Type | Calculator |
| Status | Planned |
| Used By | GloBE Information Return: Complete Filing Implementation |
| Introduced In | Section 2.3 - Substance-Based Income Exclusion |

---

## 2. Purpose & Learning Objective

### 2.1 Purpose
Practice calculating the Substance-Based Income Exclusion (SBIE) for a jurisdiction under GloBE Rules. The SBIE reduces the amount of Excess Profit subject to Top-up Tax by providing carve-outs for payroll costs and tangible assets, recognizing that profits from genuine economic substance should not be subject to top-up taxation.

### 2.2 Learning Objective
After using this tool, learners will be able to:
- Calculate the payroll component of SBIE using the applicable carve-out rate
- Calculate the tangible asset component of SBIE using the applicable carve-out rate
- Apply the correct transitional rates based on fiscal year
- Understand how SBIE reduces Excess Profit subject to Top-up Tax
- Recognize the policy rationale behind substance-based exclusions

### 2.3 Prerequisites
Learners should understand:
- What constitutes Eligible Payroll Costs under GloBE Rules (Article 5.3.3)
- What constitutes Eligible Tangible Assets under GloBE Rules (Article 5.3.4)
- The transitional period and rate phase-down schedule
- How SBIE fits into the overall Top-up Tax calculation

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
| Default Value | Current year (2024) |
| Help Text | "Select the fiscal year for which you are calculating SBIE. The carve-out rates vary by year during the transition period." |

**Dropdown Options:**

| Value | Display Text | Payroll Rate | Asset Rate |
|-------|--------------|--------------|------------|
| 2024 | FY 2024 | 9.8% | 7.8% |
| 2025 | FY 2025 | 9.6% | 7.6% |
| 2026 | FY 2026 | 9.4% | 7.4% |
| 2027 | FY 2027 | 9.2% | 7.2% |
| 2028 | FY 2028 | 9.0% | 7.0% |
| 2029 | FY 2029 | 8.2% | 6.6% |
| 2030 | FY 2030 | 7.4% | 6.2% |
| 2031 | FY 2031 | 6.6% | 5.8% |
| 2032 | FY 2032 | 5.8% | 5.4% |
| 2033+ | FY 2033 onwards | 5.0% | 5.0% |

**Validation Rules:**
| Rule | Condition | Error Message |
|------|-----------|---------------|
| Required | No selection made | "Please select a fiscal year" |

**Technical Note:** The rates shown are from the GloBE Model Rules Article 9.1 transitional provisions. For fiscal years beginning on or after 31 December 2032, the permanent rates of 5% apply to both components.

---

### 3.2 Eligible Payroll Costs

| Property | Value |
|----------|-------|
| Field ID | `eligible_payroll` |
| Label | Eligible Payroll Costs |
| Data Type | Decimal number |
| Required | **Yes** |
| Precision | 2 decimal places |
| Min Value | 0.00 |
| Max Value | 999,999,999,999.99 |
| Default Value | Empty (no default) |
| UI Element | Currency input field with thousand separators |
| Placeholder Text | "Enter total eligible payroll costs" |
| Help Text | "Total eligible employee compensation costs for the jurisdiction, including wages, salaries, and eligible benefits for employees performing activities in the jurisdiction (Article 5.3.3)" |

**Validation Rules:**
| Rule | Condition | Error Message |
|------|-----------|---------------|
| Required | Field is empty | "Eligible Payroll Costs is required" |
| Non-negative | Value < 0 | "Eligible Payroll Costs cannot be negative" |
| Numeric | Non-numeric input | "Please enter a valid number" |
| Max exceeded | Value > max | "Value exceeds maximum allowed" |

**What Constitutes Eligible Payroll (for Help tooltip):**
- Wages and salaries paid to employees
- Payroll taxes and social security contributions
- Pension and retirement benefit contributions
- Share-based compensation (with limitations)
- Other employee benefits

**What is NOT Eligible:**
- Payments to independent contractors
- Capitalised payroll costs (already in tangible assets)
- Costs related to employees not performing activities in the jurisdiction

---

### 3.3 Eligible Tangible Assets (Net Book Value)

| Property | Value |
|----------|-------|
| Field ID | `eligible_assets` |
| Label | Eligible Tangible Assets (NBV) |
| Data Type | Decimal number |
| Required | **Yes** |
| Precision | 2 decimal places |
| Min Value | 0.00 |
| Max Value | 999,999,999,999.99 |
| Default Value | Empty (no default) |
| UI Element | Currency input field with thousand separators |
| Placeholder Text | "Enter net book value of eligible tangible assets" |
| Help Text | "Average net book value of eligible tangible assets located in the jurisdiction, calculated as the average of opening and closing balances (Article 5.3.4)" |

**Validation Rules:**
| Rule | Condition | Error Message |
|------|-----------|---------------|
| Required | Field is empty | "Eligible Tangible Assets is required" |
| Non-negative | Value < 0 | "Eligible Tangible Assets cannot be negative" |
| Numeric | Non-numeric input | "Please enter a valid number" |
| Max exceeded | Value > max | "Value exceeds maximum allowed" |

**What Constitutes Eligible Tangible Assets (for Help tooltip):**
- Property, plant and equipment located in the jurisdiction
- Natural resources located in the jurisdiction
- Right-of-use assets for leases of tangible assets in the jurisdiction

**What is NOT Eligible:**
- Intangible assets (patents, trademarks, goodwill)
- Financial assets
- Assets held for sale
- Assets not located in the jurisdiction

**Averaging Note:**
The net book value should be the average of:
- Opening balance at start of fiscal year
- Closing balance at end of fiscal year

For mid-year acquisitions, use: Average of (acquisition date value + year-end value)

---

### 3.4 Currency

| Property | Value |
|----------|-------|
| Field ID | `currency` |
| Label | Currency |
| Data Type | String (dropdown selection) |
| Required | **Yes** |
| Default Value | EUR |
| UI Element | Dropdown select |
| Help Text | "Select the currency for display purposes" |

**Dropdown Options:**
| Code | Display | Symbol |
|------|---------|--------|
| EUR | Euro (EUR) | € |
| USD | US Dollar (USD) | $ |
| GBP | British Pound (GBP) | £ |
| CHF | Swiss Franc (CHF) | CHF |

---

### 3.5 Jurisdiction Name (Optional)

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

**Validation Rules:**
| Rule | Condition | Error Message |
|------|-----------|---------------|
| Max length | Length > 100 | "Jurisdiction name cannot exceed 100 characters" |

---

## 4. Output Fields

### 4.1 Payroll Carve-out Rate

| Property | Value |
|----------|-------|
| Field ID | `payroll_rate` |
| Label | Payroll Carve-out Rate |
| Data Type | Percentage |
| Precision | 1 decimal place |
| Display Format | "X.X%" |
| UI Element | Read-only text |

**Display Note:** This is a looked-up value based on the selected fiscal year, displayed to show the user which rate was applied.

---

### 4.2 Payroll SBIE Amount

| Property | Value |
|----------|-------|
| Field ID | `payroll_sbie` |
| Label | Payroll SBIE Amount |
| Data Type | Currency |
| Precision | 0 decimal places (rounded) |
| Display Format | Currency symbol + formatted number |
| UI Element | Read-only text with large font |

---

### 4.3 Asset Carve-out Rate

| Property | Value |
|----------|-------|
| Field ID | `asset_rate` |
| Label | Asset Carve-out Rate |
| Data Type | Percentage |
| Precision | 1 decimal place |
| Display Format | "X.X%" |
| UI Element | Read-only text |

**Display Note:** This is a looked-up value based on the selected fiscal year, displayed to show the user which rate was applied.

---

### 4.4 Asset SBIE Amount

| Property | Value |
|----------|-------|
| Field ID | `asset_sbie` |
| Label | Asset SBIE Amount |
| Data Type | Currency |
| Precision | 0 decimal places (rounded) |
| Display Format | Currency symbol + formatted number |
| UI Element | Read-only text with large font |

---

### 4.5 Total SBIE

| Property | Value |
|----------|-------|
| Field ID | `total_sbie` |
| Label | Total SBIE |
| Data Type | Currency |
| Precision | 0 decimal places (rounded) |
| Display Format | Currency symbol + formatted number |
| UI Element | Read-only text with large font, highlighted/emphasized |

---

### 4.6 Calculation Breakdown

| Property | Value |
|----------|-------|
| Field ID | `calculation_breakdown` |
| Label | Calculation Breakdown |
| Data Type | Formatted text block |
| UI Element | Card/panel with monospace font |

**Display Format:**
```
SBIE Calculation for {jurisdiction_name} - FY{fiscal_year}
═══════════════════════════════════════════════════════════

PAYROLL COMPONENT
─────────────────────────────────────
Eligible Payroll Costs:     {eligible_payroll}
Carve-out Rate (FY{year}):  {payroll_rate}%
Payroll SBIE:               {eligible_payroll} × {payroll_rate}%
                          = {payroll_sbie}

TANGIBLE ASSET COMPONENT
─────────────────────────────────────
Eligible Tangible Assets:   {eligible_assets}
Carve-out Rate (FY{year}):  {asset_rate}%
Asset SBIE:                 {eligible_assets} × {asset_rate}%
                          = {asset_sbie}

TOTAL SBIE
─────────────────────────────────────
Payroll SBIE:               {payroll_sbie}
Asset SBIE:                 {asset_sbie}
                            ─────────────
Total SBIE:                 {total_sbie}
```

---

## 5. Calculation Logic

### 5.1 Rate Lookup Table

```
CONSTANT SBIE_RATES = {
    2024: { payroll: 0.098, asset: 0.078 },
    2025: { payroll: 0.096, asset: 0.076 },
    2026: { payroll: 0.094, asset: 0.074 },
    2027: { payroll: 0.092, asset: 0.072 },
    2028: { payroll: 0.090, asset: 0.070 },
    2029: { payroll: 0.082, asset: 0.066 },
    2030: { payroll: 0.074, asset: 0.062 },
    2031: { payroll: 0.066, asset: 0.058 },
    2032: { payroll: 0.058, asset: 0.054 },
    2033: { payroll: 0.050, asset: 0.050 }  // Permanent rates
}
```

### 5.2 Primary Calculation

```
FUNCTION CalculateSBIE(fiscal_year, eligible_payroll, eligible_assets):

    // Validate inputs
    IF fiscal_year IS NULL THEN
        RETURN Error("Please select a fiscal year")
    END IF

    IF eligible_payroll < 0 THEN
        RETURN Error("Eligible Payroll Costs cannot be negative")
    END IF

    IF eligible_assets < 0 THEN
        RETURN Error("Eligible Tangible Assets cannot be negative")
    END IF

    // Look up rates for fiscal year
    IF fiscal_year >= 2033 THEN
        rates = SBIE_RATES[2033]  // Use permanent rates
    ELSE
        rates = SBIE_RATES[fiscal_year]
    END IF

    payroll_rate = rates.payroll
    asset_rate = rates.asset

    // Calculate SBIE components
    payroll_sbie = eligible_payroll × payroll_rate
    asset_sbie = eligible_assets × asset_rate

    // Round to whole currency units
    payroll_sbie = ROUND(payroll_sbie, 0)
    asset_sbie = ROUND(asset_sbie, 0)

    // Calculate total
    total_sbie = payroll_sbie + asset_sbie

    RETURN {
        payroll_rate: payroll_rate × 100,      // Convert to percentage for display
        asset_rate: asset_rate × 100,          // Convert to percentage for display
        payroll_sbie: payroll_sbie,
        asset_sbie: asset_sbie,
        total_sbie: total_sbie
    }

END FUNCTION
```

### 5.3 Rounding Rules

| Calculation | Rounding Method | Precision |
|-------------|-----------------|-----------|
| Payroll SBIE | Standard (half-up) | 0 decimal places (whole currency) |
| Asset SBIE | Standard (half-up) | 0 decimal places (whole currency) |
| Total SBIE | Sum of rounded components | 0 decimal places |
| Display rates | No rounding (fixed lookup values) | 1 decimal place |

### 5.4 Formula Reference

| Formula | Article Reference |
|---------|-------------------|
| Payroll SBIE = Eligible Payroll × Payroll Rate | GloBE Model Rules Article 5.3.3 |
| Asset SBIE = Eligible Assets × Asset Rate | GloBE Model Rules Article 5.3.4 |
| Total SBIE = Payroll SBIE + Asset SBIE | GloBE Model Rules Article 5.3.1 |
| Transitional Rates | GloBE Model Rules Article 9.1.2 |

---

## 6. User Interface Specifications

### 6.1 Layout Structure

```
┌─────────────────────────────────────────────────────────────┐
│  GIR SBIE Calculator                                   [?]  │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │ INPUT SECTION                                        │   │
│  ├─────────────────────────────────────────────────────┤   │
│  │                                                      │   │
│  │  Fiscal Year:     [FY 2024           ▼]             │   │
│  │                   (Rates: Payroll 9.8%, Assets 7.8%) │   │
│  │                                                      │   │
│  │  Currency:        [EUR ▼]                           │   │
│  │                                                      │   │
│  │  Eligible Payroll [________________] €              │   │
│  │  Costs:           (Required)                         │   │
│  │                                                      │   │
│  │  Eligible Tangible [________________] €             │   │
│  │  Assets (NBV):     (Required)                        │   │
│  │                                                      │   │
│  │  Jurisdiction:    [________________]                │   │
│  │                   (Optional - for reference)         │   │
│  │                                                      │   │
│  │  [   Calculate SBIE   ]    [  Clear  ]              │   │
│  │                                                      │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │ RESULTS SECTION                                      │   │
│  ├─────────────────────────────────────────────────────┤   │
│  │                                                      │   │
│  │  PAYROLL COMPONENT                                  │   │
│  │  ┌─────────────────────────────────────────────┐    │   │
│  │  │ Rate: 9.8%          Amount: €1,862,000      │    │   │
│  │  └─────────────────────────────────────────────┘    │   │
│  │                                                      │   │
│  │  ASSET COMPONENT                                    │   │
│  │  ┌─────────────────────────────────────────────┐    │   │
│  │  │ Rate: 7.8%          Amount: €1,326,000      │    │   │
│  │  └─────────────────────────────────────────────┘    │   │
│  │                                                      │   │
│  │  TOTAL SBIE                                         │   │
│  │  ┌─────────────────────────────────────────────┐    │   │
│  │  │            €3,188,000                        │    │   │
│  │  └─────────────────────────────────────────────┘    │   │
│  │                                                      │   │
│  │  ┌─────────────────────────────────────────────┐    │   │
│  │  │ Calculation Breakdown                        │    │   │
│  │  │ ─────────────────────────────────────────── │    │   │
│  │  │ Payroll: €19,000,000 × 9.8% = €1,862,000   │    │   │
│  │  │ Assets:  €17,000,000 × 7.8% = €1,326,000   │    │   │
│  │  │ Total:   €1,862,000 + €1,326,000           │    │   │
│  │  │        = €3,188,000                         │    │   │
│  │  └─────────────────────────────────────────────┘    │   │
│  │                                                      │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │ TRANSITION RATE REFERENCE (Collapsible)             │   │
│  │ [▼ Show rate table]                                 │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### 6.2 Dynamic Rate Display

When user selects a fiscal year, display the applicable rates immediately below the dropdown:

| Year Selected | Display Text |
|---------------|--------------|
| FY 2024 | "Rates: Payroll 9.8%, Assets 7.8%" |
| FY 2025 | "Rates: Payroll 9.6%, Assets 7.6%" |
| FY 2033+ | "Rates: Payroll 5.0%, Assets 5.0% (permanent)" |

### 6.3 Button Specifications

**Calculate SBIE Button:**
| Property | Value |
|----------|-------|
| Label | "Calculate SBIE" |
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
| Behavior | Clears all input fields and results, resets fiscal year to default |

### 6.4 Collapsible Rate Reference Table

Include a collapsible section showing the full transition rate schedule:

```
┌─────────────────────────────────────────────────────────────┐
│ SBIE Transition Rates Reference                        [−]  │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  Fiscal Year    Payroll Rate    Asset Rate                 │
│  ─────────────────────────────────────────                 │
│  2024           9.8%            7.8%                       │
│  2025           9.6%            7.6%                       │
│  2026           9.4%            7.4%                       │
│  2027           9.2%            7.2%                       │
│  2028           9.0%            7.0%                       │
│  2029           8.2%            6.6%                       │
│  2030           7.4%            6.2%                       │
│  2031           6.6%            5.8%                       │
│  2032           5.8%            5.4%                       │
│  2033+          5.0%            5.0%  (permanent)          │
│                                                             │
│  Source: GloBE Model Rules Article 9.1.2                   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### 6.5 Responsive Behavior

| Viewport | Layout |
|----------|--------|
| Desktop (>992px) | Side-by-side input/results panels |
| Tablet (768-992px) | Stacked panels, full width |
| Mobile (<768px) | Single column, rate table collapsed by default |

---

## 7. User Flow

### 7.1 Happy Path Flow

```
Step 1: User navigates to GIR SBIE Calculator
        → Page loads with default fiscal year (2024)
        → Rate display shows "Rates: Payroll 9.8%, Assets 7.8%"
        → Currency defaults to EUR
        → Results section shows placeholder text

Step 2: User selects Fiscal Year (if different from default)
        → Dropdown updates
        → Rate display updates to show applicable rates
        → Results section clears (if previously populated)

Step 3: User selects Currency (optional)
        → Dropdown updates
        → Currency symbol updates in input fields

Step 4: User enters Eligible Payroll Costs
        → Input accepts numeric value
        → Thousand separators added automatically
        → Validation runs on blur

Step 5: User enters Eligible Tangible Assets
        → Input accepts numeric value
        → Thousand separators added automatically
        → Validation runs on blur

Step 6: User enters Jurisdiction Name (optional)
        → Text input accepts value

Step 7: User clicks "Calculate SBIE"
        → System validates all inputs
        → IF validation passes:
            → Calculation runs
            → Payroll component displays with rate and amount
            → Asset component displays with rate and amount
            → Total SBIE displays prominently
            → Calculation breakdown shows full formula
        → IF validation fails:
            → Error messages display under relevant fields
            → Focus moves to first error field

Step 8: User reviews results
        → Can modify inputs and recalculate
        → Can expand rate reference table
        → Can click "Clear" to start over
```

### 7.2 Year Change Flow

```
User has completed a calculation
        → User changes Fiscal Year dropdown
        → Rate display updates immediately
        → Results section clears
        → User must click "Calculate SBIE" again to recalculate
        → (Alternatively: auto-recalculate on year change if inputs valid)
```

---

## 8. Edge Cases & Error Handling

### 8.1 Edge Cases

| Scenario | Input | Expected Behavior |
|----------|-------|-------------------|
| Zero payroll | payroll = 0, assets > 0 | Valid: Payroll SBIE = 0, Total = Asset SBIE only |
| Zero assets | payroll > 0, assets = 0 | Valid: Asset SBIE = 0, Total = Payroll SBIE only |
| Both zero | payroll = 0, assets = 0 | Valid: Total SBIE = 0 (display with note) |
| Very small amounts | payroll = 100 | Calculate: 100 × 9.8% = 9.80, rounds to 10 |
| Large amounts | payroll = 500,000,000,000 | Calculate normally, verify no overflow |
| Future year (2040) | fiscal_year = 2040 | Use permanent rates (5.0%, 5.0%) |
| Rounding boundary | payroll = 10,204.08 (× 9.8% = 999.99984) | Rounds to 1,000 |

### 8.2 Special Display Cases

| Scenario | Display Behavior |
|----------|------------------|
| Total SBIE = 0 | Display "€0" with note: "No SBIE available - check eligible amounts" |
| Only payroll (no assets) | Asset section shows "€0" but no error |
| Only assets (no payroll) | Payroll section shows "€0" but no error |

### 8.3 Error Messages

| Error Code | Trigger | User Message |
|------------|---------|--------------|
| ERR_001 | Fiscal Year not selected | "Please select a fiscal year" |
| ERR_002 | Payroll empty | "Eligible Payroll Costs is required" |
| ERR_003 | Payroll negative | "Eligible Payroll Costs cannot be negative" |
| ERR_004 | Payroll non-numeric | "Please enter a valid number for Eligible Payroll Costs" |
| ERR_005 | Assets empty | "Eligible Tangible Assets is required" |
| ERR_006 | Assets negative | "Eligible Tangible Assets cannot be negative" |
| ERR_007 | Assets non-numeric | "Please enter a valid number for Eligible Tangible Assets" |
| ERR_008 | Jurisdiction name too long | "Jurisdiction name cannot exceed 100 characters" |

---

## 9. Test Cases

### 9.1 Functional Test Cases

| Test ID | Description | Inputs | Expected Output | Source |
|---------|-------------|--------|-----------------|--------|
| TC-001 | Ireland FY2024 | Year: 2024, Payroll: 19,000,000, Assets: 17,000,000 | Payroll SBIE: €1,862,000, Asset SBIE: €1,326,000, Total: €3,188,000 | Case Study 1 |
| TC-002 | Switzerland FY2024 | Year: 2024, Payroll: 8,500,000, Assets: 4,200,000 | Payroll SBIE: €833,000, Asset SBIE: €327,600, Total: €1,160,600 | Case Study 1 |
| TC-003 | POPE Ireland FY2024 | Year: 2024, Payroll: 8,000,000, Assets: 6,500,000 | Payroll SBIE: €784,000, Asset SBIE: €507,000, Total: €1,291,000 | Case Study 2 |
| TC-004 | Netherlands FY2024 | Year: 2024, Payroll: 4,000,000, Assets: 2,500,000 | Payroll SBIE: €392,000, Asset SBIE: €195,000, Total: €587,000 | Case Study 4 |
| TC-005 | FY2025 rates | Year: 2025, Payroll: 10,000,000, Assets: 10,000,000 | Payroll SBIE: €960,000, Asset SBIE: €760,000, Total: €1,720,000 | Rate test |
| TC-006 | FY2033 permanent | Year: 2033, Payroll: 10,000,000, Assets: 10,000,000 | Payroll SBIE: €500,000, Asset SBIE: €500,000, Total: €1,000,000 | Rate test |
| TC-007 | Zero payroll | Year: 2024, Payroll: 0, Assets: 10,000,000 | Payroll SBIE: €0, Asset SBIE: €780,000, Total: €780,000 | Edge case |
| TC-008 | Zero assets | Year: 2024, Payroll: 10,000,000, Assets: 0 | Payroll SBIE: €980,000, Asset SBIE: €0, Total: €980,000 | Edge case |

### 9.2 Rate Verification Test Cases

| Test ID | Fiscal Year | Expected Payroll Rate | Expected Asset Rate |
|---------|-------------|----------------------|---------------------|
| RT-001 | 2024 | 9.8% | 7.8% |
| RT-002 | 2025 | 9.6% | 7.6% |
| RT-003 | 2026 | 9.4% | 7.4% |
| RT-004 | 2027 | 9.2% | 7.2% |
| RT-005 | 2028 | 9.0% | 7.0% |
| RT-006 | 2029 | 8.2% | 6.6% |
| RT-007 | 2030 | 7.4% | 6.2% |
| RT-008 | 2031 | 6.6% | 5.8% |
| RT-009 | 2032 | 5.8% | 5.4% |
| RT-010 | 2033 | 5.0% | 5.0% |
| RT-011 | 2040 | 5.0% | 5.0% |

### 9.3 Validation Test Cases

| Test ID | Description | Input | Expected Result |
|---------|-------------|-------|-----------------|
| VT-001 | Empty payroll | payroll = "" | ERR_002 displayed |
| VT-002 | Negative payroll | payroll = -1000 | ERR_003 displayed |
| VT-003 | Non-numeric payroll | payroll = "abc" | ERR_004 displayed |
| VT-004 | Empty assets | assets = "" | ERR_005 displayed |
| VT-005 | Negative assets | assets = -500 | ERR_006 displayed |
| VT-006 | Non-numeric assets | assets = "xyz" | ERR_007 displayed |

### 9.4 UI/UX Test Cases

| Test ID | Description | Action | Expected Result |
|---------|-------------|--------|-----------------|
| UX-001 | Clear button | Click Clear after calculation | All fields cleared, results hidden |
| UX-002 | Thousand separators | Enter 19000000 | Displays as 19,000,000 |
| UX-003 | Year change rate display | Select FY 2025 | Rate display shows "9.6%, 7.6%" |
| UX-004 | Rate table toggle | Click "Show rate table" | Table expands, button changes to "Hide" |
| UX-005 | Responsive layout | Resize to mobile | Layout stacks vertically |

---

## 10. Accessibility Requirements

| Requirement | Implementation |
|-------------|----------------|
| Keyboard navigation | All inputs accessible via Tab key, dropdown navigable with arrow keys |
| Screen reader | ARIA labels on all form fields, rate changes announced |
| Color contrast | Minimum 4.5:1 for text |
| Error announcement | Errors announced to screen readers |
| Focus indicator | Visible focus ring on all interactive elements |
| Rate table | Table has proper headers for screen reader navigation |

---

## 11. Technical Notes

### 11.1 Dependencies
- No external APIs required
- All calculations performed client-side
- Rate table hardcoded (no external data source)
- No data persistence required

### 11.2 Performance
- Calculation should complete in <100ms
- Rate lookup is O(1) constant time
- No network requests during calculation

### 11.3 Browser Support
- Chrome (latest 2 versions)
- Firefox (latest 2 versions)
- Safari (latest 2 versions)
- Edge (latest 2 versions)

### 11.4 Data Precision
- Internal calculations use full decimal precision
- Rounding applied only at final display
- Currency amounts rounded to whole units for display

---

## 12. Limitations & Scope

This demo tool does **NOT**:
- Determine which payroll costs are eligible under Article 5.3.3
- Determine which tangible assets are eligible under Article 5.3.4
- Calculate average net book value from opening/closing balances
- Validate asset location requirements
- Handle SBIE for Permanent Establishments (PEs)
- Handle SBIE for Joint Ventures (special rules apply)
- Handle SBIE for Investment Entities
- Connect to any tax authority system
- Store or persist calculation history
- Validate data accuracy against source documents
- Account for substance-based income exclusion elections

Users should understand this tool is for **learning purposes only** to practice the SBIE calculation concept. Users must determine eligible amounts before using this tool.

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
- Inputs: FY 2024, Payroll €19,000,000, Assets €17,000,000
- Expected Outputs:
  - Payroll Rate: 9.8%
  - Payroll SBIE: €1,862,000
  - Asset Rate: 7.8%
  - Asset SBIE: €1,326,000
  - Total SBIE: €3,188,000

**Switzerland Scenario:**
- Sample Data Location: `Appendices/Case_Study_1_GlobalTech_First_Filing/Sample_Data.md`
- Inputs: FY 2024, Payroll €8,500,000, Assets €4,200,000
- Expected Outputs:
  - Payroll SBIE: €833,000
  - Asset SBIE: €327,600
  - Total SBIE: €1,160,600

### Case Study 2: Meridian Industrial Group

**POPE Ireland Scenario:**
- Sample Data Location: `Appendices/Case_Study_2_Complex_Ownership/Sample_Data.md`
- Inputs: FY 2024, Payroll €8,000,000, Assets €6,500,000
- Expected Outputs:
  - Payroll SBIE: €784,000
  - Asset SBIE: €507,000
  - Total SBIE: €1,291,000

### Case Study 4: Atlantic Manufacturing Group

**Netherlands Scenario:**
- Sample Data Location: `Appendices/Case_Study_4_Multi_QDMTT_Jurisdictions/Sample_Data.md`
- Inputs: FY 2024, Payroll €4,000,000, Assets €2,500,000
- Expected Outputs:
  - Payroll SBIE: €392,000
  - Asset SBIE: €195,000
  - Total SBIE: €587,000

---

## 15. Appendix: SBIE Rate Transition Schedule

Per GloBE Model Rules Article 9.1.2, the carve-out percentages during the transition period are:

| Fiscal Year Beginning | Payroll Carve-out | Tangible Asset Carve-out |
|-----------------------|-------------------|--------------------------|
| On or after 31 Dec 2023 (FY 2024) | 9.8% | 7.8% |
| On or after 31 Dec 2024 (FY 2025) | 9.6% | 7.6% |
| On or after 31 Dec 2025 (FY 2026) | 9.4% | 7.4% |
| On or after 31 Dec 2026 (FY 2027) | 9.2% | 7.2% |
| On or after 31 Dec 2027 (FY 2028) | 9.0% | 7.0% |
| On or after 31 Dec 2028 (FY 2029) | 8.2% | 6.6% |
| On or after 31 Dec 2029 (FY 2030) | 7.4% | 6.2% |
| On or after 31 Dec 2030 (FY 2031) | 6.6% | 5.8% |
| On or after 31 Dec 2031 (FY 2032) | 5.8% | 5.4% |
| On or after 31 Dec 2032 (FY 2033+) | 5.0% | 5.0% |

The permanent rates of 5% for both components apply from fiscal years beginning on or after 31 December 2032.
