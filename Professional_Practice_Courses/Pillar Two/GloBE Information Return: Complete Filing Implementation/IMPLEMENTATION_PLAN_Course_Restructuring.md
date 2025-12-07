# Implementation Plan: GloBE Information Return Course Restructuring

## Document Purpose

This implementation plan provides a phased approach to restructuring the "GloBE Information Return: Complete Filing Implementation" course to align with the updated Professional Practice Course guidelines (December 2025).

**Key Principle:** This is a sensitive restructuring. The goal is to improve the course, not break what works well. The content quality is high—we're changing *how* materials are delivered, not *what* is taught.

---

## Executive Summary of Changes

| Current State | Target State |
|---------------|--------------|
| Downloadable Excel/Word files in Appendices | Examples shown inline in eBook; practice via tools.mojitax.com |
| Appendices contain template libraries | Appendices contain case studies only |
| Tools described in dedicated Section 5.1 | Tools introduced within relevant chapters |
| No tools.mojitax.com integration | Demo tools on platform for hands-on practice |
| Worked examples in main content only | Case study data in Appendices for tool practice |

---

## Phase 1: Preserve and Archive (No Content Loss)

**Objective:** Ensure no work is lost before restructuring.

**Duration:** 1-2 hours

**STATUS: COMPLETED**

### Completed Actions

1. **Archived Current Appendix Files**
   - Moved `Appendices/Appendix_Practical_Tools_Library/` to `Appendices/Archive/`
   - All Excel/Word files preserved for reference

2. **Created New Case Study Structure**
   - Created 5 case study folders matching Section 10 scenarios
   - Added README.md explaining new structure

3. **Folder Structure Now:**
   ```
   Appendices/
   ├── README.md (new - explains structure)
   ├── Archive/ (contains all original templates)
   ├── Case_Study_1_GlobalTech_First_Filing/
   ├── Case_Study_2_Complex_Ownership/
   ├── Case_Study_3_Data_Gap_Challenges/
   ├── Case_Study_4_Multi_QDMTT_Jurisdictions/
   └── Case_Study_5_Amendment_Required/
   ```

### Verification
- [x] All files safely archived
- [x] No files deleted
- [x] New case study structure created

---

## Phase 2: Define Demo Tools for tools.mojitax.com

**Objective:** Specify which demo tools are needed on the platform.

**Duration:** 2-3 hours

**STATUS: COMPLETED**

### Tools Added to TOOLS-REGISTRY (2).csv

The following tools have been specified in the central Tools Registry:

| Tool_ID | Tool_Name | Form | Chapter Reference |
|---------|-----------|------|-------------------|
| GIR-001 | GIR ETR Calculator | Calculator | Section 5.4.1 (ETR Computation) |
| GIR-002 | GIR SBIE Calculator | Calculator | Section 5.4.2 (SBIE Calculation) |
| GIR-003 | GIR Top-Up Tax Calculator | Calculator | Section 5.4.3 (Top-up Tax) |
| GIR-004 | Safe Harbour Qualification Tool | Assessment | Section 9.1 (CbCR Safe Harbour) |

### Tool-to-Case Study Mapping

| Tool | Case Study | Expected Outcome (Ireland) |
|------|------------|---------------------------|
| GIR-001 | Case Study 1: GlobalTech | ETR = 11.59% |
| GIR-002 | Case Study 1: GlobalTech | SBIE = €3,188,000 |
| GIR-003 | Case Study 1: GlobalTech | Top-up Tax = €1,010,000 |
| GIR-004 | Case Study 1: GlobalTech | Ireland = FAIL (requires full calculation) |

### Understanding the Course Developer's Role

The Course Developer:
- **Specifies** what tools are needed (in TOOLS-REGISTRY CSV)
- **Writes** tool specifications (purpose, inputs, outputs)
- **Does NOT** build the tools (App Developer does that)

### Verification
- [x] Tools Registry checked
- [x] Tool specifications written in TOOLS-REGISTRY (2).csv
- [x] Tool-to-chapter mapping complete

---

## Phase 3: Restructure Appendices as Case Studies

**Objective:** Transform Appendices from template libraries to case study collections.

**Duration:** 4-6 hours

**STATUS: COMPLETED**

### Case Studies Created

