# GIR-009: Audit File Checklist

## Tool Specification Document

**Version:** 1.0
**Status:** Draft
**Last Updated:** 2024-12-08

---

## 1. Tool Metadata

| Attribute | Value |
|-----------|-------|
| Tool ID | GIR-009 |
| Tool Name | Audit File Checklist |
| Category | Compliance / Documentation |
| Complexity | Medium |
| Estimated Dev Time | 3-4 days |
| Dependencies | None (standalone tool) |
| Related Tools | GIR-006 (Data Point Reference), GIR-008 (Practice Form) |

---

## 2. Purpose & Learning Objective

### 2.1 Purpose

The Audit File Checklist provides MNE groups with a comprehensive, interactive checklist to ensure they have assembled all required documentation to support their GloBE Information Return filing. This tool helps tax professionals systematically verify that their audit file is complete, properly organized, and compliant with Pillar Two documentation requirements.

### 2.2 Learning Objectives

Upon using this tool, learners will be able to:

1. **Identify** all documentation categories required for GIR audit compliance
2. **Organize** supporting documentation according to regulatory expectations
3. **Assess** the completeness of their GIR audit file before submission
4. **Understand** the relationship between GIR data points and supporting evidence
5. **Prepare** for potential tax authority inquiries with proper documentation

### 2.3 Target Users

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

### 3.3 Checklist Configuration

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
| `completion_percentage` | Completion Rate | Decimal | Percentage (e.g., "85%") |
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

### 5.1 Section 1: General Information Documentation

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

### 5.2 Section 2: Corporate Structure Documentation

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

### 5.3 Section 3: GloBE Computation Documentation

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

### 5.4 Elections Documentation

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

### 5.5 Safe Harbour Documentation

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

### 5.6 System and Process Controls Documentation

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

