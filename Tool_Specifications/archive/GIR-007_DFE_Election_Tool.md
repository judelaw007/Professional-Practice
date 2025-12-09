# GIR-007: DFE Election Assessment Tool - Tool Specification

**Version:** 1.0
**Last Updated:** 2024-12-07
**Status:** Planned
**Platform:** tools.mojitax.com

---

## 1. Tool Metadata

| Field | Value |
|-------|-------|
| Tool ID | GIR-007 |
| Tool Name | GIR DFE Election Assessment Tool |
| Category | Pillar Two |
| Form Type | Assessment |
| Status | Planned |
| Used By | GloBE Information Return: Complete Filing Implementation |
| Introduced In | Section 3.3 - Filing Entity Selection and Notifications |

---

## 2. Purpose & Learning Objective

### 2.1 Purpose
Practice evaluating which entity should be elected as the Designated Filing Entity (DFE) for GIR filing. This tool helps learners understand the criteria for DFE selection, the implications of the choice, and the notification requirements that follow.

### 2.2 Learning Objective
After using this tool, learners will be able to:
- Understand the role and responsibilities of a Designated Filing Entity
- Evaluate multiple DFE options based on practical criteria
- Identify the filing obligations created by DFE election
- Understand notification requirements to relevant tax authorities
- Recognize the factors that make one DFE option preferable over another
- Consider data availability and coordination challenges in DFE selection

### 2.3 Prerequisites
Learners should understand:
- The GIR filing obligation under Pillar Two
- The concept of Ultimate Parent Entity (UPE)
- Basic group structure and jurisdiction concepts
- The relationship between filing entity and filing jurisdiction

### 2.4 DFE Concept Overview

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

### 3.1 UPE Jurisdiction

| Property | Value |
|----------|-------|
| Field ID | `upe_jurisdiction` |
| Label | UPE Jurisdiction |
| Data Type | String (dropdown selection) |
| Required | **Yes** |
| UI Element | Searchable dropdown |
| Default Value | Empty |
| Help Text | "The jurisdiction where the Ultimate Parent Entity is located (tax residence)" |

**Dropdown Options (Key Jurisdictions):**
| Code | Display | Pillar Two Status | GIR Filing |
|------|---------|-------------------|------------|
| UK | United Kingdom | Implemented | Yes |
| IE | Ireland | Implemented | Yes |
| NL | Netherlands | Implemented | Yes |
| DE | Germany | Implemented | Yes |
| FR | France | Implemented | Yes |
| CH | Switzerland | QDMTT only | Limited |
| US | United States | Not implemented | No |
| AU | Australia | Implemented | Yes |
| JP | Japan | Implemented | Yes |
| SG | Singapore | Partial | Yes |
| OTHER | Other jurisdiction | Varies | Varies |

**Validation Rules:**
| Rule | Condition | Error Message |
|------|-----------|---------------|
| Required | No selection made | "Please select the UPE jurisdiction" |

---

### 3.2 UPE Has Local GIR Filing Requirement

| Property | Value |
|----------|-------|
| Field ID | `upe_local_filing` |
| Label | Does the UPE jurisdiction require local GIR filing? |
| Data Type | Boolean |
| Required | **Yes** |
| UI Element | Yes/No radio buttons |
| Default Value | null (must select) |
| Help Text | "Some jurisdictions require a local GIR filing in addition to or instead of the central DFE filing. Check if the UPE jurisdiction has this requirement." |

**Display Values:**
| Value | Display Text |
|-------|--------------|
| true | Yes - UPE jurisdiction requires local GIR filing |
| false | No - No local filing requirement in UPE jurisdiction |

**Auto-suggestion by Jurisdiction:**
| UPE Jurisdiction | Suggested Value | Note |
|------------------|-----------------|------|
| UK | Yes | HMRC requires UK UPE groups to file locally |
| NL | Yes | Netherlands requires local filing for Dutch UPEs |
| US | No | US has not implemented Pillar Two |
| CH | No | Switzerland has QDMTT only, no GIR requirement |

---

### 3.3 Potential DFE Jurisdictions

