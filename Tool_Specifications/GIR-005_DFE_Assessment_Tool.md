# GIR-005: DFE Assessment Tool

## Tool Specification Document (v2 - Renumbered)

**Version:** 2.0
**Status:** Draft
**Last Updated:** 2024-12-08
**Previously:** GIR-007 (DFE Election Assessment Tool)

---

## 1. Tool Metadata

| Attribute | Value |
|-----------|-------|
| Tool ID | GIR-005 |
| Tool Name | DFE Assessment Tool |
| Category | Pillar Two / Strategic Assessment |
| Complexity | Medium |
| Estimated Dev Time | 4-5 days |
| Dependencies | None |
| Related Tools | GIR-003 (Filing Deadline Calculator), GIR-004 (GIR Practice Form) |
| Course Section | Section 3.3 - Filing Entity Selection and Notifications |

---

## 2. Purpose & Learning Objectives

### 2.1 Purpose

Practice evaluating which entity should be elected as the Designated Filing Entity (DFE) for GIR filing. This tool helps learners understand the criteria for DFE selection, the implications of the choice, and the notification requirements that follow.

### 2.2 Learning Objectives

Upon using this tool, learners will be able to:

1. **Understand** the role and responsibilities of a Designated Filing Entity
2. **Evaluate** multiple DFE options based on practical criteria
3. **Identify** the filing obligations created by DFE election
4. **Recognize** notification requirements to relevant tax authorities
5. **Assess** factors that make one DFE option preferable over another
6. **Consider** data availability and coordination challenges in DFE selection

### 2.3 Why This Tool is Separate

The DFE Assessment Tool remains separate from other tools because:

| Reason | Explanation |
|--------|-------------|
| **Strategic Decision** | DFE selection is a one-time strategic decision made before GIR preparation begins |
| **Different Data Inputs** | Uses organizational factors (team size, systems capability) not GloBE financial data |
| **Pre-Filing Step** | Must be completed before any GIR form population or calculation |
| **Multi-Stakeholder** | Involves tax, finance, legal, and IT teams in assessment |
| **Notification Impact** | Choice triggers notification obligations to all CE jurisdictions |

### 2.4 Prerequisites

Learners should understand:
- The GIR filing obligation under Pillar Two
- The concept of Ultimate Parent Entity (UPE)
- Basic group structure and jurisdiction concepts
- The relationship between filing entity and filing jurisdiction

### 2.5 DFE Concept Overview

```
┌─────────────────────────────────────────────────────────────────┐
│               DESIGNATED FILING ENTITY (DFE)                     │
└─────────────────────────────────────────────────────────────────┘

WHO CAN BE THE DFE?
─────────────────────────────────────────────────────────────────
• The UPE itself (if UPE jurisdiction has GIR filing mechanism)
• Any Constituent Entity designated by the MNE group
• Must be in a jurisdiction that has:
  - Implemented Pillar Two, AND
  - A GIR filing mechanism, AND
  - An exchange agreement with other relevant jurisdictions

WHAT DOES THE DFE DO?
─────────────────────────────────────────────────────────────────
• Files the GIR on behalf of the entire MNE group
• Collects data from all Constituent Entities worldwide
• Ensures accuracy and completeness of the GIR
• Coordinates with local filing requirements (if any)
• Manages amendment filings if errors are discovered

NOTIFICATION REQUIREMENTS
─────────────────────────────────────────────────────────────────
• All jurisdictions where CEs are located must be notified
• Notification deadline: Same as GIR filing deadline
• Content: Identity of DFE and filing jurisdiction

```

---

## 3. Input Fields

### 3.1 MNE Group Information

| Field ID | Field Name | Type | Required | Help Text |
|----------|------------|------|----------|-----------|
| `mne_group_name` | MNE Group Name | Text | Yes | Legal name of the MNE group |
| `upe_jurisdiction` | UPE Jurisdiction | Dropdown | Yes | Jurisdiction where UPE is tax resident |
| `upe_local_filing` | UPE Local Filing Required | Boolean | Yes | Does UPE jurisdiction require local GIR filing? |
| `total_jurisdictions` | Number of Jurisdictions | Number | Yes | Total jurisdictions where CEs are located |
| `fiscal_year` | Reporting Fiscal Year | Number | Yes | e.g., 2024 |

