# Section 7.1: Filing Overview and Portal Navigation

## Learning Objectives

By the end of this section, you will be able to:
- Understand the universal GIR filing process applicable across all implementing jurisdictions
- Identify common portal features and navigation patterns across tax authority systems
- Configure authentication requirements for GIR submission portals
- Ensure technical requirements (browsers, certificates, system specifications) are met before filing
- Apply the Multi-Jurisdiction Filing Coordination Checklist for complex group structures

## Introduction

The GloBE Information Return (GIR) represents a new compliance obligation requiring electronic submission through tax authority portals across implementing jurisdictions. While each jurisdiction operates its own filing system, the underlying process follows a common pattern established by the OECD framework: registration, preparation, validation, submission, and confirmation.

This section provides the foundational knowledge needed to navigate any jurisdiction's GIR filing portal successfully. Subsequent sections (7.2 onwards) address jurisdiction-specific procedures in detail.

**Key Point:** The OECD GIR XML Schema (v1.0, January 2025) provides a standardised technical format used both for domestic filings and for automatic exchange of GIR data between tax administrations under the GIR MCAA. Understanding this common foundation enables practitioners to efficiently adapt to any jurisdiction's specific requirements.

---

## 7.1.1 The Universal GIR Filing Process

### Five-Phase Filing Framework

Regardless of jurisdiction, GIR filing follows a consistent five-phase process:

```
Universal GIR Filing Process:
│
├── PHASE 1: REGISTRATION (Pre-Filing)
│   ├── Determine filing obligation (in-scope assessment)
│   ├── Identify filing entity (UPE or DFE)
│   ├── Register with tax authority portal
│   ├── Obtain unique identifier/reference number
│   ├── Configure authorised users
│   └── Timeline: 2-6 months before first GIR deadline
│
├── PHASE 2: PREPARATION (Data and XML)
│   ├── Complete GIR calculations (using Calculator)
│   ├── Generate GIR XML file per OECD schema
│   ├── Validate XML against schema (Tier 1-2)
│   ├── Perform business rule validation (Tier 3)
│   ├── Obtain internal approvals
│   └── Timeline: 2-4 months before filing deadline
│
├── PHASE 3: SUBMISSION (Portal Upload)
│   ├── Authenticate to filing portal
│   ├── Navigate to GIR submission section
│   ├── Upload validated XML file
│   ├── Complete any supplementary forms/declarations
│   ├── Review pre-submission summary
│   └── Submit and await confirmation
│
├── PHASE 4: CONFIRMATION (Receipt)
│   ├── Receive submission acknowledgement
│   ├── Obtain reference number/receipt
│   ├── Download confirmation documentation
│   ├── Record file hash for integrity verification
│   └── Archive all submission evidence
│
└── PHASE 5: POST-SUBMISSION (Ongoing)
    ├── Monitor for tax authority queries
    ├── Respond to validation errors if rejected
    ├── File amendments if corrections needed
    ├── Coordinate with other jurisdiction filings
    └── Prepare for MCAA data exchange
```

### Timeline Visualisation

For a calendar year-end MNE Group first in scope for FY 2024:

```
GIR Filing Timeline (FY 2024, Calendar Year-End):
│
│ 2024 │        2025                    │     2026        │
│ Dec  │ Jan-Mar   Apr-Jun   Jul-Sep    │ Oct-Dec Jan-Jun │
│──────│──────────────────────────────────────────────────│
│      │                                                   │
│ FY   │ ◆ Registration     ◆ Data      ◆ Preparation     │
│ End  │   Deadline (UK)      Gathering    Complete       │
│      │   30 Jun 2025                                     │
│      │                                                   │
│      │                                           ◆ GIR   │
│      │                                             Due   │
│      │                                          30 Jun   │
│      │                                           2026    │
│──────│───────────────────────────────────────────────────│

Registration Phase: Months 1-6 (January - June 2025)
Preparation Phase: Months 7-15 (July 2025 - March 2026)
Filing Window: Months 16-18 (April - June 2026)
```

### Filing Deadline Calculations

The GIR filing deadline depends on when the MNE Group first comes within scope of the GloBE Rules:

**Standard Deadline Formula:**
```
GIR Deadline = Fiscal Year End + 15 months (standard)
                                + 18 months (first year in scope)
```

**First-Year Extension:** For the first fiscal year a group is in scope, the deadline is extended from 15 months to 18 months after fiscal year end.

