# Section 7.2: United Kingdom

## Learning Objectives

By the end of this section, you will be able to:
- Register for the HMRC "Report Pillar 2 top-up taxes" service using Government Gateway
- Understand the three UK filing obligations: Registration, UK Self Assessment Return, and GIR/ORN
- Complete the step-by-step GIR submission process through HMRC's digital service
- Calculate UK-specific deadlines for registration, filing, and payment
- Navigate the Overseas Return Notification (ORN) process when the GIR is filed in another jurisdiction
- Apply the UK Pillar Two Filing Checklist for compliance assurance
- Understand penalty exposure and amendment procedures

## Introduction

The United Kingdom implemented Pillar Two through the Multinational Top-up Tax (MTT) and Domestic Top-up Tax (DTT) rules in Finance (No.2) Act 2023, effective for accounting periods beginning on or after 31 December 2023. The Undertaxed Profits Rule (UTPR) became effective for accounting periods beginning on or after 31 December 2024.

UK-headed MNE Groups and UK members of foreign-headed groups face three distinct compliance obligations:
1. **Registration** with HMRC's "Report Pillar 2 top-up taxes" service
2. **UK Self Assessment Return** reporting MTT and DTT liabilities
3. **GloBE Information Return (GIR)** or **Overseas Return Notification (ORN)**

**Critical Point:** Even groups with no MTT or DTT liability must complete all three obligations if they are in scope. HMRC has contacted approximately 4,500 UK groups considered potentially in scope.

---

## 7.2.1 HMRC Registration Process

### Registration Requirements

Every in-scope group must register with HMRC before any returns can be filed. Registration is a one-time process covering both MTT and DTT.

**Who Must Register:**
- Groups with consolidated annual revenues of €750 million or more in at least 2 of the previous 4 accounting periods
- Groups with at least one UK entity or UK permanent establishment
- Registration required even if no top-up tax liability is expected

**Registration Service:**
- **Portal:** Report Pillar 2 top-up taxes
- **URL:** https://www.gov.uk/guidance/register-to-report-pillar-2-top-up-taxes
- **Authentication:** Organisation Government Gateway account required

### Registration Deadline Calculation

```
UK Registration Deadline Formula:

Registration Deadline = End of First In-Scope Accounting Period + 6 months

Example Calculations:
┌─────────────────────────────┬──────────────────────────┐
│ Accounting Period End       │ Registration Deadline    │
├─────────────────────────────┼──────────────────────────┤
│ 31 December 2024            │ 30 June 2025             │
│ 31 January 2025             │ 31 July 2025             │
│ 31 March 2025               │ 30 September 2025        │
│ 30 June 2025                │ 31 December 2025         │
│ 30 September 2025           │ 31 March 2026            │
└─────────────────────────────┴──────────────────────────┘
```

**Immediate Action Required:** Groups with a 31 December 2024 year-end must register by **30 June 2025**.

### Step-by-Step Registration Process

```
HMRC Pillar 2 Registration Process:
│
├── STEP 1: Prepare Government Gateway Account
│   ├── Verify organisation Government Gateway user ID exists
│   ├── Individual or agent accounts CANNOT be used
│   ├── If no organisation account exists, create one at:
│   │   https://www.gov.uk/log-in-register-hmrc-online-services
│   └── Required: Company Registration Number and Corporation Tax UTR
│
├── STEP 2: Access the Registration Service
│   ├── Navigate to: https://www.gov.uk/guidance/register-to-report-pillar-2-top-up-taxes
│   ├── Click "Register now"
│   ├── Sign in using organisation Government Gateway credentials
│   └── Note: Agents CANNOT register on behalf of groups
│
├── STEP 3: Complete Registration Information
│   ├── Enter Company Registration Number (CRN)
│   ├── Enter Corporation Tax Unique Taxpayer Reference (UTR)
│   ├── Select registration type:
│   │   ├── "UK Only" = DTT only (UK entities only)
│   │   └── "UK and Other Jurisdictions" = MTT + DTT (overseas entities)
│   ├── Enter group accounting period start and end dates
│   └── Provide contact details (1-2 individuals or teams)
│
├── STEP 4: Receive Pillar 2 Reference Number
│   ├── Registration completes immediately if details verified
│   ├── Receive unique Pillar 2 Reference Number
│   ├── IMPORTANT: Record this number—no email confirmation sent
│   ├── Use Print Page function to save PDF confirmation
│   └── This number required for all future filings
│
└── STEP 5: Add Agents (Optional, Post-Registration)
    ├── Navigate to Agent Services within the portal
    ├── Grant authority to tax advisers to manage Pillar 2 matters
    └── Note: Agents can file returns but cannot register
```

