# Section 4.4: Handling Data Gaps

## Introduction

Data gaps are an inevitable reality of GloBE Information Return preparation, particularly in the initial years of Pillar Two compliance. With approximately 480 data points required across multiple entities and jurisdictions—many of which may reside in systems outside traditional tax processes—even well-prepared MNE Groups will encounter situations where required data is unavailable, incomplete, or unreliable.

According to Wolters Kluwer's BEPS Pillar Two Readiness Survey (Q4/2023), **77.42% of respondents** anticipated difficulties in obtaining the necessary data and information required for Pillar Two compliance. The primary challenge identified was understanding the data requirements (37.63%), followed by sourcing data that resides outside tax department control.

This section provides practical guidance for:
- **Identifying and categorizing data gaps** before they become filing obstacles
- **Applying OECD-acceptable estimation methods** when precise data is unavailable
- **Documenting professional judgment** to support estimated values
- **Implementing remediation plans** to eliminate gaps for future filings
- **Leveraging transitional relief** provisions during the initial compliance years

> **Critical Context**: The OECD has recognized that MNEs are more likely to make mistakes in the initial years of GloBE Rules application. Transitional penalty relief provisions provide a "soft landing" for fiscal years beginning on or before December 31, 2026, provided the MNE demonstrates that it has taken **reasonable measures** to ensure correct application of the rules. However, this relief does not eliminate the need for accurate data—it provides tolerance for good-faith errors while the MNE works to improve data quality.

---

## 4.4.1 Missing Data Identification

Proactively identifying data gaps is essential for GIR preparation. Discovering gaps during the final stages of filing preparation creates significant risk of delays, errors, or incomplete submissions.

### Common Data Gap Scenarios

| Gap Category | Common Scenarios | Impact Level |
|--------------|------------------|--------------|
| **Acquired Entities** | Recently acquired subsidiary with different ERP, incomplete integration | Critical |
| **Legacy Systems** | Data required from decommissioned or obsolete systems | High |
| **Non-Standard Entities** | JVs, partnerships, or entities not on group consolidation | High |
| **Non-Financial Data** | SBIE data (payroll, assets) outside finance systems | High |
| **Historical Data** | Prior period data required for DTL recapture tracking | Medium |
| **Granularity Gaps** | Data exists at aggregate level, not at CE or jurisdictional level | Medium |
| **Foreign Entities** | Data held by local management in non-standard formats | Medium |
| **Timing Gaps** | Data not yet available due to local close timing | Low |

### Data Gap Categories

**Category 1: Structural Gaps**

Data that does not exist in any system and cannot be recreated:

| Structural Gap | Example | Typical Impact |
|----------------|---------|----------------|
| Entity not consolidated | Acquired company pre-acquisition period | Cannot include in GIR |
| No accounting records | Dormant entity with no financial statements | Missing CE data |
| Different accounting standards | Entity on non-IFRS/GAAP basis | Requires restatement |
| No tax records | Entity in tax-free jurisdiction with no filings | Missing Covered Tax data |

**Category 2: Access Gaps**

Data exists but cannot be accessed by the GIR preparation team:

| Access Gap | Example | Resolution |
|------------|---------|------------|
| System access restrictions | Tax team cannot access HR payroll system | Request access or data extract |
| Data ownership issues | Local finance controls entity data | Establish data sharing process |
| Third-party data | Outsourced payroll provider holds data | Request data from provider |
| Legacy system decommissioned | Historical data in archived format | Restore from archive |

**Category 3: Granularity Gaps**

Data exists but not at the required level of detail:

| Granularity Gap | Example | Resolution |
|-----------------|---------|------------|
| Entity vs. jurisdiction | Data at group level, not by CE | Allocate using methodology |
| Period aggregation | Annual data, need quarterly | Use period-end proxy |
| Category aggregation | Total payroll, not by employee | Estimate eligible portion |
| Currency aggregation | Single currency, need by original | Apply average rates |

**Category 4: Quality Gaps**

Data exists but is unreliable or requires significant adjustment:

| Quality Gap | Example | Resolution |
|-------------|---------|------------|
| Incomplete records | Payroll missing contractor costs | Supplement from alternative source |
| Known errors | Asset register with duplicate entries | Clean data before use |
| Inconsistent basis | Different depreciation methods by entity | Standardize for GIR |
| Stale data | Asset values not updated for impairment | Refresh valuations |

### Gap Impact Assessment Framework

