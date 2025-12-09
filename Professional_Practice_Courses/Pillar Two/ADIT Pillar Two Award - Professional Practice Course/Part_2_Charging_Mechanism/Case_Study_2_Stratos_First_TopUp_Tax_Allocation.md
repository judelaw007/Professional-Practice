# Case Study 2: Stratos's First Top-Up Tax Allocation

## Introduction

This case study brings together the concepts from Chapters 2.1 to 2.4. You will complete a full Top-Up Tax allocation for Stratos Group plc, working through the GloBE Calculator tool (GIR-001) and then applying the IIR and UTPR allocation methodologies.

**Important:** This case study requires you to work through the complete calculation chain—from raw financial data to final Top-Up Tax allocation. Do not skip steps.

**Time estimate:** 90-120 minutes

---

## Background: Stratos Group — FY 2025

Stratos Group plc has completed its first year subject to the GloBE Rules. The tax team has gathered financial and tax data from all jurisdictions and must now:

1. Calculate ETR for each jurisdiction
2. Determine which jurisdictions are low-taxed (ETR < 15%)
3. Calculate Top-Up Tax for low-taxed jurisdictions
4. Allocate Top-Up Tax under IIR or UTPR

### Relevant Ownership Structure

```
Stratos Group plc (UK) — UPE
    │
    ├── SG Holdings Ltd (UK) 100%
    │       │
    │       └── SG Netherlands BV (Netherlands) 100%
    │               │
    │               ├── SG Ireland Ltd (Ireland) 60% ← Note: 40% External Investor
    │               │       └── SG Ireland IP Ltd (Ireland) 100%
    │               │
    │               └── SG Singapore Pte Ltd (Singapore) 100%
    │                       └── SG Singapore Tech Pte Ltd (Singapore) 100%
    │
    ├── SG Germany GmbH (Germany) 100%
    │
    └── SG France SAS (France) 100%
```

### Qualified IIR/UTPR Status (FY 2025)

| Jurisdiction | Qualified IIR? | Qualified UTPR? |
|--------------|---------------|-----------------|
| UK | Yes | Yes |
| Netherlands | Yes | Yes |
| Germany | Yes | Yes |
| France | Yes | Yes |
| Ireland | Yes (QDMTT only) | No |
| Singapore | No | No |

---

## Task 1: ETR Calculation (GIR-001 Step 1)

### Data Provided

The following data has been extracted from Stratos's accounting and tax systems for FY 2025.

**Singapore Jurisdictional Data**

| Entity | GloBE Income (€) | GloBE Loss (€) | Adjusted Covered Taxes (€) |
|--------|------------------|----------------|---------------------------|
| SG Singapore Pte Ltd | 12,500,000 | — | 1,562,500 |
| SG Singapore Tech Pte Ltd | 4,800,000 | — | 600,000 |
| **Singapore Total** | **17,300,000** | **—** | **2,162,500** |

**Ireland Jurisdictional Data**

| Entity | GloBE Income (€) | GloBE Loss (€) | Adjusted Covered Taxes (€) |
|--------|------------------|----------------|---------------------------|
| SG Ireland Ltd | 5,200,000 | — | 650,000 |
| SG Ireland IP Ltd | 2,100,000 | — | 262,500 |
| **Ireland Total** | **7,300,000** | **—** | **912,500** |

**Other Jurisdictions (for reference)**

| Jurisdiction | Net GloBE Income (€) | Adjusted Covered Taxes (€) | ETR |
|--------------|---------------------|---------------------------|-----|
| UK | 45,600,000 | 10,944,000 | 24.0% |
| Netherlands | 8,400,000 | 2,100,000 | 25.0% |
| Germany | 22,300,000 | 6,690,000 | 30.0% |
| France | 15,800,000 | 3,950,000 | 25.0% |

### Your Task

Using the data above, calculate the Effective Tax Rate for Singapore and Ireland.

**GIR-001 Step 1: ETR Calculation**

The ETR formula is:

```
ETR = Adjusted Covered Taxes ÷ Net GloBE Income
```

Where Net GloBE Income = Total GloBE Income − Total GloBE Losses for the jurisdiction *(Article 5.1.2)*

### Expected Deliverable

Complete the ETR calculation for each low-tax jurisdiction:

**Singapore ETR Calculation**