### Registration Information Required

| Information Item | Where to Find | Notes |
|-----------------|---------------|-------|
| Company Registration Number (CRN) | Companies House register | 8-character alphanumeric |
| Corporation Tax UTR | HMRC CT41G letter or Business Tax Account | 10-digit number |
| Filing member identity | Group internal determination | UPE by default, or nominated entity |
| Accounting period dates | Group financial statements | First in-scope period start/end |
| Contact details | Internal contacts | Phone, email for 1-2 persons/teams |

### Filing Member Determination

The "filing member" is responsible for all UK Pillar Two compliance obligations:

```
Filing Member Determination:
│
├── DEFAULT: Ultimate Parent Entity (UPE)
│   └── The UPE is automatically the filing member unless:
│
├── NOMINATION: Alternative Filing Member
│   ├── UPE may nominate another group entity
│   ├── Nomination need not be documented at registration
│   ├── HMRC may request evidence during compliance checks
│   └── Nominated entity must have UK presence
│
└── REQUIREMENTS for Filing Member:
    ├── Must have organisation Government Gateway account
    ├── Must be able to fulfil all filing obligations
    └── Single filing member for entire group
```

---

## 7.2.2 UK Filing Obligations Overview

### Three-Part Compliance Framework

UK Pillar Two compliance involves three mandatory filings (assuming in-scope):

```
UK Pillar Two Filing Obligations:
│
├── 1. UK SELF ASSESSMENT RETURN (Mandatory for all registered groups)
│   ├── Purpose: Report MTT and DTT liabilities for UK group
│   ├── Format: Digital submission via HMRC portal
│   ├── Content: Liability calculations per UK entity
│   ├── Deadline: Same as GIR/ORN deadline
│   └── Required even if liability = zero
│
├── 2A. GloBE INFORMATION RETURN (GIR)
│   ├── When: Filed in UK if UPE is UK-resident
│   ├── When: Filed in UK if UK is designated filing jurisdiction
│   ├── Format: OECD XML Schema v1.0 via third-party software
│   ├── Content: Full GIR per OECD specification
│   └── Subject to automatic exchange under GIR MCAA
│
│   OR
│
├── 2B. OVERSEAS RETURN NOTIFICATION (ORN)
│   ├── When: GIR filed in another jurisdiction
│   ├── When: Foreign tax authority will exchange GIR with HMRC
│   ├── Format: Digital notification via HMRC portal
│   ├── Content: Confirms where/when GIR was filed
│   └── Cannot be used if group registered "UK Only"
│
└── BOTH Required:
    ├── UK SA Return + GIR (if filing GIR in UK)
    └── UK SA Return + ORN (if filing GIR elsewhere)
```

### Filing Deadline Framework

```
UK Pillar Two Filing Deadlines:

┌────────────────────────────────────────────────────────────────────┐
│ FIRST IN-SCOPE PERIOD: 18 months from accounting period end       │
│ SUBSEQUENT PERIODS: 15 months from accounting period end          │
│ MINIMUM DEADLINE: Not before 30 June 2026 (OECD Guidance)         │
└────────────────────────────────────────────────────────────────────┘

Deadline Examples (First Year):
┌─────────────────────────────┬──────────────────────────┬───────────────────────┐
│ Accounting Period End       │ GIR/ORN/SA Deadline      │ Payment Deadline      │
├─────────────────────────────┼──────────────────────────┼───────────────────────┤
│ 31 December 2024            │ 30 June 2026             │ 30 June 2026          │
│ 31 January 2025             │ 31 July 2026             │ 31 July 2026          │
│ 31 March 2025               │ 30 September 2026        │ 30 September 2026     │
│ 30 June 2025                │ 31 December 2026         │ 31 December 2026      │
│ 31 December 2025 (Year 2)   │ 31 March 2027 (15 mo)    │ 31 March 2027         │
└─────────────────────────────┴──────────────────────────┴───────────────────────┘

Note: Filing and payment deadlines are identical.
```

---

## 7.2.3 GIR Submission Process (UK-Filed)

### When to File GIR in UK

The GIR should be filed in the UK when:
- The Ultimate Parent Entity (UPE) is UK tax-resident
- The UK entity is the Designated Filing Entity (DFE) for the group
- The group has elected to file centrally in the UK

### Technical Requirements

