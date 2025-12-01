# Section 8.3: Election Documentation

## Learning Objectives

By the end of this section, you will be able to:

- Prepare DFE election documentation for major filing jurisdictions
- Identify supporting documentation requirements for valid elections
- Manage election filing deadlines across multiple jurisdictions
- Maintain election records for audit defence purposes
- Complete the DFE Election Template Package for client engagements

---

## 8.3.1 Overview of DFE Election Process

### The Election Framework

Designating a Filing Entity (DFE) requires formal notification to relevant tax authorities. Unlike many tax elections that are made on returns, DFE elections typically require:

1. **Advance notification** - Before or concurrent with the first GIR filing
2. **Explicit acceptance** - Some jurisdictions confirm elections; others operate on deemed acceptance
3. **Group-wide coordination** - All affected entities must be covered by the election
4. **Supporting documentation** - Proof of eligibility and authority to file

### Election vs. Notification Distinction

Different jurisdictions use different terminology:

| Term | Meaning | Common Usage |
|------|---------|--------------|
| **DFE Election** | Formal choice to designate an entity | OECD terminology |
| **DFE Notification** | Informing authorities of DFE designation | EU jurisdictions |
| **Local Filing Entity Appointment** | Designating in-jurisdiction filer | UK, Australia |
| **Nominated Filing Entity** | Alternative terminology | Some jurisdictions |

**Key Point:** Regardless of terminology, the substantive requirements are similar—formal documentation identifying the DFE and the scope of its filing responsibility.

---

## 8.3.2 Election Form Requirements by Jurisdiction

### OECD Model Approach

The OECD GIR MCAA contemplates DFE arrangements but does not prescribe specific forms. Instead, the January 2025 XML Schema includes:

- **FilingEntityRole** element to identify DFE status
- **ConstituentEntityReference** elements linking filed entities
- **AuthorisationDetails** for supporting authority documentation

Each implementing jurisdiction has developed its own election procedures within this framework.

### United Kingdom: HMRC DFE Registration

**Governing Framework:** Finance (No. 2) Act 2023, Schedule 14; The Multinational Top-up Tax (Pillar Two) Regulations 2024

**Election Process:**

1. **Register for Multinational Top-up Tax** via HMRC's online services
2. **Submit DFE Notification** through the MTT registration portal
3. **Receive confirmation** with DFE reference number

**Required Form Elements:**

```
UK DFE NOTIFICATION REQUIREMENTS
================================

Part A: Filing Entity Details
- Legal name and registered address
- Company Registration Number (CRN)
- UTR (Unique Taxpayer Reference)
- Contact details for MTT correspondence

Part B: UPE and Group Information
- Ultimate Parent Entity name and jurisdiction
- Group fiscal year end date
- Total consolidated group revenue (EUR)
- Number of constituent entities in group

Part C: DFE Scope Declaration
- Jurisdictions covered by DFE filing
- List of UK constituent entities
- Declaration of authority to file

Part D: Authorisation
- Director/authorised signatory details
- Declaration of accuracy
- Electronic signature
```

**Supporting Documents Required:**

1. Board resolution or Power of Attorney authorising DFE role
2. Group structure chart showing relationship to UPE
3. Evidence of meeting €750 million revenue threshold
4. List of all UK constituent entities with CRNs

**Filing Deadline:** Within 6 months of the end of the first fiscal year in scope (i.e., 30 June 2025 for December 2024 year-ends)

**Confirmation:** HMRC issues DFE registration acknowledgment within 15 working days

---

### European Union: National Variations

#### Germany (BZSt)

**Governing Framework:** Mindeststeuergesetz (MinStG) §§ 77-79

**Election Process:**

1. **Group Head Notification** (Meldung als Gruppenspitze) - prerequisite
2. **DFE Declaration** (Erklärung zur beauftragten Stelle) via BOP portal
3. **ELSTER submission** with qualified electronic signature

**Form Requirements (Formular MiSt-BFE):**

