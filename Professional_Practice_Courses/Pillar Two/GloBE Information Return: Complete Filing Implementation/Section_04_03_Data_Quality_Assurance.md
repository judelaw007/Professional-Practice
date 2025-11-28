# Section 4.3: Data Quality Assurance

## Introduction

Data quality is the foundation of accurate GloBE Information Return preparation. With approximately 480 data points required across three GIR sections, and calculations spanning multiple jurisdictions and entities, even minor data errors can cascade into significant ETR calculation discrepancies, incorrect Top-up Tax determinations, or filing rejections.

According to the 2024 EY Tax Function Operations Survey, **83% of respondents** indicated they would need to make moderate to significant adjustments to their source data to develop tax-ready information for Pillar Two compliance. This statistic underscores the critical importance of establishing robust data quality assurance processes before GIR preparation begins.

This section provides:
- **Completeness verification procedures** ensuring all required data is captured
- **Accuracy validation checks** confirming data correctness against source systems
- **Consistency testing frameworks** verifying data coherence across entities and jurisdictions
- **Error identification and resolution** protocols for addressing data issues
- **Data Quality Checklist** with 50+ actionable checkpoints

> **Critical Context**: The GloBE Rules require calculations at the jurisdictional level, aggregating financial data from separate entities within each jurisdiction. This represents a substantial change from traditional single-entity income tax calculations. Tax teams must often explain Pillar Two ETR computation mechanisms to non-tax stakeholders, as these calculations differ significantly from ETR computations under accounting standards.

---

## 4.3.1 Data Quality Framework

### The Four Dimensions of GIR Data Quality

Effective data quality assurance addresses four interconnected dimensions:

```
┌─────────────────────────────────────────────────────────────────┐
│                  GIR Data Quality Dimensions                     │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│   ┌─────────────┐                    ┌─────────────┐           │
│   │             │                    │             │           │
│   │ COMPLETENESS│◄──────────────────►│  ACCURACY   │           │
│   │             │                    │             │           │
│   │ All required│                    │Data matches │           │
│   │ data present│                    │source truth │           │
│   │             │                    │             │           │
│   └──────┬──────┘                    └──────┬──────┘           │
│          │                                  │                   │
│          │         ┌───────────┐           │                   │
│          │         │           │           │                   │
│          └────────►│  GIR DATA ├───────────┘                   │
│                    │  QUALITY  │                               │
│          ┌────────►│           │◄──────────┐                   │
│          │         └───────────┘           │                   │
│          │                                  │                   │
│   ┌──────┴──────┐                    ┌──────┴──────┐           │
│   │             │                    │             │           │
│   │ CONSISTENCY │◄──────────────────►│ TIMELINESS  │           │
│   │             │                    │             │           │
│   │Data coherent│                    │Data current │           │
│   │across system│                    │and as of    │           │
│   │             │                    │correct date │           │
│   └─────────────┘                    └─────────────┘           │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

| Dimension | Definition | GIR Impact |
|-----------|------------|------------|
| **Completeness** | All required data points are present for all entities and jurisdictions | Missing data leads to incomplete GIR sections or calculation errors |
| **Accuracy** | Data values correctly reflect source system values and underlying transactions | Incorrect values produce wrong ETR calculations and Top-up Tax amounts |
| **Consistency** | Data is coherent across entities, time periods, and related data points | Inconsistent data fails validation checks and creates audit issues |
| **Timeliness** | Data represents the correct fiscal period with appropriate cutoffs | Timing errors affect period-specific calculations and comparisons |

### Data Quality Governance Structure

Establish clear ownership and accountability for GIR data quality:

| Role | Responsibilities | Accountability |
|------|------------------|----------------|
| **Pillar Two Owner** | Overall GIR accuracy and filing compliance | Final sign-off on GIR submission |
| **Data Quality Lead** | Data validation process design and execution | Quality assurance certification |
| **Entity Data Stewards** | Source data accuracy for assigned entities | Entity-level data certification |
| **Technical Lead** | System extraction and transformation accuracy | Technical validation completion |
| **Finance Lead** | Financial data reconciliation to trial balance | Financial data certification |
| **HR Lead** | Payroll and employee data for SBIE | SBIE input data certification |
| **Fixed Asset Lead** | Tangible asset data for SBIE | Asset data certification |

### Data Quality Lifecycle

```
┌─────────────────────────────────────────────────────────────────┐
│                    Data Quality Lifecycle                        │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  Phase 1: PREVENTION                                             │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │ • Define data requirements and standards                  │   │
│  │ • Establish data collection templates                     │   │
│  │ • Configure extraction validation rules                   │   │
│  │ • Train data stewards on requirements                     │   │
│  └─────────────────────────┬────────────────────────────────┘   │
│                            ▼                                    │
│  Phase 2: DETECTION                                              │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │ • Execute completeness checks                             │   │
│  │ • Run accuracy validation queries                         │   │
│  │ • Perform consistency testing                             │   │
│  │ • Identify anomalies and outliers                         │   │
│  └─────────────────────────┬────────────────────────────────┘   │
│                            ▼                                    │
│  Phase 3: CORRECTION                                             │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │ • Investigate identified issues                           │   │
│  │ • Determine root cause                                    │   │
│  │ • Implement corrections                                   │   │
│  │ • Re-validate corrected data                              │   │
│  └─────────────────────────┬────────────────────────────────┘   │
│                            ▼                                    │
│  Phase 4: DOCUMENTATION                                          │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │ • Document validation procedures performed                │   │
│  │ • Record issues identified and resolutions                │   │
│  │ • Obtain sign-offs from data owners                       │   │
│  │ • Archive validation evidence for audit trail             │   │
│  └──────────────────────────────────────────────────────────┘   │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 4.3.2 Completeness Verification Procedures