Assess each identified gap using this framework:

```
┌─────────────────────────────────────────────────────────────────┐
│                  Data Gap Impact Assessment                      │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│                         PROBABILITY                              │
│                    (Gap cannot be filled)                        │
│                                                                  │
│            Low            Medium            High                 │
│      ┌──────────────┬──────────────┬──────────────┐            │
│      │              │              │              │             │
│  H   │    MEDIUM    │     HIGH     │   CRITICAL   │             │
│  i   │              │              │              │             │
│  g   │   Moderate   │   Serious    │   Severe     │             │
│  h   │   concern    │   concern    │   concern    │             │
│      │              │              │              │             │
│      ├──────────────┼──────────────┼──────────────┤            │
│  I   │              │              │              │             │
│  M   │     LOW      │    MEDIUM    │     HIGH     │             │
│  P   │              │              │              │             │
│  A   │    Minor     │   Moderate   │   Serious    │             │
│  C   │   concern    │   concern    │   concern    │             │
│  T   │              │              │              │             │
│      ├──────────────┼──────────────┼──────────────┤            │
│  L   │              │              │              │             │
│  o   │   MINIMAL    │     LOW      │    MEDIUM    │             │
│  w   │              │              │              │             │
│      │   Monitor    │    Minor     │   Moderate   │             │
│      │    only      │   concern    │   concern    │             │
│      │              │              │              │             │
│      └──────────────┴──────────────┴──────────────┘            │
│                                                                  │
│  Impact Assessment Criteria:                                     │
│  • Effect on ETR calculation accuracy                           │
│  • Effect on Top-up Tax amount                                  │
│  • Number of entities/jurisdictions affected                    │
│  • Audit risk and penalty exposure                              │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### Gap Identification Checklist by Data Category

**Financial Data Gaps**

| # | Checkpoint | Status | Gap Description | Impact |
|---|------------|--------|-----------------|--------|
| 1 | Trial balance available for all CEs | ☐ | | |
| 2 | All CEs on consistent accounting basis | ☐ | | |
| 3 | Intercompany transactions identifiable | ☐ | | |
| 4 | Revenue by income category available | ☐ | | |
| 5 | Expense detail sufficient for GloBE adjustments | ☐ | | |
| 6 | Foreign exchange gains/losses separable | ☐ | | |
| 7 | Prior period adjustments identified | ☐ | | |

**Tax Data Gaps**

| # | Checkpoint | Status | Gap Description | Impact |
|---|------------|--------|-----------------|--------|
| 8 | Current tax expense by jurisdiction | ☐ | | |
| 9 | Deferred tax expense/benefit by jurisdiction | ☐ | | |
| 10 | DTA/DTL balances by category | ☐ | | |
| 11 | Tax rate reconciliation data available | ☐ | | |
| 12 | Foreign tax credits properly allocated | ☐ | | |
| 13 | Uncertain tax position data available | ☐ | | |
| 14 | Historical DTL data for recapture tracking | ☐ | | |

**SBIE Data Gaps**

| # | Checkpoint | Status | Gap Description | Impact |
|---|------------|--------|-----------------|--------|
| 15 | Employee headcount by jurisdiction | ☐ | | |
| 16 | Eligible payroll costs by jurisdiction | ☐ | | |
| 17 | Stock-based compensation data | ☐ | | |
| 18 | Contractor costs identifiable | ☐ | | |
| 19 | Tangible asset NBV by jurisdiction | ☐ | | |
| 20 | Asset location data accurate | ☐ | | |
| 21 | Right-of-use assets included | ☐ | | |

**Entity and Structure Data Gaps**

| # | Checkpoint | Status | Gap Description | Impact |
|---|------------|--------|-----------------|--------|
| 22 | All CEs identified with TINs | ☐ | | |
| 23 | Ownership percentages documented | ☐ | | |
| 24 | PE identification complete | ☐ | | |
| 25 | GloBE status determined for all entities | ☐ | | |
| 26 | Excluded entity documentation | ☐ | | |

### Documentation Requirements for Identified Gaps

For each identified gap, document:

| Documentation Element | Description | Example |
|-----------------------|-------------|---------|
| **Gap ID** | Unique identifier | GAP-2025-001 |
| **Gap Description** | Clear description of what is missing | "Payroll data for SG Pte Ltd contractors" |
| **Data Category** | Category affected | SBIE - Eligible Payroll |
| **Entity/Jurisdiction** | Scope of gap | Singapore |
| **Impact Assessment** | Severity rating | High - affects SBIE by ~€500K |
| **Root Cause** | Why gap exists | Contractor payroll managed by agency |
| **Resolution Options** | Possible solutions | 1. Request from agency; 2. Estimate |
| **Selected Approach** | Chosen resolution | Estimate based on contract values |
| **Owner** | Person responsible | HR Lead - Singapore |
| **Target Date** | Resolution deadline | 15-Mar-2026 |
| **Status** | Current status | In progress |

---

## 4.4.2 Estimation Techniques

When data gaps cannot be filled with actual data, MNE Groups must use estimation techniques to derive reasonable values. The OECD GloBE Rules do not provide explicit guidance on estimation methods, but the principle of "reasonable measures" and the intent of the transitional penalty relief provisions support good-faith estimates that are documented and defensible.

### Estimation Principles

**Principle 1: Consistency**

Apply estimation methods consistently across similar data points, entities, and periods. Inconsistent estimation creates audit risk and undermines credibility.

**Principle 2: Conservatism**

When uncertain, err on the side of estimates that do not reduce Top-up Tax liability. This demonstrates good faith and reduces penalty risk.

**Principle 3: Supportability**

Every estimate must be supported by documented rationale, data sources, and calculations. "Best guess" without support is unacceptable.

**Principle 4: Materiality**

Focus estimation rigor on material data points. For immaterial amounts, simpler methods are acceptable.

**Principle 5: Refinement**

Estimates should improve over time as better data becomes available. Document the plan to replace estimates with actual data.

### EY's Recommended Approach

EY recommends starting with the minimum data needed to perform core calculations (approximately **60 data points per entity**), making assumptions where there are gaps, and then gradually refining the data set as you gain more clarity on requirements and materiality.

This approach acknowledges that perfect data is not achievable in early years and that reasonable estimates allow compliance while systems improve.

### Common Estimation Methods

**Method 1: Pro-Rata Allocation**

Use known total values and allocate based on a reliable proxy:

| Scenario | Known Value | Proxy Basis | Calculation |
|----------|-------------|-------------|-------------|
| Entity payroll from group total | Group payroll €50M | Headcount | Entity payroll = €50M × (Entity headcount / Group headcount) |
| Jurisdiction assets from entity | Entity assets €10M | Revenue | Jurisdiction assets = €10M × (Jurisdiction revenue / Entity revenue) |
| Tax by period from annual | Annual tax €1.2M | Revenue | Q1 tax = €1.2M × (Q1 revenue / Annual revenue) |

**Method 2: Historical Trending**

Use prior period data adjusted for known changes:

| Scenario | Prior Period | Adjustment Factor | Calculation |
|----------|--------------|-------------------|-------------|
| Current year payroll | Prior year €5M | Headcount change +10% | Current estimate = €5M × 1.10 = €5.5M |
| Current year assets | Prior year €8M | Additions - Disposals | Current estimate = €8M + €1M - €0.5M = €8.5M |
| Current year tax | Prior year €2M | Profit change +15% | Current estimate = €2M × 1.15 = €2.3M |

**Method 3: Comparable Entity Method**

Use data from similar entities as basis for estimate:

| Scenario | Comparable Entity | Adjustment | Calculation |
|----------|-------------------|------------|-------------|
| New subsidiary payroll | Similar size entity €3M | Industry adjustment | Estimate = €3M × 0.9 (lower cost jurisdiction) = €2.7M |
| PE assets | Similar PE €1M | Size adjustment | Estimate = €1M × 1.2 (larger PE) = €1.2M |

**Method 4: Industry Benchmark Method**

Use external benchmarks when internal data is unavailable:

| Scenario | Benchmark | Application | Calculation |
|----------|-----------|-------------|-------------|
| Payroll as % of revenue | Industry average 25% | Revenue €10M | Payroll estimate = €10M × 25% = €2.5M |
| NBV as % of revenue | Industry average 40% | Revenue €10M | NBV estimate = €10M × 40% = €4M |
| Tax rate | Statutory rate | Profit €5M | Tax estimate = €5M × 25% = €1.25M |

**Method 5: Management Inquiry**

Obtain estimates directly from local management with appropriate documentation:

| Scenario | Inquiry | Documentation | Validation |
|----------|---------|---------------|------------|
| Contractor headcount | Ask local HR | Email confirmation | Reasonableness check |
| Asset allocation | Ask local finance | Written estimate | Compare to prior year |
| Tax position | Ask local tax | Calculation summary | Review by group tax |

### SBIE-Specific Estimation Approaches

The Substance-Based Income Exclusion requires eligible payroll costs and tangible asset values that may not be readily available. Consider these estimation approaches:

**Eligible Payroll Cost Estimation**

| Data Gap | Estimation Method | Calculation |
|----------|-------------------|-------------|
| Contractor costs missing | Estimate from contract values | Contract value × estimated labour % |
| Employee allocation between jurisdictions | Headcount proration | Total payroll × (Jurisdiction FTE / Total FTE) |
| Stock-based compensation missing | Use financial statement SBC | SBC per P&L allocated by headcount |
| Benefits not separately tracked | Percentage of base salary | Base salary × industry benefits % (typically 15-25%) |

**Eligible Tangible Asset Estimation**

| Data Gap | Estimation Method | Calculation |
|----------|-------------------|-------------|
| Asset location unknown | Allocate by entity/revenue | Entity NBV × (Jurisdiction revenue / Entity revenue) |
| ROU assets not separately tracked | Estimate from lease expense | Annual lease expense × remaining lease term |
| Recent acquisitions without detail | Use acquisition value | Acquisition allocation × adjustment for depreciation |
| Impairment not reflected | Apply estimated impairment | Prior NBV × (1 - estimated impairment %) |

### Transitional Simplified Jurisdictional Reporting

The OECD provides a **Transitional Simplified Jurisdictional Reporting Framework** that addresses certain data availability challenges:

**Applicability Period**: Fiscal years beginning on or before 31 December 2028 (not including fiscal years ending after 30 June 2030)

**Key Simplifications**:

| Simplification | Description | Benefit |
|----------------|-------------|---------|
| Jurisdictional-level reporting | Report GloBE computations at jurisdiction level rather than CE level | Reduces granularity requirements |
| Aggregated adjustments | Report GloBE Income and Covered Tax adjustments at jurisdictional level | Simplifies data collection |
| Allocation documentation | Document allocation methodology | Provides flexibility in approach |

**Conditions for Using Simplified Reporting**:

1. No Top-up Tax liability arises in the jurisdiction, OR
2. Top-up Tax liability arises but does not need to be allocated on a CE-by-CE basis

**Documentation Requirement**: MNE Groups must document the process by which accounting information is allocated to each jurisdiction.

### Safe Harbour Estimation Approaches

Safe harbours provide alternative data sources that may be more readily available:

**Transitional CbCR Safe Harbour**

Uses Country-by-Country Report data as proxy for GloBE calculations:

| CbCR Data | Use in Safe Harbour Test |
|-----------|--------------------------|
| Total Revenue | De minimis test: < €10M |
| Profit before Tax | De minimis test: < €1M profit |
| Simplified ETR | Use CbCR profit and tax accrued |
| SBIE proxy | Use CbCR employee count and tangible assets |

> **Important**: If using CbCR Safe Harbour, the MNE must have a Qualified CbC Report. The simplified data cannot be used selectively—it applies to the entire jurisdiction's safe harbour test.

**NMCE Simplified Calculations**

For Non-Material Constituent Entities (NMCEs) not consolidated on a line-by-line basis solely for size/materiality:

| Simplification | Description |
|----------------|-------------|
| Revenue from CbCR | Use CbCR reported revenue |
| Tax from CbCR | Use CbCR tax accrued |
| Simplified ETR test | Apply safe harbour tests using simplified data |

---

## 4.4.3 Documentation of Estimates

Every estimate requires comprehensive documentation to support the filing position and demonstrate "reasonable measures" under the transitional penalty relief framework.

### Estimate Documentation Template

```
┌─────────────────────────────────────────────────────────────────┐
│                 ESTIMATE DOCUMENTATION FORM                      │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  ESTIMATE IDENTIFICATION                                         │
│  ─────────────────────────                                       │
│  Estimate ID:        [EST-2025-XXX]                             │
│  Data Point:         [GIR Field Reference]                      │
│  Entity/Jurisdiction:[Entity Name / Jurisdiction]               │
│  Fiscal Year:        [Fiscal Year End]                          │
│  Prepared By:        [Name / Date]                              │
│  Reviewed By:        [Name / Date]                              │
│                                                                  │
│  GAP DESCRIPTION                                                 │
│  ───────────────                                                 │
│  What data is missing or unavailable?                           │
│  [Description of the data gap]                                  │
│                                                                  │
│  Why is the data unavailable?                                   │
│  [Root cause explanation]                                       │
│                                                                  │
│  What efforts were made to obtain actual data?                  │
│  [Description of data sourcing attempts]                        │
│                                                                  │
│  ESTIMATION METHODOLOGY                                          │
│  ─────────────────────                                          │
│  Estimation method selected:                                    │
│  ☐ Pro-rata allocation                                          │
│  ☐ Historical trending                                          │
│  ☐ Comparable entity                                            │
│  ☐ Industry benchmark                                           │
│  ☐ Management inquiry                                           │
│  ☐ Other: [Describe]                                            │
│                                                                  │
│  Rationale for method selection:                                │
│  [Why this method is appropriate for this data point]           │
│                                                                  │
│  CALCULATION                                                     │
│  ───────────                                                     │
│  Data sources used:                                             │
│  [List all data inputs with sources]                            │
│                                                                  │
│  Calculation steps:                                             │
│  [Step-by-step calculation with formulas]                       │
│                                                                  │
│  Estimated value:    [Amount and currency]                      │
│                                                                  │
│  REASONABLENESS VALIDATION                                       │
│  ─────────────────────────                                      │
│  Comparison to prior period:                                    │
│  Prior period actual: [Amount]                                  │
│  Current estimate:    [Amount]                                  │
│  Variance:            [Amount and %]                            │
│  Variance explanation:[Why difference is reasonable]            │
│                                                                  │
│  Sensitivity analysis:                                          │
│  If estimate ±10%:    [Impact on ETR / Top-up Tax]             │
│  If estimate ±25%:    [Impact on ETR / Top-up Tax]             │
│                                                                  │
│  MATERIALITY ASSESSMENT                                          │
│  ──────────────────────                                         │
│  Estimated amount:              [Amount]                        │
│  Jurisdiction GloBE Income:     [Amount]                        │
│  % of jurisdiction income:      [%]                             │
│  Potential Top-up Tax impact:   [Amount]                        │
│  Materiality conclusion:        [Material / Immaterial]         │
│                                                                  │
│  FUTURE DATA IMPROVEMENT PLAN                                    │
│  ────────────────────────────                                   │
│  Actions to obtain actual data for future periods:              │
│  [List specific actions and timelines]                          │
│                                                                  │
│  Expected availability of actual data:                          │
│  [Target date for actual data]                                  │
│                                                                  │
│  APPROVALS                                                       │
│  ─────────                                                       │
│  Preparer:    _________________ Date: _________                 │
│  Reviewer:    _________________ Date: _________                 │
│  Approver:    _________________ Date: _________                 │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### Reasonableness Tests for Estimates

