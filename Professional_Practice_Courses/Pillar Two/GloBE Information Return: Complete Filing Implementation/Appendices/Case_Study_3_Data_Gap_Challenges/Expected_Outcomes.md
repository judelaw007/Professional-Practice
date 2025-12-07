# Case Study 3: Nexus Technologies Group - Expected Outcomes

## Challenge 1: DataFlow Mid-Year Acquisition

### GIR ETR Calculator (GIR-001)

| Output | Expected Value |
|--------|----------------|
| ETR | 21.00% |
| Top-up Tax % | 0% |
| Status | Compliant (above 15%) |

**Calculation:**
```
ETR = $2,793,000 / $13,300,000 = 21.00%
Above 15% → No Top-up Tax required
```

### GIR SBIE Calculator (GIR-002)

| Output | Expected Value |
|--------|----------------|
| Payroll SBIE ($8,500,000 × 9.8%) | $833,000 |
| Asset SBIE ($15,500,000 × 7.8%) | $1,209,000 |
| **Total SBIE** | **$2,042,000** |

**Key Point:** For mid-year acquisitions:
- Use actual 6-month payroll (not annualised)
- Use average of acquisition date and year-end for assets
- Full-year SBIE rates apply (not pro-rated)

---

## Challenge 2: Legacy ERP - Germany

### GIR ETR Calculator (GIR-001)

| Output | Expected Value |
|--------|----------------|
| ETR | 30.00% |
| Top-up Tax % | 0% |
| Status | Compliant (above 15%) |

**Calculation:**
```
ETR = €5,400,000 / €18,000,000 = 30.00%
```

### GIR SBIE Calculator (GIR-002) - With Estimates

| Output | Expected Value |
|--------|----------------|
| Estimated Eligible Payroll | €11,875,000 |
| Payroll SBIE | €1,163,750 |
| Estimated Eligible Assets | €6,970,000 |
| Asset SBIE | €543,660 |
| **Total SBIE** | **€1,707,410** |

**Estimation Documentation Required:**
```
Payroll: €12,500,000 × 95% = €11,875,000
Basis: FY2023 detailed analysis showed 95% eligible

Assets: €8,200,000 × 85% = €6,970,000
Basis: Industry benchmark; intangibles excluded
```

**Sensitivity Analysis:**
| Scenario | Payroll % | Asset % | Total SBIE |
|----------|-----------|---------|------------|
| Low | 92% | 80% | €1,637,600 |
| Best (used) | 95% | 85% | €1,707,410 |
| High | 98% | 90% | €1,775,400 |

---

## Challenge 3: Historical Acquisition - India

### GIR ETR Calculator (GIR-001)

| Output | Expected Value |
|--------|----------------|
| ETR | 15.00% |
| Top-up Tax % | 0% |
| Status | Compliant (at threshold) |

**Calculation:**
```
ETR = €1,800,000 / €12,000,000 = 15.00%
At minimum threshold → No Top-up Tax
```

### Impact Assessment

| Factor | Value |
|--------|-------|
| Residual step-up | ~€2,500,000 |
| Annual P&L impact | ~€500,000 additional depreciation |
| GloBE Income impact | Potentially understated by €500,000 |
| True GloBE Income | ~€12,500,000 |
| Adjusted ETR | ~14.4% (would trigger Top-up Tax) |

**Key Point:** Administrative Guidance permits use of current carrying values for pre-Dec 2021 acquisitions. The €500,000 impact is documented but accepted as immaterial at group level.

---

## Challenge 4: Incomplete Tax Records - Singapore

### Safe Harbour Calculation

| Data Point | Value |
|------------|-------|
| CbCR Profit Before Tax | €8,500,000 |
| Simplified Covered Taxes | €1,650,000 |
| Simplified ETR | 19.4% |
| Safe Harbour Test | PASS (>15% for FY2024) |

**UTP Treatment:**
```
All €800,000 UTP treated as Covered Tax
Basis: All positions relate to corporate income tax
Documentation: Analysis memo on file
```

**Sensitivity Analysis:**
| UTP Covered % | Simplified Covered Taxes | Simplified ETR |
|---------------|-------------------------|----------------|
| 100% (used) | €1,650,000 | 19.4% |
| 80% | €1,810,000 | 21.3% |
| 50% | €2,050,000 | 24.1% |

All scenarios pass safe harbour → UTP treatment is robust.

---

## Consolidated Resolution Summary

| Challenge | Entity | Resolution | Status |
|-----------|--------|------------|--------|
| Mid-Year Acquisition | DataFlow (USA) | Actual 6-month data | ✓ Resolved |
| Legacy ERP | Germany | 95%/85% estimation | ✓ Resolved |
| Historical Acquisition | India | AG reliance | ✓ Resolved |
| Incomplete Tax | Singapore | 100% covered UTP | ✓ Resolved |

---

## Learning Points

1. **Mid-Year Acquisitions**: Use actual period data; average assets; full-year SBIE rates

2. **Estimation Documentation**: Always document method, source, assumptions, and sensitivity

3. **AG Reliance**: For pre-Dec 2021 acquisitions without records, current carrying values are acceptable

4. **UTP Analysis**: Reasoned allocation based on nature of positions is acceptable with documentation

5. **Conservatism**: Apply conservatively where direction of error is known (higher income or lower taxes)