### 7.1 Main Layout Wireframe

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  GIR-009: Audit File Checklist                                              │
│  Ensure your GloBE documentation is complete and audit-ready                │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  SETUP INFORMATION                                                   │   │
│  │                                                                      │   │
│  │  Entity/Group Name: [_________________________________]              │   │
│  │                                                                      │   │
│  │  Fiscal Year: [____]   Jurisdictions: [__]   Filing Status: [____▼] │   │
│  │                                                                      │   │
│  │  Filing Entity: [___________________________________]                │   │
│  │                                                                      │   │
│  │  ☑ Section 1  ☑ Section 2  ☑ Section 3                              │   │
│  │  ☑ Elections  ☑ Safe Harbour  ☑ Controls                            │   │
│  │                                                                      │   │
│  │                              [ Start Checklist ]                     │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 7.2 Checklist Progress Dashboard

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  AUDIT FILE CHECKLIST - GlobalCorp Holdings                                 │
│  FY 2024 | 12 Jurisdictions | Status: PREPARED                              │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  OVERALL PROGRESS                                                    │   │
│  │                                                                      │   │
│  │  ████████████████████████████████████░░░░░░░░░░░  78%               │   │
│  │                                                                      │   │
│  │  47 of 60 items complete   |   8 incomplete   |   5 N/A             │   │
│  │                                                                      │   │
│  │  Status: 🔵 IN PROGRESS                                              │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  CATEGORY BREAKDOWN                                                  │   │
│  │                                                                      │   │
│  │  Section 1 - General Information     ████████████████████  100%  ✓  │   │
│  │  Section 2 - Corporate Structure     ████████████████░░░░   80%     │   │
│  │  Section 3 - GloBE Computation       ██████████████░░░░░░   70%     │   │
│  │  Elections Documentation             ████████████████████  100%  ✓  │   │
│  │  Safe Harbour Documentation          ██████████░░░░░░░░░░   50%     │   │
│  │  System & Controls                   ████████████████░░░░   80%     │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
│  [ View Full Checklist ]  [ Gap Analysis ]  [ Export PDF ]  [ Export XLS ] │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 7.3 Interactive Checklist View

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  SECTION 3: GloBE COMPUTATION DOCUMENTATION                    70% Complete │
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
│  │             Notes: [Add note...]                                     │   │
│  │             ⚠️ Missing - Required for audit readiness               │   │
│  │  ─────────────────────────────────────────────────────────────────  │   │
│  │  ⬜ S3-004  Excluded dividend documentation                          │   │
│  │             Priority: High  |  GIR Ref: 3.4.x                        │   │
│  │             Notes: [Add note...]                                     │   │
│  │  ─────────────────────────────────────────────────────────────────  │   │
│  │  ➖ S3-006  Asymmetric foreign currency gain/loss analysis           │   │
│  │             Priority: Medium  |  GIR Ref: 3.6.x                      │   │
│  │             Status: N/A - No foreign currency adjustments            │   │
│  │                                                                      │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
│  Legend: ✅ Complete  ⬜ Incomplete  ➖ Not Applicable  ⏳ In Progress       │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 7.4 Individual Item Detail Panel

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  CHECKLIST ITEM DETAIL                                              [X]    │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  Item ID: S3-009                                                            │
│  Description: Adjusted Covered Taxes calculation workpapers                 │
│                                                                             │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  ITEM ATTRIBUTES                                                     │   │
│  │                                                                      │   │
│  │  Priority:       ⚠️ Critical                                         │   │
│  │  GIR Reference:  3.10.x                                              │   │
│  │  Category:       Section 3 - GloBE Computation                       │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  STATUS                                                              │   │
│  │                                                                      │   │
│  │  ( ) Complete     (•) Incomplete     ( ) Not Applicable              │   │
│  │                   ( ) In Progress                                    │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  DOCUMENTATION GUIDANCE                                              │   │
│  │                                                                      │   │
│  │  This workpaper should include:                                      │   │
│  │  • Current tax expense by entity/jurisdiction                        │   │
│  │  • Mapping from financial statement tax to GloBE covered taxes       │   │
│  │  • Deferred tax adjustments (add-backs and reductions)               │   │
│  │  • Qualified Refundable Tax Credit identification                    │   │
│  │  • CFC tax regime adjustments                                        │   │
│  │  • Push-down of parent entity taxes                                  │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  NOTES                                                               │   │
│  │                                                                      │   │
│  │  [                                                                 ] │   │
│  │  [  Awaiting tax team to finalize Q4 provisions                    ] │   │
│  │  [                                                                 ] │   │
│  │                                                                      │   │
│  │  Attached Files: (none)                                              │   │
│  │                              [ Upload File ]                         │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
│                              [ Save Changes ]                               │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 7.5 Gap Analysis Report View

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  GAP ANALYSIS REPORT                                                        │
│  GlobalCorp Holdings | FY 2024 | Generated: 2024-12-08                      │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  SUMMARY                                                                    │
│  ═══════════════════════════════════════════════════════════════════════   │
│  Total Gaps Identified: 13                                                  │
│  Critical Priority: 2  |  High Priority: 6  |  Medium Priority: 5          │
│                                                                             │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  🔴 CRITICAL GAPS (2)                                                │   │
│  │                                                                      │   │
│  │  1. S3-009 - Adjusted Covered Taxes calculation workpapers          │   │
│  │     GIR Ref: 3.10.x                                                  │   │
│  │     Action: Prepare tax-to-GloBE reconciliation for all             │   │
│  │             jurisdictions with supporting schedules                  │   │
│  │                                                                      │   │
│  │  2. SH-001 - Transitional CbCR Safe Harbour qualification           │   │
│  │     GIR Ref: SH Section                                              │   │
│  │     Action: Complete Safe Harbour analysis for each jurisdiction    │   │
│  │             or document decision not to apply Safe Harbour          │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  🟠 HIGH PRIORITY GAPS (6)                                           │   │
│  │                                                                      │   │
│  │  3. S3-003 - Policy choice memorandum                                │   │
│  │  4. S3-004 - Excluded dividend documentation                         │   │
│  │  5. S3-011 - Deferred tax adjustment schedules                       │   │
│  │  6. EL-002 - Stock-based compensation election documentation         │   │
│  │  7. SH-004 - Simplified ETR Test calculation                         │   │
│  │  8. CT-004 - Manual adjustment approval process                      │   │
│  │                                                                      │   │
│  │  [Expand for details...]                                             │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
│  [ Download Full Report (PDF) ]  [ Download Action Items (Excel) ]         │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 7.6 Mobile Responsive View

```
┌─────────────────────────────┐
│  Audit Checklist      [≡]  │
│  GlobalCorp | FY 2024      │
├─────────────────────────────┤
│                             │
│  ████████████████░░░  78%  │
│  47/60 complete             │
│                             │
│  ┌───────────────────────┐ │
│  │ Section 1        100% │ │
│  │ Section 2         80% │ │
│  │ Section 3         70% │ │
│  │ Elections        100% │ │
│  │ Safe Harbour      50% │ │
│  │ Controls          80% │ │
│  └───────────────────────┘ │
│                             │
│  ⚠️ 2 Critical Gaps         │
│                             │
│  [ View Checklist ]         │
│  [ Gap Analysis ]           │
│  [ Export ]                 │
│                             │
└─────────────────────────────┘
```

