# Section 9.3: Simplified Reporting Elections

## Learning Objectives

By the end of this section, you will be able to:

- Identify all available elections under the GloBE Rules and their reporting implications
- Distinguish between annual, five-year, and irrevocable elections
- Apply the Transitional Simplified Reporting Election for jurisdictional-level reporting
- Implement simplified calculations for Non-Material Constituent Entities (NMCEs)
- Record elections correctly in the GloBE Information Return
- Manage election procedures across multiple jurisdictions

---

## 9.3.1 Overview of GloBE Elections

### The Election Framework

The GloBE Rules provide numerous elections allowing MNE groups to tailor calculations to their circumstances. These elections significantly impact both Top-up Tax calculations and GIR reporting requirements.

**Election Categories:**

| Category | Duration | Revocability | Scope |
|----------|----------|--------------|-------|
| **Annual Elections** | One fiscal year | Renewable each year | Per entity or jurisdiction |
| **Five-Year Elections** | Five consecutive years | Irrevocable during period | Per jurisdiction |
| **Transitional Elections** | Limited period | Subject to rules | Per group or jurisdiction |
| **Permanent Elections** | Indefinite | May be irrevocable | Varies |

### Why Elections Matter for GIR

Elections affect GIR in multiple ways:

1. **Calculation methodology** - Different inputs and adjustments
2. **Reporting requirements** - What data must be disclosed
3. **Documentation** - Evidence of election made
4. **Consistency** - Year-on-year tracking requirements

---

## 9.3.2 Transitional Simplified Reporting Election

### Overview

The **Transitional Simplified Reporting Election** allows MNE groups to report GloBE calculations at a **jurisdictional level** rather than entity-by-entity, reducing the reporting burden during the initial implementation period.

**Applicability Period:**
- Fiscal years beginning on or before **31 December 2028**
- Fiscal years ending no later than **30 June 2030**

### What the Election Provides

```
TRANSITIONAL SIMPLIFIED REPORTING
=================================

Standard Reporting (Entity Level):
┌─────────────────────────────────────────────────────┐
│ Section 3: Entity-by-Entity Data                    │
│                                                     │
│  Entity 1: [Full GloBE data]                        │
│  Entity 2: [Full GloBE data]                        │
│  Entity 3: [Full GloBE data]                        │
│  ...                                                │
│  Entity N: [Full GloBE data]                        │
└─────────────────────────────────────────────────────┘

Simplified Reporting (Jurisdictional Level):
┌─────────────────────────────────────────────────────┐
│ Section 2: Jurisdictional Aggregates                │
│                                                     │
│  Jurisdiction A: [Aggregate GloBE data]             │
│  Jurisdiction B: [Aggregate GloBE data]             │
│  Jurisdiction C: [Aggregate GloBE data]             │
│                                                     │
│ Section 3: Reduced entity detail                    │
└─────────────────────────────────────────────────────┘
```

### Important Limitation

**The election applies only to reporting—not calculation:**

> "When the GloBE Rules require a calculation to be undertaken at the CE level, this calculation still needs to be done at the CE level even if the information is then reported in an aggregated format in the GIR."

This means:
- ETR calculated at jurisdictional level (as per GloBE Rules)
- SBIE calculated per entity, then aggregated
- Top-up Tax allocated per entity, then reported in aggregate
- Underlying calculations must be retained for audit

### How to Make the Election

The election is made in the GIR by:

1. Selecting the simplified reporting option in the GIR header
2. Reporting jurisdictional aggregates in Section 2
3. Providing reduced entity-level detail in Section 3
4. Retaining full entity-level calculations in working papers

---

## 9.3.3 Simplified Calculations for NMCEs

### What is an NMCE?

A **Non-Material Constituent Entity (NMCE)** is an entity that:

1. Is **not consolidated** on a line-by-line basis in the group's audited consolidated financial statements
2. Is excluded **solely for size or materiality grounds**
3. Has exclusion confirmed by an **external auditor**

**Also includes:**
- Permanent Establishments of NMCEs (if the Main Entity is an NMCE)

### The Simplified Calculations Safe Harbour

The OECD provides simplified calculation methods for NMCEs to reduce data collection burden:

**Three Simplified Calculations:**

