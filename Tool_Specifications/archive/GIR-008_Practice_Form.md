# GIR-008: GIR Practice Form - Tool Specification

**Version:** 1.0
**Last Updated:** 2024-12-07
**Status:** Planned
**Platform:** tools.mojitax.com

---

## 1. Tool Metadata

| Field | Value |
|-------|-------|
| Tool ID | GIR-008 |
| Tool Name | GIR Practice Form |
| Category | Pillar Two |
| Form Type | Interactive Form |
| Status | Planned |
| Used By | GloBE Information Return: Complete Filing Implementation |
| Introduced In | Section 3.4 - Form Completion and Validation |

---

## 2. Purpose & Learning Objective

### 2.1 Purpose
Provide an interactive practice version of the GIR form structure where learners can input sample data into Sections 1-3, see how fields relate to each other, and practice form navigation before working with actual filing systems. This tool simulates the GIR filing experience without submitting real data.

### 2.2 Learning Objective
After using this tool, learners will be able to:
- Navigate the GIR form structure across all three sections
- Enter data correctly in the appropriate format for each field type
- Understand field dependencies and cross-references between sections
- Validate data entries against format requirements
- Track completion status for each section
- Identify and correct common data entry errors
- Build confidence before using actual tax authority filing portals

### 2.3 Prerequisites
Learners should have completed:
- Section 3.2 (GIR Data Requirements)
- GIR-006 Data Point Reference tool familiarization
- At least one case study review

### 2.4 GIR Form Structure Overview

```
┌─────────────────────────────────────────────────────────────────┐
│                    GIR PRACTICE FORM                            │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│ SECTION 1: GENERAL INFORMATION                                  │
│ ───────────────────────────────────────────────────────────────│
│ 1.1 MNE Group Identification                                    │
│ 1.2 Reporting Period                                            │
│ 1.3 Filing Entity Details                                       │
│ 1.4 Elections and Notifications                                 │
│ 1.5 Contact Information                                         │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│ SECTION 2: CORPORATE STRUCTURE (per Constituent Entity)        │
│ ───────────────────────────────────────────────────────────────│
│ 2.1 Entity Identification                                       │
│ 2.2 Ownership Information                                       │
│ 2.3 Entity Classification                                       │
│ 2.4 Special Entity Status                                       │
│     [Repeat for each CE in the group]                          │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│ SECTION 3: GloBE COMPUTATION (per Jurisdiction)                │
│ ───────────────────────────────────────────────────────────────│
│ 3.1 Jurisdictional Summary                                      │
│ 3.2 GloBE Income Calculation                                    │
│ 3.3 Adjusted Covered Taxes                                      │
│ 3.4 SBIE Calculation                                            │
│ 3.5 Top-up Tax Calculation                                      │
│ 3.6 Safe Harbour Elections                                      │
│ 3.7 Allocation of Top-up Tax                                    │
│     [Repeat for each jurisdiction with CEs]                    │
└─────────────────────────────────────────────────────────────────┘
```

---

## 3. Input Fields

### 3.1 Section Selector

| Property | Value |
|----------|-------|
| Field ID | `section_selector` |
| Label | Select Section |
| Data Type | String (tab selection) |
| Required | **Yes** |
| Default Value | Section 1 |
| UI Element | Tab navigation bar |

**Tab Options:**
| Tab | Label | Description |
|-----|-------|-------------|
| S1 | Section 1: General | MNE group and filing information |
| S2 | Section 2: Structure | Constituent Entity details |
| S3 | Section 3: Computation | GloBE calculations by jurisdiction |

---

### 3.2 Entity/Jurisdiction Selector (Sections 2 & 3)

| Property | Value |
|----------|-------|
| Field ID | `context_selector` |
| Label | Select Entity / Jurisdiction |
| Data Type | String (dropdown) |
| Required | **Yes** (for Sections 2 and 3) |
| UI Element | Dropdown or sidebar list |
| Help Text | "Select the entity or jurisdiction to enter data for" |

