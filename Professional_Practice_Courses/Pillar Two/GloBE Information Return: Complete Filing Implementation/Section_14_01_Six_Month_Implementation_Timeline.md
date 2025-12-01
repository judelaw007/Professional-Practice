# Section 14.1: 6-Month Implementation Timeline

## Overview

This section provides a detailed month-by-month implementation roadmap for completing your first GloBE Information Return (GIR) filing. The timeline is designed for MNE groups targeting the June 30, 2026 deadline for fiscal years ending December 31, 2024.

**Key Deadline Context:**
- First GIR filing deadline: **June 30, 2026** (18-month extended deadline for first year)
- Subsequent years: 15 months after fiscal year end
- UK registration deadline: **June 30, 2025** (6 months after first accounting period end)
- OECD Administrative Guidance confirms no filing obligations before June 30, 2026

**Timeline Assumptions:**
- Implementation begins January 2026 for June 2026 filing
- MNE group already subject to Pillar Two rules from January 1, 2024
- Group has completed initial Pillar Two impact assessment
- Basic Pillar Two calculation infrastructure in place

---

## Timeline Summary

| Month | Focus Area | Key Deliverables |
|-------|------------|------------------|
| **Month 1** | Scoping and Team Mobilization | Project charter, team assignments, governance structure |
| **Month 2** | Data Inventory and Gap Analysis | Complete data mapping, gap register, remediation plan |
| **Month 3** | System Setup and Data Extraction | Data collection templates, ERP extracts, validation rules |
| **Month 4** | GIR Calculator Population and Validation | Completed Sections 1-3, internal validation |
| **Month 5** | XML Generation and Testing | Valid XML file, jurisdiction portal testing |
| **Month 6** | Filing and Confirmation | Submitted GIR(s), confirmation documentation |

---

## Month 1: Scoping and Team Mobilization

### Week 1-2: Project Initiation

**Objective:** Establish project governance and secure executive sponsorship.

#### Key Activities:

**1.1 Executive Briefing and Sponsorship**
- Brief CFO/Tax Director on GIR requirements and resource needs
- Secure executive sponsor for cross-functional coordination
- Establish escalation pathway for resource conflicts
- Confirm budget allocation for external support (if required)

**1.2 Project Charter Development**
- Define project scope and objectives
- Establish success criteria and key milestones
- Document risks and dependencies
- Secure sign-off from executive sponsor

**Template Reference:** Project Charter Template (Word)

#### Deliverable: Approved Project Charter

---

### Week 2-3: Team Assembly

**Objective:** Build cross-functional implementation team with clear roles.

#### Core Team Structure:

| Role | Responsibilities | Department |
|------|------------------|------------|
| **Project Lead** | Overall coordination, timeline management, executive reporting | Tax |
| **GIR Technical Lead** | GIR completion, XML generation, filing submission | Tax |
| **Data Lead** | Data mapping, extraction, validation | Finance/Tax |
| **ERP/Systems Lead** | System access, data extraction, technical support | IT |
| **Entity Coordinator** | Constituent entity data collection, local coordination | Group Tax |
| **External Advisor** | Technical guidance, quality review (if engaged) | Advisory Firm |

#### Extended Team (As Needed):

| Role | Responsibilities | Engagement |
|------|------------------|------------|
| **Regional Tax Managers** | Local entity data, jurisdiction-specific requirements | Part-time |
| **Financial Controllers** | Entity financial data verification | Part-time |
| **Transfer Pricing Team** | Intra-group transaction data | Part-time |
| **Legal/Company Secretary** | Entity structure documentation, ownership percentages | As needed |

**Critical Success Factor:** Pillar Two involves multiple departments—tax, accounting, finance, legal, and IT. Although Tax may be the anticipated owner, coordination and collaboration across the organization is essential.

#### Deliverable: Team Assignment Matrix with RACI

---

### Week 3-4: Scope Assessment

**Objective:** Confirm GIR scope and identify complexity factors.

#### Key Activities:

**1.3 Constituent Entity Inventory**
- Extract complete list of legal entities from consolidation system
- Confirm entity count for GIR reporting (all constituent entities)
- Identify excluded entities (investment entities, pension funds, etc.)
- Map entity locations to jurisdictions

**1.4 Jurisdictional Scope Assessment**
- List all jurisdictions with constituent entities
- Identify jurisdictions electing safe harbour treatment
- Confirm Qualified IIR jurisdictions
- Identify UTPR exposure jurisdictions

**1.5 Complexity Factor Identification**
- Joint ventures and minority investments
- Flow-through entities
- Recent acquisitions/disposals
- Multi-tiered ownership structures
- Excluded entities requiring documentation

#### Scope Assessment Checklist:

| Item | Completed | Notes |
|------|-----------|-------|
| Total constituent entities counted | ☐ | |
| Jurisdictions with entities listed | ☐ | |
| Excluded entities identified | ☐ | |
| Safe harbour elections documented | ☐ | |
| JVs and minority investments catalogued | ☐ | |
| Recent M&A transactions identified | ☐ | |
| Filing entity determined (UPE or DFE) | ☐ | |

#### Deliverable: GIR Scope Assessment Document

---

### Month 1 Milestones

| Milestone | Target Date | Owner | Status |
|-----------|-------------|-------|--------|
| Project charter approved | Week 1 | Project Lead | ☐ |
| Core team assembled | Week 2 | Project Lead | ☐ |
| Extended team engaged | Week 3 | Project Lead | ☐ |
| Constituent entity inventory complete | Week 3 | Entity Coordinator | ☐ |
| Scope assessment finalized | Week 4 | GIR Technical Lead | ☐ |
| Month 1 status report issued | Week 4 | Project Lead | ☐ |

---

## Month 2: Data Inventory and Gap Analysis

### Week 5-6: Data Point Mapping

**Objective:** Map all ~480 GIR data points to source systems and owners.

#### Key Activities:

**2.1 GIR Data Point Inventory**
Use the GIR Data Point Tracker (provided as course deliverable) to catalogue all required data points:

| GIR Section | Data Points | Focus |
|-------------|-------------|-------|
| Section 1: MNE Group Information | ~50+ | Entity identification, ownership, corporate structure |
| Section 2: Safe Harbours | ~40 | Elections, exclusions, de minimis |
| Section 3: GloBE Computations | ~400+ | ETR calculation, top-up tax by jurisdiction |

**Note:** Data point count expands significantly based on number of jurisdictions and constituent entities.

**2.2 Source System Mapping**
For each data point, identify:
- Source system (ERP, consolidation tool, local accounts, etc.)
- Data owner (responsible person)
- Data format and transformation requirements
- Automation potential vs manual extraction

**Research Finding:** Most companies only maintain about 40-60% of required Pillar Two data in their ERP systems. Expect significant data to reside in other systems or require manual collection.

#### Source System Categories:

| Category | Typical Data | Common Systems |
|----------|--------------|----------------|
| **Financial Accounting** | Net income, revenue, tangible assets | SAP, Oracle, NetSuite |
| **Tax Provision** | Current tax expense, deferred tax | ONESOURCE, Corptax, Longview |
| **Consolidation** | Ownership percentages, eliminations | HFM, BPC, OneStream |
| **HR/Payroll** | Eligible payroll costs by jurisdiction | Workday, ADP, local systems |
| **Fixed Assets** | Tangible asset values, locations | ERP modules, local registers |
| **Entity Database** | Legal names, TINs, addresses | Entity management systems |

**Template Reference:** GIR Data Point Tracker (Excel, ~480 rows)

#### Deliverable: Completed Data Point Mapping

---

### Week 6-7: Gap Analysis

**Objective:** Identify all data gaps and assess impact on GIR completion.

#### Key Activities:

**2.3 Gap Identification**
For each data point, assess:
- Availability: Is data currently captured?
- Accessibility: Can data be extracted?
- Format: Is data in required format?
- Quality: Is data accurate and complete?

**2.4 Gap Categorization**

