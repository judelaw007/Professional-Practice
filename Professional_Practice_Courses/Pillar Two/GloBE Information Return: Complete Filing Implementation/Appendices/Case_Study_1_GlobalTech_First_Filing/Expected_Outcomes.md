# Case Study 1: GlobalTech Manufacturing - Expected Outcomes

Use these expected outcomes to verify your calculations with the demo tools.

---

## Ireland - Expected Results

### GloBE Calculator - Step 1: ETR (GIR-001)

| Output | Expected Value |
|--------|----------------|
| **Jurisdictional ETR** | 11.59% |
| **Top-up Tax Percentage** | 3.41% |
| **Status** | Low-Taxed Jurisdiction (RED) |

**Calculation Breakdown:**
```
ETR = Adjusted Covered Taxes / GloBE Income
ETR = €3,800,000 / €32,800,000
ETR = 11.59%

Top-up Tax % = 15% - ETR
Top-up Tax % = 15% - 11.59%
Top-up Tax % = 3.41%
```

### GloBE Calculator - Step 2: SBIE (GIR-001)

| Output | Expected Value |
|--------|----------------|
| **Payroll Carve-out Rate (FY2024)** | 9.8% |
| **Payroll SBIE Amount** | €1,862,000 |
| **Asset Carve-out Rate (FY2024)** | 7.8% |
| **Asset SBIE Amount** | €1,326,000 |
| **Total SBIE** | €3,188,000 |

**Calculation Breakdown:**
```
Payroll SBIE = €19,000,000 × 9.8% = €1,862,000
Asset SBIE = €17,000,000 × 7.8% = €1,326,000
Total SBIE = €1,862,000 + €1,326,000 = €3,188,000
```

### GloBE Calculator - Step 3: Top-Up Tax (GIR-001)

| Output | Expected Value |
|--------|----------------|
| **ETR** | 11.59% |
| **Top-up Tax %** | 3.41% |
| **Excess Profit** | €29,612,000 |
| **Gross Top-up Tax** | €1,009,769 |
| **QDMTT Offset** | €0 |
| **Net Top-up Tax (IIR)** | €1,009,769 |

**Calculation Breakdown:**
```
Excess Profit = GloBE Income - SBIE
Excess Profit = €32,800,000 - €3,188,000
Excess Profit = €29,612,000

Gross Top-up Tax = Excess Profit × Top-up Tax %
Gross Top-up Tax = €29,612,000 × 3.41%
Gross Top-up Tax = €1,009,769

Net Top-up Tax = Gross Top-up Tax - QDMTT
Net Top-up Tax = €1,009,769 - €0
Net Top-up Tax = €1,009,769
```

---

## Switzerland - Expected Results

### GloBE Calculator - Step 1: ETR (GIR-001)

| Output | Expected Value |
|--------|----------------|
| **Jurisdictional ETR** | 14.00% |
| **Top-up Tax Percentage** | 1.00% |
| **Status** | Low-Taxed Jurisdiction (RED) |

**Calculation Breakdown:**
```
ETR = €2,520,000 / €18,000,000 = 14.00%
Top-up Tax % = 15% - 14.00% = 1.00%
```

### GloBE Calculator - Step 2: SBIE (GIR-001)

| Output | Expected Value |
|--------|----------------|
| **Payroll SBIE Amount** | €833,000 |
| **Asset SBIE Amount** | €327,600 |
| **Total SBIE** | €1,160,600 |

**Calculation Breakdown:**
```
Payroll SBIE = €8,500,000 × 9.8% = €833,000
Asset SBIE = €4,200,000 × 7.8% = €327,600
Total SBIE = €833,000 + €327,600 = €1,160,600
```

### GloBE Calculator - Step 3: Top-Up Tax (GIR-001)

| Output | Expected Value |
|--------|----------------|
| **Excess Profit** | €16,839,400 |
| **Gross Top-up Tax** | €168,394 |
| **Net Top-up Tax** | €168,394 |

**Calculation Breakdown:**
```
Excess Profit = €18,000,000 - €1,160,600 = €16,839,400
Top-up Tax = €16,839,400 × 1.00% = €168,394
```

---

## Safe Harbour Qualifier (GIR-002) - UK Test

| Output | Expected Value |
|--------|----------------|
| **De Minimis Test** | PASS |
| **Simplified ETR Test** | PASS (23% > 15%) |
| **Routine Profits Test** | PASS |
| **Overall Status** | Safe Harbour APPLIES |
| **Recommendation** | Full GloBE calculation NOT required |

**Calculation Breakdown:**
```
Simplified ETR = €11,040,000 / €48,000,000 = 23%
23% > 15% threshold for FY2024 → PASS

UK qualifies for Transitional CbCR Safe Harbour
```

---

## Group Total Summary

| Jurisdiction | Top-up Tax |
|--------------|------------|
| Ireland | €1,009,769 |
| Switzerland | €168,394 |
| **Total UK IIR Liability** | **€1,178,163** |