Apply these tests to validate estimate reasonableness:

| Test | Description | Action if Failed |
|------|-------------|------------------|
| **Prior Period Comparison** | Compare estimate to prior year actual | Document variance rationale |
| **Trend Analysis** | Check if estimate follows logical trend | Adjust estimate or document anomaly |
| **Peer Comparison** | Compare to similar entities | Investigate significant differences |
| **Ratio Analysis** | Check ratios (e.g., payroll/revenue) | Validate unusual ratios |
| **Sensitivity Analysis** | Test impact of ±10%, ±25% | Assess materiality of estimate error |
| **Management Validation** | Local management review | Obtain written confirmation |

### Supporting Evidence Requirements

| Evidence Type | Examples | Retention |
|---------------|----------|-----------|
| **Source Data** | Trial balances, CbCR, payroll reports | 7 years |
| **Calculation Workpapers** | Excel models, formulas | 7 years |
| **Management Representations** | Emails, signed confirmations | 7 years |
| **Benchmark Data** | Industry surveys, comparables | 7 years |
| **Approval Documentation** | Sign-off forms, meeting notes | 7 years |
| **Contemporaneous Memos** | Estimation rationale memoranda | 7 years |

---

## 4.4.4 Data Gap Remediation

While estimates provide short-term solutions, the goal is to eliminate data gaps over time. Implement a structured remediation program to improve data availability and quality for future GIR filings.

