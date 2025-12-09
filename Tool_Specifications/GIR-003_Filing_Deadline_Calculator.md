# GIR-003: Filing Deadline Calculator

## Tool Specification Document (v2 - Renumbered)

**Version:** 2.0
**Status:** Draft
**Last Updated:** 2024-12-08
**Previous ID:** GIR-005

---

## 1. Tool Metadata

| Attribute | Value |
|-----------|-------|
| Tool ID | GIR-003 |
| Tool Name | Filing Deadline Calculator |
| Category | Pillar Two / Compliance Timeline |
| Complexity | Low |
| Estimated Dev Time | 2-3 days |
| Dependencies | None (standalone) |
| Related Tools | All GIR tools (determines when filing must occur) |
| Course Section | Section 7.1 (Filing Overview and Portal Navigation) |

---

## 2. Purpose & Learning Objectives

### 2.1 Purpose

The Filing Deadline Calculator helps learners determine GIR filing deadlines based on fiscal year end date and filing circumstances. It demonstrates the standard 15-month deadline, the 18-month transitional extension for first filing years, and provides jurisdiction-specific guidance.

### 2.2 Learning Objectives

Upon using this tool, learners will be able to:

1. **Calculate** the standard 15-month GIR filing deadline
2. **Identify** when the 18-month transitional extension applies
3. **Understand** jurisdiction-specific deadline variations
4. **Plan** key milestones for GIR preparation
5. **Recognize** the relationship between UPE location and filing obligations

### 2.3 Deadline Framework Overview

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         GIR FILING DEADLINES                                │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  STANDARD DEADLINE:       15 months after fiscal year end                   │
│  FIRST YEAR EXTENSION:    18 months (transitional relief)                   │
│                                                                             │
│  Example (Calendar Year End):                                               │
│                                                                             │
│  FY End: 31 Dec 2024                                                        │
│     │                                                                       │
│     ├──── + 15 months ────→  31 Mar 2026  (Standard)                       │
│     │                                                                       │
│     └──── + 18 months ────→  30 Jun 2026  (First Year Extended)            │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 3. Input Fields

### 3.1 Input Field Specifications

| Field ID | Field Name | Data Type | Required | Validation |
|----------|------------|-----------|----------|------------|
| `fiscal_year_end` | Fiscal Year End Date | Date | Yes | ≥ 31 Dec 2023, ≤ 31 Dec 2030 |
| `filing_jurisdiction` | Filing Jurisdiction | Enum | Yes | Valid jurisdiction code |
| `upe_location` | UPE Location | Enum | Yes | Valid jurisdiction code |
| `is_first_filing` | First GIR Filing Year? | Boolean | Yes | Yes/No |
| `current_date` | Current Date | Date | Auto | System date (can override) |

### 3.2 Jurisdiction Options

| Code | Display | Filing Authority |
|------|---------|------------------|
| UK | United Kingdom | HMRC |
| IE | Ireland | Revenue |
| NL | Netherlands | Belastingdienst |
| DE | Germany | BZSt |
| FR | France | DGFiP |
| CH | Switzerland | Cantonal |
| US | United States | IRS |
| AU | Australia | ATO |
| SG | Singapore | IRAS |
| OTHER | Other | Local authority |

---

## 4. Output Fields

### 4.1 Output Field Specifications

| Field ID | Field Name | Data Type | Format |
|----------|------------|-----------|--------|
| `standard_deadline` | Standard Deadline (15m) | Date | DD Month YYYY |
| `applicable_deadline` | Your Filing Deadline | Date | DD Month YYYY (highlighted) |
| `extension_applied` | Extension Applied | Boolean | Yes/No with reason |
| `days_remaining` | Days Until Deadline | Integer | Countdown with status |
| `jurisdiction_notes` | Jurisdiction Notes | Object | Authority, portal, notes |
| `milestones` | Recommended Milestones | Array | Dates and descriptions |

### 4.2 Days Remaining Visual Indicators