**OECD Administrative Guidance (December 2023):** Section 5 provides that the due date for filing and notification obligations shall not be before 30 June 2026, regardless of fiscal year end.

| Fiscal Year End | First-Year Deadline | Standard Deadline (Year 2+) |
|-----------------|--------------------|-----------------------------|
| 31 December 2024 | 30 June 2026 | 31 March 2027 |
| 31 March 2025 | 30 September 2026 | 30 June 2027 |
| 30 June 2025 | 31 December 2026 | 30 September 2027 |
| 30 September 2025 | 31 March 2027 | 31 December 2027 |

---

## 7.1.2 Common Portal Features

### Portal Architecture Overview

While each jurisdiction operates its own portal system, common architectural patterns emerge across implementations:

```
Generic Tax Authority Portal Architecture:
│
├── PUBLIC ZONE (No Authentication)
│   ├── Information pages about GIR requirements
│   ├── Registration instructions and guidance
│   ├── Schema downloads and documentation
│   ├── FAQ and help resources
│   └── Contact information
│
├── AUTHENTICATED ZONE (Login Required)
│   ├── Dashboard / Home screen
│   ├── Account management
│   ├── Filing history
│   ├── Messages from tax authority
│   └── Support ticket system
│
├── SUBMISSION ZONE (Within Authenticated Area)
│   ├── New GIR submission
│   ├── Upload XML file
│   ├── Validation results display
│   ├── Supplementary declarations
│   └── Submit and confirm
│
├── MANAGEMENT ZONE (Within Authenticated Area)
│   ├── View submitted returns
│   ├── Download receipts/confirmations
│   ├── File amendments/corrections
│   ├── View status messages
│   └── Respond to authority queries
│
└── ADMINISTRATION ZONE (Account Settings)
    ├── User management (add/remove authorised users)
    ├── Organisation details
    ├── Notification preferences
    ├── Security settings
    └── Audit log access
```

### Standard Navigation Elements

**Dashboard / Home Screen:**
Most portals present a dashboard upon login showing:
- Outstanding filing obligations with deadlines
- Recent submissions and their status
- Unread messages from the tax authority
- Quick links to common actions

**Filing Section:**
The GIR filing area typically includes:
- "Create New Return" or "New Submission" option
- Fiscal year/period selection
- File upload interface
- Validation status display
- Submission confirmation

**History Section:**
A filing history section generally provides:
- List of all submitted returns
- Status of each submission (Accepted, Rejected, Processing)
- Download links for receipts and confirmations
- Access to submitted XML files for reference

### Common Portal Features Comparison

| Feature | Typical Implementation | Purpose |
|---------|----------------------|---------|
| **XML Upload** | Drag-and-drop or file browser | Submit GIR XML file |
| **Real-Time Validation** | Immediate schema check upon upload | Identify errors before submission |
| **Error Display** | Line-by-line error messages | Diagnose validation failures |
| **Submission Preview** | Summary screen before final submit | Verify correct file and period |
| **Confirmation Receipt** | Downloadable PDF or reference number | Proof of submission |
| **Amendment Function** | "Correct Return" or "File Amendment" | Submit corrections |
| **Message Centre** | Inbox for authority communications | Receive queries and notifications |
| **Audit History** | Log of all actions on account | Track who did what and when |

### Portal Status Terminology

Tax authority portals use various terms to describe submission status. Common terminology includes:

| Status Term | Meaning | Action Required |
|-------------|---------|-----------------|
| **Received** | File uploaded but not yet processed | Wait for processing |
| **Processing** | Validation in progress | Monitor for results |
| **Accepted** | Passed all validation; officially filed | Archive confirmation |
| **Accepted with Warnings** | Filed but minor issues flagged | Review warnings; consider amendment |
| **Rejected** | Failed validation; not filed | Fix errors and resubmit |
| **Pending Payment** | Return accepted; payment outstanding | Make payment by deadline |
| **Under Review** | Selected for additional examination | Respond to any queries |

---

## 7.1.3 Authentication Requirements

### Authentication Methods Across Jurisdictions

Tax authorities employ various authentication mechanisms to secure GIR filing portals:

| Authentication Type | Description | Jurisdictions Using |
|---------------------|-------------|---------------------|
| **Government Gateway** | Centralised government login system | UK, Ireland |
| **Digital Certificate** | PKI-based authentication using X.509 certificates | Germany, France, Italy |
| **eID/National Identity** | National electronic identity systems | Netherlands, Belgium, Nordic countries |
| **Username/Password + MFA** | Traditional login with multi-factor authentication | Australia, Singapore |
| **Tax Authority Portal Account** | Jurisdiction-specific account system | Spain, Canada |
| **Third-Party Identity Provider** | Delegated authentication via approved providers | Various EU countries |

### Multi-Factor Authentication (MFA)

Most jurisdictions require or strongly recommend MFA for GIR filing. Common second factors include:

| Factor Type | Implementation | Considerations |
|-------------|----------------|----------------|
| **SMS Code** | One-time code sent to registered mobile | Phone must be accessible; roaming considerations |
| **Authenticator App** | TOTP via Google Authenticator, Microsoft Authenticator, etc. | Requires app installation; device-independent |
| **Hardware Token** | Physical device generating codes (e.g., RSA SecurID) | Additional cost; token distribution needed |
| **Email Code** | One-time code sent to registered email | Less secure than SMS/app |
| **Biometric** | Fingerprint or facial recognition | Device-dependent |
| **Smart Card** | Physical card with embedded certificate | Requires card reader |

### Agent Access and Authorisation

A critical consideration for tax advisors: **agent authorisation varies significantly by jurisdiction**.

**Agent Access Models:**

| Model | How It Works | Examples |
|-------|--------------|----------|
| **Direct Agent Access** | Tax agent logs in with own credentials; links to client account | Australia (ATO), UK (HMRC Agents) |
| **Client-Granted Access** | Client grants specific permissions to agent account | Netherlands, Ireland |
| **Shared Credentials** | Client provides login credentials to agent (not recommended) | Legacy systems; should avoid |
| **API Access** | Agent uses API with authorised credentials | UK (MTD APIs), developing elsewhere |
| **No Agent Access** | Only client can file; agent prepares file for client to submit | Some systems for initial years |

**UK-Specific Note:** Currently, there isn't agent access available for Pillar 2 registration. The registration must be completed by an authorised individual within the company with appropriate login credentials. This is expected to evolve as the system matures.

### User Management Within Organisations

For corporate filers, managing multiple authorised users is essential:

**Best Practices:**
1. **Primary Contact:** Designate a single primary contact for tax authority communications
2. **Backup Users:** Ensure at least two individuals have filing access
3. **Role Separation:** Where possible, separate "prepare" and "submit" roles
4. **Regular Review:** Quarterly review of user access; remove leavers promptly
5. **Audit Trail:** Enable logging of all user actions for internal audit

**User Role Definitions:**

| Role | Typical Permissions | Use Case |
|------|---------------------|----------|
| **Administrator** | Full access including user management | Tax Director / Manager |
| **Preparer** | Can create and edit returns; cannot submit | Tax Analyst |
| **Submitter** | Can review and submit prepared returns | Tax Manager |
| **Viewer** | Read-only access to filings and status | Finance Director, Auditors |

---

## 7.1.4 Technical Requirements

### Browser Compatibility

Tax authority portals generally support major modern browsers but may have specific requirements:

**Recommended Browser Configuration:**

| Browser | Minimum Version | Notes |
|---------|-----------------|-------|
| **Google Chrome** | Latest 3 versions | Most widely supported |
| **Microsoft Edge** | Latest 3 versions | Chromium-based versions |
| **Mozilla Firefox** | Latest 3 versions | Good support |
| **Apple Safari** | Latest 2 versions | macOS only; limited support on some portals |

**Browser Settings:**
- **JavaScript:** Must be enabled
- **Cookies:** Session cookies must be accepted
- **Pop-up Blocker:** May need exception for portal domain
- **TLS Version:** TLS 1.2 minimum; TLS 1.3 preferred
- **Cache:** Clear cache if experiencing issues after portal updates

**Not Supported:**
- Internet Explorer (all versions)
- Outdated browser versions
- Most mobile browsers (limited support)

### System Requirements

**Workstation Requirements:**

| Component | Minimum | Recommended |
|-----------|---------|-------------|
| **Operating System** | Windows 10, macOS 10.15, recent Linux | Latest OS version |
| **RAM** | 4 GB | 8+ GB |
| **Display** | 1280 x 720 | 1920 x 1080 or higher |
| **Internet** | Stable broadband connection | Low-latency connection |
| **Storage** | Sufficient for XML files (typically <10 MB each) | SSD for performance |