| Item | Formula | Your Answer |
|------|---------|-------------|
| A. Total GloBE Income | Sum of all Singapore entities | € |
| B. Total GloBE Losses | Sum of losses (if any) | € |
| C. Net GloBE Income | A − B | € |
| D. Adjusted Covered Taxes | Sum of Singapore covered taxes | € |
| E. ETR | D ÷ C (round to 4 decimal places) | % |
| F. Low-taxed? | ETR < 15%? | Yes / No |

**Ireland ETR Calculation**

| Item | Formula | Your Answer |
|------|---------|-------------|
| A. Total GloBE Income | Sum of all Ireland entities | € |
| B. Total GloBE Losses | Sum of losses (if any) | € |
| C. Net GloBE Income | A − B | € |
| D. Adjusted Covered Taxes | Sum of Ireland covered taxes | € |
| E. ETR | D ÷ C (round to 4 decimal places) | % |
| F. Low-taxed? | ETR < 15%? | Yes / No |

---

## Task 2: SBIE Calculation (GIR-001 Step 2)

### Data Provided

**Singapore Substance Data (FY 2025)**

| Entity | Eligible Employees | Eligible Payroll Costs (€) | Tangible Assets NBV (€) |
|--------|-------------------|---------------------------|------------------------|
| SG Singapore Pte Ltd | 85 | 6,200,000 | 4,500,000 |
| SG Singapore Tech Pte Ltd | 120 | 8,400,000 | 12,800,000 |
| **Singapore Total** | **205** | **14,600,000** | **17,300,000** |

**Ireland Substance Data (FY 2025)**

| Entity | Eligible Employees | Eligible Payroll Costs (€) | Tangible Assets NBV (€) |
|--------|-------------------|---------------------------|------------------------|
| SG Ireland Ltd | 45 | 3,800,000 | 2,200,000 |
| SG Ireland IP Ltd | 12 | 1,400,000 | 850,000 |
| **Ireland Total** | **57** | **5,200,000** | **3,050,000** |

**SBIE Transition Rates for FY 2025** *(Article 9.1)*

| Carve-Out | Rate |
|-----------|------|
| Payroll | 9.8% |
| Tangible Assets | 7.8% |

### Your Task

Calculate the Substance-Based Income Exclusion for Singapore and Ireland using the FY 2025 transition rates.

**GIR-001 Step 2: SBIE Calculation**

The SBIE formula is:

```
SBIE = (Eligible Payroll Costs × Payroll Rate) + (Tangible Assets NBV × Asset Rate)
```

### Expected Deliverable

**Singapore SBIE Calculation**

| Item | Formula | Your Answer |
|------|---------|-------------|
| A. Eligible Payroll Costs | From data provided | € |
| B. Payroll Rate (FY 2025) | From transition table | % |
| C. Payroll Carve-Out | A × B | € |
| D. Tangible Assets NBV | From data provided | € |
| E. Asset Rate (FY 2025) | From transition table | % |
| F. Asset Carve-Out | D × E | € |
| **G. Total SBIE** | **C + F** | **€** |

**Ireland SBIE Calculation**

| Item | Formula | Your Answer |
|------|---------|-------------|
| A. Eligible Payroll Costs | From data provided | € |
| B. Payroll Rate (FY 2025) | From transition table | % |
| C. Payroll Carve-Out | A × B | € |
| D. Tangible Assets NBV | From data provided | € |
| E. Asset Rate (FY 2025) | From transition table | % |
| F. Asset Carve-Out | D × E | € |
| **G. Total SBIE** | **C + F** | **€** |

---

## Task 3: Top-Up Tax Calculation (GIR-001 Step 3)

### Data Provided

Use your answers from Tasks 1 and 2, plus the following additional information:

**QDMTT Status**

| Jurisdiction | Has QDMTT? | QDMTT Amount Paid (€) |
|--------------|-----------|----------------------|
| Singapore | No | — |
| Ireland | Yes | 480,000 |

### Your Task

Calculate the Jurisdictional Top-Up Tax for Singapore and Ireland.

**GIR-001 Step 3: Top-Up Tax Calculation**

The Top-Up Tax formula is:

```
Top-Up Tax Percentage = 15% − ETR  (Article 5.2.1)
Excess Profit = Net GloBE Income − SBIE  (Article 5.2.2)
Jurisdictional Top-Up Tax = (Top-Up Tax % × Excess Profit) − QDMTT  (Article 5.2.3)
```