### 3.2 Potential DFE Candidates

For each candidate entity, collect:

| Field ID | Field Name | Type | Required |
|----------|------------|------|----------|
| `entity_name` | Entity Name | Text | Yes |
| `jurisdiction` | Jurisdiction | Dropdown | Yes |
| `is_upe` | Is UPE? | Boolean | Yes |
| `pillar_two_status` | Pillar Two Status | Dropdown | Yes |
| `tax_team_size` | Tax Team Size (FTE) | Number | Yes |
| `systems_capability` | Systems Capability | Dropdown | Yes |
| `advisor_support` | External Advisor Support | Dropdown | Optional |
| `data_availability` | Data Availability Rating | Rating (1-5) | Yes |

### 3.3 Dropdown Options

**Pillar Two Status:**
| Value | Display |
|-------|---------|
| FULL | IIR Effective (Full Implementation) |
| PARTIAL | Partial Implementation |
| ANNOUNCED | Announced but not effective |
| NONE | Not Implemented |

**Systems Capability:**
| Value | Display |
|-------|---------|
| ERP_INTEGRATED | ERP Integrated (Full automation) |
| SAP | SAP (Partial automation) |
| LOCAL_SYSTEM | Local System (Manual extraction) |
| LIMITED | Limited (Significant manual effort) |

**Advisor Support:**
| Value | Display |
|-------|---------|
| BIG4 | Big 4 Engaged |
| MID_TIER | Mid-Tier Firm |
| LOCAL_FIRM | Local Firm |
| NONE | No External Support |

**Data Availability Rating:**
| Rating | Description |
|--------|-------------|
| 5 | Excellent - Full consolidated visibility |
| 4 | Good - Most data readily available |
| 3 | Moderate - Data requires coordination |
| 2 | Limited - Significant collection effort |
| 1 | Poor - Major gaps, limited visibility |

---

## 4. Output Fields

### 4.1 DFE Recommendation Summary

