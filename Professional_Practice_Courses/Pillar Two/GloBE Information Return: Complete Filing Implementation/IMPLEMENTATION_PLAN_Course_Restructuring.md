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

### New Appendix Structure

```
Appendices/
├── Case_Study_1_GlobalTech_First_Filing/
│   ├── Scenario_Overview.md
│   ├── Company_Profile_Data.md
│   ├── Section_1_Sample_Data.md
│   ├── Section_2_Safe_Harbour_Data.md
│   ├── Section_3_GloBE_Computation_Data.md
│   └── Expected_Outcomes.md
│
├── Case_Study_2_Complex_Ownership/
│   ├── [Similar structure]
│   └── ...
│
├── Case_Study_3_Data_Gap_Challenges/
│   └── ...
│
└── Archive/
    └── [Preserved original templates]
```

### Case Study Format

Each case study should include:

```markdown
# Case Study [N]: [Title]

## Scenario Context
[How does this connect to the course? What situation does the learner face?]

## Company/Group Profile
[Background on the fictional company]

## Learning Objectives
[What skills will learners practice?]

## Sample Data Provided
[The actual data learners will use]

## Tool to Use
[Which tool on tools.mojitax.com]

## Task Instructions
[Step-by-step what to do]

## Expected Outcomes
[What results learners should get - for self-verification]

## Learning Points
[Key takeaways from completing this exercise]
```

### Source Material

The existing Section 10 scenarios are excellent source material:
- **Section 10.1** (GlobalTech Manufacturing) → Case Study 1
- **Section 10.2** (Complex Ownership Structure) → Case Study 2
- **Section 10.3** (Data Gap Challenges) → Case Study 3
- **Section 10.4** (Multi-QDMTT Jurisdictions) → Case Study 4
- **Section 10.5** (Amendment Required) → Case Study 5

### Tasks

1. **Create Case Study Folder Structure**
   - Set up new Appendix folder structure
   - Maintain Archive for original files

2. **Extract Case Study Data from Section 10**
   - Pull the sample data from Section 10 scenarios
   - Reformat into case study structure
   - Add expected outcomes for each

3. **Write Case Study Introduction Files**
   - Create Scenario_Overview.md for each case study
   - Include tool references and learning objectives

4. **Add Expected Outcomes**
   - Document what results learners should get
   - This enables self-verification

### Verification
- [ ] Case study folders created
- [ ] Data extracted from Section 10
- [ ] Expected outcomes documented for each
- [ ] Tool references added

---

## Phase 4: Update eBook Content - Show Examples Inline

**Objective:** Move template examples from downloadable files into the eBook content.

**Duration:** 6-10 hours (largest phase)

### What This Means

**Before (Old Style):**
> "Download the DFE Election Template from Appendix A and complete it for your group."

**After (New Style):**
> [Shows the complete DFE Election Template structure inline in the content, with annotations explaining each section, followed by:]
> "Practice completing a DFE election using the GlobalTech scenario in Case Study 1."

### Sections Requiring Updates

| Section | Current State | Update Needed |
|---------|---------------|---------------|
| 1.3 Deliverables Inventory | Lists downloadable files | Rewrite to describe inline examples + tools |
| 5.1 Calculator Overview | Dedicated tool section | Integrate tool intro into relevant sections |
| Various chapters | Reference "download template" | Show template inline, reference case study |

### Content Update Approach

For each template/tool currently offered as download:

1. **Identify where it's referenced** in the course
2. **Show the example inline** in the eBook at that location
3. **Add practice reference** pointing to case study + tool
4. **Remove download reference** from Deliverables Inventory

### Key Sections to Update

#### Section 1.3 (Deliverables Inventory)
- **Current:** 8-10 pages listing downloadable packages
- **Target:** Describe learning approach (inline examples + tools.mojitax.com + case studies)

#### Section 5.1 (Calculator Overview)
- **Current:** Standalone tool introduction
- **Target:** Redistribute tool introductions to relevant chapters; add demo vs professional tool clarification

#### All Template References
- **Current:** "See Appendix A for template"
- **Target:** Show template inline; "Practice with Case Study X on tools.mojitax.com"

### Tasks

1. **Update Section 1.3**
   - Rewrite to explain new learning model
   - Remove file download inventory
   - Describe: inline examples + demo tools + case studies

2. **Update Section 5.1**
   - Add demo tools vs professional tools clarification
   - Add case study references
   - Consider redistributing some content to where tools are used

3. **Update Template References Throughout**
   - Search for "Appendix A", "download", "template" references
   - Replace with inline examples where appropriate
   - Add case study and tool references

4. **Show Key Templates Inline**
   - DFE Election Documentation
   - Data Request Memo
   - Filing Confirmation Record
   - Safe Harbour Election Forms

### Verification
- [ ] Section 1.3 rewritten
- [ ] Section 5.1 updated with demo/professional tool distinction
- [ ] Template references updated
- [ ] Key templates shown inline

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