### Remediation Priority Framework

Prioritize gap remediation based on:

| Factor | High Priority | Medium Priority | Low Priority |
|--------|---------------|-----------------|--------------|
| **Materiality** | >1% of group GloBE Income | 0.1% - 1% of group GloBE Income | <0.1% of group GloBE Income |
| **Frequency** | Recurring gap (every year) | Occasional gap | One-time gap |
| **Complexity** | Complex estimation required | Moderate estimation | Simple estimation |
| **Audit Risk** | High audit scrutiny area | Medium scrutiny | Low scrutiny |
| **Resolution Effort** | Quick fix available | Moderate effort | Significant investment |

### Short-Term Workarounds (0-6 months)

Implement immediate solutions while permanent fixes are developed:

| Gap Type | Short-Term Workaround | Implementation |
|----------|----------------------|----------------|
| Missing entity data | Manual data collection via templates | Email data request to local finance |
| HR data inaccessible | Request periodic extracts from HR | Set up quarterly data feed |
| Asset location unknown | Management inquiry and confirmation | Local sign-off on asset allocation |
| Contractor data missing | Estimate from contract values | Apply labour percentage to contract spend |
| Tax data incomplete | Use prior year with adjustment | Apply profit change factor |

### Medium-Term System Fixes (6-18 months)