| Field | Description | Format |
|-------|-------------|--------|
| Gruppenspitze-ID | Group head reference number | BZSt-assigned |
| DFE Identifikation | DFE entity details | Name, address, Steuernummer |
| Zuständige Behörde | Filing jurisdiction authority | BZSt/competent authority |
| Umfang der Beauftragung | Scope of DFE appointment | Jurisdiction list |
| Bevollmächtigung | Authorisation details | POA reference |

**Supporting Documents:**

1. **Vollmacht** (Power of Attorney) - notarised for non-German DFE
2. **Konzernstrukturübersicht** (Group structure overview)
3. **Umsatznachweis** (Revenue evidence) - consolidated financial statements

**Deadline:** Concurrent with first GIR filing or earlier notification

---

#### Netherlands (Belastingdienst)

**Governing Framework:** Wet minimumbelasting 2024, Article 8.4

**Election Process:**

1. Access via **Mijn Belastingdienst Zakelijk** with eHerkenning Level 3
2. Submit **DFE melding** (DFE notification)
3. Receive **Bevestiging DFE-status** (DFE status confirmation)

**Required Information:**

```
DUTCH DFE NOTIFICATION (DFE Melding)
====================================

Section 1: Aanmeldende Entiteit (Notifying Entity)
- Naam (Name)
- RSIN/KvK-nummer (Chamber of Commerce number)
- Adres (Address)
- Contactpersoon (Contact person)

Section 2: Groepsinformatie (Group Information)
- Uiteindelijke moederentiteit (Ultimate Parent Entity)
- Vestigingsland UME (UPE jurisdiction)
- Boekjaar (Fiscal year)
- Geconsolideerde omzet (Consolidated revenue)

Section 3: Reikwijdte DFE (DFE Scope)
- Jurisdicties waarvoor wordt ingediend (Filing jurisdictions)
- Nederlandse groepsentiteiten (Dutch constituent entities)

Section 4: Machtiging (Authorisation)
- Bestuurdersverklaring (Director declaration)
- Datum en ondertekening (Date and signature)
```

**Key Documents:**

1. **Machtiging** - Written authorisation from UPE
2. **Organigram** - Group structure diagram
3. **Jaarrekening** - Annual accounts evidencing revenue threshold

**Deadline:** Before first GIR submission (no fixed advance period)

---

#### France (DGFiP)

**Governing Framework:** Article 223 WZ bis CGI; BOI-IS-MIN-40

**Election Process:**

1. Notification via **Compte Fiscal Professionnel** (impots.gouv.fr)
2. Submit **Formulaire 2913-SD** (DFE declaration)
3. Confirmation issued electronically

**Form 2913-SD Structure:**

| Section | Content |
|---------|---------|
| I | Identification of declaring entity (SIREN, address) |
| II | UPE identification and jurisdiction |
| III | Group composition in France |
| IV | DFE scope (jurisdictions covered) |
| V | Representative details and authorisation |
| VI | Declaration and signature |

**Required Annexes:**

- Annex A: List of French constituent entities with SIREN numbers
- Annex B: Group organisation chart
- Annex C: Authorisation documentation (procuration)

---

### Singapore (IRAS)

**Governing Framework:** MNE (Minimum Tax) Act 2024, Section 78

**Election Process:**

1. **MTT Registration** via myTax Portal (Corppass authentication)
2. **GFE/DFE Appointment** form submission
3. **Acknowledgment** issued with GFE/DFE reference

**Singapore DFE Appointment Form:**

```
IRAS DFE APPOINTMENT NOTIFICATION
=================================

Part 1: Appointed Entity Information
- Entity name
- UEN (Unique Entity Number)
- Contact details
- Authorised representative

Part 2: MNE Group Details
- UPE name and tax residence
- Group fiscal year end
- Consolidated revenue (SGD and EUR equivalent)

Part 3: Appointment Scope
- Role: GFE (Group Filing Entity) / DFE
- Jurisdictions within scope
- Singapore constituent entities covered

Part 4: Supporting Documents
- Board resolution/POA
- Group structure chart
- Revenue certification

Part 5: Declaration
- Director/Company Secretary certification
- Date and signature
```

**Key Requirements:**

1. Corppass authorisation at "Approver" level
2. Board resolution specifically authorising DFE role
3. Must be submitted **before** first GIR filing