Completeness verification ensures all required data points are present for every in-scope entity and jurisdiction. Missing data is one of the most common causes of GIR preparation delays.

### Entity Coverage Verification

**Step 1: Confirm Entity Universe**

| Verification Check | Expected Result | Action if Failed |
|--------------------|-----------------|------------------|
| All CEs identified | Entity list matches legal structure chart | Reconcile to group legal entity database |
| Entity jurisdictions assigned | Each CE has tax residence jurisdiction | Obtain tax residence confirmation |
| GloBE status determined | Each CE has GloBE classification | Complete entity classification analysis |
| Ownership percentages documented | Ownership chain is complete | Reconcile to statutory ownership records |
| Excluded entities identified | Excluded entities flagged with basis | Document exclusion rationale |

**Step 2: Entity-Level Data Presence Check**

For each Constituent Entity, verify presence of:

| Data Category | Required Data Points | Verification Method |
|---------------|---------------------|---------------------|
| **Identification** | Legal name, TIN, jurisdiction | Master data review |
| **Financial** | Trial balance, income statement | Financial system extract |
| **Tax** | Current tax, deferred tax | Tax provision data |
| **Payroll** | Employee count, payroll costs | HR system extract |
| **Assets** | Tangible asset values | Fixed asset register |
| **Intercompany** | IC transactions, eliminations | Consolidation data |

### Jurisdictional Coverage Verification

**Jurisdiction Completeness Matrix**

| Jurisdiction | CEs Present | Financial Data | Tax Data | SBIE Data | Safe Harbour | Status |
|--------------|-------------|----------------|----------|-----------|--------------|--------|
| United Kingdom | 5 | ✓ | ✓ | ✓ | N/A | Complete |
| Germany | 3 | ✓ | ✓ | ✓ | CbCR | Complete |
| United States | 12 | ✓ | ✓ | ✓ | N/A | Complete |
| Singapore | 2 | ✓ | ✓ | Pending | QDMTT | Incomplete |
| ... | ... | ... | ... | ... | ... | ... |

### Data Point Completeness by GIR Section

**Section 1: MNE Group Information (~50+ data points)**

| Data Point Category | Count | Required For | Completeness Check |
|--------------------|-------|--------------|-------------------|
| Filing CE identification | 8 | All filings | ✓ Filing CE details complete |
| UPE information | 6 | All filings | ✓ UPE details complete |
| Corporate structure | 15+ per CE | All filings | ✓ All CEs documented |
| Summary information | 10+ | All filings | ✓ Jurisdictional summary complete |

**Section 2: Safe Harbours and Exclusions (~40 data points)**

| Data Point Category | Count | Required For | Completeness Check |
|--------------------|-------|--------------|-------------------|
| CbCR Safe Harbour elections | 5 per jurisdiction | Electing jurisdictions | ✓ Elections documented |
| QDMTT Safe Harbour elections | 5 per jurisdiction | Electing jurisdictions | ✓ Elections documented |
| UTPR Safe Harbour elections | 3 per jurisdiction | Electing jurisdictions | ✓ Elections documented |
| Excluded jurisdictions | 3 per jurisdiction | Excluded jurisdictions | ✓ Exclusions documented |

**Section 3: GloBE Computations (~400 data points)**

| Data Point Category | Count | Required For | Completeness Check |
|--------------------|-------|--------------|-------------------|
| GloBE Income adjustments | 50+ per jurisdiction | All jurisdictions | ✓ All adjustment lines populated |
| Covered Taxes | 30+ per jurisdiction | All jurisdictions | ✓ Current and deferred tax complete |
| SBIE calculations | 15+ per jurisdiction | All jurisdictions | ✓ Payroll and asset data complete |
| Top-up Tax computation | 20+ per jurisdiction | Low-taxed jurisdictions | ✓ Calculation inputs complete |

### Completeness Exception Handling

When data gaps are identified:

| Gap Type | Severity | Resolution Approach | Documentation Required |
|----------|----------|---------------------|----------------------|
| Missing entity data | Critical | Obtain from entity; escalate if delayed | Data request log; escalation trail |
| Missing data point | High | Source from alternative system or estimate | Estimation methodology memo |
| Partial data | Medium | Validate partial data; obtain remainder | Reconciliation to expected total |
| Data format issue | Low | Transform to required format | Transformation specification |

---

## 4.3.3 Accuracy Validation Checks

Accuracy validation confirms that extracted data correctly represents source system values and underlying transactions. This is essential because GloBE calculations are based on financial accounting data with specific adjustments.

### Financial Data Accuracy Checks

**Trial Balance Reconciliation**

