# GIR-005: Filing Deadline Calculator - Tool Specification

**Version:** 1.0
**Last Updated:** 2024-12-07
**Status:** Planned
**Platform:** tools.mojitax.com

---

## 1. Tool Metadata

| Field | Value |
|-------|-------|
| Tool ID | GIR-005 |
| Tool Name | GIR Filing Deadline Calculator |
| Category | Pillar Two |
| Form Type | Calculator |
| Status | Planned |
| Used By | GloBE Information Return: Complete Filing Implementation |
| Introduced In | Section 3.1 - Filing Requirements and Deadlines |

---

## 2. Purpose & Learning Objective

### 2.1 Purpose
Practice determining GIR filing deadlines based on fiscal year end date and filing circumstances. This tool helps learners understand the standard 15-month deadline, the 18-month transitional extension for first filing years, and jurisdiction-specific variations.

### 2.2 Learning Objective
After using this tool, learners will be able to:
- Calculate the standard 15-month GIR filing deadline
- Identify when the 18-month transitional extension applies
- Understand jurisdiction-specific deadline variations
- Plan key milestones for GIR preparation (data collection, review, sign-off)
- Recognize the relationship between UPE location and filing obligations

### 2.3 Prerequisites
Learners should understand:
- The GIR filing obligation under Pillar Two
- The role of the Ultimate Parent Entity (UPE) and Designated Filing Entity (DFE)
- Basic concepts of fiscal year end and filing periods

### 2.4 Deadline Framework Overview

```
┌─────────────────────────────────────────────────────────────────┐
│                    GIR FILING DEADLINES                         │
└─────────────────────────────────────────────────────────────────┘

STANDARD DEADLINE: 15 months after fiscal year end

TRANSITIONAL EXTENSION: 18 months for first GIR filing year
(Fiscal years beginning on or after 31 December 2023)

Example Timeline (Calendar Year End):
┌──────────────────────────────────────────────────────────────────┐
│                                                                  │
│  FY End          Standard Deadline      First Year Deadline      │
│  31 Dec 2024  →  31 Mar 2026         →  30 Jun 2026             │
│                  (15 months)             (18 months)             │
│                                                                  │
└──────────────────────────────────────────────────────────────────┘
```

---

## 3. Input Fields

### 3.1 Fiscal Year End Date

| Property | Value |
|----------|-------|
| Field ID | `fiscal_year_end` |
| Label | Fiscal Year End Date |
| Data Type | Date |
| Required | **Yes** |
| Format | DD/MM/YYYY or locale-appropriate |
| Min Value | 31/12/2023 (first eligible GIR period) |
| Max Value | 31/12/2030 (reasonable future limit) |
| Default Value | Empty |
| UI Element | Date picker |
| Placeholder Text | "Select fiscal year end date" |
| Help Text | "The last day of the fiscal year for which the GIR is being filed. For calendar year filers, this is typically 31 December." |

**Validation Rules:**
| Rule | Condition | Error Message |
|------|-----------|---------------|
| Required | Field is empty | "Fiscal Year End Date is required" |
| Valid date | Invalid date format | "Please enter a valid date" |
| Min date | Date < 31/12/2023 | "GIR filing only applies to fiscal years ending on or after 31 December 2024 (beginning on or after 31 December 2023)" |
| Future limit | Date > 31/12/2030 | "Please enter a date within a reasonable range" |

**Common Fiscal Year Ends (for quick selection):**
| Option | Date |
|--------|------|
| Calendar Year 2024 | 31 December 2024 |
| Calendar Year 2025 | 31 December 2025 |
| UK Tax Year 2024/25 | 31 March 2025 |
| US Federal (Sep) | 30 September 2024 |

---

### 3.2 Filing Jurisdiction

| Property | Value |
|----------|-------|
| Field ID | `filing_jurisdiction` |
| Label | Filing Jurisdiction |
| Data Type | String (dropdown selection) |
| Required | **Yes** |
| UI Element | Searchable dropdown |
| Default Value | Empty |
| Help Text | "The jurisdiction where the GIR will be filed. This is typically where the UPE or DFE is located." |