| Days Remaining | Color | Icon | Status |
|----------------|-------|------|--------|
| > 180 days | Green | ✅ | On Track |
| 90-180 days | Yellow | ⚠️ | Plan Ahead |
| 30-90 days | Orange | ⚠️ | Action Required |
| < 30 days | Red | ⚡ | Urgent |
| ≤ 0 | Red | ❌ | Overdue |

---

## 5. Calculation Logic

### 5.1 Deadline Calculation Algorithm

```
FUNCTION CalculateDeadline(fiscal_year_end, is_first_filing):

    // Calculate standard 15-month deadline
    standard_deadline = AddMonths(fiscal_year_end, 15)

    // Apply first-year extension if applicable
    IF is_first_filing:
        applicable_deadline = AddMonths(fiscal_year_end, 18)
        extension_applied = TRUE
        extension_months = 3
    ELSE:
        applicable_deadline = standard_deadline
        extension_applied = FALSE
        extension_months = 0

    // Calculate days remaining
    days_remaining = DaysBetween(Today(), applicable_deadline)

    // Generate milestones
    milestones = GenerateMilestones(applicable_deadline)

    RETURN {
        standard_deadline,
        applicable_deadline,
        extension_applied,
        extension_months,
        days_remaining,
        milestones
    }
```

### 5.2 Milestone Generation

| Milestone | Timing | Description |
|-----------|--------|-------------|
| Data Collection Start | Deadline - 9 months | Begin gathering financial data |
| Safe Harbour Assessment | Deadline - 6 months | Complete GIR-002 tests |
| GloBE Calculations | Deadline - 4 months | Complete GIR-001 calculations |
| Internal Review | Deadline - 2 months | Management sign-off |
| XML Generation | Deadline - 1 month | Generate and validate GIR file |
| **FILING DEADLINE** | Deadline | Submit to tax authority |

### 5.3 Date Arithmetic Examples

| FY End | First Year? | Deadline | Calculation |
|--------|-------------|----------|-------------|
| 31 Dec 2024 | Yes | 30 Jun 2026 | +18 months |
| 31 Dec 2024 | No | 31 Mar 2026 | +15 months |
| 31 Mar 2025 | Yes | 30 Sep 2026 | +18 months |
| 30 Jun 2025 | Yes | 31 Dec 2026 | +18 months |
| 30 Sep 2025 | No | 31 Dec 2026 | +15 months |

---

## 6. User Interface Specifications

