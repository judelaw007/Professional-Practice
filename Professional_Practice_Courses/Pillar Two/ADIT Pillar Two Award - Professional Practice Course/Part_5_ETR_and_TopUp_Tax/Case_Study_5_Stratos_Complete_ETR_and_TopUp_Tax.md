# Case Study 5: Stratos's Complete ETR and Top-Up Tax Calculation

## Introduction

This case study brings together all concepts from Chapters 5.1 to 5.6. You will compute the Effective Tax Rate for each jurisdiction, apply the Substance-Based Income Exclusion (SBIE), calculate Top-up Tax, apply the De Minimis Exclusion and QDMTT offsets, and handle a Minority-Owned Constituent Entity.

**Important:** Work through each task systematically. Complete the ETR calculation for all jurisdictions before proceeding to SBIE and Top-up Tax calculations. Apply exclusions and offsets in the correct order.

**Time estimate:** 120-150 minutes

---

## Background: Stratos Group — FY 2025 Complete Top-Up Tax Computation

Stratos Group has completed its GloBE Income calculations (Case Study 3) and Covered Tax computations (Case Study 4). The tax team must now bring these together to determine ETR, SBIE, and any Top-up Tax liability across all jurisdictions.

### Entity Overview

| Entity | Jurisdiction | GloBE Income (€) | Adj. Covered Taxes (€) | Role |
|--------|--------------|------------------|------------------------|------|
| Stratos Holdings plc | UK | 8,500,000 | 2,125,000 | Ultimate Parent Entity |
| SG Germany GmbH | Germany | 53,880,000 | 12,393,000 | Operating subsidiary |
| SG Singapore Pte Ltd | Singapore | 4,000,000 | 392,206 | IP holding company |
| SG Ireland Ltd | Ireland | 15,000,000 | 1,770,000 | European HQ |
| SG Luxembourg S.à r.l. | Luxembourg | 630,000 | 55,000 | Treasury services |
| Atlas Ireland Ltd | Ireland | 2,400,000 | 288,000 | Shared services (28% MOCE) |

### Ownership Structure

```
Stratos Holdings plc (UK) — 100%
    │
    ├── SG Germany GmbH (Germany) — 100%
    │
    ├── SG Singapore Pte Ltd (Singapore) — 100%
    │
    ├── SG Ireland Ltd (Ireland) — 100%
    │
    ├── SG Luxembourg S.à r.l. (Luxembourg) — 100%
    │
    └── Atlas Ireland Ltd (Ireland) — 28% (MOCE)
            └── Consolidated due to management contract control
```

---

## Data Package

### Substance Data by Jurisdiction

**For SBIE Calculation (FY 2025 transition rates: 9.0% payroll, 7.0% tangible assets)**

| Jurisdiction | Eligible Payroll (€) | Tangible Assets NBV (€) |
|--------------|---------------------|-------------------------|
| UK | 4,200,000 | 2,800,000 |
| Germany | 12,500,000 | 18,000,000 |
| Singapore | 1,200,000 | 850,000 |
| Ireland (Main Group) | 8,400,000 | 12,000,000 |
| Luxembourg | 320,000 | 180,000 |
| Atlas Ireland (MOCE) | 1,200,000 | 800,000 |

### Three-Year Revenue and Income Data (for De Minimis)

**Luxembourg — SG Luxembourg S.à r.l.**

| Fiscal Year | GloBE Revenue (€) | GloBE Income (€) |
|-------------|-------------------|------------------|
| FY 2023 | 7,900,000 | 580,000 |
| FY 2024 | 8,400,000 | 650,000 |
| FY 2025 | 9,200,000 | 630,000 |

### QDMTT Implementation Status

| Jurisdiction | Has QDMTT? | Effective Date |
|--------------|------------|----------------|
| UK | Yes | 1 Jan 2024 |
| Germany | Yes | 1 Jan 2024 |
| Singapore | No | — |
| Ireland | Yes | 1 Jan 2024 |
| Luxembourg | Yes | 1 Jan 2024 |

### MOCE Data — Atlas Ireland Ltd

| Item | Data |
|------|------|
| UPE ownership | 28% (direct) |
| Basis for consolidation | Management contract control |
| Part of Minority-Owned Sub-Group? | No |
| Classification | Stand-alone MOCE |

---

## Task 1: ETR Calculation for All Jurisdictions

### Your Task