Address underlying system issues:

| Gap Type | Medium-Term Fix | Implementation |
|----------|-----------------|----------------|
| Multiple ERPs | Data integration layer | Deploy ETL tool or middleware |
| Granularity insufficient | Chart of accounts enhancement | Add jurisdictional or CE coding |
| HR system access | System access or interface | API connection or scheduled extract |
| Asset tracking gaps | Asset register enhancement | Add location and category fields |
| Manual processes | Automation | Deploy workflow automation |

### Long-Term Infrastructure Improvements (18-36 months)

Build sustainable data infrastructure:

| Gap Type | Long-Term Solution | Investment Required |
|----------|-------------------|---------------------|
| Fragmented systems | Enterprise Pillar Two solution | SAP PaPM, Oracle EPM, or similar |
| Data governance gaps | Data governance program | Policies, stewardship, quality programs |
| Acquired entity integration | Standard integration playbook | Post-acquisition data onboarding process |
| Global consistency | Global data standards | Common chart of accounts, coding conventions |
| Process maturity | Pillar Two Center of Excellence | Dedicated team and processes |

### Data Gap Register and Action Plan

Maintain a comprehensive register of all identified gaps with remediation plans:

**Data Gap Register Template**

| Gap ID | Description | Category | Entity/Jurisdiction | Severity | Short-Term Solution | Medium-Term Solution | Long-Term Solution | Owner | Target Resolution | Status |
|--------|-------------|----------|---------------------|----------|---------------------|---------------------|-------------------|-------|-------------------|--------|
| GAP-001 | Missing contractor payroll | SBIE | Singapore | High | Estimate from contracts | API feed from payroll provider | Integrate into group HR system | HR Lead | Q2 2026 | In progress |
| GAP-002 | Asset location unknown | SBIE | Germany | Medium | Management allocation | Asset register enhancement | Global asset tracking | FA Lead | Q4 2026 | Not started |
| GAP-003 | Acquired entity pre-acquisition data | Financial | US (NewCo) | High | Not available | Historical data rebuild | Integration complete | M&A Lead | Q1 2027 | Not started |

