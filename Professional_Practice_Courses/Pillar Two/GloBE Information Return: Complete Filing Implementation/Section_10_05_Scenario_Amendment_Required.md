# Section 10.5: Scenario 5 - Amendment Required

## Learning Objectives

By the end of this section, you will be able to:
- Identify material errors requiring GIR amendment
- Apply jurisdiction-specific amendment procedures
- Implement penalty mitigation strategies under the transitional relief regime
- Document amended filings to satisfy audit requirements
- Coordinate amended GIR filing with local Top-up Tax return corrections

---

## Scenario Facts: Phoenix Aerospace Holdings plc

**Group Profile:**
- UK-parented multinational aerospace manufacturer
- 65 Constituent Entities across 18 jurisdictions
- Consolidated revenue: €2.8 billion
- Fiscal Year End: 31 December 2024
- First GIR filing completed: 15 May 2026

**Original GIR Filing Summary:**
- Filed via UK Designated Filing Entity
- Reported Top-up Tax in three jurisdictions:
  - Ireland: €1,245,000 (ETR 11.2%)
  - Singapore: €890,000 (ETR 12.8%)
  - Switzerland: QDMTT fully offset
- Safe Harbour applied to 8 jurisdictions via Transitional CbCR Safe Harbour

**Error Discovery Timeline:**
- 3 September 2026: Internal audit identifies material error
- Error relates to Irish operations during FY2024
- Discovery occurs 7 months after filing deadline

---

## Part 1: Error Identification Process

### 1.1 How the Error Was Discovered

During routine post-filing internal audit procedures, Phoenix Aerospace's tax team identified a significant error in the Irish jurisdictional calculation:

**Nature of the Error:**

| Element | Originally Reported | Correct Position | Impact |
|---------|---------------------|------------------|--------|
| GloBE Revenue | €156,000,000 | €156,000,000 | No change |
| GloBE Income | €28,400,000 | €42,600,000 | +€14,200,000 |
| Covered Taxes | €3,180,480 | €4,771,200 | +€1,590,720 |
| Adjusted Covered Taxes | €3,180,480 | €4,771,200 | +€1,590,720 |
| ETR | 11.20% | 11.20% | No change |
| SBIE | €5,112,000 | €5,112,000 | No change |
| Excess Profit | €23,288,000 | €37,488,000 | +€14,200,000 |
| Top-up Tax Percentage | 3.80% | 3.80% | No change |
| Top-up Tax | €885,000 | €1,424,544 | +€539,544 |

**Root Cause Analysis:**

The error arose from the incorrect treatment of a €14.2 million intercompany royalty receivable. The Irish subsidiary, Phoenix Aerospace Ireland Ltd, received royalty income from a UK affiliate during Q4 2024. The original GIR preparation erroneously:

1. **Excluded the royalty from GloBE Income** - treating it as eliminated intercompany income rather than recognising it in the Irish jurisdiction's results
2. **Omitted associated Irish withholding tax** - the €1,590,720 Irish tax on the royalty was correspondingly excluded from Covered Taxes

The net ETR remained unchanged at 11.20%, but the absolute Top-up Tax increased by €539,544 due to the higher Excess Profit base.

### 1.2 Materiality Assessment Framework

Before proceeding with amendment, Phoenix Aerospace assessed whether the error met materiality thresholds requiring correction:

**Quantitative Materiality Tests:**

| Test | Threshold | Result | Conclusion |
|------|-----------|--------|------------|
| Absolute Top-up Tax change | >€100,000 | €539,544 | Material |
| Percentage of original liability | >10% | 43.3% | Material |
| Impact on ETR | >0.5% | 0% | Not material |
| Group-wide impact | >€500,000 | €539,544 | Material |

**Qualitative Materiality Factors:**

- **Systematic error risk**: Could the same error affect other jurisdictions? (Reviewed - isolated to Ireland)
- **Repeat filing impact**: Will the error recur in FY2025? (Addressed - process corrected)
- **Regulatory sensitivity**: Is the jurisdiction a high-scrutiny location? (Ireland actively monitoring Pillar Two compliance)
- **Audit trail implications**: Does non-correction create false records? (Yes - amendment required)