| Gap Category | Description | Example |
|--------------|-------------|---------|
| **Missing Data** | Data not currently captured | Payroll costs by jurisdiction |
| **Inaccessible Data** | Data exists but cannot be extracted | Legacy system limitations |
| **Format Issues** | Data requires transformation | Currency conversion needs |
| **Quality Issues** | Data incomplete or inaccurate | Missing TINs for entities |
| **Timing Issues** | Data not available when needed | Post year-end adjustments |

**2.5 Impact Assessment**
Prioritize gaps based on:
- Filing requirement criticality (mandatory vs optional)
- Materiality to ETR calculation
- Remediation complexity and time required

#### Gap Analysis Summary Template:

| Gap ID | Data Point | Gap Type | Impact | Remediation | Owner | Target Date |
|--------|------------|----------|--------|-------------|-------|-------------|
| G001 | Payroll by jurisdiction | Missing | High | New data collection | HR Lead | Month 3 |
| G002 | Entity TINs | Quality | Medium | Research and update | Entity Coord | Month 2 |
| G003 | Asset locations | Format | Medium | Mapping exercise | FA Team | Month 3 |

#### Deliverable: Data Gap Register

---

### Week 7-8: Remediation Planning

**Objective:** Develop action plans to close all critical data gaps.

#### Key Activities:

**2.6 Remediation Strategy Development**
For each gap, determine:
- Short-term workaround (for this filing)
- Long-term solution (for subsequent years)
- Resource requirements
- Dependencies and risks

**2.7 Estimation Approach Documentation**
Where data is unavailable, document:
- Estimation methodology (must be reasonable and defensible)
- Supporting calculations and assumptions
- Basis in OECD guidance where applicable

**OECD Guidance Note:** Transitional simplified jurisdictional reporting is available for fiscal years beginning on or before December 31, 2028, allowing reporting on jurisdictional rather than constituent entity basis where certain conditions met.

**2.8 Data Request Process Initiation**
- Issue data request memos to internal stakeholders
- Set clear deadlines aligned with Month 3 extraction target
- Establish escalation for non-response

**Template Reference:** Data Request Memo Template (Word)

#### Deliverable: Data Remediation Action Plan

---

### Month 2 Milestones

| Milestone | Target Date | Owner | Status |
|-----------|-------------|-------|--------|
| Data point mapping 50% complete | Week 5 | Data Lead | ☐ |
| Data point mapping 100% complete | Week 6 | Data Lead | ☐ |
| Gap analysis completed | Week 7 | Data Lead | ☐ |
| Gap register finalized | Week 7 | Data Lead | ☐ |
| Remediation plans approved | Week 8 | Project Lead | ☐ |
| Data requests issued | Week 8 | Entity Coordinator | ☐ |
| Month 2 status report issued | Week 8 | Project Lead | ☐ |

---

## Month 3: System Setup and Data Extraction

### Week 9-10: Infrastructure Preparation

**Objective:** Establish technical infrastructure for GIR data collection and processing.

#### Key Activities:

**3.1 GIR Calculator Setup**
- Configure GIR Completion Calculator (Excel tool from course)
- Set up entity master data
- Configure jurisdictional parameters
- Test validation rules with sample data

**3.2 Data Collection Templates**
- Customize templates for constituent entity data requests
- Establish secure data transfer mechanisms
- Set up central data repository (SharePoint, shared drive, etc.)
- Configure access controls and audit trail

**3.3 ERP Report Development**
- Work with IT to build required extraction reports
- Test extraction queries against live data
- Validate data completeness and accuracy
- Document extraction procedures

#### ERP Extraction Checklist:

| Data Type | Source System | Report Ready | Extraction Tested |
|-----------|---------------|--------------|-------------------|
| Trial balance by entity | ERP | ☐ | ☐ |
| Revenue by jurisdiction | ERP | ☐ | ☐ |
| Tangible assets by location | Fixed Assets | ☐ | ☐ |
| Payroll by jurisdiction | HR/Payroll | ☐ | ☐ |
| Tax provision data | Tax system | ☐ | ☐ |
| Intercompany transactions | ERP/Consolidation | ☐ | ☐ |
| Ownership percentages | Consolidation | ☐ | ☐ |

