# GIR-002: Safe Harbour Qualifier

## Tool Specification Document (v2 - Renumbered)

**Version:** 2.0
**Status:** Draft
**Last Updated:** 2024-12-08
**Previous ID:** GIR-004

---

## 1. Tool Metadata

| Attribute | Value |
|-----------|-------|
| Tool ID | GIR-002 |
| Tool Name | Safe Harbour Qualifier |
| Category | Pillar Two / Pre-Screening |
| Complexity | Medium |
| Estimated Dev Time | 3-4 days |
| Dependencies | None (standalone, but links to GIR-001) |
| Related Tools | GIR-001 (GloBE Calculator) |
| Course Section | Section 9.1 (Transitional CbCR Safe Harbour) |

---

## 2. Purpose & Learning Objectives

### 2.1 Purpose

The Safe Harbour Qualifier helps learners assess whether a jurisdiction qualifies for the Transitional CbCR Safe Harbour. This is a **pre-screening tool** - used BEFORE deciding whether to perform full GloBE calculations. If a jurisdiction qualifies, the MNE can use simplified CbCR data instead of performing detailed GloBE computations.

### 2.2 Learning Objectives

Upon using this tool, learners will be able to:

1. **Apply** the De Minimis Test thresholds correctly (Revenue <€10M AND Profit <€1M)
2. **Calculate** the Simplified ETR Test with year-specific thresholds (15%/16%/17%)
3. **Evaluate** the Routine Profits Test (Profit ≤ SBIE)
4. **Determine** overall safe harbour qualification status
5. **Recognize** which jurisdictions require full GloBE calculations vs. safe harbour treatment
6. **Understand** the compliance benefit of safe harbour elections

### 2.3 Why This Tool is Separate (Not Merged)

This tool uses **CbCR data** (not GloBE-adjusted data), making it fundamentally different from the GloBE Calculator:
- GIR-001 uses GloBE Income and Adjusted Covered Taxes
- GIR-002 uses CbCR Revenue, CbCR Profit, and Simplified Covered Taxes

The safe harbour assessment is a **gate** that happens before calculations, not part of the calculation itself.

### 2.4 Prerequisites

Learners should understand:
- Country-by-Country Reporting (CbCR) concepts
- Difference between CbCR data and GloBE-adjusted data
- Transitional nature of the safe harbour (FY 2024-2026 only)
- Basic SBIE concepts (for Routine Profits Test)

---

## 3. Safe Harbour Overview

The Transitional CbCR Safe Harbour allows MNE groups to avoid full GloBE calculations for certain jurisdictions. A jurisdiction qualifies if it meets **ANY ONE** of three tests:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│              TRANSITIONAL CbCR SAFE HARBOUR (FY 2024-2026)                  │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│        ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐       │
│        │  DE MINIMIS     │  │  SIMPLIFIED     │  │  ROUTINE        │       │
│        │  TEST           │  │  ETR TEST       │  │  PROFITS TEST   │       │
│        ├─────────────────┤  ├─────────────────┤  ├─────────────────┤       │
│        │ Revenue < €10M  │  │ ETR ≥ 15% (2024)│  │ Profit ≤ SBIE   │       │
│        │      AND        │  │ ETR ≥ 16% (2025)│  │                 │       │
│        │ Profit < €1M    │  │ ETR ≥ 17% (2026)│  │                 │       │
│        └────────┬────────┘  └────────┬────────┘  └────────┬────────┘       │
│                 │                    │                    │                 │
│                 └────────────────────┼────────────────────┘                 │
│                                      │                                      │
│                                      ▼                                      │
│                          ┌─────────────────────┐                           │
│                          │    PASS ANY ONE     │                           │
│                          │         =           │                           │
│                          │   SAFE HARBOUR      │                           │
│                          │      APPLIES        │                           │
│                          └─────────────────────┘                           │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 4. Input Fields

### 4.1 Input Field Specifications

