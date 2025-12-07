# GIR-001: ETR Calculator - Tool Specification

**Version:** 1.0
**Last Updated:** 2024-12-07
**Status:** Planned
**Platform:** tools.mojitax.com

---

## 1. Tool Metadata

| Field | Value |
|-------|-------|
| Tool ID | GIR-001 |
| Tool Name | GIR ETR Calculator |
| Category | Pillar Two |
| Form Type | Calculator |
| Status | Planned |
| Used By | GloBE Information Return: Complete Filing Implementation |
| Introduced In | Section 2.1 - GloBE Income Calculation |

---

## 2. Purpose & Learning Objective

### 2.1 Purpose
Practice calculating the Effective Tax Rate (ETR) for a jurisdiction under GloBE Rules. This is the foundational calculation that determines whether a jurisdiction is "low-taxed" and therefore subject to Top-up Tax.

### 2.2 Learning Objective
After using this tool, learners will be able to:
- Calculate jurisdictional ETR using the GloBE formula
- Interpret the ETR result against the 15% minimum threshold
- Identify low-taxed jurisdictions requiring Top-up Tax
- Understand the relationship between GloBE Income and Adjusted Covered Taxes

### 2.3 Prerequisites
Learners should understand:
- What constitutes GloBE Income (covered in Section 2.1)
- What constitutes Adjusted Covered Taxes (covered in Section 2.2)
- The 15% minimum tax concept under Pillar Two

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
| Help Text | "The net GloBE Income for the jurisdiction after all adjustments (Article 3.1)" |

**Validation Rules:**
| Rule | Condition | Error Message |
|------|-----------|---------------|
| Required | Field is empty | "GloBE Income is required" |
| Positive | Value <= 0 | "GloBE Income must be greater than zero" |
| Numeric | Non-numeric input | "Please enter a valid number" |
| Max exceeded | Value > max | "Value exceeds maximum allowed" |

**Special Handling:**
- If GloBE Income is zero or negative, the tool cannot calculate ETR (division by zero)
- Negative GloBE Income scenarios exist but are out of scope for this demo tool
- Users should be directed to course material for negative income treatment

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
| Help Text | "Total Adjusted Covered Taxes for the jurisdiction (Article 4.1)" |

**Validation Rules:**
| Rule | Condition | Error Message |
|------|-----------|---------------|
| Required | Field is empty | "Adjusted Covered Taxes is required" |
| Non-negative | Value < 0 | "Adjusted Covered Taxes cannot be negative" |
| Numeric | Non-numeric input | "Please enter a valid number" |
| Max exceeded | Value > max | "Value exceeds maximum allowed" |

**Special Handling:**
- Zero is valid (represents no tax liability)
- In real scenarios, negative covered taxes can occur but are out of scope for demo

---

### 3.3 Currency

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

**Note:** Currency selection affects display formatting only. ETR calculation is currency-agnostic (both inputs must be in the same currency).

---

### 3.4 Jurisdiction Name (Optional)

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

### 4.1 Jurisdictional ETR

| Property | Value |
|----------|-------|
| Field ID | `etr_percentage` |
| Label | Jurisdictional ETR |
| Data Type | Percentage |
| Precision | 2 decimal places |
| Display Format | "XX.XX%" |
| UI Element | Read-only text with large font |

**Display Rules:**
- Always show 2 decimal places (e.g., "11.59%", "14.00%", "25.00%")
- If ETR exceeds 100%, display with warning indicator

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

**Display Rules:**
- If ETR >= 15%, display "0.00%"
- If ETR < 15%, display the difference (15% - ETR)
- Always show 2 decimal places

---

### 4.3 Status Indicator

| Property | Value |
|----------|-------|
| Field ID | `status` |
| Label | Status |
| Data Type | String (enumerated) |
| UI Element | Badge/pill with background color |