#### Deliverable: Configured GIR Calculator and Data Templates

---

### Week 10-12: Data Extraction and Collection

**Objective:** Extract and collect all data required for GIR completion.

#### Key Activities:

**3.4 Centralized Data Extraction**
- Run ERP extraction reports for all entities
- Extract consolidation data (ownership, eliminations)
- Pull tax provision data for covered taxes
- Export HR/payroll data for SBIE calculations

**3.5 Decentralized Data Collection**
- Collect local entity data via templates
- Chase responses from non-responsive entities
- Escalate collection issues through regional managers
- Document workarounds for unavailable data

**3.6 Data Validation**
- Cross-check extracted data against source systems
- Reconcile entity-level data to consolidated figures
- Identify and resolve discrepancies
- Document validation results

#### Data Quality Checkpoints:

| Check | Description | Pass/Fail |
|-------|-------------|-----------|
| Entity count matches | CE count equals consolidation entity count | ☐ |
| Revenue reconciliation | Sum of entity revenue reconciles to consolidated | ☐ |
| Currency consistency | All amounts in reporting currency | ☐ |
| TIN completeness | All entities have TIN or "NOTIN" documented | ☐ |
| Ownership chain | All ownership percentages sum correctly | ☐ |
| Covered taxes | Tax expense reconciles to provision | ☐ |

**Template Reference:** Data Quality Checklist (50+ checkpoints)

#### Deliverable: Complete Validated Data Set

---

### Month 3 Milestones

| Milestone | Target Date | Owner | Status |
|-----------|-------------|-------|--------|
| GIR Calculator configured | Week 9 | GIR Technical Lead | ☐ |
| Data collection templates distributed | Week 9 | Entity Coordinator | ☐ |
| ERP extractions complete | Week 10 | ERP/Systems Lead | ☐ |
| Entity data 75% collected | Week 11 | Entity Coordinator | ☐ |
| Entity data 100% collected | Week 12 | Entity Coordinator | ☐ |
| Data validation completed | Week 12 | Data Lead | ☐ |
| Month 3 status report issued | Week 12 | Project Lead | ☐ |

---

## Month 4: GIR Calculator Population and Validation

### Week 13-14: Section 1 Completion

**Objective:** Complete GIR Section 1 - MNE Group Information.

#### Key Activities:

**4.1 Filing Constituent Entity Data**
- Enter Filing CE identification details
- Input UPE information (name, TIN, jurisdiction)
- Record general accounting information
- Confirm financial accounting standard used

**4.2 Corporate Structure Data Entry**
For each constituent entity, enter:
- Legal name and TIN
- Jurisdiction location (ISO country code)
- GloBE status (constituent entity, excluded entity, etc.)
- Ownership percentage
- QIIR applicability indicator
- UTPR applicability indicator

**4.3 Summary Information**
- Complete high-level group metrics
- Populate ETR range by jurisdiction summary
- Generate Section 1 validation report

#### Section 1 Completion Checklist:

| Element | Data Points | Completed | Validated |
|---------|-------------|-----------|-----------|
| Filing CE identification | ~10 | ☐ | ☐ |
| UPE information | ~10 | ☐ | ☐ |
| Constituent entity list | ~15 per entity | ☐ | ☐ |
| Ownership structure | ~5 per entity | ☐ | ☐ |
| Summary information | ~10 | ☐ | ☐ |

#### Deliverable: Completed GIR Section 1

---

### Week 14-15: Section 2 Completion

**Objective:** Complete GIR Section 2 - Safe Harbours and Exclusions.

#### Key Activities:

**4.4 Safe Harbour Elections**
Document elections for each jurisdiction:
- Transitional CbCR Safe Harbour (if applicable)
- Transitional UTPR Safe Harbour
- QDMTT Safe Harbour (where qualified)