### Digital Certificate Requirements

For jurisdictions requiring certificate-based authentication:

**Certificate Specifications:**

| Attribute | Requirement |
|-----------|-------------|
| **Format** | X.509 v3 |
| **Key Length** | RSA 2048-bit minimum; 4096-bit recommended |
| **Hash Algorithm** | SHA-256 or stronger |
| **Validity** | Within validity period; typically 1-3 years |
| **Issuer** | Approved Certificate Authority for the jurisdiction |
| **Purpose** | Must include Digital Signature and/or Client Authentication |

**Certificate Installation:**

1. **Obtain Certificate:** Request from approved CA or tax authority
2. **Install in Browser:** Import certificate to browser certificate store
3. **Install in OS:** For some portals, install in OS certificate store
4. **Associate with Portal Account:** Link certificate to your filing account
5. **Test Access:** Verify login works before filing deadline

**Common Certificate Issues:**

| Issue | Symptom | Resolution |
|-------|---------|------------|
| Certificate expired | Cannot authenticate | Renew certificate; install new cert |
| Wrong certificate selected | Authentication fails | Select correct certificate during login |
| Certificate not trusted | Browser warning | Ensure CA root certificates are installed |
| Private key not available | Cannot sign | Check certificate installation includes private key |
| Certificate revoked | Access denied | Contact CA; obtain new certificate |

### XML File Size Limits

Portal file upload limits vary by jurisdiction:

| Jurisdiction | Typical Limit | Notes |
|--------------|---------------|-------|
| **UK (HMRC)** | 10 MB | Uncompressed XML |
| **Germany (BZSt)** | 50 MB | May accept compressed |
| **Netherlands** | 25 MB | Uncompressed XML |
| **Ireland** | 20 MB | Per file |
| **Australia** | 20 MB | Per submission |

**Large File Strategies:**
- Ensure efficient XML generation (no unnecessary whitespace)
- Compress if portal accepts compressed uploads
- Split submissions if multiple GIRs required (e.g., for DFE arrangements)
- Contact tax authority if file exceeds limits

### Network and Firewall Considerations

Corporate networks may require configuration for portal access:

**Firewall Requirements:**

| Protocol | Ports | Purpose |
|----------|-------|---------|
| HTTPS | 443 | All portal communications |
| HTTP | 80 | Redirects to HTTPS (may be used) |

**Proxy Configuration:**
- Ensure proxy allows access to government domains
- May need to whitelist specific portal URLs
- Check SSL/TLS inspection compatibility

**Domain Whitelisting Examples:**

| Jurisdiction | Domains to Whitelist |
|--------------|---------------------|
| **UK** | *.service.gov.uk, *.access.service.gov.uk, *.tax.service.gov.uk |
| **Germany** | *.bzst.de, *.elster.de |
| **Netherlands** | *.belastingdienst.nl |
| **Ireland** | *.revenue.ie, *.ros.ie |
| **Australia** | *.ato.gov.au |

---

## 7.1.5 GIR Submission Workflow

### Step-by-Step Generic Submission Process

The following workflow applies across most jurisdictions with minor variations:

```
GIR Submission Workflow:
│
├── Step 1: PREPARE FOR SUBMISSION
│   ├── ☐ Complete GIR calculations
│   ├── ☐ Generate XML file using validated schema
│   ├── ☐ Run schema validation locally (xmllint, XMLSpy, etc.)
│   ├── ☐ Obtain internal approvals
│   ├── ☐ Document file hash (SHA-256)
│   └── ☐ Confirm deadline and jurisdiction requirements
│
├── Step 2: ACCESS PORTAL
│   ├── ☐ Open approved browser
│   ├── ☐ Navigate to filing portal URL
│   ├── ☐ Authenticate using required method
│   ├── ☐ Complete MFA if required
│   └── ☐ Verify correct account/organisation
│
├── Step 3: INITIATE SUBMISSION
│   ├── ☐ Navigate to GIR filing section
│   ├── ☐ Select "New Return" or "Create Submission"
│   ├── ☐ Choose correct fiscal year/period
│   ├── ☐ Select GIR type (Standard, Amendment, etc.)
│   └── ☐ Proceed to upload
│
├── Step 4: UPLOAD XML FILE
│   ├── ☐ Click upload button / drag file
│   ├── ☐ Select validated XML file
│   ├── ☐ Wait for upload to complete
│   ├── ☐ Review portal validation results
│   └── ☐ If errors, correct and re-upload
│
├── Step 5: COMPLETE DECLARATIONS
│   ├── ☐ Review pre-submission summary
│   ├── ☐ Complete any supplementary declarations
│   ├── ☐ Confirm declaration of accuracy
│   ├── ☐ Check contact details are current
│   └── ☐ Proceed to submit
│
├── Step 6: SUBMIT AND CONFIRM
│   ├── ☐ Click final "Submit" button
│   ├── ☐ Wait for submission confirmation
│   ├── ☐ Record reference number
│   ├── ☐ Download receipt/confirmation
│   └── ☐ Save confirmation email if sent
│
└── Step 7: POST-SUBMISSION ACTIONS
    ├── ☐ Save receipt to compliance file
    ├── ☐ Update file register with submission details
    ├── ☐ Notify relevant stakeholders
    ├── ☐ Monitor for authority acknowledgement
    └── ☐ Archive submitted XML with hash verification
```