### Expected Deliverable

**Singapore Top-Up Tax Calculation**

| Item | Formula | Your Answer |
|------|---------|-------------|
| A. Net GloBE Income | From Task 1 | € |
| B. ETR | From Task 1 | % |
| C. Top-Up Tax Percentage | 15% − B (if B < 15%) | % |
| D. SBIE | From Task 2 | € |
| E. Excess Profit | A − D | € |
| F. Initial Top-Up Tax | C × E | € |
| G. QDMTT Offset | From data provided | € |
| **H. Jurisdictional Top-Up Tax** | **F − G** | **€** |

**Ireland Top-Up Tax Calculation**

| Item | Formula | Your Answer |
|------|---------|-------------|
| A. Net GloBE Income | From Task 1 | € |
| B. ETR | From Task 1 | % |
| C. Top-Up Tax Percentage | 15% − B (if B < 15%) | % |
| D. SBIE | From Task 2 | € |
| E. Excess Profit | A − D | € |
| F. Initial Top-Up Tax | C × E | € |
| G. QDMTT Offset | From data provided | € |
| **H. Jurisdictional Top-Up Tax** | **F − G** | **€** |

---

## Task 4: Entity Allocation Within Jurisdictions

### Your Task

Allocate the Jurisdictional Top-Up Tax to individual Constituent Entities within each low-taxed jurisdiction.

**Allocation Rule** *(Article 5.2.4)*: Top-Up Tax is allocated to CEs in proportion to their share of positive GloBE Income in the jurisdiction.

### Expected Deliverable

**Singapore Entity Allocation**

| Entity | GloBE Income | Share of Total | Allocated Top-Up Tax |
|--------|--------------|----------------|---------------------|
| SG Singapore Pte Ltd | € | % | € |
| SG Singapore Tech Pte Ltd | € | % | € |
| **Total** | **€** | **100%** | **€** |

**Ireland Entity Allocation**

| Entity | GloBE Income | Share of Total | Allocated Top-Up Tax |
|--------|--------------|----------------|---------------------|
| SG Ireland Ltd | € | % | € |
| SG Ireland IP Ltd | € | % | € |
| **Total** | **€** | **100%** | **€** |

---

## Task 5: IIR Allocation to Parent Entities

### Data Provided (Ownership Details)

**Singapore Ownership Chain:**
```
Stratos Group plc (UK) — 100%
    └── SG Holdings Ltd (UK) — 100%
            └── SG Netherlands BV (Netherlands) — 100%
                    └── SG Singapore Pte Ltd (Singapore) — 100%
                            └── SG Singapore Tech Pte Ltd (Singapore) — 100%
```

**Ireland Ownership Chain:**
```
Stratos Group plc (UK) — 100%
    └── SG Holdings Ltd (UK) — 100%
            └── SG Netherlands BV (Netherlands) — 60% ← 40% held by External Investor A
                    └── SG Ireland Ltd (Ireland) — 100%
                            └── SG Ireland IP Ltd (Ireland) — 100%
```

**Note:** External Investor A is not part of an MNE Group subject to Pillar Two.

### Your Task

Calculate the Allocable Share under IIR for each parent entity in the ownership chain.

**IIR Allocation Formula** *(Article 2.2)*:

```
Allocable Share = Entity Top-Up Tax × Inclusion Ratio
Inclusion Ratio = (GloBE Income − Amount to other owners) ÷ GloBE Income
```

### Expected Deliverable

**Singapore IIR Allocation**

| Step | Calculation | Result |
|------|-------------|--------|
| 1. Singapore jurisdictional Top-Up Tax | From Task 3 | € |
| 2. Stratos's ownership of Singapore entities | Direct + indirect | % |
| 3. Stratos's Inclusion Ratio | (Based on 100% ownership) | % |
| 4. **Stratos's Allocable Share (IIR)** | Top-Up Tax × Inclusion Ratio | **€** |

**Ireland IIR Allocation**

Work through the ownership chain to determine IIR allocation:

| Step | Description | Calculation | Result |
|------|-------------|-------------|--------|
| 1 | Ireland jurisdictional Top-Up Tax | From Task 3 | € |
| 2 | SG Netherlands BV ownership of Ireland entities | Direct | % |
| 3 | External Investor's share of GloBE Income | 40% of Ireland GloBE Income | € |
| 4 | Netherlands Inclusion Ratio in Ireland | (Total − External share) ÷ Total | % |
| 5 | Netherlands Allocable Share (if Netherlands IIR applies) | Top-Up Tax × Netherlands Ratio | € |
| 6 | Stratos's ownership of Netherlands | Via SG Holdings | % |
| 7 | **Stratos's Allocable Share (IIR)** | Netherlands share × Stratos ownership | **€** |

**Question:** Does the 40% external investor portion get collected under IIR?

---

## Task 6: Determine if UTPR Applies

### Your Task

Analyse whether any Top-Up Tax remains uncollected after IIR and determine if UTPR allocation is required.

### Expected Deliverable

**Singapore Analysis**

| Item | Value | Notes |
|------|-------|-------|
| A. Total Singapore Top-Up Tax | € | From Task 3 |
| B. IIR Allocable Share (Stratos) | € | From Task 5 |
| C. IIR collection rate | % | B ÷ A |
| D. Residual for UTPR | € | A − B |

**Conclusion:** Does UTPR apply to Singapore? ______

**Ireland Analysis**

| Item | Value | Notes |
|------|-------|-------|
| A. Total Ireland Top-Up Tax | € | From Task 3 |
| B. IIR Allocable Share (Stratos) | € | From Task 5 |
| C. External Investor share | € | 40% not collected under IIR |
| D. IIR collection rate | % | B ÷ A |
| E. Residual for UTPR | € | A − B |

**Conclusion:** Does UTPR apply to Ireland? ______

---

## Task 7: UTPR Allocation (If Applicable)

### Data Provided

**Stratos Group UTPR Jurisdiction Data (Qualified UTPR jurisdictions only)**

| Jurisdiction | Eligible Employees | Tangible Assets (€M) |
|--------------|-------------------|---------------------|
| UK | 450 | 85.0 |
| Netherlands | 95 | 18.5 |
| Germany | 185 | 32.0 |
| France | 120 | 22.5 |
| **Total** | **850** | **158.0** |

### Your Task

If UTPR applies (from Task 6), allocate the residual Top-Up Tax across UTPR jurisdictions using the substance-based formula.

**UTPR Allocation Formula** *(Article 2.6)*:

```
UTPR % = (Employee Factor × 50%) + (Tangible Asset Factor × 50%)
Employee Factor = Jurisdiction employees ÷ Total UTPR employees
Asset Factor = Jurisdiction assets ÷ Total UTPR assets
```

### Expected Deliverable

**UTPR Percentage Calculation**

| Jurisdiction | Employees | Emp Factor | Assets (€M) | Asset Factor | Emp×50% | Asset×50% | **UTPR %** |
|--------------|-----------|------------|-------------|--------------|---------|-----------|-----------|
| UK | 450 | % | 85.0 | % | % | % | **%** |
| Netherlands | 95 | % | 18.5 | % | % | % | **%** |
| Germany | 185 | % | 32.0 | % | % | % | **%** |
| France | 120 | % | 22.5 | % | % | % | **%** |
| **Total** | **850** | **100%** | **158.0** | **100%** | | | **100%** |

**UTPR Allocation of Residual Top-Up Tax**

| Jurisdiction | UTPR % | Residual × UTPR % | **Allocated UTPR** |
|--------------|--------|-------------------|-------------------|
| UK | % | € | **€** |
| Netherlands | % | € | **€** |
| Germany | % | € | **€** |
| France | % | € | **€** |
| **Total** | **100%** | | **€** |

---

## Task 8: Complete Top-Up Tax Summary

### Your Task

Prepare a summary of all Top-Up Tax allocations for Stratos's FY 2025 GIR filing.

### Expected Deliverable

**Top-Up Tax Summary by Mechanism**

| Source Jurisdiction | Total Top-Up Tax | IIR Amount | UTPR Amount | Collection Rate |
|--------------------|------------------|------------|-------------|-----------------|
| Singapore | € | € | € | % |
| Ireland | € | € | € | % |
| **Total** | **€** | **€** | **€** | **%** |

**Top-Up Tax by Collecting Jurisdiction**

