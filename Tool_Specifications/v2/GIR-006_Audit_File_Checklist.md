# GIR-006: Audit File Checklist

## Tool Specification Document (v2 - Renumbered)

**Version:** 2.0
**Status:** Draft
**Last Updated:** 2024-12-08
**Previously:** GIR-009 (Audit File Checklist)

---

## 1. Tool Metadata

| Attribute | Value |
|-----------|-------|
| Tool ID | GIR-006 |
| Tool Name | Audit File Checklist |
| Category | Compliance / Documentation |
| Complexity | Medium |
| Estimated Dev Time | 3-4 days |
| Dependencies | None (standalone tool) |
| Related Tools | GIR-004 (GIR Practice Form) |
| Course Section | Section 6 - Documentation and Audit Readiness |

---

## 2. Purpose & Learning Objectives

### 2.1 Purpose

The Audit File Checklist provides MNE groups with a comprehensive, interactive checklist to ensure they have assembled all required documentation to support their GloBE Information Return filing. This tool helps tax professionals systematically verify that their audit file is complete, properly organized, and compliant with Pillar Two documentation requirements.

### 2.2 Learning Objectives

Upon using this tool, learners will be able to:

1. **Identify** all documentation categories required for GIR audit compliance
2. **Organize** supporting documentation according to regulatory expectations
3. **Assess** the completeness of their GIR audit file before submission
4. **Understand** the relationship between GIR data points and supporting evidence
5. **Prepare** for potential tax authority inquiries with proper documentation
6. **Generate** gap analysis reports to prioritize outstanding items

### 2.3 Why This Tool is Separate

The Audit File Checklist remains separate from other tools because:

| Reason | Explanation |
|--------|-------------|
| **Different Purpose** | Documentation tracking vs. calculation or form filling |
| **Post-Preparation Activity** | Used after GIR is prepared, before/after submission |
| **Audit Defense Focus** | Supports tax authority inquiries, not GIR completion |
| **Independent Workflow** | Can be used across multiple filing periods |
| **External Stakeholders** | Used by auditors, reviewers, and management separately |

### 2.4 Target Users

- Tax compliance professionals preparing GIR submissions
- Tax managers overseeing Pillar Two compliance
- External auditors reviewing GIR documentation
- Students learning GIR documentation requirements

---

## 3. Input Fields

### 3.1 Setup Information

| Field ID | Field Name | Data Type | Required | Default | Validation |
|----------|------------|-----------|----------|---------|------------|
| `audit_entity_name` | Entity/Group Name | String | Yes | — | 1-200 characters |
| `audit_fiscal_year` | Fiscal Year | Integer | Yes | Current year - 1 | 2024-2100 |
| `audit_jurisdiction_count` | Number of Jurisdictions | Integer | Yes | — | 1-250 |
| `audit_filing_entity` | Filing Entity Name | String | Yes | — | 1-200 characters |
| `audit_gir_status` | GIR Filing Status | Enum | Yes | DRAFT | See 3.2 |
| `audit_date` | Audit Date | Date | No | Today | Valid date |

### 3.2 GIR Filing Status Options

| Value | Display Label |
|-------|---------------|
| `DRAFT` | Draft - Not yet filed |
| `PREPARED` | Prepared - Ready for review |
| `SUBMITTED` | Submitted - Filed with authority |
| `AMENDED` | Amended - Revision filed |

### 3.3 Checklist Section Configuration

| Field ID | Field Name | Data Type | Required | Default |
|----------|------------|-----------|----------|---------|
| `include_section_1` | Include Section 1 (General Information) | Boolean | No | true |
| `include_section_2` | Include Section 2 (Corporate Structure) | Boolean | No | true |
| `include_section_3` | Include Section 3 (GloBE Computation) | Boolean | No | true |
| `include_elections` | Include Elections Documentation | Boolean | No | true |
| `include_safe_harbour` | Include Safe Harbour Documentation | Boolean | No | true |
| `include_system_controls` | Include System/Process Documentation | Boolean | No | true |

---

## 4. Output Fields

### 4.1 Checklist Summary

| Field ID | Field Name | Data Type | Format |
|----------|------------|-----------|--------|
| `total_items` | Total Checklist Items | Integer | Plain number |
| `completed_items` | Completed Items | Integer | Plain number |
| `incomplete_items` | Incomplete Items | Integer | Plain number |
| `na_items` | Not Applicable Items | Integer | Plain number |
| `completion_percentage` | Completion Rate | Decimal | Percentage (e.g., "71.4%") |
| `overall_status` | Overall Audit Status | Enum | Status badge |