| Calculation | Standard Method | Simplified Method |
|-------------|-----------------|-------------------|
| **GloBE Income/Loss** | Full GloBE adjustments | CbCR Total Revenue |
| **GloBE Revenue** | Detailed calculation | CbCR Total Revenue |
| **Adjusted Covered Taxes** | Full tax adjustments | Current Year Accrued Income Tax (CbCR) |

### Simplified Calculations in Detail

#### Simplified Income Calculation

```
SIMPLIFIED INCOME CALCULATION FOR NMCE
======================================

Standard Calculation:
  Accounting Income                           XXX
  + GloBE Adjustments                        XXX
  - GloBE Exclusions                        (XXX)
  = GloBE Income/Loss                        XXX

Simplified Calculation:
  CbCR Total Revenue                         XXX
  = GloBE Income/Loss (simplified)           XXX
```

**Key Point:** GloBE Income equals GloBE Revenue under simplified method.

#### Simplified Tax Calculation

```
SIMPLIFIED TAX CALCULATION FOR NMCE
===================================

Standard Calculation:
  Current Tax Expense                        XXX
  + Deferred Tax Expense                     XXX
  - Non-Covered Taxes                       (XXX)
  +/- Other Adjustments                      XXX
  = Adjusted Covered Taxes                   XXX

Simplified Calculation:
  Current Year Accrued Income Tax (CbCR)     XXX
  = Adjusted Covered Taxes (simplified)      XXX
```

**Excluded from Simplified Calculation:**
- Deferred tax expense
- Adjustments for non-current items
- Provisions for uncertain tax liabilities

### Election Mechanics for NMCEs

| Feature | Rule |
|---------|------|
| **Election type** | Annual |
| **Scope** | Per NMCE (not jurisdictional) |
| **Eligibility** | Must meet NMCE definition |
| **Documentation** | Auditor confirmation of NMCE status |
| **GIR reporting** | Indicate simplified method used |

### NMCE Example

**Scenario:** Small subsidiary excluded from consolidation due to immateriality

```
NMCE SIMPLIFIED CALCULATION EXAMPLE
===================================

Entity: SmallCo Ltd (NMCE)
Jurisdiction: Ireland
Fiscal Year: 2024

CbCR Data:
- Total Revenue: €800,000
- Current Year Accrued Income Tax: €90,000

Simplified Calculation:
- GloBE Income: €800,000 (= CbCR Revenue)
- GloBE Revenue: €800,000 (= CbCR Revenue)
- Adjusted Covered Taxes: €90,000 (= CbCR Tax)

Simplified ETR: €90,000 / €800,000 = 11.25%

Result: ETR below 15%, potential Top-up Tax
(but small amount given NMCE size)
```

---

## 9.3.4 Annual Elections

### Stock-Based Compensation Election (Article 3.2.2)

**Purpose:** Align GloBE income with tax treatment of stock-based compensation

**Standard Treatment:**
- Financial accounting: Fair value at grant date, amortised over vesting
- Creates permanent book-tax differences

**Election Treatment:**
- Replace accounting amount with tax-deductible amount
- Typically deduction at exercise (market value of stock)

**Election Details:**

| Feature | Rule |
|---------|------|
| Type | Annual |
| Scope | Per Constituent Entity |
| Impact | Adjusts GloBE Income |
| Deferred tax | Must be calculated on elected basis |

**Example:**

```
STOCK-BASED COMPENSATION ELECTION
=================================

Without Election:
  Accounting stock-comp expense        €500,000
  Tax deduction allowed                €800,000
  Permanent difference                 €300,000
  ► Lower GloBE Income but no tax effect

With Election:
  GloBE Income adjustment             +€500,000 (remove accounting)
  GloBE Income adjustment             -€800,000 (add tax deduction)
  Net adjustment                      -€300,000
  ► Higher GloBE Income offset by actual tax deduction
  ► Better alignment of income and taxes
```

### Excluded Dividends Election

**Purpose:** Exclude certain dividends from GloBE Income

**Standard Treatment:**
- Short-term portfolio dividends included in GloBE Income
- May create ETR distortion

**Election:** Exclude dividends from portfolio shareholdings (<10% ownership) held for less than one year

### Excluded Equity Gain/Loss Election

**Purpose:** Exclude gains/losses on equity interests from GloBE Income

**Application:** Similar to excluded dividends; applies to gains on disposal of portfolio shareholdings

---

## 9.3.5 Five-Year Elections