---

## 8. User Flow

### 8.1 Primary Flow: Complete Audit Checklist

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                                                                             │
│  START                                                                      │
│    │                                                                        │
│    ▼                                                                        │
│  ┌──────────────────────┐                                                  │
│  │ 1. Enter Setup Info  │                                                  │
│  │    - Entity name     │                                                  │
│  │    - Fiscal year     │                                                  │
│  │    - Jurisdictions   │                                                  │
│  └──────────┬───────────┘                                                  │
│             │                                                               │
│             ▼                                                               │
│  ┌──────────────────────┐                                                  │
│  │ 2. Select Sections   │                                                  │
│  │    to Include        │                                                  │
│  └──────────┬───────────┘                                                  │
│             │                                                               │
│             ▼                                                               │
│  ┌──────────────────────┐                                                  │
│  │ 3. View Progress     │◄──────────────────────────────────┐              │
│  │    Dashboard         │                                    │              │
│  └──────────┬───────────┘                                    │              │
│             │                                                 │              │
│             ▼                                                 │              │
│  ┌──────────────────────┐                                    │              │
│  │ 4. Work Through      │                                    │              │
│  │    Checklist Items   │────────────────────────────────────┘              │
│  │    - Mark complete   │     (Update progress)                             │
│  │    - Add notes       │                                                   │
│  │    - Mark N/A        │                                                   │
│  └──────────┬───────────┘                                                  │
│             │                                                               │
│             ▼                                                               │
│        ┌────────────┐                                                      │
│        │ All items  │                                                      │
│        │ addressed? │                                                      │
│        └─────┬──────┘                                                      │
│          Yes │                                                              │
│              ▼                                                              │
│  ┌──────────────────────┐                                                  │
│  │ 5. Review Gap        │                                                  │
│  │    Analysis Report   │                                                  │
│  └──────────┬───────────┘                                                  │
│             │                                                               │
│             ▼                                                               │
│  ┌──────────────────────┐                                                  │
│  │ 6. Export Reports    │                                                  │
│  │    - PDF Checklist   │                                                  │
│  │    - Excel Tracker   │                                                  │
│  │    - Gap Analysis    │                                                  │
│  └──────────┬───────────┘                                                  │
│             │                                                               │
│             ▼                                                               │
│           END                                                               │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 8.2 Alternative Flow: Quick Gap Assessment

1. Enter minimal setup information
2. Select all checklist sections
3. Navigate directly to Gap Analysis
4. Review critical and high priority gaps
5. Export action item list

### 8.3 Workflow Integration

```
┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│   GIR-008    │     │   GIR-009    │     │   Submit     │
│   Practice   │────▶│    Audit     │────▶│    GIR to    │
│    Form      │     │   Checklist  │     │   Authority  │
└──────────────┘     └──────────────┘     └──────────────┘
      │                     │
      │                     │
      ▼                     ▼
┌──────────────┐     ┌──────────────┐
│   GIR-006    │     │   Archived   │
│  Data Point  │     │    Audit     │
│  Reference   │     │    File      │
└──────────────┘     └──────────────┘
```

---

## 9. Edge Cases & Error Handling

### 9.1 Input Validation Errors

| Error Code | Condition | User Message |
|------------|-----------|--------------|
| `ERR_ENTITY_REQUIRED` | Entity name is empty | "Please enter the entity or group name" |
| `ERR_FISCAL_YEAR_INVALID` | Fiscal year outside valid range | "Please enter a fiscal year between 2024 and 2100" |
| `ERR_JURISDICTION_INVALID` | Jurisdiction count < 1 or > 250 | "Please enter a valid number of jurisdictions (1-250)" |
| `ERR_NO_SECTIONS` | No checklist sections selected | "Please select at least one checklist section to include" |

### 9.2 Edge Cases

| Scenario | Handling |
|----------|----------|
| All items marked N/A | Show 100% completion with message "All items marked as not applicable" |
| Large number of gaps (>20) | Paginate gap analysis, show critical items first |
| Browser session timeout | Auto-save progress every 30 seconds, restore on reload |
| Conflicting status updates | Last update wins, show timestamp of last change |
| Export with incomplete data | Include incomplete status in export, highlight gaps |

### 9.3 Warning Messages