**Section 2 Display:** List of Constituent Entities
**Section 3 Display:** List of Jurisdictions (with entity count)

---

### 3.3 Case Study Pre-load Option

| Property | Value |
|----------|-------|
| Field ID | `preload_case_study` |
| Label | Load Case Study Data |
| Data Type | String (dropdown) |
| Required | **No** |
| Default Value | "Start Empty" |
| UI Element | Dropdown with load button |

**Options:**
| Value | Label |
|-------|-------|
| EMPTY | Start with empty form |
| CS1 | Case Study 1: GlobalTech Manufacturing |
| CS2 | Case Study 2: Meridian Industrial Group |
| CS3 | Case Study 3: Nexus Technologies |
| CS4 | Case Study 4: Atlantic Manufacturing |
| CS5 | Case Study 5: Phoenix Aerospace |

---

### 3.4 Section 1 Fields: General Information

#### 3.4.1 MNE Group Identification (S1.1)

| Field ID | Field Name | Type | Required | Format |
|----------|------------|------|----------|--------|
| S1.1.1 | MNE Group Name | Text | Yes | Max 200 chars |
| S1.1.2 | UPE Name | Text | Yes | Max 200 chars |
| S1.1.3 | UPE Jurisdiction | Code | Yes | ISO 3166-1 alpha-2 |
| S1.1.4 | UPE TIN | Text | Conditional | Jurisdiction format |
| S1.1.5 | LEI | Text | Optional | 20 chars alphanumeric |

#### 3.4.2 Reporting Period (S1.2)

| Field ID | Field Name | Type | Required | Format |
|----------|------------|------|----------|--------|
| S1.2.1 | Fiscal Year Start | Date | Yes | YYYY-MM-DD |
| S1.2.2 | Fiscal Year End | Date | Yes | YYYY-MM-DD |
| S1.2.3 | Reporting Currency | Code | Yes | ISO 4217 |
| S1.2.4 | First Filing Year | Boolean | Yes | Yes/No |

#### 3.4.3 Filing Entity Details (S1.3)

| Field ID | Field Name | Type | Required | Format |
|----------|------------|------|----------|--------|
| S1.3.1 | DFE Name | Text | Yes | Max 200 chars |
| S1.3.2 | DFE Jurisdiction | Code | Yes | ISO 3166-1 alpha-2 |
| S1.3.3 | DFE TIN | Text | Yes | Jurisdiction format |
| S1.3.4 | Filing Type | Code | Yes | ORIGINAL / AMENDED |
| S1.3.5 | Amendment Reason | Text | Conditional | If AMENDED |

#### 3.4.4 Elections (S1.4)

| Field ID | Field Name | Type | Required | Format |
|----------|------------|------|----------|--------|
| S1.4.1 | Safe Harbour Elections | Multi | Optional | Jurisdiction list |
| S1.4.2 | SBIE Election | Boolean | Optional | Yes/No |
| S1.4.3 | QDMTT Election | Boolean | Optional | Yes/No |

---

### 3.5 Section 2 Fields: Corporate Structure (Per Entity)

#### 3.5.1 Entity Identification (S2.1)

| Field ID | Field Name | Type | Required | Format |
|----------|------------|------|----------|--------|
| S2.1.1 | Entity Name | Text | Yes | Max 200 chars |
| S2.1.2 | Entity ID | Text | Yes | Internal reference |
| S2.1.3 | Jurisdiction | Code | Yes | ISO 3166-1 alpha-2 |
| S2.1.4 | TIN | Text | Conditional | Jurisdiction format |
| S2.1.5 | Address | Text | Optional | Multi-line |
| S2.1.6 | Incorporation Date | Date | Optional | YYYY-MM-DD |

#### 3.5.2 Ownership Information (S2.2)