Calculate the Effective Tax Rate for each jurisdiction using the formula:

```
ETR = Adjusted Covered Taxes ÷ Jurisdictional Net GloBE Income
```

For the MOCE (Atlas Ireland Ltd), calculate ETR separately as required by Article 5.6.2.

### Expected Deliverable

**ETR Calculation Worksheet**

| # | Jurisdiction | GloBE Income (€) | Adj. Covered Taxes (€) | ETR | Low-taxed? |
|---|--------------|------------------|------------------------|-----|------------|
| 1 | UK | | | | |
| 2 | Germany | | | | |
| 3 | Singapore | | | | |
| 4 | Ireland (Main Group) | | | | |
| 5 | Luxembourg | | | | |
| 6 | Atlas Ireland (MOCE) | | | | |

**Note:** A jurisdiction is "low-taxed" if ETR < 15%.

**Summary:**

```
Total jurisdictions assessed:           ______
Jurisdictions with ETR ≥ 15%:          ______
Jurisdictions with ETR < 15%:          ______
```

---

## Task 2: Apply De Minimis Exclusion Assessment

### Your Task

Assess whether Luxembourg qualifies for the De Minimis Exclusion under Article 5.5.1 using the three-year average thresholds:
- Average GloBE Revenue < €10 million
- Average GloBE Income < €1 million

### Expected Deliverable

**De Minimis Assessment — Luxembourg**

**Step 1: Calculate Three-Year Averages**

| Fiscal Year | GloBE Revenue (€) | GloBE Income (€) |
|-------------|-------------------|------------------|
| FY 2023 | | |
| FY 2024 | | |
| FY 2025 | | |
| **Total** | | |
| **Average (÷ 3)** | | |

**Step 2: Apply Thresholds**

| Test | Average | Threshold | Pass? |
|------|---------|-----------|-------|
| Revenue Test | €__________ | < €10 million | |
| Income Test | €__________ | < €1 million | |

**Step 3: Conclusion**

```
Does Luxembourg qualify for De Minimis Exclusion?   YES / NO

If YES:
→ No ETR calculation required for Luxembourg
→ GloBE Income deemed €0
→ Top-up Tax deemed €0
→ Election made: YES

If NO:
→ Proceed with full ETR and Top-up Tax calculation
```

---

## Task 3: SBIE Calculation for Low-Taxed Jurisdictions

### Your Task

For each jurisdiction with ETR < 15% (excluding any qualifying for De Minimis), calculate the Substance-Based Income Exclusion using FY 2025 transition rates:
- Payroll carve-out: 9.0%
- Tangible asset carve-out: 7.0%

### Expected Deliverable

**SBIE Calculation — Singapore**

| Component | Eligible Amount (€) | Rate (2025) | Carve-out (€) |
|-----------|---------------------|-------------|---------------|
| Payroll | | 9.0% | |
| Tangible Assets (NBV) | | 7.0% | |
| **Total SBIE** | | | |

**Excess Profit Calculation**

```
Net GloBE Income:                       €__________________
Less: SBIE:                            (€__________________)
                                        ────────────────────
Excess Profit:                          €__________________
```

---

**SBIE Calculation — Ireland (Main Group)**

| Component | Eligible Amount (€) | Rate (2025) | Carve-out (€) |
|-----------|---------------------|-------------|---------------|
| Payroll | | 9.0% | |
| Tangible Assets (NBV) | | 7.0% | |
| **Total SBIE** | | | |

**Excess Profit Calculation**

```
Net GloBE Income:                       €__________________
Less: SBIE:                            (€__________________)
                                        ────────────────────
Excess Profit:                          €__________________
```

---

**SBIE Calculation — Atlas Ireland Ltd (MOCE)**

| Component | Eligible Amount (€) | Rate (2025) | Carve-out (€) |
|-----------|---------------------|-------------|---------------|
| Payroll | | 9.0% | |
| Tangible Assets (NBV) | | 7.0% | |
| **Total SBIE** | | | |

**Excess Profit Calculation**

```
Net GloBE Income:                       €__________________
Less: SBIE:                            (€__________________)
                                        ────────────────────
Excess Profit:                          €__________________
```

---

## Task 4: Top-Up Tax Computation

### Your Task

For each low-taxed jurisdiction (excluding De Minimis), calculate:
1. Top-up Tax Percentage (15% − ETR)
2. Jurisdictional Top-up Tax (Top-up Tax % × Excess Profit)