| Property | Value |
|----------|-------|
| Field ID | `potential_dfe_jurisdictions` |
| Label | Potential DFE Jurisdictions |
| Data Type | Array of strings (multi-select) |
| Required | **Yes** |
| Min Selection | 1 |
| Max Selection | 10 |
| UI Element | Multi-select checkboxes or tag input |
| Help Text | "Select all jurisdictions where the group has entities that could potentially serve as DFE. Include the UPE jurisdiction if applicable." |

**Dropdown Options:** Same jurisdiction list as UPE Jurisdiction

**Validation Rules:**
| Rule | Condition | Error Message |
|------|-----------|---------------|
| Required | No selection made | "Please select at least one potential DFE jurisdiction" |
| Min selection | Less than 1 selected | "Select at least one potential DFE jurisdiction" |

---

### 3.4 Group Structure Complexity

| Property | Value |
|----------|-------|
| Field ID | `structure_complexity` |
| Label | Group Structure Complexity |
| Data Type | String (enumerated) |
| Required | **Yes** |
| UI Element | Radio buttons with descriptions |
| Default Value | null (must select) |
| Help Text | "Rate the complexity of your group's ownership structure" |

**Options:**
| Value | Display Text | Description |
|-------|--------------|-------------|
| LOW | Low | Simple structure: Single UPE with direct subsidiaries, few jurisdictions (<5), no complex holdings |
| MEDIUM | Medium | Moderate structure: Multiple holding layers, 5-15 jurisdictions, some JVs or minority interests |
| HIGH | High | Complex structure: Multiple POPEs, JVs, extensive holding chains, >15 jurisdictions, M&A activity |

---

### 3.5 Data Availability Assessment

| Property | Value |
|----------|-------|
| Field ID | `data_availability` |
| Label | Data Availability by Potential DFE Location |
| Data Type | Array of objects |
| Required | **Yes** |
| UI Element | Rating table |
| Help Text | "For each potential DFE jurisdiction, rate the availability of group-wide GloBE data at that location" |

**Rating Scale:**
| Rating | Value | Description |
|--------|-------|-------------|
| ★★★★★ | 5 | Excellent - Centralized data, direct access to all entities |
| ★★★★☆ | 4 | Good - Most data readily available, minor gaps |
| ★★★☆☆ | 3 | Moderate - Data available but requires coordination |
| ★★☆☆☆ | 2 | Limited - Significant data collection effort required |
| ★☆☆☆☆ | 1 | Poor - Major gaps, limited visibility |