### 4.2 Overall Status Values

| Status | Condition | Display |
|--------|-----------|---------|
| `COMPLETE` | completion_percentage = 100% | ✅ Complete |
| `SUBSTANTIALLY_COMPLETE` | completion_percentage >= 90% | 🟡 Substantially Complete |
| `IN_PROGRESS` | completion_percentage >= 50% | 🔵 In Progress |
| `INCOMPLETE` | completion_percentage < 50% | 🔴 Incomplete |

### 4.3 Category Breakdown

| Field ID | Field Name | Data Type |
|----------|------------|-----------|
| `section_1_status` | Section 1 Completion | Object {completed, total, percentage} |
| `section_2_status` | Section 2 Completion | Object {completed, total, percentage} |
| `section_3_status` | Section 3 Completion | Object {completed, total, percentage} |
| `elections_status` | Elections Completion | Object {completed, total, percentage} |
| `safe_harbour_status` | Safe Harbour Completion | Object {completed, total, percentage} |
| `controls_status` | Controls Completion | Object {completed, total, percentage} |

### 4.4 Export Outputs

| Field ID | Field Name | Format |
|----------|------------|--------|
| `checklist_pdf` | Downloadable Checklist | PDF report |
| `checklist_excel` | Excel Tracker | .xlsx workbook |
| `gap_report` | Gap Analysis Report | PDF summary |

---

## 5. Checklist Categories and Items

### 5.1 Section 1: General Information Documentation (10 items)

| Item ID | Checklist Item | Priority | GIR Reference |
|---------|----------------|----------|---------------|
| S1-001 | UPE identification documents (certificate of incorporation, tax registration) | Critical | 1.1.1-1.1.4 |
| S1-002 | Group organizational chart showing ownership structure | Critical | 1.2.x |
| S1-003 | Designated Filing Entity appointment documentation | Critical | 1.3.x |
| S1-004 | Fiscal year determination memorandum | High | 1.4.x |
| S1-005 | Consolidated revenue documentation (prior 2 of 4 years) | Critical | 1.5.x |
| S1-006 | €750M threshold analysis workpaper | Critical | 1.5.x |
| S1-007 | List of all Constituent Entities with jurisdiction mapping | Critical | 1.6.x |
| S1-008 | Excluded Entity classification analysis | High | 1.7.x |
| S1-009 | Joint Venture identification and ownership documentation | Medium | 1.8.x |
| S1-010 | Minority-Owned Constituent Entity analysis | Medium | 1.9.x |

### 5.2 Section 2: Corporate Structure Documentation (10 items)

| Item ID | Checklist Item | Priority | GIR Reference |
|---------|----------------|----------|---------------|
| S2-001 | Complete entity listing with TIN/LEI identifiers | Critical | 2.1.x |
| S2-002 | Ownership percentage schedules for all entities | Critical | 2.2.x |
| S2-003 | Entity classification memoranda (PE, JV, MOCE, etc.) | High | 2.3.x |
| S2-004 | Transparent entity analysis and flow-through documentation | High | 2.4.x |
| S2-005 | Reverse hybrid entity identification | Medium | 2.5.x |
| S2-006 | Stateless entity analysis | Medium | 2.6.x |
| S2-007 | Investment entity classification documentation | Medium | 2.7.x |
| S2-008 | Tax transparent structure diagrams | High | 2.8.x |
| S2-009 | Changes in group structure during fiscal year | High | 2.9.x |
| S2-010 | Acquisitions/dispositions documentation | Medium | 2.10.x |

### 5.3 Section 3: GloBE Computation Documentation (18 items)