### Expected Deliverable

**Top-Up Tax Calculation — Singapore**

| Step | Calculation | Result |
|------|-------------|--------|
| Top-up Tax % | 15% − ______% | ______% |
| Excess Profit | From Task 3 | €____________ |
| **Jurisdictional Top-up Tax** | ______% × €____________ | **€____________** |

---

**Top-Up Tax Calculation — Ireland (Main Group)**

| Step | Calculation | Result |
|------|-------------|--------|
| Top-up Tax % | 15% − ______% | ______% |
| Excess Profit | From Task 3 | €____________ |
| **Jurisdictional Top-up Tax** | ______% × €____________ | **€____________** |

---

**Top-Up Tax Calculation — Atlas Ireland Ltd (MOCE)**

| Step | Calculation | Result |
|------|-------------|--------|
| Top-up Tax % | 15% − ______% | ______% |
| Excess Profit | From Task 3 | €____________ |
| **MOCE Top-up Tax** | ______% × €____________ | **€____________** |

---

## Task 5: Apply QDMTT Offsets

### Your Task

For jurisdictions with QDMTT, determine whether the QDMTT offsets the Jurisdictional Top-up Tax. Calculate the Net Top-up Tax (IIR/UTPR liability).

### Expected Deliverable

**QDMTT Offset Analysis**

| Jurisdiction | Jur. Top-up Tax (€) | Has QDMTT? | QDMTT Paid (€) | Net Top-up Tax (€) |
|--------------|---------------------|------------|----------------|-------------------|
| Singapore | | | | |
| Ireland (Main) | | | | |
| Atlas Ireland (MOCE) | | | | |

**Notes:**

```
Singapore: _____________________________________________________________

Ireland (Main): ________________________________________________________

Atlas Ireland (MOCE): __________________________________________________
```

---

## Task 6: Consolidated Top-Up Tax Summary

### Your Task

Prepare a consolidated summary showing:
1. All jurisdictions assessed
2. ETR by jurisdiction
3. Top-up Tax before and after exclusions/offsets
4. Final IIR liability for Stratos Holdings plc

### Expected Deliverable

**Jurisdiction Summary Table**

| Jurisdiction | GloBE Income (€) | ETR | Top-up Tax % | Exclusion/Offset | Final Liability (€) |
|--------------|------------------|-----|--------------|------------------|---------------------|
| UK | | | | | |
| Germany | | | | | |
| Singapore | | | | | |
| Ireland (Main) | | | | | |
| Luxembourg | | | | | |
| Atlas Ireland (MOCE) | | | | | |
| **TOTAL** | | | | | |

**IIR Liability Summary**

| Item | Amount (€) |
|------|------------|
| Singapore Top-up Tax (IIR) | |
| Ireland Top-up Tax (QDMTT offset) | |
| Luxembourg (De Minimis) | |
| Atlas Ireland (QDMTT offset) | |
| **Total IIR Liability** | |

**Where Is Top-up Tax Paid?**

| Amount (€) | Recipient | Mechanism |
|------------|-----------|-----------|
| | | IIR |
| | | QDMTT |
| | | QDMTT |
| **Total** | | |

---

## Task 7: MOCE Verification and Separate Treatment

### Your Task

Verify the MOCE treatment for Atlas Ireland Ltd and confirm the separate calculation was applied correctly per Article 5.6.2.

### Expected Deliverable

**MOCE Verification Checklist**

| Question | Answer | Reference |
|----------|--------|-----------|
| Is UPE ownership ≤ 30%? | | Art. 10.1 |
| Is entity consolidated? | | |
| Is entity an Investment Entity? | | Art. 7.4/7.5 |
| Is entity part of a Minority-Owned Sub-Group? | | |
| **Classification** | | |

**Separate Calculation Verification**

| Item | Main Group Ireland | Atlas Ireland (MOCE) | Combined? |
|------|-------------------|---------------------|-----------|
| GloBE Income | | | NO |
| Covered Taxes | | | NO |
| ETR calculated separately? | | | |
| SBIE calculated separately? | | | |
| Top-up Tax calculated separately? | | | |

**Why Separate Treatment?**

```
Explanation: _____________________________________________________________

____________________________________________________________________________

____________________________________________________________________________
```

---

## Model Answers

### Answer 1: ETR Calculation