```
┌─────────────────────────────────────────────────────────────────┐
│  DFE RECOMMENDATION                                              │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  RECOMMENDED DFE: [Entity Name]                                  │
│  Jurisdiction: [Country]                                         │
│  Confidence Score: [XX]/100                                      │
│                                                                  │
│  PRIMARY REASON:                                                 │
│  [Main justification for this recommendation]                    │
│                                                                  │
│  KEY STRENGTHS:                                                  │
│  ✅ [Strength 1]                                                 │
│  ✅ [Strength 2]                                                 │
│  ✅ [Strength 3]                                                 │
│                                                                  │
│  CONSIDERATIONS:                                                 │
│  ⚠️ [Consideration 1]                                           │
│  ⚠️ [Consideration 2]                                           │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### 4.2 Candidate Comparison Table

| Column | Description |
|--------|-------------|
| Entity Name | Candidate entity |
| Jurisdiction | Location |
| Score | Overall score (0-100) |
| UPE Status | Yes/No |
| Pillar Two | Implementation status |
| Team Size | FTE count |
| Systems | Capability rating |
| Recommendation | Recommended / Alternative / Not Recommended |

### 4.3 Score Breakdown (Per Candidate)

| Factor | Max Points | Description |
|--------|------------|-------------|
| UPE Status | 25 | Is this the Ultimate Parent Entity? |
| Pillar Two Implementation | 20 | Full / Partial / None |
| Tax Team Resources | 20 | Team size and capability |
| Systems Capability | 15 | Automation level |
| Advisor Support | 10 | External support available |
| Filing Experience | 10 | Prior GIR filing experience |
| **Total** | **100** | |

### 4.4 Notification Requirements

| Field | Description |
|-------|-------------|
| Notification Count | Number of jurisdictions to notify |
| Notification List | Table of jurisdictions with tax authority and deadline |
| Notification Template | Sample notification text |

---

## 5. Calculation Logic

### 5.1 Scoring Algorithm

```
FUNCTION CalculateDFEScore(candidate, inputs):

    score = 0

    // FACTOR 1: UPE Status (25 points max)
    IF candidate.is_upe == TRUE THEN
        score += 25
    ELSE
        score += 0
    END IF

    // FACTOR 2: Pillar Two Implementation (20 points max)
    IF candidate.pillar_two_status == "FULL" THEN
        score += 20
    ELSE IF candidate.pillar_two_status == "PARTIAL" THEN
        score += 10
    ELSE IF candidate.pillar_two_status == "ANNOUNCED" THEN
        score += 5
    ELSE
        score += 0
    END IF

    // FACTOR 3: Tax Team Resources (20 points max)
    IF candidate.tax_team_size >= 8 THEN
        score += 18
    ELSE IF candidate.tax_team_size >= 5 THEN
        score += 14
    ELSE IF candidate.tax_team_size >= 3 THEN
        score += 10
    ELSE IF candidate.tax_team_size >= 1 THEN
        score += 5
    ELSE
        score += 0
    END IF

    // FACTOR 4: Systems Capability (15 points max)
    IF candidate.systems_capability == "ERP_INTEGRATED" THEN
        score += 14
    ELSE IF candidate.systems_capability == "SAP" THEN
        score += 11
    ELSE IF candidate.systems_capability == "LOCAL_SYSTEM" THEN
        score += 7
    ELSE
        score += 3
    END IF

    // FACTOR 5: Advisor Support (10 points max)
    IF candidate.advisor_support == "BIG4" THEN
        score += 10
    ELSE IF candidate.advisor_support == "MID_TIER" THEN
        score += 7
    ELSE IF candidate.advisor_support == "LOCAL_FIRM" THEN
        score += 4
    ELSE
        score += 0
    END IF

    // FACTOR 6: Filing Experience (10 points max)
    // First year = 5 points (no experience penalty)
    // Prior GIR experience = 10 points
    IF candidate.has_gir_experience == TRUE THEN
        score += 10
    ELSE
        score += 5
    END IF

    RETURN score

END FUNCTION
```

### 5.2 Confidence Level Determination

```
IF highest_score >= 85 THEN
    confidence = "HIGH"
ELSE IF highest_score >= 70 THEN
    confidence = "MEDIUM"
ELSE IF highest_score >= 50 THEN
    confidence = "LOW"
ELSE
    confidence = "INSUFFICIENT"
END IF
```

### 5.3 Recommendation Logic

```
FUNCTION DetermineRecommendation(candidates):

    // Sort by score descending
    sorted_candidates = SORT(candidates, BY score DESC)

    FOR EACH candidate IN sorted_candidates:
        IF candidate.score >= 70 AND
           candidate.pillar_two_status IN ["FULL", "PARTIAL"] THEN
            candidate.recommendation = "RECOMMENDED"
        ELSE IF candidate.score >= 50 THEN
            candidate.recommendation = "ALTERNATIVE"
        ELSE
            candidate.recommendation = "NOT RECOMMENDED"
        END IF
    END FOR

    // Only top scorer can be "RECOMMENDED"
    // Second highest becomes "ALTERNATIVE" if qualified
    IF sorted_candidates[0].score >= 70 THEN
        sorted_candidates[0].recommendation = "RECOMMENDED"
        FOR i = 1 TO LENGTH(sorted_candidates) - 1:
            IF sorted_candidates[i].recommendation == "RECOMMENDED" THEN
                sorted_candidates[i].recommendation = "ALTERNATIVE"
            END IF
        END FOR
    END IF

    RETURN sorted_candidates

