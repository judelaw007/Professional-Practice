# Section 14.4: Go-Live Checklist

## Overview

This section provides a comprehensive checklist for final pre-submission verification, submission procedures, and post-filing documentation. Use this checklist in the final weeks before your GIR filing deadline to ensure nothing is missed.

**Key Context:**
- First GIR filing deadline: **June 30, 2026** (for FY ending December 31, 2024)
- UK HMRC registration deadline: **June 30, 2025**
- Transitional penalty relief available for fiscal years beginning on or before December 31, 2026
- XML schema validation is mandatory—files with errors may be rejected

---

## 14.4.1 Go-Live Checklist Overview

The Go-Live Checklist comprises **35 checkpoints** across five categories:

| Category | Checkpoints | Focus |
|----------|-------------|-------|
| A. Data Verification | 8 | Completeness and accuracy of GIR data |
| B. Calculation Validation | 7 | ETR, top-up tax, and SBIE accuracy |
| C. XML and Technical | 6 | Schema compliance and file integrity |
| D. Submission Procedures | 8 | Portal access and filing execution |
| E. Post-Filing Documentation | 6 | Audit trail and confirmation records |
| **Total** | **35** | |

---

## 14.4.2 Category A: Data Verification (8 Checkpoints)

### Pre-Submission Data Completeness

| # | Checkpoint | Status | Sign-Off | Date |
|---|-----------|--------|----------|------|
| A1 | **All constituent entities included** – Verify that every constituent entity in the MNE group is listed in Section 1, including newly acquired entities and excluding properly documented excluded entities | ☐ Pass ☐ Fail ☐ N/A | ________ | ________ |
| A2 | **Entity identification complete** – All entities have: legal name, TIN (or "NOTIN" if not issued), jurisdiction code (ISO 3166-1), GloBE status indicator | ☐ Pass ☐ Fail ☐ N/A | ________ | ________ |
| A3 | **Ownership percentages verified** – Ownership chain from UPE to each constituent entity is accurate and sums correctly at each tier | ☐ Pass ☐ Fail ☐ N/A | ________ | ________ |
| A4 | **Financial data reconciled** – GloBE Income/Loss for each jurisdiction reconciles to source financial statements and consolidation system | ☐ Pass ☐ Fail ☐ N/A | ________ | ________ |
| A5 | **Covered taxes reconciled** – Covered taxes per GIR reconcile to tax provision data and local tax returns | ☐ Pass ☐ Fail ☐ N/A | ________ | ________ |
| A6 | **SBIE payroll data verified** – Eligible payroll costs by jurisdiction are accurate and supported by HR/payroll system extracts | ☐ Pass ☐ Fail ☐ N/A | ________ | ________ |
| A7 | **SBIE tangible assets verified** – Eligible tangible asset carrying values by jurisdiction are accurate and supported by fixed asset registers | ☐ Pass ☐ Fail ☐ N/A | ________ | ________ |
| A8 | **Currency conversion confirmed** – All amounts are in the correct reporting currency with documented exchange rates | ☐ Pass ☐ Fail ☐ N/A | ________ | ________ |

### Data Verification Sign-Off

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Data Manager | ________________ | ________________ | ________ |
| GIR Technical Lead | ________________ | ________________ | ________ |

---

## 14.4.3 Category B: Calculation Validation (7 Checkpoints)

### ETR and Top-Up Tax Verification