**Decision: Amendment Required**

Based on both quantitative thresholds and qualitative factors, Phoenix Aerospace concluded that amendment was mandatory rather than discretionary.

### 1.3 Error Classification Framework

**Category 1: Administrative Errors**
- Typographical mistakes
- Incorrect entity codes
- Wrong fiscal year references
- Generally correctable without penalty

**Category 2: Calculation Errors**
- Mathematical mistakes
- Incorrect formula application
- Currency conversion errors
- May attract penalties depending on materiality

**Category 3: Classification Errors**
- Wrong entity categorisation
- Incorrect ownership percentages
- Misapplied safe harbour elections
- Higher penalty risk due to judgmental nature

**Category 4: Omission Errors**
- Missing Constituent Entities
- Unreported income/expenses
- Excluded Covered Taxes
- Highest penalty risk - potential negligence finding

**Phoenix Aerospace Classification:**
The royalty error constituted a **Category 4: Omission Error** - income and taxes were incorrectly excluded from the Irish jurisdictional calculation.

---

## Part 2: Amendment Procedures by Jurisdiction

### 2.1 UK Amendment Procedure (Filing Jurisdiction)

As the Designated Filing Entity is UK-resident, the primary GIR amendment follows HMRC procedures.

**HMRC Multinational Top-up Tax Amendment Rules:**

Under Schedule 14 to Finance (No.2) Act 2023, the filing member may amend its self-assessment return within defined time limits:

| Amendment Type | Time Limit | Authority |
|----------------|------------|-----------|
| Taxpayer-initiated amendment | 12 months from original filing date | Para 19, Schedule 14 |
| HMRC compliance check amendment | 12 months from amendment date | Para 28, Schedule 14 |
| Discovery assessment (HMRC) | 4 years from end of accounting period | Para 31, Schedule 14 |

**Phoenix Aerospace Timeline Analysis:**

- Original filing date: 15 May 2026
- 12-month amendment window: Until 15 May 2027
- Error discovered: 3 September 2026
- **Conclusion**: Within taxpayer-initiated amendment window

**Amendment Filing Steps:**

1. **Prepare Amended GIR**
   - Generate corrected XML file with amended return indicator = "Yes"
   - Update all affected Section 2 and Section 3 data elements
   - Document all changes in supporting workpapers

2. **Submit to HMRC**
   - File amended GIR via HMRC's digital submission portal
   - Include covering letter explaining nature and cause of error
   - Attach calculation workpapers demonstrating correction

3. **Pay Additional Top-up Tax**
   - Calculate interest on late payment from original due date
   - Submit payment with amended return reference

4. **Notify Other Jurisdictions**
   - Inform Irish Revenue of amended UK-filed GIR
   - Provide copy of amended jurisdictional data

### 2.2 Ireland - Domestic Top-up Tax Impact

The error directly affects Irish Top-up Tax liability. Ireland has implemented QDMTT (Qualified Domestic Minimum Top-up Tax) but Phoenix Aerospace Ireland Ltd was below the QDMTT threshold due to the original (incorrect) calculation.

**Revised Irish Position:**

| Element | Original | Amended | Change |
|---------|----------|---------|--------|
| GloBE Income | €28,400,000 | €42,600,000 | +€14,200,000 |
| Irish DTT liability | €0 | €0 | No change |
| IIR collected in UK | €885,000 | €1,424,544 | +€539,544 |

**Irish Revenue Notification Requirements:**

Although Ireland operates a QDMTT, Phoenix Aerospace Ireland Ltd's Top-up Tax is collected via the UK's IIR (as the UPE jurisdiction). The amended GIR:

1. Increases UK IIR collection
2. Does not create additional Irish DTT liability
3. Requires notification to Irish Revenue of amended position

**Irish Revenue Contact:**
- Email: pillar2@revenue.ie
- Reference: Company Tax Number + "GIR Amendment Notification"

### 2.3 Multi-Jurisdiction Amendment Coordination

When a GIR amendment affects multiple jurisdictions, coordination is essential:

**Amendment Impact Matrix for Phoenix Aerospace:**

