# Section 6.4: XML File Management

## Introduction

Effective management of GIR XML files is essential for ongoing compliance, audit readiness, and operational efficiency. With filing deadlines spanning multiple years and potential examination periods extending well beyond, organisations must establish robust file naming conventions, version control procedures, and archival practices.

This section provides comprehensive guidance for managing GIR XML files throughout their lifecycle—from initial generation through long-term retention and potential amendment.

**Learning Objectives:**
- Implement standardised file naming conventions for GIR files
- Establish version control procedures for iterative development
- Configure secure storage and archival systems
- Manage amended returns and resubmissions
- Maintain audit-ready documentation and access controls

---

## 6.4.1 File Naming Conventions

### Importance of Consistent Naming

A well-designed file naming convention ensures:

```
Benefits of Standardised Naming:
├── Quick identification of file contents
├── Logical sorting and retrieval
├── Clear version history
├── Prevention of accidental overwrites
├── Audit trail maintenance
└── Team-wide consistency
```

### GIR File Naming Standard

**Recommended Format:**

```
[MNEGroup]_GIR_[FiscalYear]_[Jurisdiction]_[Version]_[Date].[Extension]

Components:
├── MNEGroup: Short identifier for MNE Group (max 20 chars)
├── GIR: Fixed identifier for GloBE Information Return
├── FiscalYear: Reporting year (YYYY)
├── Jurisdiction: Filing jurisdiction (ISO 3166-1 alpha-2)
├── Version: Version number (v01, v02, etc.)
├── Date: File creation date (YYYYMMDD)
└── Extension: File type (.xml, .xlsx, .pdf)
```

**Examples:**

| Scenario | File Name |
|----------|-----------|
| Initial UK filing for 2024 | `GlobalCo_GIR_2024_GB_v01_20250615.xml` |
| Revised version after review | `GlobalCo_GIR_2024_GB_v02_20250618.xml` |
| Final submitted version | `GlobalCo_GIR_2024_GB_v03_FINAL_20250620.xml` |
| Amended return | `GlobalCo_GIR_2024_GB_AMD01_20250815.xml` |
| German local filing | `GlobalCo_GIR_2024_DE_v01_20250625.xml` |

### Supporting File Naming

| File Type | Naming Convention | Example |
|-----------|------------------|---------|
| Calculator workbook | `[MNE]_GIRCalc_[FY]_v[##]_[Date].xlsx` | `GlobalCo_GIRCalc_2024_v05_20250615.xlsx` |
| Validation log | `[MNE]_GIR_[FY]_ValLog_[Date].pdf` | `GlobalCo_GIR_2024_ValLog_20250618.pdf` |
| Reconciliation | `[MNE]_GIR_[FY]_Recon_[Date].xlsx` | `GlobalCo_GIR_2024_Recon_20250615.xlsx` |
| Sign-off memo | `[MNE]_GIR_[FY]_SignOff_[Date].pdf` | `GlobalCo_GIR_2024_SignOff_20250620.pdf` |
| Tax authority receipt | `[MNE]_GIR_[FY]_[Jur]_Receipt_[Date].pdf` | `GlobalCo_GIR_2024_GB_Receipt_20250620.pdf` |

### Characters to Avoid

```
Avoid in File Names:
├── Spaces → Use underscores (_) instead
├── Special characters: / \ : * ? " < > |
├── Accented characters: é, ñ, ü
├── Leading/trailing spaces
├── Consecutive underscores
└── Excessively long names (>80 characters)
```

---

## 6.4.2 Version Control

### Version Control Framework

```
Version Control Lifecycle:
│
├── Development Phase (v01, v02, v03...)
│   ├── Initial data entry
│   ├── Iterative refinement
│   ├── Review and correction
│   └── Each save = new version
│
├── Review Phase (v##_REVIEW)
│   ├── Sent for independent review
│   ├── Comments incorporated
│   └── Tax director review
│
├── Final Phase (v##_FINAL)
│   ├── All approvals obtained
│   ├── Ready for submission
│   └── No further changes
│
├── Submitted Phase (v##_SUBMITTED)
│   ├── File submitted to authority
│   ├── Timestamp recorded
│   └── Receipt obtained
│
└── Amended Phase (AMD01, AMD02...)
    ├── Post-submission corrections
    ├── New amendment number per submission
    └── Links to original submission
```