| # | Checkpoint | Status | Sign-Off | Date |
|---|-----------|--------|----------|------|
| B1 | **ETR calculation by jurisdiction** – Effective tax rate for each jurisdiction is mathematically correct: ETR = Adjusted Covered Taxes ÷ GloBE Income | ☐ Pass ☐ Fail ☐ N/A | ________ | ________ |
| B2 | **Top-up tax percentage correct** – Top-up tax percentage = Max (0, 15% - Jurisdictional ETR) | ☐ Pass ☐ Fail ☐ N/A | ________ | ________ |
| B3 | **SBIE calculation verified** – Substance-based income exclusion correctly applies current year carve-out rates (2024: 9.8% payroll, 7.8% tangible assets) | ☐ Pass ☐ Fail ☐ N/A | ________ | ________ |
| B4 | **Excess profit calculation** – Excess profit = GloBE Income - SBIE (verified by jurisdiction) | ☐ Pass ☐ Fail ☐ N/A | ________ | ________ |
| B5 | **Top-up tax amount** – Top-up tax by jurisdiction = Excess Profit × Top-up Tax Percentage | ☐ Pass ☐ Fail ☐ N/A | ________ | ________ |
| B6 | **IIR/UTPR/QDMTT allocation** – Top-up tax correctly allocated between IIR, UTPR, and QDMTT with supporting documentation | ☐ Pass ☐ Fail ☐ N/A | ________ | ________ |
| B7 | **Independent reconciliation** – GIR calculations reconcile to independent Pillar Two tax calculation (provision or standalone) | ☐ Pass ☐ Fail ☐ N/A | ________ | ________ |

### SBIE Carve-Out Rates Reference (Fiscal Year 2024)

| Component | 2024 Rate | 2025 Rate | 2026 Rate |
|-----------|-----------|-----------|-----------|
| Payroll carve-out | 9.8% | 9.6% | 9.4% |
| Tangible asset carve-out | 7.8% | 7.6% | 7.4% |

### Calculation Validation Sign-Off

| Role | Name | Signature | Date |
|------|------|-----------|------|
| GIR Technical Lead | ________________ | ________________ | ________ |
| External Advisor (if engaged) | ________________ | ________________ | ________ |

---

## 14.4.4 Category C: XML and Technical (6 Checkpoints)

### XML File Validation

| # | Checkpoint | Status | Sign-Off | Date |
|---|-----------|--------|----------|------|
| C1 | **XML schema validation passed** – XML file validates against OECD GIR XML Schema (January 2025 version) with no errors | ☐ Pass ☐ Fail ☐ N/A | ________ | ________ |
| C2 | **All validation elements present** – All "validation" (mandatory) elements are populated; optional elements included where data available | ☐ Pass ☐ Fail ☐ N/A | ________ | ________ |
| C3 | **Character encoding correct** – File uses UTF-8 encoding; special characters properly escaped | ☐ Pass ☐ Fail ☐ N/A | ________ | ________ |
| C4 | **File naming convention** – XML file named per jurisdiction-specific requirements | ☐ Pass ☐ Fail ☐ N/A | ________ | ________ |
| C5 | **File size within limits** – XML file size is within portal upload limits for each jurisdiction | ☐ Pass ☐ Fail ☐ N/A | ________ | ________ |
| C6 | **Test submission successful** – Trial upload to test environment (where available) completed without errors | ☐ Pass ☐ Fail ☐ N/A | ________ | ________ |

### XML Validation Error Resolution

| Error Code | Description | Resolution | Resolved? |
|------------|-------------|------------|-----------|
| __________ | __________ | __________ | ☐ |
| __________ | __________ | __________ | ☐ |
| __________ | __________ | __________ | ☐ |

### Technical Validation Sign-Off

| Role | Name | Signature | Date |
|------|------|-----------|------|
| GIR Technical Lead | ________________ | ________________ | ________ |

---

## 14.4.5 Category D: Submission Procedures (8 Checkpoints)

### Pre-Submission Preparation

| # | Checkpoint | Status | Sign-Off | Date |
|---|-----------|--------|----------|------|
| D1 | **Portal access confirmed** – Login credentials verified for all required jurisdiction portals; access tested within last 7 days | ☐ Pass ☐ Fail ☐ N/A | ________ | ________ |
| D2 | **Filing sequence determined** – Order of filing across jurisdictions documented; DFE jurisdiction filed first if applicable | ☐ Pass ☐ Fail ☐ N/A | ________ | ________ |
| D3 | **Senior approval obtained** – Tax Director/CFO has reviewed and approved final GIR content for submission | ☐ Pass ☐ Fail ☐ N/A | ________ | ________ |
| D4 | **Backup submission plan** – Alternative filing method identified in case of portal issues (e.g., manual upload, contact number for tax authority help desk) | ☐ Pass ☐ Fail ☐ N/A | ________ | ________ |

