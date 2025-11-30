# Section 6.4: XML File Management

## Learning Objectives

By the end of this section, you will be able to:
- Implement standardised file naming conventions for GIR XML files and supporting documentation
- Establish robust version control procedures throughout the GIR preparation lifecycle
- Configure secure storage with appropriate backup and disaster recovery procedures
- Design and enforce access controls aligned with data protection requirements
- Maintain comprehensive audit trails for regulatory compliance and examination readiness
- Use the XML File Register template to document all GIR files systematically

## Introduction

Effective management of GIR XML files is essential for ongoing compliance, audit readiness, and operational efficiency. With filing deadlines spanning multiple years and potential examination periods extending well beyond initial submission, organisations must establish robust file naming conventions, version control procedures, and archival practices that meet both regulatory requirements and practical operational needs.

This section provides comprehensive guidance for managing GIR XML files throughout their entire lifecycle—from initial generation through long-term retention and potential amendment. The approach aligns with ISO 15489 records management principles while addressing specific requirements of tax compliance documentation.

**Key Principle:** The GIR contains detailed financial information for Constituent Entities across multiple jurisdictions. Proper file management is not merely administrative convenience—it is a fundamental compliance requirement that supports audit defence, amendment tracking, and multi-year consistency in Pillar Two reporting.

---

## 6.4.1 File Storage and Version Control

### Storage Architecture Requirements

GIR file storage must address several key requirements simultaneously:

```
GIR Storage Requirements Framework:
│
├── Availability
│   ├── Files accessible to authorised users
│   ├── Multiple geographic locations (for multi-jurisdictional groups)
│   ├── Offline access capabilities for travel/remote work
│   └── Service level: 99.9% uptime minimum
│
├── Integrity
│   ├── Prevention of accidental modification
│   ├── Detection of unauthorised changes
│   ├── Cryptographic verification (checksums)
│   └── Audit logging of all access
│
├── Confidentiality
│   ├── Encryption at rest (AES-256 minimum)
│   ├── Encryption in transit (TLS 1.3)
│   ├── Access restricted to authorised personnel
│   └── Data classification: Highly Confidential
│
└── Retention
    ├── Minimum 10-year retention capability
    ├── Format migration support (XML longevity)
    ├── Media refresh procedures
    └── Legal hold capabilities
```

### Recommended Storage Platforms

| Platform Type | Examples | Strengths | Considerations |
|---------------|----------|-----------|----------------|
| **Enterprise Cloud** | SharePoint, OneDrive for Business, Google Workspace | Built-in versioning, access controls, audit logs | Data residency compliance |
| **Document Management System** | OpenText, M-Files, Documentum | Robust metadata, workflow, retention | Higher cost, implementation time |
| **Network File Shares** | Windows Server, NAS appliances | Familiar, cost-effective | Manual versioning, limited audit |
| **Specialist Tax Platforms** | Thomson Reuters ONESOURCE, Vertex | Tax-specific features, compliance focus | Vendor lock-in risk |

**Recommended Approach:** Enterprise cloud storage (SharePoint/OneDrive) with supplementary document management for organisations without specialist tax platforms. This provides automatic versioning, access controls, and audit logs while remaining cost-effective.

### File Naming Conventions

A well-designed file naming convention ensures quick identification, logical sorting, and clear version history.

**GIR XML File Naming Standard:**

```
[MNEGroup]_GIR_[FiscalYear]_[Jurisdiction]_[Version]_[Date].[Extension]

Components:
├── MNEGroup: Short identifier for MNE Group (max 20 chars, no spaces)
├── GIR: Fixed identifier for GloBE Information Return
├── FiscalYear: Reporting year (YYYY)
├── Jurisdiction: Filing jurisdiction (ISO 3166-1 alpha-2)
├── Version: Version number (v01, v02, etc.) or status (FINAL, SUBMITTED)
├── Date: File creation/modification date (YYYYMMDD)
└── Extension: File type (.xml)
```

**Examples:**

| Scenario | File Name |
|----------|-----------|
| Initial UK filing draft | `GlobalCo_GIR_2024_GB_v01_20250601.xml` |
| Second draft after corrections | `GlobalCo_GIR_2024_GB_v02_20250605.xml` |
| Review version | `GlobalCo_GIR_2024_GB_v05_REVIEW_20250610.xml` |
| Final approved version | `GlobalCo_GIR_2024_GB_v08_FINAL_20250618.xml` |
| Submitted version | `GlobalCo_GIR_2024_GB_v08_SUBMITTED_20250620.xml` |
| First amendment | `GlobalCo_GIR_2024_GB_AMD01_v01_20250815.xml` |
| German local filing | `GlobalCo_GIR_2024_DE_v01_20250625.xml` |

**Supporting Documentation Naming:**

| Document Type | Naming Convention | Example |
|---------------|-------------------|---------|
| Calculator workbook | `[MNE]_GIRCalc_[FY]_v[##]_[Date].xlsx` | `GlobalCo_GIRCalc_2024_v12_20250618.xlsx` |
| Validation log | `[MNE]_GIR_[FY]_[Jur]_ValLog_[Date].pdf` | `GlobalCo_GIR_2024_GB_ValLog_20250619.pdf` |
| Reconciliation | `[MNE]_GIR_[FY]_Recon_[Type]_[Date].xlsx` | `GlobalCo_GIR_2024_Recon_CbCR_20250615.xlsx` |
| Sign-off memo | `[MNE]_GIR_[FY]_SignOff_[Date].pdf` | `GlobalCo_GIR_2024_SignOff_20250620.pdf` |
| Submission receipt | `[MNE]_GIR_[FY]_[Jur]_Receipt_[Date].pdf` | `GlobalCo_GIR_2024_GB_Receipt_20250620.pdf` |
| Hash verification | `[MNE]_GIR_[FY]_[Jur]_SHA256_[Date].txt` | `GlobalCo_GIR_2024_GB_SHA256_20250620.txt` |