| Collecting Jurisdiction | Mechanism | Source | Amount |
|------------------------|-----------|--------|--------|
| UK (Stratos Group plc) | IIR | Singapore | € |
| UK (Stratos Group plc) | IIR | Ireland | € |
| UK | UTPR | Ireland (residual) | € |
| Netherlands | UTPR | Ireland (residual) | € |
| Germany | UTPR | Ireland (residual) | € |
| France | UTPR | Ireland (residual) | € |
| **Total** | | | **€** |

---

## Model Answers

### Task 1: ETR Calculation

**Singapore ETR Calculation**

| Item | Formula | Answer |
|------|---------|--------|
| A. Total GloBE Income | €12,500,000 + €4,800,000 | **€17,300,000** |
| B. Total GloBE Losses | No losses | **€0** |
| C. Net GloBE Income | €17,300,000 − €0 | **€17,300,000** |
| D. Adjusted Covered Taxes | €1,562,500 + €600,000 | **€2,162,500** |
| E. ETR | €2,162,500 ÷ €17,300,000 | **12.50%** |
| F. Low-taxed? | 12.50% < 15% | **Yes** |

**Ireland ETR Calculation**

| Item | Formula | Answer |
|------|---------|--------|
| A. Total GloBE Income | €5,200,000 + €2,100,000 | **€7,300,000** |
| B. Total GloBE Losses | No losses | **€0** |
| C. Net GloBE Income | €7,300,000 − €0 | **€7,300,000** |
| D. Adjusted Covered Taxes | €650,000 + €262,500 | **€912,500** |
| E. ETR | €912,500 ÷ €7,300,000 | **12.50%** |
| F. Low-taxed? | 12.50% < 15% | **Yes** |

---

### Task 2: SBIE Calculation

**Singapore SBIE Calculation**

| Item | Formula | Answer |
|------|---------|--------|
| A. Eligible Payroll Costs | From data | **€14,600,000** |
| B. Payroll Rate (FY 2025) | Transition rate | **9.8%** |
| C. Payroll Carve-Out | €14,600,000 × 9.8% | **€1,430,800** |
| D. Tangible Assets NBV | From data | **€17,300,000** |
| E. Asset Rate (FY 2025) | Transition rate | **7.8%** |
| F. Asset Carve-Out | €17,300,000 × 7.8% | **€1,349,400** |
| **G. Total SBIE** | €1,430,800 + €1,349,400 | **€2,780,200** |

**Ireland SBIE Calculation**

| Item | Formula | Answer |
|------|---------|--------|
| A. Eligible Payroll Costs | From data | **€5,200,000** |
| B. Payroll Rate (FY 2025) | Transition rate | **9.8%** |
| C. Payroll Carve-Out | €5,200,000 × 9.8% | **€509,600** |
| D. Tangible Assets NBV | From data | **€3,050,000** |
| E. Asset Rate (FY 2025) | Transition rate | **7.8%** |
| F. Asset Carve-Out | €3,050,000 × 7.8% | **€237,900** |
| **G. Total SBIE** | €509,600 + €237,900 | **€747,500** |

---

### Task 3: Top-Up Tax Calculation

**Singapore Top-Up Tax Calculation**

| Item | Formula | Answer |
|------|---------|--------|
| A. Net GloBE Income | From Task 1 | **€17,300,000** |
| B. ETR | From Task 1 | **12.50%** |
| C. Top-Up Tax Percentage | 15% − 12.50% | **2.50%** |
| D. SBIE | From Task 2 | **€2,780,200** |
| E. Excess Profit | €17,300,000 − €2,780,200 | **€14,519,800** |
| F. Initial Top-Up Tax | 2.50% × €14,519,800 | **€362,995** |
| G. QDMTT Offset | No Singapore QDMTT | **€0** |
| **H. Jurisdictional Top-Up Tax** | €362,995 − €0 | **€362,995** |

**Ireland Top-Up Tax Calculation**

| Item | Formula | Answer |
|------|---------|--------|
| A. Net GloBE Income | From Task 1 | **€7,300,000** |
| B. ETR | From Task 1 | **12.50%** |
| C. Top-Up Tax Percentage | 15% − 12.50% | **2.50%** |
| D. SBIE | From Task 2 | **€747,500** |
| E. Excess Profit | €7,300,000 − €747,500 | **€6,552,500** |
| F. Initial Top-Up Tax | 2.50% × €6,552,500 | **€163,813** |
| G. QDMTT Offset | Ireland QDMTT paid | **€163,813*** |
| **H. Jurisdictional Top-Up Tax** | €163,813 − €163,813 | **€0** |