**Safe Harbour Rate Thresholds (Transitional CbCR):**

| Fiscal Year | Simplified ETR Threshold |
|-------------|-------------------------|
| 2023-2024 | 15% |
| 2025 | 16% |
| 2026 | 17% |

**4.5 Exclusions Documentation**
- Record de minimis exclusion elections
- Document initial phase of international activity exclusions
- Justify basis for each exclusion

**4.6 Section 2 Validation**
- Verify all elections are consistent with calculations
- Confirm documentation supports each election
- Generate Section 2 validation report

#### Deliverable: Completed GIR Section 2

---

### Week 15-16: Section 3 Completion

**Objective:** Complete GIR Section 3 - GloBE Computations.

#### Key Activities:

**4.7 ETR Computation Data Entry**
For each jurisdiction:
- GloBE Income/Loss calculation
- Covered Taxes allocation
- Adjusted Covered Taxes
- ETR calculation

**4.8 Substance-Based Income Exclusion**
- Enter payroll carve-out data by jurisdiction
- Enter tangible asset carve-out data
- Calculate SBIE amounts
- Apply phase-in rates (5% payroll / 5% tangible assets for 2024)

**SBIE Phase-In Schedule (2024):**

| Component | Rate |
|-----------|------|
| Payroll carve-out | 5.0% |
| Tangible asset carve-out | 5.0% |

**4.9 Top-Up Tax Computation**
- Calculate excess profit by jurisdiction
- Apply top-up tax percentage
- Compute top-up tax amounts
- Allocate IIR, UTPR, and QDMTT amounts

**4.10 Section 3 Validation**
- Reconcile to independent Pillar Two calculations
- Verify mathematical accuracy
- Cross-check jurisdiction totals
- Generate comprehensive validation report

#### Section 3 Validation Checks:

| Check | Description | Result |
|-------|-------------|--------|
| ETR reasonableness | ETRs within expected ranges | ☐ |
| Top-up tax reconciliation | Matches external calculation | ☐ |
| SBIE calculation | Carve-outs correctly applied | ☐ |
| Allocation accuracy | IIR/UTPR/QDMTT properly allocated | ☐ |
| Currency consistency | All in EUR or reporting currency | ☐ |

**Template Reference:** GIR-to-Tax Calculation Reconciliation Tool (Excel)

#### Deliverable: Completed GIR Section 3

---

### Month 4 Milestones

| Milestone | Target Date | Owner | Status |
|-----------|-------------|-------|--------|
| Section 1 data entry complete | Week 14 | GIR Technical Lead | ☐ |
| Section 1 validated | Week 14 | Data Lead | ☐ |
| Section 2 data entry complete | Week 15 | GIR Technical Lead | ☐ |
| Section 2 validated | Week 15 | Data Lead | ☐ |
| Section 3 data entry complete | Week 16 | GIR Technical Lead | ☐ |
| Section 3 validated | Week 16 | Data Lead | ☐ |
| Full GIR internal review | Week 16 | External Advisor | ☐ |
| Month 4 status report issued | Week 16 | Project Lead | ☐ |

---

## Month 5: XML Generation and Testing

### Week 17-18: XML File Generation

**Objective:** Generate valid XML file(s) meeting OECD January 2025 schema.

#### Key Activities:

**5.1 Pre-Generation Validation**
- Run final validation on all GIR sections
- Resolve any outstanding data issues
- Confirm all mandatory fields populated
- Verify character encoding requirements

**5.2 XML Generation**
- Export GIR data to XML format using Calculator tool
- Verify file structure against OECD schema
- Check element hierarchy and attribute requirements
- Confirm correct file naming convention

**XML File Requirements:**
- Schema version: January 2025 OECD GIR XML Schema
- Encoding: UTF-8
- File extension: .xml
- Naming convention: Per jurisdiction-specific requirements

**5.3 Schema Validation**
- Validate XML against OECD XSD schema
- Use multiple validation tools for cross-checking
- Document all validation errors
- Resolve schema compliance issues