**Characters to Avoid in File Names:**

| Character | Problem | Alternative |
|-----------|---------|-------------|
| Spaces | URL encoding issues, script failures | Use underscores `_` |
| `/` `\` `:` | Path separators | Omit or use hyphen `-` |
| `*` `?` `"` `<` `>` `|` | OS reserved characters | Omit |
| Accented characters | Encoding inconsistencies | Use ASCII equivalents |
| Periods (except extension) | Multiple extension confusion | Use underscores |

### Version Control Framework

Version control for GIR files follows a structured lifecycle:

```
GIR Version Control Lifecycle:
│
├── Phase 1: DEVELOPMENT (v01, v02, v03...)
│   ├── Initial data entry and XML generation
│   ├── Iterative refinement based on validation
│   ├── Each significant save creates new version
│   ├── Working files editable by tax team
│   └── Typical: 5-15 versions
│
├── Phase 2: REVIEW (v##_REVIEW)
│   ├── Sent for independent review
│   ├── Review comments tracked separately
│   ├── Reviewer cannot modify source file
│   └── Typical: 1-3 review cycles
│
├── Phase 3: APPROVAL (v##_APPROVED)
│   ├── All review comments resolved
│   ├── Tax director/manager sign-off obtained
│   ├── File becomes read-only pending final checks
│   └── Single approval version per jurisdiction
│
├── Phase 4: FINAL (v##_FINAL)
│   ├── Final validation completed
│   ├── Ready for submission
│   ├── File locked (read-only)
│   └── No further changes permitted
│
├── Phase 5: SUBMITTED (v##_SUBMITTED)
│   ├── File submitted to tax authority
│   ├── Submission timestamp recorded
│   ├── Receipt/confirmation obtained
│   ├── Hash value recorded for integrity
│   └── Permanent archive copy created
│
└── Phase 6: AMENDMENT (AMD01, AMD02...)
    ├── Only if post-submission correction needed
    ├── New amendment number for each submission
    ├── Links to original MessageRefID
    └── Complete new approval cycle required
```

**Version Log Template:**

| Version | Date | Time | Author | Description | Status | Reviewer | Hash (first 16 chars) |
|---------|------|------|--------|-------------|--------|----------|----------------------|
| v01 | 2025-06-01 | 09:30 | J Smith | Initial data entry from Calculator | Development | - | - |
| v02 | 2025-06-05 | 14:15 | J Smith | Section 1 entities added | Development | - | - |
| v03 | 2025-06-08 | 11:00 | J Smith | All sections completed | Development | - | - |
| v04 | 2025-06-10 | 16:45 | J Smith | Validation errors corrected | Development | - | - |
| v05_REVIEW | 2025-06-12 | 10:00 | J Smith | Sent for manager review | Review | M Jones | - |
| v06 | 2025-06-14 | 13:30 | J Smith | Review comments addressed | Development | - | - |
| v07_APPROVED | 2025-06-16 | 15:00 | M Jones | Tax director approved | Approved | M Jones | - |
| v08_FINAL | 2025-06-18 | 09:00 | J Smith | Final validation passed | Final | - | 9f86d081884c7d65 |
| v08_SUBMITTED | 2025-06-20 | 10:30 | J Smith | Submitted to HMRC | Submitted | - | 9f86d081884c7d65 |

### Recommended Folder Structure

```
GIR_Compliance/
├── 2024/                                    # Fiscal Year
│   ├── 01_Calculator/
│   │   ├── Development/
│   │   │   └── [Working versions]
│   │   └── Final/
│   │       └── GlobalCo_GIRCalc_2024_v12_FINAL_20250618.xlsx
│   │
│   ├── 02_XML/
│   │   ├── Development/
│   │   │   └── [Working XML versions by jurisdiction]
│   │   ├── Review/
│   │   │   └── [Review versions]
│   │   ├── Final/
│   │   │   └── GlobalCo_GIR_2024_GB_v08_FINAL_20250618.xml
│   │   └── Submitted/
│   │       ├── GB/
│   │       │   ├── GlobalCo_GIR_2024_GB_v08_SUBMITTED_20250620.xml
│   │       │   └── GlobalCo_GIR_2024_GB_SHA256_20250620.txt
│   │       ├── DE/
│   │       └── [Other jurisdictions]
│   │
│   ├── 03_Validation/
│   │   ├── GlobalCo_GIR_2024_GB_ValLog_20250619.pdf
│   │   └── [Validation logs per jurisdiction]
│   │
│   ├── 04_Reconciliation/
│   │   ├── GlobalCo_GIR_2024_Recon_FS_20250610.xlsx
│   │   ├── GlobalCo_GIR_2024_Recon_CbCR_20250612.xlsx
│   │   └── GlobalCo_GIR_2024_Recon_TaxProv_20250614.xlsx
│   │
│   ├── 05_Approvals/
│   │   ├── GlobalCo_GIR_2024_SignOff_20250620.pdf
│   │   └── GlobalCo_GIR_2024_TaxDirectorApproval_20250618.pdf
│   │
│   ├── 06_Submissions/
│   │   ├── GB/
│   │   │   ├── GlobalCo_GIR_2024_GB_Receipt_20250620.pdf
│   │   │   └── GlobalCo_GIR_2024_GB_Confirmation_20250620.pdf
│   │   └── [Other jurisdictions]
│   │
│   ├── 07_Amendments/
│   │   └── AMD01/
│   │       ├── GlobalCo_GIR_2024_GB_AMD01_v01_20250815.xml
│   │       ├── GlobalCo_GIR_2024_AMD01_Explanation_20250815.pdf
│   │       └── GlobalCo_GIR_2024_GB_AMD01_Receipt_20250820.pdf
│   │
│   ├── 08_Supporting_Documentation/
│   │   ├── DataExtracts/
│   │   ├── WorkPapers/
│   │   └── Correspondence/
│   │
│   ├── 09_File_Register/
│   │   └── GlobalCo_GIR_2024_FileRegister.xlsx
│   │
│   └── README.txt
│
├── 2025/
│   └── [Same structure]
│
├── Templates/
│   ├── GIR_Calculator_Template_v1.xlsx
│   ├── GIR_FileRegister_Template.xlsx
│   └── GIR_ValidationChecklist_Template.xlsx
│
├── Schemas/
│   ├── GIR_v1.0.xsd
│   └── [Supporting schema files]
│
└── Documentation/
    ├── GIR_FileManagement_Procedures.pdf
    ├── GIR_NamingConvention_Guide.pdf
    └── GIR_AccessControl_Matrix.pdf
```