**ETR Calculation Worksheet**

| # | Jurisdiction | GloBE Income (€) | Adj. Covered Taxes (€) | ETR | Low-taxed? |
|---|--------------|------------------|------------------------|-----|------------|
| 1 | UK | 8,500,000 | 2,125,000 | **25.00%** | No |
| 2 | Germany | 53,880,000 | 12,393,000 | **23.00%** | No |
| 3 | Singapore | 4,000,000 | 392,206 | **9.81%** | **Yes** |
| 4 | Ireland (Main) | 15,000,000 | 1,770,000 | **11.80%** | **Yes** |
| 5 | Luxembourg | 630,000 | 55,000 | **8.73%** | **Yes** |
| 6 | Atlas Ireland (MOCE) | 2,400,000 | 288,000 | **12.00%** | **Yes** |

**Calculations:**

- **UK:** €2,125,000 ÷ €8,500,000 = 25.00%
- **Germany:** €12,393,000 ÷ €53,880,000 = 23.00%
- **Singapore:** €392,206 ÷ €4,000,000 = 9.81%
- **Ireland (Main):** €1,770,000 ÷ €15,000,000 = 11.80%
- **Luxembourg:** €55,000 ÷ €630,000 = 8.73%
- **Atlas Ireland:** €288,000 ÷ €2,400,000 = 12.00%

**Summary:**

```
Total jurisdictions assessed:           6
Jurisdictions with ETR ≥ 15%:          2 (UK, Germany)
Jurisdictions with ETR < 15%:          4 (Singapore, Ireland Main, Luxembourg, Atlas Ireland)
```

---

### Answer 2: De Minimis Exclusion — Luxembourg

**Step 1: Calculate Three-Year Averages**

| Fiscal Year | GloBE Revenue (€) | GloBE Income (€) |
|-------------|-------------------|------------------|
| FY 2023 | 7,900,000 | 580,000 |
| FY 2024 | 8,400,000 | 650,000 |
| FY 2025 | 9,200,000 | 630,000 |
| **Total** | **25,500,000** | **1,860,000** |
| **Average (÷ 3)** | **€8,500,000** | **€620,000** |

**Step 2: Apply Thresholds**

| Test | Average | Threshold | Pass? |
|------|---------|-----------|-------|
| Revenue Test | €8,500,000 | < €10 million | **Yes** |
| Income Test | €620,000 | < €1 million | **Yes** |

**Step 3: Conclusion**

```
Does Luxembourg qualify for De Minimis Exclusion?   YES ✓

→ No ETR calculation required for Luxembourg
→ GloBE Income deemed €0
→ Top-up Tax deemed €0
→ Election made: YES

Luxembourg excluded from further Top-up Tax calculation.
```

---

### Answer 3: SBIE Calculations

**SBIE Calculation — Singapore**

| Component | Eligible Amount (€) | Rate (2025) | Carve-out (€) |
|-----------|---------------------|-------------|---------------|
| Payroll | 1,200,000 | 9.0% | **108,000** |
| Tangible Assets (NBV) | 850,000 | 7.0% | **59,500** |
| **Total SBIE** | | | **167,500** |

*Note: The chapter examples used slightly different substance figures. Using the data package values provided.*

**Alternative calculation with chapter data (€190,090):**
- Payroll: €1,300,000 × 9.0% = €117,000
- Assets: €1,044,143 × 7.0% = €73,090
- Total: €190,090

**Using Data Package values for consistency:**

**Excess Profit Calculation**

```
Net GloBE Income:                       €4,000,000
Less: SBIE:                            (€167,500)
                                        ────────────────────
Excess Profit:                          €3,832,500
```

---

**SBIE Calculation — Ireland (Main Group)**

| Component | Eligible Amount (€) | Rate (2025) | Carve-out (€) |
|-----------|---------------------|-------------|---------------|
| Payroll | 8,400,000 | 9.0% | **756,000** |
| Tangible Assets (NBV) | 12,000,000 | 7.0% | **840,000** |
| **Total SBIE** | | | **1,596,000** |

**Excess Profit Calculation**

```
Net GloBE Income:                       €15,000,000
Less: SBIE:                            (€1,596,000)
                                        ────────────────────
Excess Profit:                          €13,404,000
```

---

**SBIE Calculation — Atlas Ireland Ltd (MOCE)**