| Case Study | Source | Files Created |
|------------|--------|---------------|
| Case_Study_1_GlobalTech_First_Filing | Section 10.1 | Scenario_Overview.md, Sample_Data.md, Expected_Outcomes.md |
| Case_Study_2_Complex_Ownership | Section 10.2 | Scenario_Overview.md, Sample_Data.md, Expected_Outcomes.md |
| Case_Study_3_Data_Gap_Challenges | Section 10.3 | Scenario_Overview.md, Sample_Data.md, Expected_Outcomes.md |
| Case_Study_4_Multi_QDMTT_Jurisdictions | Section 10.4 | Scenario_Overview.md, Sample_Data.md, Expected_Outcomes.md |
| Case_Study_5_Amendment_Required | Section 10.5 | Scenario_Overview.md, Sample_Data.md, Expected_Outcomes.md |

### Case Study Format Used

Each case study includes:
- **Scenario_Overview.md** - Context, learning objectives, company profile, tools to use
- **Sample_Data.md** - Input data for demo tools, structured for practice
- **Expected_Outcomes.md** - Expected results, calculation breakdowns, learning points

### Tool References in Case Studies

| Tool ID | Tool Name | Used In Case Studies |
|---------|-----------|---------------------|
| GIR-001 | GIR ETR Calculator | 1, 2, 3, 4, 5 |
| GIR-002 | GIR SBIE Calculator | 1, 2, 3, 4 |
| GIR-003 | GIR Top-Up Tax Calculator | 1, 2, 3, 4, 5 |
| GIR-004 | Safe Harbour Qualification Tool | 1 |

### Verification
- [x] Case study folders created
- [x] Data extracted from Section 10
- [x] Expected outcomes documented for each
- [x] Tool references added

---

## Phase 4: Update eBook Content - Show Examples Inline

**Objective:** Move template examples from downloadable files into the eBook content.

**Duration:** 6-10 hours (largest phase)

**STATUS: IN PROGRESS**

### Completed Updates

1. **Section 1.3 (Deliverables Inventory) - REWRITTEN**
   - Removed all downloadable file inventory (Excel tools, Word templates, checklists)
   - Replaced with "How This Course Helps You Learn" explaining new approach
   - Added demo tools table with tool IDs and purposes
   - Added case studies overview table
   - Added demo vs professional tools distinction
   - Added recommended learning path

2. **Section 5.1 (Calculator Overview) - UPDATED**
   - Added "Demo Tools vs Professional Tools" section at beginning
   - Listed all 4 demo tools with IDs and purposes
   - Added comparison table: when to use demo vs professional tools
   - Added "Practice with Case Studies" section with tool mapping
   - Clarified that demo tools are for learning, not production use

3. **eBook_Structural_Plan.md - UPDATED**
   - Replaced "Mandatory Deliverables Checklist" with "Learning Approach"
   - Updated Section 1.3 description from deliverables to learning approach
   - Added tools and case studies tables

4. **Section 1 Summary - UPDATED**
   - Changed "Tools" row to "Learning Approach"
   - Updated Next Steps to remove download references

5. **Section 1.4 (Implementation Timeline) - UPDATED**
   - Replaced all 6 "Template Used:" references with "Learning Resources:"
   - Now points to relevant course sections, demo tools, and case studies
   - Months 4-6 reference specific demo tools and case studies

### Verification
- [x] Section 1.3 rewritten
- [x] Section 5.1 updated with demo/professional tool distinction
- [x] Template references updated (all "Template Used:" references fixed)
- [ ] Key templates shown inline (optional - lower priority)

**STATUS: PHASE 4 COMPLETE**

---

## Phase 5: Add Tool Introductions Within Chapters

**Objective:** Introduce demo tools naturally within relevant chapters.

**Duration:** 3-4 hours

### Tool Introduction Placement

| Tool | Introduce In Chapter | After Teaching |
|------|---------------------|----------------|
| GIR Section 1-3 Practice Tool | Section 5.2/5.3/5.4 | Each section completion |
| ETR Calculator | Section 5.4.1 | ETR calculation methodology |
| SBIE Calculator | Section 5.4.2 | SBIE calculation methodology |
| Safe Harbour Qualification Tool | Section 9.1 | CbCR safe harbour criteria |
| Deadline Lookup Tool | Section 2.3 | Filing deadlines |

### Tool Introduction Format

Each tool introduction should include:

```markdown
---

**Practice This Skill**

Now that you understand [concept just taught], you can practice using the [Tool Name] on tools.mojitax.com.

**Important:** This is a demo tool for learning purposes. In professional practice, you would use enterprise Pillar Two software with full audit trails and compliance features. The demo tool helps you understand the mechanics without the complexity of production systems.

**To practice:**
1. Go to tools.mojitax.com and find [Tool Name]
2. Use the GlobalTech data from Case Study 1 in the Appendices
3. Enter the values as shown in the case study
4. Your result should be [expected outcome]

If your result differs, review [specific section] to check your understanding.

---
```