**Deadline:** 30 September of the year following the first in-scope fiscal year (30 September 2025 for FY2024)

---

### Australia (ATO)

**Governing Framework:** Taxation (Multinational—Global and Domestic Minimum Tax) Act 2024, Division 140

**Election Process:**

1. Access **ATO Online Services** via myGovID (Standard identity strength)
2. Submit **Designated Filing Entity notification**
3. Receive **DFE notification acknowledgment**

**Notification Requirements:**

| Element | Detail |
|---------|--------|
| **CE ABN** | Australian Business Numbers for all covered entities |
| **UPE Details** | Name, jurisdiction, TIN where available |
| **Group Revenue** | Consolidated revenue in AUD and EUR |
| **DFE Role** | Scope of filing responsibility |
| **Authorisation** | Public officer or authorised contact |

**Supporting Documentation:**

1. Director/officer authorisation (letter or board minutes)
2. Group structure showing Australian entities
3. CbCR (if previously lodged) confirming group composition

**Deadline:** Aligned with GIR lodgment deadline (15/18 months post fiscal year-end)

---

### United States Considerations

**Current Status:** The US has not implemented Pillar Two domestic legislation (as of 2025).

**Implications for DFE Elections:**

- US-parented MNE groups **must** designate a DFE in a participating jurisdiction
- The DFE cannot be a US entity
- Elections must be made in the DFE's jurisdiction of tax residence

**Common DFE Locations for US Groups:**

| Jurisdiction | Advantages | Considerations |
|--------------|------------|----------------|
| **UK** | Major operations, English language | HMRC registration required |
| **Netherlands** | Holding company location, EU access | eHerkenning requirement |
| **Ireland** | HQ for many US tech/pharma | Revenue registration |
| **Singapore** | APAC operations hub | Corppass requirement |
| **Luxembourg** | Finance/holding structures | ACD portal access |

---

## 8.3.3 Supporting Documentation Requirements

### Core Documentation Package

Every DFE election requires a consistent set of supporting documents. The following represents best practice documentation:

#### 1. Authorisation Documentation

**Purpose:** Evidence that the DFE has authority to file on behalf of all covered entities

**Acceptable Forms:**

| Document Type | Description | When Required |
|---------------|-------------|---------------|
| **Board Resolution** | Formal approval from DFE board | All elections |
| **Power of Attorney** | Written authority from UPE | Cross-border DFE |
| **Group Treasury Mandate** | Internal authorisation document | Large groups |
| **Intercompany Agreement** | Formal agreement between UPE and DFE | Best practice |

**Board Resolution Template:**

```
BOARD RESOLUTION - DESIGNATED FILING ENTITY APPOINTMENT
========================================================

Company: [DFE Legal Name]
Meeting Date: [Date]
Resolution Number: [Reference]

WHEREAS [UPE Name] is the Ultimate Parent Entity of an MNE group
subject to the GloBE Rules under the OECD Pillar Two framework;

WHEREAS the group has determined that [DFE Name] shall serve as the
Designated Filing Entity for GloBE Information Return filings;

IT IS HEREBY RESOLVED:

1. [DFE Name] is appointed as the Designated Filing Entity for the
   [UPE Name] MNE Group effective for fiscal years beginning on or
   after [Date].

2. The DFE shall file GloBE Information Returns on behalf of
   Constituent Entities in the following jurisdictions: [List].

3. [Named Individual/Position] is authorised to execute all documents
   and filings necessary to fulfil the DFE's obligations.

4. The Board authorises the allocation of appropriate resources and
   systems to fulfil DFE responsibilities.

Approved by: _______________________
             [Director Name/Title]

Date: _______________________
```

#### 2. Group Structure Documentation

**Purpose:** Demonstrate the relationship between DFE, UPE, and all covered entities

**Required Elements:**

- Legal entity names and jurisdictions of incorporation
- Ownership percentages (showing >50% consolidation threshold)
- Tax residence of each entity
- Entity classification (CE, PE, JV, excluded entity)

**Format Options:**

1. **Organisation chart** - Visual representation
2. **Entity listing** - Spreadsheet with all required fields
3. **Legal structure diagram** - From existing corporate records