| Component | Eligible Amount (€) | Rate (2025) | Carve-out (€) |
|-----------|---------------------|-------------|---------------|
| Payroll | 1,200,000 | 9.0% | **108,000** |
| Tangible Assets (NBV) | 800,000 | 7.0% | **56,000** |
| **Total SBIE** | | | **164,000** |

**Excess Profit Calculation**

```
Net GloBE Income:                       €2,400,000
Less: SBIE:                            (€164,000)
                                        ────────────────────
Excess Profit:                          €2,236,000
```

---

### Answer 4: Top-Up Tax Computation

**Top-Up Tax Calculation — Singapore**

| Step | Calculation | Result |
|------|-------------|--------|
| Top-up Tax % | 15% − 9.81% | **5.19%** |
| Excess Profit | From Task 3 | €3,832,500 |
| **Jurisdictional Top-up Tax** | 5.19% × €3,832,500 | **€198,907** |

---

**Top-Up Tax Calculation — Ireland (Main Group)**

| Step | Calculation | Result |
|------|-------------|--------|
| Top-up Tax % | 15% − 11.80% | **3.20%** |
| Excess Profit | From Task 3 | €13,404,000 |
| **Jurisdictional Top-up Tax** | 3.20% × €13,404,000 | **€428,928** |

---

**Top-Up Tax Calculation — Atlas Ireland Ltd (MOCE)**

| Step | Calculation | Result |
|------|-------------|--------|
| Top-up Tax % | 15% − 12.00% | **3.00%** |
| Excess Profit | From Task 3 | €2,236,000 |
| **MOCE Top-up Tax** | 3.00% × €2,236,000 | **€67,080** |

---

### Answer 5: QDMTT Offsets

**QDMTT Offset Analysis**

| Jurisdiction | Jur. Top-up Tax (€) | Has QDMTT? | QDMTT Paid (€) | Net Top-up Tax (€) |
|--------------|---------------------|------------|----------------|-------------------|
| Singapore | 198,907 | **No** | 0 | **198,907** |
| Ireland (Main) | 428,928 | **Yes** | 428,928 | **0** |
| Atlas Ireland (MOCE) | 67,080 | **Yes** | 67,080 | **0** |

**Notes:**

```
Singapore: No QDMTT implemented. Full Top-up Tax of €198,907 payable via IIR
           to Stratos Holdings plc (UK).

Ireland (Main): Ireland has QDMTT effective 1 Jan 2024. Ireland collects €428,928
                domestically. No IIR liability for UK parent on Irish operations.

Atlas Ireland (MOCE): Although a MOCE with separate calculation, Ireland's QDMTT
                      still applies. Ireland collects €67,080 domestically. MOCE
                      Top-up Tax does not flow to UK parent via IIR.
```

---

### Answer 6: Consolidated Summary

**Jurisdiction Summary Table**

| Jurisdiction | GloBE Income (€) | ETR | Top-up Tax % | Exclusion/Offset | Final Liability (€) |
|--------------|------------------|-----|--------------|------------------|---------------------|
| UK | 8,500,000 | 25.00% | — | N/A | **0** |
| Germany | 53,880,000 | 23.00% | — | N/A | **0** |
| Singapore | 4,000,000 | 9.81% | 5.19% | None | **198,907 (IIR)** |
| Ireland (Main) | 15,000,000 | 11.80% | 3.20% | QDMTT | **0 (QDMTT)** |
| Luxembourg | 630,000 | 8.73% | N/A | **De Minimis** | **0** |
| Atlas Ireland (MOCE) | 2,400,000 | 12.00% | 3.00% | QDMTT | **0 (QDMTT)** |
| **TOTAL** | **84,410,000** | — | — | — | **198,907** |

**IIR Liability Summary**

| Item | Amount (€) |
|------|------------|
| Singapore Top-up Tax (IIR) | **198,907** |
| Ireland Top-up Tax (QDMTT offset) | 0 |
| Luxembourg (De Minimis) | 0 |
| Atlas Ireland (QDMTT offset) | 0 |
| **Total IIR Liability** | **198,907** |

**Where Is Top-up Tax Paid?**

| Amount (€) | Recipient | Mechanism |
|------------|-----------|-----------|
| 198,907 | UK (Stratos Holdings plc) | **IIR** |
| 428,928 | Ireland | **QDMTT** |
| 67,080 | Ireland | **QDMTT** |
| **694,915** | **Total Group Top-up Tax** | |