| Jurisdiction | Filing Status | Amendment Impact | Action Required |
|--------------|---------------|------------------|-----------------|
| UK | DFE | Primary amendment | File amended GIR |
| Ireland | Affected | Top-up Tax increase | Notify Revenue |
| Germany | No change | — | None |
| France | No change | — | None |
| Netherlands | No change | — | None |
| Singapore | No change | — | None |
| Switzerland | No change | — | None |
| Other (11) | No change | — | None |

**Coordination Protocol:**

```
Week 1: Finalise corrected calculations
        Obtain sign-off from Group Tax Director

Week 2: Prepare amended GIR XML
        Draft covering letter to HMRC
        Calculate interest on underpayment

Week 3: Submit amended GIR to HMRC
        Pay additional Top-up Tax plus interest

Week 4: Notify Irish Revenue
        Update internal records
        Brief external auditors
```

### 2.4 Jurisdiction-Specific Amendment Procedures

**Germany (Minimum Tax Act - Mindeststeuergesetz):**

| Element | Requirement |
|---------|-------------|
| Amendment window | 4 years from assessment |
| Filing method | ELSTER electronic submission |
| Supporting documentation | Detailed calculation reconciliation |
| Language | German (official) |
| Contact | Bundeszentralamt für Steuern |

**Netherlands (Minimum Tax Act 2024 - Wet minimumbelasting 2024):**

| Element | Requirement |
|---------|-------------|
| Amendment window | 5 years from fiscal year end |
| Filing method | Online portal (Mijn Belastingdienst Zakelijk) |
| Supporting documentation | Amended return with explanation |
| Language | Dutch or English |
| Contact | Belastingdienst |

**France (Impôt Minimum Mondial):**

| Element | Requirement |
|---------|-------------|
| Amendment window | Until 31 December of 2nd year following assessment |
| Filing method | Via impots.gouv.fr professional portal |
| Supporting documentation | Formal réclamation with supporting evidence |
| Language | French |
| Contact | Direction Générale des Finances Publiques |

**Singapore (Global Anti-Base Erosion Rules):**

| Element | Requirement |
|---------|-------------|
| Amendment window | 4 years from end of basis period |
| Filing method | IRAS e-submission |
| Supporting documentation | Amendment request with detailed workings |
| Language | English |
| Contact | Inland Revenue Authority of Singapore |

---

## Part 3: Penalty Mitigation Strategies

### 3.1 OECD Transitional Penalty Relief Regime

The OECD Inclusive Framework established a Transitional Penalty Relief Regime recognising the complexity of initial GloBE compliance.

**Key Principle:**
> "No penalties or sanctions should apply during a transitional period in connection with filing GloBE Information Returns where an MNE has taken reasonable measures to ensure the correct application of the GloBE rules."

**Transitional Period:**
- Begins: Fiscal years starting on or after 31 December 2023
- Ends: Fiscal years ending after 30 June 2028
- Phoenix Aerospace FY2024: **Within transitional period**

**"Reasonable Measures" Standard:**

Tax administrations may consider that an MNE has taken reasonable measures where the MNE can demonstrate:

| Factor | Phoenix Aerospace Evidence |
|--------|---------------------------|
| Good faith compliance effort | Engaged Big 4 advisor for first filing |
| Documented processes | GIR preparation procedures manual in place |
| Training undertaken | Tax team completed Pillar Two training |
| Internal controls | Three-stage review process implemented |
| Timely disclosure | Error self-reported within 4 months of discovery |
| Prompt correction | Amendment filed within 6 weeks of discovery |

### 3.2 UK Penalty Framework

Under UK legislation, penalties for incorrect GIR filing follow established principles:

**Penalty Categories:**

| Behaviour | Penalty Range (Unprompted) | Penalty Range (Prompted) |
|-----------|---------------------------|-------------------------|
| Reasonable care taken | 0% | 0% |
| Careless error | 0-30% | 15-30% |
| Deliberate error | 20-70% | 35-70% |
| Deliberate and concealed | 30-100% | 50-100% |

**Phoenix Aerospace Penalty Assessment:**