| Field ID | Field Name | Data Type | Required | Validation |
|----------|------------|-----------|----------|------------|
| `fiscal_year` | Fiscal Year | Enum | Yes | 2024, 2025, or 2026 only |
| `jurisdiction_name` | Jurisdiction | String | Yes | Max 100 chars |
| `cbcr_revenue` | CbCR Revenue | Decimal | Yes | ≥ 0 |
| `cbcr_profit` | CbCR Profit Before Tax | Decimal | Yes | Can be negative (loss) |
| `simplified_taxes` | Simplified Covered Taxes | Decimal | Yes | ≥ 0 |
| `sbie_amount` | SBIE Amount | Decimal | Yes | ≥ 0 |
| `currency` | Currency | Enum | Yes | EUR, USD, GBP, CHF |

### 4.2 ETR Threshold by Fiscal Year

| Fiscal Year | ETR Threshold | Notes |
|-------------|---------------|-------|
| 2024 | 15% | First year of safe harbour |
| 2025 | 16% | Threshold increases |
| 2026 | 17% | Final year of transitional safe harbour |
| 2027+ | N/A | Safe harbour expires |

### 4.3 De Minimis Thresholds

| Threshold | Amount | Currency |
|-----------|--------|----------|
| Revenue | < €10,000,000 | EUR |
| Profit | < €1,000,000 | EUR |

**Note:** Both conditions must be met for De Minimis Test to pass.

---

## 5. Output Fields

### 5.1 Output Field Specifications

| Field ID | Field Name | Data Type | Format |
|----------|------------|-----------|--------|
| `de_minimis_result` | De Minimis Test | Object | Status + details |
| `simplified_etr_result` | Simplified ETR Test | Object | Status + ETR + threshold |
| `routine_profits_result` | Routine Profits Test | Object | Status + comparison |
| `overall_status` | Safe Harbour Status | Enum | QUALIFIES / NOT_QUALIFIED |
| `qualifying_test` | Qualifying Test Name | String | Which test passed (if any) |
| `recommendation` | Recommendation | Text | Action guidance |

### 5.2 Status Values

| Status | Condition | Display |
|--------|-----------|---------|
| `QUALIFIES` | Any test passes | ✅ "SAFE HARBOUR APPLIES" |
| `NOT_QUALIFIED` | All tests fail | ❌ "FULL GloBE CALCULATION REQUIRED" |

---

## 6. Calculation Logic

### 6.1 Complete Assessment Algorithm

```
FUNCTION AssessSafeHarbour(fiscal_year, cbcr_revenue, cbcr_profit,
                           simplified_taxes, sbie_amount):

    // Get ETR threshold for fiscal year
    etr_thresholds = {2024: 15, 2025: 16, 2026: 17}
    etr_threshold = etr_thresholds[fiscal_year]

    // Constants
    DE_MINIMIS_REVENUE = 10,000,000  // €10M
    DE_MINIMIS_PROFIT = 1,000,000    // €1M

    // ═══════════════════════════════════════════════════════════════
    // TEST 1: DE MINIMIS TEST
    // ═══════════════════════════════════════════════════════════════

    de_minimis_pass = (cbcr_revenue < DE_MINIMIS_REVENUE) AND
                      (cbcr_profit < DE_MINIMIS_PROFIT)

    // ═══════════════════════════════════════════════════════════════
    // TEST 2: SIMPLIFIED ETR TEST
    // ═══════════════════════════════════════════════════════════════

    IF cbcr_profit <= 0:
        simplified_etr = NULL
        simplified_etr_pass = FALSE
        etr_status = "N/A - No positive profit"
    ELSE:
        simplified_etr = (simplified_taxes / cbcr_profit) * 100
        simplified_etr_pass = simplified_etr >= etr_threshold
        etr_status = simplified_etr_pass ? "PASS" : "FAIL"

    // ═══════════════════════════════════════════════════════════════
    // TEST 3: ROUTINE PROFITS TEST
    // ═══════════════════════════════════════════════════════════════

    IF cbcr_profit <= 0:
        routine_profits_pass = TRUE  // No positive profit = automatic pass
    ELSE:
        routine_profits_pass = cbcr_profit <= sbie_amount

    // ═══════════════════════════════════════════════════════════════
    // OVERALL DETERMINATION
    // ═══════════════════════════════════════════════════════════════

    qualifies = de_minimis_pass OR simplified_etr_pass OR routine_profits_pass

    qualifying_test =
        de_minimis_pass ? "De Minimis" :
        simplified_etr_pass ? "Simplified ETR" :
        routine_profits_pass ? "Routine Profits" : NULL

    RETURN {
        de_minimis: {pass: de_minimis_pass, revenue: cbcr_revenue, profit: cbcr_profit},
        simplified_etr: {pass: simplified_etr_pass, etr: simplified_etr, threshold: etr_threshold},
        routine_profits: {pass: routine_profits_pass, profit: cbcr_profit, sbie: sbie_amount},
        overall: qualifies ? "QUALIFIES" : "NOT_QUALIFIED",
        qualifying_test: qualifying_test
    }
```