**UI Display:**
```
┌─────────────────────────────────────────────────────────────────┐
│ DATA AVAILABILITY ASSESSMENT                                    │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│ Rate data availability for each potential DFE location:         │
│                                                                 │
│ United Kingdom     [★][★][★][★][★]  Excellent                  │
│ Ireland            [★][★][★][★][☆]  Good                       │
│ Netherlands        [★][★][★][☆][☆]  Moderate                   │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

### 3.6 Existing Tax Function Locations

| Property | Value |
|----------|-------|
| Field ID | `tax_function_locations` |
| Label | Existing Tax/Finance Function Locations |
| Data Type | Array of strings (multi-select) |
| Required | **No** (optional) |
| UI Element | Multi-select from potential DFE jurisdictions |
| Help Text | "Select jurisdictions where the group has existing tax or finance teams that could manage GIR filing" |

---

### 3.7 Preferred Language

| Property | Value |
|----------|-------|
| Field ID | `preferred_language` |
| Label | Preferred Filing Language |
| Data Type | String (dropdown) |
| Required | **No** (optional) |
| Default Value | "English" |
| UI Element | Dropdown select |
| Options | English, German, French, Dutch, Other |
| Help Text | "If the group has a preference for filing language, this may influence DFE selection" |

---

## 4. Output Fields

### 4.1 DFE Recommendation Summary

| Property | Value |
|----------|-------|
| Field ID | `recommendation_summary` |
| Label | DFE Recommendation |
| Data Type | Object |
| UI Element | Highlighted recommendation card |

**Display Components:**
| Component | Description |
|-----------|-------------|
| Recommended DFE | Primary recommended jurisdiction |
| Confidence | High / Medium / Low |
| Key Reason | Primary factor for recommendation |

---

### 4.2 DFE Options Comparison Table

| Property | Value |
|----------|-------|
| Field ID | `options_comparison` |
| Label | DFE Options Comparison |
| Data Type | Array of option objects |
| UI Element | Comparison table with scoring |

**Table Columns:**
| Column | Description |
|--------|-------------|
| Jurisdiction | DFE jurisdiction option |
| Overall Score | Weighted score (0-100) |
| Pillar Two Status | Implementation status |
| Data Availability | User-provided rating |
| Filing Infrastructure | Assessment of local filing capability |
| Exchange Agreements | Coverage of group jurisdictions |
| Recommendation | Recommended / Alternative / Not Recommended |

---

### 4.3 Detailed Analysis per Option

For each DFE option, provide:

| Property | Value |
|----------|-------|
| Field ID | `option_analysis` |
| Label | Detailed Analysis |
| Data Type | Object per jurisdiction |
| UI Element | Expandable cards |

**Analysis Components:**

**Pros:**
- List of advantages for this DFE option

**Cons:**
- List of disadvantages for this DFE option

**Filing Obligations Created:**
- Primary GIR filing in this jurisdiction
- Any secondary/local filings required
- Notification requirements

**Risk Assessment:**
- Low / Medium / High risk rating
- Key risk factors

---

### 4.4 Notification Requirements

| Property | Value |
|----------|-------|
| Field ID | `notification_requirements` |
| Label | Notification Requirements |
| Data Type | Array of notification objects |
| UI Element | Checklist table |

**Table Format:**
```
┌──────────────────┬──────────────────┬────────────────┬───────────┐
│ Jurisdiction     │ Notification To  │ Deadline       │ Method    │
├──────────────────┼──────────────────┼────────────────┼───────────┤
│ United Kingdom   │ HMRC             │ Same as GIR    │ Digital   │
│ Ireland          │ Revenue          │ Same as GIR    │ ROS       │
│ Germany          │ BZSt             │ Same as GIR    │ Online    │
│ Netherlands      │ Belastingdienst  │ Same as GIR    │ Portal    │
└──────────────────┴──────────────────┴────────────────┴───────────┘
```

---

### 4.5 Implementation Checklist

| Property | Value |
|----------|-------|
| Field ID | `implementation_checklist` |
| Label | DFE Election Implementation Checklist |
| Data Type | Array of checklist items |
| UI Element | Checklist with status |

**Checklist Items:**
```
□ Confirm DFE entity has legal authority to file on behalf of group
□ Register with filing jurisdiction's tax authority
□ Establish data collection processes from all CEs
□ Prepare notification letters for all CE jurisdictions
□ Set up filing calendar and reminder system
□ Document DFE election in GIR Section 1
□ Coordinate with local compliance teams
□ Establish amendment procedures
```

---

## 5. Calculation Logic

### 5.1 DFE Scoring Algorithm

```
FUNCTION AssessDFEOptions(inputs):

    options = []

    FOR EACH jurisdiction IN inputs.potential_dfe_jurisdictions:

        score = CalculateDFEScore(jurisdiction, inputs)
        analysis = GenerateAnalysis(jurisdiction, inputs)

        options.APPEND({
            jurisdiction: jurisdiction,
            score: score,
            analysis: analysis
        })

    END FOR

    // Sort by score descending
    options = SORT(options, BY score DESC)

    // Determine recommendation
    IF options[0].score >= 70 THEN
        recommendation = {
            jurisdiction: options[0].jurisdiction,
            confidence: "HIGH",
            reason: GetPrimaryReason(options[0])
        }
    ELSE IF options[0].score >= 50 THEN
        recommendation = {
            jurisdiction: options[0].jurisdiction,
            confidence: "MEDIUM",
            reason: GetPrimaryReason(options[0])
        }
    ELSE
        recommendation = {
            jurisdiction: options[0].jurisdiction,
            confidence: "LOW",
            reason: "No strong DFE option - consider alternatives"
        }
    END IF

    RETURN {
        recommendation: recommendation,
        options: options,
        notifications: GenerateNotifications(recommendation.jurisdiction, inputs)
    }