| Factor | Analysis | Conclusion |
|--------|----------|------------|
| Nature of error | Omission of income/taxes | Careless, not deliberate |
| Systems in place | Documented controls existed | Demonstrates reasonable care intent |
| Discovery method | Self-identified | Unprompted disclosure |
| Disclosure timing | Within 4 months | Timely |
| Transitional relief | FY2024 within scope | Applicable |

**Expected Penalty Outcome:**
- **Primary position**: 0% penalty (reasonable care + transitional relief)
- **Fallback position**: 0-15% of understated tax (unprompted careless error)

### 3.3 Reasonable Excuse Defence

Under UK law, penalties do not apply if the filing member can demonstrate a "reasonable excuse" for the error.

**Reasonable Excuse Factors:**

| Factor | Weight | Phoenix Aerospace Position |
|--------|--------|---------------------------|
| Complexity of rules | High | First-year GloBE filing - novel rules |
| Reliance on advisors | Medium | Big 4 firm engaged |
| Systems failures | Medium | Intercompany elimination process error |
| Time pressures | Low | Filed ahead of deadline |
| Resource constraints | Low | Adequate resources deployed |

**Documentation to Support Reasonable Excuse:**

1. **Advisor engagement letter** - demonstrating professional advice sought
2. **Training records** - showing team preparation for Pillar Two
3. **Process documentation** - evidencing systematic approach
4. **Review evidence** - three-stage sign-off completed
5. **Error explanation** - detailed root cause analysis
6. **Corrective actions** - process improvements implemented

### 3.4 Interest Calculation

Regardless of penalty position, interest accrues on underpaid Top-up Tax:

**UK Interest Calculation:**

```
Underpaid amount:           £463,050 (€539,544 @ 0.8586 GBP/EUR)
Original due date:          30 June 2026
Amendment payment date:     20 October 2026 (assumed)
Days late:                  112 days
HMRC late payment rate:     7.5% p.a. (current rate)

Interest calculation:
£463,050 × 7.5% × (112/365) = £10,661
```

**Interest Mitigation:**
Interest cannot be mitigated or appealed - it compensates HMRC for late receipt of funds. However, prompt amendment minimises the interest quantum.

---

## Part 4: Documentation for Amended Filing

### 4.1 Amended GIR XML Structure

The amended GIR must include specific indicators and updated data:

**Section 1: General Information Updates**

```xml
<gir:GIR>
  <gir:GeneralInfo>
    <gir:ReportingFiscalYear>2024</gir:ReportingFiscalYear>
    <gir:ReportingMNEGroup>
      <gir:Name>Phoenix Aerospace Holdings plc</gir:Name>
      <gir:ResCountryCode>GB</gir:ResCountryCode>
    </gir:ReportingMNEGroup>
    <gir:FilingConstituent>
      <gir:Name>Phoenix Aerospace Holdings plc</gir:Name>
      <gir:TIN>1234567890</gir:TIN>
      <gir:ResCountryCode>GB</gir:ResCountryCode>
    </gir:FilingConstituent>
    <!-- CRITICAL: Amended Return Indicator -->
    <gir:AmendedReturn>true</gir:AmendedReturn>
    <gir:FilingDate>2026-10-15</gir:FilingDate>
  </gir:GeneralInfo>
```

**Section 2: Jurisdictional Data Updates (Ireland)**

```xml
<gir:JurisdictionalData>
  <gir:Jurisdiction>
    <gir:JurisdictionCode>IE</gir:JurisdictionCode>
    <gir:JurisdictionType>Standard</gir:JurisdictionType>

    <!-- AMENDED VALUES -->
    <gir:GloBERevenue>156000000</gir:GloBERevenue>
    <gir:GloBEIncomeOrLoss>42600000</gir:GloBEIncomeOrLoss>
    <gir:CoveredTaxes>4771200</gir:CoveredTaxes>
    <gir:AdjustedCoveredTaxes>4771200</gir:AdjustedCoveredTaxes>
    <gir:ETR>0.1120</gir:ETR>
    <gir:SubstanceBasedIncomeExclusion>5112000</gir:SubstanceBasedIncomeExclusion>
    <gir:ExcessProfit>37488000</gir:ExcessProfit>
    <gir:TopUpTaxPercentage>0.0380</gir:TopUpTaxPercentage>
    <gir:JurisdictionalTopUpTax>1424544</gir:JurisdictionalTopUpTax>

    <!-- Amendment Explanation Field -->
    <gir:AdditionalInfo>
      Amendment to correct omission of intercompany royalty income
      (EUR 14,200,000) and associated Irish covered taxes (EUR 1,590,720).
      Original filing dated 15 May 2026 understated jurisdictional
      top-up tax by EUR 539,544.
    </gir:AdditionalInfo>
  </gir:Jurisdiction>
</gir:JurisdictionalData>
```