### Version Numbering Rules

| Version Type | Format | When Used |
|--------------|--------|-----------|
| Development | v01, v02, v03... | Each significant save during preparation |
| Review | v05_REVIEW | Sent for independent review |
| Approved | v07_APPROVED | Tax director approval obtained |
| Final | v08_FINAL | Ready for submission |
| Submitted | v08_FINAL_SUBMITTED | After successful submission |
| Amendment 1 | AMD01_v01 | First correction after submission |
| Amendment 2 | AMD02_v01 | Second correction after submission |

### Version Log Template

**Tab:** `Version Log`

| Version | Date | Author | Description | Status | Reviewer |
|---------|------|--------|-------------|--------|----------|
| v01 | 2025-06-01 | [Name] | Initial data entry | Draft | - |
| v02 | 2025-06-05 | [Name] | Section 1 completed | Draft | - |
| v03 | 2025-06-10 | [Name] | All sections completed | Draft | - |
| v04 | 2025-06-12 | [Name] | Validation errors fixed | Draft | - |
| v05_REVIEW | 2025-06-14 | [Name] | Sent for review | Review | [Reviewer] |
| v06 | 2025-06-16 | [Name] | Review comments addressed | Draft | - |
| v07_APPROVED | 2025-06-18 | [Name] | Tax director approved | Approved | [Director] |
| v08_FINAL | 2025-06-19 | [Name] | Final version for submission | Final | - |
| v08_SUBMITTED | 2025-06-20 | [Name] | Submitted to HMRC | Submitted | - |

### Version Control Best Practices

```
Version Control Guidelines:
│
├── Always Work on Latest Version
│   ├── Check version log before editing
│   ├── Never edit archived versions
│   └── Create new version for changes
│
├── Document All Changes
│   ├── Brief description in version log
│   ├── Note reviewer if applicable
│   └── Include timestamp
│
├── Maintain Clear Status
│   ├── Draft/Review/Final/Submitted
│   ├── Update status immediately
│   └── No ambiguous states
│
├── Lock Final Versions
│   ├── Mark files as read-only
│   ├── Move to separate folder
│   └── Prevent accidental changes
│
└── Use Version Control Software
    ├── Git for technical teams
    ├── SharePoint versioning
    └── Document management systems
```

---

## 6.4.3 Folder Structure

### Recommended Directory Structure