| Validation Check | Expected Outcome | Tolerance | Action if Failed |
|------------------|------------------|-----------|------------------|
| TB total assets = Total liabilities + Equity | Balanced | €0 | Investigate imbalance |
| Extracted revenue = TB revenue accounts | Match | €1,000 | Reconcile difference |
| Extracted expenses = TB expense accounts | Match | €1,000 | Reconcile difference |
| Extracted tax = TB tax accounts | Match | €100 | Reconcile difference |
| Entity count in extract = Entity count in TB | Match | 0 | Identify missing entities |

**Income Statement Validation**

| Validation Check | Expected Outcome | Tolerance | Action if Failed |
|------------------|------------------|-----------|------------------|
| Revenue ≥ 0 for operating entities | Positive or zero | N/A | Validate if negative is legitimate |
| Gross profit ≤ Revenue | Logical relationship | N/A | Investigate if gross profit > revenue |
| Operating expenses > 0 for operating entities | Positive | N/A | Validate if zero |
| Pre-tax income = Revenue - Expenses | Calculation correct | €1 | Fix calculation error |
| Income statement ties to TB | Match | €100 | Reconcile to trial balance |

### Tax Data Accuracy Checks

**Current Tax Validation**

| Validation Check | Expected Outcome | Action if Failed |
|------------------|------------------|------------------|
| Current tax expense ≠ 0 if profitable | Tax recorded | Investigate nil tax position |
| Current tax = Taxable income × Statutory rate (approx.) | Reasonable relationship | Document permanent differences |
| Current tax payable = Prior year + Current provision - Payments | Reconciles | Fix current tax provision data |
| Foreign tax credits properly allocated | Allocated to jurisdiction of source | Reallocate FTCs |

**Deferred Tax Validation**

| Validation Check | Expected Outcome | Action if Failed |
|------------------|------------------|------------------|
| DTA recognized only if probable utilization | Recoverability assessed | Document recoverability analysis |
| DTL recognized for all taxable temporary differences | Complete DTL recognition | Identify missing DTLs |
| Deferred tax calculated at enacted rates | Correct rates applied | Adjust to enacted rates |
| Deferred tax movement reconciles | Opening + Movement = Closing | Investigate reconciling items |

**15% Cap Validation (GloBE-Specific)**

Under the GloBE Rules, deferred tax adjustments must be recast at the 15% minimum rate if calculated at a higher rate:

| Validation Check | Expected Outcome | Action if Failed |
|------------------|------------------|------------------|
| DTAs recorded at rates > 15% identified | DTAs flagged | Flag for 15% cap adjustment |
| DTAs recorded at rates < 15% identified | DTAs flagged | Flag for recast to 15% |
| DTLs subject to recapture identified | DTLs tracked | Initiate DTL recapture tracking |
| 15% cap adjustments calculated | Adjustments computed | Calculate cap adjustment |

### SBIE Data Accuracy Checks

The Substance-Based Income Exclusion requires accurate payroll and tangible asset data. Errors here directly impact the excess profit calculation and Top-up Tax amount.

**Eligible Payroll Costs Validation**

| Validation Check | Expected Outcome | Action if Failed |
|------------------|------------------|------------------|
| Payroll costs = Sum of eligible wage types | Reconciles to payroll system | Identify missing/excluded items |
| Employee count = FTE in jurisdiction | Matches HR records | Reconcile employee count |
| Remote/mobile employees allocated correctly | Allocation documented | Review allocation methodology |
| Independent contractors included if eligible | Contractors evaluated | Assess contractor eligibility |
| Stock-based compensation included | SBC per financial statements | Add SBC to eligible payroll |
| Capitalized payroll excluded (in tangible assets) | Not double-counted | Remove capitalized amounts |

**Eligible Payroll Costs Reconciliation**

```
Total Payroll per Financial Statements         XX,XXX,XXX
Less: Payroll for ineligible employees              (XXX,XXX)
Less: Payroll capitalized in tangible assets        (XXX,XXX)
Less: Payroll for employees in other jurisdictions  (XXX,XXX)
Add:  Stock-based compensation (per FS)              XXX,XXX
Add:  Independent contractor costs (eligible)        XXX,XXX
─────────────────────────────────────────────────────────────
Eligible Payroll Costs for SBIE                XX,XXX,XXX
```

**Eligible Tangible Assets Validation**

| Validation Check | Expected Outcome | Action if Failed |
|------------------|------------------|------------------|
| NBV = Cost - Accumulated depreciation | Calculation correct | Fix NBV calculation |
| Asset location = Entity jurisdiction | Assets correctly located | Reallocate mislocated assets |
| Leased assets included (per IFRS 16/ASC 842) | ROU assets in scope | Add ROU asset values |
| Impairment reversals limited to original carrying value | Reversal capped | Adjust reversal amount |
| Intangible assets excluded | Intangibles not included | Remove intangible assets |
| Natural resources excluded | Resources not included | Remove natural resources |

**Eligible Tangible Assets Reconciliation**

```
Total Tangible Fixed Assets per Balance Sheet  XX,XXX,XXX
Add:  Right-of-use assets (leases)                  XXX,XXX
Less: Assets located in other jurisdictions        (XXX,XXX)
Less: Assets not meeting tangible asset definition (XXX,XXX)
─────────────────────────────────────────────────────────────
Carrying Value of Eligible Tangible Assets     XX,XXX,XXX
```

### ETR Calculation Validation

**GloBE ETR Computation Check**