---

## 7. User Interface Specifications

### 7.1 Main Layout Wireframe

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  GIR-002: Safe Harbour Qualifier                                            │
│  Assess Transitional CbCR Safe Harbour eligibility                          │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  INPUT: CbCR DATA                                                    │   │
│  │                                                                      │   │
│  │  Fiscal Year: [2024 ▼]          ETR Threshold: 15%                  │   │
│  │                                                                      │   │
│  │  Jurisdiction: [United Kingdom_______________________]               │   │
│  │                                                                      │   │
│  │  Currency: [EUR ▼]                                                   │   │
│  │                                                                      │   │
│  │  CbCR Revenue:              € [320,000,000.00________]              │   │
│  │  CbCR Profit Before Tax:    € [48,000,000.00_________]              │   │
│  │  Simplified Covered Taxes:  € [11,040,000.00_________]              │   │
│  │  SBIE Amount:               € [15,000,000.00_________]              │   │
│  │                                                                      │   │
│  │                     [ Check Safe Harbour ]   [ Clear ]               │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
│  ═══════════════════════════════════════════════════════════════════════   │
│                                                                             │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                                                                      │   │
│  │         ┌─────────────────────────────────────────────────┐         │   │
│  │         │           ✅ SAFE HARBOUR APPLIES               │         │   │
│  │         │         Qualifies via: Simplified ETR Test      │         │   │
│  │         └─────────────────────────────────────────────────┘         │   │
│  │                                                                      │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  TEST RESULTS                                                        │   │
│  │                                                                      │   │
│  │  ┌───────────────────────────────────────────────────────────────┐  │   │
│  │  │ ❌ DE MINIMIS TEST                                    FAIL    │  │   │
│  │  │    Revenue: €320,000,000 ≥ €10,000,000                        │  │   │
│  │  │    Profit:  €48,000,000 ≥ €1,000,000                          │  │   │
│  │  │    Both must be below thresholds                              │  │   │
│  │  └───────────────────────────────────────────────────────────────┘  │   │
│  │                                                                      │   │
│  │  ┌───────────────────────────────────────────────────────────────┐  │   │
│  │  │ ✅ SIMPLIFIED ETR TEST                                PASS    │  │   │
│  │  │    Simplified ETR: 23.00%                                     │  │   │
│  │  │    FY2024 Threshold: 15%                                      │  │   │
│  │  │    23.00% ≥ 15% ✓                                             │  │   │
│  │  └───────────────────────────────────────────────────────────────┘  │   │
│  │                                                                      │   │
│  │  ┌───────────────────────────────────────────────────────────────┐  │   │
│  │  │ ❌ ROUTINE PROFITS TEST                               FAIL    │  │   │
│  │  │    CbCR Profit: €48,000,000                                   │  │   │
│  │  │    SBIE Amount: €15,000,000                                   │  │   │
│  │  │    €48,000,000 > €15,000,000 ✗                                │  │   │
│  │  └───────────────────────────────────────────────────────────────┘  │   │
│  │                                                                      │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  RECOMMENDATION                                                      │   │
│  │                                                                      │   │
│  │  This jurisdiction qualifies for the Transitional CbCR Safe Harbour.│   │
│  │                                                                      │   │
│  │  ✓ Action: Elect safe harbour treatment for United Kingdom          │   │
│  │  ✓ Result: Top-up Tax for this jurisdiction is deemed ZERO          │   │
│  │  ✓ Benefit: Full GloBE calculations NOT required                    │   │
│  │                                                                      │   │
│  │  Note: Document this election in GIR Section 2.                     │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 7.2 Not Qualified Result Display

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                                                                             │
│         ┌─────────────────────────────────────────────────┐                │
│         │     ❌ FULL GloBE CALCULATION REQUIRED          │                │
│         │        All three tests failed                   │                │
│         └─────────────────────────────────────────────────┘                │
│                                                                             │
│  RECOMMENDATION                                                             │
│  ─────────────────────────────────────────────────────────────────────────  │
│  This jurisdiction does NOT qualify for the Transitional Safe Harbour.     │
│                                                                             │
│  Next Steps:                                                                │
│  1. Use GIR-001 GloBE Calculator to compute ETR, SBIE, and Top-up Tax     │
│  2. The jurisdiction may still have no Top-up Tax if ETR ≥ 15%            │
│     after full GloBE calculations                                          │
│                                                                             │
│                    [ Open GIR-001 GloBE Calculator ]                       │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 8. Test Cases