**Software Requirements:**
- GIR must be submitted using **third-party software** that integrates with HMRC's Pillar 2 API
- Direct portal upload of XML files is not available
- Software must comply with HMRC's minimum functionality standards
- HMRC Developer Hub: https://developer.service.hmrc.gov.uk/guides/pillar2-service-guide/

**XML Schema:**
- OECD GIR XML Schema v1.0 (January 2025)
- UK accepts the international OECD schema format
- Validate XML locally before submission

**Software Functionality Requirements:**

| Requirement | Description |
|-------------|-------------|
| Transaction monitoring | Provide HMRC fraud prevention header data |
| UKTR submission | Submit UK Tax Return |
| BTN submission | Submit Below Threshold Notification |
| Amendment capability | Make corrections to submitted returns |
| Obligation retrieval | Retrieve filing obligations per period |
| Digital record keeping | Create and maintain required digital records |
| Data export | Enable user access to and export of records |

### Step-by-Step GIR Filing Process

```
UK GIR Filing Process:
│
├── PRE-SUBMISSION
│   ├── Ensure registration complete (Pillar 2 Reference Number obtained)
│   ├── Verify third-party software configured with HMRC API
│   ├── Complete GIR data compilation per OECD specification
│   ├── Generate XML file using OECD Schema v1.0
│   ├── Validate XML using three-tier validation:
│   │   ├── Tier 1: Well-formedness
│   │   ├── Tier 2: Schema validation
│   │   └── Tier 3: Business rules
│   └── Obtain internal sign-off on GIR content
│
├── SUBMISSION
│   ├── Access third-party filing software
│   ├── Authenticate using Government Gateway credentials
│   ├── Navigate to GIR submission function
│   ├── Select accounting period for submission
│   ├── Upload validated GIR XML file
│   ├── Software performs final validation
│   ├── Review submission summary
│   └── Confirm and submit
│
├── UK SELF ASSESSMENT RETURN
│   ├── Access HMRC portal or third-party software
│   ├── Complete UK SA Return for same period
│   ├── Enter MTT liability amounts per UK entity
│   ├── Enter DTT liability amounts per UK entity
│   ├── Review and submit UK SA Return
│   └── Note: Can be filed simultaneously with GIR
│
└── POST-SUBMISSION
    ├── Receive submission confirmation/reference number
    ├── Download and archive confirmation documentation
    ├── Record submission details in filing register
    ├── Set reminder for payment deadline (if liability due)
    └── Monitor for HMRC queries or rejection notices
```

---

## 7.2.4 Overseas Return Notification (ORN) Process

### When ORN is Required

The ORN is required when:
- The group files its GIR in another jurisdiction (e.g., parent company jurisdiction)
- The group expects that jurisdiction to exchange the GIR with HMRC under the GIR MCAA
- The group is NOT registered as "UK Only" (DTT-only groups cannot submit ORN)

### ORN Information Requirements

```
ORN Required Information:
│
├── Filing Entity Details
│   ├── Tax Identification Number (TIN) of entity submitting ORN
│   ├── Country code for TIN issuing jurisdiction
│   └── Pillar 2 Reference Number (from UK registration)
│
├── Accounting Period
│   ├── Period start date
│   └── Period end date
│
└── GIR Filing Details
    ├── Submission date of GIR in other jurisdiction
    ├── Country code where GIR was filed
    └── Note: Must be a jurisdiction participating in GIR MCAA
```

### Step-by-Step ORN Process

```
ORN Filing Process:
│
├── PREREQUISITES
│   ├── GIR must already be filed in other jurisdiction
│   ├── Obtain confirmation of GIR submission (date, reference)
│   ├── Verify other jurisdiction is GIR MCAA participant
│   └── Confirm UK registration is NOT "UK Only"
│
├── SUBMISSION
│   ├── Access HMRC Pillar 2 service
│   ├── Authenticate using Government Gateway
│   ├── Navigate to ORN submission section
│   ├── Enter filing entity TIN details
│   ├── Enter accounting period dates
│   ├── Enter GIR submission details:
│   │   ├── Country where GIR filed
│   │   └── Date GIR was submitted
│   └── Submit ORN
│
├── UK SELF ASSESSMENT RETURN
│   ├── UK SA Return still required separately
│   ├── Complete as per Section 7.2.3
│   └── Same deadline applies
│
└── POST-SUBMISSION
    ├── Receive ORN confirmation
    ├── Archive confirmation with GIR filing evidence
    └── Retain records per document retention policy
```

**Important:** The ORN does not contain the substantive GIR data—it simply notifies HMRC that the GIR was filed elsewhere and will be received via automatic exchange.

---

## 7.2.5 UK-Specific Requirements