| Validation Check | Expected Outcome | Action if Failed |
|------------------|------------------|------------------|
| GloBE Income = Financial income + Adjustments | Calculation correct | Review adjustment completeness |
| Adjusted Covered Taxes correctly computed | Calculation correct | Review tax adjustments |
| ETR = Adjusted Covered Taxes / GloBE Income | Calculation correct | Fix formula error |
| ETR within reasonable range (0% - 50%) | Reasonable | Investigate unusual ETR |
| ETR < 15% flagged for Top-up Tax | Low-tax jurisdictions identified | Ensure completeness |

**ETR Reasonableness Checks**

| Scenario | Expected Range | If Outside Range |
|----------|----------------|------------------|
| Standard trading entity | Statutory rate ± 5% | Document permanent differences |
| Entity with tax losses | 0% or N/A | Verify loss position |
| Entity with tax incentives | Below statutory rate | Document incentive impact |
| Entity with one-time items | Varies | Document unusual items |
| Holding company (passive income) | Varies | Review holding company treatment |

---

## 4.3.4 Consistency Testing Across Entities

Consistency testing ensures data coherence across related data points, entities, time periods, and external sources.

### Cross-Entity Consistency Checks

**Intercompany Transaction Matching**

| Validation Check | Expected Outcome | Action if Failed |
|------------------|------------------|------------------|
| IC revenue (Entity A) = IC expense (Entity B) | Match within tolerance | Investigate timing/FX differences |
| IC receivable (Entity A) = IC payable (Entity B) | Match within tolerance | Reconcile intercompany |
| IC eliminations = Sum of IC transactions | Complete elimination | Identify missing eliminations |
| Net IC position across group = 0 | Balanced | Fix imbalance |

**Intercompany Reconciliation Template**

| Entity A | Entity B | Transaction Type | Amount (A) | Amount (B) | Difference | Status |
|----------|----------|------------------|------------|------------|------------|--------|
| UK Ltd | DE GmbH | Management fee | €1,200,000 | €1,200,000 | €0 | Matched |
| UK Ltd | US Inc | IP royalty | €800,000 | €802,500 | €(2,500) | FX diff |
| DE GmbH | SG Pte | Service fee | €500,000 | €495,000 | €5,000 | Timing |

**Ownership Consistency**

| Validation Check | Expected Outcome | Action if Failed |
|------------------|------------------|------------------|
| Ownership % sums to 100% for each CE | 100% ownership | Investigate missing ownership |
| Ownership chain complete from UPE | All tiers documented | Complete ownership chain |
| Minority interests properly identified | MI flagged | Flag minority interests |
| JV/associate treatment consistent | Consistent classification | Standardize treatment |

### Cross-Jurisdiction Consistency Checks

**Currency Consistency**

| Validation Check | Expected Outcome | Action if Failed |
|------------------|------------------|------------------|
| All entities report in consistent group currency | Single group currency | Convert to group currency |
| FX rates consistently applied | Same rate source/date | Standardize FX rates |
| Translation differences reconciled | Differences explained | Document FX impact |

**Accounting Policy Consistency**

| Validation Check | Expected Outcome | Action if Failed |
|------------------|------------------|------------------|
| Revenue recognition consistent across entities | Same policy applied | Document policy differences |
| Depreciation methods consistent | Same methods used | Note method differences |
| Lease accounting consistent (IFRS 16/ASC 842) | Same standard applied | Flag standard differences |
| Stock compensation accounting consistent | Same measurement | Note SBC differences |

### Time Period Consistency Checks

**Year-over-Year Consistency**

| Validation Check | Expected Outcome | Action if Failed |
|------------------|------------------|------------------|
| Entity count YoY explained | Changes documented | Document additions/disposals |
| Revenue change YoY reasonable | Within expected range | Investigate large movements |
| Employee count change YoY reasonable | Within expected range | Investigate large changes |
| Asset values change YoY explained | Changes documented | Document additions/impairments |

**Period-End Cutoff Consistency**

| Validation Check | Expected Outcome | Action if Failed |
|------------------|------------------|------------------|
| All entities report same fiscal period | Consistent period end | Align to GloBE Fiscal Year |
| Acquisition/disposal cutoffs correct | Transactions properly allocated | Adjust cutoff timing |
| Currency translation at period-end rate | Consistent translation date | Apply period-end rates |

### External Data Consistency

**Reconciliation to Published Financials**

| Validation Check | Expected Outcome | Action if Failed |
|------------------|------------------|------------------|
| GIR group revenue ≈ Consolidated financial statements | Reasonable reconciliation | Document reconciling items |
| GIR tax expense ≈ Tax note in annual report | Reasonable reconciliation | Document differences |
| GIR entity count ≈ Subsidiary list in annual report | Reasonable reconciliation | Explain entity differences |

**Reconciliation to CbCR Data**

| Validation Check | Expected Outcome | Action if Failed |
|------------------|------------------|------------------|
| GIR jurisdiction list = CbCR jurisdiction list | Same jurisdictions | Investigate differences |
| GIR revenue by jurisdiction ≈ CbCR revenue | Reasonable reconciliation | Document basis differences |
| GIR employee count ≈ CbCR employee count | Reasonable reconciliation | Explain count differences |
| GIR tangible assets ≈ CbCR tangible assets | Reasonable reconciliation | Document valuation differences |

> **Important Note**: CbCR and GIR data may differ due to different definitional bases. Document all reconciling items and their rationale.