**Dropdown Options (Key Jurisdictions):**
| Code | Display | Notes |
|------|---------|-------|
| UK | United Kingdom | HMRC filing |
| IE | Ireland | Revenue filing |
| NL | Netherlands | Belastingdienst filing |
| DE | Germany | BZSt filing |
| FR | France | DGFiP filing |
| CH | Switzerland | Cantonal filing |
| US | United States | IRS filing |
| AU | Australia | ATO filing |
| JP | Japan | NTA filing |
| SG | Singapore | IRAS filing |
| OTHER | Other jurisdiction | Generic deadlines |

**Validation Rules:**
| Rule | Condition | Error Message |
|------|-----------|---------------|
| Required | No selection made | "Please select a filing jurisdiction" |

---

### 3.3 Is First Filing Year

| Property | Value |
|----------|-------|
| Field ID | `is_first_filing` |
| Label | Is this the group's first GIR filing year? |
| Data Type | Boolean |
| Required | **Yes** |
| UI Element | Toggle switch or Yes/No radio buttons |
| Default Value | Yes (for FY2024) |
| Help Text | "Select 'Yes' if this is the first fiscal year for which the MNE group is required to file a GIR. The first filing year qualifies for an 18-month (instead of 15-month) deadline extension." |

**Display Values:**
| Value | Display Text |
|-------|--------------|
| true | Yes - First GIR filing year (18-month deadline) |
| false | No - Subsequent filing year (15-month deadline) |

**Auto-suggestion Logic:**
- If fiscal year end is in 2024 or early 2025, suggest "Yes" as default
- Display note: "For most groups, FY2024 (ending in 2024 or early 2025) is the first GIR filing year"

---

### 3.4 UPE Location

| Property | Value |
|----------|-------|
| Field ID | `upe_location` |
| Label | UPE Location |
| Data Type | String (dropdown selection) |
| Required | **Yes** |
| UI Element | Searchable dropdown |
| Default Value | Empty |
| Help Text | "The jurisdiction where the Ultimate Parent Entity (UPE) is located. This affects filing obligations and potential local filing requirements." |

**Dropdown Options:** Same as Filing Jurisdiction dropdown

**Validation Rules:**
| Rule | Condition | Error Message |
|------|-----------|---------------|
| Required | No selection made | "Please select the UPE location" |

---

### 3.5 Today's Date (System)

| Property | Value |
|----------|-------|
| Field ID | `current_date` |
| Label | Current Date |
| Data Type | Date |
| Required | **Yes** (auto-populated) |
| UI Element | Read-only display (auto-populated with system date) |
| Help Text | "Today's date, used to calculate days remaining until deadline" |

**Note:** This is automatically set to the current system date. User can optionally override for planning purposes.

---

## 4. Output Fields

### 4.1 Standard Filing Deadline

| Property | Value |
|----------|-------|
| Field ID | `standard_deadline` |
| Label | Standard Deadline (15 months) |
| Data Type | Date |
| Display Format | DD Month YYYY (e.g., "31 March 2026") |
| UI Element | Read-only text |

---

### 4.2 Applicable Filing Deadline

| Property | Value |
|----------|-------|
| Field ID | `applicable_deadline` |
| Label | Your Filing Deadline |
| Data Type | Date |
| Display Format | DD Month YYYY |
| UI Element | Read-only text with large font, highlighted |

**Display Note:** This shows the actual applicable deadline considering first-year extension.

---

### 4.3 Extension Status

| Property | Value |
|----------|-------|
| Field ID | `extension_status` |
| Label | Extension Status |
| Data Type | Object |
| UI Element | Status card |

**Display Components:**
| Component | Description |
|-----------|-------------|
| Extension Applied | Yes/No |
| Extension Type | "18-month transitional extension" or "None" |
| Extension Period | "3 additional months" or "N/A" |
| Reason | "First GIR filing year" or "Subsequent year - standard deadline applies" |