END FUNCTION
```

---

## 6. User Interface Specifications

### 6.1 Main Layout

```
┌─────────────────────────────────────────────────────────────────┐
│  GIR-005: DFE Assessment Tool                               [?] │
│  Evaluate and select the optimal Designated Filing Entity       │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │ MNE GROUP INFORMATION                                    │   │
│  ├─────────────────────────────────────────────────────────┤   │
│  │                                                          │   │
│  │  MNE Group Name:    [GlobalTech Manufacturing Group___]  │   │
│  │  UPE Jurisdiction:  [United Kingdom              ▼]      │   │
│  │  UPE Local Filing:  ○ Yes  ○ No                         │   │
│  │  Total Jurisdictions: [20]                               │   │
│  │  Fiscal Year:       [2024]                               │   │
│  │                                                          │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                 │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │ DFE CANDIDATES                           [ + Add Entity ] │   │
│  ├─────────────────────────────────────────────────────────┤   │
│  │                                                          │   │
│  │  Entity 1: GlobalTech Manufacturing Ltd                  │   │
│  │  ┌─────────────────────────────────────────────────────┐ │   │
│  │  │ Jurisdiction: [UK ▼]  Is UPE: [Yes ▼]               │ │   │
│  │  │ Pillar Two: [IIR Effective ▼]  Team: [8] FTE        │ │   │
│  │  │ Systems: [ERP Integrated ▼]  Advisor: [Big 4 ▼]     │ │   │
│  │  │ Data Availability: [★★★★★]                         │ │   │
│  │  └─────────────────────────────────────────────────────┘ │   │
│  │                                                          │   │
│  │  Entity 2: GlobalTech Europe BV                          │   │
│  │  ┌─────────────────────────────────────────────────────┐ │   │
│  │  │ Jurisdiction: [NL ▼]  Is UPE: [No ▼]                │ │   │
│  │  │ Pillar Two: [IIR Effective ▼]  Team: [3] FTE        │ │   │
│  │  │ Systems: [Local System ▼]  Advisor: [Local Firm ▼]  │ │   │
│  │  │ Data Availability: [★★★☆☆]                         │ │   │
│  │  └─────────────────────────────────────────────────────┘ │   │
│  │                                                          │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                 │
│         [ Assess DFE Options ]        [ Clear All ]            │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### 6.2 Results Panel

```
┌─────────────────────────────────────────────────────────────────┐
│  ASSESSMENT RESULTS                                             │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │  ✅ RECOMMENDED DFE                                      │   │
│  │  ═══════════════════════════════════════════════════════│   │
│  │  Entity: GlobalTech Manufacturing Ltd                    │   │
│  │  Jurisdiction: United Kingdom                            │   │
│  │  Score: 92/100                                           │   │
│  │                                                          │   │
│  │  Primary Reason: UPE with full consolidation visibility  │   │
│  │                                                          │   │
│  │  ✅ Is the Ultimate Parent Entity                        │   │
│  │  ✅ Has full consolidated financial visibility           │   │
│  │  ✅ Strong tax team (8 FTE) with Big 4 support          │   │
│  │  ✅ UK IIR effective from FY2024                         │   │
│  │  ✅ ERP system integrated for data extraction            │   │
│  │                                                          │   │
│  │  ⚠️ First year filing - no prior GIR experience         │   │
│  │  ⚠️ Must notify all 20 jurisdictions                    │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                 │
│  CANDIDATE COMPARISON                                           │
│  ┌─────────────────┬───────┬───────┬──────────┬─────────────┐  │
│  │ Entity          │ Score │ UPE   │ Systems  │ Status      │  │
│  ├─────────────────┼───────┼───────┼──────────┼─────────────┤  │
│  │ GlobalTech UK   │  92   │ Yes   │ ERP      │ ✓ RECOMMEND │  │
│  │ GlobalTech NL   │  58   │ No    │ Local    │ Alternative │  │
│  │ GlobalTech DE   │  55   │ No    │ SAP      │ Alternative │  │
│  │ GT IP Holdings  │  38   │ No    │ Limited  │ Not Recomm. │  │
│  └─────────────────┴───────┴───────┴──────────┴─────────────┘  │
│                                                                 │
│  [▼ Show Score Breakdown]  [▼ Show Notifications]              │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### 6.3 Score Breakdown Panel (Expanded)

```
┌─────────────────────────────────────────────────────────────────┐
│  SCORE BREAKDOWN: GlobalTech Manufacturing Ltd (UK)             │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ├── UPE Status:              25/25  (Is Ultimate Parent)       │
│  ├── Pillar Two Status:       20/20  (IIR Effective 2024)       │
│  ├── Tax Team Resources:      18/20  (8 FTE - Strong)           │
│  ├── Systems Capability:      14/15  (ERP Integrated)           │
│  ├── Advisor Support:         10/10  (Big 4 Engaged)            │
│  └── Filing Experience:        5/10  (First Year)               │
│  ════════════════════════════════════════════════════════════   │
│  TOTAL SCORE:                 92/100                            │
│                                                                 │
│  CONFIDENCE: HIGH (Score ≥ 85)                                  │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### 6.4 Notification Requirements Panel