### Undertaxed Profits Rule (UTPR)

The UK UTPR became effective for accounting periods beginning on or after 31 December 2024:

```
UK UTPR Implementation:
│
├── EFFECTIVE DATE
│   └── Accounting periods beginning on or after 31 December 2024
│
├── TRANSITIONAL RULES
│   ├── Group first in scope of UTPR = later of:
│   │   ├── First period meeting revenue threshold, AND
│   │   └── First period beginning on or after 31 December 2024
│   └── Groups already in scope of IIR will add UTPR obligations
│
├── UTPR SAFE HARBOUR
│   ├── Applies for one year only
│   ├── Available if accounting period commences on or before 31 December 2025
│   ├── UPE jurisdiction must have minimum tax rate of at least 20%
│   └── Allows simplified calculation where safe harbour applies
│
├── ELECTION OPTIONS
│   └── Single Constituent Entity election available:
│       └── One UK entity can be designated liable for entire UK UTPR allocation
│
└── INTERACTION WITH ORIP
    └── Offshore Receipts in Respect of Intangible Property (ORIP) rules
        repealed for income arising from same date UTPR effective
```

### UK Self Assessment Return Content

The UK SA Return covers both MTT and DTT in a single submission:

```
UK SA Return Content Structure:
│
├── GROUP INFORMATION
│   ├── Pillar 2 Reference Number
│   ├── Accounting period dates
│   └── Filing member details
│
├── MTT LIABILITY SECTION
│   ├── Total MTT liability for group
│   ├── MTT liability allocated to each UK constituent entity
│   ├── Top-up tax amounts by low-tax jurisdiction
│   └── Any UTPR top-up tax allocated to UK
│
├── DTT LIABILITY SECTION
│   ├── Total DTT liability for group
│   ├── DTT liability per UK constituent entity
│   └── QDMTT calculations if applicable
│
├── ELECTIONS AND NOTIFICATIONS
│   ├── Any elections made for the period
│   ├── Safe harbour claims
│   └── DFE nominations
│
└── DECLARATION
    ├── Authorised signatory details
    └── Declaration of accuracy
```

### Below Threshold Notification (BTN)

If a group ceases to meet the €750 million revenue threshold, it may submit a Below Threshold Notification:

```
Below Threshold Notification:
│
├── WHEN TO USE
│   ├── Group no longer meets revenue threshold
│   ├── Group has fallen below €750m in 2 of last 4 periods
│   └── No longer wishes to remain in Pillar 2 scope
│
├── EFFECT
│   ├── Group deregistered from Pillar 2 obligations
│   ├── No further SA returns, GIR, or ORN required
│   └── Must re-register if threshold later met again
│
└── PROCESS
    └── Submit BTN via HMRC Pillar 2 service
```

---

## 7.2.6 Penalties and Interest

### Penalty Framework

UK Pillar Two penalties follow existing HMRC penalty frameworks:

```
UK Pillar Two Penalty Framework:
│
├── LATE REGISTRATION PENALTY
│   ├── Legislative basis: Schedule 41, Finance Act 2008
│   ├── "Failure to notify" penalty regime
│   ├── Penalty based on:
│   │   ├── Behaviour (deliberate vs careless vs reasonable care)
│   │   └── Potential lost revenue
│   ├── Maximum penalty: 100% of potential lost revenue (deliberate)
│   └── Reduced for disclosure and cooperation
│
├── LATE FILING PENALTY
│   ├── Legislative basis: Schedule 55, Finance Act 2009
│   ├── Applies to: GIR, ORN, and UK SA Return
│   ├── Structure:
│   │   ├── Initial fixed penalty at deadline
│   │   ├── Daily penalties after 3 months
│   │   └── Tax-geared penalties after 6/12 months
│   └── Penalty amounts set by regulations
│
├── LATE PAYMENT PENALTY
│   ├── Legislative basis: Schedule 56, Finance Act 2009
│   ├── Applies when MTT/DTT payment overdue
│   ├── Percentage-based on unpaid tax
│   └── Escalates over time
│
├── INACCURACY PENALTY
│   ├── Legislative basis: Schedule 24, Finance Act 2007
│   ├── Applies to inaccurate returns
│   ├── Based on behaviour and potential lost revenue
│   └── Maximum: 100% of potential lost revenue
│
└── REASONABLE EXCUSE DEFENCE
    ├── Available for all penalty types
    ├── Must demonstrate genuine reasonable excuse
    ├── Excuse must continue until filing occurs
    └── Common excuses: system failures, illness, bereavement
```

### Interest on Late Payment