---

### 4.4 Days Until Deadline

| Property | Value |
|----------|-------|
| Field ID | `days_remaining` |
| Label | Days Until Deadline |
| Data Type | Integer |
| UI Element | Countdown display with visual indicator |

**Visual Indicators:**
| Days Remaining | Color | Icon |
|----------------|-------|------|
| > 180 days | Green | ✓ |
| 90-180 days | Yellow | ⚠ |
| 30-90 days | Orange | ⚠ |
| < 30 days | Red | ⚡ |
| Overdue | Red | ✗ |

**Display Format:**
- If positive: "X days remaining"
- If zero: "Deadline is TODAY"
- If negative: "X days OVERDUE"

---

### 4.5 Jurisdiction-Specific Notes

| Property | Value |
|----------|-------|
| Field ID | `jurisdiction_notes` |
| Label | Jurisdiction-Specific Information |
| Data Type | Formatted text |
| UI Element | Information panel |

**Content varies by jurisdiction - see Section 5.2**

---

### 4.6 Key Milestone Dates

| Property | Value |
|----------|-------|
| Field ID | `milestone_dates` |
| Label | Recommended Preparation Milestones |
| Data Type | Array of date/description pairs |
| UI Element | Timeline or table |

**Milestone Template:**
```
┌─────────────────────────────────────────────────────────────────┐
│ RECOMMENDED MILESTONES                                          │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ○ Data Collection Start     [Deadline - 9 months]             │
│    Begin gathering financial data from all entities             │
│                                                                 │
│  ○ Safe Harbour Assessment   [Deadline - 6 months]             │
│    Complete safe harbour qualification tests                    │
│                                                                 │
│  ○ GloBE Calculations        [Deadline - 4 months]             │
│    Complete ETR, SBIE, Top-up Tax calculations                 │
│                                                                 │
│  ○ Internal Review           [Deadline - 2 months]             │
│    Management review and sign-off preparation                   │
│                                                                 │
│  ○ XML Generation            [Deadline - 1 month]              │
│    Generate and validate GIR XML file                          │
│                                                                 │
│  ◉ FILING DEADLINE           [Applicable Deadline]             │
│    Submit GIR to tax authority                                 │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

### 4.7 Filing Obligation Summary

| Property | Value |
|----------|-------|
| Field ID | `filing_summary` |
| Label | Filing Obligation Summary |
| Data Type | Formatted text |
| UI Element | Summary panel |

**Display Format:**
```
FILING SUMMARY
══════════════════════════════════════════════

Fiscal Year:            1 January 2024 - 31 December 2024
Filing Jurisdiction:    United Kingdom
UPE Location:           United Kingdom
Filing Type:            First GIR Filing

Standard Deadline:      31 March 2026 (15 months)
Extension Applied:      Yes - Transitional first year
YOUR DEADLINE:          30 June 2026 (18 months)

Days Remaining:         XXX days

