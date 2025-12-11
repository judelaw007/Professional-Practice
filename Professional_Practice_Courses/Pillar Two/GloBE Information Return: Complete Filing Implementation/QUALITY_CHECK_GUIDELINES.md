# Quality Check Guidelines

## GloBE Information Return: Complete Filing Implementation Course

**Document Purpose:** This document defines the quality check standards and principles applied to all sections of this Professional Practice Course.

**Last Updated:** December 2025

---

## Quality Check Principles

### 1. Upward-Only Cross-Referencing Rule

**Principle:** Sections can only reference PREVIOUS sections (upward/backward referencing), not FUTURE sections (forward/downward referencing).

**Rationale:**
- Creates progressive, linear learning path
- Reduces reader confusion and cognitive load
- Each section is self-contained with knowledge available at that point
- Follows professional textbook and training material standards
- Forward references create unnecessary "you'll learn this later" frustration

**Implementation:**

✅ **ALLOWED - Upward References:**
```markdown
Section 5 can reference: Section 1, 2, 3, or 4
Section 10 can reference: Section 1-9
```

❌ **NOT ALLOWED - Forward References:**
```markdown
Section 1 CANNOT reference: Section 2, 3, 4, etc.
Section 5 CANNOT reference: Section 6, 7, 8, etc.
```

**Alternative Approach for Section 1 (Introductory Content):**

When Section 1 needs to mention topics covered later, use **generic references** without specific section numbers:

✅ **CORRECT:**
```markdown
**Learning Resources:** XML generation and validation processes are covered in detail later in this course.
**Learning Resources:** ERP data extraction strategies are covered in detail later in this course.
```

❌ **INCORRECT:**
```markdown
**Learning Resources:** Section 6 (XML Generation and Validation) covers this topic.
**Learning Resources:** See Section 4.2 for ERP extraction guidance.
```

**Exception:** Case Study references are allowed from any section since Case Studies are in the Appendices and are practice materials, not linear content.

✅ **ALLOWED:**
```markdown
Case Study 4 provides multi-jurisdiction filing practice scenarios.
Practice with Case Study 5 (Amendment Required) for post-filing scenarios.
```

---

### 2. Content Consistency Standards

**Terminology Consistency:**
- Use consistent acronyms throughout (GIR, MNE, GloBE, DFE, QDMTT, IIR, UTPR, etc.)
- Define acronyms on first use in each major section
- Use consistent capitalization (e.g., "Constituent Entity" not "constituent entity")

**Formatting Consistency:**
- Date formats: Use consistent format (e.g., "June 30, 2026" or "December 31, 2024")
- Number formats: Use consistent decimal separators and thousand separators
- Currency: Always specify currency (€750 million, not 750 million)
- Section headers: Use consistent heading levels

**Table Formatting:**
- All tables must have headers
- Use consistent column alignment
- Include table separators (---|---)
- Ensure all rows have the same number of columns

> **Note:** For comprehensive consistency audits, use the prompt at `Quality /Content Consistency & Flow Check`

---

### 3. Flow and Readability

**Section Structure:**
- Each section should have clear learning objectives
- Progressive complexity within each section
- Smooth transitions between subsections
- Clear summary or key takeaways at the end

**Paragraph Structure:**
- Keep paragraphs focused on single topics
- Use bullet points for lists of 3+ items
- Break up long text with tables, examples, or diagrams

**Professional Tone:**
- Implementation-focused, not conceptual
- Direct, actionable language
- Avoid academic or overly formal language
- Assume reader has Pillar Two foundation knowledge

---

### 4. Technical Accuracy

**Data Points:**
- Verify all data point counts (e.g., ~480 total data points)
- Cross-reference with OECD January 2025 GIR Template
- Ensure alignment with latest OECD Administrative Guidance

**Deadlines and Dates:**
- Verify all filing deadlines against official sources
- Include jurisdiction-specific variations
- Note transitional relief periods accurately

**Regulatory References:**
- Link to official OECD guidance documents
- Reference specific jurisdictional guidance (HMRC, BZSt, IRAS, ATO, etc.)
- Update links periodically to ensure they remain active

---

### 5. Examples and Case Studies

**Inline Examples:**
- Use realistic, practical scenarios
- Include complete data, not partial examples
- Annotate examples to explain each element
- Show both correct and incorrect approaches where helpful

**Case Study References:**
- Reference case studies by name and number
- Explain what the case study demonstrates
- Indicate which demo tools to use with each case study

---

## Quality Check Checklist

Use this checklist when performing quality checks on each section:

### Cross-Referencing
- [ ] All cross-references follow upward-only principle
- [ ] No forward references to later sections (unless generic: "covered later in this course")
- [ ] Case Study references are appropriate and helpful
- [ ] Demo tool references are accurate

### Content
- [ ] Learning objectives are clear and measurable
- [ ] Content flows logically from beginning to end
- [ ] Terminology is consistent throughout
- [ ] No conflicting information with other sections
- [ ] Technical accuracy verified against OECD sources

### Formatting
- [ ] All tables properly formatted with headers
- [ ] Consistent date and number formats
- [ ] Heading levels are appropriate and consistent
- [ ] Bullet points and lists are properly formatted
- [ ] Code blocks and examples are properly formatted

### Readability
- [ ] No spelling or grammar errors
- [ ] Sentences are clear and concise
- [ ] Professional, implementation-focused tone
- [ ] Appropriate use of examples and illustrations
- [ ] Smooth transitions between topics

### Links and References
- [ ] All external links are valid and working
- [ ] Source citations are complete
- [ ] References to official guidance are accurate
- [ ] Portal links are current and correct

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | December 2025 | Initial quality check guidelines created with upward-only cross-referencing principle |
| 1.1 | December 2025 | Simplified Content Consistency section; moved detailed audit prompt to Quality folder |

---

*End of Quality Check Guidelines*