### 6.1 Main Layout Wireframe

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  GIR-003: Filing Deadline Calculator                                        │
│  Determine your GIR filing deadline and preparation milestones              │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  INPUT                                                               │   │
│  │                                                                      │   │
│  │  Fiscal Year End:    [📅 31 December 2024_____]                     │   │
│  │                      Quick: [Dec 2024] [Mar 2025] [Jun 2025]        │   │
│  │                                                                      │   │
│  │  Filing Jurisdiction: [United Kingdom ▼]                            │   │
│  │                                                                      │   │
│  │  UPE Location:        [United Kingdom ▼]                            │   │
│  │                                                                      │   │
│  │  First GIR Filing?    (•) Yes - 18 month deadline                   │   │
│  │                       ( ) No - 15 month deadline                    │   │
│  │                                                                      │   │
│  │                    [ Calculate Deadline ]   [ Clear ]                │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
│  ═══════════════════════════════════════════════════════════════════════   │
│                                                                             │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                                                                      │   │
│  │         ┌─────────────────────────────────────────────────┐         │   │
│  │         │           YOUR FILING DEADLINE                  │         │   │
│  │         │                                                 │         │   │
│  │         │              30 JUNE 2026                       │         │   │
│  │         │                                                 │         │   │
│  │         │    ┌─────────────────────────────────────┐     │         │   │
│  │         │    │   ✅  547 DAYS REMAINING            │     │         │   │
│  │         │    └─────────────────────────────────────┘     │         │   │
│  │         │                                                 │         │   │
│  │         │  Standard deadline: 31 March 2026               │         │   │
│  │         │  Extension: +3 months (first year transitional) │         │   │
│  │         └─────────────────────────────────────────────────┘         │   │
│  │                                                                      │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  JURISDICTION INFORMATION                                            │   │
│  │                                                                      │   │
│  │  Filing Authority: HMRC                                              │   │
│  │  Portal: HMRC Online Services                                        │   │
│  │                                                                      │   │
│  │  Notes:                                                              │   │
│  │  • File via HMRC's GIR digital service                              │   │
│  │  • Registration required before first filing                         │   │
│  │  • Penalties: £100 initial + £10/day for late filing                │   │
│  │  • UK implements IIR (2024) and UTPR (2025)                         │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  RECOMMENDED MILESTONES                              [ Expand ▼ ]   │   │
│  │                                                                      │   │
│  │  ──●─────────●─────────●─────────●─────────●─────────◉──            │   │
│  │    │         │         │         │         │         │              │   │
│  │   Sep       Dec       Feb       Apr       May       Jun             │   │
│  │   2025      2025      2026      2026      2026      2026            │   │
│  │    │         │         │         │         │         │              │   │
│  │  Data     Safe      GloBE    Review     XML     DEADLINE            │   │
│  │  Start    Harbour   Calcs              Gen                          │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 6.2 Milestone Detail Table (Expanded)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  MILESTONE DETAILS                                                          │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  | Milestone              | Date         | Days Away | Status    |         │
│  |------------------------|--------------|-----------|-----------|         │
│  | Data Collection Start  | 30 Sep 2025  | 298 days  | ○ Pending |         │
│  | Safe Harbour (GIR-002) | 31 Dec 2025  | 390 days  | ○ Pending |         │
│  | GloBE Calcs (GIR-001)  | 28 Feb 2026  | 449 days  | ○ Pending |         │
│  | Internal Review        | 30 Apr 2026  | 510 days  | ○ Pending |         │
│  | XML Generation         | 31 May 2026  | 541 days  | ○ Pending |         │
│  | FILING DEADLINE        | 30 Jun 2026  | 547 days  | ◉ Target  |         │
│                                                                             │
│  [ Export to Calendar ]  [ Download Timeline PDF ]                          │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 7. Jurisdiction-Specific Information

### 7.1 UK Filing Notes

| Attribute | Value |
|-----------|-------|
| Authority | HMRC |
| Portal | HMRC Online Services |
| IIR Effective | 2024 |
| UTPR Effective | 2025 |
| QDMTT | No |
| Registration | Required within 6 months of first period end |
| Penalties | £100 initial + £10/day late |

### 7.2 Other Key Jurisdictions

| Jurisdiction | Authority | IIR | UTPR | QDMTT |
|--------------|-----------|-----|------|-------|
| Ireland | Revenue | 2024 | 2025 | 2024 |
| Netherlands | Belastingdienst | 2024 | 2025 | 2024 |
| Germany | BZSt | 2024 | 2025 | Partial |
| France | DGFiP | 2024 | 2025 | 2024 |
| Switzerland | Cantonal | N/A | N/A | 2024 |
| Australia | ATO | 2024 | 2025 | No |
| Singapore | IRAS | 2025 | TBD | TBD |
| United States | IRS | No | No | No |

---

## 8. Test Cases

### 8.1 Case Study 1: GlobalTech Manufacturing - UK Filing

**Inputs:**
| Field | Value |
|-------|-------|
| Fiscal Year End | 31 December 2024 |
| Filing Jurisdiction | United Kingdom |
| UPE Location | United Kingdom |
| First GIR Filing | Yes |

**Expected Outputs:**
| Output | Expected Value |
|--------|----------------|
| Standard Deadline | 31 March 2026 |
| Extension Applied | Yes (+3 months) |
| Applicable Deadline | **30 June 2026** |
| Deadline Type | First Filing - Extended |

**Milestones:**
| Milestone | Date |
|-----------|------|
| Data Collection Start | 30 September 2025 |
| Safe Harbour Assessment | 31 December 2025 |
| GloBE Calculations | 28 February 2026 |
| Internal Review | 30 April 2026 |
| XML Generation | 31 May 2026 |
| **FILING DEADLINE** | **30 June 2026** |