### Realisation Basis Election (Article 3.2.5)

**Purpose:** Replace fair value accounting with realisation method for gains/losses

**Standard Treatment:**
- Fair value gains/losses included in GloBE Income as they arise
- Creates volatility in ETR

**Election Treatment:**
- Gains/losses only included when asset/liability is sold
- Excludes fair value adjustments from GloBE Income
- Deferred tax on fair value excluded from Covered Taxes

**Election Details:**

| Feature | Rule |
|---------|------|
| Type | Five-year irrevocable |
| Scope | Per jurisdiction |
| Application | All relevant assets in jurisdiction |
| Renewal | New election after five years |

**Practical Considerations:**
- Beneficial for entities with significant investment portfolios
- Reduces ETR volatility
- Requires tracking of deferred realisation amounts

### Asset Gain/Loss Spreading Election (Article 3.2.6)

**Purpose:** Spread gains/losses on sales of local tangible fixed assets

**Standard Treatment:**
- Full gain/loss in year of sale
- May spike or crash ETR in sale year

**Election Treatment:**
- Spread gain/loss over current year plus four prior years
- Smooths ETR impact of major asset disposals

**Election Details:**

| Feature | Rule |
|---------|------|
| Type | Five-year irrevocable |
| Scope | Per jurisdiction |
| Assets | Local immovable tangible assets |
| Method | Current year plus four prior years (equal spread) |

**Example:**

```
ASSET GAIN SPREADING ELECTION
=============================

Gain on sale of building: €10,000,000

Without Election:
  Year 0: €10,000,000 gain in GloBE Income
  ► ETR impact in single year

With Election:
  Year 0: €2,000,000
  Year -1: €2,000,000 (restate)
  Year -2: €2,000,000 (restate)
  Year -3: €2,000,000 (restate)
  Year -4: €2,000,000 (restate)
  ► Gain spread equally across five years
```

### GloBE Loss Election (Article 4.5)

**Purpose:** Alternative to deferred tax approach for GloBE losses

**Standard Treatment:**
- Deferred tax rules apply
- Track DTAs and recapture

**Election Treatment:**
- Dispense with deferred tax expense calculation
- Establish deemed DTA equal to GloBE loss × 15%
- DTA reduces future Top-up Tax

**Election Details:**

| Feature | Rule |
|---------|------|
| Type | Made in first GIR; generally irrevocable |
| Scope | Per jurisdiction |
| Effect | Simplifies loss tracking |
| Calculation | Loss × 15% = Deemed DTA |

**Example:**

```
GLOBE LOSS ELECTION
===================

Year 1: GloBE Loss of €5,000,000
Year 2: GloBE Income of €3,000,000, ETR 10%

With GloBE Loss Election:

Year 1:
  GloBE Loss: (€5,000,000)
  Deemed DTA: €5,000,000 × 15% = €750,000
  Top-up Tax: €0

Year 2:
  GloBE Income: €3,000,000
  Top-up Tax before DTA: €3,000,000 × 5% = €150,000
  DTA utilised: (€150,000)
  Net Top-up Tax: €0
  Remaining DTA: €600,000
```

---

## 9.3.6 Intra-Group Asset Transfer Elections

### Article 6.3.4 Elections

When assets are transferred between Constituent Entities within the group, elections determine how gains/losses and tax basis are treated.

**Option 1: Exclude gain/loss from GloBE Income**
- Gain/loss excluded from transferor's GloBE Income
- Transferee uses transferor's carrying value
- Deferred tax adjusted accordingly

**Option 2: Include gain/loss in GloBE Income**
- Gain/loss included in transferor's GloBE Income
- Transferee uses acquisition date fair value
- Can elect to spread over five years

**Election Scope:**

| Feature | Rule |
|---------|------|
| Type | Per transaction or per category |
| Timing | Made in year of transfer |
| Assets | Non-inventory assets |
| Documentation | Transfer agreement and election |

### Transition Year Asset Transfers

For transfers occurring between 30 November 2021 and the start of the Transition Year:

- Transferee's basis = Transferor's carrying value at disposition
- DTAs/DTLs brought into GloBE on that basis
- Ensures consistent treatment across transition

---

## 9.3.7 Deferred Tax Elections

### DTL Recapture Election

**Issue:** Certain DTLs must be tracked and recaptured if they don't reverse within five years