| Warning Code | Condition | Message |
|--------------|-----------|---------|
| `WARN_CRITICAL_INCOMPLETE` | Critical priority items not complete | "⚠️ You have incomplete critical documentation items. These are essential for audit readiness." |
| `WARN_LOW_COMPLETION` | Completion < 50% | "📋 Your checklist is less than 50% complete. Continue documenting to improve audit readiness." |
| `WARN_SAFE_HARBOUR_GAP` | Safe Harbour section incomplete when elections imply it's used | "⚠️ Safe Harbour documentation appears incomplete. Ensure you have support for all Safe Harbour claims." |

### 9.4 Data Persistence

- Checklist progress should be saved to browser local storage
- Option to export/import progress as JSON
- Clear all progress option with confirmation dialog

---

## 10. Test Cases

### 10.1 Functional Test Cases

| Test ID | Description | Input | Expected Output |
|---------|-------------|-------|-----------------|
| TC-001 | Calculate completion percentage | 47 complete, 8 incomplete, 5 N/A | 85.5% (47/55) |
| TC-002 | Overall status - Complete | 100% completion, all critical done | Status: COMPLETE |
| TC-003 | Overall status - Substantially Complete | 92% completion | Status: SUBSTANTIALLY_COMPLETE |
| TC-004 | Overall status - In Progress | 65% completion | Status: IN_PROGRESS |
| TC-005 | Overall status - Incomplete | 40% completion | Status: INCOMPLETE |
| TC-006 | Category breakdown calculation | Section 1: 8/10 complete | Section 1: 80% |
| TC-007 | Gap analysis generation | 5 incomplete items | Gap report with 5 items sorted by priority |
| TC-008 | All N/A handling | All 60 items marked N/A | 100%, "All items marked as not applicable" |

### 10.2 Case Study Test Data

#### GlobalCorp Holdings (Case Study 1)

**Setup:**
- Entity Name: GlobalCorp Holdings plc
- Fiscal Year: 2024
- Jurisdictions: 5 (UK, DE, IE, NL, SG)
- Filing Entity: GlobalCorp Holdings plc (UK)
- Status: PREPARED

**Expected Checklist Progress (Sample):**

| Category | Items | Complete | N/A | Percentage |
|----------|-------|----------|-----|------------|
| Section 1 - General | 10 | 10 | 0 | 100% |
| Section 2 - Structure | 10 | 8 | 0 | 80% |
| Section 3 - Computation | 18 | 14 | 2 | 87.5% |
| Elections | 10 | 6 | 2 | 75% |
| Safe Harbour | 8 | 4 | 0 | 50% |
| Controls | 10 | 8 | 0 | 80% |
| **TOTAL** | **66** | **50** | **4** | **80.6%** |

**Gap Analysis (Critical Items):**
1. S3-009 - Adjusted Covered Taxes workpapers (Critical)
2. SH-001 - Safe Harbour qualification analysis (Critical)

#### TechStart Inc. (Case Study 2)

**Setup:**
- Entity Name: TechStart Inc.
- Fiscal Year: 2024
- Jurisdictions: 3 (US, IE, UK)
- Filing Entity: TechStart Inc. (US)
- Status: DRAFT

**Expected Overall:** 65% completion, Status: IN_PROGRESS

### 10.3 UI/UX Test Cases

| Test ID | Description | Steps | Expected Result |
|---------|-------------|-------|-----------------|
| UI-001 | Checklist item toggle | Click checkbox for item S1-001 | Status toggles between Complete/Incomplete |
| UI-002 | N/A marking | Select "Not Applicable" for item | Item excluded from completion calculation |
| UI-003 | Notes field | Enter notes for item S3-003 | Notes saved and displayed |
| UI-004 | Filter by status | Select "Incomplete" filter | Only incomplete items displayed |
| UI-005 | Filter by priority | Select "Critical" priority | Only critical items displayed |
| UI-006 | Progress bar update | Mark 5 items complete | Progress bar increases, percentage updates |
| UI-007 | Export PDF | Click "Export PDF" | PDF downloads with current checklist state |
| UI-008 | Mobile responsiveness | View on 375px width | Checklist displays in single-column layout |

---

## 11. Accessibility Requirements

### 11.1 WCAG 2.1 AA Compliance

| Requirement | Implementation |
|-------------|----------------|
| Keyboard Navigation | All checklist items accessible via Tab key, Space/Enter to toggle |
| Screen Reader | ARIA labels for all interactive elements, progress announcements |
| Color Contrast | Minimum 4.5:1 contrast ratio for all text |
| Focus Indicators | Visible focus ring on all interactive elements |
| Text Scaling | Supports 200% zoom without horizontal scrolling |

### 11.2 ARIA Labels

