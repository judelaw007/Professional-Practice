# Case Study 5: Phoenix Aerospace Holdings - Sample Data

## Original GIR Filing Data (Incorrect)

### Ireland - Originally Reported

| Data Point | Amount (EUR) |
|------------|--------------|
| GloBE Revenue | 156,000,000 |
| GloBE Income | 28,400,000 |
| Covered Taxes | 3,180,480 |
| Adjusted Covered Taxes | 3,180,480 |
| ETR | 11.20% |
| SBIE | 5,112,000 |
| Excess Profit | 23,288,000 |
| Top-up Tax % | 3.80% |
| **Top-up Tax** | **€885,000** |

---

## Error Details

### The Missing Transaction

| Item | Amount (EUR) |
|------|--------------|
| Intercompany royalty income (Q4 2024) | 14,200,000 |
| Irish withholding tax on royalty | 1,590,720 |

**Root Cause:**
The royalty income from Phoenix Aerospace UK Ltd to Phoenix Aerospace Ireland Ltd was incorrectly:
1. Excluded from Irish GloBE Income (treated as eliminated intercompany)
2. Omitted from Irish Covered Taxes

---

## Corrected Data

### Ireland - Amended Position

| Data Point | Original | Corrected | Change |
|------------|----------|-----------|--------|
| GloBE Revenue | €156,000,000 | €156,000,000 | — |
| GloBE Income | €28,400,000 | €42,600,000 | +€14,200,000 |
| Covered Taxes | €3,180,480 | €4,771,200 | +€1,590,720 |
| Adjusted Covered Taxes | €3,180,480 | €4,771,200 | +€1,590,720 |
| ETR | 11.20% | 11.20% | — |
| SBIE | €5,112,000 | €5,112,000 | — |
| Excess Profit | €23,288,000 | €37,488,000 | +€14,200,000 |
| Top-up Tax % | 3.80% | 3.80% | — |
| **Top-up Tax** | **€885,000** | **€1,424,544** | **+€539,544** |

---

## Materiality Assessment Data

### Quantitative Tests

| Test | Threshold | Actual | Result |
|------|-----------|--------|--------|
| Absolute Top-up Tax change | >€100,000 | €539,544 | **MATERIAL** |
| Percentage of original | >10% | 61% | **MATERIAL** |
| Impact on ETR | >0.5% | 0% | Not material |
| Group-wide impact | >€500,000 | €539,544 | **MATERIAL** |

### Error Classification

| Category | Description | This Error? |
|----------|-------------|-------------|
| Category 1 | Administrative errors | No |
| Category 2 | Calculation errors | No |
| Category 3 | Classification errors | No |
| **Category 4** | **Omission errors** | **YES** |

---

## Penalty Context Data

### Transitional Period Check

| Factor | Status |
|--------|--------|
| Fiscal Year | 2024 |
| Transitional period start | FY beginning on/after 31 Dec 2023 |
| Transitional period end | FY ending after 30 June 2028 |
| **FY2024 in transitional period?** | **YES** |

### "Reasonable Measures" Evidence

| Factor | Phoenix Aerospace Evidence |
|--------|---------------------------|
| Good faith effort | Big 4 advisor engaged |
| Documented processes | GIR preparation manual in place |
| Training | Tax team completed Pillar Two training |
| Internal controls | Three-stage review process |
| Timely disclosure | Error self-reported within 4 months |
| Prompt correction | Amendment within 6 weeks of discovery |

### UK Penalty Framework

| Behaviour | Unprompted Range | Prompted Range |
|-----------|------------------|----------------|
| Reasonable care | 0% | 0% |
| Careless | 0-30% | 15-30% |
| Deliberate | 20-70% | 35-70% |

---

## Interest Calculation Data

| Data Point | Value |
|------------|-------|
| Underpaid amount (GBP) | £463,050 |
| Exchange rate (EUR/GBP) | 0.8586 |
| Original due date | 30 June 2026 |
| Amendment payment date (assumed) | 20 October 2026 |
| Days late | 112 days |
| HMRC late payment rate | 7.5% p.a. |

---

## Other Jurisdictions (No Change)

| Jurisdiction | Original Top-up Tax | Change |
|--------------|---------------------|--------|
| Singapore | €890,000 | None |
| Switzerland | QDMTT offset | None |
| All others | €0 (safe harbour) | None |

---

## Group Total Summary

| Line | Original | Amended | Change |
|------|----------|---------|--------|
| Ireland Top-up Tax | €885,000 | €1,424,544 | +€539,544 |
| Singapore Top-up Tax | €890,000 | €890,000 | — |
| Other jurisdictions | €0 | €0 | — |
| **Total IIR** | **€1,775,000** | **€2,314,544** | **+€539,544** |