```
GIR_Files/
├── 2024/                              # Fiscal Year
│   ├── Calculator/
│   │   ├── GlobalCo_GIRCalc_2024_v01_20250601.xlsx
│   │   ├── GlobalCo_GIRCalc_2024_v02_20250605.xlsx
│   │   └── GlobalCo_GIRCalc_2024_v08_FINAL_20250619.xlsx
│   │
│   ├── XML/
│   │   ├── Development/
│   │   │   ├── GlobalCo_GIR_2024_GB_v01_20250615.xml
│   │   │   └── GlobalCo_GIR_2024_GB_v02_20250618.xml
│   │   │
│   │   ├── Final/
│   │   │   └── GlobalCo_GIR_2024_GB_v03_FINAL_20250620.xml
│   │   │
│   │   └── Submitted/
│   │       └── GlobalCo_GIR_2024_GB_v03_FINAL_SUBMITTED_20250620.xml
│   │
│   ├── Validation/
│   │   ├── GlobalCo_GIR_2024_ValLog_20250618.pdf
│   │   └── GlobalCo_GIR_2024_SchemaVal_20250619.txt
│   │
│   ├── Reconciliation/
│   │   ├── GlobalCo_GIR_2024_Recon_FS_20250615.xlsx
│   │   ├── GlobalCo_GIR_2024_Recon_TaxProv_20250616.xlsx
│   │   └── GlobalCo_GIR_2024_Recon_CbCR_20250617.xlsx
│   │
│   ├── Approvals/
│   │   ├── GlobalCo_GIR_2024_SignOff_20250620.pdf
│   │   └── GlobalCo_GIR_2024_TaxDirectorApproval_20250619.pdf
│   │
│   ├── Submissions/
│   │   ├── GB/
│   │   │   ├── GlobalCo_GIR_2024_GB_Receipt_20250620.pdf
│   │   │   └── GlobalCo_GIR_2024_GB_Confirmation_20250620.pdf
│   │   │
│   │   └── DE/
│   │       ├── GlobalCo_GIR_2024_DE_Receipt_20250625.pdf
│   │       └── GlobalCo_GIR_2024_DE_Confirmation_20250625.pdf
│   │
│   ├── Amendments/
│   │   └── AMD01/
│   │       ├── GlobalCo_GIR_2024_GB_AMD01_v01_20250815.xml
│   │       └── GlobalCo_GIR_2024_AMD01_Explanation_20250815.pdf
│   │
│   └── Supporting_Documentation/
│       ├── DataExtracts/
│       ├── WorkPapers/
│       └── Correspondence/
│
├── 2025/
│   └── [Similar structure]
│
├── Templates/
│   ├── GIR_Calculator_Template_v1.xlsx
│   └── README.txt
│
└── Schemas/
    ├── GIR_v1.0.xsd
    └── CommonTypes_v1.0.xsd
```

### Access Controls

| Folder | Access Level | Who |
|--------|-------------|-----|
| Calculator/ | Read-Write | Tax team |
| XML/Development/ | Read-Write | Tax team |
| XML/Final/ | Read-Only (after approval) | All |
| XML/Submitted/ | Read-Only | All |
| Approvals/ | Read-Write (approvers) | Tax director, reviewers |
| Submissions/ | Read-Only | All |
| Amendments/ | Read-Write | Tax team |
| Schemas/ | Read-Only | All |

---

## 6.4.4 Storage and Security

### Storage Requirements

```
GIR File Storage Requirements:
│
├── Primary Storage
│   ├── Network shared drive or cloud storage
│   ├── Automatic backup enabled
│   ├── Access-controlled
│   └── Encrypted at rest
│
├── Backup Strategy
│   ├── Daily incremental backups
│   ├── Weekly full backups
│   ├── Monthly archive snapshots
│   ├── Off-site/cloud backup
│   └── Regular restore testing
│
└── Disaster Recovery
    ├── Recovery Point Objective (RPO): 24 hours
    ├── Recovery Time Objective (RTO): 4 hours
    ├── Documented recovery procedures
    └── Annual DR testing
```

### Security Controls

| Control | Implementation | Purpose |
|---------|---------------|---------|
| **Access Control** | Role-based permissions | Limit access to authorised users |
| **Encryption** | AES-256 at rest, TLS in transit | Protect sensitive tax data |
| **Audit Logging** | File access and modification logs | Track all file activity |
| **Version Protection** | Read-only flag on final versions | Prevent unauthorised changes |
| **Integrity Checks** | Hash values for submitted files | Detect tampering |
| **Multi-Factor Auth** | MFA for storage access | Enhanced authentication |

### Hash Value Recording

For audit purposes, record cryptographic hashes of submitted files:

```
Hash Value Record:

File: GlobalCo_GIR_2024_GB_v03_FINAL_SUBMITTED_20250620.xml
SHA-256: 9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08
MD5: 098f6bcd4621d373cade4e832627b4f6
Generated: 2025-06-20 14:30:00 UTC
Generated By: [Name]
Submission Reference: HMRC-GIR-2024-GB-000123
```

**PowerShell Command:**
```powershell
Get-FileHash -Path "GlobalCo_GIR_2024_GB_v03_FINAL_SUBMITTED_20250620.xml" -Algorithm SHA256
```