| Field ID | Field Name | Type | Required | Format |
|----------|------------|------|----------|--------|
| S2.2.1 | Direct Parent | Reference | Yes | Entity ID |
| S2.2.2 | Ownership Percentage | Numeric | Yes | 0-100%, 2 decimals |
| S2.2.3 | Ownership Type | Code | Yes | DIRECT / INDIRECT |
| S2.2.4 | Controlling Interest | Boolean | Yes | Yes/No |

#### 3.5.3 Entity Classification (S2.3)

| Field ID | Field Name | Type | Required | Format |
|----------|------------|------|----------|--------|
| S2.3.1 | Entity Type | Code | Yes | UPE / CE / PE / JV / Other |
| S2.3.2 | Excluded Entity | Boolean | Yes | Yes/No |
| S2.3.3 | Exclusion Reason | Code | Conditional | If Excluded = Yes |
| S2.3.4 | POPE Status | Boolean | Optional | Yes/No |
| S2.3.5 | Investment Entity | Boolean | Optional | Yes/No |

---

### 3.6 Section 3 Fields: GloBE Computation (Per Jurisdiction)

#### 3.6.1 Jurisdictional Summary (S3.1)

| Field ID | Field Name | Type | Required | Format |
|----------|------------|------|----------|--------|
| S3.1.1 | Jurisdiction | Code | Yes | ISO 3166-1 alpha-2 |
| S3.1.2 | Number of CEs | Numeric | Auto | Integer |
| S3.1.3 | Total Revenue | Numeric | Yes | Currency, 2 decimals |
| S3.1.4 | Total Employees | Numeric | Optional | Integer |

#### 3.6.2 GloBE Income Calculation (S3.2)

| Field ID | Field Name | Type | Required | Format |
|----------|------------|------|----------|--------|
| S3.2.1 | Financial Accounting Income | Numeric | Yes | Currency, 2 decimals |
| S3.2.2 | Net Taxes in Income | Numeric | Yes | Currency, 2 decimals |
| S3.2.3 | Excluded Dividends | Numeric | Optional | Currency, 2 decimals |
| S3.2.4 | Excluded Equity Gains | Numeric | Optional | Currency, 2 decimals |
| S3.2.5 | Policy Disallowed Expenses | Numeric | Optional | Currency, 2 decimals |
| S3.2.6 | Stock Compensation Adjustment | Numeric | Optional | Currency, 2 decimals |
| S3.2.7 | Other Adjustments | Numeric | Optional | Currency, 2 decimals |
| S3.2.8 | **GloBE Income** | Numeric | Calculated | Currency, 2 decimals |

#### 3.6.3 Adjusted Covered Taxes (S3.3)

| Field ID | Field Name | Type | Required | Format |
|----------|------------|------|----------|--------|
| S3.3.1 | Current Tax Expense | Numeric | Yes | Currency, 2 decimals |
| S3.3.2 | Deferred Tax Expense | Numeric | Yes | Currency, 2 decimals |
| S3.3.3 | Total Tax Expense | Numeric | Calculated | Currency, 2 decimals |
| S3.3.4 | UTP Adjustment | Numeric | Optional | Currency, 2 decimals |
| S3.3.5 | Non-Covered Tax Adjustment | Numeric | Optional | Currency, 2 decimals |
| S3.3.6 | Other Tax Adjustments | Numeric | Optional | Currency, 2 decimals |
| S3.3.7 | **Adjusted Covered Taxes** | Numeric | Calculated | Currency, 2 decimals |

#### 3.6.4 SBIE Calculation (S3.4)

| Field ID | Field Name | Type | Required | Format |
|----------|------------|------|----------|--------|
| S3.4.1 | Eligible Payroll Costs | Numeric | Yes | Currency, 2 decimals |
| S3.4.2 | Payroll Carve-out Rate | Numeric | Auto | Percentage |
| S3.4.3 | Payroll SBIE | Numeric | Calculated | Currency, 2 decimals |
| S3.4.4 | Eligible Tangible Assets | Numeric | Yes | Currency, 2 decimals |
| S3.4.5 | Asset Carve-out Rate | Numeric | Auto | Percentage |
| S3.4.6 | Asset SBIE | Numeric | Calculated | Currency, 2 decimals |
| S3.4.7 | **Total SBIE** | Numeric | Calculated | Currency, 2 decimals |