---

## 6.4.2 Backup Procedures

### Backup Strategy Overview

GIR files require a comprehensive backup strategy that addresses both operational recovery and long-term retention requirements.

```
GIR Backup Strategy:
│
├── Tier 1: Real-Time Replication
│   ├── Purpose: Immediate failover capability
│   ├── Method: Synchronous replication to secondary site
│   ├── RPO: Near-zero (seconds)
│   ├── RTO: Minutes
│   └── Applies to: Active working files
│
├── Tier 2: Daily Backup
│   ├── Purpose: Point-in-time recovery
│   ├── Method: Incremental backup to separate storage
│   ├── RPO: 24 hours
│   ├── RTO: 4 hours
│   ├── Retention: 30 days
│   └── Applies to: All GIR files and working papers
│
├── Tier 3: Weekly Full Backup
│   ├── Purpose: Weekly recovery point
│   ├── Method: Full backup to offsite/cloud
│   ├── RPO: 7 days
│   ├── RTO: 24 hours
│   ├── Retention: 52 weeks
│   └── Applies to: Complete GIR folder structure
│
└── Tier 4: Annual Archive
    ├── Purpose: Long-term retention
    ├── Method: Compressed, encrypted archive
    ├── Storage: Offsite + cloud redundancy
    ├── Retention: 10+ years
    └── Applies to: Completed fiscal year packages
```

### Backup Implementation

**Daily Incremental Backup Script (Bash/Linux):**

```bash
#!/bin/bash
# GIR Daily Backup Script
# Schedule via cron: 0 2 * * * /path/to/gir_backup.sh

# Configuration
SOURCE_DIR="/data/GIR_Compliance"
BACKUP_DIR="/backup/GIR"
DATE=$(date +%Y%m%d)
LOG_FILE="/var/log/gir_backup_${DATE}.log"

# Create backup directory
mkdir -p "${BACKUP_DIR}/${DATE}"

echo "GIR Backup Started: $(date)" >> "$LOG_FILE"

# Incremental backup using rsync
rsync -avz --delete \
    --backup --backup-dir="${BACKUP_DIR}/incremental_${DATE}" \
    "$SOURCE_DIR" "${BACKUP_DIR}/current/" >> "$LOG_FILE" 2>&1

# Verify backup integrity
if [ $? -eq 0 ]; then
    echo "Backup completed successfully" >> "$LOG_FILE"

    # Generate checksum of backup
    find "${BACKUP_DIR}/current" -type f -name "*.xml" \
        -exec sha256sum {} \; > "${BACKUP_DIR}/${DATE}/checksums.sha256"

    echo "Checksums generated" >> "$LOG_FILE"
else
    echo "BACKUP FAILED - Check logs" >> "$LOG_FILE"
    # Send alert (implement notification)
fi

echo "GIR Backup Completed: $(date)" >> "$LOG_FILE"
```

**Weekly Full Backup Script (PowerShell/Windows):**

```powershell
<#
.SYNOPSIS
    GIR Weekly Full Backup Script
.DESCRIPTION
    Creates compressed, encrypted backup of GIR files with integrity verification
#>

# Configuration
$SourcePath = "D:\GIR_Compliance"
$BackupPath = "\\backup-server\GIR_Backups"
$Date = Get-Date -Format "yyyyMMdd"
$ArchiveName = "GIR_FullBackup_$Date.zip"
$LogPath = "D:\Logs\GIR_Backup_$Date.log"

# Start logging
"GIR Weekly Full Backup Started: $(Get-Date)" | Out-File $LogPath

try {
    # Create compressed archive
    $ArchiveFullPath = Join-Path $BackupPath $ArchiveName

    Compress-Archive -Path "$SourcePath\*" `
                     -DestinationPath $ArchiveFullPath `
                     -CompressionLevel Optimal `
                     -Force

    "Archive created: $ArchiveFullPath" | Out-File $LogPath -Append

    # Generate and store hash
    $Hash = Get-FileHash -Path $ArchiveFullPath -Algorithm SHA256
    $HashFile = Join-Path $BackupPath "GIR_FullBackup_$Date.sha256"
    "$($Hash.Hash)  $ArchiveName" | Out-File $HashFile

    "SHA256 hash: $($Hash.Hash)" | Out-File $LogPath -Append

    # Verify archive integrity
    $TestResult = Test-Path $ArchiveFullPath
    if ($TestResult) {
        "Backup verification: PASSED" | Out-File $LogPath -Append
    } else {
        throw "Backup verification failed"
    }

    # Cleanup old backups (keep 52 weeks)
    Get-ChildItem -Path $BackupPath -Filter "GIR_FullBackup_*.zip" |
        Where-Object { $_.LastWriteTime -lt (Get-Date).AddDays(-365) } |
        Remove-Item -Force

    "Old backups cleaned up" | Out-File $LogPath -Append

} catch {
    "BACKUP FAILED: $_" | Out-File $LogPath -Append
    # Send alert notification
    throw
}