---

## 4.3.5 Error Identification and Resolution

### Error Classification Framework

| Error Category | Description | Severity | Resolution Priority |
|----------------|-------------|----------|---------------------|
| **Critical** | Prevents GIR filing or causes material misstatement | Filing blocked | Immediate resolution required |
| **High** | Affects ETR calculation or Top-up Tax amount | Calculation error | Resolution within 24-48 hours |
| **Medium** | Causes inconsistency but doesn't affect calculations | Data quality issue | Resolution within 1 week |
| **Low** | Formatting or presentation issue | Minor defect | Resolution before filing |

### Common Error Types and Resolution

**Error Type 1: Missing Entity Data**

| Symptom | Root Cause | Resolution Steps |
|---------|------------|------------------|
| Entity appears in entity list but no financial data | Data not extracted | 1. Verify entity in source system; 2. Re-extract data; 3. If unavailable, escalate to entity |
| Entity not in entity list but should be | Entity master incomplete | 1. Update entity master; 2. Extract entity data; 3. Add to GIR |
| Partial entity data (some fields missing) | Incomplete extraction | 1. Identify missing fields; 2. Source from alternative system; 3. Estimate if necessary |

**Error Type 2: Calculation Discrepancies**

| Symptom | Root Cause | Resolution Steps |
|---------|------------|------------------|
| ETR outside expected range | Data input error or formula issue | 1. Review input data; 2. Verify calculation formula; 3. Trace to source |
| Top-up Tax amount seems high/low | SBIE or Covered Tax error | 1. Validate SBIE inputs; 2. Review Covered Tax adjustments; 3. Recalculate |
| SBIE carve-out incorrect | Wrong phase-in rate applied | 1. Verify fiscal year; 2. Apply correct transitional rate; 3. Recalculate |

**Error Type 3: Intercompany Imbalances**

| Symptom | Root Cause | Resolution Steps |
|---------|------------|------------------|
| IC doesn't eliminate to zero | Timing or FX differences | 1. Identify specific IC pairs; 2. Reconcile differences; 3. Adjust or document |
| IC revenue ≠ IC expense | Classification difference | 1. Standardize IC coding; 2. Reclassify transactions; 3. Verify elimination |
| IC transactions with non-CE entities | Scope error | 1. Identify non-CE transactions; 2. Remove from IC eliminations; 3. Verify entity scope |

**Error Type 4: DTL Recapture Tracking Errors**

| Symptom | Root Cause | Resolution Steps |
|---------|------------|------------------|
| DTL not tracked for recapture | Tracking not implemented | 1. Identify DTLs in scope; 2. Set up tracking by GL account; 3. Implement 5-year monitoring |
| Recapture exception not applied | Exception not identified | 1. Review DTL categories; 2. Apply Article 4.4.5 exceptions; 3. Document basis |
| Recapture triggered incorrectly | Tracking error | 1. Verify 5-year period; 2. Confirm DTL reversal status; 3. Adjust recapture |

### Error Resolution Workflow