```

---

## 5. Calculation Logic

### 5.1 Deadline Calculation

```
FUNCTION CalculateDeadline(fiscal_year_end, is_first_filing, filing_jurisdiction, upe_location):

    // Validate fiscal year end is within GloBE scope
    globe_start_date = Date("2023-12-31")
    IF fiscal_year_end < globe_start_date THEN
        RETURN Error("GIR filing only applies to fiscal years beginning on or after 31 December 2023")
    END IF

    // Calculate standard 15-month deadline
    standard_deadline = AddMonths(fiscal_year_end, 15)

    // Check for first-year transitional extension
    IF is_first_filing THEN
        // 18-month deadline for first filing year
        applicable_deadline = AddMonths(fiscal_year_end, 18)
        extension_applied = true
        extension_months = 3
    ELSE
        applicable_deadline = standard_deadline
        extension_applied = false
        extension_months = 0
    END IF

    // Check for jurisdiction-specific variations
    jurisdiction_adjustment = GetJurisdictionAdjustment(filing_jurisdiction)
    IF jurisdiction_adjustment IS NOT NULL THEN
        applicable_deadline = ApplyJurisdictionRules(applicable_deadline, jurisdiction_adjustment)
    END IF

    // Calculate days remaining
    current_date = Today()
    days_remaining = DaysBetween(current_date, applicable_deadline)

    // Generate milestone dates
    milestones = GenerateMilestones(applicable_deadline)

    RETURN {
        fiscal_year_end: fiscal_year_end,
        standard_deadline: standard_deadline,
        applicable_deadline: applicable_deadline,
        extension_applied: extension_applied,
        extension_months: extension_months,
        days_remaining: days_remaining,
        milestones: milestones,
        jurisdiction_notes: GetJurisdictionNotes(filing_jurisdiction, upe_location)
    }

END FUNCTION
```

### 5.2 Jurisdiction-Specific Rules

```
FUNCTION GetJurisdictionNotes(filing_jurisdiction, upe_location):

    notes = {
        UK: {
            authority: "HMRC",
            portal: "HMRC Online Services",
            local_deadline_variation: null,
            notes: [
                "File via HMRC's GIR digital service",
                "Registration required before first filing",
                "Penalties apply for late filing: £100 initial + £10/day",
                "UK imposes UTPR from 2025 for non-UK UPE groups"
            ]
        },
        IE: {
            authority: "Revenue Commissioners",
            portal: "ROS (Revenue Online Service)",
            local_deadline_variation: null,
            notes: [
                "File via ROS",
                "Ireland has enacted QDMTT and IIR",
                "Local filing entity must be registered"
            ]
        },
        NL: {
            authority: "Belastingdienst",
            portal: "Mijn Belastingdienst Zakelijk",
            local_deadline_variation: null,
            notes: [
                "Netherlands has enacted comprehensive Pillar Two legislation",
                "QDMTT applies from 2024",
                "IIR applies from 2024, UTPR from 2025"
            ]
        },
        DE: {
            authority: "BZSt (Bundeszentralamt für Steuern)",
            portal: "BZSt Online Portal",
            local_deadline_variation: null,
            notes: [
                "File via BZStOnline",
                "Germany has enacted IIR and UTPR",
                "Separate domestic minimum tax may apply"
            ]
        },
        CH: {
            authority: "Cantonal tax authority",
            portal: "Varies by canton",
            local_deadline_variation: null,
            notes: [
                "Switzerland has enacted QDMTT (Mindeststeuer)",
                "Filing at cantonal level",
                "Different cantons may have different processes"
            ]
        },
        US: {
            authority: "IRS (Internal Revenue Service)",
            portal: "IRS e-file",
            local_deadline_variation: null,
            notes: [
                "US has not yet enacted Pillar Two rules",
                "US MNEs with foreign parents may be subject to UTPR",
                "Monitor IRS guidance for future requirements"
            ]
        },
        OTHER: {
            authority: "Local tax authority",
            portal: "Varies",
            local_deadline_variation: null,
            notes: [
                "Check local implementation of GloBE rules",
                "Deadline may vary - verify with local authority",
                "Some jurisdictions may not have enacted Pillar Two"
            ]
        }
    }

    RETURN notes[filing_jurisdiction] OR notes["OTHER"]

