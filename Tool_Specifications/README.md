# Tool Specifications

This folder contains detailed technical specifications for demo tools on tools.mojitax.com. These specifications provide app developers with comprehensive requirements for building and maintaining the tools.

---

## Current Tools (v2 - Consolidated)

The tool suite has been consolidated from 9 separate tools to 6 integrated tools for better usability and maintenance.

| Tool ID | Tool Name | Status | Specification |
|---------|-----------|--------|---------------|
| GIR-001 | GloBE Calculator | Live | [GIR-001_GloBE_Calculator.md](GIR-001_GloBE_Calculator.md) |
| GIR-002 | Safe Harbour Qualifier | Live | [GIR-002_Safe_Harbour_Qualifier.md](GIR-002_Safe_Harbour_Qualifier.md) |
| GIR-003 | Filing Deadline Calculator | Live | [GIR-003_Filing_Deadline_Calculator.md](GIR-003_Filing_Deadline_Calculator.md) |
| GIR-004 | GIR Practice Form | Live | [GIR-004_GIR_Practice_Form.md](GIR-004_GIR_Practice_Form.md) |
| GIR-005 | DFE Assessment Tool | Live | [GIR-005_DFE_Assessment_Tool.md](GIR-005_DFE_Assessment_Tool.md) |
| GIR-006 | Audit File Checklist | Live | [GIR-006_Audit_File_Checklist.md](GIR-006_Audit_File_Checklist.md) |

---

## Tool Descriptions

### GIR-001: GloBE Calculator
**Integrated 3-step calculation tool** that combines:
- Step 1: ETR calculation from GloBE Income and Covered Taxes
- Step 2: SBIE calculation with transition rates
- Step 3: Top-Up Tax computation

*Consolidates previous: ETR Calculator, SBIE Calculator, Top-Up Tax Calculator*

### GIR-002: Safe Harbour Qualifier
**Pre-screening tool** for Transitional CbCR Safe Harbour assessment:
- De Minimis Test (Revenue < €10M AND Profit < €1M)
- Simplified ETR Test (15%/16%/17% thresholds by year)
- Routine Profits Test (Profit ≤ SBIE)

### GIR-003: Filing Deadline Calculator
**Compliance timeline tool** that calculates:
- Standard 15-month GIR filing deadline
- 18-month transitional extension for first filings
- Jurisdiction-specific variations

### GIR-004: GIR Practice Form
**Interactive form** for practicing GloBE Information Return completion with:
- All required data fields
- Validation and error checking
- Export/save functionality

### GIR-005: DFE Assessment Tool
**Election guidance tool** for Designated Filing Entity decisions:
- DFE qualification criteria
- Filing obligation analysis
- Surrogate filing considerations

### GIR-006: Audit File Checklist
**Documentation tool** for GloBE compliance audit readiness:
- Required documentation checklist
- Evidence requirements by category
- Audit trail guidance

---

## Folder Structure

```
Tool_Specifications/
├── README.md                          (this file)
├── GIR-001_GloBE_Calculator.md
├── GIR-002_Safe_Harbour_Qualifier.md
├── GIR-003_Filing_Deadline_Calculator.md
├── GIR-004_GIR_Practice_Form.md
├── GIR-005_DFE_Assessment_Tool.md
├── GIR-006_Audit_File_Checklist.md
└── archive/                           (superseded v1 specifications)
    ├── GIR-001_ETR_Calculator.md
    ├── GIR-002_SBIE_Calculator.md
    ├── GIR-003_TopUp_Tax_Calculator.md
    ├── GIR-004_Safe_Harbour_Tool.md
    ├── GIR-005_Deadline_Calculator.md
    ├── GIR-006_Data_Point_Reference.md
    ├── GIR-007_DFE_Election_Tool.md
    ├── GIR-008_Practice_Form.md
    └── GIR-009_Audit_Checklist.md
```

---

## Specification Template Structure

Each tool specification follows this standard structure:

```
1.  Tool Metadata
2.  Purpose & Learning Objective
3.  Input Fields (with full validation rules)
4.  Output Fields (with display formats)
5.  Calculation Logic (pseudocode)
6.  User Interface Specifications (wireframes)
7.  User Flow (step-by-step)
8.  Edge Cases & Error Handling
9.  Test Cases (mapped to case studies)
10. Accessibility Requirements
11. Technical Notes
12. Limitations & Scope
13. Version History
14. Appendix: Case Study Alignment
```

---

## For App Developers

When implementing or updating a tool:

1. Read the complete specification document
2. Implement all input validations as specified
3. Follow the calculation logic exactly
4. Use the test cases for QA verification
5. Ensure all edge cases are handled
6. Meet accessibility requirements

---

## Courses Using These Tools

| Course | Tools Used |
|--------|------------|
| GloBE Information Return: Complete Filing Implementation | All 6 tools |
| ADIT Pillar Two Professional Practice Course | GIR-001 (Parts 2,4,5,6), GIR-002 through GIR-006 (Part 7) |

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 2.0 | 2024-12-09 | Consolidated from 9 to 6 tools; archived v1 specs |
| 1.0 | 2024-12-07 | Initial structure with 9 separate tool specifications |