### Tasks

1. **Draft Tool Introduction Text**
   - Write introduction text for each tool
   - Include demo vs professional disclaimer
   - Include case study reference
   - Include expected outcome

2. **Insert Into Relevant Chapters**
   - Add tool introductions at appropriate points
   - Ensure flow with surrounding content

3. **Add Cross-References**
   - Link between chapters, case studies, and tools

### Verification
- [ ] Tool introductions drafted
- [ ] Introductions inserted at correct locations
- [ ] Demo vs professional clarification included
- [ ] Case study references added
- [ ] Expected outcomes stated

---

## Phase 6: Update Structural Plan and Metadata

**Objective:** Align the eBook_Structural_Plan.md with new course structure.

**Duration:** 1-2 hours

### Updates Needed

1. **Remove "Mandatory Deliverables Checklist"**
   - Old style listed minimum Excel/Word file counts
   - Replace with new approach description

2. **Update Appendix Description**
   - Change from "Template libraries" to "Case studies only"

3. **Add Tools Platform Section**
   - Document which tools are used
   - Reference Tools Registry check requirement

4. **Update Quality Assurance Checklist**
   - Add case study verification
   - Add tool integration verification

### Tasks

1. **Update eBook_Structural_Plan.md**
   - Revise deliverables section
   - Update appendix structure
   - Add tools.mojitax.com integration notes

### Verification
- [ ] Structural plan updated
- [ ] Mandatory minimums removed
- [ ] New approach documented

---

## Phase 7: Quality Assurance and Final Review

**Objective:** Verify all changes are complete and coherent.

**Duration:** 2-3 hours

### Checklist

**Content Quality:**
- [ ] All template examples shown inline in content
- [ ] All tool references include case study connections
- [ ] Demo vs professional tool distinction added
- [ ] No broken references to old appendix structure

**Appendix Structure:**
- [ ] Appendices contain case studies only
- [ ] Each case study has complete data
- [ ] Expected outcomes documented
- [ ] Original templates archived (not deleted)

**Tool Integration:**
- [ ] Tool specifications written
- [ ] Tools introduced within relevant chapters
- [ ] Case study data connects to tools
- [ ] Expected outcomes enable verification

**Overall Coherence:**
- [ ] Course flows logically
- [ ] No contradictions between sections
- [ ] Consistent terminology throughout

---

## Risk Mitigation

| Risk | Mitigation |
|------|------------|
| Content loss during restructuring | Archive everything first; no deletions without backup |
| Tools not ready when course launches | Course content works standalone; tools enhance but aren't required |
| Broken internal references | Use search to find all "Appendix" references; update systematically |
| Confusion for existing users | Add version note explaining the update |

---

## Timeline Summary

| Phase | Duration | Dependencies |
|-------|----------|--------------|
| Phase 1: Archive | 1-2 hours | None |
| Phase 2: Tool Specifications | 2-3 hours | Phase 1 |
| Phase 3: Restructure Appendices | 4-6 hours | Phases 1, 2 |
| Phase 4: Update eBook Content | 6-10 hours | Phase 3 |
| Phase 5: Tool Introductions | 3-4 hours | Phases 2, 4 |
| Phase 6: Update Structural Plan | 1-2 hours | Phases 3, 4, 5 |
| Phase 7: Quality Assurance | 2-3 hours | All prior phases |

**Total Estimated Effort:** 19-30 hours

---

## What Stays the Same

These elements are already excellent and don't need changes:

- ✅ Implementation-first approach
- ✅ Jurisdiction-specific filing procedures (Section 7)
- ✅ XML generation guidance (Section 6)
- ✅ Common pitfalls content (Section 11)
- ✅ Penalty regimes by jurisdiction
- ✅ Worked example narratives (Section 10 - teaching content)
- ✅ Resource directory and links (Section 13)
- ✅ Quality of calculations and explanations

---

## Next Steps

1. **Review this plan** and confirm approach
2. **Decide on timeline** for implementation
3. **Begin Phase 1** (Archive) to ensure nothing is lost
4. **Proceed sequentially** through remaining phases

---

*Document Version: 1.0*
*Created: December 2025*
*Status: Awaiting approval before implementation*