**Summary:**
- **Total Top-up Tax liability across group:** €694,915
- **Paid via IIR to UK:** €198,907 (Singapore)
- **Retained by Ireland via QDMTT:** €496,008 (Main Group + MOCE)
- **Luxembourg:** Excluded via De Minimis election

---

### Answer 7: MOCE Verification

**MOCE Verification Checklist**

| Question | Answer | Reference |
|----------|--------|-----------|
| Is UPE ownership ≤ 30%? | **Yes** (28%) | Art. 10.1 |
| Is entity consolidated? | **Yes** (management contract) | IFRS 10 |
| Is entity an Investment Entity? | **No** | Art. 7.4/7.5 |
| Is entity part of a Minority-Owned Sub-Group? | **No** (no MOCE subsidiaries) | Art. 10.1 |
| **Classification** | **Stand-alone MOCE** | Art. 5.6.2 |

**Separate Calculation Verification**

| Item | Main Group Ireland | Atlas Ireland (MOCE) | Combined? |
|------|-------------------|---------------------|-----------|
| GloBE Income | €15,000,000 | €2,400,000 | **NO** |
| Covered Taxes | €1,770,000 | €288,000 | **NO** |
| ETR calculated separately? | 11.80% | 12.00% | **YES** ✓ |
| SBIE calculated separately? | €1,596,000 | €164,000 | **YES** ✓ |
| Top-up Tax calculated separately? | €428,928 | €67,080 | **YES** ✓ |

**Why Separate Treatment?**

```
Explanation: Stratos Holdings plc owns only 28% of Atlas Ireland Ltd. The
remaining 72% is owned by minority shareholders. If Atlas Ireland's income
and taxes were blended with SG Ireland Ltd (Main Group), the minority
shareholders would effectively bear or benefit from Top-up Tax calculations
related to income they don't own.

By calculating Atlas Ireland separately (Article 5.6.2), only the economic
substance belonging to the 28% UPE ownership is considered for the MNE
Group's Top-up Tax liability. This prevents the 72% minority-owned portion
from distorting the Group's GloBE calculations.

Note: Although calculated separately, Ireland's QDMTT still applies to Atlas
Ireland's Top-up Tax, so the €67,080 is collected domestically by Ireland.
```

---

## ETR and Top-Up Tax Calculation Template

Use this template for each jurisdiction:

```
COMPLETE ETR AND TOP-UP TAX WORKSHEET
Jurisdiction: _________________________
Fiscal Year: _________________________
Entity Classification: MAIN GROUP / MOCE / SUB-GROUP

═══════════════════════════════════════════════════════════════════════
SECTION A: PRE-SCREENING
═══════════════════════════════════════════════════════════════════════

A1  De Minimis Assessment Required?                  YES / NO
A2  If YES: Average GloBE Revenue (3-year)          €__________________
A3          Average GloBE Income (3-year)           €__________________
A4          Revenue < €10M AND Income < €1M?        YES / NO
A5          De Minimis Election Made?               YES / NO

    If De Minimis applies: STOP. Top-up Tax = €0

═══════════════════════════════════════════════════════════════════════
SECTION B: ETR CALCULATION
═══════════════════════════════════════════════════════════════════════

B1  Jurisdictional Net GloBE Income                 €__________________
B2  Adjusted Covered Taxes                          €__________________
B3  ETR (B2 ÷ B1)                                   __________________%

    If ETR ≥ 15%: STOP. No Top-up Tax.

═══════════════════════════════════════════════════════════════════════
SECTION C: SBIE CALCULATION
═══════════════════════════════════════════════════════════════════════

C1  Eligible Payroll Costs                          €__________________
C2  Payroll Carve-out Rate (FY 2025: 9.0%)         __________________%
C3  Payroll Carve-out (C1 × C2)                     €__________________

C4  Tangible Assets (NBV)                           €__________________
C5  Asset Carve-out Rate (FY 2025: 7.0%)           __________________%
C6  Asset Carve-out (C4 × C5)                       €__________________

C7  TOTAL SBIE (C3 + C6)                            €__________________
C8  Excess Profit (B1 − C7)                         €__________________

    If Excess Profit ≤ 0: STOP. No Top-up Tax.

═══════════════════════════════════════════════════════════════════════
SECTION D: TOP-UP TAX COMPUTATION
═══════════════════════════════════════════════════════════════════════

D1  Minimum Rate                                     15%
D2  Jurisdictional ETR (B3)                         __________________%
D3  Top-up Tax Percentage (D1 − D2)                 __________________%
D4  Excess Profit (C8)                              €__________________
D5  JURISDICTIONAL TOP-UP TAX (D3 × D4)             €__________________

═══════════════════════════════════════════════════════════════════════
SECTION E: QDMTT OFFSET
═══════════════════════════════════════════════════════════════════════

E1  Does jurisdiction have Qualified QDMTT?          YES / NO

    If NO: Net Top-up Tax = D5. Proceed to Section F.

E2  QDMTT Paid                                      €__________________
E3  NET TOP-UP TAX (D5 − E2)                        €__________________

    If E3 ≤ 0: No IIR/UTPR liability. Jurisdiction retains via QDMTT.

═══════════════════════════════════════════════════════════════════════
SECTION F: CHARGING MECHANISM
═══════════════════════════════════════════════════════════════════════

F1  Net Top-up Tax (E3 or D5)                       €__________________
F2  Is UPE in IIR jurisdiction?                      YES / NO

    If YES: IIR applies → UPE pays via IIR
    If NO:  UTPR applies → Allocated to UTPR jurisdictions

F3  Allocated Top-up Tax                            €__________________
F4  Mechanism                                        IIR / UTPR / QDMTT
```