| Item ID | Checklist Item | Priority | GIR Reference |
|---------|----------------|----------|---------------|
| S3-001 | Financial accounting net income by jurisdiction | Critical | 3.1.x |
| S3-002 | GloBE Income adjustments workpapers | Critical | 3.2.x |
| S3-003 | Policy choice memorandum | High | 3.3.x |
| S3-004 | Excluded dividend documentation | High | 3.4.x |
| S3-005 | Excluded equity gain/loss calculations | High | 3.5.x |
| S3-006 | Asymmetric foreign currency gain/loss analysis | Medium | 3.6.x |
| S3-007 | Stock-based compensation adjustment workpapers | Medium | 3.7.x |
| S3-008 | Prior period error and accounting changes documentation | Medium | 3.8.x |
| S3-009 | Adjusted Covered Taxes calculation workpapers | Critical | 3.10.x |
| S3-010 | Current tax expense reconciliation to GloBE taxes | Critical | 3.11.x |
| S3-011 | Deferred tax adjustment schedules | High | 3.12.x |
| S3-012 | Qualified Refundable Tax Credit analysis | High | 3.13.x |
| S3-013 | Non-Qualified Refundable Tax Credit documentation | Medium | 3.14.x |
| S3-014 | ETR calculation workpapers by jurisdiction | Critical | 3.15.x |
| S3-015 | SBIE calculation workpapers (payroll, assets) | Critical | 3.16.x |
| S3-016 | Top-up Tax computation by jurisdiction | Critical | 3.17.x |
| S3-017 | QDMTT calculation (if applicable) | High | 3.18.x |
| S3-018 | IIR/UTPR allocation workpapers | High | 3.19.x |

### 5.4 Elections Documentation (10 items)

| Item ID | Checklist Item | Priority | GIR Reference |
|---------|----------------|----------|---------------|
| EL-001 | Election inventory listing all elections made | Critical | Various |
| EL-002 | Stock-based compensation election documentation | High | Election 1 |
| EL-003 | Eligible distribution tax system election | High | Election 2 |
| EL-004 | Aggregate partnership allocation election | Medium | Election 3 |
| EL-005 | QDMTT Safe Harbour election documentation | High | Election 4 |
| EL-006 | Transitional CbCR Safe Harbour election | High | Election 5 |
| EL-007 | Annual election vs. Five-year election documentation | Medium | Various |
| EL-008 | Election effective date tracking schedule | High | Various |
| EL-009 | Election revocation documentation (if any) | Medium | Various |
| EL-010 | Board/committee approval for key elections | High | Various |

### 5.5 Safe Harbour Documentation (8 items)

| Item ID | Checklist Item | Priority | GIR Reference |
|---------|----------------|----------|---------------|
| SH-001 | Transitional CbCR Safe Harbour qualification analysis | Critical | SH Section |
| SH-002 | Qualified CbCR report supporting Safe Harbour | Critical | SH Section |
| SH-003 | De Minimis Test calculation (Revenue < €10M, Profit < €1M) | High | Test 1 |
| SH-004 | Simplified ETR Test calculation with threshold analysis | High | Test 2 |
| SH-005 | Routine Profits Test workpaper | High | Test 3 |
| SH-006 | Jurisdiction-by-jurisdiction Safe Harbour determination | Critical | SH Section |
| SH-007 | CbCR to Financial Statement reconciliation | High | SH Section |
| SH-008 | Safe Harbour transitional period tracking | Medium | SH Section |

### 5.6 System and Process Controls Documentation (10 items)

| Item ID | Checklist Item | Priority | GIR Reference |
|---------|----------------|----------|---------------|
| CT-001 | GloBE data collection process documentation | High | N/A |
| CT-002 | Chart of accounts mapping to GIR data points | High | N/A |
| CT-003 | Source system to GIR data flow diagrams | Medium | N/A |
| CT-004 | Manual adjustment approval process | High | N/A |
| CT-005 | Data validation and reconciliation procedures | High | N/A |
| CT-006 | Calculation engine/tool documentation | Medium | N/A |
| CT-007 | Review and sign-off workflow documentation | High | N/A |
| CT-008 | Audit trail and change log | High | N/A |
| CT-009 | Training documentation for GIR preparers | Medium | N/A |
| CT-010 | SOX/internal control documentation (if applicable) | Medium | N/A |

---

## 6. Calculation Logic

### 6.1 Completion Percentage Calculation

```
FUNCTION calculateCompletionPercentage(checklistItems):

    applicableItems = FILTER items WHERE status != 'NOT_APPLICABLE'
    completedItems = FILTER applicableItems WHERE status = 'COMPLETE'

    IF COUNT(applicableItems) = 0:
        RETURN 100%  // All items marked N/A

    completionPercentage = (COUNT(completedItems) / COUNT(applicableItems)) * 100

    RETURN ROUND(completionPercentage, 1)
```

### 6.2 Overall Status Determination