### 8.1 Case Study 1: GlobalTech Manufacturing - UK Test

**Inputs:**
| Field | Value |
|-------|-------|
| Fiscal Year | 2024 |
| Jurisdiction | United Kingdom |
| CbCR Revenue | €320,000,000 |
| CbCR Profit Before Tax | €48,000,000 |
| Simplified Covered Taxes | €11,040,000 |
| SBIE Amount | €15,000,000 |

**Expected Outputs:**
| Test | Result | Details |
|------|--------|---------|
| De Minimis | FAIL | Revenue €320M ≥ €10M, Profit €48M ≥ €1M |
| Simplified ETR | PASS | 23.00% ≥ 15% threshold |
| Routine Profits | FAIL | €48M > €15M |
| **Overall** | **QUALIFIES** | Via Simplified ETR Test |

**Calculation:**
```
Simplified ETR = €11,040,000 ÷ €48,000,000 = 0.23 = 23%
23% ≥ 15% (FY2024 threshold) → PASS
```

### 8.2 Additional Test Cases

| Test ID | Scenario | FY | Revenue | Profit | Taxes | SBIE | Expected |
|---------|----------|------|---------|--------|-------|------|----------|
| TC-001 | UK Safe Harbour (Case Study 1) | 2024 | €320M | €48M | €11.04M | €15M | QUALIFIES (ETR 23%) |
| TC-002 | Small jurisdiction - De Minimis | 2024 | €5M | €0.5M | €0.1M | €0.2M | QUALIFIES (De Minimis) |
| TC-003 | Loss jurisdiction | 2024 | €50M | -€5M | €0 | €1M | QUALIFIES (Routine - auto) |
| TC-004 | Low-tax fails all | 2024 | €100M | €30M | €3M | €5M | NOT_QUALIFIED |
| TC-005 | Routine profits pass | 2024 | €50M | €3M | €0.3M | €5M | QUALIFIES (Routine) |
| TC-006 | FY2025 threshold pass | 2025 | €100M | €50M | €8M | €10M | QUALIFIES (ETR 16%) |
| TC-007 | FY2025 threshold fail | 2025 | €100M | €50M | €7.9M | €10M | NOT_QUALIFIED (ETR 15.8%) |
| TC-008 | FY2026 threshold pass | 2026 | €100M | €50M | €8.5M | €10M | QUALIFIES (ETR 17%) |
| TC-009 | ETR exactly at threshold | 2024 | €100M | €20M | €3M | €5M | QUALIFIES (ETR 15.00%) |

### 8.3 Boundary Test Cases