### Remediation Progress Tracking

Track remediation progress with metrics:

| Metric | Q1 2026 | Q2 2026 | Q3 2026 | Q4 2026 | Target |
|--------|---------|---------|---------|---------|--------|
| Total gaps identified | 25 | 22 | 18 | 12 | 0 |
| Critical gaps open | 5 | 3 | 1 | 0 | 0 |
| High gaps open | 10 | 8 | 6 | 4 | 0 |
| Medium gaps open | 7 | 8 | 8 | 6 | <5 |
| Low gaps open | 3 | 3 | 3 | 2 | <5 |
| Estimates in GIR | 15 | 12 | 8 | 4 | 0 |
| % data from actual | 85% | 90% | 94% | 97% | 100% |

---

## 4.4.5 Transitional Penalty Relief

The OECD's transitional penalty relief provisions provide important protection during the initial years of GloBE compliance, but MNE Groups must demonstrate "reasonable measures" to benefit from this relief.

### Transitional Period Coverage

| Provision | Applicable Period | End Date |
|-----------|-------------------|----------|
| IIR penalty relief | Fiscal years beginning on or before 31 Dec 2026 | FY ending 30 Jun 2028 |
| UTPR penalty relief | Fiscal years beginning on or before 31 Dec 2026 | FY ending 30 Jun 2028 |
| Simplified jurisdictional reporting | Fiscal years beginning on or before 31 Dec 2028 | FY ending 30 Jun 2030 |