```
FUNCTION determineOverallStatus(completionPercentage, criticalItemsComplete):

    // Critical items must all be complete for COMPLETE status
    IF completionPercentage = 100 AND criticalItemsComplete = TRUE:
        RETURN "COMPLETE"

    IF completionPercentage >= 90:
        RETURN "SUBSTANTIALLY_COMPLETE"

    IF completionPercentage >= 50:
        RETURN "IN_PROGRESS"

    RETURN "INCOMPLETE"
```

### 6.3 Category Status Calculation

```
FUNCTION calculateCategoryStatus(categoryItems):

    total = COUNT(categoryItems WHERE status != 'NOT_APPLICABLE')
    completed = COUNT(categoryItems WHERE status = 'COMPLETE')
    percentage = (completed / total) * 100 IF total > 0 ELSE 100

    RETURN {
        completed: completed,
        total: total,
        percentage: ROUND(percentage, 1)
    }
```

### 6.4 Gap Analysis Generation

```
FUNCTION generateGapAnalysis(checklistItems):

    gaps = []

    FOR EACH item IN checklistItems:
        IF item.status = 'INCOMPLETE' OR item.status = 'PENDING':
            gap = {
                item_id: item.id,
                description: item.description,
                priority: item.priority,
                gir_reference: item.gir_reference,
                recommended_action: getRecommendedAction(item)
            }
            APPEND gap TO gaps

    // Sort by priority (Critical > High > Medium > Low)
    SORT gaps BY priority DESC

    RETURN gaps
```

---

## 7. User Interface Specifications

### 7.1 Main Layout

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  GIR-006: Audit File Checklist                                              │
│  Ensure your GloBE documentation is complete and audit-ready                │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  SETUP INFORMATION                                                   │   │
│  │                                                                      │   │
│  │  Entity/Group Name: [GlobalTech Manufacturing Ltd______________]    │   │
│  │                                                                      │   │
│  │  Fiscal Year: [2024]  Jurisdictions: [20]  Filing Status: [Draft▼]  │   │
│  │                                                                      │   │
│  │  Filing Entity: [GlobalTech Manufacturing Ltd__________________]    │   │
│  │                                                                      │   │
│  │  Sections to Include:                                               │   │
│  │  ☑ Section 1  ☑ Section 2  ☑ Section 3                              │   │
│  │  ☑ Elections  ☑ Safe Harbour  ☑ Controls                            │   │
│  │                                                                      │   │
│  │                              [ Start Checklist ]                     │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 7.2 Progress Dashboard

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  AUDIT FILE CHECKLIST - GlobalTech Manufacturing Ltd                        │
│  FY 2024 | 20 Jurisdictions | Status: DRAFT - First Filing                  │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  OVERALL PROGRESS                                                    │   │
│  │                                                                      │   │
│  │  ████████████████████████████████████░░░░░░░░░░░░░  71.4%           │   │
│  │                                                                      │   │
│  │  45 of 63 items complete   |   18 incomplete   |   3 N/A            │   │
│  │                                                                      │   │
│  │  Status: 🔵 IN PROGRESS                                              │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  CATEGORY BREAKDOWN                                                  │   │
│  │                                                                      │   │
│  │  Section 1 - General Information     ████████████████████  100%  ✅  │   │
│  │  Section 2 - Corporate Structure     ████████████████░░░░   80%     │   │
│  │  Section 3 - GloBE Computation       ███████████████░░░░░   78%     │   │
│  │  Elections Documentation             ██████░░░░░░░░░░░░░░   30%     │   │
│  │  Safe Harbour Documentation          ████████████░░░░░░░░   63%     │   │
│  │  System & Process Controls           ██████████░░░░░░░░░░   50%     │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
│  [ View Full Checklist ]  [ Gap Analysis ]  [ Export PDF ]  [ Export XLS ] │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 7.3 Interactive Checklist View

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  SECTION 3: GloBE COMPUTATION DOCUMENTATION                    78% Complete │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  Filter: [All ▼]  Priority: [All ▼]  Status: [All ▼]    🔍 [Search...]     │
│                                                                             │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                                                                      │   │
│  │  ✅ S3-001  Financial accounting net income by jurisdiction          │   │
│  │             Priority: Critical  |  GIR Ref: 3.1.x                    │   │
│  │             Notes: [Uploaded: GL_Extract_2024.xlsx]                  │   │
│  │  ─────────────────────────────────────────────────────────────────  │   │
│  │  ✅ S3-002  GloBE Income adjustments workpapers                      │   │
│  │             Priority: Critical  |  GIR Ref: 3.2.x                    │   │
│  │             Notes: [Uploaded: GloBE_Adjustments_WP.pdf]              │   │
│  │  ─────────────────────────────────────────────────────────────────  │   │
│  │  ⬜ S3-003  Policy choice memorandum                                 │   │
│  │             Priority: High  |  GIR Ref: 3.3.x                        │   │
│  │             Notes: [Draft memo for stock comp treatment]             │   │
│  │             ⚠️ Missing - Required for audit readiness               │   │
│  │  ─────────────────────────────────────────────────────────────────  │   │
│  │  ⬜ S3-009  Adjusted Covered Taxes calculation workpapers            │   │
│  │             Priority: Critical  |  GIR Ref: 3.10.x                   │   │
│  │             Notes: [Complete tax reconciliation for CH]              │   │
│  │             🔴 CRITICAL - Must complete before submission           │   │
│  │                                                                      │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
│  Legend: ✅ Complete  ⬜ Incomplete  ➖ Not Applicable  ⏳ In Progress       │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 7.4 Gap Analysis Report

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  GAP ANALYSIS REPORT                                                        │
│  GlobalTech Manufacturing Ltd | FY 2024 | Generated: 2024-12-08             │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  SUMMARY                                                                    │
│  ═══════════════════════════════════════════════════════════════════════   │
│  Total Gaps Identified: 18                                                  │
│  Critical Priority: 2  |  High Priority: 8  |  Medium Priority: 8          │
│                                                                             │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  🔴 CRITICAL GAPS (2)                                                │   │
│  │                                                                      │   │
│  │  1. S3-009 - Adjusted Covered Taxes calculation workpapers          │   │
│  │     GIR Ref: 3.10.x                                                  │   │
│  │     Action: Complete tax reconciliation for Switzerland             │   │
│  │                                                                      │   │
│  │  2. EL-001 - Election inventory listing                             │   │
│  │     GIR Ref: Various                                                 │   │
│  │     Action: Document all policy choices made                        │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  🟠 HIGH PRIORITY GAPS (8)                                           │   │
│  │                                                                      │   │
│  │  3. S3-003 - Policy choice memorandum                                │   │
│  │  4. SH-001 - Safe Harbour qualification analysis                     │   │
│  │  5. CT-004 - Manual adjustment approval process                      │   │
│  │  6. CT-007 - Review and sign-off workflow                           │   │
│  │  ... [+4 more]                                                       │   │
│  │                                                                      │   │
│  │  [Expand for details...]                                             │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
│  [ Download Full Report (PDF) ]  [ Download Action Items (Excel) ]         │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 8. Test Cases