**Election:** Make an "unclaimed accrual" election for DTL categories not expected to reverse within five years

**Effect:**
- DTL benefit not claimed in Covered Taxes initially
- Avoids recapture requirement
- Simplifies tracking

### Annual Exclusion of DTL Increase

**Election:** Exclude deferred tax expense related to DTL increases from Adjusted Covered Taxes on an annual basis

**Application:**
- Available for specific DTL categories
- Prevents benefit that would need to be tracked for recapture
- Reduces compliance complexity

---

## 9.3.8 Election Tracking and Documentation

### Election Register

MNE groups should maintain a comprehensive election register:

```
GLOBE ELECTION REGISTER
=======================

Group: [MNE Group Name]
Prepared by: [Name]
Last Updated: [Date]

ANNUAL ELECTIONS (FY2024)

| Election              | Jurisdiction | Entity        | Made? | GIR Reference |
|-----------------------|--------------|---------------|-------|---------------|
| Stock Compensation    | UK           | UK HoldCo     | Yes   | Section 2.4   |
| Stock Compensation    | Germany      | DE OpCo       | No    | N/A           |
| NMCE Simplified Calc  | Ireland      | IE SmallCo    | Yes   | Section 3.7   |
| Excluded Dividends    | Netherlands  | NL FinCo      | Yes   | Section 2.6   |

FIVE-YEAR ELECTIONS

| Election              | Jurisdiction | Start Year | End Year | Renewable |
|-----------------------|--------------|------------|----------|-----------|
| Realisation Basis     | UK           | 2024       | 2028     | 2029      |
| Asset Gain Spreading  | Germany      | 2024       | 2028     | 2029      |
| GloBE Loss            | Singapore    | 2024       | N/A      | N/A       |

TRANSITIONAL ELECTIONS

| Election                        | Scope     | Start    | End      |
|---------------------------------|-----------|----------|----------|
| Transitional Simplified Report  | Group     | 2024     | 2028     |
| Transitional CbCR Safe Harbour  | Various   | 2024     | 2026     |
```

### Documentation Requirements

**Per Election:**

| Document | Purpose |
|----------|---------|
| Election form/memo | Record of decision made |
| Board/management approval | Governance evidence |
| Impact analysis | Rationale for election |
| Calculation workpapers | Application of election |
| GIR extract | Where reported |
| Renewal tracker | For time-limited elections |

---

## 9.3.9 Jurisdictional Variations

### How Jurisdictions Implement Elections

While the OECD Model Rules are consistent, jurisdictional implementation may vary:

| Jurisdiction | Election Approach | Notable Variations |
|--------------|-------------------|-------------------|
| **UK** | Follows OECD model | Elections made in MTT return |
| **Germany** | Follows OECD model | Separate MinStG election provisions |
| **Netherlands** | Follows OECD model | Specific election procedures |
| **France** | Follows OECD model | Local filing requirements |
| **Australia** | Follows OECD model | Elections in CGDMTR |

### Local Filing of Elections

Some jurisdictions require elections to be filed locally in addition to the GIR:

**Example - UK:**
- Elections made in Multinational Top-up Tax (MTT) return
- Certain elections notified to HMRC separately
- GIR reflects elections made

**Example - Germany:**
- Elections documented in Mindeststeuer-Erklärung
- BZSt notification for specific elections
- Consistency with GIR required

---

## 9.3.10 Practical Application

### Election Decision Framework

When deciding whether to make an election:

```
ELECTION DECISION FRAMEWORK
===========================

Step 1: Identify Available Elections
        └── Review all elections applicable to group's circumstances

Step 2: Model Impact
        └── Calculate effect on:
            - GloBE Income
            - Covered Taxes
            - ETR
            - Top-up Tax

Step 3: Assess Long-Term Implications
        └── Consider:
            - Five-year lock-in periods
            - Consistency requirements
            - Future business changes

Step 4: Document Rationale
        └── Record:
            - Why election made (or not made)
            - Expected impact
            - Risks considered

Step 5: Implement in GIR
        └── Report:
            - Election indicator
            - Adjusted calculations
            - Supporting schedules

Step 6: Track and Monitor
        └── Maintain:
            - Election register
            - Renewal dates
            - Ongoing compliance
```

### Case Study: Comprehensive Election Analysis

**Scenario:** UK-headquartered technology company with operations in UK, Germany, Ireland, and Singapore