### Handling Submission Errors

When portal validation fails, follow this diagnostic process:

**Error Triage:**

| Error Type | Immediate Action | Resolution |
|------------|------------------|------------|
| **Schema Validation Error** | Do not resubmit | Fix XML against schema; revalidate locally |
| **Business Rule Error** | Review error details | Correct data in source; regenerate XML |
| **File Format Error** | Check file properties | Ensure UTF-8 encoding, no BOM, correct extension |
| **Authentication Error** | Re-authenticate | Check credentials, certificate, MFA |
| **System Error** | Wait and retry | Portal may be experiencing issues |
| **File Size Error** | Reduce file size | Compress or optimise XML |

**Error Resolution Workflow:**

```
Error Encountered:
│
├── Step 1: Document the Error
│   ├── Screenshot error message
│   ├── Record error code/reference
│   ├── Note timestamp and file details
│   └── Save any error log provided
│
├── Step 2: Categorise the Error
│   ├── Schema error → Local validation issue
│   ├── Business rule error → Data or calculation issue
│   ├── Technical error → Portal or connectivity issue
│   └── Authentication error → Credential or certificate issue
│
├── Step 3: Implement Fix
│   ├── Schema: Correct XML element/attribute/value
│   ├── Business: Revise calculation or data
│   ├── Technical: Try different browser, clear cache, retry later
│   └── Auth: Reset credentials, reinstall certificate
│
├── Step 4: Revalidate Locally
│   ├── Run full schema validation
│   ├── Confirm error resolved
│   ├── Generate new file hash
│   └── Update version log
│
└── Step 5: Reattempt Submission
    ├── Upload corrected file
    ├── Verify successful validation
    ├── Complete submission
    └── Document resolution
```

---

## 7.1.6 Multi-Jurisdiction Coordination

### When Multi-Jurisdiction Filing Applies

MNE Groups may have GIR filing obligations in multiple jurisdictions when:

1. **Local Filing Requirements:** Some jurisdictions require local GIR filing regardless of MCAA exchange
2. **No DFE Election:** Each jurisdiction's CE files locally if no DFE is designated
3. **QDMTT Filing:** Jurisdictions with QDMTT may require separate top-up tax returns
4. **Non-MCAA Jurisdictions:** Jurisdictions not signed to MCAA require direct filing

### Coordination Principles

**Single Source of Truth:**
- All GIR data originates from one GIR Calculator
- XML files for different jurisdictions contain consistent data
- Amendments in one jurisdiction must be coordinated across all

**Filing Sequence Strategy:**
```
Recommended Filing Sequence:
│
├── 1. Primary Filing Jurisdiction (UPE or DFE location)
│   └── File GIR with complete group data
│
├── 2. MCAA Signatory Jurisdictions
│   ├── File ORN/notification that GIR filed elsewhere
│   └── Monitor for MCAA exchange confirmation
│
├── 3. Non-MCAA Jurisdictions
│   └── File full GIR (or jurisdiction-specific return)
│
├── 4. QDMTT Jurisdictions
│   └── File separate top-up tax returns where required
│
└── 5. Cross-Check All Filings
    ├── Verify consistent data across all submissions
    ├── Document any jurisdiction-specific adjustments
    └── Maintain central tracking log
```

---

## 7.1.7 Multi-Jurisdiction Filing Coordination Checklist

**Template Reference:** Use this comprehensive checklist when coordinating GIR filings across multiple jurisdictions.

### Pre-Filing Coordination Checklist