#### 3.6.5 Top-up Tax Calculation (S3.5)

| Field ID | Field Name | Type | Required | Format |
|----------|------------|------|----------|--------|
| S3.5.1 | GloBE Income | Numeric | From S3.2 | Currency, 2 decimals |
| S3.5.2 | Adjusted Covered Taxes | Numeric | From S3.3 | Currency, 2 decimals |
| S3.5.3 | **Jurisdictional ETR** | Numeric | Calculated | Percentage, 4 decimals |
| S3.5.4 | Minimum Rate | Numeric | Constant | 15.00% |
| S3.5.5 | **Top-up Tax Percentage** | Numeric | Calculated | Percentage, 2 decimals |
| S3.5.6 | Total SBIE | Numeric | From S3.4 | Currency, 2 decimals |
| S3.5.7 | **Excess Profit** | Numeric | Calculated | Currency, 2 decimals |
| S3.5.8 | **Gross Top-up Tax** | Numeric | Calculated | Currency, 2 decimals |
| S3.5.9 | QDMTT Amount | Numeric | Optional | Currency, 2 decimals |
| S3.5.10 | **Net Top-up Tax** | Numeric | Calculated | Currency, 2 decimals |

---

## 4. Output Fields

### 4.1 Section Completion Status

| Property | Value |
|----------|-------|
| Field ID | `completion_status` |
| Label | Completion Status |
| Data Type | Object |
| UI Element | Progress indicators per section |

**Display Format:**
```
┌─────────────────────────────────────────────────────────────────┐
│ COMPLETION STATUS                                               │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  Section 1: General Information    ████████████████░░░░  80%   │
│  Section 2: Corporate Structure    ██████████████████░░  90%   │
│  Section 3: GloBE Computation      ████████████░░░░░░░░  60%   │
│                                                                 │
│  Overall Completion:               ██████████████░░░░░░  77%   │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

### 4.2 Field Validation Messages

| Property | Value |
|----------|-------|
| Field ID | `validation_messages` |
| Label | Validation |
| Data Type | Array of messages |
| UI Element | Inline messages and summary panel |

**Validation Types:**
| Type | Color | Icon | Example |
|------|-------|------|---------|
| Error | Red | ✗ | "UPE Jurisdiction is required" |
| Warning | Yellow | ⚠ | "ETR exceeds 100% - please verify" |
| Info | Blue | ℹ | "This field is optional" |
| Success | Green | ✓ | "Valid ISO country code" |

---

### 4.3 Cross-Reference Checks

| Property | Value |
|----------|-------|
| Field ID | `cross_reference_checks` |
| Label | Cross-Reference Validation |
| Data Type | Array of check results |
| UI Element | Validation panel |

**Cross-Reference Rules:**
| Check ID | Description | Sections | Status |
|----------|-------------|----------|--------|
| XR-001 | UPE in S1 matches UPE entity in S2 | S1 ↔ S2 | Pass/Fail |
| XR-002 | All S2 jurisdictions have S3 entries | S2 ↔ S3 | Pass/Fail |
| XR-003 | DFE in S1 exists as entity in S2 | S1 ↔ S2 | Pass/Fail |
| XR-004 | Entity references in S2 are valid | S2 internal | Pass/Fail |
| XR-005 | Total revenue reconciles across sections | S2 ↔ S3 | Pass/Fail |
| XR-006 | Fiscal year dates are consistent | S1 ↔ S3 | Pass/Fail |

**Display Format:**
```
┌─────────────────────────────────────────────────────────────────┐
│ CROSS-REFERENCE VALIDATION                                      │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ✓ XR-001: UPE identification consistent                       │
│  ✓ XR-002: All jurisdictions have computation data             │
│  ✗ XR-003: DFE entity not found in Section 2                   │
│  ✓ XR-004: All entity references valid                         │
│  ⚠ XR-005: Revenue difference of €15,000 between sections      │
│  ✓ XR-006: Fiscal year dates consistent                        │
│                                                                 │
│  Status: 4 passed, 1 failed, 1 warning                         │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