END FUNCTION
```

### 5.2 Scoring Criteria

```
FUNCTION CalculateDFEScore(jurisdiction, inputs):

    score = 0
    max_score = 100

    // FACTOR 1: Pillar Two Implementation (25 points max)
    implementation_status = GetImplementationStatus(jurisdiction)
    IF implementation_status == "FULL" THEN
        score += 25
    ELSE IF implementation_status == "PARTIAL" THEN
        score += 15
    ELSE IF implementation_status == "ANNOUNCED" THEN
        score += 5
    ELSE
        score += 0  // Not implemented
    END IF

    // FACTOR 2: Data Availability (25 points max)
    data_rating = inputs.data_availability[jurisdiction]
    score += data_rating × 5  // 1-5 rating × 5 = 5-25 points

    // FACTOR 3: UPE Alignment (20 points max)
    IF jurisdiction == inputs.upe_jurisdiction THEN
        score += 20  // Strong preference for UPE jurisdiction
    ELSE IF HasOwnershipLink(jurisdiction, inputs.upe_jurisdiction) THEN
        score += 10  // Some alignment
    ELSE
        score += 0
    END IF

    // FACTOR 4: Exchange Agreement Coverage (15 points max)
    coverage = GetExchangeCoverage(jurisdiction, inputs.all_ce_jurisdictions)
    score += coverage × 15  // 0-100% coverage × 15 points

    // FACTOR 5: Tax Function Presence (10 points max)
    IF jurisdiction IN inputs.tax_function_locations THEN
        score += 10
    END IF

    // FACTOR 6: Language Compatibility (5 points max)
    IF SupportsLanguage(jurisdiction, inputs.preferred_language) THEN
        score += 5
    END IF

    RETURN score

END FUNCTION
```

### 5.3 Implementation Status Reference

```
CONSTANT IMPLEMENTATION_STATUS = {
    UK: "FULL",      // IIR 2024, UTPR 2025
    IE: "FULL",      // IIR 2024, QDMTT 2024
    NL: "FULL",      // IIR 2024, UTPR 2025, QDMTT 2024
    DE: "FULL",      // IIR 2024, UTPR 2025
    FR: "FULL",      // IIR 2024, UTPR 2025, QDMTT 2024
    CH: "PARTIAL",   // QDMTT only
    US: "NONE",      // Not implemented
    AU: "FULL",      // IIR 2024
    JP: "FULL",      // IIR 2024
    SG: "PARTIAL"    // Announced, phased implementation
}
```

### 5.4 Pros and Cons Generation

```
FUNCTION GenerateProsAndCons(jurisdiction, inputs):

    pros = []
    cons = []

    // UPE jurisdiction considerations
    IF jurisdiction == inputs.upe_jurisdiction THEN
        pros.APPEND("Aligned with UPE location - natural filing point")
        pros.APPEND("Likely has best visibility of group-wide data")
    ELSE
        cons.APPEND("Not the UPE jurisdiction - may require additional coordination")
    END IF

    // Implementation status
    status = IMPLEMENTATION_STATUS[jurisdiction]
    IF status == "FULL" THEN
        pros.APPEND("Full Pillar Two implementation with established filing infrastructure")
    ELSE IF status == "PARTIAL" THEN
        cons.APPEND("Partial implementation - verify GIR filing capability")
    ELSE
        cons.APPEND("Pillar Two not implemented - cannot serve as DFE")
    END IF

    // Data availability
    data_rating = inputs.data_availability[jurisdiction]
    IF data_rating >= 4 THEN
        pros.APPEND("Good data availability at this location")
    ELSE IF data_rating <= 2 THEN
        cons.APPEND("Limited data availability - significant collection effort required")
    END IF

    // Tax function
    IF jurisdiction IN inputs.tax_function_locations THEN
        pros.APPEND("Existing tax/finance function to manage filing")
    ELSE
        cons.APPEND("No existing tax function - may need to build capability")
    END IF

    // Complexity considerations
    IF inputs.structure_complexity == "HIGH" THEN
        IF data_rating >= 4 THEN
            pros.APPEND("Central data access helpful for complex structure")
        ELSE
            cons.APPEND("Complex structure + limited data = high coordination burden")
        END IF
    END IF

    RETURN { pros: pros, cons: cons }