END FUNCTION
```

### 5.3 Milestone Generation

```
FUNCTION GenerateMilestones(applicable_deadline):

    milestones = [
        {
            name: "Data Collection Start",
            date: SubtractMonths(applicable_deadline, 9),
            description: "Begin gathering financial data from all constituent entities"
        },
        {
            name: "Safe Harbour Assessment",
            date: SubtractMonths(applicable_deadline, 6),
            description: "Complete safe harbour qualification tests for eligible jurisdictions"
        },
        {
            name: "GloBE Calculations Complete",
            date: SubtractMonths(applicable_deadline, 4),
            description: "Complete ETR, SBIE, and Top-up Tax calculations for all jurisdictions"
        },
        {
            name: "Internal Review",
            date: SubtractMonths(applicable_deadline, 2),
            description: "Management review, governance sign-off, and documentation"
        },
        {
            name: "XML Generation & Validation",
            date: SubtractMonths(applicable_deadline, 1),
            description: "Generate GIR XML file and validate against schema"
        },
        {
            name: "FILING DEADLINE",
            date: applicable_deadline,
            description: "Submit GIR to tax authority",
            is_deadline: true
        }
    ]

    RETURN milestones

END FUNCTION
```

### 5.4 Date Arithmetic Rules

| Operation | Rule |
|-----------|------|
| AddMonths | Add calendar months, adjust to last day if necessary |
| End of month | If FY end is 31st, deadline is last day of target month |
| Weekend/holiday | No automatic adjustment (user should verify with authority) |

**Examples:**
| FY End | + 15 months | + 18 months |
|--------|-------------|-------------|
| 31 Dec 2024 | 31 Mar 2026 | 30 Jun 2026 |
| 31 Mar 2025 | 30 Jun 2026 | 30 Sep 2026 |
| 30 Jun 2024 | 30 Sep 2025 | 31 Dec 2025 |
| 28 Feb 2025 | 31 May 2026 | 31 Aug 2026 |

---

## 6. User Interface Specifications

### 6.1 Layout Structure

```
┌─────────────────────────────────────────────────────────────────┐
│  GIR Filing Deadline Calculator                            [?]  │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │ INPUT SECTION                                            │   │
│  ├─────────────────────────────────────────────────────────┤   │
│  │                                                          │   │
│  │  Fiscal Year End:  [📅 31/12/2024        ]              │   │
│  │                    Common: [2024] [2025] [Mar] [Sep]     │   │
│  │                                                          │   │
│  │  Filing            [United Kingdom          ▼]          │   │
│  │  Jurisdiction:                                           │   │
│  │                                                          │   │
│  │  UPE Location:     [United Kingdom          ▼]          │   │
│  │                                                          │   │
│  │  First GIR         ○ Yes (18-month deadline)            │   │
│  │  Filing Year:      ○ No (15-month deadline)             │   │
│  │                                                          │   │
│  │  [  Calculate Deadline  ]    [  Clear  ]                │   │
│  │                                                          │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                 │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │ RESULTS SECTION                                          │   │
│  ├─────────────────────────────────────────────────────────┤   │
│  │                                                          │   │
│  │  ┌─────────────────────────────────────────────┐        │   │
│  │  │         YOUR FILING DEADLINE                │        │   │
│  │  │                                             │        │   │
│  │  │           30 JUNE 2026                      │        │   │
│  │  │                                             │        │   │
│  │  │    ┌────────────────────────────────┐      │        │   │
│  │  │    │  🟢 547 DAYS REMAINING         │      │        │   │
│  │  │    └────────────────────────────────┘      │        │   │
│  │  │                                             │        │   │
│  │  │  Standard deadline: 31 March 2026           │        │   │
│  │  │  Extension applied: +3 months (first year)  │        │   │
│  │  └─────────────────────────────────────────────┘        │   │
│  │                                                          │   │
│  │  JURISDICTION INFORMATION                               │   │
│  │  ┌─────────────────────────────────────────────┐        │   │
│  │  │ Filing Authority: HMRC                      │        │   │
│  │  │ Portal: HMRC Online Services                │        │   │
│  │  │                                             │        │   │
│  │  │ Notes:                                      │        │   │
│  │  │ • File via HMRC's GIR digital service      │        │   │
│  │  │ • Registration required before first filing │        │   │
│  │  │ • Penalties: £100 initial + £10/day late   │        │   │
│  │  └─────────────────────────────────────────────┘        │   │
│  │                                                          │   │
│  │  [▼ Show Recommended Milestones]                        │   │
│  │                                                          │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### 6.2 Milestone Timeline (Expandable)