**SECTION A: Obligation Mapping (Complete First)**

| # | Check Item | Jurisdiction 1 | Jurisdiction 2 | Jurisdiction 3 | Jurisdiction 4 |
|---|------------|----------------|----------------|----------------|----------------|
| A1 | Jurisdiction name | _____________ | _____________ | _____________ | _____________ |
| A2 | Filing requirement confirmed (GIR/ORN/Other) | ☐ GIR ☐ ORN ☐ Other | ☐ GIR ☐ ORN ☐ Other | ☐ GIR ☐ ORN ☐ Other | ☐ GIR ☐ ORN ☐ Other |
| A3 | Filing entity identified | _____________ | _____________ | _____________ | _____________ |
| A4 | MCAA signatory status | ☐ Yes ☐ No | ☐ Yes ☐ No | ☐ Yes ☐ No | ☐ Yes ☐ No |
| A5 | Registration completed | ☐ Yes ☐ N/A | ☐ Yes ☐ N/A | ☐ Yes ☐ N/A | ☐ Yes ☐ N/A |
| A6 | Portal access confirmed | ☐ Yes | ☐ Yes | ☐ Yes | ☐ Yes |
| A7 | Filing deadline | ___/___/____ | ___/___/____ | ___/___/____ | ___/___/____ |
| A8 | QDMTT return also required | ☐ Yes ☐ No | ☐ Yes ☐ No | ☐ Yes ☐ No | ☐ Yes ☐ No |

**SECTION B: Primary Filing Preparation**

| # | Check Item | Status | Date | Notes |
|---|------------|--------|------|-------|
| B1 | Primary filing jurisdiction identified | ☐ | | |
| B2 | GIR Calculator completed for full group | ☐ | | |
| B3 | All jurisdictional data validated | ☐ | | |
| B4 | XML file generated (primary) | ☐ | | |
| B5 | Schema validation passed | ☐ | | |
| B6 | Business rule validation passed | ☐ | | |
| B7 | Internal approvals obtained | ☐ | | |
| B8 | File hash recorded (SHA-256) | ☐ | | Hash: __________________ |

**SECTION C: Multi-Jurisdiction XML Preparation**

| # | Check Item | Status | Date | Notes |
|---|------------|--------|------|-------|
| C1 | Secondary jurisdiction requirements documented | ☐ | | |
| C2 | XML files for each jurisdiction prepared | ☐ | | |
| C3 | Consistency verification across all files | ☐ | | |
| C4 | Each XML validated against schema | ☐ | | |
| C5 | File naming convention applied | ☐ | | |
| C6 | All files hashed and recorded | ☐ | | |

**SECTION D: Submission Tracking**

| # | Jurisdiction | Filing Type | Submit Date | Reference # | Status | Confirmed By |
|---|--------------|-------------|-------------|-------------|--------|--------------|
| D1 | ____________ | ☐ GIR ☐ ORN | ___/___/____ | ____________ | ☐ Accepted ☐ Rejected | ____________ |
| D2 | ____________ | ☐ GIR ☐ ORN | ___/___/____ | ____________ | ☐ Accepted ☐ Rejected | ____________ |
| D3 | ____________ | ☐ GIR ☐ ORN | ___/___/____ | ____________ | ☐ Accepted ☐ Rejected | ____________ |
| D4 | ____________ | ☐ GIR ☐ ORN | ___/___/____ | ____________ | ☐ Accepted ☐ Rejected | ____________ |
| D5 | ____________ | ☐ GIR ☐ ORN | ___/___/____ | ____________ | ☐ Accepted ☐ Rejected | ____________ |

**SECTION E: QDMTT Return Tracking (If Applicable)**

| # | Jurisdiction | Return Type | Submit Date | Tax Liability | Payment Date | Reference # |
|---|--------------|-------------|-------------|---------------|--------------|-------------|
| E1 | ____________ | QDMTT | ___/___/____ | €____________ | ___/___/____ | ____________ |
| E2 | ____________ | QDMTT | ___/___/____ | €____________ | ___/___/____ | ____________ |
| E3 | ____________ | QDMTT | ___/___/____ | €____________ | ___/___/____ | ____________ |

**SECTION F: Post-Filing Verification**