**Bash Command:**
```bash
sha256sum GlobalCo_GIR_2024_GB_v03_FINAL_SUBMITTED_20250620.xml
```

---

## 6.4.5 Retention Requirements

### Minimum Retention Periods

```
GIR Document Retention:
│
├── Primary GIR Files
│   ├── Submitted XML files: 10 years minimum
│   ├── Calculator workbooks: 10 years minimum
│   ├── Validation logs: 10 years minimum
│   └── Submission receipts: 10 years minimum
│
├── Supporting Documentation
│   ├── Source data extracts: 10 years
│   ├── Reconciliation workpapers: 10 years
│   ├── Approval documentation: 10 years
│   └── Correspondence: 10 years
│
├── Working Papers (Optional)
│   ├── Draft versions: 3 years after final
│   ├── Review comments: 3 years after final
│   └── Internal memos: 3 years after final
│
└── Jurisdiction-Specific
    ├── May vary by country
    ├── Longest applicable period controls
    └── Consult local regulations
```

### Retention Period Calculation

```
Retention Start Date:
├── For annual GIR: Later of filing date or filing deadline
├── For amended GIR: Date of amendment submission
│
├── Example (Calendar Year MNE):
│   ├── FY 2024 GIR filed: 20 June 2025
│   ├── Filing deadline: 30 June 2026 (18-month first year)
│   ├── Retention starts: 30 June 2026
│   ├── 10-year retention ends: 30 June 2036
│   └── Safe destruction date: 1 July 2036
```

### Retention Schedule Template

| Document Type | FY 2024 | Retention End | Destruction Date |
|---------------|---------|---------------|------------------|
| GIR XML (submitted) | 20 Jun 2025 | 30 Jun 2036 | 1 Jul 2036 |
| Calculator | 19 Jun 2025 | 30 Jun 2036 | 1 Jul 2036 |
| Validation Log | 20 Jun 2025 | 30 Jun 2036 | 1 Jul 2036 |
| Reconciliations | 18 Jun 2025 | 30 Jun 2036 | 1 Jul 2036 |
| Sign-off Memo | 20 Jun 2025 | 30 Jun 2036 | 1 Jul 2036 |
| Draft Versions | 15 Jun 2025 | 30 Jun 2029 | 1 Jul 2029 |

---

## 6.4.6 Amendment Management

### Amendment Triggers

```
When to Amend a GIR:
│
├── Material Errors Discovered
│   ├── Mathematical errors in calculations
│   ├── Incorrect data from source systems
│   ├── Misclassification of entities
│   └── Wrong jurisdiction assignments
│
├── Post-Filing Events
│   ├── Tax audit adjustments
│   ├── Transfer pricing corrections
│   ├── Amended financial statements
│   └── M&A transaction adjustments
│
├── Omissions Identified
│   ├── Missing Constituent Entities
│   ├── Undisclosed jurisdictions
│   └── Incomplete safe harbour elections
│
└── Regulatory Requirements
    ├── Tax authority request
    ├── New guidance affecting prior filings
    └── Legislative clarifications
```

### Amendment Procedure

**Step 1: Assess Materiality**

| Factor | Threshold | Action |
|--------|-----------|--------|
| Top-up Tax impact | > €50,000 | Amendment recommended |
| Percentage of total | > 5% | Amendment recommended |
| Collection mechanism change | Any | Amendment required |
| Jurisdictional change | Any | Amendment likely required |
| Entity count change | > 10% | Amendment recommended |

**Step 2: Prepare Amendment**

```
Amendment Preparation Checklist:
☐ Document error/change identified
☐ Calculate correct values
☐ Update Calculator with corrections
☐ Run full validation suite
☐ Generate new XML with amendment indicator
☐ Prepare amendment explanation memo
☐ Obtain required approvals
```

**Step 3: XML Amendment Indicator**

```xml
<!-- In the GIR XML, set the Amended indicator -->
<globe:FilingInfo>
    <globe:AmendedReturn>true</globe:AmendedReturn>
    <globe:OriginalMessageRefId>GB2024GIR000001</globe:OriginalMessageRefId>
    <!-- Other elements... -->
</globe:FilingInfo>
```