**Template Reference:** XML Validation Checklist (25 checkpoints)

#### Deliverable: Schema-Validated XML File

---

### Week 18-20: Portal Testing

**Objective:** Test submission process in jurisdiction portal(s).

#### Key Activities:

**5.4 Portal Access Verification**
- Confirm login credentials for all required portals
- Verify user permissions for GIR submission
- Test connectivity and technical requirements
- Document portal navigation steps

**5.5 Test Environment Submissions (Where Available)**
- UK HMRC: Use test environment for validation
- Other jurisdictions: Check for sandbox availability
- Upload XML file to test environment
- Review validation feedback
- Resolve any portal-specific errors

**5.6 File Compatibility Testing**
- Verify file size within portal limits
- Confirm character encoding accepted
- Test upload speed and timeout handling
- Document any technical issues

#### Portal Testing Checklist:

| Jurisdiction | Portal Access | Test Upload | Validation Passed |
|--------------|---------------|-------------|-------------------|
| UK (HMRC) | ☐ | ☐ | ☐ |
| [Jurisdiction 2] | ☐ | ☐ | ☐ |
| [Jurisdiction 3] | ☐ | ☐ | ☐ |
| [Add as needed] | ☐ | ☐ | ☐ |

#### Deliverable: Portal-Ready XML File(s)

---

### Week 20: Final Review

**Objective:** Complete final quality assurance before filing.

#### Key Activities:

**5.7 Senior Review**
- Tax Director/VP Tax review of all GIR content
- Reconciliation to Pillar Two tax calculations confirmed
- Comparison to CbCR data where applicable
- Sign-off on accuracy and completeness

**5.8 External Advisor Review (If Engaged)**
- Technical review of GloBE calculations
- XML schema compliance confirmation
- Jurisdiction-specific requirement check
- Independent validation documentation

**5.9 Pre-Filing Checklist Completion**
Run through comprehensive pre-filing checklist:

| Category | Items | Completed |
|----------|-------|-----------|
| Data completeness | All mandatory fields populated | ☐ |
| Calculation accuracy | ETR and top-up tax verified | ☐ |
| Elections documented | All safe harbour elections recorded | ☐ |
| XML validity | Schema validation passed | ☐ |
| Portal readiness | Access confirmed, file tested | ☐ |
| Approvals obtained | Senior management sign-off | ☐ |

**Template Reference:** Pre-Filing Data Verification Checklist (50+ items)

#### Deliverable: Approved Final GIR Package

---

### Month 5 Milestones

| Milestone | Target Date | Owner | Status |
|-----------|-------------|-------|--------|
| XML file generated | Week 17 | GIR Technical Lead | ☐ |
| Schema validation passed | Week 18 | GIR Technical Lead | ☐ |
| Portal access confirmed | Week 18 | GIR Technical Lead | ☐ |
| Test submissions completed | Week 19 | GIR Technical Lead | ☐ |
| Senior review completed | Week 20 | Tax Director | ☐ |
| External review completed | Week 20 | External Advisor | ☐ |
| Pre-filing checklist signed | Week 20 | Project Lead | ☐ |
| Month 5 status report issued | Week 20 | Project Lead | ☐ |

---

## Month 6: Filing and Confirmation

### Week 21-22: GIR Submission

**Objective:** Submit GIR to all required jurisdictions.

#### Key Activities:

**6.1 Filing Sequence Planning**
Determine optimal filing order:
- DFE jurisdiction first (if applicable)
- Then other required jurisdictions
- Allow time between submissions for issue resolution

**6.2 Primary Jurisdiction Filing**
- Upload XML file to primary jurisdiction portal
- Complete any portal-specific additional forms
- Submit GIR
- Capture submission confirmation/receipt

**6.3 Secondary Jurisdiction Filings**
- File in additional jurisdictions as required
- Submit Overseas Return Notification (ORN) where applicable (UK requirement if GIR filed elsewhere)
- Complete local notifications as required
- Document all submission confirmations

**Filing Documentation Requirements:**