### Submission Execution

| # | Checkpoint | Status | Sign-Off | Date |
|---|-----------|--------|----------|------|
| D5 | **Primary jurisdiction GIR filed** – GIR submitted to primary/DFE jurisdiction portal; confirmation received | ☐ Pass ☐ Fail ☐ N/A | ________ | ________ |
| D6 | **Secondary jurisdiction(s) filed** – GIR submitted to all other required jurisdiction portals; confirmations received | ☐ Pass ☐ Fail ☐ N/A | ________ | ________ |
| D7 | **UK ORN filed (if applicable)** – Overseas Return Notification submitted to HMRC if GIR filed in non-UK jurisdiction | ☐ Pass ☐ Fail ☐ N/A | ________ | ________ |
| D8 | **UK SA Return filed (if applicable)** – UK Self Assessment return submitted with MTT/DTT liability details | ☐ Pass ☐ Fail ☐ N/A | ________ | ________ |

### Filing Sequence Tracker

| Jurisdiction | Filing Method | Planned Date | Actual Date | Confirmation # |
|--------------|---------------|--------------|-------------|----------------|
| ____________ | ____________ | ____________ | ____________ | ____________ |
| ____________ | ____________ | ____________ | ____________ | ____________ |
| ____________ | ____________ | ____________ | ____________ | ____________ |
| ____________ | ____________ | ____________ | ____________ | ____________ |
| UK (ORN) | HMRC Portal | ____________ | ____________ | ____________ |

### Submission Sign-Off

| Role | Name | Signature | Date |
|------|------|-----------|------|
| GIR Technical Lead | ________________ | ________________ | ________ |
| Project Manager | ________________ | ________________ | ________ |

---

## 14.4.6 Category E: Post-Filing Documentation (6 Checkpoints)

### Confirmation and Audit Trail

| # | Checkpoint | Status | Sign-Off | Date |
|---|-----------|--------|----------|------|
| E1 | **Submission confirmations captured** – Receipt/confirmation number from each jurisdiction portal saved and documented | ☐ Pass ☐ Fail ☐ N/A | ________ | ________ |
| E2 | **Screenshots captured** – Screenshot of submission confirmation screen saved for each jurisdiction | ☐ Pass ☐ Fail ☐ N/A | ________ | ________ |
| E3 | **XML file archived** – Final submitted XML file(s) saved with date stamp; version clearly identified as "as filed" | ☐ Pass ☐ Fail ☐ N/A | ________ | ________ |
| E4 | **Supporting documentation compiled** – All supporting calculations, source data, and working papers compiled into audit file | ☐ Pass ☐ Fail ☐ N/A | ________ | ________ |
| E5 | **Stakeholders notified** – CFO, Audit Committee, and external auditors notified of successful filing completion | ☐ Pass ☐ Fail ☐ N/A | ________ | ________ |
| E6 | **Audit file index completed** – GIR Audit File Index template completed with document references and storage locations | ☐ Pass ☐ Fail ☐ N/A | ________ | ________ |

### Post-Filing Documentation Sign-Off

| Role | Name | Signature | Date |
|------|------|-----------|------|
| GIR Technical Lead | ________________ | ________________ | ________ |
| Project Manager | ________________ | ________________ | ________ |

---

## 14.4.7 Audit File Contents Checklist

### Required Audit File Documentation