**Relevant Facts:**
- Significant stock-based compensation expense
- Investment property portfolio (fair value accounting)
- Small immaterial subsidiary in Ireland (NMCE)
- Prior year loss in Singapore

**Election Analysis:**

| Jurisdiction | Issue | Election | Decision | Rationale |
|--------------|-------|----------|----------|-----------|
| UK | Stock compensation mismatch | Stock-based Compensation Election | MAKE | Tax deduction > accounting expense; improves ETR alignment |
| UK | Investment property volatility | Realisation Basis Election | MAKE | Significant FV movements; prefer realisation timing |
| Germany | Stock compensation mismatch | Stock-based Compensation Election | MAKE | Consistent with UK approach |
| Ireland | NMCE compliance burden | Simplified Calculations | MAKE | Entity below materiality; use CbCR data |
| Singapore | Prior year loss | GloBE Loss Election | MAKE | Simplifies loss tracking; creates deemed DTA |

**GIR Reporting:**

```
GIR ELECTIONS SUMMARY (FY2024)
==============================

Section 1: Group Elections
- Transitional Simplified Reporting: ELECTED

Section 2: Jurisdictional Elections
- UK: Realisation Basis (5-year)
- UK: Stock-based Compensation (annual)
- Germany: Stock-based Compensation (annual)
- Singapore: GloBE Loss Election

Section 3: Entity Elections
- IE SmallCo Ltd: NMCE Simplified Calculations
```

---

## Deliverable: Simplified Reporting Elections Forms

### Template 1: Annual Election Form

```
GLOBE ANNUAL ELECTION FORM
==========================

PART A: ELECTION IDENTIFICATION

MNE Group: _________________________________________
Fiscal Year: _______________________________________
Jurisdiction: ______________________________________
Constituent Entity (if applicable): _________________
Election Type: _____________________________________
Article Reference: _________________________________

PART B: ELECTION DETAILS

Description of Election:
________________________________________________________
________________________________________________________

Effective Date: _______________________________________

Impact on GloBE Calculations:

| Metric              | Without Election | With Election | Difference |
|---------------------|------------------|---------------|------------|
| GloBE Income        | €____________    | €____________ | €_________ |
| Covered Taxes       | €____________    | €____________ | €_________ |
| ETR                 | ____________%    | ____________% | _________% |
| Top-up Tax          | €____________    | €____________ | €_________ |

PART C: RATIONALE

Reason for making this election:
________________________________________________________
________________________________________________________
________________________________________________________

PART D: AUTHORISATION

Prepared by: ______________________ Date: ______________
Reviewed by: ______________________ Date: ______________
Approved by: ______________________ Date: ______________

PART E: GIR REFERENCE

GIR Section: _________________
Line/Field Reference: _________________
```

### Template 2: Five-Year Election Register

```
FIVE-YEAR ELECTION REGISTER
===========================

Group: _______________________________________________
As at: _______________________________________________

ACTIVE FIVE-YEAR ELECTIONS

Election 1:
┌─────────────────────────────────────────────────────────┐
│ Election Type: _____________________________________   │
│ Jurisdiction: ______________________________________   │
│ Article Reference: _________________________________   │
│                                                         │
│ Election Period:                                        │
│   Start Year: _________ End Year: _________            │
│                                                         │
│ Status:                                                 │
│   □ Year 1  □ Year 2  □ Year 3  □ Year 4  □ Year 5     │
│                                                         │
│ Renewal Date: _______________________________________   │
│ Renewal Decision Due: _______________________________   │
│                                                         │
│ Notes: _____________________________________________   │
└─────────────────────────────────────────────────────────┘

Election 2:
┌─────────────────────────────────────────────────────────┐
│ Election Type: _____________________________________   │
│ Jurisdiction: ______________________________________   │
│ Article Reference: _________________________________   │
│                                                         │
│ Election Period:                                        │
│   Start Year: _________ End Year: _________            │
│                                                         │
│ Status:                                                 │
│   □ Year 1  □ Year 2  □ Year 3  □ Year 4  □ Year 5     │
│                                                         │
│ Renewal Date: _______________________________________   │
│ Renewal Decision Due: _______________________________   │
│                                                         │
│ Notes: _____________________________________________   │
└─────────────────────────────────────────────────────────┘

[Continue for additional elections]

ELECTIONS EXPIRING WITHIN 12 MONTHS

| Election | Jurisdiction | Expiry Date | Renewal Decision |
|----------|--------------|-------------|------------------|
| ________ | ____________ | ___________ | □ Renew □ Lapse  |
| ________ | ____________ | ___________ | □ Renew □ Lapse  |

ELECTION RENEWAL WORKFLOW

□ Review election 6 months before expiry
□ Model impact of renewal vs. lapse
□ Document decision and rationale
□ Obtain management approval
□ Update GIR for new election period
```