---

## Learning Points

### Point 1: De Minimis Provides Significant Compliance Relief

Luxembourg's De Minimis election eliminates:
- ETR calculation requirement
- SBIE calculation requirement
- Top-up Tax liability (~€39,500 if calculated)
- Associated GIR reporting complexity

**Cost-benefit:** For small jurisdictions, the administrative burden of full GloBE calculations may exceed the potential Top-up Tax. De Minimis provides proportionate relief.

### Point 2: QDMTT Fundamentally Changes Cash Flow

| Without QDMTT | With QDMTT |
|---------------|------------|
| Singapore: €198,907 → UK | Ireland: €496,008 stays in Ireland |
| Ireland: €428,928 → UK | |
| **UK receives: €627,835** | **UK receives: €198,907** |

Ireland's QDMTT redirects ~70% of Group Top-up Tax from UK to Ireland. This is a deliberate policy choice by source jurisdictions to retain taxing rights.

### Point 3: MOCE Separation Prevents Blending Distortion

If Atlas Ireland were blended with Main Group Ireland:

**Combined Ireland Calculation (hypothetical):**
| Item | Combined |
|------|----------|
| GloBE Income | €15,000,000 + €2,400,000 = €17,400,000 |
| Covered Taxes | €1,770,000 + €288,000 = €2,058,000 |
| Combined ETR | €2,058,000 ÷ €17,400,000 = **11.83%** |

**Actual Separate Calculations:**
| | Main Group | MOCE |
|-|------------|------|
| ETR | 11.80% | 12.00% |
| Top-up Tax % | 3.20% | 3.00% |

The MOCE's slightly higher ETR (12.00% vs 11.80%) would marginally improve the blended rate, benefiting minority shareholders at the expense of accuracy. Separation ensures each calculation reflects economic reality.

### Point 4: SBIE Transition Rates Are Declining

FY 2025 rates (9.0% payroll, 7.0% assets) will decline to 5.0% each by 2033. Future Top-up Tax liabilities will increase as SBIE carve-outs shrink:

| Fiscal Year | Singapore SBIE | Ireland SBIE | Impact on Excess Profit |
|-------------|----------------|--------------|------------------------|
| 2025 (current) | €167,500 | €1,596,000 | Current calculation |
| 2033+ | €93,000 | €888,000 | +€74,500 / +€708,000 |

Plan for increasing Top-up Tax exposure as transition rates phase down.

### Point 5: IIR Flows to UPE Jurisdiction

Singapore's Top-up Tax flows to UK (Stratos Holdings plc) because:
1. Singapore has no QDMTT
2. UK has implemented IIR
3. Stratos Holdings plc is the UPE with 100% ownership

If UK had not implemented IIR, UTPR jurisdictions would collect via denied deductions.

---

## Alternative Scenario: What If Ireland Had No QDMTT?

For additional practice, consider this alternative scenario:

**Assume:** Ireland has not implemented QDMTT.

**Questions:**
1. What would be the total IIR liability for Stratos Holdings plc?
2. How would the Group's cash flow be affected?
3. Would the MOCE treatment change?