"GIR Weekly Full Backup Completed: $(Get-Date)" | Out-File $LogPath -Append
```

### Backup Verification Procedures

**Monthly Backup Verification Checklist:**

| # | Check Item | Method | Status | Date | Verified By |
|---|------------|--------|--------|------|-------------|
| 1 | Daily backups running | Check backup logs for past 30 days | ☐ | | |
| 2 | Weekly backups complete | Verify weekly archive files exist | ☐ | | |
| 3 | Backup integrity | Run checksum verification | ☐ | | |
| 4 | Restore test | Restore random file from backup | ☐ | | |
| 5 | Offsite replication | Confirm cloud/offsite copy current | ☐ | | |
| 6 | Storage capacity | Check backup storage utilisation | ☐ | | |

**Quarterly Restore Test Procedure:**

```
Restore Test Procedure:
│
├── Step 1: Select Test Scope
│   ├── Choose random XML file from each fiscal year
│   ├── Choose supporting documentation sample
│   └── Document selected files
│
├── Step 2: Perform Restore
│   ├── Restore files to isolated test location
│   ├── Record restore time
│   └── Do not overwrite production files
│
├── Step 3: Verify Integrity
│   ├── Compare restored file hash to original
│   ├── Open and validate XML structure
│   ├── Confirm all content readable
│   └── Check timestamps preserved
│
├── Step 4: Document Results
│   ├── Record pass/fail status
│   ├── Note any issues encountered
│   ├── Calculate actual RTO achieved
│   └── Archive test documentation
│
└── Step 5: Remediate Issues
    ├── Investigate any failures
    ├── Update backup procedures if needed
    └── Re-test if changes made
```

### Disaster Recovery Considerations

| Scenario | Recovery Approach | Target RTO | Target RPO |
|----------|-------------------|------------|------------|
| **Single file corruption** | Restore from daily backup | 1 hour | 24 hours |
| **Folder deletion** | Restore from daily/weekly backup | 4 hours | 24 hours |
| **Storage failure** | Failover to replicated storage | 1 hour | Near-zero |
| **Site disaster** | Restore from offsite backup | 24 hours | 7 days |
| **Ransomware attack** | Restore from isolated offline backup | 48 hours | 7 days |

---

## 6.4.3 Access Control Considerations

### Data Classification

GIR files contain sensitive financial and tax information requiring appropriate classification and handling:

```
GIR Data Classification:
│
├── Classification Level: HIGHLY CONFIDENTIAL
│   ├── Contains: Entity financial data, tax calculations, TINs
│   ├── Jurisdiction: Multi-country sensitive information
│   ├── Regulatory: Subject to tax secrecy laws, GDPR
│   └── Business: Commercially sensitive, competitive risk
│
├── Handling Requirements
│   ├── Encryption mandatory at rest and in transit
│   ├── Access restricted to named individuals
│   ├── External sharing only via secure channels
│   ├── Printing discouraged; secure disposal required
│   └── No storage on personal devices
│
└── Retention Classification
    ├── Legal hold: Subject to tax authority examination
    ├── Minimum retention: 10 years
    └── Destruction: Authorised disposal only
```

### Role-Based Access Control (RBAC)

Define access permissions based on organisational roles:

**GIR Access Control Matrix:**

| Role | Calculator | XML Development | XML Final | Submissions | Approvals | Amendments |
|------|------------|-----------------|-----------|-------------|-----------|------------|
| **Tax Manager** | Read-Write | Read-Write | Read | Read | Read-Write | Read-Write |
| **Tax Analyst** | Read-Write | Read-Write | Read | Read | Read | Read |
| **Tax Director** | Read | Read | Read | Read | Read-Write | Read-Write |
| **External Advisor** | Read | Read | Read | No Access | Read | Read |
| **IT Support** | No Access | No Access | No Access | No Access | No Access | No Access |
| **Auditor (Internal)** | Read | Read | Read | Read | Read | Read |
| **Auditor (External)** | Read (on request) | Read (on request) | Read | Read | Read | Read |

**Access Control Implementation:**

```
Access Control Procedures:
│
├── User Provisioning
│   ├── Access request via formal process
│   ├── Manager approval required
│   ├── Role assignment based on job function
│   ├── Minimum necessary access principle
│   └── Document access grants in register
│
├── Authentication Requirements
│   ├── Multi-factor authentication (MFA) mandatory
│   ├── Strong password policy (12+ characters)
│   ├── Session timeout: 15 minutes inactivity
│   └── No shared accounts permitted
│
├── Access Review
│   ├── Quarterly access certification
│   ├── Remove access for leavers within 24 hours
│   ├── Review role changes promptly
│   └── Document all access changes
│
└── External Access
    ├── Advisors: Time-limited read access via secure portal
    ├── Tax authorities: Provide copies, not direct access
    ├── No direct access to production file shares
    └── All external sharing logged