END FUNCTION
```

---

## 6. User Interface Specifications

### 6.1 Layout Structure

```
┌─────────────────────────────────────────────────────────────────┐
│  GIR DFE Election Assessment Tool                          [?]  │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │ INPUT SECTION                                            │   │
│  ├─────────────────────────────────────────────────────────┤   │
│  │                                                          │   │
│  │  UPE Jurisdiction:     [United Kingdom          ▼]      │   │
│  │                                                          │   │
│  │  Local GIR Filing Required in UPE Jurisdiction?          │   │
│  │                        ○ Yes    ○ No                     │   │
│  │                                                          │   │
│  │  Potential DFE Jurisdictions: (select all that apply)    │   │
│  │  ☑ United Kingdom    ☑ Ireland    ☐ Netherlands         │   │
│  │  ☐ Germany           ☐ France     ☐ Switzerland         │   │
│  │                                                          │   │
│  │  Group Structure Complexity:                             │   │
│  │  ○ Low    ○ Medium    ○ High                            │   │
│  │                                                          │   │
│  │  Data Availability by Location:                          │   │
│  │  United Kingdom  [★★★★★]                                │   │
│  │  Ireland         [★★★★☆]                                │   │
│  │                                                          │   │
│  │  Tax Function Locations: (optional)                      │   │
│  │  ☑ United Kingdom    ☐ Ireland                          │   │
│  │                                                          │   │
│  │  [  Assess DFE Options  ]    [  Clear  ]                │   │
│  │                                                          │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                 │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │ RECOMMENDATION                                           │   │
│  ├─────────────────────────────────────────────────────────┤   │
│  │                                                          │   │
│  │  ┌─────────────────────────────────────────────┐        │   │
│  │  │  RECOMMENDED DFE: UNITED KINGDOM            │        │   │
│  │  │  Confidence: HIGH                           │        │   │
│  │  │                                             │        │   │
│  │  │  Primary Reason: UPE jurisdiction with full │        │   │
│  │  │  Pillar Two implementation and excellent    │        │   │
│  │  │  data availability                          │        │   │
│  │  └─────────────────────────────────────────────┘        │   │
│  │                                                          │   │
│  │  OPTIONS COMPARISON                                     │   │
│  │  ┌────────────────┬───────┬──────────┬──────────────┐   │   │
│  │  │ Jurisdiction   │ Score │ Status   │ Recommend    │   │   │
│  │  ├────────────────┼───────┼──────────┼──────────────┤   │   │
│  │  │ United Kingdom │  92   │ Full     │ ✓ RECOMMENDED│   │   │
│  │  │ Ireland        │  68   │ Full     │ Alternative  │   │   │
│  │  └────────────────┴───────┴──────────┴──────────────┘   │   │
│  │                                                          │   │
│  │  [▼ Show Detailed Analysis]                             │   │
│  │                                                          │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### 6.2 Detailed Analysis Panel (Expanded)

```
┌─────────────────────────────────────────────────────────────────┐
│ DETAILED ANALYSIS: UNITED KINGDOM                               │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  SCORE BREAKDOWN                                               │
│  ├── Pillar Two Status:    25/25  (Full implementation)       │
│  ├── Data Availability:    25/25  (★★★★★ Excellent)           │
│  ├── UPE Alignment:        20/20  (Is UPE jurisdiction)       │
│  ├── Exchange Coverage:    12/15  (80% coverage)              │
│  ├── Tax Function:         10/10  (Present)                   │
│  └── Language:              0/5   (English - N/A)             │
│  ════════════════════════════════════════════                  │
│  TOTAL:                    92/100                              │
│                                                                 │
│  PROS                                                          │
│  ✓ Aligned with UPE location - natural filing point           │
│  ✓ Full Pillar Two implementation with established filing     │
│  ✓ Excellent data availability at this location               │
│  ✓ Existing tax/finance function to manage filing             │
│                                                                 │
│  CONS                                                          │
│  ✗ UK requires local GIR filing (additional obligation)       │
│                                                                 │
│  FILING OBLIGATIONS                                            │
│  • File GIR with HMRC via digital service                     │
│  • Register for Pillar Two before first filing                │
│  • Submit notifications to all CE jurisdictions               │
│                                                                 │
│  RISK ASSESSMENT: LOW                                          │
│  Established jurisdiction with clear guidance and support      │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### 6.3 Notification Requirements Panel

```
┌─────────────────────────────────────────────────────────────────┐
│ NOTIFICATION REQUIREMENTS                                       │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  If you elect United Kingdom as DFE, notify these authorities: │
│                                                                 │
│  ┌─────────────┬──────────────────┬─────────────┬───────────┐  │
│  │ Jurisdiction│ Authority        │ Deadline    │ Status    │  │
│  ├─────────────┼──────────────────┼─────────────┼───────────┤  │
│  │ ☐ UK        │ HMRC             │ With GIR    │ Required  │  │
│  │ ☐ Ireland   │ Revenue          │ With GIR    │ Required  │  │
│  │ ☐ Germany   │ BZSt             │ With GIR    │ Required  │  │
│  │ ☐ France    │ DGFiP            │ With GIR    │ Required  │  │
│  │ ☐ Singapore │ IRAS             │ With GIR    │ Required  │  │
│  └─────────────┴──────────────────┴─────────────┴───────────┘  │
│                                                                 │
│  Total notifications required: 5                               │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## 7. User Flow

