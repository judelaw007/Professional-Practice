# Case Study 1: GlobalTech Manufacturing - Expected Outcomes

Use these expected outcomes to verify your calculations with the demo tools.

---

## Ireland - Expected Results

### GIR ETR Calculator (GIR-001)

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

### GIR SBIE Calculator (GIR-002)

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

### GIR Top-Up Tax Calculator (GIR-003)

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

### GIR ETR Calculator (GIR-001)

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

### GIR SBIE Calculator (GIR-002)

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

### GIR Top-Up Tax Calculator (GIR-003)

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

## Safe Harbour Qualification Tool (GIR-004) - UK Test

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

## Learning Points

If your results differ from these expected outcomes:

1. **ETR differs**: Check you're using Adjusted Covered Taxes (not Total Tax Expense) divided by GloBE Income (not Accounting Income)

2. **SBIE differs**: Verify you're using the correct FY2024 rates (9.8% payroll, 7.8% assets) and check your input totals

3. **Top-up Tax differs**: Ensure you're calculating Excess Profit correctly (GloBE Income minus SBIE, not minus taxes)

4. **Safe Harbour fails unexpectedly**: Check you're using CbCR data (not GloBE-adjusted figures) for the safe harbour test