| # | Check Item | Status | Date | Verified By |
|---|------------|--------|------|-------------|
| F1 | All primary GIR submissions confirmed accepted | ☐ | | |
| F2 | All ORN/notifications confirmed accepted | ☐ | | |
| F3 | All QDMTT returns submitted and confirmed | ☐ | | |
| F4 | All payments made by deadline | ☐ | | |
| F5 | MCAA exchange confirmed (if trackable) | ☐ | | |
| F6 | Receipts/confirmations archived for all filings | ☐ | | |
| F7 | File register updated | ☐ | | |
| F8 | Internal stakeholders notified of completion | ☐ | | |
| F9 | Any authority queries responded to | ☐ | | |
| F10 | Next year planning notes documented | ☐ | | |

**SECTION G: Amendment Coordination (If Required)**

| # | Check Item | Status | Notes |
|---|------------|--------|-------|
| G1 | Amendment scope identified (which jurisdictions affected) | ☐ | |
| G2 | Corrected XML prepared for each affected jurisdiction | ☐ | |
| G3 | Consistency verified across amended files | ☐ | |
| G4 | Amendment filed in primary jurisdiction first | ☐ | |
| G5 | Secondary jurisdictions notified/amended | ☐ | |
| G6 | All amendment receipts obtained and archived | ☐ | |

---

**Completion Sign-Off:**

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Prepared By | _________________________ | _____________ | ___/___/____ |
| Reviewed By | _________________________ | _____________ | ___/___/____ |
| Approved By | _________________________ | _____________ | ___/___/____ |

---

## 7.1.8 Portal Troubleshooting Guide

### Common Portal Issues and Solutions

| Issue | Symptoms | Likely Cause | Resolution |
|-------|----------|--------------|------------|
| **Cannot log in** | Authentication fails | Wrong credentials, expired password, certificate issue | Reset password; reinstall certificate; contact helpdesk |
| **Session timeout** | Logged out unexpectedly | Inactivity; session expired | Re-authenticate; work in shorter sessions |
| **Page not loading** | Blank screen, error message | Browser compatibility, network issue | Try different browser; check network; clear cache |
| **Upload fails** | File not accepted | File too large, wrong format, network interruption | Check file size; verify .xml extension; retry |
| **Validation takes too long** | Stuck on "Processing" | Large file, server busy | Wait 10-15 minutes; retry during off-peak hours |
| **Cannot find GIR section** | Section not visible | Account not registered for GIR; wrong portal section | Complete registration; navigate to correct area |
| **Error after submission** | Rejection notification | Schema or business rule failure | Review error details; fix and resubmit |
| **No confirmation received** | No receipt after submit | Submission incomplete; email issue | Check submission history; verify email settings |

### Portal Support Contacts

When issues cannot be resolved through troubleshooting, contact the relevant tax authority support:

| Jurisdiction | Support Channel | Hours | Notes |
|--------------|-----------------|-------|-------|
| **UK (HMRC)** | Online helpdesk via portal; Phone lines available | Mon-Fri 08:30-17:00 | Pillar 2 specific support available |
| **Germany (BZSt)** | Support form via BZSt portal | Business hours | German language primary |
| **Netherlands** | Belastingdienst helpline | Mon-Fri 08:00-17:00 | English support available |
| **Ireland** | ROS technical support | Mon-Fri 09:30-17:00 | Pillar Two Hub launched Aug 2025 |
| **Australia** | ATO Business Portal support | Mon-Fri 08:00-18:00 | Local time zones |

---

## Practice This Skill: GIR Filing Deadline Calculator

Understanding filing deadlines is critical for compliance. Practice using the **GIR Filing Deadline Calculator (GIR-005)** on tools.mojitax.com.

| Tool | Tool ID | Purpose |
|------|---------|---------|
| GIR Filing Deadline Calculator | GIR-005 | Determine GIR filing deadlines based on fiscal year end and jurisdiction |

**Demo Tool vs Professional Tool**

This is a demo tool for learning purposes. In professional practice, you would use compliance management software that tracks deadlines across all jurisdictions with automated reminders. The demo tool helps you understand deadline rules.

**To Practice:**

1. Go to tools.mojitax.com and find **GIR Filing Deadline Calculator**
2. Use the GlobalTech data from **Case Study 1**:
   - Fiscal Year End: 31 December 2024
   - Filing Jurisdiction: United Kingdom
   - First Filing Year: Yes
3. Enter the values and calculate
4. **Expected Results:**
   - Standard Deadline: 31 March 2026 (15 months from FYE)
   - First Year Extension: 30 June 2026 (18 months available)
   - Recommended milestones for preparation