*The Ireland QDMTT fully covers the Top-Up Tax due.

**Important Finding:** Ireland has no residual Top-Up Tax for IIR/UTPR because the Irish QDMTT already collects the full amount.

---

### Task 4: Entity Allocation Within Jurisdictions

**Singapore Entity Allocation**

| Entity | GloBE Income | Share of Total | Allocated Top-Up Tax |
|--------|--------------|----------------|---------------------|
| SG Singapore Pte Ltd | €12,500,000 | 72.25% | €262,264 |
| SG Singapore Tech Pte Ltd | €4,800,000 | 27.75% | €100,731 |
| **Total** | **€17,300,000** | **100%** | **€362,995** |

**Ireland Entity Allocation**

| Entity | GloBE Income | Share of Total | Allocated Top-Up Tax |
|--------|--------------|----------------|---------------------|
| SG Ireland Ltd | €5,200,000 | 71.23% | €0* |
| SG Ireland IP Ltd | €2,100,000 | 28.77% | €0* |
| **Total** | **€7,300,000** | **100%** | **€0*** |

*Ireland Top-Up Tax is €0 after QDMTT offset.

---

### Task 5: IIR Allocation to Parent Entities

**Singapore IIR Allocation**

| Step | Calculation | Result |
|------|-------------|--------|
| 1. Singapore jurisdictional Top-Up Tax | From Task 3 | **€362,995** |
| 2. Stratos's ownership of Singapore entities | 100% × 100% × 100% | **100%** |
| 3. Stratos's Inclusion Ratio | No external ownership | **100%** |
| 4. **Stratos's Allocable Share (IIR)** | €362,995 × 100% | **€362,995** |

The UK (Stratos Group plc) applies its Qualified IIR and collects the full €362,995.

**Ireland IIR Allocation**

| Step | Description | Calculation | Result |
|------|-------------|-------------|--------|
| 1 | Ireland jurisdictional Top-Up Tax | From Task 3 | **€0** |
| 2-7 | IIR allocation | Not applicable | **€0** |

**No IIR allocation required for Ireland** because the QDMTT has already collected the Top-Up Tax.

**Answer to Question:** The 40% external investor portion is irrelevant in this case because Ireland's QDMTT collected 100% of the Top-Up Tax. If there had been residual Top-Up Tax, the external investor's 40% share would not be collected under IIR (since the investor is not part of an MNE Group). That portion would flow to UTPR.

---

### Task 6: Determine if UTPR Applies

**Singapore Analysis**

| Item | Value | Notes |
|------|-------|-------|
| A. Total Singapore Top-Up Tax | €362,995 | From Task 3 |
| B. IIR Allocable Share (Stratos) | €362,995 | From Task 5 |
| C. IIR collection rate | 100% | Full collection |
| D. Residual for UTPR | €0 | A − B |

**Conclusion:** UTPR does **not** apply to Singapore. The UK IIR collects 100%.

**Ireland Analysis**

| Item | Value | Notes |
|------|-------|-------|
| A. Total Ireland Top-Up Tax | €0 | After QDMTT offset |
| B. IIR Allocable Share | €0 | Nothing to allocate |
| C. External Investor share | €0 | N/A |
| D. IIR collection rate | N/A | No Top-Up Tax due |
| E. Residual for UTPR | €0 | Nothing remaining |

**Conclusion:** UTPR does **not** apply to Ireland. The Irish QDMTT already collected the Top-Up Tax.

---

### Task 7: UTPR Allocation

**No UTPR allocation required** for FY 2025 because:

1. Singapore Top-Up Tax: 100% collected under UK IIR
2. Ireland Top-Up Tax: 100% collected under Irish QDMTT

The UTPR calculations are therefore **not applicable** in this case study. The UTPR allocation template is provided for reference if there had been residual Top-Up Tax.

**What If Scenario:** If Ireland did NOT have a QDMTT, the 40% external investor share (€65,525) would flow to UTPR allocation across UK, Netherlands, Germany, and France using the substance-based formula.

---

### Task 8: Complete Top-Up Tax Summary

**Top-Up Tax Summary by Mechanism**