```

### GDPR and Data Protection Compliance

GIR files contain personal data (TINs, individual names for certain entity types) requiring GDPR compliance:

**Data Protection Considerations:**

| GDPR Requirement | GIR Application |
|------------------|-----------------|
| **Lawful basis** | Legal obligation (tax compliance) and legitimate interest |
| **Purpose limitation** | Tax compliance and audit defence only |
| **Data minimisation** | Include only required data elements |
| **Storage limitation** | 10-year retention justified by examination periods |
| **Security** | Encryption, access controls, audit logging |
| **Rights management** | Subject access requests may apply to certain data |

**Privacy Impact Note:** While GIR data primarily relates to corporate entities, individual TINs and names (e.g., for partnerships, sole traders) constitute personal data. Maintain records of processing activities (Article 30) and apply appropriate safeguards.

---

## 6.4.4 Audit Trail Maintenance

### Audit Trail Requirements

A comprehensive audit trail is essential for regulatory compliance, internal governance, and examination defence. HMRC and other tax authorities expect clear documentation of file history and changes.

```
GIR Audit Trail Components:
│
├── File-Level Audit Trail
│   ├── Creation timestamp and user
│   ├── All modifications with timestamps
│   ├── Access events (opens, views)
│   ├── Version progression
│   ├── Approval events
│   └── Submission events
│
├── Content-Level Audit Trail
│   ├── Data source documentation
│   ├── Calculation methodology
│   ├── Adjustment justifications
│   ├── Election rationale
│   └── Position papers for uncertain items
│
└── Process-Level Audit Trail
    ├── Review evidence
    ├── Approval sign-offs
    ├── Validation completion
    ├── Submission confirmations
    └── Amendment history
```

### File Integrity Verification

Record cryptographic hashes (SHA-256) for all submitted files to ensure integrity can be verified:

**Hash Generation and Recording:**

```bash
# Linux/Mac: Generate SHA-256 hash
sha256sum GlobalCo_GIR_2024_GB_v08_SUBMITTED_20250620.xml > GlobalCo_GIR_2024_GB_SHA256_20250620.txt

# Output format:
# 9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08  GlobalCo_GIR_2024_GB_v08_SUBMITTED_20250620.xml
```

```powershell
# Windows PowerShell: Generate SHA-256 hash
$Hash = Get-FileHash -Path "GlobalCo_GIR_2024_GB_v08_SUBMITTED_20250620.xml" -Algorithm SHA256
"$($Hash.Hash)  $($Hash.Path | Split-Path -Leaf)" | Out-File "GlobalCo_GIR_2024_GB_SHA256_20250620.txt"
```

**Hash Verification Record Template:**

```
┌─────────────────────────────────────────────────────────────────┐
│              FILE INTEGRITY VERIFICATION RECORD                 │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  MNE Group: GlobalCo Holdings plc                               │
│  Fiscal Year: 2024                                              │
│  Filing Jurisdiction: United Kingdom (HMRC)                     │
│                                                                 │
│  ─────────────────────────────────────────────────────────────  │
│  SUBMITTED FILE                                                 │
│  ─────────────────────────────────────────────────────────────  │
│                                                                 │
│  Filename: GlobalCo_GIR_2024_GB_v08_SUBMITTED_20250620.xml      │
│  File Size: 2,456,789 bytes                                     │
│  Created: 2025-06-18 09:00:00 UTC                               │
│  Modified: 2025-06-18 09:00:00 UTC                              │
│                                                                 │
│  SHA-256 Hash:                                                  │
│  9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08│
│                                                                 │
│  MD5 Hash (legacy reference):                                   │
│  098f6bcd4621d373cade4e832627b4f6                                │
│                                                                 │
│  ─────────────────────────────────────────────────────────────  │
│  SUBMISSION DETAILS                                             │
│  ─────────────────────────────────────────────────────────────  │
│                                                                 │
│  Submission Date: 2025-06-20                                    │
│  Submission Time: 10:30:00 UTC                                  │
│  Submitted By: John Smith                                       │
│  Submission Reference: HMRC-GIR-2024-GB-000123456               │
│                                                                 │
│  ─────────────────────────────────────────────────────────────  │
│  VERIFICATION                                                   │
│  ─────────────────────────────────────────────────────────────  │
│                                                                 │
│  Hash Generated By: John Smith                                  │
│  Hash Generation Date: 2025-06-20 10:35:00 UTC                  │
│  Tool Used: sha256sum (GNU coreutils 8.32)                      │
│                                                                 │
│  Hash Verified By: Mary Jones                                   │
│  Verification Date: 2025-06-20 11:00:00 UTC                     │
│  Verification Result: ☑ VERIFIED - Hashes Match                 │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### Activity Logging

Implement comprehensive activity logging for GIR files:

**Activity Log Format:**