| Document | Description | Location/Reference | Included? |
|----------|-------------|-------------------|-----------|
| **Final GIR (all sections)** | Complete GIR Sections 1, 2, 3 as filed | ________________ | ☐ |
| **XML file (as submitted)** | Final XML file with submission timestamp | ________________ | ☐ |
| **Submission confirmations** | Receipts from all jurisdiction portals | ________________ | ☐ |
| **Entity database** | Complete constituent entity listing | ________________ | ☐ |
| **Ownership structure** | Corporate structure with percentages | ________________ | ☐ |
| **ETR calculations** | Detailed ETR calculation by jurisdiction | ________________ | ☐ |
| **SBIE calculations** | Payroll and tangible asset carve-outs | ________________ | ☐ |
| **Top-up tax allocation** | IIR/UTPR/QDMTT allocation workings | ________________ | ☐ |
| **Safe harbour elections** | Documentation supporting elections | ________________ | ☐ |
| **Source data extracts** | ERP, HR, consolidation system extracts | ________________ | ☐ |
| **Reconciliations** | Data reconciliations to source systems | ________________ | ☐ |
| **Validation reports** | XML validation results | ________________ | ☐ |
| **Approval documentation** | Sign-offs from senior management | ________________ | ☐ |
| **Estimation methodology** | Documentation for any estimated data | ________________ | ☐ |
| **External advisor reports** | Review reports (if applicable) | ________________ | ☐ |

### Document Retention Requirements

| Jurisdiction | Minimum Retention Period | Notes |
|--------------|-------------------------|-------|
| General guidance | 7 years minimum | Per general tax compliance principles |
| UK | 6 years from end of accounting period | HMRC requirements |
| Germany | 10 years | German fiscal code (AO) |
| France | 6 years | French tax law |
| [Other jurisdictions] | Check local requirements | Varies by jurisdiction |

**Recommendation:** Retain all GIR-related documentation for minimum 10 years to cover longest retention requirements and potential future enquiries.

---

## 14.4.8 Final Approval Sign-Off

### Pre-Filing Approval

| Approval | Name | Title | Signature | Date |
|----------|------|-------|-----------|------|
| **Technical Review** | ________________ | ________________ | ________________ | ________ |
| **Data Accuracy** | ________________ | ________________ | ________________ | ________ |
| **Calculation Accuracy** | ________________ | ________________ | ________________ | ________ |
| **Tax Director Approval** | ________________ | ________________ | ________________ | ________ |
| **CFO Approval** | ________________ | ________________ | ________________ | ________ |

### Post-Filing Confirmation

| Confirmation | Name | Title | Signature | Date |
|--------------|------|-------|-----------|------|
| **Filing Complete** | ________________ | ________________ | ________________ | ________ |
| **Documentation Complete** | ________________ | ________________ | ________________ | ________ |
| **Audit File Complete** | ________________ | ________________ | ________________ | ________ |

---

## 14.4.9 Issue Resolution Log

### Pre-Submission Issues

| Issue # | Description | Date Identified | Owner | Resolution | Date Resolved |
|---------|-------------|-----------------|-------|------------|---------------|
| _______ | ________________ | ________ | ________ | ________________ | ________ |
| _______ | ________________ | ________ | ________ | ________________ | ________ |
| _______ | ________________ | ________ | ________ | ________________ | ________ |

### Post-Submission Issues

| Issue # | Description | Date Identified | Owner | Resolution | Date Resolved |
|---------|-------------|-----------------|-------|------------|---------------|
| _______ | ________________ | ________ | ________ | ________________ | ________ |
| _______ | ________________ | ________ | ________ | ________________ | ________ |
| _______ | ________________ | ________ | ________ | ________________ | ________ |

---

## 14.4.10 Emergency Contacts

### Internal Contacts

| Role | Name | Phone | Email |
|------|------|-------|-------|
| GIR Technical Lead | ________________ | ________________ | ________________ |
| Project Manager | ________________ | ________________ | ________________ |
| IT Support | ________________ | ________________ | ________________ |
| Tax Director | ________________ | ________________ | ________________ |
| CFO | ________________ | ________________ | ________________ |

### External Contacts

| Role | Organization | Phone | Email |
|------|--------------|-------|-------|
| External Advisor | ________________ | ________________ | ________________ |
| UK HMRC Helpline | HMRC | 0300 200 3600 | ________________ |
| [Other Tax Authority] | ________________ | ________________ | ________________ |