### 8.1 Case Study 1: GlobalTech Manufacturing - Audit Checklist

**Setup Input:**
| Field | Value |
|-------|-------|
| Entity/Group Name | GlobalTech Manufacturing Ltd |
| Fiscal Year | 2024 |
| Number of Jurisdictions | 20 |
| Filing Entity | GlobalTech Manufacturing Ltd |
| GIR Filing Status | Draft - First Filing |
| Audit Date | Current Date |

**Expected Category Breakdown:**

| Category | Complete | Total | Percentage |
|----------|----------|-------|------------|
| Section 1 - General Information | 10 | 10 | 100% ✅ |
| Section 2 - Corporate Structure | 8 | 10 | 80% |
| Section 3 - GloBE Computation | 14 | 18 | 78% |
| Elections Documentation | 3 | 10 | 30% |
| Safe Harbour Documentation | 5 | 8 | 63% |
| System & Process Controls | 5 | 10 | 50% |

**Expected Overall Progress:**
| Metric | Value |
|--------|-------|
| Total Checklist Items | 66 |
| Completed Items | 45 |
| Incomplete Items | 18 |
| Not Applicable | 3 |
| Completion Percentage | 71.4% |
| Overall Status | 🔵 IN PROGRESS |

**Expected Gap Analysis - Critical Items:**

| Item ID | Description | Priority | Action Required |
|---------|-------------|----------|-----------------|
| S3-009 | Adjusted Covered Taxes workpapers | Critical | Complete tax reconciliation for CH |
| EL-001 | Election inventory listing | Critical | Document policy choices made |

**Expected Gap Analysis - High Priority Items:**