```
Interest on Unpaid MTT/DTT:
│
├── INTEREST RATE
│   ├── Base rate + 2.5% (standard HMRC rate)
│   ├── Compounds daily
│   └── Runs from payment deadline until payment received
│
├── CALCULATION
│   ├── Interest = Unpaid Tax × Daily Rate × Days Overdue
│   └── Daily Rate = (Base Rate + 2.5%) ÷ 365
│
└── CURRENT RATES
    └── Check: https://www.gov.uk/government/publications/rates-and-allowances-hmrc-interest-rates-for-late-and-early-payments
```

### Penalty Mitigation

| Mitigation Factor | Effect on Penalty |
|-------------------|-------------------|
| Unprompted disclosure | 30-50% reduction |
| Prompted disclosure with cooperation | 10-30% reduction |
| Reasonable excuse | Full relief possible |
| First-time error | HMRC may exercise discretion |
| Technical difficulty with HMRC systems | Likely full relief |

---

## 7.2.7 Amendment Procedures

### Amending Filed Returns

```
Amendment Process:
│
├── TIMING
│   ├── Amendments can be submitted using third-party software
│   ├── No specific time limit stated for Pillar 2 amendments
│   ├── General SA amendment principles may apply:
│   │   ├── Taxpayer amendment: within 12 months of filing deadline
│   │   └── HMRC correction: within 9 months of filing
│   └── Beyond time limits: contact HMRC in writing
│
├── PROCESS
│   ├── Generate corrected GIR XML file
│   ├── Submit amended return via software
│   ├── Software marks submission as amendment
│   ├── HMRC processes amendment against original
│   └── May result in additional liability or refund
│
├── UK SA RETURN AMENDMENTS
│   ├── Submit corrected UK SA Return
│   ├── Use same software/portal process
│   └── HMRC computes revised liability
│
└── DOCUMENTATION
    ├── Maintain clear audit trail of changes
    ├── Document reason for amendment
    ├── Retain original and amended versions
    └── Update filing register with amendment details
```

### HMRC Enquiries

```
HMRC Enquiry Process:
│
├── OPENING ENQUIRY
│   ├── HMRC may open enquiry into any return
│   ├── Enquiry window: generally within 12 months of filing
│   ├── Notice of enquiry issued in writing
│   └── Group must respond to information requests
│
├── INFORMATION POWERS
│   ├── Schedule 36, Finance Act 2008
│   ├── HMRC can request documents and information
│   ├── Third-party information notices possible
│   └── Failure to comply: penalties apply
│
├── RESOLUTION
│   ├── Enquiry closed by closure notice
│   ├── May result in amended assessment
│   ├── Interest and penalties may apply
│   └── Appeal rights available
│
└── APPEALS
    ├── Appeal within 30 days of decision
    ├── Internal review available
    ├── Tribunal appeal if unresolved
    └── First-tier Tribunal (Tax Chamber)
```

---

## 7.2.8 UK Portal Navigation Guide

### HMRC Digital Services Overview

```
HMRC Pillar 2 Digital Services:
│
├── REGISTRATION SERVICE
│   ├── URL: https://www.gov.uk/guidance/register-to-report-pillar-2-top-up-taxes
│   ├── Purpose: One-time registration for MTT/DTT
│   ├── Access: Organisation Government Gateway only
│   └── Output: Pillar 2 Reference Number
│
├── MAIN SERVICE PORTAL
│   ├── URL: https://www.gov.uk/guidance/report-pillar-2-top-up-taxes
│   ├── Purpose: File returns, submit notifications
│   ├── Access: Post-registration, Government Gateway login
│   └── Functions: Filing, amendments, account management
│
├── GUIDANCE AND HELP
│   ├── Main guidance: https://www.gov.uk/guidance/how-to-report-pillar-2-top-up-taxes
│   ├── Preparation guide: https://www.gov.uk/government/publications/preparing-for-the-multinational-top-up-tax-and-the-domestic-top-up-tax
│   ├── HMRC manual: https://www.gov.uk/hmrc-internal-manuals/multinational-top-up-tax-and-domestic-top-up-tax
│   └── API documentation: https://developer.service.hmrc.gov.uk/guides/pillar2-service-guide/
│
├── AGENT SERVICES
│   ├── Agents access via Agent Services Account
│   ├── Must be authorised by group after registration
│   ├── Can file returns on behalf of clients
│   └── Cannot register groups (filing member must register)
│
└── SUPPORT CONTACTS
    ├── Pillar 2 helpline: Contact via online form
    ├── Technical support: HMRC Developer Hub
    └── General enquiries: Business Tax Account
```