**Step 4: Submit and Document**

```
Amendment Submission Package:
├── Amended XML file (AMD## version)
├── Amendment explanation memo
├── Comparison showing changes
├── Supporting documentation
├── Tax authority submission receipt
└── Updated retention schedule
```

### Amendment Tracking Log

| AMD # | Discovery Date | Error Description | Impact (€) | Filed Date | Authority | Status |
|-------|---------------|-------------------|------------|------------|-----------|--------|
| AMD01 | 2025-08-10 | ETR calculation error DE | +125,000 | 2025-08-15 | HMRC | Accepted |
| AMD02 | 2025-11-20 | Missing CE in France | +45,000 | 2025-11-25 | HMRC | Pending |

---

## 6.4.7 Archival Procedures

### Archive Preparation

```
Annual Archive Package (per FY):
│
├── Submitted Files
│   ├── Final XML files (all jurisdictions)
│   ├── Submission receipts
│   └── Authority confirmations
│
├── Working Files
│   ├── Final Calculator version
│   ├── Final validation logs
│   └── Reconciliation workbooks
│
├── Approvals
│   ├── Sign-off documentation
│   ├── Review notes
│   └── Tax director approval
│
├── Supporting Documentation
│   ├── Source data extracts
│   ├── Key working papers
│   └── Correspondence
│
├── Amendments (if any)
│   ├── All amendment packages
│   └── Amendment tracking log
│
└── Index
    ├── README.txt with contents
    ├── File inventory spreadsheet
    └── Retention schedule
```

### Archive Format

| Archive Type | Format | Use Case |
|--------------|--------|----------|
| **Active Archive** | Original files on shared drive | Years 1-3, frequent access |
| **Cold Archive** | Compressed ZIP with integrity check | Years 4-7, occasional access |
| **Long-term Archive** | Encrypted archive with metadata | Years 8+, rare access |

### Archive Integrity

```bash
# Create archive with integrity verification
# Linux/Mac
tar -cvf GlobalCo_GIR_2024_Archive.tar GIR_Files/2024/
gzip GlobalCo_GIR_2024_Archive.tar
sha256sum GlobalCo_GIR_2024_Archive.tar.gz > GlobalCo_GIR_2024_Archive.sha256

# Windows PowerShell
Compress-Archive -Path "GIR_Files\2024\*" -DestinationPath "GlobalCo_GIR_2024_Archive.zip"
Get-FileHash -Path "GlobalCo_GIR_2024_Archive.zip" -Algorithm SHA256 | Out-File "GlobalCo_GIR_2024_Archive.sha256"
```

### Archive Verification

Periodically verify archive integrity:

```bash
# Verify archive integrity
sha256sum -c GlobalCo_GIR_2024_Archive.sha256

# Expected output:
# GlobalCo_GIR_2024_Archive.tar.gz: OK
```

---

## 6.4.8 Multi-Jurisdiction Coordination

### Central vs. Local Filing

```
GIR Filing Approaches:
│
├── Centralised Filing
│   ├── Single FCE files for entire group
│   ├── Designates Filing Entity per jurisdiction
│   ├── Central XML generation
│   └── Coordinated submission timeline
│
└── Decentralised Filing
    ├── Local entities file individually
    ├── Local XML generation
    ├── Local submission
    └── Central consolidation for records
```

### Multi-Jurisdiction File Management

| Jurisdiction | FCE | Filing Due | File Location | Status |
|--------------|-----|------------|---------------|--------|
| UK (HMRC) | GlobalCo Holdings plc | 30 Jun 2026 | /2024/Submissions/GB/ | Filed |
| Germany (BZSt) | GlobalCo Holdings plc | 30 Jun 2026 | /2024/Submissions/DE/ | Filed |
| France (DGFiP) | GlobalCo France SARL | 30 Jun 2026 | /2024/Submissions/FR/ | Pending |
| Ireland (Revenue) | GlobalCo Holdings plc | 30 Jun 2026 | /2024/Submissions/IE/ | Filed |
| Netherlands (Belastingdienst) | GlobalCo Holdings plc | 30 Jun 2026 | /2024/Submissions/NL/ | Pending |