### 4.4 Calculated Fields Summary

| Property | Value |
|----------|-------|
| Field ID | `calculated_summary` |
| Label | Calculated Values Summary |
| Data Type | Table |
| UI Element | Summary panel |

**Display Format:**
```
┌─────────────────────────────────────────────────────────────────┐
│ CALCULATED VALUES SUMMARY                                       │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  Jurisdiction: Ireland                                          │
│  ───────────────────────────────────────────────────────────── │
│  GloBE Income:              €32,800,000                        │
│  Adjusted Covered Taxes:    €3,800,000                         │
│  Jurisdictional ETR:        11.59%                             │
│  Top-up Tax %:              3.41%                              │
│  Total SBIE:                €3,188,000                         │
│  Excess Profit:             €29,612,000                        │
│  Gross Top-up Tax:          €1,009,769                         │
│  Net Top-up Tax:            €1,009,769                         │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

### 4.5 Data Export

| Property | Value |
|----------|-------|
| Field ID | `export_options` |
| Label | Export Data |
| Data Type | Action buttons |
| UI Element | Export panel |

**Export Options:**
| Option | Format | Description |
|--------|--------|-------------|
| Export Summary | PDF | Summary report of all entered data |
| Export Data | JSON | Machine-readable data export |
| Export for Review | Excel | Spreadsheet for offline review |

---

## 5. Calculation Logic

### 5.1 GloBE Income Calculation

```
FUNCTION CalculateGloBEIncome(inputs):

    globe_income = inputs.financial_accounting_income
                 + inputs.net_taxes_in_income
                 - inputs.excluded_dividends
                 - inputs.excluded_equity_gains
                 + inputs.policy_disallowed_expenses
                 + inputs.stock_compensation_adjustment
                 + inputs.other_adjustments

    RETURN ROUND(globe_income, 2)

END FUNCTION
```

### 5.2 Adjusted Covered Taxes Calculation

```
FUNCTION CalculateAdjustedCoveredTaxes(inputs):

    total_tax_expense = inputs.current_tax_expense
                      + inputs.deferred_tax_expense

    adjusted_covered_taxes = total_tax_expense
                           - inputs.utp_adjustment
                           - inputs.non_covered_tax_adjustment
                           + inputs.other_tax_adjustments

    RETURN ROUND(adjusted_covered_taxes, 2)

END FUNCTION
```

### 5.3 ETR and Top-up Tax Calculation

```
FUNCTION CalculateTopUpTax(globe_income, covered_taxes, sbie, qdmtt):

    // ETR Calculation
    IF globe_income <= 0 THEN
        etr = 0
    ELSE
        etr = (covered_taxes / globe_income) × 100
    END IF

    // Top-up Tax Percentage
    IF etr >= 15.00 THEN
        topup_pct = 0
    ELSE
        topup_pct = 15.00 - etr
    END IF

    // Excess Profit
    excess_profit = MAX(globe_income - sbie, 0)

    // Gross Top-up Tax
    gross_topup = excess_profit × (topup_pct / 100)

    // Net Top-up Tax
    net_topup = MAX(gross_topup - qdmtt, 0)

    RETURN {
        etr: ROUND(etr, 4),
        topup_pct: ROUND(topup_pct, 2),
        excess_profit: ROUND(excess_profit, 2),
        gross_topup: ROUND(gross_topup, 0),
        net_topup: ROUND(net_topup, 0)
    }

END FUNCTION
```

### 5.4 Completion Percentage Calculation

```
FUNCTION CalculateCompletion(section, data):

    total_required = COUNT(section.required_fields)
    filled_required = COUNT(section.required_fields WHERE value IS NOT EMPTY)

    completion_pct = (filled_required / total_required) × 100

    RETURN ROUND(completion_pct, 0)