#### 3. Revenue Threshold Evidence

**Purpose:** Confirm the group meets the €750 million consolidated revenue threshold

**Acceptable Documentation:**

| Source | Description | Preference |
|--------|-------------|------------|
| **Audited Financials** | Consolidated financial statements | Preferred |
| **CbCR Data** | Country-by-Country Report revenue | Acceptable |
| **Management Accounts** | Internal consolidation | Last resort |

**Key Points:**

- Must show revenue for **at least two** of the four preceding fiscal years
- Currency conversion using average exchange rate for the fiscal year
- Revenue measured under applicable accounting standards (IFRS/local GAAP)

#### 4. Entity Coverage Listing

**Purpose:** Identify all Constituent Entities covered by the DFE filing

**Required Fields per Entity:**

| Field | Description |
|-------|-------------|
| Legal Name | Full registered name |
| Jurisdiction | Country of incorporation |
| Tax Residence | Country of tax residence (may differ) |
| TIN | Local tax identification number |
| Entity Type | Operating, holding, finance, etc. |
| Covered by DFE | Yes/No |

---

## 8.3.4 Filing Deadlines for Elections

### Standard Timeline Framework

DFE elections must be made within specific timeframes to be effective for a given fiscal year:

```
ELECTION TIMING FRAMEWORK
=========================

Fiscal Year End ──┬── Election Window Opens
                  │   (varies by jurisdiction)
                  │
                  ├── Some jurisdictions: No advance requirement
                  │
                  ├── Other jurisdictions: Election required
                  │   before first GIR filing
                  │
                  ├── +15 months: Standard GIR deadline
                  │   (election must be in place)
                  │
                  └── +18 months: Transitional first-year deadline
                      (election still must be in place)
```

### Jurisdiction-Specific Election Deadlines

| Jurisdiction | Election Deadline | Relative To |
|--------------|-------------------|-------------|
| **United Kingdom** | 6 months after FY end | Registration deadline |
| **Germany** | With or before first GIR | GIR filing |
| **Netherlands** | Before first GIR | GIR filing |
| **France** | Before first GIR | GIR filing |
| **Singapore** | 30 September following FY | Fixed date |
| **Australia** | With first GIR lodgment | GIR deadline |
| **Ireland** | Before first return | GIR filing |
| **Switzerland** | Before first return | GIR filing |
| **Japan** | Before first return | GIR filing |
| **Canada** | 12 months after FY end | Fixed period |

### First-Year Transitional Timing (FY2024)

For the first in-scope fiscal year (2024 for calendar year-end groups):

| Event | Standard Date | Transitional Date |
|-------|---------------|-------------------|
| Fiscal Year End | 31 December 2024 | 31 December 2024 |
| Election Deadline | Varies | Varies (aligned to GIR) |
| GIR Filing Deadline | 31 March 2026 | 30 June 2026 |

**Practical Implication:** Groups have until the extended first-year deadline to complete both DFE elections and initial GIR filings, but earlier election is advisable to:

1. Confirm filing procedures
2. Test portal access
3. Resolve any registration issues
4. Allow time for corrections

### Multi-Jurisdiction Election Coordination

When a DFE files in multiple jurisdictions, election timing must be coordinated:

**Example: UK-Headquartered DFE Filing for EU Subsidiaries**

```
Timeline for December 2024 Year-End
===================================

31 Dec 2024    Fiscal year ends

30 Jun 2025    UK MTT registration deadline
               └── Must complete by this date

Jul-Dec 2025   Complete DFE notifications to:
               - Netherlands (before GIR)
               - Germany (before GIR)
               - France (before GIR)

30 Jun 2026    First GIR filing deadline (transitional)
               └── All elections must be in place
```

---

## 8.3.5 Election Amendments and Revocations

### Amending DFE Elections

Elections may need amendment for various reasons:

| Reason | Action Required |
|--------|-----------------|
| **Additional jurisdictions** | Extend DFE scope |
| **Jurisdictions removed** | Narrow DFE scope |
| **Entity changes** | Update CE listing |
| **DFE entity change** | New election required |

**Amendment Process (General):**