```
┌─────────────────────────────────────────────────────────────────┐
│ RECOMMENDED PREPARATION MILESTONES                              │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ──●────────●────────●────────●────────●────────◉──            │
│    │        │        │        │        │        │              │
│    │        │        │        │        │        │              │
│   Sep      Dec      Feb      Apr      May      Jun             │
│   2025     2025     2026     2026     2026     2026            │
│    │        │        │        │        │        │              │
│    │        │        │        │        │        │              │
│  Data    Safe     GloBE   Internal   XML    DEADLINE           │
│  Start   Harbour  Calcs   Review    Gen     30 Jun             │
│                                                                 │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │ Milestone          │ Date        │ Days Away │ Status    │  │
│  ├────────────────────┼─────────────┼───────────┼───────────┤  │
│  │ Data Collection    │ 30 Sep 2025 │ 298 days  │ ○ Pending │  │
│  │ Safe Harbour       │ 31 Dec 2025 │ 390 days  │ ○ Pending │  │
│  │ GloBE Calculations │ 28 Feb 2026 │ 449 days  │ ○ Pending │  │
│  │ Internal Review    │ 30 Apr 2026 │ 510 days  │ ○ Pending │  │
│  │ XML Generation     │ 31 May 2026 │ 541 days  │ ○ Pending │  │
│  │ FILING DEADLINE    │ 30 Jun 2026 │ 547 days  │ ◉ Target  │  │
│  └──────────────────────────────────────────────────────────┘  │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### 6.3 Button Specifications

**Calculate Deadline Button:**
| Property | Value |
|----------|-------|
| Label | "Calculate Deadline" |
| Type | Primary |
| Color | Blue (#007BFF) |
| Behavior | Validates inputs, calculates deadline, displays results |

**Clear Button:**
| Property | Value |
|----------|-------|
| Label | "Clear" |
| Type | Secondary |
| Color | Grey (#6C757D) |
| Behavior | Clears all inputs and results |

### 6.4 Responsive Behavior

| Viewport | Layout |
|----------|--------|
| Desktop (>992px) | Side-by-side input/results |
| Tablet (768-992px) | Stacked panels |
| Mobile (<768px) | Single column, timeline simplified |

---

## 7. User Flow

### 7.1 Happy Path Flow

```
Step 1: User navigates to Filing Deadline Calculator
        → Page loads with empty fields
        → First Filing Year defaults to "Yes" for current period

Step 2: User selects Fiscal Year End Date
        → Can use date picker or quick select buttons
        → e.g., selects 31 December 2024

Step 3: User selects Filing Jurisdiction
        → e.g., selects United Kingdom

Step 4: User selects UPE Location
        → e.g., selects United Kingdom

Step 5: User confirms First Filing Year status
        → Yes = 18-month deadline
        → No = 15-month deadline

Step 6: User clicks "Calculate Deadline"
        → System calculates applicable deadline
        → Days remaining countdown displays
        → Jurisdiction notes display
        → Milestones available via expansion

Step 7: User reviews results
        → Notes the deadline date
        → Reviews recommended milestones
        → Can expand for jurisdiction-specific guidance