---

---

## Filing Deadline Calculator (GIR-003) - UK Filing

| Output | Expected Value |
|--------|----------------|
| **Standard Deadline** | 31 March 2026 |
| **First Year Extension** | 18 months (applies) |
| **Extended Deadline** | 30 June 2026 |
| **Deadline Type** | First Filing - Extended |

**Calculation Breakdown:**
```
Fiscal Year End: 31 December 2024

Standard Deadline = FY End + 15 months
Standard Deadline = 31 December 2024 + 15 months
Standard Deadline = 31 March 2026

First Year Extension = Additional 3 months
Extended Deadline = 31 March 2026 + 3 months
Extended Deadline = 30 June 2026
```

**Key Milestones:**

| Milestone | Date |
|-----------|------|
| Fiscal Year End | 31 December 2024 |
| Data Collection Complete | 31 March 2025 (recommended) |
| Draft GIR Review | 30 September 2025 (recommended) |
| Final Review | 31 March 2026 (recommended) |
| Standard Filing Deadline | 31 March 2026 |
| Extended Filing Deadline | 30 June 2026 |

---

## GIR Practice Form - Data Point Search (GIR-004) - Sample Searches

| Search Query | Expected Results |
|--------------|------------------|
| "UPE name" | Section 1, Field 1.1.1 - Legal name of Ultimate Parent Entity |
| "GloBE Income" | Section 3, Field 3.2.x - GloBE Income per jurisdiction |
| "SBIE" | Section 3, Fields 3.4.x - Substance-Based Income Exclusion |
| "Top-up Tax" | Section 3, Fields 3.5.x - Top-up Tax computation |

**Learning Outcome:**
Students should be able to navigate the ~480 GIR data points using the integrated search bar and identify which fields correspond to each calculation performed in GIR-001.

---

## DFE Assessment Tool (GIR-005) - GlobalTech Assessment

| Output | Expected Value |
|--------|----------------|
| **Recommended DFE** | GlobalTech Manufacturing Ltd (UK) |
| **Confidence Score** | 92/100 |
| **Primary Reason** | UPE with full consolidation visibility |

**Scoring Breakdown:**

| Factor | GlobalTech UK | Weight | Score |
|--------|---------------|--------|-------|
| UPE Status | Yes | 25 | 25 |
| Pillar Two Implementation | IIR Effective 2024 | 20 | 20 |
| Tax Team Resources | 8 FTE (Strong) | 20 | 18 |
| Systems Capability | ERP Integrated | 15 | 14 |
| Advisor Support | Big 4 Engaged | 10 | 10 |
| Filing Experience | First Year | 10 | 5 |
| **Total** | | **100** | **92** |

**Alternative Assessment (GlobalTech Europe BV - NL):**

| Factor | Score |
|--------|-------|
| Total Score | 58/100 |
| Key Weakness | Not UPE, regional visibility only |
| Recommendation | Not recommended as DFE |

**DFE Recommendation Summary:**
```
GlobalTech Manufacturing Ltd (UK) is strongly recommended as the
Designated Filing Entity because:

✅ Is the Ultimate Parent Entity (simplifies compliance)
✅ Has full consolidated financial visibility
✅ Strong tax team (8 FTE) with Big 4 support
✅ UK IIR effective from FY2024 - filing obligation exists
✅ ERP system integrated for data extraction

Considerations:
⚠️ First year filing - no prior GIR experience
⚠️ Must notify all 20 jurisdictions of DFE appointment
```

---

## GIR Practice Form (GIR-004) - Validation Results

**Section 1 Validation:**

| Field | Input | Validation | Status |
|-------|-------|------------|--------|
| UPE Name | GlobalTech Manufacturing Ltd | Required field | ✅ PASS |
| UPE Jurisdiction | United Kingdom | Valid ISO code | ✅ PASS |
| Fiscal Year | 2024 | Valid year | ✅ PASS |
| Revenue | €1,350,000,000 | ≥ €750M threshold | ✅ PASS |
| DFE Name | GlobalTech Manufacturing Ltd | Required field | ✅ PASS |

**Section 2 Validation (Sample):**

| Entity | Validation Check | Status |
|--------|------------------|--------|
| GlobalTech Manufacturing Ltd | UPE flagged correctly | ✅ PASS |
| GT IP Holdings Ltd | Ownership = 100% | ✅ PASS |
| All Ireland Entities | Jurisdiction consistent | ✅ PASS |

**Section 3 Validation (Ireland):**

| Cross-Reference Check | Expected | Status |
|-----------------------|----------|--------|
| ETR = Covered Taxes / GloBE Income | 11.59% | ✅ PASS |
| Total SBIE = Payroll SBIE + Asset SBIE | €3,188,000 | ✅ PASS |
| Excess Profit = GloBE Income - SBIE | €29,612,000 | ✅ PASS |
| Top-up Tax = Excess Profit × Top-up % | €1,009,769 | ✅ PASS |