| Item | Captured | Stored |
|------|----------|--------|
| Submission timestamp | ☐ | ☐ |
| Confirmation number/receipt | ☐ | ☐ |
| XML file copy (as submitted) | ☐ | ☐ |
| Screenshot of submission confirmation | ☐ | ☐ |
| Portal transaction log | ☐ | ☐ |

**Template Reference:** GIR Filing Confirmation Record Template (Word)

#### Deliverable: Submitted GIR(s) with Confirmation

---

### Week 22-23: Post-Filing Verification

**Objective:** Verify successful filing and address any issues.

#### Key Activities:

**6.4 Submission Confirmation**
- Verify GIR accepted by each portal
- Check for any rejection notifications
- Monitor email for tax authority communications
- Document filing status for all jurisdictions

**6.5 Issue Resolution (If Required)**
- Address any rejection reasons promptly
- Correct errors and resubmit if needed
- Document correction process
- Update internal records

**6.6 Stakeholder Notification**
- Notify executive sponsor of successful filing
- Update Audit Committee (if required)
- Brief external auditors
- Document in group tax compliance records

#### Post-Filing Verification Checklist:

| Jurisdiction | Submitted | Accepted | Confirmation Stored |
|--------------|-----------|----------|---------------------|
| [Primary] | ☐ | ☐ | ☐ |
| [Secondary 1] | ☐ | ☐ | ☐ |
| [Secondary 2] | ☐ | ☐ | ☐ |
| UK (ORN if applicable) | ☐ | ☐ | ☐ |

**Template Reference:** Post-Filing Confirmation Checklist

#### Deliverable: Filing Confirmation Documentation

---

### Week 23-24: Documentation and Close-Out

**Objective:** Complete project documentation and lessons learned.

#### Key Activities:

**6.7 Audit File Assembly**
Compile complete GIR audit file including:
- Final XML file (as submitted)
- All supporting calculations
- Data source documentation
- Validation reports
- Approval documentation
- Submission confirmations
- Correspondence with tax authorities

**6.8 Lessons Learned Session**
- Conduct team debrief meeting
- Document what worked well
- Identify improvement opportunities
- Capture recommendations for Year 2

**6.9 Year 2 Planning Initiation**
- Document data gaps requiring long-term solutions
- Identify system enhancements needed
- Estimate Year 2 resource requirements
- Update implementation timeline for 15-month cycle

#### Project Close-Out Deliverables:

| Deliverable | Owner | Completed |
|-------------|-------|-----------|
| Complete audit file | GIR Technical Lead | ☐ |
| Lessons learned document | Project Lead | ☐ |
| Year 2 planning memo | Project Lead | ☐ |
| Project close-out report | Project Lead | ☐ |
| Team recognition | Executive Sponsor | ☐ |

**Template Reference:** GIR Audit File Index Template (Word)

#### Deliverable: Complete Project Documentation

---

### Month 6 Milestones

| Milestone | Target Date | Owner | Status |
|-----------|-------------|-------|--------|
| Primary GIR filed | Week 21 | GIR Technical Lead | ☐ |
| All GIRs filed | Week 22 | GIR Technical Lead | ☐ |
| Filing acceptance confirmed | Week 22 | GIR Technical Lead | ☐ |
| Stakeholders notified | Week 23 | Project Lead | ☐ |
| Audit file assembled | Week 23 | GIR Technical Lead | ☐ |
| Lessons learned completed | Week 24 | Project Lead | ☐ |
| Project close-out report issued | Week 24 | Project Lead | ☐ |

---

## Implementation Gantt Chart Overview