### "Reasonable Measures" Standard

While not explicitly defined by the OECD, reasonable measures include:

| Category | Evidence of Reasonable Measures |
|----------|-------------------------------|
| **Data Collection** | Documented data requirements; formal data requests; escalation procedures |
| **Estimation** | Documented estimation methodology; reasonableness testing; approval process |
| **Validation** | Data quality checks; reconciliations; error resolution procedures |
| **Documentation** | Contemporaneous memos; calculation workpapers; audit trail |
| **Governance** | Defined roles and responsibilities; review and approval process |
| **Improvement** | Gap remediation plan; progress tracking; investment in systems |

### Documentation to Demonstrate Reasonable Measures

Maintain evidence package demonstrating good-faith compliance efforts:

| Document | Purpose | Content |
|----------|---------|---------|
| **Pillar Two Compliance Framework** | Overall approach | Policies, procedures, governance structure |
| **Data Gap Register** | Gap management | All gaps identified, assessed, and tracked |
| **Estimation Documentation** | Support estimates | Methodology, calculations, approvals |
| **Remediation Plan** | Improvement commitment | Actions, timelines, investments |
| **Progress Reports** | Track improvement | Metrics, milestones achieved |
| **Lessons Learned** | Continuous improvement | Issues resolved, process improvements |

### Limitations of Penalty Relief

The transitional relief does not apply to:

| Exclusion | Explanation |
|-----------|-------------|
| Avoidance, fraud, or abuse | Intentional non-compliance |
| Unpaid Top-up Tax | Tax liability remains regardless of penalty relief |
| Repeat errors | Failure to correct known issues |
| Lack of documentation | No evidence of reasonable measures |
| Post-transitional periods | Relief expires per schedule above |

### Australian Example: ATO Practical Compliance

The Australian Taxation Office (ATO) has provided guidance on transitional compliance in Practical Compliance Guideline PCG 2025/4 (formerly Draft PCG 2025/D3):

> "Remission of penalties and/or suspension of lodgment enforcement actions may be possible if applicable MNE Groups act in good faith and take 'reasonable measures' to comply with the Minimum Tax law during the transition period."

**Key ATO Points**:
- Onus is on MNE Groups to demonstrate reasonable measures
- ATO will not provide blanket penalty concession
- Documentation of compliance efforts is essential
- Penalty relief is transitional, not permanent

---

## Summary: Handling Data Gaps Process