1. Submit amended notification to relevant authority
2. Reference original election/notification
3. Specify changes and effective date
4. Provide updated supporting documentation

### Revoking DFE Status

DFE status can be terminated:

**Voluntary Revocation:**
- Submit revocation notice to each jurisdiction
- Ensure replacement filing arrangements in place
- Typically effective from next fiscal year

**Automatic Termination:**
- DFE ceases to be a Constituent Entity
- Group falls below revenue threshold
- DFE becomes ineligible (e.g., excluded entity)

**Consequences of Revocation:**
- Local filing obligations revert to Constituent Entities
- Must be coordinated to avoid filing gaps
- Historical filings remain valid

---

## 8.3.6 Record-Keeping Requirements

### Retention Periods

DFE election documentation must be retained for audit and compliance purposes:

| Jurisdiction | Minimum Retention | Notes |
|--------------|-------------------|-------|
| **UK** | 6 years | From end of relevant period |
| **Germany** | 10 years | Standard tax retention |
| **Netherlands** | 7 years | Fiscale bewaarplicht |
| **France** | 6 years | From filing date |
| **Singapore** | 5 years | From filing date |
| **Australia** | 5 years | From lodgment date |
| **OECD Best Practice** | 10 years | Recommended |

### What to Retain

**Complete DFE Documentation File Should Include:**

1. **Election/Notification Forms**
   - Copies of all submitted forms
   - Submission confirmations/receipts
   - Reference numbers issued

2. **Supporting Documentation**
   - Board resolutions
   - Powers of Attorney
   - Group structure charts
   - Revenue evidence

3. **Correspondence**
   - Authority acknowledgments
   - Queries and responses
   - Amendment notifications

4. **Internal Documentation**
   - Decision memos
   - Approval chains
   - Risk assessments

---

## 8.3.7 Common Issues and Solutions

### Issue 1: Authority Chain Documentation

**Problem:** DFE cannot demonstrate clear authority to file for all entities

**Solution:**
- Obtain explicit written authorisation from UPE
- Cascade authority through intercompany agreements
- Document authority chain in board minutes

### Issue 2: Timing Misalignment

**Problem:** Different jurisdictions have different election deadlines

**Solution:**
- Create consolidated timeline for all jurisdictions
- Start with earliest deadline
- Build in buffer time for corrections

### Issue 3: Entity Changes During Year

**Problem:** Acquisitions/disposals change the CE population after election

**Solution:**
- Monitor group changes continuously
- Submit election amendments promptly
- Document changes for audit trail

### Issue 4: Portal Access Issues

**Problem:** Cannot access jurisdiction portal for election submission

**Solution:**
- Start registration process early
- Engage local advisors for portal navigation
- Use authorised representatives where permitted

### Issue 5: Language Barriers

**Problem:** Election forms in local language

**Solution:**
- Use professional translation services
- Engage local country advisors
- Maintain English translations for internal records

---

## Practical Exercise: DFE Election Documentation

### Scenario

Your client, GlobalTech Solutions Inc. (US-parented), needs to appoint a DFE. They have selected their UK subsidiary, GlobalTech UK Ltd, as the DFE. The group has operations in:
- United States (UPE)
- United Kingdom (proposed DFE)
- Germany (3 entities)
- Netherlands (2 entities)
- Singapore (1 entity)
- Australia (1 entity)

The fiscal year is calendar year; first in-scope year is 2024.

### Task

Prepare an election documentation timeline and checklist for this group.

### Model Answer

**Election Timeline:**

| Date | Action | Jurisdiction |
|------|--------|--------------|
| Q1 2025 | Board resolution - GlobalTech UK Ltd | Internal |
| Q1 2025 | UPE authorisation letter | US → UK |
| 30 Jun 2025 | UK MTT registration + DFE notification | UK (HMRC) |
| Q3 2025 | DFE notification submissions | Germany, Netherlands |
| 30 Sep 2025 | GFE/DFE registration | Singapore |
| Q4 2025 | DFE notification | Australia |
| 30 Jun 2026 | First GIR filing | All jurisdictions |

**Documentation Checklist:**