```
┌─────────────────────────────────────────────────────────────────┐
│                    Error Resolution Workflow                     │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  Step 1: ERROR DETECTION                                         │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │ • Validation check identifies error                       │   │
│  │ • Log error in Error Register with:                       │   │
│  │   - Error ID and description                              │   │
│  │   - Data point(s) affected                                │   │
│  │   - Entity/jurisdiction affected                          │   │
│  │   - Detection date and method                             │   │
│  └─────────────────────────┬────────────────────────────────┘   │
│                            ▼                                    │
│  Step 2: ERROR CLASSIFICATION                                    │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │ • Assign severity (Critical/High/Medium/Low)              │   │
│  │ • Determine resolution priority                           │   │
│  │ • Identify responsible owner                              │   │
│  │ • Set target resolution date                              │   │
│  └─────────────────────────┬────────────────────────────────┘   │
│                            ▼                                    │
│  Step 3: ROOT CAUSE ANALYSIS                                     │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │ • Investigate source of error                             │   │
│  │ • Determine if systemic or isolated                       │   │
│  │ • Document root cause                                     │   │
│  │ • Identify other potentially affected data                │   │
│  └─────────────────────────┬────────────────────────────────┘   │
│                            ▼                                    │
│  Step 4: CORRECTION IMPLEMENTATION                               │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │ • Implement data correction                               │   │
│  │ • If systemic, correct all affected data points           │   │
│  │ • Document correction made                                │   │
│  │ • Obtain approval if material                             │   │
│  └─────────────────────────┬────────────────────────────────┘   │
│                            ▼                                    │
│  Step 5: RE-VALIDATION                                           │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │ • Re-run validation check that detected error             │   │
│  │ • Confirm error is resolved                               │   │
│  │ • Check for unintended consequences                       │   │
│  │ • Update Error Register with resolution                   │   │
│  └─────────────────────────┬────────────────────────────────┘   │
│                            ▼                                    │
│  Step 6: PREVENTIVE ACTION                                       │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │ • Identify process improvements to prevent recurrence     │   │
│  │ • Update validation checks if needed                      │   │
│  │ • Communicate lessons learned                             │   │
│  │ • Close error in Error Register                           │   │
│  └──────────────────────────────────────────────────────────┘   │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### Error Register Template

| Error ID | Description | Entity/ Jurisdiction | Data Point | Severity | Status | Owner | Detected | Resolved | Root Cause | Resolution |
|----------|-------------|---------------------|------------|----------|--------|-------|----------|----------|------------|------------|
| ERR-001 | Missing payroll data | DE GmbH | SBIE | High | Resolved | HR Lead | 15-Feb | 17-Feb | HR export excluded contractors | Re-extracted with contractors |
| ERR-002 | DTL not tracked | UK Ltd | Covered Tax | Medium | Open | Tax Lead | 18-Feb | - | New process not implemented | Implementing DTL tracking |
| ERR-003 | IC imbalance €50K | US-UK | Elimination | Low | Resolved | Finance | 20-Feb | 21-Feb | FX rate timing | Adjusted to period-end rate |

### Materiality Threshold for Error Resolution

The OECD Model Rules permit an election for "immaterial" decreases in Adjusted Covered Taxes, defined as an aggregate decrease of less than **€1 million** in the jurisdiction. Consider this threshold when prioritizing error resolution:

| Error Impact | Threshold | Resolution Requirement |
|--------------|-----------|----------------------|
| Affects Top-up Tax by > €1M | Material | Must correct before filing |
| Affects Top-up Tax by €100K - €1M | Significant | Should correct; document if not |
| Affects Top-up Tax by < €100K | Immaterial | May aggregate; document decision |

---

## 4.3.6 Data Quality Checklist (50+ Checkpoints)

The following checklist provides actionable checkpoints for comprehensive GIR data quality assurance. This checklist should be completed and signed off before GIR finalization.

### Pre-Extraction Checks (10 Checkpoints)

| # | Checkpoint | Owner | Status | Date | Notes |
|---|------------|-------|--------|------|-------|
| 1 | Entity master list reconciled to legal entity database | Entity Steward | ☐ | | |
| 2 | All in-scope Constituent Entities identified | Pillar Two Owner | ☐ | | |
| 3 | Excluded entities documented with rationale | Pillar Two Owner | ☐ | | |
| 4 | Fiscal period confirmed (end date, duration) | Finance Lead | ☐ | | |
| 5 | Source systems identified for all data categories | Technical Lead | ☐ | | |
| 6 | Extraction queries/reports validated on test data | Technical Lead | ☐ | | |
| 7 | Data stewards assigned for each entity/data type | DQ Lead | ☐ | | |
| 8 | Extraction schedule agreed and communicated | DQ Lead | ☐ | | |
| 9 | Currency and FX rate sources confirmed | Finance Lead | ☐ | | |
| 10 | Period-end close confirmed for all entities | Finance Lead | ☐ | | |

### Completeness Checks (12 Checkpoints)

| # | Checkpoint | Owner | Status | Date | Notes |
|---|------------|-------|--------|------|-------|
| 11 | All CEs have identification data (name, TIN, jurisdiction) | Entity Steward | ☐ | | |
| 12 | All CEs have financial data extracted | Finance Lead | ☐ | | |
| 13 | All CEs have current tax data | Tax Lead | ☐ | | |
| 14 | All CEs have deferred tax data | Tax Lead | ☐ | | |
| 15 | All jurisdictions have employee/payroll data for SBIE | HR Lead | ☐ | | |
| 16 | All jurisdictions have tangible asset data for SBIE | FA Lead | ☐ | | |
| 17 | Section 1 data points complete for all required fields | DQ Lead | ☐ | | |
| 18 | Section 2 safe harbour elections documented | Pillar Two Owner | ☐ | | |
| 19 | Section 3 GloBE computation data complete | DQ Lead | ☐ | | |
| 20 | Intercompany transaction data captured | Finance Lead | ☐ | | |
| 21 | Prior period data available for comparatives | Finance Lead | ☐ | | |
| 22 | No blank/null values in mandatory fields | Technical Lead | ☐ | | |

### Accuracy Checks (15 Checkpoints)

| # | Checkpoint | Owner | Status | Date | Notes |
|---|------------|-------|--------|------|-------|
| 23 | Trial balance totals reconciled to extracted data | Finance Lead | ☐ | | |
| 24 | Revenue figures reconciled to income statement | Finance Lead | ☐ | | |
| 25 | Expense figures reconciled to income statement | Finance Lead | ☐ | | |
| 26 | Current tax expense reconciled to tax provision | Tax Lead | ☐ | | |
| 27 | Deferred tax movements reconciled to tax provision | Tax Lead | ☐ | | |
| 28 | 15% cap adjustments calculated for high-rate DTAs | Tax Lead | ☐ | | |
| 29 | DTL recapture tracking implemented for in-scope DTLs | Tax Lead | ☐ | | |
| 30 | Eligible payroll costs reconciled to payroll system | HR Lead | ☐ | | |
| 31 | Employee count reconciled to HR records | HR Lead | ☐ | | |
| 32 | Tangible asset NBV reconciled to fixed asset register | FA Lead | ☐ | | |
| 33 | Asset jurisdiction allocation verified | FA Lead | ☐ | | |
| 34 | GloBE Income adjustments correctly calculated | Pillar Two Owner | ☐ | | |
| 35 | Covered Tax adjustments correctly calculated | Tax Lead | ☐ | | |
| 36 | SBIE phase-in rates correct for fiscal year | Pillar Two Owner | ☐ | | |
| 37 | ETR calculations verified for all jurisdictions | Pillar Two Owner | ☐ | | |

### Consistency Checks (10 Checkpoints)

| # | Checkpoint | Owner | Status | Date | Notes |
|---|------------|-------|--------|------|-------|
| 38 | Intercompany transactions balance to zero (IC elim) | Finance Lead | ☐ | | |
| 39 | Ownership percentages sum to 100% per entity | Entity Steward | ☐ | | |
| 40 | Currency conversion consistently applied | Finance Lead | ☐ | | |
| 41 | Accounting policies consistent across entities | Finance Lead | ☐ | | |
| 42 | Year-over-year changes in entity count explained | Entity Steward | ☐ | | |
| 43 | Year-over-year changes in revenue/profit reasonable | Finance Lead | ☐ | | |
| 44 | GIR data reconciled to published financials (high-level) | Finance Lead | ☐ | | |
| 45 | GIR data reconciled to CbCR data (where applicable) | Tax Lead | ☐ | | |
| 46 | Entity classification consistent with prior year (or changes documented) | Pillar Two Owner | ☐ | | |
| 47 | Safe harbour elections consistent with eligibility analysis | Pillar Two Owner | ☐ | | |

### Final Validation Checks (8 Checkpoints)

| # | Checkpoint | Owner | Status | Date | Notes |
|---|------------|-------|--------|------|-------|
| 48 | All Critical and High severity errors resolved | DQ Lead | ☐ | | |
| 49 | Error Register reviewed and closed out | DQ Lead | ☐ | | |
| 50 | Reasonableness review of ETR by jurisdiction completed | Pillar Two Owner | ☐ | | |
| 51 | Reasonableness review of Top-up Tax amounts completed | Pillar Two Owner | ☐ | | |
| 52 | All data owner sign-offs obtained | DQ Lead | ☐ | | |
| 53 | Documentation complete for audit trail | DQ Lead | ☐ | | |
| 54 | GIR data ready for XML generation | Technical Lead | ☐ | | |
| 55 | Final data quality certification signed | Pillar Two Owner | ☐ | | |

---

## 4.3.7 Documentation and Audit Trail

### Documentation Requirements

Maintain comprehensive documentation to support GIR data quality and provide audit trail:

| Document Type | Contents | Retention Period |
|---------------|----------|------------------|
| **Data Quality Plan** | Framework, roles, validation procedures | 7 years |
| **Extraction Specifications** | Queries, parameters, source systems | 7 years |
| **Validation Results** | Test results, pass/fail status, exceptions | 7 years |
| **Error Register** | All errors, root causes, resolutions | 7 years |
| **Reconciliations** | TB reconciliations, IC reconciliations | 7 years |
| **Sign-off Forms** | Data owner certifications | 7 years |
| **Supporting Calculations** | SBIE calculations, ETR calculations | 7 years |

### Data Quality Certification Form

```
┌─────────────────────────────────────────────────────────────────┐
│              GIR DATA QUALITY CERTIFICATION                      │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  MNE Group:     [Group Name]                                    │
│  Fiscal Year:   [Year End Date]                                 │
│  GIR Version:   [Version Number]                                │
│                                                                  │
│  CERTIFICATIONS:                                                 │
│                                                                  │
│  1. COMPLETENESS                                                 │
│     I certify that all required data points have been collected │
│     for all in-scope Constituent Entities and jurisdictions.    │
│                                                                  │
│     Name: _______________ Signature: __________ Date: _____     │
│     Title: Data Quality Lead                                    │
│                                                                  │
│  2. ACCURACY                                                     │
│     I certify that the financial data has been reconciled to    │
│     source systems and validated for accuracy.                  │
│                                                                  │
│     Name: _______________ Signature: __________ Date: _____     │
│     Title: Finance Lead                                         │
│                                                                  │
│  3. TAX DATA                                                     │
│     I certify that the current and deferred tax data is         │
│     accurate and GloBE adjustments correctly applied.           │
│                                                                  │
│     Name: _______________ Signature: __________ Date: _____     │
│     Title: Tax Lead                                             │
│                                                                  │
│  4. SBIE DATA                                                    │
│     I certify that eligible payroll costs and tangible asset    │
│     values are accurate and correctly allocated.                │
│                                                                  │
│     Name: _______________ Signature: __________ Date: _____     │
│     Title: HR Lead / FA Lead                                    │
│                                                                  │
│  5. FINAL APPROVAL                                               │
│     I certify that the GIR data has passed all data quality     │
│     checks and is ready for XML generation and filing.          │
│                                                                  │
│     Name: _______________ Signature: __________ Date: _____     │
│     Title: Pillar Two Owner                                     │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### Audit Readiness