**Status Values:**
| Status | Condition | Display Text | Background Color | Text Color |
|--------|-----------|--------------|------------------|------------|
| LOW_TAXED | ETR < 15% | "Low-Taxed Jurisdiction" | Red (#DC3545) | White |
| COMPLIANT | ETR >= 15% | "Compliant" | Green (#28A745) | White |
| WARNING | ETR > 100% | "ETR Exceeds 100% - Review Data" | Orange (#FFC107) | Black |

---

### 4.4 Calculation Breakdown

| Property | Value |
|----------|-------|
| Field ID | `calculation_breakdown` |
| Label | Calculation Breakdown |
| Data Type | Formatted text block |
| UI Element | Card/panel with monospace font |

**Display Format:**
```
ETR Calculation:
─────────────────────────────────────
ETR = Adjusted Covered Taxes ÷ GloBE Income × 100

ETR = {covered_taxes} ÷ {globe_income} × 100
ETR = {etr_percentage}%

Top-up Tax Percentage:
─────────────────────────────────────
Minimum Rate: 15.00%
Jurisdictional ETR: {etr_percentage}%
Top-up Tax %: {topup_percentage}%
```

---

## 5. Calculation Logic

### 5.1 Primary Calculation

```
FUNCTION CalculateETR(globe_income, covered_taxes):

    // Validate inputs
    IF globe_income <= 0 THEN
        RETURN Error("GloBE Income must be greater than zero")
    END IF

    IF covered_taxes < 0 THEN
        RETURN Error("Adjusted Covered Taxes cannot be negative")
    END IF

    // Calculate ETR
    etr_decimal = covered_taxes / globe_income
    etr_percentage = etr_decimal × 100

    // Round to 2 decimal places (standard rounding)
    etr_percentage = ROUND(etr_percentage, 2)

    // Calculate Top-up Tax Percentage
    IF etr_percentage >= 15.00 THEN
        topup_percentage = 0.00
        status = "COMPLIANT"
    ELSE
        topup_percentage = 15.00 - etr_percentage
        topup_percentage = ROUND(topup_percentage, 2)
        status = "LOW_TAXED"
    END IF

    // Check for anomalous ETR
    IF etr_percentage > 100.00 THEN
        status = "WARNING"
    END IF

    RETURN {
        etr_percentage: etr_percentage,
        topup_percentage: topup_percentage,
        status: status
    }

END FUNCTION
```

### 5.2 Rounding Rules

| Calculation | Rounding Method | Precision |
|-------------|-----------------|-----------|
| ETR Percentage | Standard (half-up) | 2 decimal places |
| Top-up Tax Percentage | Standard (half-up) | 2 decimal places |
| Display values | Truncate trailing zeros only for whole numbers | 2 decimal places minimum |

### 5.3 Formula Reference

| Formula | Article Reference |
|---------|-------------------|
| ETR = Adjusted Covered Taxes ÷ GloBE Income | GloBE Model Rules Article 5.1 |
| Top-up Tax % = 15% - ETR (if ETR < 15%) | GloBE Model Rules Article 5.2 |

---

## 6. User Interface Specifications

### 6.1 Layout Structure

```
┌─────────────────────────────────────────────────────────────┐
│  GIR ETR Calculator                                    [?]  │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │ INPUT SECTION                                        │   │
│  ├─────────────────────────────────────────────────────┤   │
│  │                                                      │   │
│  │  Currency:        [EUR ▼]                           │   │
│  │                                                      │   │
│  │  GloBE Income:    [________________] €              │   │
│  │                   (Required)                         │   │
│  │                                                      │   │
│  │  Adjusted Covered [________________] €              │   │
│  │  Taxes:           (Required)                         │   │
│  │                                                      │   │
│  │  Jurisdiction:    [________________]                │   │
│  │                   (Optional - for reference)         │   │
│  │                                                      │   │
│  │  [    Calculate ETR    ]    [  Clear  ]             │   │
│  │                                                      │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │ RESULTS SECTION                                      │   │
│  ├─────────────────────────────────────────────────────┤   │
│  │                                                      │   │
│  │  ┌───────────────┐  ┌───────────────┐               │   │
│  │  │ ETR           │  │ Top-up Tax %  │               │   │
│  │  │   11.59%      │  │    3.41%      │               │   │
│  │  └───────────────┘  └───────────────┘               │   │
│  │                                                      │   │
│  │  Status: [  Low-Taxed Jurisdiction  ] (RED)         │   │
│  │                                                      │   │
│  │  ┌─────────────────────────────────────────────┐    │   │
│  │  │ Calculation Breakdown                        │    │   │
│  │  │ ─────────────────────────────────────────── │    │   │
│  │  │ ETR = €3,800,000 ÷ €32,800,000 × 100       │    │   │
│  │  │ ETR = 11.59%                                │    │   │
│  │  │                                             │    │   │
│  │  │ Top-up Tax % = 15.00% - 11.59%             │    │   │
│  │  │ Top-up Tax % = 3.41%                        │    │   │
│  │  └─────────────────────────────────────────────┘    │   │
│  │                                                      │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### 6.2 Button Specifications

**Calculate ETR Button:**
| Property | Value |
|----------|-------|
| Label | "Calculate ETR" |
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

### 6.3 Responsive Behavior

| Viewport | Layout |
|----------|--------|
| Desktop (>992px) | Side-by-side input/results panels |
| Tablet (768-992px) | Stacked panels, full width |
| Mobile (<768px) | Single column, compact spacing |

---

## 7. User Flow

### 7.1 Happy Path Flow

```
Step 1: User navigates to GIR ETR Calculator
        → Page loads with empty input fields
        → Currency defaults to EUR
        → Results section shows placeholder text

Step 2: User selects Currency (optional)
        → Dropdown updates
        → Currency symbol updates in input fields

Step 3: User enters GloBE Income
        → Input accepts numeric value
        → Thousand separators added automatically
        → Validation runs on blur

Step 4: User enters Adjusted Covered Taxes
        → Input accepts numeric value
        → Thousand separators added automatically
        → Validation runs on blur

Step 5: User enters Jurisdiction Name (optional)
        → Text input accepts value

Step 6: User clicks "Calculate ETR"
        → System validates all inputs
        → IF validation passes:
            → Calculation runs
            → Results section populates
            → Status badge displays with appropriate color
            → Calculation breakdown shows
        → IF validation fails:
            → Error messages display under relevant fields
            → Focus moves to first error field

Step 7: User reviews results
        → Can modify inputs and recalculate
        → Can click "Clear" to start over
```

### 7.2 Error Flow

```
User enters invalid data → Clicks Calculate
        → Validation fails
        → Error message appears below field
        → Field border turns red
        → Focus moves to first error field
        → Results section remains empty/previous state
```

---

## 8. Edge Cases & Error Handling

### 8.1 Edge Cases

| Scenario | Input | Expected Behavior |
|----------|-------|-------------------|
| Zero GloBE Income | globe_income = 0 | Error: "GloBE Income must be greater than zero" |
| Zero Covered Taxes | covered_taxes = 0, globe_income > 0 | Valid: ETR = 0.00%, Top-up = 15.00%, Status = LOW_TAXED |
| ETR exactly 15% | covered_taxes/globe_income = 0.15 | ETR = 15.00%, Top-up = 0.00%, Status = COMPLIANT |
| ETR just below 15% | ETR = 14.99% | Top-up = 0.01%, Status = LOW_TAXED |
| ETR just above 15% | ETR = 15.01% | Top-up = 0.00%, Status = COMPLIANT |
| Very high ETR | ETR = 150% | Display with WARNING status |
| Very small amounts | globe_income = 0.01 | Calculate normally |
| Large amounts | globe_income = 999,999,999,999.99 | Calculate normally |
| Taxes > Income | covered_taxes > globe_income | Valid: ETR > 100%, Status = WARNING |

### 8.2 Error Messages

| Error Code | Trigger | User Message |
|------------|---------|--------------|
| ERR_001 | GloBE Income empty | "GloBE Income is required" |
| ERR_002 | GloBE Income <= 0 | "GloBE Income must be greater than zero" |
| ERR_003 | GloBE Income non-numeric | "Please enter a valid number for GloBE Income" |
| ERR_004 | Covered Taxes empty | "Adjusted Covered Taxes is required" |
| ERR_005 | Covered Taxes < 0 | "Adjusted Covered Taxes cannot be negative" |
| ERR_006 | Covered Taxes non-numeric | "Please enter a valid number for Adjusted Covered Taxes" |
| ERR_007 | Jurisdiction name too long | "Jurisdiction name cannot exceed 100 characters" |

---

## 9. Test Cases

### 9.1 Functional Test Cases

| Test ID | Description | Inputs | Expected Output | Source |
|---------|-------------|--------|-----------------|--------|
| TC-001 | Ireland - Low-taxed | GloBE: 32,800,000 / Taxes: 3,800,000 | ETR: 11.59%, Top-up: 3.41%, RED | Case Study 1 |
| TC-002 | Switzerland - Low-taxed | GloBE: 18,000,000 / Taxes: 2,520,000 | ETR: 14.00%, Top-up: 1.00%, RED | Case Study 1 |
| TC-003 | UK - Compliant | GloBE: 120,000,000 / Taxes: 30,000,000 | ETR: 25.00%, Top-up: 0.00%, GREEN | Case Study 4 |
| TC-004 | Germany - Compliant | GloBE: 85,000,000 / Taxes: 25,500,000 | ETR: 30.00%, Top-up: 0.00%, GREEN | Case Study 4 |
| TC-005 | Exactly 15% threshold | GloBE: 10,000,000 / Taxes: 1,500,000 | ETR: 15.00%, Top-up: 0.00%, GREEN | Boundary test |
| TC-006 | Just below 15% | GloBE: 10,000,000 / Taxes: 1,499,000 | ETR: 14.99%, Top-up: 0.01%, RED | Boundary test |
| TC-007 | Zero taxes | GloBE: 10,000,000 / Taxes: 0 | ETR: 0.00%, Top-up: 15.00%, RED | Edge case |
| TC-008 | High ETR (>100%) | GloBE: 10,000,000 / Taxes: 15,000,000 | ETR: 150.00%, Top-up: 0.00%, WARNING | Anomaly test |

### 9.2 Validation Test Cases

| Test ID | Description | Input | Expected Result |
|---------|-------------|-------|-----------------|
| VT-001 | Empty GloBE Income | globe_income = "" | ERR_001 displayed |
| VT-002 | Negative GloBE Income | globe_income = -1000 | ERR_002 displayed |
| VT-003 | Zero GloBE Income | globe_income = 0 | ERR_002 displayed |
| VT-004 | Non-numeric GloBE Income | globe_income = "abc" | ERR_003 displayed |
| VT-005 | Empty Covered Taxes | covered_taxes = "" | ERR_004 displayed |
| VT-006 | Negative Covered Taxes | covered_taxes = -500 | ERR_005 displayed |
| VT-007 | Non-numeric Covered Taxes | covered_taxes = "xyz" | ERR_006 displayed |

### 9.3 UI/UX Test Cases

| Test ID | Description | Action | Expected Result |
|---------|-------------|--------|-----------------|
| UX-001 | Clear button | Click Clear after entering data | All fields cleared, results hidden |
| UX-002 | Thousand separators | Enter 32800000 | Displays as 32,800,000 |
| UX-003 | Currency symbol | Select GBP | Symbol changes to £ |
| UX-004 | Responsive layout | Resize to mobile | Layout stacks vertically |
| UX-005 | Calculation breakdown | Complete calculation | Breakdown shows formula with values |

---

## 10. Accessibility Requirements

| Requirement | Implementation |
|-------------|----------------|
| Keyboard navigation | All inputs accessible via Tab key |
| Screen reader | ARIA labels on all form fields |
| Color contrast | Minimum 4.5:1 for text |
| Error announcement | Errors announced to screen readers |
| Focus indicator | Visible focus ring on all interactive elements |

---

## 11. Technical Notes

### 11.1 Dependencies
- No external APIs required
- All calculations performed client-side
- No data persistence required

### 11.2 Performance
- Calculation should complete in <100ms
- No network requests during calculation

### 11.3 Browser Support
- Chrome (latest 2 versions)
- Firefox (latest 2 versions)
- Safari (latest 2 versions)
- Edge (latest 2 versions)

---

## 12. Limitations & Scope

This demo tool does **NOT**:
- Perform GloBE Income adjustments (user must input pre-calculated amount)
- Calculate Adjusted Covered Taxes from components
- Handle negative GloBE Income scenarios (loss jurisdictions)
- Handle currency conversion between inputs
- Connect to any tax authority system
- Store or persist calculation history
- Validate data accuracy against source documents
- Generate actual GIR filings or XML
- Provide professional tax advice

Users should understand this tool is for **learning purposes only** to practice the ETR calculation concept.

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
- Input: GloBE Income €32,800,000, Adjusted Covered Taxes €3,800,000
- Expected Output: ETR 11.59%, Top-up Tax % 3.41%, Status: Low-Taxed (RED)

**Switzerland Scenario:**
- Sample Data Location: `Appendices/Case_Study_1_GlobalTech_First_Filing/Sample_Data.md`
- Input: GloBE Income €18,000,000, Adjusted Covered Taxes €2,520,000
- Expected Output: ETR 14.00%, Top-up Tax % 1.00%, Status: Low-Taxed (RED)

### Case Study 4: Atlantic Manufacturing Group

**UK Scenario:**
- Sample Data Location: `Appendices/Case_Study_4_Multi_QDMTT_Jurisdictions/Sample_Data.md`
- Input: GloBE Income €120,000,000, Covered Taxes €30,000,000
- Expected Output: ETR 25.00%, Top-up Tax % 0.00%, Status: Compliant (GREEN)