- [ ] GlobalTech UK Ltd board resolution
- [ ] GlobalTech Solutions Inc. authorisation letter
- [ ] Group structure chart (all 8+ entities)
- [ ] Consolidated revenue evidence (FY2022, FY2023)
- [ ] Entity listing with TINs for each jurisdiction
- [ ] UK: CRN, UTR confirmation
- [ ] Germany: BZSt registration, ELSTER access
- [ ] Netherlands: eHerkenning Level 3, KvK number
- [ ] Singapore: Corppass setup, UEN
- [ ] Australia: ABN listing, myGovID for authorised person

---

## Deliverable: DFE Election Template Package

### Package Contents

The DFE Election Template Package includes the following templates for client use:

---

### Template 1: DFE Board Resolution

```
BOARD RESOLUTION
================

Company: [DFE Company Name]
Registered Number: [Registration Number]
Date of Meeting: [Date]
Resolution Reference: [Number]

APPOINTMENT AS DESIGNATED FILING ENTITY UNDER OECD PILLAR TWO

BACKGROUND

A. [Ultimate Parent Entity Name] is the Ultimate Parent Entity of an
   MNE Group with consolidated revenues exceeding EUR 750 million.

B. The MNE Group is subject to the GloBE Rules implemented under OECD
   Pillar Two in various jurisdictions.

C. The MNE Group has determined that a Designated Filing Entity should
   be appointed to file GloBE Information Returns centrally.

RESOLUTION

IT IS RESOLVED THAT:

1. APPOINTMENT
   [DFE Company Name] is hereby appointed as the Designated Filing
   Entity for the [Group Name] MNE Group with effect from [Date].

2. SCOPE
   The DFE appointment covers GloBE Information Return filings in the
   following jurisdictions:

   - [Jurisdiction 1]
   - [Jurisdiction 2]
   - [Jurisdiction 3]
   [Add/remove as applicable]

3. AUTHORISED SIGNATORIES
   The following individuals are authorised to sign and submit filings
   on behalf of the DFE:

   Name: _________________________ Title: _________________________
   Name: _________________________ Title: _________________________

4. RESOURCES
   The Board approves the allocation of necessary resources, systems,
   and personnel to fulfil DFE responsibilities.

5. DELEGATION
   The [CEO/CFO/Tax Director] is authorised to take all necessary
   actions to implement this resolution.

CERTIFICATION

I certify that this is a true copy of the resolution passed at a
meeting of the Board of Directors on [Date].

_____________________________
Company Secretary
Date: _______________________
```

---

### Template 2: UPE Authorisation Letter

```
[UPE LETTERHEAD]

AUTHORISATION FOR DESIGNATED FILING ENTITY APPOINTMENT
======================================================

Date: [Date]

To Whom It May Concern

RE: Appointment of Designated Filing Entity - GloBE Information Returns

[Ultimate Parent Entity Name] ("UPE"), incorporated in [Jurisdiction],
is the Ultimate Parent Entity of the [Group Name] multinational
enterprise group.

AUTHORISATION

The UPE hereby authorises and appoints:

[DFE Company Name]
[Address]
[Registration Number/Tax ID]

as the Designated Filing Entity for the MNE Group for purposes of
filing GloBE Information Returns under the OECD Pillar Two framework.

SCOPE OF AUTHORISATION

This authorisation covers:

1. Registration with relevant tax authorities as the DFE
2. Preparation and filing of GloBE Information Returns
3. Submission of related notifications and elections
4. Correspondence with tax authorities regarding GIR matters
5. Amendment of filings as necessary

JURISDICTIONS COVERED

This authorisation applies to filings in the following jurisdictions:

☐ United Kingdom          ☐ Germany
☐ Netherlands             ☐ France
☐ Singapore               ☐ Australia
☐ Ireland                 ☐ Other: ____________

DURATION

This authorisation is effective from [Start Date] and continues until
revoked in writing by the UPE.

ACKNOWLEDGMENT

The UPE acknowledges that:
- The DFE will require data from all Constituent Entities
- Local filing obligations may be satisfied through DFE filing
- The UPE remains ultimately responsible for GloBE compliance

_____________________________
Authorised Signatory
[Name]
[Title]
[Ultimate Parent Entity Name]

Date: _______________________
```