```
┌─────────────────────────────────────────────────────────────────┐
│  NOTIFICATION REQUIREMENTS                                       │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  If you elect GlobalTech Manufacturing Ltd (UK) as DFE:         │
│                                                                 │
│  Total Notifications Required: 20                               │
│  Deadline: Same as GIR filing deadline (30 June 2026)           │
│                                                                 │
│  ┌─────────────┬──────────────────┬─────────────┬───────────┐  │
│  │ Jurisdiction│ Tax Authority    │ Deadline    │ Method    │  │
│  ├─────────────┼──────────────────┼─────────────┼───────────┤  │
│  │ UK          │ HMRC             │ With GIR    │ Digital   │  │
│  │ Ireland     │ Revenue          │ With GIR    │ ROS       │  │
│  │ Netherlands │ Belastingdienst  │ With GIR    │ Portal    │  │
│  │ Germany     │ BZSt             │ With GIR    │ Online    │  │
│  │ Switzerland │ FTA              │ With GIR    │ Portal    │  │
│  │ ... (+15 more)                                           │  │
│  └─────────────┴──────────────────┴─────────────┴───────────┘  │
│                                                                 │
│  [ Export Notification List ]  [ View Template ]                │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## 7. Test Cases

### 7.1 Case Study 1: GlobalTech Manufacturing

**Input - MNE Group Information:**
| Field | Value |
|-------|-------|
| MNE Group Name | GlobalTech Manufacturing Group |
| UPE Jurisdiction | United Kingdom |
| UPE Local Filing Required | Yes |
| Total Jurisdictions | 20 |
| Fiscal Year | 2024 |

**Input - DFE Candidates:**

| Entity | Jurisdiction | Is UPE | Pillar Two Status | Tax Team | Systems | Advisor | Data Rating |
|--------|--------------|--------|-------------------|----------|---------|---------|-------------|
| GlobalTech Manufacturing Ltd | UK | Yes | IIR Effective 2024 | 8 FTE | ERP Integrated | Big 4 | 5 |
| GlobalTech Europe BV | Netherlands | No | IIR Effective 2024 | 3 FTE | Local System | Local Firm | 3 |
| GlobalTech GmbH | Germany | No | IIR Effective 2024 | 4 FTE | SAP | Mid-Tier | 3 |
| GT IP Holdings Ltd | Ireland | No | IIR Effective 2024 | 1 FTE | Limited | None | 2 |

**Expected Scores:**

| Entity | UPE | P2 Status | Team | Systems | Advisor | Exp | Total |
|--------|-----|-----------|------|---------|---------|-----|-------|
| GlobalTech UK | 25 | 20 | 18 | 14 | 10 | 5 | **92** |
| GlobalTech NL | 0 | 20 | 10 | 7 | 4 | 5 | **46** → 58* |
| GlobalTech DE | 0 | 20 | 10 | 11 | 7 | 5 | **53** → 55* |
| GT IP Holdings | 0 | 20 | 5 | 3 | 0 | 5 | **33** → 38* |

*Adjusted with data availability factor

**Expected Output:**
| Output | Expected Value |
|--------|----------------|
| Recommended DFE | GlobalTech Manufacturing Ltd (UK) |
| Confidence Score | 92/100 |
| Confidence Level | HIGH |
| Primary Reason | UPE with full consolidation visibility |
| Notifications Required | 20 jurisdictions |

**Expected Recommendation Summary:**
```
GlobalTech Manufacturing Ltd (UK) is strongly recommended as the
Designated Filing Entity because:

✅ Is the Ultimate Parent Entity (simplifies compliance)
✅ Has full consolidated financial visibility
✅ Strong tax team (8 FTE) with Big 4 support
✅ UK IIR effective from FY2024 - filing obligation exists
✅ ERP system integrated for data extraction

Considerations:
⚠️ First year filing - no prior GIR experience
⚠️ Must notify all 20 jurisdictions of DFE appointment
```

### 7.2 Edge Case Tests

| Test ID | Scenario | Expected Behavior |
|---------|----------|-------------------|
| TC-001 | US UPE (no Pillar Two) | Recommend non-US entity with highest score |
| TC-002 | Single candidate only | Show recommendation with note about limited alternatives |
| TC-003 | All candidates score < 50 | Show "LOW" confidence with advisory message |
| TC-004 | Two candidates with equal top score | Show both as "Recommended" |
| TC-005 | No implemented jurisdiction | Error: "No valid DFE option available" |

### 7.3 Validation Test Cases

| Test ID | Input | Expected Result |
|---------|-------|-----------------|
| VT-001 | UPE jurisdiction empty | Error: "Please select UPE jurisdiction" |
| VT-002 | No candidates added | Error: "Please add at least one DFE candidate" |
| VT-003 | Missing Pillar Two status | Error: "Please select Pillar Two status for all candidates" |
| VT-004 | All fields complete | Assessment runs successfully |

---

## 8. Validation & Error Handling

### 8.1 Required Field Validation

| Field | Validation | Error Message |
|-------|------------|---------------|
| MNE Group Name | Not empty | "Please enter the MNE group name" |
| UPE Jurisdiction | Selected | "Please select the UPE jurisdiction" |
| UPE Local Filing | Selected | "Please indicate if local filing is required" |
| At least one candidate | Exists | "Please add at least one DFE candidate" |
| Candidate jurisdiction | Selected | "Please select jurisdiction for all candidates" |

### 8.2 Warning Messages

| Condition | Warning |
|-----------|---------|
| UPE not in candidate list | "Consider adding the UPE as a DFE candidate" |
| All candidates have low data availability | "Limited data visibility may impact GIR quality" |
| Only one candidate | "Consider evaluating additional alternatives" |
| No candidate in implemented jurisdiction | "No candidate is in a Pillar Two implemented jurisdiction" |

---

## 9. Accessibility Requirements

| Requirement | Implementation |
|-------------|----------------|
| Keyboard Navigation | Tab through all fields, arrow keys for ratings |
| Screen Reader | ARIA labels on all controls, scores announced |
| Color Contrast | Minimum 4.5:1 for all text |
| Star Ratings | Also shown as numeric (e.g., "4 out of 5") |
| Focus Indicators | Visible focus ring on all interactive elements |

---

## 10. Technical Notes

### 10.1 Data Model

```typescript
interface DFEAssessment {
  id: string;
  mneGroupName: string;
  upeJurisdiction: string;
  upeLocalFiling: boolean;
  totalJurisdictions: number;
  fiscalYear: number;
  candidates: DFECandidate[];
  results: DFEResults | null;
  createdAt: Date;
}

interface DFECandidate {
  entityName: string;
  jurisdiction: string;
  isUPE: boolean;
  pillarTwoStatus: 'FULL' | 'PARTIAL' | 'ANNOUNCED' | 'NONE';
  taxTeamSize: number;
  systemsCapability: 'ERP_INTEGRATED' | 'SAP' | 'LOCAL_SYSTEM' | 'LIMITED';
  advisorSupport: 'BIG4' | 'MID_TIER' | 'LOCAL_FIRM' | 'NONE';
  dataAvailability: 1 | 2 | 3 | 4 | 5;
  hasGIRExperience: boolean;
}