**Section 3: Top-up Tax Allocation Updates**

```xml
<gir:TopUpTaxAllocation>
  <gir:Allocation>
    <gir:ChargedEntity>
      <gir:Name>Phoenix Aerospace Holdings plc</gir:Name>
      <gir:TIN>1234567890</gir:TIN>
      <gir:ResCountryCode>GB</gir:ResCountryCode>
    </gir:ChargedEntity>

    <gir:AllocationDetails>
      <gir:JurisdictionCode>IE</gir:JurisdictionCode>
      <gir:TopUpTaxAmount>1424544</gir:TopUpTaxAmount>
      <gir:AllocationRule>IIR</gir:AllocationRule>
      <gir:QDMTTOffset>0</gir:QDMTTOffset>
      <!-- AMENDED: Previous amount was 885000 -->
    </gir:AllocationDetails>

    <!-- Updated Group Total -->
    <gir:GroupTotalTopUpTax>2854544</gir:GroupTotalTopUpTax>
    <!-- Original: 2315000, Increase: 539544 -->
  </gir:Allocation>
</gir:TopUpTaxAllocation>
```

### 4.2 Amendment Covering Letter

**Template: HMRC GIR Amendment Covering Letter**

```
[Company Letterhead]

HM Revenue & Customs
Pillar 2 Compliance Team
[Address]

Date: [Amendment Filing Date]

Reference: Phoenix Aerospace Holdings plc
Company UTR: [UTR Number]
Multinational Top-up Tax Reference: [MTT Reference]
GloBE Information Return - Fiscal Year 2024 - AMENDED FILING

Dear Sirs,

AMENDED GLOBE INFORMATION RETURN - FISCAL YEAR ENDED 31 DECEMBER 2024

We write to submit an amended GloBE Information Return for Phoenix
Aerospace Holdings plc for the fiscal year ended 31 December 2024.

SUMMARY OF AMENDMENT

The original GIR, filed on 15 May 2026, contained an error in the
Irish jurisdictional calculation. This amendment corrects that error.

Nature of Error:
Intercompany royalty income of €14,200,000 received by Phoenix
Aerospace Ireland Ltd from Phoenix Aerospace UK Ltd was incorrectly
excluded from Irish GloBE Income. The associated Irish covered taxes
of €1,590,720 were correspondingly omitted.

Impact of Correction:
- Irish jurisdictional Top-up Tax increases from €885,000 to €1,424,544
- Group total Top-up Tax increases by €539,544
- IIR liability payable in UK increases by €539,544

ERROR DISCOVERY AND DISCLOSURE

The error was identified during internal post-filing audit procedures
on 3 September 2026. We are making voluntary disclosure of this error
in accordance with our obligations under Schedule 14, Finance (No.2)
Act 2023.

PENALTY RELIEF CLAIM

We request that no penalties be applied to this amendment on the
following grounds:

1. Transitional Period Relief: This filing relates to FY2024, within
   the OECD transitional penalty relief period.

2. Reasonable Measures: We can demonstrate that reasonable measures
   were taken to ensure correct GloBE application, including:
   - Engagement of [Advisor Name] for GloBE compliance advisory
   - Implementation of documented GIR preparation procedures
   - Three-stage review process for all calculations
   - Staff training on Pillar Two requirements

3. Voluntary Disclosure: This amendment is made on our own initiative,
   not prompted by HMRC enquiry.

4. Prompt Correction: Amendment submitted within [X] weeks of error
   discovery.

PAYMENT

We attach payment of £[Amount] representing:
- Additional Top-up Tax: £463,050
- Interest to date: £[Amount]
- Total: £[Total]

SUPPORTING DOCUMENTATION

The following documents accompany this submission:
1. Amended GIR XML file (USB/secure portal upload)
2. Reconciliation schedule: Original vs. Amended figures
3. Root cause analysis memorandum
4. Corrective action plan
5. Advisor engagement documentation

We confirm that to the best of our knowledge and belief, the amended
GIR is correct and complete.

Please contact [Name] at [Email] or [Phone] if you require any
additional information.

Yours faithfully,


[Authorised Signatory]
Group Tax Director
Phoenix Aerospace Holdings plc
```