### Template 3: NMCE Simplified Calculation Worksheet

```
NMCE SIMPLIFIED CALCULATION WORKSHEET
=====================================

PART A: NMCE IDENTIFICATION

Entity Name: ________________________________________
Jurisdiction: _______________________________________
Fiscal Year: ________________________________________

NMCE Status Confirmation:
□ Entity excluded from line-by-line consolidation
□ Exclusion is solely for size/materiality grounds
□ External auditor has confirmed NMCE status

Auditor Name: _______________________________________
Confirmation Date: __________________________________

PART B: SIMPLIFIED CALCULATIONS

Data Source: Country-by-Country Report for FY________

Simplified Income Calculation:
  CbCR Total Revenue                    €______________
  = GloBE Income (Simplified)           €______________

Simplified Revenue Calculation:
  CbCR Total Revenue                    €______________
  = GloBE Revenue (Simplified)          €______________

Simplified Tax Calculation:
  CbCR Current Year Accrued Income Tax  €______________
  = Adjusted Covered Taxes (Simplified) €______________

Simplified ETR:
  Covered Taxes / GloBE Income          ______________%

PART C: IMPACT ANALYSIS

Jurisdictional ETR (including NMCE):    ______________%
Top-up Tax impact (if any):             €______________

PART D: DOCUMENTATION

□ CbCR extract attached
□ Auditor NMCE confirmation attached
□ Calculation workpaper retained
□ GIR election indicator marked

PART E: SIGN-OFF

Prepared by: ______________________ Date: ______________
Reviewed by: ______________________ Date: ______________
```

---

## Section Summary

GloBE elections provide significant flexibility in how MNE groups calculate and report their Pillar Two obligations:

1. **Transitional Simplified Reporting** - Jurisdictional-level reporting during implementation
2. **NMCE Simplified Calculations** - CbCR-based calculations for immaterial entities
3. **Annual Elections** - Stock compensation, dividends, equity gains
4. **Five-Year Elections** - Realisation basis, asset gain spreading, GloBE loss
5. **Asset Transfer Elections** - Intra-group transfer treatment

Proper election management requires:
- Comprehensive election registers
- Impact modelling before decisions
- Consistent application across the group
- Tracking of renewal dates for time-limited elections
- Coordination with local filing requirements

---

## Key Takeaways

| Topic | Key Point |
|-------|-----------|
| **Transitional Simplified Reporting** | Jurisdictional aggregation until FY ending June 2030 |
| **NMCE Definition** | Excluded from consolidation for materiality only |
| **NMCE Simplified Calculations** | Use CbCR revenue and current tax |
| **Stock Compensation** | Annual election per entity |
| **Realisation Basis** | Five-year irrevocable per jurisdiction |
| **GloBE Loss Election** | Made in first GIR; creates deemed DTA |
| **Documentation** | Maintain election register and workpapers |
| **Local Filing** | Some jurisdictions require separate election filing |

---

## Sources

Key references for this section include:

- [OECD Simplified Calculations Safe Harbours](https://oecdpillars.com/pillar-tab/simplified-calculations-safe-harbours/)
- [Pillar Two Transitional Simplified Reporting Election](https://oecdpillars.com/pillar-tab/pillar-two-transitional-reporting-election/)
- [Stock-Based Compensation Election](https://oecdpillars.com/pillar-two-elections/stock-based-compensation-election/)
- [GloBE Loss Election](https://oecdpillars.com/pillar-two-elections/globe-loss-election/)
- [KPMG - Administrative Guidance on GloBE Model Rules](https://assets.kpmg.com/content/dam/kpmg/xx/pdf/2023/12/globe-model-rules-pillar-two.pdf)

---

*Section 9.3 Complete. Proceed to Section 9.4: Safe Harbour Documentation for GIR.*