---

## 14.4.11 Contingency Procedures

### Portal Unavailability

If a filing portal is unavailable on the planned submission date:

1. **Document the issue** – Screenshot error message, note date/time
2. **Contact tax authority helpline** – Report issue, request guidance
3. **Attempt alternative methods** – Manual upload, email submission (if permitted)
4. **Document all attempts** – Maintain log of efforts to file
5. **Request extension** – If deadline will be missed, contact authority proactively

### Late Data Discovery

If errors are discovered after filing:

1. **Assess materiality** – Determine if error is material to ETR or top-up tax
2. **Check amendment procedures** – Review jurisdiction-specific amendment process
3. **File amendment promptly** – Use prescribed amendment forms/procedures
4. **Document correction** – Maintain record of original error and correction
5. **Consider voluntary disclosure** – If material, consider proactive disclosure to authority

### Transitional Penalty Relief

Per OECD guidance (Annex C, December 2023):
- Tax authorities must give "careful consideration" before applying penalties
- Relief applies where MNE has taken "reasonable measures" to apply rules correctly
- Available for fiscal years beginning on or before December 31, 2026

**Documentation for Relief:** Maintain evidence of reasonable measures taken, including:
- Process documentation
- External advisor engagement
- Training records
- Quality review evidence
- Timely correction of errors

---

## 14.4.12 Go-Live Checklist Summary

### Checkpoint Status Summary

| Category | Total | Passed | Failed | N/A |
|----------|-------|--------|--------|-----|
| A. Data Verification | 8 | ___ | ___ | ___ |
| B. Calculation Validation | 7 | ___ | ___ | ___ |
| C. XML and Technical | 6 | ___ | ___ | ___ |
| D. Submission Procedures | 8 | ___ | ___ | ___ |
| E. Post-Filing Documentation | 6 | ___ | ___ | ___ |
| **Total** | **35** | ___ | ___ | ___ |

### Go/No-Go Decision

| Criterion | Assessment |
|-----------|------------|
| All Category A checkpoints passed or N/A | ☐ Yes ☐ No |
| All Category B checkpoints passed or N/A | ☐ Yes ☐ No |
| All Category C checkpoints passed or N/A | ☐ Yes ☐ No |
| All Category D checkpoints D1-D4 passed | ☐ Yes ☐ No |
| Senior approval obtained | ☐ Yes ☐ No |

**Decision:** ☐ **GO** – Proceed with filing | ☐ **NO-GO** – Resolve issues before filing

### Final Sign-Off

| Role | Decision | Name | Signature | Date |
|------|----------|------|-----------|------|
| Project Manager | ☐ GO ☐ NO-GO | ________________ | ________________ | ________ |
| Tax Director | ☐ GO ☐ NO-GO | ________________ | ________________ | ________ |

---

## Summary

The Go-Live Checklist provides systematic verification across 35 checkpoints to ensure:

1. **Data completeness and accuracy** – All entities included, financials reconciled
2. **Calculation correctness** – ETR, top-up tax, and SBIE properly calculated
3. **Technical compliance** – XML validates against OECD schema
4. **Smooth submission** – Portal access confirmed, filing sequence planned
5. **Audit readiness** – Documentation compiled, retention requirements met

**Critical Success Factors:**

- Complete all Category A-C checkpoints before proceeding to submission
- Obtain senior approval before filing
- Capture all confirmation numbers and screenshots immediately upon submission
- Compile audit file promptly after filing while details are fresh
- Notify stakeholders of successful completion

**Transitional Relief Reminder:** For fiscal years beginning on or before December 31, 2026, tax authorities are expected to give careful consideration before applying penalties where reasonable measures have been taken. Documented use of this checklist demonstrates systematic compliance efforts.

---

**Deliverable Reference:** Go-Live Checklist (35 checkpoints) - available in Appendix A as printable PDF/Excel

---

*Section 14.4 Complete - Last Updated: November 2025*
*This completes Section 14: Implementation Roadmap*