| Timestamp (UTC) | User | Action | File | Details | IP Address |
|-----------------|------|--------|------|---------|------------|
| 2025-06-18 09:00:15 | jsmith | CREATE | GlobalCo_GIR_2024_GB_v08_FINAL.xml | Generated from Calculator v12 | 10.0.1.45 |
| 2025-06-18 09:05:22 | jsmith | VALIDATE | GlobalCo_GIR_2024_GB_v08_FINAL.xml | Schema validation PASSED | 10.0.1.45 |
| 2025-06-18 10:30:00 | mjones | ACCESS | GlobalCo_GIR_2024_GB_v08_FINAL.xml | Read access for review | 10.0.2.88 |
| 2025-06-18 14:00:00 | mjones | APPROVE | GlobalCo_GIR_2024_GB_v08_FINAL.xml | Tax director approval | 10.0.2.88 |
| 2025-06-20 10:30:45 | jsmith | SUBMIT | GlobalCo_GIR_2024_GB_v08_SUBMITTED.xml | HMRC submission ref: 000123456 | 10.0.1.45 |
| 2025-06-20 10:35:00 | jsmith | HASH | GlobalCo_GIR_2024_GB_v08_SUBMITTED.xml | SHA-256 generated | 10.0.1.45 |
| 2025-06-20 11:00:00 | mjones | VERIFY | GlobalCo_GIR_2024_GB_v08_SUBMITTED.xml | Hash verification confirmed | 10.0.2.88 |

### Retention of Audit Records

Audit trail records must be retained for at least as long as the underlying GIR files:

| Record Type | Minimum Retention | Storage Location |
|-------------|-------------------|------------------|
| Version logs | 10 years from filing deadline | Same as GIR files |
| Access logs | 10 years from filing deadline | Secure log archive |
| Hash records | 10 years from filing deadline | Same as GIR files |
| Approval records | 10 years from filing deadline | Approvals folder |
| Activity logs | 10 years from filing deadline | Centralised log system |

---

## 6.4.5 Document Retention Requirements

### Jurisdiction-Specific Retention Periods

While OECD Model Rules do not specify a universal retention period, implementing jurisdictions set their own requirements:

| Jurisdiction | General Tax Records | GIR Recommendation | Authority |
|--------------|--------------------|--------------------|-----------|
| **United Kingdom** | 6 years (standard) | 10 years | HMRC |
| **Germany** | 10 years (commercial) | 10 years | BZSt |
| **France** | 6 years (general) / 10 years (serious fraud) | 10 years | DGFiP |
| **Netherlands** | 7 years | 10 years | Belastingdienst |
| **Ireland** | 6 years | 10 years | Revenue |
| **Australia** | 5-8 years | 10 years | ATO |
| **United States** | 3-7 years (varies) | 10 years | IRS |
| **Switzerland** | 10 years | 10 years | Cantonal |

**Recommended Approach:** Apply 10-year retention universally to meet the most stringent requirements and ensure consistent treatment across jurisdictions.

### Retention Period Calculation

```
Retention Period Calculation:
│
├── Start Date: Later of:
│   ├── Actual filing date, OR
│   └── Filing deadline for the fiscal year
│
├── Example (Calendar Year MNE, FY 2024):
│   ├── Fiscal year end: 31 December 2024
│   ├── Filing deadline: 30 June 2026 (18-month first year)
│   ├── Actual filing: 20 June 2025
│   ├── Retention starts: 30 June 2026 (later of the two)
│   ├── Retention period: 10 years
│   └── Earliest destruction: 1 July 2036
│
└── Amendment Impact:
    ├── Amendment filed: 15 August 2025
    ├── Retention for amendment: Starts from amendment date
    └── May extend overall retention period
```

### Retention Schedule Template

| Document Type | FY 2024 Filed | Retention Start | Retention Period | Destruction Date | Legal Hold |
|---------------|---------------|-----------------|------------------|------------------|------------|
| GIR XML (submitted) | 20 Jun 2025 | 30 Jun 2026 | 10 years | 1 Jul 2036 | None |
| Calculator (final) | 18 Jun 2025 | 30 Jun 2026 | 10 years | 1 Jul 2036 | None |
| Validation logs | 19 Jun 2025 | 30 Jun 2026 | 10 years | 1 Jul 2036 | None |
| Reconciliations | 15 Jun 2025 | 30 Jun 2026 | 10 years | 1 Jul 2036 | None |
| Sign-off memo | 20 Jun 2025 | 30 Jun 2026 | 10 years | 1 Jul 2036 | None |
| Submission receipts | 20 Jun 2025 | 30 Jun 2026 | 10 years | 1 Jul 2036 | None |
| Draft versions | Various | 30 Jun 2026 | 3 years | 1 Jul 2029 | None |

---

## 6.4.6 XML File Register Template

The XML File Register is the central tracking document for all GIR files, providing a comprehensive inventory for audit and compliance purposes.

### XML File Register Structure

**Template: GIR_FileRegister_[FY].xlsx**

**Sheet 1: File Inventory**

| File ID | Filename | Type | Jurisdiction | Version | Status | Created Date | Created By | File Size (KB) | SHA-256 (first 16) | Storage Location |
|---------|----------|------|--------------|---------|--------|--------------|------------|----------------|-------------------|------------------|
| GIR-2024-001 | GlobalCo_GIR_2024_GB_v08_SUBMITTED_20250620.xml | XML | GB | v08 | Submitted | 2025-06-18 | J Smith | 2,456 | 9f86d081884c7d65 | /2024/02_XML/Submitted/GB/ |
| GIR-2024-002 | GlobalCo_GIR_2024_DE_v05_SUBMITTED_20250625.xml | XML | DE | v05 | Submitted | 2025-06-23 | J Smith | 1,890 | a3bf4f1b2b0b822c | /2024/02_XML/Submitted/DE/ |
| GIR-2024-003 | GlobalCo_GIR_2024_FR_v03_FINAL_20250628.xml | XML | FR | v03 | Final | 2025-06-26 | M Jones | 1,234 | d15d6c15b0f00a08 | /2024/02_XML/Final/ |
| CALC-2024-001 | GlobalCo_GIRCalc_2024_v12_FINAL_20250618.xlsx | Calculator | ALL | v12 | Final | 2025-06-18 | J Smith | 5,678 | - | /2024/01_Calculator/Final/ |