### Portal Navigation Steps

**Screenshot Reference Points (for compliance documentation):**

```
Key Portal Screens to Document:
│
├── SCREEN 1: Government Gateway Login
│   ├── URL: https://www.access.service.gov.uk/login
│   ├── Document: Successful login confirmation
│   └── Capture: Date/time of access
│
├── SCREEN 2: Pillar 2 Dashboard
│   ├── Shows: Registration status and reference number
│   ├── Shows: Outstanding filing obligations
│   └── Capture: Before each filing session
│
├── SCREEN 3: Filing Submission Confirmation
│   ├── Shows: Reference number for submission
│   ├── Shows: Date/time of submission
│   └── Capture: Immediately after successful submission
│
├── SCREEN 4: Payment Confirmation
│   ├── Shows: Amount paid
│   ├── Shows: Payment reference
│   └── Capture: After payment processed
│
└── SCREEN 5: Filing History
    ├── Shows: All submissions for accounting period
    ├── Shows: Status of each submission
    └── Capture: Periodically for records
```

---

## 7.2.9 Common Issues and Solutions

### Registration Issues

| Issue | Cause | Solution |
|-------|-------|----------|
| Cannot access registration | Individual/agent Government Gateway account | Create organisation Government Gateway account |
| UTR not recognised | Corporation Tax not registered | Ensure Corporation Tax registration complete first |
| CRN validation error | Incorrect company number format | Verify 8-character CRN from Companies House |
| "Already registered" message | Previous registration attempt | Check Business Tax Account for existing Pillar 2 registration |
| Agent cannot register | Attempting agent registration | Agent must wait for filing member to register, then be authorised |

### Filing Issues

| Issue | Cause | Solution |
|-------|-------|----------|
| XML validation failure | Schema error in GIR file | Run three-tier validation before submission; correct schema errors |
| Software API error | HMRC service disruption | Retry with exponential backoff; check HMRC service status |
| Cannot submit ORN | Registered as "UK Only" | Contact HMRC to change registration to include MTT |
| Missing accounting period | Period not registered | Verify accounting period dates in registration |
| Amendment rejected | Outside amendment window | Contact HMRC in writing for out-of-time correction |

### Payment Issues

| Issue | Cause | Solution |
|-------|-------|----------|
| Payment allocation error | Incorrect reference used | Ensure Pillar 2 Reference Number used for payment |
| Overpayment | Error in calculation | Request refund via HMRC portal |
| Underpayment | Amended liability | Pay balance promptly to minimise interest |
| Cannot find payment option | Service limitation | Contact HMRC for payment instructions |

---

## 7.2.10 Deliverable: UK Pillar Two Filing Checklist

### UK Pillar Two Compliance Checklist