### Coordination Checklist

```
Multi-Jurisdiction Filing Checklist:
☐ Identify all filing jurisdictions
☐ Confirm FCE/DFE designations
☐ Map filing deadlines
☐ Generate jurisdiction-specific XML (if required)
☐ Coordinate local filing requirements
☐ Track submission status per jurisdiction
☐ Collect all receipts/confirmations
☐ Archive by jurisdiction
☐ Consolidate records centrally
```

---

## 6.4.9 File Management Checklist

Use this checklist for comprehensive file management:

**Naming and Structure:**

| # | Check Item | Status |
|---|------------|--------|
| 1 | File naming convention documented | ☐ |
| 2 | Folder structure established | ☐ |
| 3 | All files named consistently | ☐ |
| 4 | Version numbering applied | ☐ |
| 5 | Status indicators used (DRAFT/FINAL/etc.) | ☐ |

**Version Control:**

| # | Check Item | Status |
|---|------------|--------|
| 6 | Version log maintained | ☐ |
| 7 | Change descriptions recorded | ☐ |
| 8 | Final versions locked (read-only) | ☐ |
| 9 | Submitted versions archived | ☐ |
| 10 | Amendment versions tracked | ☐ |

**Storage and Security:**

| # | Check Item | Status |
|---|------------|--------|
| 11 | Files stored on approved location | ☐ |
| 12 | Access controls configured | ☐ |
| 13 | Encryption enabled | ☐ |
| 14 | Backup verified | ☐ |
| 15 | Hash values recorded for submitted files | ☐ |

**Retention:**

| # | Check Item | Status |
|---|------------|--------|
| 16 | Retention periods documented | ☐ |
| 17 | Retention end dates calculated | ☐ |
| 18 | Archive schedule established | ☐ |
| 19 | Destruction dates recorded | ☐ |

**Documentation:**

| # | Check Item | Status |
|---|------------|--------|
| 20 | README file in each folder | ☐ |
| 21 | File inventory maintained | ☐ |
| 22 | Submission receipts filed | ☐ |
| 23 | Amendment log current | ☐ |
| 24 | Audit trail complete | ☐ |

---

## 6.4.10 Key Takeaways

### File Management Best Practices

1. **Consistency is Critical**
   - Establish naming conventions before first filing
   - Document standards in README files
   - Train all team members on conventions

2. **Version Control Prevents Errors**
   - Always create new version for changes
   - Lock final versions after submission
   - Never edit archived files directly

3. **Secure Storage Protects Data**
   - Use encrypted, access-controlled storage
   - Implement regular backup procedures
   - Record integrity hashes for submitted files

4. **Retention Supports Audit Readiness**
   - Plan for 10+ year retention
   - Calculate retention dates at filing
   - Establish archive procedures early

5. **Amendments Need Process**
   - Document amendment triggers and thresholds
   - Track all amendments in central log
   - Maintain complete amendment packages

---

## Section Summary

Effective XML file management ensures compliance readiness and operational efficiency. Key requirements include:

- **Naming Conventions:** Standardised format with MNE, FY, jurisdiction, version, date
- **Version Control:** Clear progression from draft to submitted with version log
- **Folder Structure:** Organised hierarchy by year, type, and jurisdiction
- **Security:** Encryption, access controls, hash values for integrity
- **Retention:** 10-year minimum with calculated end dates
- **Amendments:** Documented procedures with tracking log

Proper file management from the first filing establishes a foundation for multi-year GIR compliance.

---

## Navigation

**Previous:** [Section 6.3: XML Validation Procedures](Section_06_03_XML_Validation_Procedures.md)

**Next:** [Section 7: Filing and Submission](Section_07_Filing_and_Submission.md)

**Return to:** [Table of Contents](00_Table_of_Contents.md)