**Sheet 2: Submission Tracking**

| Jurisdiction | FCE | Filing Deadline | Submission Date | Submission Reference | Receipt Obtained | Status | Submitted By |
|--------------|-----|-----------------|-----------------|---------------------|------------------|--------|--------------|
| United Kingdom | GlobalCo Holdings plc | 30 Jun 2026 | 20 Jun 2025 | HMRC-GIR-2024-GB-000123 | Yes | Accepted | J Smith |
| Germany | GlobalCo Holdings plc | 30 Jun 2026 | 25 Jun 2025 | BZSt-GIR-2024-000456 | Yes | Accepted | J Smith |
| France | GlobalCo France SARL | 30 Jun 2026 | - | - | - | Pending | - |
| Netherlands | GlobalCo Holdings plc | 30 Jun 2026 | 28 Jun 2025 | BD-GIR-2024-000789 | Yes | Processing | M Jones |

**Sheet 3: Version History**

| File ID | Version | Date | Author | Description | Status | Reviewer | Review Date |
|---------|---------|------|--------|-------------|--------|----------|-------------|
| GIR-2024-001 | v01 | 2025-06-01 | J Smith | Initial XML generation | Development | - | - |
| GIR-2024-001 | v02 | 2025-06-05 | J Smith | Validation errors fixed | Development | - | - |
| GIR-2024-001 | v05_REVIEW | 2025-06-12 | J Smith | Sent for review | Review | M Jones | 2025-06-14 |
| GIR-2024-001 | v07_APPROVED | 2025-06-16 | M Jones | Director approved | Approved | M Jones | 2025-06-16 |
| GIR-2024-001 | v08_FINAL | 2025-06-18 | J Smith | Final version | Final | - | - |
| GIR-2024-001 | v08_SUBMITTED | 2025-06-20 | J Smith | Submitted to HMRC | Submitted | - | - |

**Sheet 4: Amendment Register**

| Amendment ID | Original File ID | Jurisdiction | Discovery Date | Error Description | Impact (€) | Amendment Filed | Authority Response | Status |
|--------------|------------------|--------------|----------------|-------------------|------------|-----------------|-------------------|--------|
| AMD01-2024-GB | GIR-2024-001 | GB | 2025-08-10 | ETR calculation error for DE jurisdiction | +125,000 | 2025-08-15 | Accepted 2025-08-25 | Closed |
| AMD02-2024-GB | GIR-2024-001 | GB | 2025-11-20 | Missing CE in France | +45,000 | Pending | - | Open |

**Sheet 5: Retention Schedule**

| File ID | Document Type | Fiscal Year | Filed/Created | Retention Start | Retention Years | Destruction Date | Legal Hold | Archived |
|---------|---------------|-------------|---------------|-----------------|-----------------|------------------|------------|----------|
| GIR-2024-001 | Submitted XML | 2024 | 20 Jun 2025 | 30 Jun 2026 | 10 | 1 Jul 2036 | No | No |
| GIR-2024-002 | Submitted XML | 2024 | 25 Jun 2025 | 30 Jun 2026 | 10 | 1 Jul 2036 | No | No |
| CALC-2024-001 | Calculator | 2024 | 18 Jun 2025 | 30 Jun 2026 | 10 | 1 Jul 2036 | No | No |

**Sheet 6: Access Log Summary**

| Month | Total Access Events | Unique Users | Most Accessed File | Access by Role (Tax Team / Management / Advisors) |
|-------|---------------------|--------------|-------------------|--------------------------------------------------|
| Jun 2025 | 245 | 8 | GIR-2024-001 (87) | 180 / 45 / 20 |
| Jul 2025 | 52 | 5 | GIR-2024-001 (23) | 35 / 12 / 5 |
| Aug 2025 | 78 | 6 | AMD01-2024-GB (45) | 55 / 18 / 5 |

### File Register Maintenance Procedures

```
File Register Maintenance:
│
├── Daily Tasks
│   ├── Update file inventory for new files created
│   ├── Record version changes
│   └── Log submissions and receipts
│
├── Weekly Tasks
│   ├── Verify file counts match actual folders
│   ├── Update status for pending submissions
│   └── Review access log summary
│
├── Monthly Tasks
│   ├── Generate access log summary
│   ├── Verify backup inclusion
│   └── Check retention dates approaching
│
├── Quarterly Tasks
│   ├── Full file register audit
│   ├── Verify SHA-256 hashes for submitted files
│   ├── Review and update access permissions
│   └── Archive completed periods
│
└── Annual Tasks
    ├── Archive previous year package
    ├── Calculate retention dates for current year
    ├── Review and update file management procedures
    └── Prepare new year folder structure
```

---

## 6.4.7 File Management Checklist

Use this comprehensive checklist to ensure complete file management compliance:

### Pre-Filing Checklist

| # | Check Item | Responsible | Status | Date |
|---|------------|-------------|--------|------|
| 1 | Folder structure created for fiscal year | Tax Manager | ☐ | |
| 2 | File naming convention documented and communicated | Tax Manager | ☐ | |
| 3 | Access permissions configured | IT / Tax Manager | ☐ | |
| 4 | Backup schedule confirmed operational | IT | ☐ | |
| 5 | File Register template prepared | Tax Analyst | ☐ | |