END FUNCTION
```

---

## 6. User Interface Specifications

### 6.1 Main Layout Structure

```
┌─────────────────────────────────────────────────────────────────┐
│  GIR Practice Form                                    [?] [⚙]  │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │ [Section 1: General] [Section 2: Structure] [Section 3]  │  │
│  │                                             [Computation] │  │
│  └──────────────────────────────────────────────────────────┘  │
│                                                                 │
│  ┌────────────────┬─────────────────────────────────────────┐  │
│  │ NAVIGATION     │  FORM CONTENT                           │  │
│  ├────────────────┼─────────────────────────────────────────┤  │
│  │                │                                         │  │
│  │ ▼ S1.1 Group   │  S1.1 MNE GROUP IDENTIFICATION          │  │
│  │   Identification│  ─────────────────────────────────────  │  │
│  │   ● Complete   │                                         │  │
│  │                │  MNE Group Name *                       │  │
│  │ ▶ S1.2 Period  │  [GlobalTech Manufacturing Group plc ]  │  │
│  │   ○ Incomplete │                                         │  │
│  │                │  UPE Name *                             │  │
│  │ ▶ S1.3 Filing  │  [GlobalTech Holdings plc             ]  │  │
│  │   ○ Incomplete │                                         │  │
│  │                │  UPE Jurisdiction *                     │  │
│  │ ▶ S1.4 Elections│  [United Kingdom (GB)              ▼]  │  │
│  │   ○ Not started│                                         │  │
│  │                │  UPE TIN                                │  │
│  │                │  [1234567890                          ]  │  │
│  │                │                                         │  │
│  │                │  LEI (optional)                         │  │
│  │                │  [                                    ]  │  │
│  │                │                                         │  │
│  │                │  [Save Section]  [Clear Section]        │  │
│  │                │                                         │  │
│  └────────────────┴─────────────────────────────────────────┘  │
│                                                                 │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │ STATUS BAR                                                │  │
│  │ Section 1: 80% complete | 2 errors | 1 warning           │  │
│  └──────────────────────────────────────────────────────────┘  │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### 6.2 Section 2 Layout (Entity-Based)