| Test ID | Test | Value | Threshold | Expected |
|---------|------|-------|-----------|----------|
| BT-001 | De Minimis Revenue | €9,999,999 | €10M | Below threshold |
| BT-002 | De Minimis Revenue | €10,000,000 | €10M | At threshold - FAIL |
| BT-003 | De Minimis Profit | €999,999 | €1M | Below threshold |
| BT-004 | De Minimis Profit | €1,000,000 | €1M | At threshold - FAIL |
| BT-005 | ETR 2024 | 14.99% | 15% | FAIL |
| BT-006 | ETR 2024 | 15.00% | 15% | PASS (equals threshold) |
| BT-007 | ETR 2025 | 15.99% | 16% | FAIL |
| BT-008 | ETR 2026 | 16.99% | 17% | FAIL |
| BT-009 | Routine | Profit = SBIE | - | PASS (equals) |

### 8.4 Edge Cases

| Scenario | Inputs | Expected Behavior |
|----------|--------|-------------------|
| Zero revenue and profit | Rev=0, Profit=0 | De Minimis: PASS |
| Negative profit (loss) | Profit < 0 | ETR: N/A, Routine: PASS (auto) |
| Zero taxes, positive profit | Taxes=0, Profit>0 | ETR = 0%, FAIL |
| Very large numbers | Rev = €500B | Calculate normally |
| All tests fail | All conditions fail | NOT_QUALIFIED |

---

## 9. User Flow

### 9.1 Primary Flow

```
┌──────────────────────────────────────────────────────────────────────────┐
│                                                                          │
│  START: User wants to check if jurisdiction qualifies for safe harbour   │
│    │                                                                     │
│    ▼                                                                     │
│  ┌─────────────────────────────┐                                        │
│  │ 1. Select Fiscal Year       │                                        │
│  │    (2024/2025/2026)         │                                        │
│  │    → Threshold displayed    │                                        │
│  └──────────────┬──────────────┘                                        │
│                 │                                                        │
│                 ▼                                                        │
│  ┌─────────────────────────────┐                                        │
│  │ 2. Enter CbCR Data          │                                        │
│  │    - Revenue                │                                        │
│  │    - Profit Before Tax      │                                        │
│  │    - Simplified Taxes       │                                        │
│  │    - SBIE Amount            │                                        │
│  └──────────────┬──────────────┘                                        │
│                 │                                                        │
│                 ▼                                                        │
│  ┌─────────────────────────────┐                                        │
│  │ 3. Click "Check Safe        │                                        │
│  │    Harbour"                 │                                        │
│  └──────────────┬──────────────┘                                        │
│                 │                                                        │
│                 ▼                                                        │
│  ┌─────────────────────────────┐                                        │
│  │ 4. View Results             │                                        │
│  │    - All three tests        │                                        │
│  │    - Overall status         │                                        │
│  │    - Recommendation         │                                        │
│  └──────────────┬──────────────┘                                        │
│                 │                                                        │
│        ┌────────┴────────┐                                              │
│        │                 │                                              │
│        ▼                 ▼                                              │
│  ┌───────────┐    ┌───────────────────┐                                │
│  │ QUALIFIES │    │ NOT QUALIFIED     │                                │
│  │           │    │                   │                                │
│  │ Document  │    │ Use GIR-001       │                                │
│  │ election  │    │ GloBE Calculator  │                                │
│  └───────────┘    └───────────────────┘                                │
│                                                                          │
└──────────────────────────────────────────────────────────────────────────┘
```

---

## 10. Accessibility Requirements

### 10.1 WCAG 2.1 AA Compliance

| Requirement | Implementation |
|-------------|----------------|
| Keyboard Navigation | Tab through all fields, Enter to submit |
| Screen Reader | ARIA labels, live regions for results |
| Color Contrast | 4.5:1 minimum |
| Status Communication | PASS/FAIL conveyed via text AND icon AND color |
| Focus Indicators | Visible focus ring on all elements |

### 10.2 Status Indicators