### During-Preparation Checklist

| # | Check Item | Responsible | Status | Date |
|---|------------|-------------|--------|------|
| 6 | Version log maintained current | Tax Analyst | ☐ | |
| 7 | All versions saved with correct naming | Tax Analyst | ☐ | |
| 8 | File Register updated with each new file | Tax Analyst | ☐ | |
| 9 | Review versions clearly marked | Tax Analyst | ☐ | |
| 10 | Approval evidence documented | Tax Manager | ☐ | |

### Pre-Submission Checklist

| # | Check Item | Responsible | Status | Date |
|---|------------|-------------|--------|------|
| 11 | Final version locked (read-only) | Tax Manager | ☐ | |
| 12 | SHA-256 hash generated and recorded | Tax Analyst | ☐ | |
| 13 | File Register updated with final status | Tax Analyst | ☐ | |
| 14 | Backup verified to include final version | Tax Analyst | ☐ | |
| 15 | Sign-off memo completed | Tax Director | ☐ | |

### Post-Submission Checklist

| # | Check Item | Responsible | Status | Date |
|---|------------|-------------|--------|------|
| 16 | Submitted version saved with SUBMITTED suffix | Tax Analyst | ☐ | |
| 17 | Submission receipt saved to folder | Tax Analyst | ☐ | |
| 18 | File Register updated with submission details | Tax Analyst | ☐ | |
| 19 | Hash verification completed by second person | Tax Manager | ☐ | |
| 20 | Retention dates calculated and recorded | Tax Analyst | ☐ | |

### Annual Archive Checklist

| # | Check Item | Responsible | Status | Date |
|---|------------|-------------|--------|------|
| 21 | All jurisdictions submitted | Tax Manager | ☐ | |
| 22 | File Register complete and verified | Tax Manager | ☐ | |
| 23 | Archive package created | Tax Analyst | ☐ | |
| 24 | Archive integrity verified (hash check) | Tax Analyst | ☐ | |
| 25 | Archive transferred to long-term storage | IT | ☐ | |

---

## Summary

Effective XML file management is fundamental to GIR compliance success. This section has provided comprehensive guidance on:

1. **File Storage and Version Control**
   - Standardised naming conventions for consistent identification
   - Structured folder hierarchy by fiscal year and document type
   - Version control lifecycle from development through submission

2. **Backup Procedures**
   - Tiered backup strategy (real-time, daily, weekly, annual)
   - Automated backup scripts for consistent execution
   - Regular verification and restore testing

3. **Access Control Considerations**
   - Role-based access control matrix
   - GDPR and data protection compliance
   - Authentication and authorisation requirements

4. **Audit Trail Maintenance**
   - File integrity verification using SHA-256 hashes
   - Comprehensive activity logging
   - Long-term retention of audit records

5. **XML File Register Template**
   - Central tracking document for all GIR files
   - Multi-sheet structure for inventory, submissions, versions, amendments
   - Maintenance procedures for ongoing accuracy

**Key Takeaway:** Invest in proper file management infrastructure before the first GIR filing. The 10+ year retention requirement means that files created today must remain accessible, verifiable, and auditable for over a decade. A disciplined approach from the outset prevents compliance gaps and supports examination defence throughout the retention period.

---

## References and Resources

### Standards and Guidance
- [ISO 15489-1:2016 - Information and documentation — Records management](https://www.iso.org/standard/62542.html) - International records management standard
- [HMRC Guidelines for Compliance (GfC8)](https://www.gov.uk/government/publications/hmrc-guidelines-for-compliance) - VAT compliance controls guidance with audit trail requirements
- [GDPR Article 5 - Principles relating to processing of personal data](https://gdpr-info.eu/art-5-gdpr/) - Storage limitation and data protection principles

### Technical Resources
- [File Integrity Monitoring Best Practices](https://www.sysdig.com/blog/file-integrity-monitoring) - Guidance on checksum verification and FIM implementation
- [Document Version Control Guide](https://start.docuware.com/blog/document-management/what-is-version-control-why-is-it-important) - Best practices for version control systems

### Pillar Two Administration
- [OECD GloBE Information Return](https://www.oecd.org/tax/beps/globe-information-return-pillar-two.pdf) - Original OECD GIR documentation
- [Pillar Two Administration](https://oecdpillars.com/pillar-tab/pillar-two-administration/) - Administrative guidance overview

---

## Section Progress

| Subsection | Status | Page Estimate |
|------------|--------|---------------|
| 6.4.1 File Storage and Version Control | Complete | 4 pages |
| 6.4.2 Backup Procedures | Complete | 2 pages |
| 6.4.3 Access Control Considerations | Complete | 2 pages |
| 6.4.4 Audit Trail Maintenance | Complete | 2 pages |
| 6.4.5 Document Retention Requirements | Complete | 1 page |
| 6.4.6 XML File Register Template | Complete | 2 pages |
| 6.4.7 File Management Checklist | Complete | 1 page |
| **Total** | **Complete** | **14 pages** |

*Target: 10-12 pages | Achieved: ~14 pages*

---

## Navigation

**Previous:** [Section 6.3: XML Validation Procedures](Section_06_03_XML_Validation_Procedures.md)

**Next:** [Section 7: Jurisdiction-Specific Filing Procedures](Section_07_01_Filing_Overview_and_Portal_Navigation.md)

**Return to:** [Table of Contents](00_Table_of_Contents.md)