### 4.3 Supporting Workpaper Package

**Required Documentation Checklist:**

| Document | Purpose | Retention Period |
|----------|---------|------------------|
| Original GIR copy | Baseline for comparison | 10 years |
| Amended GIR copy | Current filing record | 10 years |
| Reconciliation schedule | Document changes | 10 years |
| Root cause analysis | Explain error origin | 10 years |
| Board/Committee approval | Governance evidence | 10 years |
| Advisor correspondence | Professional advice evidence | 10 years |
| Process improvement memo | Demonstrate corrective action | 7 years |
| Interest calculation | Payment support | 7 years |
| Payment confirmation | Evidence of settlement | 7 years |

### 4.4 Reconciliation Schedule

**Original vs. Amended GIR Reconciliation - Ireland**

| Data Element | Original GIR | Amended GIR | Variance | Explanation |
|--------------|--------------|-------------|----------|-------------|
| **Section 2 - Jurisdictional Data** |||||
| GloBE Revenue | €156,000,000 | €156,000,000 | — | No change |
| GloBE Income | €28,400,000 | €42,600,000 | +€14,200,000 | Royalty income added |
| Covered Taxes | €3,180,480 | €4,771,200 | +€1,590,720 | WHT on royalty added |
| Adjusted Covered Taxes | €3,180,480 | €4,771,200 | +€1,590,720 | Corresponding adjustment |
| ETR | 11.20% | 11.20% | — | No change (proportional) |
| SBIE Amount | €5,112,000 | €5,112,000 | — | No change |
| Excess Profit | €23,288,000 | €37,488,000 | +€14,200,000 | Higher income base |
| Top-up Tax % | 3.80% | 3.80% | — | No change |
| **Section 3 - Allocation** |||||
| Irish Top-up Tax | €885,000 | €1,424,544 | +€539,544 | Higher excess profit × 3.8% |
| IIR (UK) | €885,000 | €1,424,544 | +€539,544 | Full increase to UK IIR |
| QDMTT Offset | €0 | €0 | — | No QDMTT claimed |
| **Group Total** |||||
| Total Top-up Tax | €2,315,000 | €2,854,544 | +€539,544 | Irish increase only |

---

## Part 5: Post-Amendment Actions

### 5.1 Process Improvement Implementation

Following the amendment, Phoenix Aerospace implemented the following process improvements:

**Intercompany Transaction Review Enhancement:**

| Control | Previous State | Enhanced State |
|---------|---------------|----------------|
| Royalty identification | Manual review | Automated flag in consolidation system |
| WHT mapping | Spreadsheet-based | Integrated tax data warehouse |
| Elimination reconciliation | Year-end only | Quarterly reconciliation |
| GloBE vs. consolidated accounts | Informal check | Formal sign-off procedure |

**GIR Preparation Checklist Addition:**

New mandatory step added to GIR preparation procedures:

```
Step 14A: Intercompany Income Reconciliation

□ Obtain list of all intercompany income items >€1m from consolidation
□ Verify each item is correctly included in receiving entity's GloBE Income
□ Confirm associated withholding taxes mapped to correct jurisdiction
□ Reconcile GloBE intercompany totals to consolidation eliminations
□ Sign-off by [Senior Tax Manager] required before Section 2 finalisation
```

### 5.2 Authority Communication Log

**Record of Authority Communications:**