### 7.1 Happy Path Flow

```
Step 1: User navigates to DFE Election Assessment Tool
        → Page loads with empty input fields

Step 2: User selects UPE Jurisdiction
        → e.g., United Kingdom
        → System may auto-suggest local filing requirement

Step 3: User indicates local filing requirement
        → Yes/No selection

Step 4: User selects potential DFE jurisdictions
        → Multi-select from available options
        → Should include UPE jurisdiction if applicable

Step 5: User rates group structure complexity
        → Low / Medium / High

Step 6: User rates data availability for each potential DFE
        → Star rating for each selected jurisdiction

Step 7: User optionally indicates tax function locations
        → Multi-select from potential DFE jurisdictions

Step 8: User clicks "Assess DFE Options"
        → System calculates scores for each option
        → Recommendation displayed prominently
        → Comparison table shows all options
        → Detailed analysis available via expansion

Step 9: User reviews recommendation
        → Expands detailed analysis for preferred options
        → Reviews pros and cons
        → Notes notification requirements

Step 10: User uses implementation checklist
         → Tracks steps to implement DFE election
```

---

## 8. Edge Cases & Error Handling

### 8.1 Edge Cases

| Scenario | Expected Behavior |
|----------|-------------------|
| Only one DFE option selected | Still provide analysis, note limited alternatives |
| UPE jurisdiction not in potential DFEs | Warning: "Consider including UPE jurisdiction as potential DFE" |
| No implemented jurisdictions selected | Error: "No selected jurisdiction has GIR filing capability" |
| All options score below 50 | Show recommendation with LOW confidence + advisory message |
| US as UPE, no US in potential DFEs | Normal operation - US cannot be DFE |
| Equal scores for top options | Show both as "Recommended" with note |

### 8.2 Warning Messages

| Condition | Warning Message |
|-----------|-----------------|
| UPE not in DFE options | "Consider including the UPE jurisdiction (XX) as a potential DFE option" |
| Low data availability for all | "Limited data availability across all options - significant collection effort expected" |
| Complex structure + low data | "High complexity with limited data availability - consider centralized data strategy before DFE election" |
| Non-implemented UPE | "UPE jurisdiction has not implemented Pillar Two - DFE must be in another jurisdiction" |

### 8.3 Error Messages

| Error Code | Trigger | User Message |
|------------|---------|--------------|
| ERR_001 | UPE jurisdiction empty | "Please select the UPE jurisdiction" |
| ERR_002 | Local filing not selected | "Please indicate if the UPE jurisdiction requires local GIR filing" |
| ERR_003 | No potential DFEs selected | "Please select at least one potential DFE jurisdiction" |
| ERR_004 | Complexity not selected | "Please rate the group structure complexity" |
| ERR_005 | Data availability not rated | "Please rate data availability for all potential DFE jurisdictions" |
| ERR_006 | No valid DFE options | "None of the selected jurisdictions can serve as DFE - please select jurisdictions with Pillar Two implementation" |

---

## 9. Test Cases

### 9.1 Functional Test Cases