```
┌─────────────────────────────────────────────────────────────────┐
│  [Section 1] [Section 2: Structure ●] [Section 3]              │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌────────────────┬─────────────────────────────────────────┐  │
│  │ ENTITIES       │  ENTITY DETAILS                         │  │
│  ├────────────────┼─────────────────────────────────────────┤  │
│  │                │                                         │  │
│  │ [+ Add Entity] │  GT Holdings plc (UPE)                  │  │
│  │                │  ═════════════════════════════════════  │  │
│  │ ● GT Holdings  │                                         │  │
│  │   (UPE) - GB   │  Entity Name *                          │  │
│  │                │  [GT Holdings plc                     ]  │  │
│  │ ○ GT IP Ltd    │                                         │  │
│  │   - IE         │  Entity ID *                            │  │
│  │                │  [CE-001                              ]  │  │
│  │ ○ GT Services  │                                         │  │
│  │   - IE         │  Jurisdiction *                         │  │
│  │                │  [United Kingdom (GB)              ▼]   │  │
│  │ ○ GT Trading   │                                         │  │
│  │   - CH         │  Entity Type *                          │  │
│  │                │  [UPE - Ultimate Parent Entity     ▼]   │  │
│  │ ○ GT Finance   │                                         │  │
│  │   - CH         │  Direct Parent                          │  │
│  │                │  [— None (Top of structure) —      ▼]   │  │
│  │                │                                         │  │
│  │ Total: 5       │  Ownership %                            │  │
│  │                │  [100.00                      ] %       │  │
│  │                │                                         │  │
│  └────────────────┴─────────────────────────────────────────┘  │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### 6.3 Section 3 Layout (Jurisdiction-Based)

```
┌─────────────────────────────────────────────────────────────────┐
│  [Section 1] [Section 2] [Section 3: Computation ●]            │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌────────────────┬─────────────────────────────────────────┐  │
│  │ JURISDICTIONS  │  IRELAND - GloBE COMPUTATION            │  │
│  ├────────────────┼─────────────────────────────────────────┤  │
│  │                │                                         │  │
│  │ ● Ireland (4)  │  ┌─────────────────────────────────────┐│  │
│  │   ETR: 11.59%  │  │ 3.2 GloBE INCOME                    ││  │
│  │   Top-up: Yes  │  ├─────────────────────────────────────┤│  │
│  │                │  │ Financial Accounting Income *       ││  │
│  │ ○ Switzerland  │  │ [28,000,000.00               ] €    ││  │
│  │   (2)          │  │                                     ││  │
│  │   ETR: 14.00%  │  │ Net Taxes in Income                 ││  │
│  │   Top-up: Yes  │  │ [3,500,000.00                ] €    ││  │
│  │                │  │                                     ││  │
│  │ ○ UK (3)       │  │ ... more fields ...                 ││  │
│  │   ETR: 25.00%  │  │                                     ││  │
│  │   Top-up: No   │  │ ═══════════════════════════════════ ││  │
│  │                │  │ GloBE INCOME:    €32,800,000.00    ││  │
│  │                │  └─────────────────────────────────────┘│  │
│  │ Group Total:   │                                         │  │
│  │ €1,178,163     │  [▼ 3.3 Adjusted Covered Taxes]        │  │
│  │                │  [▼ 3.4 SBIE Calculation]              │  │
│  │                │  [▼ 3.5 Top-up Tax Calculation]        │  │
│  │                │                                         │  │
│  └────────────────┴─────────────────────────────────────────┘  │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### 6.4 Validation Panel (Slide-out)

```
┌─────────────────────────────────────────────────────────────────┐
│ VALIDATION RESULTS                                         [×] │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ERRORS (2)                                                    │
│  ─────────────────────────────────────────────────────────────│
│  ✗ S1.3.1: DFE Name is required                               │
│    → Click to navigate to field                                │
│                                                                 │
│  ✗ S2.1.3: Entity "GT Services" has invalid jurisdiction code │
│    → Click to navigate to field                                │
│                                                                 │
│  WARNINGS (1)                                                  │
│  ─────────────────────────────────────────────────────────────│
│  ⚠ S3.5.3: Ireland ETR (11.59%) below 15% - verify Top-up Tax │
│    → This is expected for low-taxed jurisdictions              │
│                                                                 │
│  CROSS-REFERENCES (6)                                          │
│  ─────────────────────────────────────────────────────────────│
│  ✓ UPE consistent across sections                              │
│  ✓ All entities have valid parent references                   │
│  ✓ Jurisdiction coverage complete                              │
│  ✗ DFE entity not found in Section 2                          │
│  ✓ Revenue totals reconcile                                    │
│  ✓ Fiscal dates consistent                                     │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## 7. User Flow

### 7.1 New Form Flow

```
Step 1: User navigates to GIR Practice Form
        → Page loads with Section 1 active
        → Option to load case study data or start empty

Step 2: User optionally loads case study
        → Selects "Case Study 1: GlobalTech"
        → Form populates with sample data
        → Completion status updates

Step 3: User completes Section 1
        → Enters/verifies MNE Group details
        → Enters reporting period
        → Enters filing entity details
        → Navigation shows completion progress

Step 4: User moves to Section 2
        → Clicks Section 2 tab
        → Adds Constituent Entities one by one
        → Enters ownership and classification details
        → Cross-references validate against Section 1

Step 5: User moves to Section 3
        → Clicks Section 3 tab
        → Selects jurisdiction from sidebar
        → Enters GloBE Income components
        → System calculates GloBE Income
        → Enters Covered Taxes
        → System calculates ETR
        → Enters SBIE data
        → System calculates Top-up Tax