| Item ID | Description | Action Required |
|---------|-------------|-----------------|
| S3-003 | Policy choice memorandum | Draft memo for stock comp treatment |
| SH-001 | Safe Harbour qualification analysis | Complete for remaining 16 jurisdictions |
| CT-004 | Manual adjustment approval process | Document review workflow |
| CT-007 | Review and sign-off workflow | Establish approval chain |

**Expected Audit Readiness Assessment:**
```
GlobalTech Manufacturing Ltd - FY2024 GIR Audit File

Status: IN PROGRESS (71.4% complete)

Strengths:
✅ Section 1 (General Information) fully documented
✅ Core GloBE calculations completed for low-tax jurisdictions
✅ Safe Harbour analysis started for qualifying jurisdictions

Gaps to Address:
⚠️ Elections documentation incomplete (first year - limited elections)
⚠️ Process controls documentation needs formalization
⚠️ 2 critical items outstanding

Estimated Completion: 2-3 weeks of focused effort
```

### 8.2 Functional Test Cases

| Test ID | Description | Input | Expected Output |
|---------|-------------|-------|-----------------|
| TC-001 | Calculate completion percentage | 45 complete, 18 incomplete, 3 N/A | 71.4% (45/63) |
| TC-002 | Overall status - Complete | 100% completion, all critical done | Status: COMPLETE |
| TC-003 | Overall status - Substantially Complete | 92% completion | Status: SUBSTANTIALLY_COMPLETE |
| TC-004 | Overall status - In Progress | 71% completion | Status: IN_PROGRESS |
| TC-005 | Overall status - Incomplete | 40% completion | Status: INCOMPLETE |
| TC-006 | Category breakdown calculation | Section 1: 10/10 complete | Section 1: 100% |
| TC-007 | Gap analysis generation | 18 incomplete items | Gap report with 18 items sorted by priority |
| TC-008 | All N/A handling | All 66 items marked N/A | 100%, "All items marked as not applicable" |

### 8.3 Validation Test Cases

| Test ID | Input | Expected Result |
|---------|-------|-----------------|
| VT-001 | Entity name empty | Error: "Please enter the entity or group name" |
| VT-002 | Fiscal year = 2020 | Error: "Please enter a fiscal year between 2024 and 2100" |
| VT-003 | Jurisdictions = 0 | Error: "Please enter a valid number of jurisdictions (1-250)" |
| VT-004 | No sections selected | Error: "Please select at least one checklist section" |
| VT-005 | All fields valid | Checklist loads successfully |

---

## 9. Error Handling & Warnings

### 9.1 Warning Messages

| Warning Code | Condition | Message |
|--------------|-----------|---------|
| `WARN_CRITICAL_INCOMPLETE` | Critical priority items not complete | "⚠️ You have incomplete critical documentation items. These are essential for audit readiness." |
| `WARN_LOW_COMPLETION` | Completion < 50% | "📋 Your checklist is less than 50% complete. Continue documenting to improve audit readiness." |
| `WARN_SAFE_HARBOUR_GAP` | Safe Harbour section incomplete | "⚠️ Safe Harbour documentation appears incomplete. Ensure you have support for all Safe Harbour claims." |

### 9.2 Data Persistence

- Checklist progress saved to browser local storage automatically
- Auto-save every 30 seconds
- Option to export/import progress as JSON
- Clear all progress option with confirmation dialog

---

## 10. Accessibility Requirements

| Requirement | Implementation |
|-------------|----------------|
| Keyboard Navigation | Tab through all items, Space/Enter to toggle status |
| Screen Reader | ARIA labels on all elements, progress announcements |
| Color Contrast | Minimum 4.5:1 contrast ratio |
| Focus Indicators | Visible focus ring on all interactive elements |
| Text Scaling | Supports 200% zoom without horizontal scrolling |

---

## 11. Technical Notes

### 11.1 Data Model