| Test ID | Description | Inputs | Expected Output |
|---------|-------------|--------|-----------------|
| TC-001 | UK UPE, UK as DFE | UPE: UK, DFEs: UK/IE, Data: UK=5/IE=4, Complexity: Low | Recommend UK (score ~90+) |
| TC-002 | US UPE, must use EU DFE | UPE: US, DFEs: UK/NL, Data: UK=4/NL=4 | Recommend either UK or NL |
| TC-003 | Multiple equal options | UPE: DE, DFEs: DE/NL/FR, all equal ratings | Show multiple recommendations |
| TC-004 | Single option | UPE: AU, DFEs: AU only | Recommend AU with note |
| TC-005 | Non-implemented only | UPE: US, DFEs: US only | Error - no valid DFE |
| TC-006 | Complex structure test | UPE: UK, Complexity: HIGH, Data: Low | Warning about coordination |

### 9.2 Score Calculation Test Cases

| Test ID | Inputs | Expected Score Breakdown |
|---------|--------|--------------------------|
| SC-001 | UK UPE, UK DFE, Data=5, Tax=Yes | Status:25 + Data:25 + UPE:20 + Tax:10 = 80+ |
| SC-002 | US UPE, UK DFE, Data=4, Tax=Yes | Status:25 + Data:20 + UPE:0 + Tax:10 = 55+ |
| SC-003 | CH DFE option | Status:15 (partial) + other factors |

### 9.3 Validation Test Cases

| Test ID | Description | Input | Expected Result |
|---------|-------------|-------|-----------------|
| VT-001 | Empty UPE | upe_jurisdiction = "" | ERR_001 displayed |
| VT-002 | No DFEs selected | potential_dfe = [] | ERR_003 displayed |
| VT-003 | Missing data rating | data_availability = incomplete | ERR_005 displayed |
| VT-004 | Valid inputs | All fields complete | Assessment runs |

---

## 10. Accessibility Requirements

| Requirement | Implementation |
|-------------|----------------|
| Keyboard navigation | All inputs accessible via Tab, radio buttons via arrow keys |
| Screen reader | ARIA labels on all controls, scores announced |
| Color contrast | Minimum 4.5:1 for text |
| Star ratings | Also shown as numeric (e.g., "4 out of 5") |
| Recommendation | Announced prominently to screen readers |

---

## 11. Technical Notes

### 11.1 Dependencies
- Jurisdiction reference data (implementation status, exchange agreements)
- No external APIs required
- No data persistence required

### 11.2 Performance
- Score calculation: <100ms
- No network requests during assessment

### 11.3 Browser Support
- Chrome (latest 2 versions)
- Firefox (latest 2 versions)
- Safari (latest 2 versions)
- Edge (latest 2 versions)

---

## 12. Limitations & Scope

This demo tool does **NOT**:
- Provide binding legal advice on DFE election
- Verify actual exchange agreement coverage
- Submit DFE elections to tax authorities
- Track notification status
- Account for all jurisdiction-specific requirements
- Consider commercial or political factors in DFE selection
- Handle group reorganizations or DFE changes

This tool is for **learning purposes only** to understand DFE election considerations.

---

## 13. Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2024-12-07 | Initial specification |

---

## 14. Appendix: Case Study Alignment

### Case Study 1: GlobalTech Manufacturing

**DFE Assessment Scenario:**
- To be added to Sample_Data.md:
  - UPE Jurisdiction: United Kingdom
  - UPE Local Filing Required: Yes
  - Potential DFE Jurisdictions: UK, Ireland
  - Group Structure Complexity: Medium (8 jurisdictions)
  - Data Availability: UK=5, Ireland=4
  - Tax Function Locations: UK

- Expected Outcomes:
  - Recommended DFE: United Kingdom
  - Confidence: High
  - Key Reason: UPE jurisdiction with full implementation and excellent data availability
  - Notifications Required: All 8 CE jurisdictions

---

## 15. Appendix: Pillar Two Implementation Status

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

## 16. Appendix: DFE Decision Flowchart

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
   │ • Data availability             │
   │ • Tax function presence         │
   │ • Exchange agreement coverage   │
   │ • Filing infrastructure         │
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