**Form Completion Status:**
- Section 1: 100% Complete
- Section 2: 7 of 75 entities entered (sample)
- Section 3: 2 of 20 jurisdictions computed (Ireland, Switzerland)

---

## Audit File Checklist (GIR-006) - Completion Status

**Overall Progress:**

| Metric | Value |
|--------|-------|
| **Total Checklist Items** | 66 |
| **Completed Items** | 45 |
| **Incomplete Items** | 18 |
| **Not Applicable** | 3 |
| **Completion Percentage** | 71.4% |
| **Overall Status** | 🔵 IN PROGRESS |

**Category Breakdown:**

| Category | Complete | Total | Percentage |
|----------|----------|-------|------------|
| Section 1 - General Information | 10 | 10 | 100% ✅ |
| Section 2 - Corporate Structure | 8 | 10 | 80% |
| Section 3 - GloBE Computation | 14 | 18 | 78% |
| Elections Documentation | 3 | 10 | 30% |
| Safe Harbour Documentation | 5 | 8 | 63% |
| System & Process Controls | 5 | 10 | 50% |

**Gap Analysis - Critical Items:**

| Item ID | Description | Priority | Action Required |
|---------|-------------|----------|-----------------|
| S3-009 | Adjusted Covered Taxes workpapers | Critical | Complete tax reconciliation for CH |
| EL-001 | Election inventory listing | Critical | Document policy choices made |

**Gap Analysis - High Priority Items:**

| Item ID | Description | Action Required |
|---------|-------------|-----------------|
| S3-003 | Policy choice memorandum | Draft memo for stock comp treatment |
| SH-001 | Safe Harbour qualification analysis | Complete for remaining 16 jurisdictions |
| CT-004 | Manual adjustment approval process | Document review workflow |
| CT-007 | Review and sign-off workflow | Establish approval chain |

**Audit Readiness Assessment:**
```
GlobalTech Manufacturing Ltd - FY2024 GIR Audit File

Status: IN PROGRESS (71.4% complete)

Strengths:
✅ Section 1 (General Information) fully documented
✅ Core GloBE calculations completed for low-tax jurisdictions
✅ Safe Harbour analysis started for qualifying jurisdictions

Gaps to Address:
⚠️ Elections documentation incomplete (first year - limited elections)
⚠️ Process controls documentation needs formalization
⚠️ 2 critical items outstanding

Estimated Completion: 2-3 weeks of focused effort
```

---

## Group Total Summary (All Tools)

### Financial Summary

| Jurisdiction | ETR | Top-up Tax | Safe Harbour? |
|--------------|-----|------------|---------------|
| Ireland | 11.59% | €1,009,769 | No |
| Switzerland | 14.00% | €168,394 | No |
| UK | N/A | €0 | Yes |
| Other 17 jurisdictions | Various | €0 | Yes |
| **Total IIR Liability** | | **€1,178,163** | |

### Tool Usage Summary

| Tool ID | Tool Name | Used For | Key Output |
|---------|-----------|----------|------------|
| GIR-001 | GloBE Calculator | ETR, SBIE, Top-up Tax for IE & CH | ETR 11.59%/14.00%, SBIE €3.19M/€1.16M, Top-up €1.18M |
| GIR-002 | Safe Harbour Qualifier | UK qualification test | Safe Harbour APPLIES (CbCR data) |
| GIR-003 | Filing Deadline Calculator | Filing timeline | 30 June 2026 (18-month extended) |
| GIR-004 | GIR Practice Form | Form population + data point lookup | Validation passed, ~480 data points |
| GIR-005 | DFE Assessment Tool | Filing entity selection | UK UPE recommended (92/100) |
| GIR-006 | Audit File Checklist | Documentation tracking | 71.4% complete (45/63 items) |

---

## Learning Points

If your results differ from these expected outcomes:

1. **ETR differs (GIR-001 Step 1)**: Check you're using Adjusted Covered Taxes (not Total Tax Expense) divided by GloBE Income (not Accounting Income)

2. **SBIE differs (GIR-001 Step 2)**: Verify you're using the correct FY2024 rates (9.8% payroll, 7.8% assets) and check your input totals

3. **Top-up Tax differs (GIR-001 Step 3)**: Ensure you're calculating Excess Profit correctly (GloBE Income minus SBIE, not minus taxes)

4. **Safe Harbour fails unexpectedly (GIR-002)**: Check you're using CbCR data (not GloBE-adjusted figures) for the safe harbour test

5. **Filing deadline incorrect (GIR-003)**: Verify you selected "First Filing Year = Yes" to get the 18-month extension

6. **DFE score differs (GIR-005)**: Check you're assessing all six factors and applying correct weights

7. **Form validation fails (GIR-004)**: Ensure cross-reference checks match (ETR calculation, SBIE totals, etc.)

8. **Audit checklist incomplete (GIR-006)**: Focus on Critical priority items first before addressing High/Medium items