**Analysis:**

**Without Ireland QDMTT:**

| Jurisdiction | Top-up Tax (€) | Mechanism |
|--------------|----------------|-----------|
| Singapore | 198,907 | IIR → UK |
| Ireland (Main) | 428,928 | IIR → UK |
| Atlas Ireland (MOCE) | 67,080 | IIR → UK |
| Luxembourg | 0 | De Minimis |
| **Total IIR to UK** | **694,915** | |

**With Ireland QDMTT (actual):**

| Jurisdiction | Top-up Tax (€) | Mechanism |
|--------------|----------------|-----------|
| Singapore | 198,907 | IIR → UK |
| Ireland (Main) | 0 | QDMTT → Ireland |
| Atlas Ireland (MOCE) | 0 | QDMTT → Ireland |
| Luxembourg | 0 | De Minimis |
| **Total IIR to UK** | **198,907** | |

**Impact comparison:**

| Scenario | IIR to UK (€) | QDMTT to Ireland (€) | Total (€) |
|----------|---------------|----------------------|-----------|
| No Ireland QDMTT | 694,915 | 0 | 694,915 |
| With Ireland QDMTT | 198,907 | 496,008 | 694,915 |
| **Difference** | **(496,008)** | **+496,008** | **0** |

**Key insight:** QDMTT doesn't change the total Top-up Tax, but it changes **who collects it**. Ireland's QDMTT redirects €496,008 from UK to Ireland.

**MOCE treatment:** Would remain unchanged—separate calculation is required regardless of QDMTT status. Only the collection mechanism (IIR vs QDMTT) differs.

---

## Integration with GIR Tools

### Tool Workflow for Case Study 5

| Step | Tool | Action |
|------|------|--------|
| 1. Pre-screening | Manual | Apply De Minimis checklist (Luxembourg) |
| 2. ETR Calculation | **GIR-001 Step 1** | Enter GloBE Income + Covered Taxes |
| 3. SBIE Calculation | **GIR-001 Step 2** | Enter Payroll + Tangible Assets |
| 4. Top-up Tax | **GIR-001 Step 3** | Tool calculates automatically |
| 5. QDMTT Offset | **GIR-001 Step 3** | Enter QDMTT paid |
| 6. MOCE Calculation | **GIR-001** (separate run) | Repeat Steps 2-5 for MOCE |

### GIR-001 Input Summary

| Run | Jurisdiction | GloBE Income (€) | Covered Taxes (€) | Payroll (€) | Assets (€) |
|-----|--------------|------------------|-------------------|-------------|------------|
| 1 | Singapore | 4,000,000 | 392,206 | 1,200,000 | 850,000 |
| 2 | Ireland (Main) | 15,000,000 | 1,770,000 | 8,400,000 | 12,000,000 |
| 3 | Atlas Ireland (MOCE) | 2,400,000 | 288,000 | 1,200,000 | 800,000 |

**Note:** Luxembourg skipped (De Minimis applies).

Use **GIR-001 GloBE Calculator** at tools.mojitax.com to verify your calculations and practice the complete workflow.

---

## Key References

**OECD GloBE Model Rules:**
- Article 5.1.1 — ETR calculation formula
- Article 5.2.1 — Top-up Tax Percentage
- Article 5.2.2 — Jurisdictional Top-up Tax
- Article 5.3.1 — SBIE formula
- Article 5.3.3 — SBIE transition rates
- Article 5.5.1 — De Minimis Exclusion criteria
- Article 5.6.2 — MOCE separate calculation
- Article 10.1 — QDMTT definition and criteria

**Administrative Guidance:**
- December 2022: SBIE transition rate schedule
- July 2023: QDMTT Safe Harbour
- December 2023: MOCE calculation clarifications

**OECD Commentary:**
- Chapter 5, paragraphs 1-182 — ETR, SBIE, Top-up Tax, De Minimis, MOCE

---

## Next Step

You have completed Part 5: ETR Calculation and Top-Up Tax Determination. With all core computations covered (GloBE Income, Covered Taxes, ETR, SBIE, Top-up Tax, De Minimis, QDMTT, MOCE), proceed to **Part 6: Special Structures, Restructurings, and Tax Regimes** to learn how Pillar Two applies to M&A transactions, joint ventures, multi-parented groups, and investment entities.