```
Month 1: Scoping and Team Mobilization
├── Week 1-2: Project initiation and executive briefing
├── Week 2-3: Team assembly and role assignment
└── Week 3-4: Scope assessment and CE inventory

Month 2: Data Inventory and Gap Analysis
├── Week 5-6: Data point mapping (~480 points)
├── Week 6-7: Gap analysis and categorization
└── Week 7-8: Remediation planning and data requests

Month 3: System Setup and Data Extraction
├── Week 9-10: Infrastructure and calculator setup
├── Week 10-11: ERP extraction and local data collection
└── Week 11-12: Data validation and reconciliation

Month 4: Calculator Population and Validation
├── Week 13-14: Section 1 completion (MNE Group Info)
├── Week 14-15: Section 2 completion (Safe Harbours)
└── Week 15-16: Section 3 completion (GloBE Computations)

Month 5: XML Generation and Testing
├── Week 17-18: XML generation and schema validation
├── Week 18-20: Portal testing and trial submissions
└── Week 20: Final review and pre-filing checklist

Month 6: Filing and Confirmation
├── Week 21-22: GIR submission to all jurisdictions
├── Week 22-23: Post-filing verification and issue resolution
└── Week 23-24: Documentation, lessons learned, Year 2 planning
```

**Deliverable Reference:** Implementation Gantt Chart Template (Excel) - available in Appendix A

---

## Resource Requirements by Month

### Time Allocation Estimates

| Role | Month 1 | Month 2 | Month 3 | Month 4 | Month 5 | Month 6 |
|------|---------|---------|---------|---------|---------|---------|
| Project Lead | 40% | 30% | 30% | 30% | 40% | 30% |
| GIR Technical Lead | 20% | 40% | 60% | 80% | 80% | 60% |
| Data Lead | 20% | 60% | 60% | 40% | 20% | 10% |
| ERP/Systems Lead | 10% | 20% | 40% | 20% | 10% | 5% |
| Entity Coordinator | 30% | 50% | 60% | 30% | 10% | 10% |
| External Advisor | 10% | 10% | 10% | 20% | 30% | 10% |

### Peak Resource Periods

- **Month 3:** Data extraction and collection peak
- **Month 4:** Calculator completion intensive period
- **Month 5:** XML generation and testing focus

---

## Critical Path Activities

The following activities are on the critical path and must be completed on schedule to meet the filing deadline:

| Activity | Dependency | Float |
|----------|------------|-------|
| Team assembly | Project approval | 1 week |
| Data point mapping | Team assembly | 0 days |
| Gap remediation | Gap analysis | 0 days |
| ERP extraction | Infrastructure setup | 0 days |
| Section 3 completion | Sections 1-2 complete | 0 days |
| XML validation | Section 3 complete | 0 days |
| Portal submission | XML validation passed | 0 days |

**Warning:** Any delay in critical path activities directly impacts the filing deadline.

---

## Risk Register

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| Data gaps larger than expected | High | High | Early gap assessment, estimation approach documented |
| Entity data collection delays | Medium | High | Regional escalation, deadline enforcement |
| ERP extraction issues | Medium | Medium | IT engagement early, backup manual extraction |
| Staff resource conflicts | Medium | Medium | Executive sponsor escalation pathway |
| Portal technical issues | Low | High | Early testing, multiple submission attempts planned |
| Late regulatory changes | Low | Medium | Monitor OECD guidance, build flexibility into timeline |

---

## Summary

This 6-month implementation timeline provides a structured approach to completing your first GIR filing by the June 30, 2026 deadline. Key success factors:

1. **Start Early:** The 18-month first-year deadline provides buffer, but data challenges often require full 6 months
2. **Cross-Functional Coordination:** Pillar Two requires tax, finance, IT, and local teams working together
3. **Data Focus:** Most implementation effort is data collection and validation
4. **Quality over Speed:** Transitional penalty relief available, but quality filing is priority
5. **Document Everything:** Build audit file from day one for defence in future enquiries

**Transitional Relief Reminder:** Per OECD guidance (Annex C), jurisdictions are expected to give "careful consideration" before applying penalties where businesses have taken reasonable measures to apply rules correctly. This relief applies for fiscal years beginning on or before December 31, 2026.

**Next Steps:** Proceed to Section 14.2 (Resource Requirements) for detailed team composition and external advisor engagement guidance.

---

*Section 14.1 Complete - Last Updated: November 2025*
*Next Section: Section 14.2 - Resource Requirements*