---

### Template 3: Constituent Entity Coverage Matrix

```
DFE CONSTITUENT ENTITY COVERAGE MATRIX
======================================

DFE Entity: [Name]
Effective Date: [Date]
Prepared by: [Name]
Date Prepared: [Date]

+----+----------------------+--------------+--------------+------------+----------+----------+
| #  | Entity Name          | Jurisdiction | Tax Res.     | TIN        | Type     | Covered? |
+----+----------------------+--------------+--------------+------------+----------+----------+
| 1  | [Entity name]        | [Country]    | [Country]    | [Number]   | [Type]   | Yes/No   |
+----+----------------------+--------------+--------------+------------+----------+----------+
| 2  |                      |              |              |            |          |          |
+----+----------------------+--------------+--------------+------------+----------+----------+
| 3  |                      |              |              |            |          |          |
+----+----------------------+--------------+--------------+------------+----------+----------+
| 4  |                      |              |              |            |          |          |
+----+----------------------+--------------+--------------+------------+----------+----------+
| 5  |                      |              |              |            |          |          |
+----+----------------------+--------------+--------------+------------+----------+----------+

Entity Types:
- UPE = Ultimate Parent Entity
- IPE = Intermediate Parent Entity
- POPE = Partially-Owned Parent Entity
- CE = Constituent Entity (standard)
- JV = Joint Venture
- JVCE = JV Constituent Entity
- PE = Permanent Establishment
- EXC = Excluded Entity

Covered Status:
- Yes = Included in DFE filing scope
- No = Files separately / Excluded

SUMMARY

Total Constituent Entities: [Number]
Entities Covered by DFE: [Number]
Entities Filing Separately: [Number]
Excluded Entities: [Number]

JURISDICTIONS SUMMARY

| Jurisdiction | # Entities | # Covered | Filing Authority |
|--------------|------------|-----------|------------------|
| [Country]    | [#]        | [#]       | [Authority name] |
|              |            |           |                  |

_____________________________
Prepared by: [Name/Title]
Date: _______________________

_____________________________
Approved by: [Name/Title]
Date: _______________________
```

---

### Template 4: DFE Election Checklist

```
DFE ELECTION DOCUMENTATION CHECKLIST
====================================

Client: _________________________________
DFE Entity: _____________________________
Effective FY: ___________________________
Prepared by: _____________ Date: ________

CORE DOCUMENTATION                               Status    Date
===================                              ======    ====

□ Board Resolution - DFE appointment             [  ]      ____
□ UPE Authorisation Letter                       [  ]      ____
□ Group Structure Chart                          [  ]      ____
□ Constituent Entity Coverage Matrix             [  ]      ____
□ Revenue Threshold Evidence                     [  ]      ____
  - FY [    ] consolidated financials            [  ]      ____
  - FY [    ] consolidated financials            [  ]      ____

JURISDICTION-SPECIFIC REQUIREMENTS               Status    Date
==================================               ======    ====

United Kingdom (HMRC)
□ MTT Registration completed                     [  ]      ____
□ DFE Notification submitted                     [  ]      ____
□ Confirmation received                          [  ]      ____
□ Reference number: ____________________

Germany (BZSt)
□ Group Head Notification submitted              [  ]      ____
□ DFE Declaration (MiSt-BFE) submitted           [  ]      ____
□ Vollmacht on file                              [  ]      ____
□ Reference number: ____________________

Netherlands (Belastingdienst)
□ eHerkenning Level 3 obtained                   [  ]      ____
□ DFE Melding submitted                          [  ]      ____
□ Bevestiging received                           [  ]      ____
□ Reference number: ____________________

France (DGFiP)
□ Form 2913-SD submitted                         [  ]      ____
□ Confirmation received                          [  ]      ____
□ Reference number: ____________________

Singapore (IRAS)
□ MTT Registration completed                     [  ]      ____
□ GFE/DFE Appointment submitted                  [  ]      ____
□ Acknowledgment received                        [  ]      ____
□ Reference number: ____________________

Australia (ATO)
□ DFE Notification submitted                     [  ]      ____
□ Acknowledgment received                        [  ]      ____
□ Reference number: ____________________

Other: _______________________
□ Registration/notification submitted            [  ]      ____
□ Confirmation received                          [  ]      ____
□ Reference number: ____________________

FILING PREPARATION                               Status    Date
==================                               ======    ====

□ All portal access credentials confirmed        [  ]      ____
□ Data collection process established            [  ]      ____
□ Filing calendar created                        [  ]      ____
□ Responsible persons assigned                   [  ]      ____

SIGN-OFF
========

Preparer: _____________________ Date: __________
Reviewer: _____________________ Date: __________
Partner: ______________________ Date: __________
```