| Status | Color | Icon | Text |
|--------|-------|------|------|
| PASS | Green (#28A745) | ✅ | "PASS" |
| FAIL | Red (#DC3545) | ❌ | "FAIL" |
| N/A | Grey (#6C757D) | ➖ | "N/A" |
| QUALIFIES | Green | ✅ | "SAFE HARBOUR APPLIES" |
| NOT_QUALIFIED | Red | ❌ | "FULL GloBE CALCULATION REQUIRED" |

---

## 11. Technical Notes

### 11.1 Data Model

```typescript
interface SafeHarbourAssessment {
  id: string;
  fiscalYear: 2024 | 2025 | 2026;
  jurisdiction: string;
  currency: 'EUR' | 'USD' | 'GBP' | 'CHF';

  // Inputs
  cbcrRevenue: number;
  cbcrProfit: number;
  simplifiedTaxes: number;
  sbieAmount: number;

  // Results
  deMinimisResult: {
    pass: boolean;
    revenueCheck: boolean;
    profitCheck: boolean;
  };
  simplifiedEtrResult: {
    pass: boolean;
    etr: number | null;
    threshold: number;
  };
  routineProfitsResult: {
    pass: boolean;
  };

  overallStatus: 'QUALIFIES' | 'NOT_QUALIFIED';
  qualifyingTest: string | null;

  createdAt: Date;
}
```

### 11.2 Integration with GIR-001

When result is NOT_QUALIFIED, provide link/button to open GIR-001 GloBE Calculator with the jurisdiction name pre-filled.

---

## 12. Limitations & Scope

### 12.1 In Scope

- ✅ Three test evaluation (De Minimis, Simplified ETR, Routine Profits)
- ✅ Year-specific ETR thresholds (15%/16%/17%)
- ✅ Clear pass/fail determination
- ✅ Recommendation guidance
- ✅ Link to GIR-001 when not qualified

### 12.2 Out of Scope

- ❌ Validating CbCR data comes from a "Qualified CbCR"
- ❌ Permanent CbCR Safe Harbour (different mechanism)
- ❌ QDMTT Safe Harbour (separate concept)
- ❌ Multi-jurisdiction batch assessment
- ❌ Storing election records
- ❌ Generating GIR documentation

---

## 13. Version History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2024-12-07 | — | Initial specification (as GIR-004) |
| 2.0 | 2024-12-08 | — | Renumbered to GIR-002; updated references to GIR-001 GloBE Calculator |

---

## 14. Appendix: Safe Harbour Decision Tree

```
START: Assess jurisdiction for Safe Harbour
              │
              ▼
    ┌─────────────────────┐
    │ Is FY 2024-2026?    │
    └─────────────────────┘
              │
       ┌──────┴──────┐
       │ NO          │ YES
       ▼             ▼
  ┌─────────┐   ┌─────────────────────────────────┐
  │ Safe    │   │ Check De Minimis Test           │
  │ Harbour │   │ Revenue <€10M AND Profit <€1M?  │
  │ NOT     │   └─────────────────────────────────┘
  │ Available│            │
  └─────────┘      ┌──────┴──────┐
                   │ YES         │ NO
                   ▼             ▼
              ┌─────────┐   ┌─────────────────────────────────┐
              │ PASS    │   │ Check Simplified ETR Test       │
              │ Safe    │   │ Simplified ETR ≥ Threshold?     │
              │ Harbour │   └─────────────────────────────────┘
              │ APPLIES │            │
              └─────────┘     ┌──────┴──────┐
                              │ YES         │ NO
                              ▼             ▼
                         ┌─────────┐   ┌─────────────────────────────────┐
                         │ PASS    │   │ Check Routine Profits Test      │
                         │ Safe    │   │ Profit ≤ SBIE?                  │
                         │ Harbour │   └─────────────────────────────────┘
                         │ APPLIES │            │
                         └─────────┘     ┌──────┴──────┐
                                         │ YES         │ NO
                                         ▼             ▼
                                    ┌─────────┐   ┌─────────────┐
                                    │ PASS    │   │ FAIL        │
                                    │ Safe    │   │ Use GIR-001 │
                                    │ Harbour │   │ GloBE       │
                                    │ APPLIES │   │ Calculator  │
                                    └─────────┘   └─────────────┘
```

---

*End of GIR-002 Safe Harbour Qualifier Specification*