interface DFEResults {
  recommendation: DFECandidate;
  confidenceScore: number;
  confidenceLevel: 'HIGH' | 'MEDIUM' | 'LOW' | 'INSUFFICIENT';
  primaryReason: string;
  strengths: string[];
  considerations: string[];
  candidateScores: CandidateScore[];
  notificationCount: number;
}
```

### 10.2 Dependencies

- Jurisdiction reference data (Pillar Two implementation status)
- No external APIs required
- No data persistence required (session only)

### 10.3 Performance

- Score calculation: < 100ms
- No network requests during assessment

---

## 11. Limitations & Scope

### 11.1 In Scope

- ✅ Multi-candidate DFE comparison
- ✅ Weighted scoring algorithm
- ✅ Notification requirements summary
- ✅ Score breakdown visualization
- ✅ Case study pre-load

### 11.2 Out of Scope

- ❌ Binding legal advice on DFE election
- ❌ Verification of actual exchange agreements
- ❌ Submission to tax authorities
- ❌ Notification tracking/status
- ❌ Commercial/political factors in selection
- ❌ DFE change/transfer scenarios

---

## 12. Version History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2024-12-07 | — | Initial specification (as GIR-007) |
| 2.0 | 2024-12-08 | — | Renumbered to GIR-005, updated cross-references, aligned test cases with Case Study 1 |

---

## 13. Migration Notes

### 13.1 Renumbering

| Previous | New | Change |
|----------|-----|--------|
| GIR-007 | GIR-005 | Renumbered due to tool consolidation |

### 13.2 Cross-Reference Updates

| Old Reference | New Reference |
|---------------|---------------|
| GIR-005 (Deadline Calculator) | GIR-003 (Filing Deadline Calculator) |
| GIR-008 (Practice Form) | GIR-004 (GIR Practice Form) |
| GIR-009 (Audit Checklist) | GIR-006 (Audit File Checklist) |

---

## 14. Appendix: Pillar Two Implementation Status Reference

| Jurisdiction | IIR | UTPR | QDMTT | GIR Filing | Exchange |
|--------------|-----|------|-------|------------|----------|
| United Kingdom | 2024 | 2025 | No | Yes | EU, OECD |
| Ireland | 2024 | 2025 | 2024 | Yes | EU, OECD |
| Netherlands | 2024 | 2025 | 2024 | Yes | EU, OECD |
| Germany | 2024 | 2025 | Partial | Yes | EU, OECD |
| France | 2024 | 2025 | 2024 | Yes | EU, OECD |
| Switzerland | No | No | 2024 | Limited | OECD |
| United States | No | No | No | No | Limited |
| Australia | 2024 | 2025 | No | Yes | OECD |
| Japan | 2024 | 2025 | No | Yes | OECD |
| Singapore | 2025 | 2025 | 2025 | Yes | OECD |

**Note:** Status as of late 2024. Subject to change.

---

## 15. Appendix: DFE Decision Flowchart

```
                    START
                      │
                      ▼
        ┌───────────────────────┐
        │ Has UPE jurisdiction  │
        │ implemented Pillar    │
        │ Two with GIR filing?  │
        └───────────────────────┘
                │
         ┌──────┴──────┐
         │ YES         │ NO
         ▼             ▼
   ┌───────────┐   ┌───────────────────┐
   │ UPE is    │   │ Must elect DFE in │
   │ natural   │   │ another Pillar    │
   │ DFE       │   │ Two jurisdiction  │
   │ option    │   └───────────────────┘
   └───────────┘            │
         │                  │
         ▼                  ▼
   ┌─────────────────────────────────┐
   │ Evaluate options based on:      │
   │ • UPE status                    │
   │ • Tax team resources            │
   │ • Systems capability            │
   │ • Advisor support               │
   │ • Data availability             │
   └─────────────────────────────────┘
                │
                ▼
   ┌─────────────────────────────────┐
   │ Select DFE with highest score   │
   │ Document election in GIR        │
   │ Send notifications to all       │
   │ CE jurisdictions                │
   └─────────────────────────────────┘
                │
                ▼
               END
```

---

*End of GIR-005 DFE Assessment Tool Specification*