```typescript
interface AuditChecklistSession {
  id: string;
  entityName: string;
  fiscalYear: number;
  jurisdictionCount: number;
  filingEntity: string;
  girStatus: 'DRAFT' | 'PREPARED' | 'SUBMITTED' | 'AMENDED';
  auditDate: Date;
  sections: {
    section1: boolean;
    section2: boolean;
    section3: boolean;
    elections: boolean;
    safeHarbour: boolean;
    controls: boolean;
  };
  items: ChecklistItem[];
  createdAt: Date;
  updatedAt: Date;
}

interface ChecklistItem {
  id: string;
  category: string;
  description: string;
  priority: 'CRITICAL' | 'HIGH' | 'MEDIUM' | 'LOW';
  girReference: string;
  status: 'COMPLETE' | 'INCOMPLETE' | 'NOT_APPLICABLE' | 'IN_PROGRESS';
  notes: string;
  attachments: string[];
  lastUpdated: Date;
}

interface GapAnalysisReport {
  generatedAt: Date;
  totalGaps: number;
  criticalGaps: GapItem[];
  highGaps: GapItem[];
  mediumGaps: GapItem[];
  lowGaps: GapItem[];
}
```

### 11.2 Export Formats

**PDF Report Contents:**
1. Cover page with entity details and date
2. Executive summary with overall status
3. Category breakdown with progress bars
4. Full checklist with status indicators
5. Gap analysis section
6. Action items summary

**Excel Export Structure:**
- Sheet 1: Summary Dashboard
- Sheet 2: Section 1 Items
- Sheet 3: Section 2 Items
- Sheet 4: Section 3 Items
- Sheet 5: Elections Items
- Sheet 6: Safe Harbour Items
- Sheet 7: Controls Items
- Sheet 8: Gap Analysis

---

## 12. Limitations & Scope

### 12.1 In Scope

- ✅ Comprehensive checklist (66 items across 6 categories)
- ✅ Progress tracking with visual indicators
- ✅ Gap analysis and reporting
- ✅ Export to PDF and Excel
- ✅ Local storage persistence
- ✅ Notes and status tracking per item
- ✅ Case study pre-load

### 12.2 Out of Scope

- ❌ Actual document storage or management
- ❌ Integration with document management systems
- ❌ Multi-user collaboration features
- ❌ Workflow approvals or sign-offs
- ❌ Direct GIR submission functionality
- ❌ Jurisdiction-specific checklist customization

---

## 13. Version History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2024-12-08 | — | Initial specification (as GIR-009) |
| 2.0 | 2024-12-08 | — | Renumbered to GIR-006, updated cross-references, aligned test cases with Case Study 1 |

---

## 14. Migration Notes

### 14.1 Renumbering

| Previous | New | Change |
|----------|-----|--------|
| GIR-009 | GIR-006 | Renumbered due to tool consolidation |

### 14.2 Cross-Reference Updates

| Old Reference | New Reference |
|---------------|---------------|
| GIR-006 (Data Point Reference) | Merged into GIR-004 |
| GIR-008 (Practice Form) | GIR-004 (GIR Practice Form) |

### 14.3 Workflow Integration

```
┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│   GIR-004    │     │   GIR-006    │     │   Submit     │
│   Practice   │────▶│    Audit     │────▶│    GIR to    │
│    Form      │     │   Checklist  │     │   Authority  │
└──────────────┘     └──────────────┘     └──────────────┘
```

---

## 15. Appendix: Documentation Templates

### 15.1 Policy Choice Memorandum Template (S3-003)

```markdown
# GloBE Policy Choice Memorandum
## [Entity Name] - FY [Year]

### 1. Introduction
This memorandum documents the GloBE policy choices made by [Entity Name]
for the fiscal year ending [Date].

### 2. Policy Choices Made

#### 2.1 Stock-Based Compensation (Election 1)
- Choice: [Accounting basis / Tax deduction basis]
- Rationale: [Explanation]
- Annual vs. Five-Year Election: [Selection]

#### 2.2 [Other elections...]

### 3. Impact Analysis
[Summary of impact on GloBE calculations]

### 4. Approval
Approved by: [Name, Title]
Date: [Date]
```

### 15.2 Adjusted Covered Taxes Workpaper Template (S3-009)

```markdown
# Adjusted Covered Taxes Calculation
## [Jurisdiction] - FY [Year]

| Line | Description | Amount (€) |
|------|-------------|------------|
| 1 | Current tax expense (per financial statements) | |
| 2 | Add: Deferred tax expense adjustments | |
| 3 | Less: Non-GloBE taxes | |
| 4 | Add: CFC regime taxes pushed down | |
| 5 | Less: Qualified Refundable Tax Credits | |
| 6 | Other adjustments | |
| 7 | **Adjusted Covered Taxes** | |

Prepared by: [Name]
Reviewed by: [Name]
Date: [Date]
```

---

*End of GIR-006 Audit File Checklist Specification*