```
UK PILLAR TWO FILING CHECKLIST
Group Name: ________________________________
Accounting Period: ____ / ____ / ____  to  ____ / ____ / ____
Pillar 2 Reference Number: _________________
Filing Member: ____________________________

═══════════════════════════════════════════════════════════════════════════════

SECTION A: REGISTRATION (Complete Before First Filing)
─────────────────────────────────────────────────────────────────────────────
☐ A1. Confirmed group meets €750m revenue threshold (2 of 4 years)
☐ A2. Identified filing member (UPE or nominated entity)
☐ A3. Filing member has organisation Government Gateway account
☐ A4. Corporation Tax UTR available for filing member
☐ A5. Company Registration Number (CRN) verified
☐ A6. Determined registration type:
      ☐ UK Only (DTT only)
      ☐ UK and Other Jurisdictions (MTT + DTT)
☐ A7. Completed registration via HMRC portal
☐ A8. Recorded Pillar 2 Reference Number: _________________
☐ A9. Saved registration confirmation (PDF screenshot)
☐ A10. Set up agent access (if using tax adviser for filing)

Registration Completed By: _____________ Date: ____ / ____ / ____

═══════════════════════════════════════════════════════════════════════════════

SECTION B: PRE-FILING PREPARATION
─────────────────────────────────────────────────────────────────────────────
☐ B1. Calculated registration deadline: _________________
☐ B2. Calculated GIR/ORN/SA deadline: _________________
☐ B3. Calculated payment deadline: _________________
☐ B4. Determined filing approach:
      ☐ File GIR in UK (proceed to Section C)
      ☐ File GIR overseas (proceed to Section D)
☐ B5. Third-party filing software configured and tested
☐ B6. API connection to HMRC verified
☐ B7. GIR data compilation complete
☐ B8. GIR XML file generated per OECD Schema v1.0
☐ B9. XML validation complete:
      ☐ Tier 1: Well-formedness PASS
      ☐ Tier 2: Schema validation PASS
      ☐ Tier 3: Business rules PASS
☐ B10. Internal review and sign-off obtained

Sign-off By: _____________ Position: _____________ Date: ____ / ____ / ____

═══════════════════════════════════════════════════════════════════════════════

SECTION C: GIR FILING (UK-Filed Returns)
─────────────────────────────────────────────────────────────────────────────
☐ C1. Authenticated to third-party software with Government Gateway
☐ C2. Selected correct accounting period
☐ C3. Uploaded validated GIR XML file
☐ C4. Reviewed submission summary for accuracy
☐ C5. Submitted GIR to HMRC
☐ C6. GIR submission reference received: _________________
☐ C7. GIR confirmation document downloaded and archived
☐ C8. Filed UK Self Assessment Return (Section E)
☐ C9. Updated filing register with GIR details

GIR Filed By: _____________ Date: ____ / ____ / ____ Time: ______

═══════════════════════════════════════════════════════════════════════════════

SECTION D: ORN FILING (GIR Filed Overseas)
─────────────────────────────────────────────────────────────────────────────
☐ D1. GIR filed in other jurisdiction: _________________
☐ D2. GIR filing date: ____ / ____ / ____
☐ D3. GIR filing reference obtained from other jurisdiction: _________________
☐ D4. Confirmed other jurisdiction is GIR MCAA participant
☐ D5. Confirmed UK registration NOT "UK Only"
☐ D6. Authenticated to HMRC Pillar 2 portal
☐ D7. Navigated to ORN submission section
☐ D8. Entered filing entity TIN and country code
☐ D9. Entered accounting period dates
☐ D10. Entered GIR filing country and submission date
☐ D11. Submitted ORN
☐ D12. ORN confirmation reference received: _________________
☐ D13. ORN confirmation document archived
☐ D14. Filed UK Self Assessment Return (Section E)
☐ D15. Updated filing register with ORN details

ORN Filed By: _____________ Date: ____ / ____ / ____ Time: ______

═══════════════════════════════════════════════════════════════════════════════

SECTION E: UK SELF ASSESSMENT RETURN
─────────────────────────────────────────────────────────────────────────────
☐ E1. Total MTT liability calculated: £ _________________
☐ E2. MTT liability per UK entity documented
☐ E3. Total DTT liability calculated: £ _________________
☐ E4. DTT liability per UK entity documented
☐ E5. UTPR allocations included (if applicable): £ _________________
☐ E6. Any elections documented in return
☐ E7. Safe harbour claims completed
☐ E8. UK SA Return submitted via software/portal
☐ E9. UK SA Return reference received: _________________
☐ E10. UK SA Return confirmation archived

UK SA Return Filed By: _____________ Date: ____ / ____ / ____

═══════════════════════════════════════════════════════════════════════════════

SECTION F: PAYMENT (If Liability Due)
─────────────────────────────────────────────────────────────────────────────
☐ F1. Total liability due: £ _________________
      (MTT: £ _________ + DTT: £ _________)
☐ F2. Payment deadline confirmed: ____ / ____ / ____
☐ F3. Payment method arranged:
      ☐ Direct Debit
      ☐ BACS
      ☐ CHAPS
      ☐ Online banking
☐ F4. Payment made using Pillar 2 Reference Number
☐ F5. Payment confirmation received
☐ F6. Payment confirmation archived
☐ F7. Verified payment reflected in HMRC account

Payment Made By: _____________ Date: ____ / ____ / ____ Amount: £ _________

═══════════════════════════════════════════════════════════════════════════════

SECTION G: POST-FILING
─────────────────────────────────────────────────────────────────────────────
☐ G1. All confirmation documents archived to filing folder
☐ G2. Filing register updated with all submission details
☐ G3. XML file and hash recorded for retention
☐ G4. Source documentation retained per retention policy
☐ G5. Set reminder for next period registration/filing deadlines
☐ G6. Briefed management on filing completion
☐ G7. Team notified of any HMRC query monitoring requirements

Post-Filing Completed By: _____________ Date: ____ / ____ / ____

═══════════════════════════════════════════════════════════════════════════════

CERTIFICATION
─────────────────────────────────────────────────────────────────────────────
I confirm that all applicable items in this checklist have been completed
and all UK Pillar Two filing obligations for the above accounting period
have been fulfilled.

Prepared By: _____________________________________________ Date: ____ / ____ / ____
                          (Name and Position)

Reviewed By: _____________________________________________ Date: ____ / ____ / ____
                          (Senior Reviewer)

Approved By: _____________________________________________ Date: ____ / ____ / ____
                          (Tax Director/Partner)

═══════════════════════════════════════════════════════════════════════════════

NOTES AND EXCEPTIONS
─────────────────────────────────────────────────────────────────────────────
[Document any issues encountered, exceptions, or matters requiring follow-up]

__________________________________________________________________________

__________________________________________________________________________

__________________________________________________________________________

__________________________________________________________________________

═══════════════════════════════════════════════════════════════════════════════
```