```

---

## 8. Edge Cases & Error Handling

### 8.1 Edge Cases

| Scenario | Inputs | Expected Behavior |
|----------|--------|-------------------|
| Pre-GloBE fiscal year | FY End: 30 Jun 2023 | Error: "GIR not applicable for this period" |
| Far future date | FY End: 31 Dec 2035 | Warning: "Please verify - this is far in the future" |
| Deadline already passed | FY End in past, deadline < today | Show "OVERDUE" status with negative days |
| Same day as deadline | Today = deadline | Show "Deadline is TODAY" |
| Non-standard FY end | FY End: 15 Mar 2025 | Calculate normally (15 Jun 2026 or 15 Sep 2026) |
| UPE in non-implementing jurisdiction | UPE: US | Show note about US implementation status |

### 8.2 Warning Messages (Non-blocking)

| Condition | Warning Message |
|-----------|-----------------|
| Deadline < 90 days away | "⚠ Deadline approaching - less than 90 days remaining" |
| Deadline < 30 days away | "⚡ URGENT: Less than 30 days until deadline" |
| Deadline passed | "✗ OVERDUE: Filing deadline has passed" |
| Far future date | "Please verify this fiscal year end date is correct" |

### 8.3 Error Messages

| Error Code | Trigger | User Message |
|------------|---------|--------------|
| ERR_001 | FY End empty | "Fiscal Year End Date is required" |
| ERR_002 | Invalid date | "Please enter a valid date" |
| ERR_003 | Pre-GloBE date | "GIR filing applies to fiscal years beginning on or after 31 December 2023" |
| ERR_004 | Filing jurisdiction empty | "Please select a filing jurisdiction" |
| ERR_005 | UPE location empty | "Please select the UPE location" |
| ERR_006 | First filing not selected | "Please indicate if this is the first GIR filing year" |

---

## 9. Test Cases

### 9.1 Functional Test Cases

| Test ID | Description | Inputs | Expected Output | Source |
|---------|-------------|--------|-----------------|--------|
| TC-001 | UK Calendar Year First Filing | FY: 31 Dec 2024, Jurisdiction: UK, UPE: UK, First: Yes | Deadline: 30 Jun 2026 (18 months) | Case Study 1 |
| TC-002 | UK Calendar Year Subsequent | FY: 31 Dec 2025, Jurisdiction: UK, UPE: UK, First: No | Deadline: 31 Mar 2027 (15 months) | Standard |
| TC-003 | March Year End First Filing | FY: 31 Mar 2025, Jurisdiction: UK, UPE: UK, First: Yes | Deadline: 30 Sep 2026 (18 months) | Variation |
| TC-004 | June Year End | FY: 30 Jun 2024, Jurisdiction: IE, UPE: IE, First: Yes | Deadline: 31 Dec 2025 (18 months) | Variation |
| TC-005 | September Year End | FY: 30 Sep 2024, Jurisdiction: US, UPE: US, First: Yes | Deadline: 31 Mar 2026 (18 months) | Variation |
| TC-006 | Non-calendar year | FY: 28 Feb 2025, Jurisdiction: NL, UPE: NL, First: Yes | Deadline: 31 Aug 2026 (18 months) | Edge case |

### 9.2 Date Arithmetic Test Cases

| Test ID | FY End | First Filing | Expected Deadline |
|---------|--------|--------------|-------------------|
| DA-001 | 31 Dec 2024 | Yes | 30 Jun 2026 |
| DA-002 | 31 Dec 2024 | No | 31 Mar 2026 |
| DA-003 | 31 Mar 2025 | Yes | 30 Sep 2026 |
| DA-004 | 30 Jun 2025 | Yes | 31 Dec 2026 |
| DA-005 | 30 Sep 2025 | No | 31 Dec 2026 |
| DA-006 | 28 Feb 2025 | Yes | 31 Aug 2026 |
| DA-007 | 31 Jan 2025 | Yes | 31 Jul 2026 |

### 9.3 Days Remaining Test Cases

| Test ID | Deadline | Current Date | Expected Days |
|---------|----------|--------------|---------------|
| DR-001 | 30 Jun 2026 | 1 Jan 2025 | 546 |
| DR-002 | 30 Jun 2026 | 30 Jun 2026 | 0 ("TODAY") |
| DR-003 | 30 Jun 2026 | 1 Jul 2026 | -1 ("OVERDUE") |
| DR-004 | 31 Mar 2026 | 1 Jan 2026 | 89 |

### 9.4 Validation Test Cases

| Test ID | Description | Input | Expected Result |
|---------|-------------|-------|-----------------|
| VT-001 | Empty FY End | fiscal_year_end = "" | ERR_001 displayed |
| VT-002 | Pre-GloBE date | fiscal_year_end = 31/12/2022 | ERR_003 displayed |
| VT-003 | No jurisdiction | filing_jurisdiction = "" | ERR_004 displayed |
| VT-004 | Valid inputs | All fields valid | Calculation runs |

---

## 10. Accessibility Requirements

| Requirement | Implementation |
|-------------|----------------|
| Keyboard navigation | All inputs accessible via Tab, date picker keyboard-friendly |
| Screen reader | ARIA labels on all fields, deadline announced clearly |
| Color contrast | Minimum 4.5:1 for text |
| Status indicators | Days remaining communicated via text AND color |
| Date format | Support locale-appropriate date formats |

---

## 11. Technical Notes

### 11.1 Dependencies
- Date library for date arithmetic (e.g., date-fns, moment.js)
- No external APIs required
- No data persistence required

### 11.2 Performance
- Calculation should complete in <50ms
- No network requests during calculation

### 11.3 Browser Support
- Chrome (latest 2 versions)
- Firefox (latest 2 versions)
- Safari (latest 2 versions)
- Edge (latest 2 versions)

### 11.4 Date Handling
- Store dates in ISO 8601 format internally
- Display in user's locale format
- Handle month-end edge cases correctly

---

## 12. Limitations & Scope

This demo tool does **NOT**:
- Connect to tax authority systems to verify actual deadlines
- Track actual filing status or submissions
- Send deadline reminders or notifications
- Account for all possible jurisdiction-specific variations
- Handle extension requests or late filing applications
- Provide legal advice on deadline compliance
- Consider weekends/holidays for deadline adjustments
- Track multiple entities or group-wide filing calendars

This tool is for **learning purposes only** to understand GIR filing deadline calculations.

---

## 13. Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2024-12-07 | Initial specification |

---

## 14. Appendix: Case Study Alignment

### Case Study 1: GlobalTech Manufacturing

**Filing Deadline Scenario:**
- To be added to Sample_Data.md:
  - Fiscal Year End: 31 December 2024
  - Filing Jurisdiction: United Kingdom
  - UPE Location: United Kingdom
  - First GIR Filing Year: Yes

- Expected Outcomes:
  - Standard Deadline: 31 March 2026
  - Extension: Yes (+3 months for first year)
  - Applicable Deadline: 30 June 2026
  - Filing Authority: HMRC

---

## 15. Appendix: GIR Deadline Reference Table

| Fiscal Year End | First Year Deadline (18m) | Subsequent Deadline (15m) |
|-----------------|--------------------------|---------------------------|
| 31 Dec 2024 | 30 Jun 2026 | 31 Mar 2026 |
| 31 Mar 2025 | 30 Sep 2026 | 30 Jun 2026 |
| 30 Jun 2025 | 31 Dec 2026 | 30 Sep 2026 |
| 30 Sep 2025 | 31 Mar 2027 | 31 Dec 2026 |
| 31 Dec 2025 | 30 Jun 2027 | 31 Mar 2027 |
| 31 Mar 2026 | 30 Sep 2027 | 30 Jun 2027 |

---

## 16. Appendix: Jurisdiction Implementation Status

| Jurisdiction | IIR | UTPR | QDMTT | GIR Filing Portal |
|--------------|-----|------|-------|-------------------|
| United Kingdom | 2024 | 2025 | No | HMRC Online |
| Ireland | 2024 | 2025 | 2024 | ROS |
| Netherlands | 2024 | 2025 | 2024 | Belastingdienst |
| Germany | 2024 | 2025 | Partial | BZStOnline |
| France | 2024 | 2025 | 2024 | DGFiP |
| Switzerland | N/A | N/A | 2024 | Cantonal |
| United States | No | No | No | TBD |
| Australia | 2024 | 2025 | No | ATO Online |

**Note:** Implementation dates are indicative and subject to change. Verify with local authorities.