If your results differ, review the deadline rules earlier in this section.

---

## Summary

This section has provided comprehensive guidance on the universal GIR filing process and portal navigation, covering:

1. **Five-Phase Filing Framework**
   - Registration, Preparation, Submission, Confirmation, Post-Submission
   - Timeline visualisation for calendar year-end groups
   - Filing deadline calculations

2. **Common Portal Features**
   - Standard portal architecture and navigation patterns
   - Status terminology and feature comparison
   - What to expect across different jurisdiction portals

3. **Authentication Requirements**
   - Authentication methods by jurisdiction
   - Multi-factor authentication considerations
   - Agent access models and user management

4. **Technical Requirements**
   - Browser compatibility and settings
   - System and certificate requirements
   - Network and firewall considerations

5. **GIR Submission Workflow**
   - Step-by-step submission process
   - Error handling and resolution

6. **Multi-Jurisdiction Coordination**
   - When multi-jurisdiction filing applies
   - Coordination principles and filing sequence
   - Comprehensive Multi-Jurisdiction Filing Coordination Checklist

**Key Takeaway:** While each jurisdiction operates its own filing portal, the underlying process follows a common pattern. Mastering the universal framework in this section provides the foundation to efficiently navigate any jurisdiction's specific requirements covered in subsequent sections.

---

## References and Resources

### OECD Resources
- [GloBE Information Return (January 2025)](https://www.oecd.org/en/publications/tax-challenges-arising-from-the-digitalisation-of-the-economy-globe-information-return-january-2025_a05ec99a-en.html) - Official OECD GIR specification
- [GIR XML Schema (January 2025)](https://www.oecd.org/en/publications/2025/01/globe-information-return-pillar-two-xml-schema_3980638f.html) - XML schema and user guide
- [Pillar Two Administration](https://oecdpillars.com/pillar-tab/pillar-two-administration/) - Administrative guidance overview
- [Pillar Two Domestic Registration Requirements](https://oecdpillars.com/pillar-two-domestic-registration-requirements/) - Registration tracker

### Jurisdiction Portal Links
- [UK: Report Pillar 2 top-up taxes](https://www.gov.uk/guidance/report-pillar-2-top-up-taxes) - HMRC filing portal
- [Germany: BZSt Pillar 2](https://www.bzst.de/EN/Businesses/Pillar_2/Procedure/procedure_node.html) - German federal tax office
- [Ireland: Pillar Two Hub](https://www.revenue.ie/) - Irish Revenue portal
- [Australia: ATO](https://www.ato.gov.au/) - Australian Taxation Office

### Professional Guidance
- [ICAEW: HMRC reminds groups of Pillar 2 requirements](https://www.icaew.com/insights/tax-news/2025/apr-2025/hmrc-reminds-groups-of-pillar-2-requirements) - UK registration guidance
- [PwC: Upcoming Pillar Two registration and notification deadlines](https://www.pwc.com/us/en/services/tax/library/upcoming-pillar-two-registration-and-notification-deadlines.html) - Global deadline tracker
- [BDO: Pillar Two Quarterly Update](https://www.bdo.global/en-gb/insights/tax/world-wide-tax/international-pillar-two-quarterly-update-(1-august-%E2%80%93-11-november-2025)) - Latest developments

---

## Section Progress

| Subsection | Status | Page Estimate |
|------------|--------|---------------|
| 7.1.1 The Universal GIR Filing Process | Complete | 2 pages |
| 7.1.2 Common Portal Features | Complete | 2 pages |
| 7.1.3 Authentication Requirements | Complete | 2 pages |
| 7.1.4 Technical Requirements | Complete | 2 pages |
| 7.1.5 GIR Submission Workflow | Complete | 2 pages |
| 7.1.6 Multi-Jurisdiction Coordination | Complete | 1 page |
| 7.1.7 Multi-Jurisdiction Filing Coordination Checklist | Complete | 2 pages |
| 7.1.8 Portal Troubleshooting Guide | Complete | 1 page |
| **Total** | **Complete** | **14 pages** |

*Target: 12-15 pages | Achieved: ~14 pages*

---

## Navigation

**Previous:** [Section 6.4: XML File Management](Section_06_04_XML_File_Management.md)

**Next:** [Section 7.2: United Kingdom](Section_07_02_United_Kingdom.md)

**Return to:** [Table of Contents](00_Table_of_Contents.md)