### 8.2 Additional Test Cases

| Test ID | FY End | Jurisdiction | First? | Expected Deadline |
|---------|--------|--------------|--------|-------------------|
| TC-001 | 31 Dec 2024 | UK | Yes | 30 Jun 2026 |
| TC-002 | 31 Dec 2025 | UK | No | 31 Mar 2027 |
| TC-003 | 31 Mar 2025 | UK | Yes | 30 Sep 2026 |
| TC-004 | 30 Jun 2024 | IE | Yes | 31 Dec 2025 |
| TC-005 | 30 Sep 2024 | US | Yes | 31 Mar 2026 |
| TC-006 | 28 Feb 2025 | NL | Yes | 31 Aug 2026 |
| TC-007 | 31 Dec 2024 | DE | No | 31 Mar 2026 |

### 8.3 Edge Cases

| Scenario | Input | Expected Behavior |
|----------|-------|-------------------|
| Pre-GloBE FY | FY End: 30 Jun 2023 | Error: "GIR not applicable" |
| Far future | FY End: 31 Dec 2035 | Warning: "Verify date" |
| Deadline passed | Today > Deadline | "OVERDUE" status |
| Today = Deadline | Today = 30 Jun 2026 | "Deadline is TODAY" |

---

## 9. Accessibility Requirements

| Requirement | Implementation |
|-------------|----------------|
| Keyboard Navigation | Tab through fields, date picker accessible |
| Screen Reader | ARIA labels, deadline announced clearly |
| Color Contrast | 4.5:1 minimum |
| Status Communication | Days remaining via text + color + icon |
| Date Format | Locale-appropriate display |

---

## 10. Technical Notes

### 10.1 Data Model

```typescript
interface DeadlineCalculation {
  id: string;
  fiscalYearEnd: Date;
  filingJurisdiction: string;
  upeLocation: string;
  isFirstFiling: boolean;

  standardDeadline: Date;
  applicableDeadline: Date;
  extensionApplied: boolean;
  extensionMonths: number;
  daysRemaining: number;

  jurisdictionNotes: JurisdictionInfo;
  milestones: Milestone[];

  calculatedAt: Date;
}

interface Milestone {
  name: string;
  date: Date;
  description: string;
  isDeadline: boolean;
}
```

### 10.2 Date Handling

- Store dates in ISO 8601 format internally
- Display in user's locale format
- Handle month-end edge cases (e.g., Jan 31 + 1 month = Feb 28/29)

---

## 11. Limitations & Scope

### 11.1 In Scope

- ✅ Standard 15-month deadline calculation
- ✅ First-year 18-month extension
- ✅ Jurisdiction-specific notes
- ✅ Milestone timeline generation
- ✅ Days remaining countdown

### 11.2 Out of Scope

- ❌ Connection to tax authority systems
- ❌ Filing status tracking
- ❌ Deadline reminders/notifications
- ❌ Extension request handling
- ❌ Weekend/holiday adjustments
- ❌ Multi-entity filing calendars

---

## 12. Version History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2024-12-07 | — | Initial specification (as GIR-005) |
| 2.0 | 2024-12-08 | — | Renumbered to GIR-003; updated milestone references to new tool IDs |

---

## 13. Appendix: GIR Deadline Reference Table

| Fiscal Year End | First Year (18m) | Subsequent (15m) |
|-----------------|------------------|------------------|
| 31 Dec 2024 | 30 Jun 2026 | 31 Mar 2026 |
| 31 Mar 2025 | 30 Sep 2026 | 30 Jun 2026 |
| 30 Jun 2025 | 31 Dec 2026 | 30 Sep 2026 |
| 30 Sep 2025 | 31 Mar 2027 | 31 Dec 2026 |
| 31 Dec 2025 | 30 Jun 2027 | 31 Mar 2027 |
| 31 Mar 2026 | 30 Sep 2027 | 30 Jun 2027 |

---

*End of GIR-003 Filing Deadline Calculator Specification*