Step 6: User reviews validation
        → Opens validation panel
        → Reviews errors and warnings
        → Clicks to navigate to problem fields
        → Corrects issues

Step 7: User exports/saves work
        → Clicks Export button
        → Selects format (PDF/JSON/Excel)
        → Downloads summary for reference
```

---

## 8. Edge Cases & Error Handling

### 8.1 Edge Cases

| Scenario | Expected Behavior |
|----------|-------------------|
| Zero GloBE Income | Display warning, ETR shows as 0% |
| Negative GloBE Income | Display warning about loss jurisdiction |
| Missing entity in parent reference | Show validation error, highlight field |
| Duplicate Entity IDs | Prevent save, show error |
| Circular ownership | Detect and display error |
| ETR > 100% | Display warning to verify inputs |

### 8.2 Auto-Save Behavior

| Event | Action |
|-------|--------|
| Field blur | Auto-save field value |
| Tab change | Auto-save section |
| Browser close | Prompt to save changes |
| Session timeout | Auto-save to local storage |

---

## 9. Test Cases

### 9.1 Functional Test Cases

| Test ID | Description | Action | Expected Result |
|---------|-------------|--------|-----------------|
| TC-001 | Load Case Study 1 | Select CS1, click Load | Form populates with GlobalTech data |
| TC-002 | Add new entity | Click Add Entity, enter data | Entity appears in list |
| TC-003 | Calculate GloBE Income | Enter S3.2 values | GloBE Income calculates correctly |
| TC-004 | Cross-reference validation | Enter mismatched UPE | XR-001 shows failure |
| TC-005 | Section completion | Fill all required S1 fields | S1 shows 100% |
| TC-006 | Navigate to error | Click error in validation | Form scrolls to field |

### 9.2 Calculation Test Cases

| Test ID | Inputs | Expected Output |
|---------|--------|-----------------|
| CA-001 | CS1 Ireland S3.2 values | GloBE Income: €32,800,000 |
| CA-002 | CS1 Ireland S3.3 values | Covered Taxes: €3,800,000 |
| CA-003 | CS1 Ireland S3.5 | ETR: 11.59%, Top-up: €1,009,769 |

---

## 10. Accessibility Requirements

| Requirement | Implementation |
|-------------|----------------|
| Keyboard navigation | Tab through fields, section navigation |
| Screen reader | ARIA labels, form field descriptions |
| Error announcement | Errors announced when validation runs |
| Focus management | Focus moves to first error field |
| High contrast | Support high contrast mode |

---

## 11. Technical Notes

### 11.1 Data Storage
- Session storage for in-progress forms
- No server-side persistence
- Export to JSON for external storage

### 11.2 Performance
- Form should remain responsive with 50+ entities
- Calculations complete in <100ms
- Validation runs on field blur and explicit request

---

## 12. Limitations & Scope

This demo tool does **NOT**:
- Generate actual GIR XML files
- Submit to any tax authority
- Store data permanently (session only)
- Replicate exact portal interfaces
- Validate against live XML schemas
- Support all GIR extensions/variations
- Provide official filing capability

This tool is for **learning purposes only**.

---

## 13. Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2024-12-07 | Initial specification |

---

## 14. Appendix: Case Study Data Mapping

### Case Study 1: GlobalTech Manufacturing

| Section | Field | Value |
|---------|-------|-------|
| S1.1.1 | MNE Group Name | GlobalTech Manufacturing Group plc |
| S1.1.3 | UPE Jurisdiction | GB |
| S1.2.1 | Fiscal Year Start | 2024-01-01 |
| S1.2.2 | Fiscal Year End | 2024-12-31 |
| S3.2.8 | Ireland GloBE Income | €32,800,000 |
| S3.3.7 | Ireland Covered Taxes | €3,800,000 |
| S3.4.7 | Ireland Total SBIE | €3,188,000 |
| S3.5.10 | Ireland Net Top-up Tax | €1,009,769 |