| Date | Authority | Method | Subject | Outcome |
|------|-----------|--------|---------|---------|
| 15 Oct 2026 | HMRC | Portal | Amended GIR submission | Confirmation received |
| 15 Oct 2026 | HMRC | CHAPS | Payment £473,711 | Cleared same day |
| 18 Oct 2026 | Irish Revenue | Email | Amendment notification | Acknowledged 20 Oct |
| 22 Oct 2026 | HMRC | Post | Covering letter | Received (tracked) |
| 15 Nov 2026 | HMRC | Email | Penalty decision request | Pending |

### 5.3 External Auditor Briefing

**Briefing Note for External Auditors:**

```
CONFIDENTIAL

To: [External Audit Partner]
From: Group Tax Director
Date: [Date]
Re: GIR Amendment - FY2024

This note informs you of an amendment to Phoenix Aerospace Holdings
plc's GloBE Information Return for fiscal year 2024.

Summary:
- Original GIR filed 15 May 2026 contained an error
- Irish jurisdictional Top-up Tax understated by €539,544
- Amendment filed 15 October 2026
- Payment made including interest

Impact on FY2026 Financial Statements:
- Additional Pillar Two tax expense: £463,050
- Interest expense: £10,661
- No penalty expected (transitional relief claimed)
- Disclosure in tax note regarding amendment

Please contact me to discuss any audit procedures you wish to perform
in relation to this matter.
```

---

## Practical Deliverable: Amendment Filing Checklist

### GIR Amendment Filing Checklist

**Phase 1: Error Identification and Assessment**

| Step | Task | Owner | Date | Sign-off |
|------|------|-------|------|----------|
| 1.1 | Document nature of error identified | Tax Manager | ___ | ___ |
| 1.2 | Quantify impact on jurisdictional calculations | Tax Analyst | ___ | ___ |
| 1.3 | Quantify impact on Top-up Tax allocation | Tax Analyst | ___ | ___ |
| 1.4 | Complete materiality assessment | Tax Manager | ___ | ___ |
| 1.5 | Determine error classification (Cat 1-4) | Tax Director | ___ | ___ |
| 1.6 | Identify all affected jurisdictions | Tax Manager | ___ | ___ |
| 1.7 | Confirm amendment within time limits | Tax Director | ___ | ___ |

**Phase 2: Amendment Preparation**

| Step | Task | Owner | Date | Sign-off |
|------|------|-------|------|----------|
| 2.1 | Prepare corrected calculations | Tax Analyst | ___ | ___ |
| 2.2 | Review corrected calculations | Tax Manager | ___ | ___ |
| 2.3 | Generate amended GIR XML file | Tax Technology | ___ | ___ |
| 2.4 | Validate XML against OECD schema | Tax Technology | ___ | ___ |
| 2.5 | Prepare reconciliation schedule | Tax Analyst | ___ | ___ |
| 2.6 | Draft root cause analysis memo | Tax Manager | ___ | ___ |
| 2.7 | Draft covering letter | Tax Director | ___ | ___ |
| 2.8 | Calculate interest on underpayment | Finance | ___ | ___ |
| 2.9 | Obtain Group Tax Director approval | Tax Director | ___ | ___ |

**Phase 3: Filing and Payment**

| Step | Task | Owner | Date | Sign-off |
|------|------|-------|------|----------|
| 3.1 | Submit amended GIR to primary authority | Tax Manager | ___ | ___ |
| 3.2 | Obtain submission confirmation | Tax Manager | ___ | ___ |
| 3.3 | Make payment (tax + interest) | Finance | ___ | ___ |
| 3.4 | Obtain payment confirmation | Finance | ___ | ___ |
| 3.5 | Send covering letter (if separate) | Tax Manager | ___ | ___ |

**Phase 4: Multi-Jurisdiction Coordination**

| Step | Task | Owner | Date | Sign-off |
|------|------|-------|------|----------|
| 4.1 | Identify notification requirements | Tax Manager | ___ | ___ |
| 4.2 | Notify affected jurisdictions | Tax Manager | ___ | ___ |
| 4.3 | File local amended returns (if required) | Local Tax | ___ | ___ |
| 4.4 | Document all authority communications | Tax Analyst | ___ | ___ |