---

## Key Resources and Links

### HMRC Portals and Services

| Resource | URL |
|----------|-----|
| Registration Service | https://www.gov.uk/guidance/register-to-report-pillar-2-top-up-taxes |
| Main Filing Service | https://www.gov.uk/guidance/report-pillar-2-top-up-taxes |
| How to Report Guide | https://www.gov.uk/guidance/how-to-report-pillar-2-top-up-taxes |
| Check if You Need to Report | https://www.gov.uk/guidance/check-if-you-need-to-report-pillar-2-top-up-taxes |
| Preparation Guide | https://www.gov.uk/government/publications/preparing-for-the-multinational-top-up-tax-and-the-domestic-top-up-tax |
| Government Gateway | https://www.gov.uk/log-in-register-hmrc-online-services |
| Developer Hub (API) | https://developer.service.hmrc.gov.uk/guides/pillar2-service-guide/ |

### HMRC Technical Guidance

| Resource | URL |
|----------|-----|
| HMRC MTT/DTT Manual | https://www.gov.uk/hmrc-internal-manuals/multinational-top-up-tax-and-domestic-top-up-tax |
| GIR Structure (MTT52100) | https://www.gov.uk/hmrc-internal-manuals/multinational-top-up-tax-and-domestic-top-up-tax/mtt52100 |
| UTPR Manual (MTT62920) | https://www.gov.uk/hmrc-internal-manuals/multinational-top-up-tax-and-domestic-top-up-tax/mtt62920 |
| Safe Harbours (MTT15910) | https://www.gov.uk/hmrc-internal-manuals/multinational-top-up-tax-and-domestic-top-up-tax/mtt15910 |

### Legislation

| Resource | Reference |
|----------|-----------|
| Finance (No.2) Act 2023 | Part 3 (MTT), Part 4 (DTT) |
| Finance Act 2024-25 | UTPR provisions |
| Schedule 41, FA 2008 | Failure to notify penalties |
| Schedule 55, FA 2009 | Late filing penalties |
| Schedule 56, FA 2009 | Late payment penalties |
| Schedule 24, FA 2007 | Inaccuracy penalties |

### Interest Rates

| Resource | URL |
|----------|-----|
| HMRC Interest Rates | https://www.gov.uk/government/publications/rates-and-allowances-hmrc-interest-rates-for-late-and-early-payments |

---

## Summary

The UK's implementation of Pillar Two through MTT and DTT creates comprehensive compliance obligations for in-scope MNE Groups. Success requires:

1. **Timely Registration:** Complete within 6 months of first in-scope period end
2. **Three-Part Filing:** UK SA Return + GIR (or ORN) for every period
3. **Software Integration:** Third-party software required for GIR submission
4. **Penalty Awareness:** Significant penalties for late registration, filing, and payment
5. **Ongoing Monitoring:** Watch for HMRC queries and MCAA data exchange implications

The UK Pillar Two Filing Checklist provides a comprehensive framework for ensuring all obligations are met for each accounting period.

---

## Section Review Questions

1. What is the registration deadline for a group with an accounting period ending 31 December 2024?

2. Can a tax agent register a group for Pillar Two on behalf of their client?

3. What three filing obligations must a UK-headed MNE Group complete each period?

4. When should an Overseas Return Notification (ORN) be filed instead of a GIR?

5. What penalty legislation applies to late registration for Pillar Two?

6. From what date is the UK UTPR effective?

7. What type of Government Gateway account is required for Pillar Two registration?

**Answers:** 1) 30 June 2025; 2) No—filing member must register; 3) UK SA Return + GIR or ORN; 4) When GIR filed in another jurisdiction that will exchange with UK under GIR MCAA; 5) Schedule 41, Finance Act 2008; 6) Accounting periods beginning on or after 31 December 2024; 7) Organisation account (not individual or agent).

---

*Section 7.2 Complete. Proceed to Section 7.3: Germany for German-specific filing procedures.*
