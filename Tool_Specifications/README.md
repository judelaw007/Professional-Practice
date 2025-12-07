# Tool Specifications

This folder contains detailed technical specifications for each demo tool in the GloBE Information Return course. These specifications provide app developers with comprehensive requirements for building the tools on tools.mojitax.com.

---

## Purpose

The specifications in this folder replace the summary-level `TOOLS-REGISTRY (2).csv` with comprehensive, developer-ready documentation that includes:

- Detailed input field definitions with validation rules
- Output field specifications with display formats
- Complete calculation logic with formulas
- User interface wireframes and layouts
- Error handling and edge cases
- Test cases mapped to case study data
- Accessibility requirements

---

## Tool Index

| Tool ID | Tool Name | Status | Specification |
|---------|-----------|--------|---------------|
| GIR-001 | ETR Calculator | Draft | [GIR-001_ETR_Calculator.md](GIR-001_ETR_Calculator.md) |
| GIR-002 | SBIE Calculator | Draft | [GIR-002_SBIE_Calculator.md](GIR-002_SBIE_Calculator.md) |
| GIR-003 | Top-Up Tax Calculator | Draft | [GIR-003_TopUp_Tax_Calculator.md](GIR-003_TopUp_Tax_Calculator.md) |
| GIR-004 | Safe Harbour Qualification Tool | Pending | GIR-004_Safe_Harbour_Tool.md |
| GIR-005 | Filing Deadline Calculator | Pending | GIR-005_Deadline_Calculator.md |
| GIR-006 | Data Point Reference | Pending | GIR-006_Data_Point_Reference.md |
| GIR-007 | DFE Election Assessment Tool | Pending | GIR-007_DFE_Election_Tool.md |
| GIR-008 | GIR Practice Form | Pending | GIR-008_Practice_Form.md |
| GIR-009 | Audit File Checklist | Pending | GIR-009_Audit_Checklist.md |

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

## Relationship to Other Documents

| Document | Purpose |
|----------|---------|
| `TOOLS-REGISTRY (2).csv` | Quick-reference index (retained for overview) |
| `Tool_Specifications/*.md` | Detailed developer specifications |
| `Case_Study_*/Sample_Data.md` | Test input data for each tool |
| `Case_Study_*/Expected_Outcomes.md` | Expected results for verification |

---

## For App Developers

When implementing a tool:

1. Read the complete specification document
2. Implement all input validations as specified
3. Follow the calculation logic exactly
4. Use the test cases for QA verification
5. Ensure all edge cases are handled
6. Meet accessibility requirements

---

## Version

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2024-12-07 | — | Initial structure with GIR-001 template |