```html
<div role="progressbar" aria-valuenow="78" aria-valuemin="0" aria-valuemax="100"
     aria-label="Audit checklist completion: 78 percent">

<input type="checkbox" id="s1-001" aria-describedby="s1-001-desc"
       aria-label="UPE identification documents: Complete">

<button aria-label="Export checklist as PDF document">Export PDF</button>
```

### 11.3 Status Announcements

- When an item is marked complete: "Item [ID] marked as complete. Overall progress: [X]%"
- When overall status changes: "Audit checklist status changed to [STATUS]"

---

## 12. Technical Notes

### 12.1 Data Model

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

interface GapItem {
  itemId: string;
  description: string;
  priority: string;
  girReference: string;
  recommendedAction: string;
}
```

### 12.2 Local Storage Schema

```json
{
  "audit_checklist_sessions": [
    {
      "id": "session_001",
      "entityName": "GlobalCorp Holdings plc",
      "fiscalYear": 2024,
      "items": [
        {
          "id": "S1-001",
          "status": "COMPLETE",
          "notes": "Uploaded incorporation certificate"
        }
      ],
      "updatedAt": "2024-12-08T10:30:00Z"
    }
  ]
}
```

### 12.3 Export Formats

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

## 13. Limitations & Scope

### 13.1 In Scope

- ✅ Comprehensive checklist covering all GIR documentation requirements
- ✅ Progress tracking with visual indicators
- ✅ Gap analysis and reporting
- ✅ Export to PDF and Excel
- ✅ Local storage persistence
- ✅ Notes and status tracking per item

### 13.2 Out of Scope

- ❌ Actual document storage or management
- ❌ Integration with document management systems
- ❌ Multi-user collaboration features
- ❌ Workflow approvals or sign-offs
- ❌ Direct GIR submission functionality
- ❌ Jurisdiction-specific checklist customization

### 13.3 Educational Limitations

This tool is designed for educational purposes to help learners understand GIR documentation requirements. Users should:

1. Consult with qualified tax advisors for actual filing requirements
2. Verify documentation requirements with relevant tax authorities
3. Not rely solely on this tool for audit preparation

---

## 14. Version History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2024-12-08 | — | Initial specification |

---

## 15. Appendix: Case Study Alignment

### 15.1 Case Study 1: GlobalCorp Holdings

**Applicable Checklist Items:**

| Item ID | Relevance | Case Study Data Available |
|---------|-----------|---------------------------|
| S1-001 | UPE identification | ✅ GlobalCorp Holdings plc (UK) |
| S1-005 | Consolidated revenue | ✅ €850M (meets threshold) |
| S1-007 | Constituent Entities | ✅ 5 entities across 5 jurisdictions |
| S3-001 | Financial income by jurisdiction | ✅ Full P&L data provided |
| S3-014 | ETR calculations | ✅ All jurisdiction ETRs |
| S3-015 | SBIE calculations | ✅ Payroll and asset data |
| S3-016 | Top-up Tax | ✅ Expected outcomes provided |
| SH-001 | Safe Harbour analysis | ✅ CbCR data for analysis |
| EL-001 | Election inventory | ⚠️ Limited - no elections specified |

### 15.2 Case Study 2-5 Alignment

| Case Study | Entity | Key Focus Areas |
|------------|--------|-----------------|
| CS-2 | TechStart Inc. | Startup company, US parent, R&D intensive |
| CS-3 | Manufacturing Co. | Asset-heavy, multiple production facilities |
| CS-4 | Financial Services | Investment entities, complex structures |
| CS-5 | Retail Group | High employee count, multiple retail locations |

### 15.3 Checklist Item to GIR Data Point Mapping

| Checklist Item | Related GIR Data Points (GIR-006) |
|----------------|-----------------------------------|
| S1-001 | DP-001, DP-002, DP-003, DP-004 |
| S1-007 | DP-010 through DP-050 |
| S3-001 | DP-301, DP-302 |
| S3-009 | DP-310 through DP-330 |
| S3-014 | DP-340 |
| S3-015 | DP-350, DP-351, DP-352 |

---

## 16. Appendix: Documentation Guidance Templates

### 16.1 Policy Choice Memorandum Template (S3-003)

```markdown
# GloBE Policy Choice Memorandum
## [Entity Name] - FY [Year]

### 1. Introduction
This memorandum documents the GloBE policy choices made by [Entity Name] for the fiscal year ending [Date].

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

### 16.2 Adjusted Covered Taxes Workpaper Template (S3-009)

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

*End of GIR-009 Specification*