```
┌─────────────────────────────────────────────────────────────────┐
│                  Handling Data Gaps Process                      │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  PHASE 1: IDENTIFICATION                                         │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │ ✓ Conduct gap identification checklist                   │   │
│  │ ✓ Categorize gaps (Structural/Access/Granularity/Quality)│   │
│  │ ✓ Assess impact (Critical/High/Medium/Low)               │   │
│  │ ✓ Document all identified gaps in Gap Register           │   │
│  └─────────────────────────┬────────────────────────────────┘   │
│                            ▼                                    │
│  PHASE 2: RESOLUTION PLANNING                                    │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │ ✓ Determine if actual data can be obtained               │   │
│  │ ✓ If yes: Source actual data and validate                │   │
│  │ ✓ If no: Select appropriate estimation method            │   │
│  │ ✓ Assign owners and target dates                         │   │
│  └─────────────────────────┬────────────────────────────────┘   │
│                            ▼                                    │
│  PHASE 3: ESTIMATION (if required)                               │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │ ✓ Apply consistent estimation methodology                │   │
│  │ ✓ Document estimation rationale and calculation          │   │
│  │ ✓ Perform reasonableness tests                           │   │
│  │ ✓ Obtain approval for estimates                          │   │
│  └─────────────────────────┬────────────────────────────────┘   │
│                            ▼                                    │
│  PHASE 4: DOCUMENTATION                                          │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │ ✓ Complete Estimate Documentation Forms                  │   │
│  │ ✓ Retain supporting evidence                             │   │
│  │ ✓ Build "reasonable measures" evidence package           │   │
│  │ ✓ Archive documentation for audit trail                  │   │
│  └─────────────────────────┬────────────────────────────────┘   │
│                            ▼                                    │
│  PHASE 5: REMEDIATION                                            │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │ ✓ Implement short-term workarounds                       │   │
│  │ ✓ Plan medium-term system fixes                          │   │
│  │ ✓ Invest in long-term infrastructure                     │   │
│  │ ✓ Track progress toward eliminating gaps                 │   │
│  └──────────────────────────────────────────────────────────┘   │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## Template References

| Template | Description | Format |
|----------|-------------|--------|
| Data_Gap_Register.xlsx | Comprehensive gap tracking with remediation plans | Excel |
| Gap_Identification_Checklist.xlsx | Checklist for identifying data gaps by category | Excel |
| Estimate_Documentation_Form.docx | Template for documenting each estimate | Word |
| Reasonableness_Testing_Workpaper.xlsx | Workpaper for estimate validation tests | Excel |
| Remediation_Progress_Tracker.xlsx | Dashboard for tracking gap closure progress | Excel |
| Reasonable_Measures_Evidence_Index.xlsx | Index of documentation supporting penalty relief | Excel |

---

## Key Takeaways

1. **Data gaps are expected** - 77% of organizations anticipate difficulties obtaining required Pillar Two data

2. **Proactive identification is essential** - Discover gaps early, not during final filing preparation

3. **Categorize and prioritize** - Structural, access, granularity, and quality gaps require different approaches

4. **Estimation is acceptable** - Apply consistent, documented methods when actual data is unavailable

5. **Documentation is critical** - Every estimate must be supported by documented rationale and calculations

6. **"Reasonable measures" protect** - Transitional penalty relief requires demonstrable good-faith compliance efforts

7. **Transitional simplifications help** - Simplified jurisdictional reporting and safe harbours address some data challenges

8. **Remediation is required** - Estimates are temporary; work toward actual data for future filings

9. **Start with 60 data points** - Begin with minimum viable data set and refine as materiality dictates

10. **Build evidence package** - Maintain comprehensive documentation to demonstrate reasonable measures

---

## Sources and References

- [EY: How to Alleviate BEPS 2.0 Pillar Two Data Challenges](https://www.ey.com/en_us/insights/tax/how-to-alleviate-beps-2-0-pillar-two-data-challenges)
- [KPMG: Pillar Two Challenges - Data Gaps, Technology Needs, and Modeling](https://kpmg.com/us/en/articles/2023/pillar-two-data-and-technology.html)
- [Wolters Kluwer: Understanding Data Requirements and Managing Data for Pillar Two](https://www.wolterskluwer.com/en/expert-insights/understanding-beps-pillar-two-data)
- [PwC: Pillar Two Data and Compliance Challenges](https://www.pwc.com/us/en/services/tax/library/pillar-two-compliance-challenges.html)
- [PwC: Pillar Two Readiness - What's Your Data Strategy?](https://www.pwc.com/us/en/services/tax/library/pillar-two-data-strategy.html)
- [OECD: Safe Harbours and Penalty Relief (Pillar Two)](https://www.oecd.org/content/dam/oecd/en/topics/policy-sub-issues/global-minimum-tax/safe-harbours-and-penalty-relief-global-anti-base-erosion-rules-pillar-two.pdf)
- [OECD: GloBE Information Return (Pillar Two)](https://www.oecd.org/content/dam/oecd/en/publications/reports/2023/07/tax-challenges-arising-from-the-digitalisation-of-the-economy-globe-information-return-pillar-two_10977da1/91a49ec3-en.pdf)
- [Citco: Pillar 2 Update - Getting to Grips with the GloBE Information Return](https://www.citco.com/insights/pillar-2-update-getting-to-grips-with-the-globe-information-return)
- [oecdpillars.com: Simplified Calculations Safe Harbours](https://oecdpillars.com/pillar-tab/simplified-calculations-safe-harbours/)
- [Deloitte: Pillar Two in Practice - Seven Lessons from the Front Lines of Compliance](https://www.deloitte.com/us/en/services/tax/articles/pillar-two-seven-lessons-from-compliance.html)
- [ATO: When and How the Pillar Two Rules Apply](https://www.ato.gov.au/businesses-and-organisations/international-tax-for-business/in-detail/multinationals/global-and-domestic-minimum-tax/when-and-how-the-pillar-two-rules-apply)

---

*This section provides practical guidance for handling data gaps that are inevitable in GIR preparation. With comprehensive data gathering strategies now established, the following sections will cover the practical implementation of GIR completion tools and calculators.*