---

### Template 5: Multi-Jurisdiction Election Timeline

```
DFE ELECTION TIMELINE - MULTI-JURISDICTION
==========================================

Client: _________________________________
DFE Entity: _____________________________
First In-Scope FY End: __________________

TIMELINE
========

[Fiscal Year End Date]: _______________

+----------+------------------+-------------------------------------------+--------+
| Target   | Jurisdiction     | Action Required                           | Status |
+----------+------------------+-------------------------------------------+--------+
| +3 mo    | Internal         | Board resolution approved                 | [  ]   |
+----------+------------------+-------------------------------------------+--------+
| +3 mo    | Internal         | UPE authorisation obtained                | [  ]   |
+----------+------------------+-------------------------------------------+--------+
| +4 mo    | UK               | MTT registration initiated                | [  ]   |
+----------+------------------+-------------------------------------------+--------+
| +5 mo    | Germany          | BZSt Group Head Notification              | [  ]   |
+----------+------------------+-------------------------------------------+--------+
| +6 mo    | UK               | MTT registration/DFE notification deadline| [  ]   |
+----------+------------------+-------------------------------------------+--------+
| +6 mo    | Netherlands      | eHerkenning application (if needed)       | [  ]   |
+----------+------------------+-------------------------------------------+--------+
| +9 mo    | Singapore        | MTT registration deadline (30 Sep)        | [  ]   |
+----------+------------------+-------------------------------------------+--------+
| +12 mo   | All EU           | DFE notifications completed               | [  ]   |
+----------+------------------+-------------------------------------------+--------+
| +12 mo   | Australia        | DFE notification submitted                | [  ]   |
+----------+------------------+-------------------------------------------+--------+
| +15 mo   | All              | Standard GIR filing deadline              | [  ]   |
+----------+------------------+-------------------------------------------+--------+
| +18 mo   | All              | Transitional GIR filing deadline          | [  ]   |
+----------+------------------+-------------------------------------------+--------+

NOTES:
- All dates calculated from fiscal year end
- Transitional +18 month deadline applies to first in-scope FY only
- Adjust for non-calendar year-ends
- Build in buffer time for portal issues

KEY DATES FOR FY [____]:

FY End:                    _______________
UK Registration Deadline:  _______________
Singapore Deadline:        _______________
Standard GIR Deadline:     _______________
Transitional GIR Deadline: _______________
```

---

## Section Summary

DFE election documentation requires careful attention to:

1. **Jurisdiction-specific requirements** - Each country has unique forms and processes
2. **Supporting documentation** - Authorisation, structure, and revenue evidence
3. **Timeline coordination** - Multiple deadlines across jurisdictions
4. **Record-keeping** - Retention for audit and compliance purposes

The DFE Election Template Package provides standardised documentation that can be adapted to any MNE group structure.

---

## Key Takeaways

| Topic | Key Point |
|-------|-----------|
| **Election vs. Notification** | Terms vary; substance similar across jurisdictions |
| **Core Documents** | Board resolution, UPE authorisation, structure chart, revenue evidence |
| **UK Deadline** | 6 months after FY end for MTT registration |
| **EU Approach** | Generally before first GIR filing |
| **Singapore Deadline** | 30 September following fiscal year |
| **Retention** | Minimum 6-10 years depending on jurisdiction |
| **Amendment Process** | Submit updated notification; reference original |

---

*Section 8.3 Complete. Proceed to Section 8.4: DFE Responsibilities for data collection, coordination, and liability considerations.*
