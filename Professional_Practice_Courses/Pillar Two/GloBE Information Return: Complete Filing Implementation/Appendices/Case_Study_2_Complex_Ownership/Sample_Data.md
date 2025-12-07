# Case Study 2: Meridian Industrial Group - Sample Data

## Part 1: POPE Structure Data

### Ownership Structure

```
Meridian Industrial Group plc (UK - UPE)
        │
        ├── 70% ─────────────────────────┐
        │                                │
        │                    ┌───────────▼──────────┐
        │                    │ Meridian Tech        │
        │                    │ Ventures BV          │◄── 30% External
        │                    │ (Netherlands)        │    Investors
        │                    │ [POPE]               │
        │                    └───────────┬──────────┘
        │                                │
        │                    ┌───────────┴──────────┐
        │                    │                      │
        │              Meridian AI          Meridian Quantum
        │              Ireland Ltd           GmbH (Germany)
        │              (Ireland)             100% owned
        │              100% owned
```

### POPE Subsidiary - Ireland Data

**Input Data for GIR ETR Calculator (GIR-001):**

| Data Point | Amount (EUR) |
|------------|--------------|
| GloBE Income | 25,000,000 |
| Adjusted Covered Taxes | 2,875,000 |

**Input Data for GIR SBIE Calculator (GIR-002):**

| Data Point | Amount (EUR) |
|------------|--------------|
| Fiscal Year | 2024 |
| Eligible Payroll Costs | 8,000,000 |
| Eligible Tangible Assets (NBV) | 6,500,000 |

**Ownership for Allocation:**

| Party | Ownership % |
|-------|-------------|
| UPE (Meridian Industrial Group plc) indirect | 70% |
| POPE (Meridian Tech Ventures BV) for external | 30% |

---

## Part 2: Joint Venture Data

### JV Structure

```
Meridian Industrial Group plc (UK - UPE)
        │
        ├── 50% ─────────────────────────┐
        │                                │
Strategic Partner ────► 50%    ┌─────────▼─────────┐
  (External)                   │  MeridiaTech      │
                               │  JV LLC (USA)     │
                               │  [JV - Equity     │
                               │   Method]         │
                               └─────────┬─────────┘
                                         │
                               ┌─────────┴─────────┐
                               │                   │
                           JV OpCo 1          JV OpCo 2
                           (Delaware)         (California)
                             100%               100%
```

### JV Group - Delaware Operations (Low Tax)

| Data Point | Amount (EUR) |
|------------|--------------|
| Aggregate GloBE Income | 15,000,000 |
| Aggregate Covered Taxes | 1,800,000 |
| Eligible Payroll Costs | 8,000,000 |
| Eligible Tangible Assets (NBV) | 3,500,000 |

### JV Group - California Operations (Normal Tax)

| Data Point | Amount (EUR) |
|------------|--------------|
| Aggregate GloBE Income | 8,000,000 |
| Aggregate Covered Taxes | 2,080,000 |

**Note:** JV is treated as separate MNE group - no blending with main group

---

## Part 3: Minority-Owned Subgroup (MOS) Data

### MOS Structure

```
Meridian Industrial Group plc (UK - UPE)
        │
        ├── 25% (controlled via shareholder agreement)
        │
        │                    ┌───────────────────────┐
Other Investors ──► 75%      │  Meridian Green       │
                             │  Energy Ltd           │
                             │  (Ireland)            │
                             │  [MOCE - Head]        │
                             └───────────┬───────────┘
                                         │
                               ┌─────────┴─────────┐
                               │                   │
                          Green Wind          Solar Power
                          Holdings Ltd        Holdings Ltd
                          (Ireland)           (Netherlands)
                          100%                100%
                          [MOS member]        [MOS member]
```

### MOCE Head Entity - Meridian Green Energy Ltd (Ireland)

| Data Point | Amount (EUR) |
|------------|--------------|
| GloBE Income | 12,000,000 |
| Adjusted Covered Taxes | 1,440,000 |
| Eligible Payroll Costs | 4,500,000 |
| Eligible Tangible Assets (NBV) | 3,000,000 |

### MOS Member - Green Wind Holdings Ltd (Ireland)

| Data Point | Amount (EUR) |
|------------|--------------|
| GloBE Income | 5,000,000 |
| Adjusted Covered Taxes | 600,000 |
| Eligible Payroll Costs | 2,000,000 |
| Eligible Tangible Assets (NBV) | 1,500,000 |

### MOS Member - Solar Power Holdings Ltd (Netherlands)

| Data Point | Amount (EUR) |
|------------|--------------|
| GloBE Income | 3,000,000 |
| Adjusted Covered Taxes | 750,000 |

**Note:** Netherlands entity has ETR above 15% - no Top-up Tax

---

## SBIE Rates for FY2024

| Rate Type | FY2024 Rate |
|-----------|-------------|
| Payroll Carve-out | 9.8% |
| Asset Carve-out | 7.8% |