Tax authorities may request supporting documentation for GIR submissions. Ensure the following are readily available:

| Audit Request | Supporting Documentation |
|---------------|-------------------------|
| Entity list verification | Legal entity database, ownership charts |
| GloBE Income calculation | Financial statements, adjustment schedules |
| Covered Taxes verification | Tax provision workpapers, tax returns |
| SBIE calculation | Payroll reports, fixed asset register, allocation methodology |
| ETR calculation | ETR computation workpaper, supporting schedules |
| Safe harbour election | Eligibility analysis, election documentation |
| Data quality process | DQ plan, validation results, certifications |

---

## Summary: Data Quality Assurance Process

```
┌─────────────────────────────────────────────────────────────────┐
│              Data Quality Assurance Summary                      │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  BEFORE EXTRACTION                                               │
│  ✓ Define data requirements (~480 data points)                  │
│  ✓ Establish governance structure and owners                    │
│  ✓ Configure extraction specifications                          │
│  ✓ Complete Pre-Extraction Checks (10 checkpoints)              │
│                                                                  │
│  DURING DATA COLLECTION                                          │
│  ✓ Execute completeness verification                            │
│  ✓ Complete Completeness Checks (12 checkpoints)                │
│  ✓ Monitor extraction progress                                  │
│  ✓ Address data gaps immediately                                │
│                                                                  │
│  AFTER EXTRACTION                                                │
│  ✓ Perform accuracy validation                                  │
│  ✓ Complete Accuracy Checks (15 checkpoints)                    │
│  ✓ Execute consistency testing                                  │
│  ✓ Complete Consistency Checks (10 checkpoints)                 │
│                                                                  │
│  ERROR RESOLUTION                                                │
│  ✓ Classify and prioritize errors                               │
│  ✓ Investigate root causes                                      │
│  ✓ Implement corrections                                        │
│  ✓ Re-validate corrected data                                   │
│                                                                  │
│  FINAL CERTIFICATION                                             │
│  ✓ Complete Final Validation Checks (8 checkpoints)             │
│  ✓ Obtain data owner sign-offs                                  │
│  ✓ Complete Data Quality Certification                          │
│  ✓ Archive documentation for audit trail                        │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## Template References

| Template | Description | Format |
|----------|-------------|--------|
| Data_Quality_Checklist.xlsx | 55-checkpoint validation checklist | Excel |
| Error_Register.xlsx | Error tracking and resolution log | Excel |
| Data_Quality_Certification.docx | Sign-off form for data owners | Word |
| TB_Reconciliation_Template.xlsx | Trial balance to GIR reconciliation | Excel |
| SBIE_Validation_Workpaper.xlsx | Payroll and tangible asset validation | Excel |
| IC_Reconciliation_Template.xlsx | Intercompany transaction matching | Excel |
| ETR_Reasonableness_Checklist.xlsx | ETR validation by jurisdiction | Excel |

---

## Key Takeaways

1. **Data quality is foundational** - 83% of organizations need moderate to significant data adjustments for Pillar Two compliance

2. **Four dimensions matter** - Completeness, accuracy, consistency, and timeliness must all be addressed

3. **Establish clear governance** - Define roles, responsibilities, and accountability for data quality

4. **Validate at multiple levels** - Entity, jurisdiction, and group-level validation is required

5. **SBIE data requires special attention** - Payroll and tangible asset data are often outside traditional tax processes

6. **Track DTLs for recapture** - The 5-year DTL recapture rule requires specific tracking by GL account

7. **Document everything** - Comprehensive documentation provides audit trail and supports filing positions

8. **Use the checklist** - 55 checkpoints ensure nothing is missed before GIR submission

---

## Sources and References

- [EY: How to Alleviate BEPS 2.0 Pillar Two Data Challenges](https://www.ey.com/en_us/insights/tax/how-to-alleviate-beps-2-0-pillar-two-data-challenges)
- [KPMG: Pillar Two Compliance](https://kpmg.com/us/en/articles/2024/pillar-two-compliance.html)
- [PwC: Pillar Two Data and Compliance Challenges](https://www.pwc.com/us/en/services/tax/library/pillar-two-compliance-challenges.html)
- [Deloitte: Getting Ready for Pillar Two](https://www.deloitte.com/us/en/services/audit/articles/pillar-two-tax.html)
- [EY: Steps for Operational Impact of Pillar Two](https://www.ey.com/en_gl/insights/tax/six-steps-to-prepare-for-the-operational-impact-of-pillar-two)
- [Forvis Mazars: Pillar Two Year-End Accounting Reminders](https://www.forvismazars.us/forsights/2025/01/pillar-two-year-end-accounting-reminders)
- [OECD: GloBE Information Return](https://www.oecd.org/content/dam/oecd/en/publications/reports/2023/07/tax-challenges-arising-from-the-digitalisation-of-the-economy-globe-information-return-pillar-two_10977da1/91a49ec3-en.pdf)
- [oecdpillars.com: Substance-Based Income Exclusion](https://oecdpillars.com/pillar-tab/substance-based-income-exclusion/)
- [oecdpillars.com: Deferred Tax Recapture Rule](https://oecdpillars.com/pillar-tab/deferred-tax-recapture-rule/)
- [KPMG: SBIE FAQ](https://assets.kpmg.com/content/dam/kpmg/cn/pdf/en/2024/08/faq-on-substance-based-income-exclusion.pdf)
- [Wolters Kluwer: Overcoming Challenges in Preparing GloBE Information Return](https://www.wolterskluwer.com/en-au/expert-insights/overcoming-challenges-in-preparing-for-beps-pillar-two)
- [Citco: Getting to Grips with the GloBE Information Return](https://www.citco.com/insights/pillar-2-update-getting-to-grips-with-the-globe-information-return)

---

*This section establishes the data quality assurance framework essential for accurate GIR preparation. The next section (4.4 Handling Data Gaps) addresses procedures for managing situations where required data is unavailable or incomplete.*