| Source Jurisdiction | Total Top-Up Tax | QDMTT | IIR Amount | UTPR Amount | Collection Rate |
|--------------------|------------------|-------|------------|-------------|-----------------|
| Singapore | €362,995 | €0 | €362,995 | €0 | 100% |
| Ireland | €163,813 | €163,813 | €0 | €0 | 100% |
| **Total** | **€526,808** | **€163,813** | **€362,995** | **€0** | **100%** |

**Top-Up Tax by Collecting Jurisdiction**

| Collecting Jurisdiction | Mechanism | Source | Amount |
|------------------------|-----------|--------|--------|
| Ireland (QDMTT) | QDMTT | Ireland | €163,813 |
| UK (Stratos Group plc) | IIR | Singapore | €362,995 |
| **Total** | | | **€526,808** |

---

## Learning Points

1. **QDMTT eliminates IIR/UTPR obligation** — Ireland's domestic top-up tax means Stratos has no additional IIR liability for Ireland, regardless of the 40% external investor.

2. **The three-step GloBE Calculator workflow matters** — You cannot calculate allocation without first computing ETR (Step 1), SBIE (Step 2), and Top-Up Tax (Step 3).

3. **Jurisdictional blending affects ETR** — Both Singapore entities' income and taxes are combined for a single Singapore ETR of 12.50%.

4. **SBIE reduces the Top-Up Tax base significantly** — Singapore's SBIE of €2.78M reduced the excess profit from €17.3M to €14.5M, lowering the Top-Up Tax by approximately €70,000.

5. **100% ownership simplifies IIR** — When the UPE has 100% direct/indirect ownership, the Inclusion Ratio is 100% and all Top-Up Tax is collected under the UPE's IIR.

6. **External investors create potential UTPR situations** — The 40% external investor in Ireland would have created a UTPR situation if Ireland had no QDMTT.

7. **Check qualified IIR/UTPR status early** — Knowing that UK has Qualified IIR determined that Stratos Group plc would be the collecting entity.

8. **Document the complete calculation chain** — The GIR filing requires disclosure of each step: ETR, SBIE, Top-Up Tax, entity allocation, and parent allocation.

---

## GIR Filing Integration

The calculations completed in this case study feed directly into the following GIR sections:

| GIR Section | Data Source | This Case Study Task |
|-------------|-------------|---------------------|
| Section 2: Jurisdictional ETR | ETR by jurisdiction | Task 1 |
| Section 2: SBIE | Payroll and asset carve-outs | Task 2 |
| Section 2: Top-Up Tax | Jurisdictional Top-Up Tax | Task 3 |
| Section 3: Entity Allocation | CE-level Top-Up Tax | Task 4 |
| Section 4: IIR Amounts | Parent Allocable Shares | Task 5 |
| Section 5: UTPR Amounts | UTPR allocation by jurisdiction | Task 7 (if applicable) |

Use **GIR-004 GIR Practice Form** to practice entering this data in the official filing format.

---

## Alternative Scenario: What If Ireland Had No QDMTT?

For additional practice, recalculate Tasks 5-8 assuming Ireland has **no QDMTT**:

**Revised Ireland Top-Up Tax:** €163,813 (no offset)

**Revised IIR Allocation:**
- Stratos's 60% share: €163,813 × 60% = €98,288 (UK IIR)
- External Investor's 40%: €163,813 × 40% = €65,525 (not collected under IIR)

**UTPR Allocation of €65,525:**

| Jurisdiction | UTPR % | Allocated |
|--------------|--------|-----------|
| UK | 53.75%* | €35,220 |
| Netherlands | 11.85%* | €7,765 |
| Germany | 21.22%* | €13,904 |
| France | 13.18%* | €8,636 |
| **Total** | **100%** | **€65,525** |

*Based on the 50/50 employee/asset formula from Task 7 data.

This alternative scenario demonstrates the UTPR backstop function when IIR does not achieve full collection.

---

## Next Step

You have completed Part 2: The Charging Mechanism. You understand how to:
- Calculate ETR, SBIE, and Top-Up Tax using GIR-001
- Allocate Top-Up Tax to entities within a jurisdiction
- Determine parent Allocable Shares under IIR
- Apply UTPR when IIR does not achieve full collection

Proceed to **Part 3: Computing GloBE Income or Loss** to learn how to calculate the GloBE Income figures that feed into these calculations.