**Phase 5: Post-Filing Actions**

| Step | Task | Owner | Date | Sign-off |
|------|------|-------|------|----------|
| 5.1 | Update internal GIR records | Tax Analyst | ___ | ___ |
| 5.2 | Brief external auditors | Tax Director | ___ | ___ |
| 5.3 | Complete root cause analysis | Tax Manager | ___ | ___ |
| 5.4 | Implement process improvements | Tax Manager | ___ | ___ |
| 5.5 | Update GIR preparation procedures | Tax Manager | ___ | ___ |
| 5.6 | Archive amendment documentation | Tax Analyst | ___ | ___ |
| 5.7 | Monitor for authority queries | Tax Manager | Ongoing | ___ |

**Phase 6: Penalty Management**

| Step | Task | Owner | Date | Sign-off |
|------|------|-------|------|----------|
| 6.1 | Assess penalty risk | Tax Director | ___ | ___ |
| 6.2 | Compile reasonable excuse evidence | Tax Manager | ___ | ___ |
| 6.3 | Compile transitional relief evidence | Tax Manager | ___ | ___ |
| 6.4 | Respond to penalty assessment (if issued) | Tax Director | ___ | ___ |
| 6.5 | Appeal penalty (if appropriate) | External Advisor | ___ | ___ |

---

## Key Takeaways

1. **Error Discovery**: Robust post-filing internal audit procedures are essential for identifying errors before tax authority discovery

2. **Materiality Assessment**: Apply both quantitative thresholds and qualitative factors when determining whether amendment is required

3. **Transitional Relief**: The OECD transitional penalty relief regime provides significant protection for good-faith errors during initial compliance years

4. **Documentation**: Comprehensive documentation of the error, correction process, and preventive measures is critical for penalty mitigation

5. **Multi-Jurisdiction Coordination**: Amended GIR filing may trigger notification requirements in affected jurisdictions even where no local filing change is required

6. **Process Improvement**: Each error should result in documented process improvements to prevent recurrence

7. **Time Limits**: Amendment windows vary by jurisdiction - prompt action upon error discovery is essential

---

## Section Summary

This scenario demonstrated the complete lifecycle of a GIR amendment:

- **Error identification** through post-filing internal audit
- **Materiality assessment** using quantitative and qualitative criteria
- **Amendment procedures** following UK HMRC requirements
- **Penalty mitigation** under the OECD transitional relief regime
- **Documentation** requirements for amended filings
- **Post-amendment actions** including process improvement

The Phoenix Aerospace scenario illustrates that prompt, well-documented self-disclosure combined with evidence of reasonable compliance efforts provides the strongest foundation for penalty mitigation during the transitional period.

---

## Further Reading and Resources

- [OECD Safe Harbours and Penalty Relief](https://www.oecd.org/content/dam/oecd/en/topics/policy-sub-issues/global-minimum-tax/safe-harbours-and-penalty-relief-global-anti-base-erosion-rules-pillar-two.pdf)
- [HMRC MTT Manual: Taxpayer Amendments](https://www.gov.uk/hmrc-internal-manuals/multinational-top-up-tax-and-domestic-top-up-tax/mtt55140)
- [HMRC MTT Manual: Compliance Time Limits](https://www.gov.uk/hmrc-internal-manuals/multinational-top-up-tax-and-domestic-top-up-tax/mtt55130)
- [UK Pillar 2 Further Amendments Guidance](https://www.gov.uk/government/publications/further-amendments-to-multinational-top-up-tax-and-domestic-top-up-tax/pillar-2-further-amendments-to-multinational-top-up-tax-and-domestic-top-up-tax)
- [OECD GloBE Information Return (January 2025)](https://www.oecd.org/en/publications/tax-challenges-arising-from-the-digitalisation-of-the-economy-globe-information-return-january-2025_a05ec99a-en.html)
- [Transitional Penalty Relief Regime Overview](https://oecdpillars.com/pillar-tab/transitional-penalty-relief-regime/)

---

*End of Section 10.5*
