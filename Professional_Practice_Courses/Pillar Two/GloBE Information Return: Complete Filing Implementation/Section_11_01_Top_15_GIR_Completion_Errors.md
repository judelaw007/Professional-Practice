# Section 11.1: Top 15 GIR Completion Errors

## Learning Objectives

By the end of this section, you will be able to:
- Identify the 15 most common GIR completion errors
- Understand root causes behind each error category
- Apply prevention strategies to avoid errors in initial filings
- Implement correction procedures when errors are discovered
- Prioritise quality assurance efforts based on error frequency and impact

---

## Introduction

Tax authorities across implementing jurisdictions have already begun identifying recurring errors in Pillar Two filings. The French tax administration, for example, has specifically warned taxpayers about common mistakes in GloBE-related filings, noting that these errors "could have substantial consequences and lead to penalties."

This section analyses the 15 most common GIR completion errors, providing practitioners with:
- Detailed error descriptions
- Root cause analysis
- Prevention strategies
- Correction procedures

The errors are presented in order of frequency and impact based on early compliance experience across multiple jurisdictions.

---

## Error 1: Incorrect Constituent Entity Identification

### Error Description

Failure to correctly identify all Constituent Entities (CEs) within the MNE Group, resulting in either:
- **Omission errors**: Entities that should be included are excluded
- **Inclusion errors**: Entities that should be excluded are incorrectly included
- **Classification errors**: Entities assigned to wrong ownership categories

### Common Manifestations

| Error Type | Example | Impact |
|------------|---------|--------|
| Missed subsidiary | Recently acquired entity not included | Understated GloBE Income |
| Dormant entity excluded | Inactive company with tax losses omitted | Lost loss carry-forward benefit |
| PE not identified | Branch operations not treated as separate CE | Incorrect jurisdictional allocation |
| Flow-through missed | Partnership interest not properly attributed | GloBE Income misallocation |
| JV misclassified | 45% owned JV treated as CE instead of JV | Incorrect ownership allocation |

### Root Causes

1. **Incomplete entity register**: Group legal entity database not aligned with consolidation scope
2. **Acquisition lag**: Newly acquired entities not promptly added to GloBE tracking
3. **PE identification gaps**: Permanent establishments not separately tracked in finance systems
4. **Ownership threshold confusion**: Misunderstanding of >50% control test versus ownership percentage
5. **Consolidation scope mismatch**: Using statutory consolidation scope rather than GloBE-specific scope

### Prevention Strategy

**Three-Way Reconciliation Process:**

```
Step 1: Extract consolidation entity list from group reporting system
Step 2: Extract legal entity register from company secretarial database
Step 3: Extract prior year GIR entity list (if applicable)

Reconcile all three sources:
- Identify additions (new acquisitions, formations)
- Identify deletions (disposals, liquidations, mergers)
- Identify reclassifications (ownership changes affecting status)

Document all differences and resolution
```

**Key Control Points:**

| Control | Frequency | Owner |
|---------|-----------|-------|
| M&A notification to tax | Per transaction | Corporate Development |
| Entity register reconciliation | Quarterly | Group Tax |
| PE status review | Annual | International Tax |
| Ownership threshold monitoring | Semi-annual | Legal/Tax |

### Correction Procedure

1. Identify all affected CEs through comprehensive reconciliation
2. Determine fiscal years impacted
3. Recalculate all affected jurisdictional ETRs
4. Prepare amended GIR with corrected CE list
5. Quantify Top-up Tax impact
6. File amendment with supporting documentation
7. Implement preventive controls for future periods

---

## Error 2: Ownership Percentage Miscalculation

### Error Description

Incorrect calculation of ownership percentages used for:
- Determining CE status (>50% ownership test)
- Allocating GloBE Income to POPEs and minority interests
- Calculating Top-up Tax allocations under IIR/UTPR

### Common Manifestations

| Error Type | Example | Impact |
|------------|---------|--------|
| Direct vs. indirect | Only direct holding considered | CE status incorrect |
| Voting vs. economic | Voting rights used instead of ownership interest | Allocation errors |
| Dilution events | Stock options/convertibles not factored | Ownership overstated |
| Cross-holdings | Circular ownership structures miscalculated | Multiple errors |
| Weighted average | Mid-year changes not time-weighted | Incorrect annual allocation |

### Root Causes

1. **Static ownership data**: Using year-end snapshot instead of weighted average
2. **Instrument complexity**: Convertible instruments not properly analysed
3. **Multi-tier structures**: Indirect ownership through multiple tiers miscalculated
4. **Cross-border complexity**: Different legal concepts of ownership across jurisdictions
5. **System limitations**: Finance systems not tracking GloBE-specific ownership metrics

### Prevention Strategy

**Ownership Calculation Framework:**

```
For each Constituent Entity:

1. Identify all ownership paths from UPE
2. For each path:
   a. Calculate direct ownership at each tier
   b. Multiply through to get indirect ownership
3. Sum all paths for total ownership percentage
4. Apply time-weighting for mid-year changes:
   Weighted % = Σ (Ownership % × Days held) / Total days in FY
5. Document calculation with supporting evidence
```

**Ownership Change Protocol:**

| Event | Required Action | Timeline |
|-------|-----------------|----------|
| Acquisition | Update ownership register, notify GloBE team | Within 30 days |
| Disposal | Update register, recalculate all affected percentages | Within 30 days |
| Reorganisation | Full ownership recalculation for affected entities | Within 60 days |
| Year-end | Verify all ownership percentages against legal records | Pre-GIR filing |

### Correction Procedure

1. Obtain legal ownership evidence (share registers, partnership agreements)
2. Recalculate correct ownership percentages for all affected entities
3. Determine impact on CE status, POPE/JV classification
4. Recalculate GloBE Income/Loss allocations
5. Recalculate Top-up Tax allocations
6. File amended GIR if changes are material
7. Document lessons learned for process improvement

---

## Error 3: Excluded Entity Misclassification

### Error Description

Incorrect classification of entities as Excluded Entities under Article 1.5, or failure to recognise entities that qualify for exclusion.

### Excluded Entity Categories (Article 1.5.1)

| Category | Definition | Common Errors |
|----------|------------|---------------|
| Governmental Entity | Entity owned by government performing governmental functions | Commercial SOEs incorrectly excluded |
| International Organisation | Established by treaty, primarily intergovernmental | NGOs incorrectly treated as IOs |
| Non-profit Organisation | Established for religious, charitable, educational purposes | Operating subsidiaries included |
| Pension Fund | Regulated entity providing retirement benefits | Pension services entities confused |
| Investment Fund (UPE) | Investment fund that is UPE of MNE Group | Non-UPE funds incorrectly excluded |
| REIT (UPE) | Real estate vehicle that is UPE of MNE Group | Non-UPE REITs incorrectly excluded |

### Extended Exclusion Rules

**95% Ownership Test (Article 1.5.2(a)):**
An entity 95%+ owned by Excluded Entities qualifies if it:
- Operates exclusively to hold assets/invest funds for benefit of Excluded Entity, OR
- Carries out activities ancillary to Excluded Entity's activities

**85% Ownership Test (Article 1.5.2(b)):**
An entity 85%+ owned by Excluded Entities (excluding Pension Services Entities) qualifies if substantially all income is Excluded Dividends or Excluded Equity Gain/Loss.

### Root Causes

1. **Pension Fund confusion**: Mixing up Pension Funds (excluded) with Pension Services Entities (not excluded)
2. **Investment Entity vs. Investment Fund**: Failing to distinguish Investment Funds (UPE = excluded) from Investment Entities (special rules apply)
3. **Ownership threshold errors**: Misapplying 95%/85% tests for extended exclusions
4. **Activity test failures**: Not verifying "exclusively" or "substantially all" conditions
5. **Documentation gaps**: Insufficient records to support exclusion claims

### Prevention Strategy

**Excluded Entity Assessment Checklist:**

```
For each potential Excluded Entity:

□ Primary exclusion test (Article 1.5.1):
  □ Governmental Entity - government ownership AND governmental function?
  □ International Organisation - treaty-based AND intergovernmental?
  □ Non-profit - established for qualifying purpose AND no private benefit?
  □ Pension Fund - regulated AND provides retirement benefits?
  □ Investment Fund - is this entity the UPE of the MNE Group?
  □ REIT - is this entity the UPE of the MNE Group?

□ Extended exclusion test (Article 1.5.2):
  □ 95%+ owned by Excluded Entities?
    □ If yes: exclusively holds assets/invests OR ancillary activities?
  □ 85%+ owned by Excluded Entities (non-Pension Services)?
    □ If yes: substantially all income is Excluded Dividends/Gains?

□ Documentation obtained and retained
□ Annual status reconfirmation scheduled
```

### Correction Procedure

1. Review classification evidence for each entity claimed as excluded
2. Apply correct Article 1.5.1 or 1.5.2 tests
3. Reclassify entities as CEs where exclusion criteria not met
4. Include newly identified CEs in jurisdictional calculations
5. Recalculate affected ETRs and Top-up Tax
6. File amended GIR
7. Establish annual reconfirmation process

---

## Error 4: GloBE Income/Loss Calculation Errors

### Error Description

Incorrect calculation of GloBE Income or Loss, which forms the numerator for ETR calculations and the basis for Top-up Tax computations.

### Common Manifestations

| Error Type | Example | Impact |
|------------|---------|--------|
| FANIL baseline error | Using tax accounts instead of financial accounts | Fundamental miscalculation |
| Policy choice inconsistency | Different accounting policies across entities | Non-comparable results |
| Excluded income inclusion | International shipping income not excluded | Overstated GloBE Income |
| Dividend elimination | Intra-group dividends not properly eliminated | Double-counting |
| Prior period adjustment | Opening adjustments not correctly allocated | Wrong fiscal year |

### GloBE Income Adjustments Framework

**Starting Point:**
Financial Accounting Net Income or Loss (FANIL) per consolidated financial statements

**Required Adjustments:**

| Adjustment | Direction | Reference |
|------------|-----------|-----------|
| Net taxes expense | Add back | Art. 3.2.1(a) |
| Excluded dividends | Deduct | Art. 3.2.1(b) |
| Excluded equity gain/loss | Deduct | Art. 3.2.1(c) |
| Included revaluation method gain/loss | Add/Deduct | Art. 3.2.1(d) |
| Asymmetric foreign currency gain/loss | Deduct | Art. 3.2.1(e) |
| Policy disallowed expenses | Add back | Art. 3.2.1(f) |
| Prior period errors | Adjust | Art. 3.2.1(g) |
| Accrued pension expense | Adjust | Art. 3.2.1(h) |
| Stock-based compensation | Optional election | Art. 3.2.2 |
| Asset gain/loss | Optional election | Art. 3.2.3-3.2.5 |
| Intra-group transactions | Eliminate | Art. 3.2.6 |

### Root Causes

1. **FANIL sourcing errors**: Using wrong accounting framework (tax vs. GAAP vs. IFRS)
2. **Adjustment omissions**: Missing required adjustments from statutory to GloBE basis
3. **Election tracking failures**: Not consistently applying optional elections
4. **Intercompany elimination issues**: Incomplete or incorrect elimination entries
5. **Currency translation timing**: Using wrong exchange rates for adjustments

### Prevention Strategy

**GloBE Income Calculation Template:**

| Line | Description | Amount (€) | Reference |
|------|-------------|------------|-----------|
| 1 | FANIL per financial statements | ___ | [Source] |
| 2 | Add: Net taxes expense | ___ | Art. 3.2.1(a) |
| 3 | Less: Excluded dividends | ___ | Art. 3.2.1(b) |
| 4 | Less: Excluded equity gains | ___ | Art. 3.2.1(c) |
| 5 | Adjust: Foreign currency | ___ | Art. 3.2.1(e) |
| 6 | Add: Disallowed expenses | ___ | Art. 3.2.1(f) |
| 7 | Adjust: Prior period errors | ___ | Art. 3.2.1(g) |
| 8 | Adjust: Pension expenses | ___ | Art. 3.2.1(h) |
| 9 | Election: Stock compensation | ___ | If elected |
| 10 | Election: Asset revaluation | ___ | If elected |
| 11 | Less: Intercompany eliminations | ___ | Art. 3.2.6 |
| 12 | **GloBE Income/(Loss)** | ___ | Sum |

### Correction Procedure

1. Reconcile FANIL to audited financial statements
2. Verify each adjustment is correctly calculated
3. Confirm election consistency across all CEs and fiscal years
4. Trace intercompany eliminations to consolidation workpapers
5. Recalculate jurisdictional totals
6. Assess ETR and Top-up Tax impact
7. File amendment if material

---

## Error 5: Covered Taxes Misallocation

### Error Description

Incorrect identification, calculation, or allocation of Covered Taxes to jurisdictions, affecting ETR calculations.

### Common Manifestations

| Error Type | Example | Impact |
|------------|---------|--------|
| Current tax only | Deferred tax movements excluded | Understated Covered Taxes |
| Wrong jurisdiction | Tax allocated to HQ instead of local CE | ETR distortion |
| Withholding tax omission | WHT on intercompany not included | Understated local Covered Taxes |
| CFC tax allocation | Parent's CFC tax not pushed to low-tax jurisdiction | Incorrect ETR |
| Uncertain tax positions | UTP reserves not properly adjusted | Timing mismatch |

### Covered Taxes Categories

**Included in Covered Taxes (Article 4.2.1):**

| Category | Examples |
|----------|----------|
| Taxes on income | Corporate income tax, state/local income tax |
| Taxes in lieu | Withholding tax on deemed distributions |
| Qualified domestic top-up tax | QDMTT paid to local jurisdiction |
| Taxes allocated from other CEs | CFC taxes, taxes on transparent entities |
| Deferred tax adjustments | Movement in deferred tax assets/liabilities |

**Excluded from Covered Taxes (Article 4.2.2):**

| Exclusion | Rationale |
|-----------|-----------|
| Top-up Tax | Not included in ETR calculation |
| Disqualified refundable imputation tax | Below minimum threshold |
| Taxes paid by insurance company for policyholders | Not CE's own tax |

### Root Causes

1. **Deferred tax complexity**: Incorrect treatment of DTL recapture, temporary vs. permanent differences
2. **Push-down failures**: CFC taxes not allocated to low-tax CE
3. **WHT tracking gaps**: Withholding taxes not mapped to correct receiving jurisdiction
4. **Uncertain tax positions**: Provisions for uncertain positions not adjusted
5. **Tax consolidation**: Allocation within tax groups incorrectly determined

### Prevention Strategy

**Covered Taxes Allocation Framework:**

```
For each Constituent Entity:

1. Current Tax Expense
   □ Extract from CE's local tax return or provision
   □ Verify jurisdiction matches CE location
   □ Include state/provincial taxes where applicable

2. Withholding Taxes
   □ Identify all WHT suffered on inbound income
   □ Include in CE's Covered Taxes (receiving jurisdiction)
   □ Cross-reference to intercompany payment records

3. CFC/Controlled Taxes
   □ Identify CFC taxes paid by parent entities
   □ Push down to low-tax CE that generated income
   □ Document allocation methodology

4. Deferred Tax Adjustments
   □ Calculate opening vs. closing deferred tax
   □ Apply recapture rules for DTLs (Article 4.4)
   □ Exclude taxes related to Excluded Income

5. Total Covered Taxes = 1 + 2 + 3 + 4
```

### Correction Procedure

1. Reconcile Covered Taxes to tax provision workpapers
2. Verify jurisdictional allocation of each component
3. Check deferred tax movement calculations
4. Confirm push-down of CFC taxes applied correctly
5. Recalculate ETR for affected jurisdictions
6. Assess Top-up Tax impact
7. File amendment with detailed reconciliation

---

## Error 6: Substance-Based Income Exclusion (SBIE) Data Errors

### Error Description

Incorrect calculation of the Substance-Based Income Exclusion, which reduces the Excess Profit base for Top-up Tax calculations.

### SBIE Formula

```
SBIE = (Payroll Carve-out Rate × Eligible Payroll Costs) +
       (Tangible Asset Carve-out Rate × Eligible Tangible Assets)
```

**Transition Period Rates:**

| Fiscal Year Start | Payroll Rate | Tangible Asset Rate |
|-------------------|--------------|---------------------|
| 2024 | 9.8% | 7.8% |
| 2025 | 9.6% | 7.6% |
| 2026 | 9.4% | 7.4% |
| 2027 | 9.2% | 7.2% |
| 2028 | 9.0% | 7.0% |
| 2029 | 8.2% | 6.6% |
| 2030 | 7.4% | 6.2% |
| 2031 | 6.6% | 5.8% |
| 2032 | 5.8% | 5.4% |
| 2033+ | 5.0% | 5.0% |

### Common Manifestations

| Error Type | Example | Impact |
|------------|---------|--------|
| Wrong rate year | Using 5% instead of transition rate | Understated SBIE |
| Payroll scope | Excluding stock compensation | Understated eligible payroll |
| Asset valuation | Using tax basis instead of book value | Incorrect asset carve-out |
| Mobile employees | Not allocating across jurisdictions | Wrong jurisdictional SBIE |
| Capitalised payroll | Double-counting in both carve-outs | Overstated SBIE |
| Leased assets | Including operating lease ROU assets incorrectly | Overstated SBIE |

### Root Causes

1. **Payroll data gaps**: Employee cost data not jurisdictionally allocated
2. **Asset location tracking**: Fixed asset register doesn't track physical location
3. **Mobile asset/employee complexity**: Time-based allocation not performed
4. **Capitalisation treatment**: Payroll capitalised into assets counted twice
5. **Transition rate confusion**: Using wrong year's rates

### Prevention Strategy

**SBIE Data Collection Checklist:**

```
Eligible Payroll Costs:
□ Base salaries and wages
□ Bonuses and commissions
□ Employer payroll taxes
□ Employer pension contributions
□ Stock-based compensation (financial accounts amount)
□ Other employee benefits
□ LESS: Payroll capitalised into tangible assets
□ LESS: Payroll for mobile employees (pro-rata to other jurisdictions)

Eligible Tangible Assets (Average Carrying Value):
□ Property, plant and equipment
□ Natural resources
□ Lessee's right-of-use assets (finance leases only)
□ Licence/concession agreements for real property use
□ LESS: Assets located in other jurisdictions (pro-rata)
□ LESS: Assets held for sale
□ LESS: Assets used to earn excluded income

Calculation:
Opening NBV: ___
Closing NBV: ___
Average: (Opening + Closing) / 2 = ___
```

### Correction Procedure

1. Verify payroll data extraction from HR/payroll systems
2. Confirm asset data reconciles to fixed asset register
3. Check transition rates for correct fiscal year
4. Verify mobile employee/asset allocations
5. Eliminate double-counting of capitalised payroll
6. Recalculate SBIE for all affected jurisdictions
7. Assess impact on Excess Profit and Top-up Tax
8. File amendment if material

---

## Error 7: Intra-Group Transaction Double-Counting

### Error Description

Failure to properly eliminate intra-group transactions, resulting in GloBE Income being counted in multiple jurisdictions.

### Common Manifestations

| Error Type | Example | Impact |
|------------|---------|--------|
| Revenue/cost mismatch | Sale recognised but cost not eliminated | Overstated group income |
| Intercompany dividends | Dividend not excluded per Article 3.2.1(b) | Double-counted income |
| Intercompany interest | Interest income/expense not matched | Jurisdictional distortion |
| Royalties | Royalty income included without expense offset | Inflated licensor income |
| Management fees | Fees not netted across entities | Income overstatement |

### GloBE Elimination Requirements

**Article 3.2.6 - Intra-Group Transactions:**

Unrealised gains and losses from transactions between CEs must be eliminated from jurisdictional GloBE Income calculations when:
- Assets remain within the consolidated group
- Applying the same elimination principles used in consolidation

**Key Principle:**
Intra-group transactions should not create GloBE Income/Loss until realised through transaction with third party.

### Root Causes

1. **Timing differences**: Intercompany invoices recorded in different periods
2. **Currency mismatches**: FX rates differ between buyer and seller recognition
3. **Accounting policy differences**: Different recognition policies across CEs
4. **System limitations**: ERP cannot identify all intercompany counterparties
5. **Manual process failures**: Elimination entries manually prepared with errors

### Prevention Strategy

**Intercompany Reconciliation Protocol:**

```
Pre-Filing Reconciliation:

1. Extract all intercompany transactions by:
   - Counterparty entity
   - Transaction type (sales, interest, royalty, dividend, etc.)
   - Jurisdiction

2. Match transactions:
   - Payer amount = Payee amount (in functional currency)
   - Timing alignment (same fiscal period)
   - Classification alignment (same transaction type)

3. Identify and resolve breaks:
   - Timing differences: Adjust to common recognition point
   - FX differences: Use consistent rate
   - Unmatched items: Investigate and correct

4. Verify eliminations:
   - Group-level eliminations applied
   - No double-counting in jurisdictional totals
   - Unrealised profit eliminated from asset values
```

### Correction Procedure

1. Perform comprehensive intercompany reconciliation
2. Identify all uneliminated transactions
3. Determine jurisdictional impact of each item
4. Apply correct elimination entries
5. Recalculate affected jurisdictional ETRs
6. Quantify Top-up Tax impact
7. File amendment with supporting reconciliation

---

## Error 8: Currency Conversion Errors

### Error Description

Incorrect application of exchange rates when converting local currency amounts to the GIR presentation currency.

### GloBE Currency Requirements

**General Rule (Article 1.1):**
All amounts in the GIR should be reported in the currency used in the UPE's Consolidated Financial Statements.

**Translation Methodology:**

| Data Type | Exchange Rate | Reference |
|-----------|---------------|-----------|
| Income/expense items | Average rate for fiscal year | Per consolidation |
| Balance sheet items | Closing rate at fiscal year end | Per consolidation |
| Top-up Tax | Rate at payment date | Practical |
| Prior year adjustments | Historical rate when originated | Consistency |

### Common Manifestations

| Error Type | Example | Impact |
|------------|---------|--------|
| Rate source inconsistency | Using different rate sources across CEs | Non-comparable data |
| Spot vs. average confusion | Using spot rate for income items | Volatility introduced |
| Historical rate errors | Using current rate for prior period items | Comparability lost |
| Rounding accumulation | Small rounding errors compounding | Material variance |
| Hyperinflation adjustment | Not applying IAS 29 where required | Misstated values |

### Root Causes

1. **Multiple rate sources**: Different CEs using different FX rate providers
2. **Timing mismatches**: Rates extracted at different points
3. **Manual entry errors**: Transcription mistakes in rate entry
4. **System configuration**: ERP currency settings incorrect
5. **Methodology inconsistency**: Different translation methods across entities

### Prevention Strategy

**Currency Conversion Controls:**

```
1. Designate Single Rate Source
   - Specify approved FX rate provider (e.g., central bank, ECB)
   - Document rate extraction timing (e.g., daily close)
   - Maintain rate archive for audit trail

2. Standardise Translation Methodology
   - Income/expense: Average rate (specify calculation method)
   - Balance sheet: Closing rate at FY end
   - Document methodology in GIR procedures manual

3. Implement Reconciliation Checks
   - Verify rates used match designated source
   - Cross-check translation to consolidation workpapers
   - Perform reasonableness test (year-on-year comparison)

4. Handle Special Situations
   - Hyperinflationary economies: Apply IAS 29
   - Restricted currencies: Document approach
   - Mid-year acquisitions: Use acquisition date rates
```

### Correction Procedure

1. Identify all currency conversion points in GIR data
2. Verify rates against designated source
3. Recalculate using correct rates
4. Quantify impact of rate corrections
5. Determine if differences are material
6. File amendment if necessary
7. Strengthen rate source controls

---

## Error 9: XML Schema Validation Failures

### Error Description

Technical errors preventing successful electronic submission of the GIR due to XML schema non-compliance.

### Common Validation Failures

| Error Code | Description | Common Cause |
|------------|-------------|--------------|
| XSD-001 | Missing required element | Mandatory field left blank |
| XSD-002 | Invalid data type | Text in numeric field |
| XSD-003 | Enumeration violation | Value not in allowed list |
| XSD-004 | Format error | Incorrect date or number format |
| XSD-005 | Length violation | Field exceeds maximum characters |
| XSD-006 | Namespace error | Wrong or missing namespace declaration |
| XSD-007 | Schema version mismatch | Using outdated schema version |
| XSD-008 | Encoding error | Special characters not properly encoded |

### GIR XML Structure Requirements

**OECD January 2025 Schema Elements:**

```xml
<gir:GIR xmlns:gir="urn:oecd:ties:gir:v1">
  <gir:MessageSpec>
    <!-- Message identification metadata -->
  </gir:MessageSpec>
  <gir:GIRBody>
    <gir:GeneralInfo>
      <!-- Section 1: Group and filing information -->
    </gir:GeneralInfo>
    <gir:JurisdictionalData>
      <!-- Section 2: Per-jurisdiction calculations -->
    </gir:JurisdictionalData>
    <gir:TopUpTaxAllocation>
      <!-- Section 3: Top-up tax allocation details -->
    </gir:TopUpTaxAllocation>
  </gir:GIRBody>
</gir:GIR>
```

### Root Causes

1. **Schema version mismatch**: Using old schema when authorities require updated version
2. **Data extraction errors**: Source system exports in wrong format
3. **Manual data entry**: Typos and formatting mistakes
4. **Character encoding**: Special characters (accents, symbols) not UTF-8 encoded
5. **Tool limitations**: GIR preparation software has bugs or limitations

### Prevention Strategy

**Pre-Submission Validation Protocol:**

```
Step 1: Schema Validation
□ Validate against current OECD schema (January 2025)
□ Validate against jurisdiction-specific schema (if different)
□ Use official validation tool if available

Step 2: Data Type Verification
□ All numeric fields contain valid numbers
□ All date fields in YYYY-MM-DD format
□ All country codes per ISO 3166-1 alpha-2
□ All currency codes per ISO 4217

Step 3: Business Rule Validation
□ Total Top-up Tax = Sum of jurisdictional allocations
□ ETR calculations mathematically consistent
□ Ownership percentages sum correctly
□ All referenced entities exist in CE list

Step 4: Character Encoding Check
□ File encoded as UTF-8
□ Special characters properly escaped
□ No invalid XML characters (control characters)

Step 5: Test Submission
□ Submit to test environment (if available)
□ Review any warning messages
□ Correct issues before production submission
```

### Correction Procedure

1. Capture exact error message from validation/submission
2. Identify specific data element causing failure
3. Correct source data or XML generation process
4. Re-validate against schema
5. Resubmit when validation passes
6. Document issue and resolution for future reference

---

## Error 10: DFE Election Timing Mistakes

### Error Description

Failure to make Designated Filing Entity elections within required timeframes, or making elections incorrectly.

### DFE Election Requirements by Jurisdiction

| Jurisdiction | Election Deadline | Method | Duration |
|--------------|-------------------|--------|----------|
| UK | With first GIR | Online notification | Until revoked |
| Germany | Pre-filing | Formal application | Per fiscal year |
| Netherlands | With first return | Electronic filing | Rolling |
| France | Start of fiscal year | Form submission | Annual |
| Ireland | 9 months after FY end | Online notification | Until revoked |
| Singapore | Pre-filing | IRAS portal | Per fiscal year |

### Common Manifestations

| Error Type | Example | Impact |
|------------|---------|--------|
| Missed deadline | Election made after filing date | Local filing obligations triggered |
| Wrong jurisdiction | DFE elected in non-qualifying jurisdiction | Invalid centralised filing |
| Incomplete coverage | Some CEs not covered by DFE election | Multiple filing obligations |
| Revocation failure | Prior DFE election not properly terminated | Conflicting filings |
| Authority mismatch | Different DFEs elected in different jurisdictions | Coordination failures |

### Root Causes

1. **Deadline tracking gaps**: No calendar tracking of jurisdiction-specific deadlines
2. **Coordination failures**: Different teams managing different jurisdiction elections
3. **Legal entity changes**: New CEs not added to DFE coverage
4. **System limitations**: No automated DFE election management
5. **Documentation gaps**: Election evidence not properly retained

### Prevention Strategy

**DFE Election Management Framework:**

```
1. Centralised Election Register
   - Maintain register of all DFE elections
   - Track election date, coverage, duration
   - Monitor expiry/renewal requirements

2. Deadline Calendar
   - Build calendar of all jurisdiction election deadlines
   - Set reminders 90/60/30 days before deadlines
   - Assign responsibility for each jurisdiction

3. Coverage Verification
   - Annually verify all CEs covered by DFE elections
   - Add new CEs to election scope
   - Remove disposed CEs from coverage

4. Documentation Archive
   - Retain copies of all election submissions
   - Maintain authority confirmation receipts
   - File supporting board resolutions

5. Annual Review
   - Review all elections pre-filing season
   - Confirm elections remain valid
   - Make renewals/changes as needed
```

### Correction Procedure

1. Identify election deficiency
2. Determine if late election is permitted
3. If permitted: Make election with explanation of delay
4. If not permitted: File locally in affected jurisdictions
5. Coordinate with DFE to avoid duplicate reporting
6. Implement controls to prevent recurrence

---

## Error 11: Safe Harbour Misapplication

### Error Description

Incorrect application of Transitional CbCR Safe Harbour or QDMTT Safe Harbour, leading to non-compliance or lost simplification opportunities.

### Transitional CbCR Safe Harbour Tests

A jurisdiction qualifies if it meets ANY ONE of three tests:

| Test | Criteria | Data Source |
|------|----------|-------------|
| De Minimis | Revenue <€10M AND Profit Before Tax <€1M | CbCR |
| Simplified ETR | ETR ≥ Transition Rate (15%/16%/17%) | CbCR |
| Routine Profits | Profit Before Tax ≤ SBIE Amount | CbCR + SBIE calc |

### "Once Out, Always Out" Rule

**Critical Rule:**
If a jurisdiction fails to qualify for the Transitional CbCR Safe Harbour in any fiscal year, that jurisdiction is permanently excluded from using the safe harbour for all subsequent fiscal years.

### Common Manifestations

| Error Type | Example | Impact |
|------------|---------|--------|
| Premature application | Applying safe harbour without verifying tests | Future disqualification risk |
| Test selection error | Using wrong test when another would qualify | Unnecessary full calculation |
| CbCR data mismatch | Using different data than filed CbCR | Invalid safe harbour |
| QDMTT misapplication | Claiming QDMTT Safe Harbour for non-qualified regime | Top-up Tax underpayment |
| Transition rate error | Using 15% instead of 16%/17% for later years | Incorrect test result |

### Root Causes

1. **Test complexity**: Not understanding the three alternative tests
2. **Data inconsistency**: CbCR data differs from GloBE calculations
3. **Transition rate confusion**: Not tracking rate increases by fiscal year
4. **"Once out" unawareness**: Not understanding permanent disqualification rule
5. **QDMTT assessment gaps**: Not verifying QDMTT regime qualification

### Prevention Strategy

**Safe Harbour Decision Framework:**

```
For each jurisdiction:

Step 1: Verify eligibility period
□ Fiscal year ends on or before 30 June 2028?
□ Jurisdiction not previously disqualified (once out, always out)?

Step 2: Gather CbCR data
□ Revenue for jurisdiction
□ Profit Before Tax for jurisdiction
□ Income tax paid/accrued

Step 3: Apply tests (in order of simplicity)

Test A - De Minimis:
□ Revenue < €10,000,000?
□ Profit Before Tax < €1,000,000?
□ If BOTH yes → Safe Harbour applies

Test B - Simplified ETR:
□ Calculate: Income Tax Accrued ÷ Profit Before Tax
□ Compare to Transition Rate for fiscal year
□ If ETR ≥ Transition Rate → Safe Harbour applies

Test C - Routine Profits:
□ Calculate SBIE for jurisdiction
□ Compare Profit Before Tax to SBIE
□ If PBT ≤ SBIE → Safe Harbour applies

Step 4: Document decision
□ Record which test applied
□ Retain supporting calculations
□ Note any close calls for monitoring
```

### Correction Procedure

1. Review safe harbour application for all jurisdictions
2. Verify CbCR data matches filed returns
3. Confirm test calculations are correct
4. If safe harbour incorrectly claimed:
   - Perform full GloBE calculation
   - File amended GIR with full jurisdictional data
   - Assess "once out, always out" implications
5. Document correct safe harbour positions

---

## Error 12: Jurisdictional Filing Deadline Misses

### Error Description

Failure to meet GIR filing deadlines, resulting in late filing penalties.

### Standard Filing Deadlines

**OECD Standard:**
- Regular filing: 15 months after fiscal year end
- First year filing: 18 months after fiscal year end
- First filings due: 30 June 2026 (for December 2024 FY end)

**Jurisdiction-Specific Variations:**

| Jurisdiction | Standard Deadline | First Year Extension | Local Variations |
|--------------|-------------------|---------------------|------------------|
| UK | 15 months | 18 months | Aligned with OECD |
| Germany | 15 months | 18 months | Local return may differ |
| Netherlands | 15 months | 18 months | Aligned with OECD |
| France | 15 months | 18 months | Aligned with OECD |
| Ireland | 15 months | 18 months | Aligned with OECD |
| Singapore | 15 months | 18 months | Local variations possible |
| Australia | 15 months | 18 months | Local CGDMTR deadlines |

### Common Manifestations

| Error Type | Example | Impact |
|------------|---------|--------|
| Deadline miscalculation | Counting from wrong date | Late filing penalty |
| Extension failure | Not applying for available extension | Unnecessary late filing |
| Notification miss | Registration/notification deadline missed | Compliance gap |
| DFE reliance error | Assuming DFE filed when they didn't | Multiple late filings |
| Calendar error | Wrong fiscal year end used | Cascading deadline errors |

### Root Causes

1. **Fiscal year complexity**: Non-calendar year ends create confusion
2. **First year uncertainty**: Unclear when 18-month extension applies
3. **Multi-jurisdiction coordination**: Different deadlines in different countries
4. **DFE communication gaps**: DFE not confirming filing to CEs
5. **Calendar management failures**: No systematic deadline tracking

### Prevention Strategy

**Filing Deadline Management:**

```
1. Build Comprehensive Deadline Calendar

   For each jurisdiction where group has CEs:
   - GIR filing deadline (15/18 months)
   - Local Top-up Tax return deadline
   - DFE notification deadline
   - Registration deadline
   - Payment deadline

2. Set Milestone Reminders

   T-6 months: Data collection begins
   T-3 months: Draft GIR review
   T-1 month: Final GIR approval
   T-2 weeks: Submission preparation
   T-1 week: Submission and verification

3. Assign Clear Responsibilities

   - Deadline tracking: [Named individual]
   - Submission execution: [Named individual]
   - Confirmation verification: [Named individual]

4. Maintain Evidence File

   - Submission confirmation receipts
   - Authority acknowledgment records
   - Timeline documentation
```

### Correction Procedure

1. Identify missed deadline and days overdue
2. Prepare and file GIR immediately
3. Calculate potential penalty exposure
4. Prepare reasonable excuse submission (if available)
5. Apply for penalty relief under transitional provisions
6. Pay any penalties assessed
7. Implement deadline management controls

---

## Error 13: Amendment Procedure Non-Compliance

### Error Description

Failure to follow correct procedures when amending a previously filed GIR, potentially creating additional penalties or compliance issues.

### Amendment Requirements

**OECD Standard:**
- Amended return indicator must be set to "true"
- Full GIR must be resubmitted (not just changed data)
- Original and amended returns must be retained

**UK HMRC Requirements:**
- Amendment within 12 months of original filing date
- Supporting documentation explaining changes
- Interest on any underpaid tax

### Common Manifestations

| Error Type | Example | Impact |
|------------|---------|--------|
| Informal correction | Verbal/email correction without formal filing | Not recognised by authority |
| Partial submission | Only changed sections submitted | Invalid amendment |
| Missing indicator | Amended return flag not set | System rejection |
| Time limit breach | Amendment after deadline | May require discovery assessment |
| Documentation gaps | No explanation provided | Authority queries |

### Root Causes

1. **Procedure unfamiliarity**: Not understanding amendment requirements
2. **System limitations**: Software doesn't support amendment filings
3. **Communication failures**: Changes made but not formally filed
4. **Deadline unawareness**: Not knowing amendment time limits
5. **Documentation neglect**: Changes made without supporting records

### Prevention Strategy

**Amendment Control Framework:**

```
When error identified:

1. Assess Materiality
   □ Quantify impact on Top-up Tax
   □ Apply materiality thresholds
   □ Determine if amendment required

2. Check Time Limits
   □ Verify amendment deadline for jurisdiction
   □ Confirm within taxpayer-initiated window
   □ If outside window, assess options

3. Prepare Amended Filing
   □ Generate complete replacement GIR
   □ Set amended return indicator = true
   □ Document all changes from original
   □ Prepare reconciliation schedule

4. Submit with Documentation
   □ File through official channel
   □ Include covering letter
   □ Attach supporting calculations
   □ Retain confirmation receipt

5. Post-Filing Actions
   □ Pay additional tax with interest
   □ Notify affected jurisdictions
   □ Update internal records
   □ Brief stakeholders
```

### Correction Procedure

1. Determine if amendment was properly filed
2. If not: Prepare and submit formal amendment immediately
3. If outside time limit: Seek authority guidance
4. Document the original error and amendment
5. Calculate and pay interest on any underpayment
6. Implement amendment controls for future

---

## Error 14: Documentation Deficiencies

### Error Description

Insufficient documentation to support GIR positions, creating audit risk and potential penalties.

### Documentation Requirements

**OECD GIR Commentary:**
The GIR data should be supported by documentation sufficient to demonstrate the accuracy of reported amounts and the basis for positions taken.

**Key Documentation Categories:**

| Category | Examples | Retention Period |
|----------|----------|------------------|
| Entity information | CE list, ownership charts, exclusion evidence | 10 years |
| Financial data | FANIL calculations, adjustment workpapers | 10 years |
| Tax data | Covered tax calculations, allocation methodology | 10 years |
| Election records | Election forms, board resolutions, expiry tracking | Life of election + 6 years |
| Safe harbour support | CbCR reconciliation, test calculations | 10 years |
| Process documentation | Procedures, controls, review evidence | Current + 3 years |

### Common Manifestations

| Error Type | Example | Impact |
|------------|---------|--------|
| Missing workpapers | No calculation support for ETR | Cannot defend positions |
| Source data gaps | Original data overwritten | Cannot reproduce calculations |
| Election evidence lost | No record of elections made | Authority challenge risk |
| Approval gaps | No sign-off evidence | Governance weakness |
| Version control failure | Cannot identify which version filed | Reconciliation impossible |

### Root Causes

1. **No documentation standard**: Requirements not defined
2. **System limitations**: No document management system
3. **Retention gaps**: Documents purged prematurely
4. **Ownership unclear**: No designated documentation owner
5. **Process informality**: Calculations done but not documented

### Prevention Strategy

**GIR Documentation Standards:**

```
1. Establish Documentation Requirements

   For each GIR data element, specify:
   - Source system/document
   - Calculation methodology
   - Approval requirements
   - Retention period

2. Implement Audit File Structure

   GIR Audit File/
   ├── 1_Entity_Information/
   │   ├── CE_Register.xlsx
   │   ├── Ownership_Charts.pdf
   │   └── Exclusion_Analysis.docx
   ├── 2_Jurisdictional_Calculations/
   │   ├── [Jurisdiction]_GloBE_Income.xlsx
   │   ├── [Jurisdiction]_Covered_Taxes.xlsx
   │   └── [Jurisdiction]_ETR_Calc.xlsx
   ├── 3_TopUp_Tax_Allocation/
   │   ├── IIR_Allocation.xlsx
   │   └── UTPR_Allocation.xlsx
   ├── 4_Elections/
   │   ├── Election_Register.xlsx
   │   └── [Election]_Evidence.pdf
   ├── 5_Safe_Harbours/
   │   ├── CbCR_Reconciliation.xlsx
   │   └── Safe_Harbour_Analysis.xlsx
   └── 6_Filing_Records/
       ├── GIR_XML_Filed.xml
       ├── Submission_Confirmation.pdf
       └── Amendment_Records/

3. Implement Version Control

   - Date-stamp all documents
   - Maintain version history
   - Lock filed versions
   - Archive superseded versions

4. Require Sign-Off Evidence

   - Preparer signature and date
   - Reviewer signature and date
   - Approver signature and date
```

### Correction Procedure

1. Assess current documentation state
2. Identify gaps against requirements
3. Reconstruct documentation where possible
4. Document that reconstruction occurred (with limitations)
5. Implement documentation standards for future periods
6. Consider voluntary disclosure if positions cannot be supported

---

## Error 15: Coordination Failures with Tax Calculations

### Error Description

Disconnect between GIR reporting and underlying Top-up Tax calculations, leading to inconsistencies that trigger authority scrutiny.

### Coordination Requirements

**GIR Must Align With:**

| Element | Coordination Point |
|---------|-------------------|
| Pillar Two tax provision | GIR Top-up Tax = provision for same jurisdiction |
| Local Top-up Tax returns | GIR data = local return data |
| QDMTT returns | QDMTT reported = QDMTT offset claimed |
| CbCR (if safe harbour used) | CbCR data = safe harbour test inputs |
| Financial statements | GloBE Income derived from audited FANIL |

### Common Manifestations

| Error Type | Example | Impact |
|------------|---------|--------|
| Provision mismatch | GIR shows €1M, provision shows €1.2M | Unexplained variance |
| Local return difference | DFE GIR differs from local CE filing | Authority queries |
| QDMTT inconsistency | QDMTT offset claimed doesn't match local return | Incorrect IIR/UTPR |
| CbCR variance | Safe harbour CbCR data differs from filed CbCR | Invalid safe harbour |
| Timing difference | GIR and provision use different FY data | Reconciliation needed |

### Root Causes

1. **Parallel processes**: GIR and tax provision prepared separately
2. **System disconnects**: Different systems for different outputs
3. **Timing mismatches**: Provision finalised before GIR adjustments
4. **Ownership fragmentation**: Different teams responsible for different outputs
5. **Version control failures**: Using different versions of source data

### Prevention Strategy

**Integrated Pillar Two Process:**

```
Single Source of Truth Model:

1. Establish Master Data Set
   - One authoritative GloBE calculation
   - Feeds all downstream outputs
   - Version-controlled and locked

2. Derive All Outputs from Master

   Master GloBE
   Calculation
        │
        ├──► GIR Section 2 (jurisdictional data)
        │
        ├──► GIR Section 3 (Top-up Tax allocation)
        │
        ├──► Tax provision workpapers
        │
        ├──► Local Top-up Tax returns
        │
        └──► Financial statement disclosures

3. Implement Reconciliation Controls

   For each output:
   - Trace to master calculation
   - Document any differences with explanation
   - Obtain sign-off on reconciliation

4. Coordinate Timing

   Phase 1: Complete master GloBE calculation
   Phase 2: Prepare tax provision (from master)
   Phase 3: Prepare GIR (from master)
   Phase 4: Reconcile all outputs
   Phase 5: File GIR
   Phase 6: File local returns (from master)

5. Assign Integration Responsibility

   - Designate Pillar Two process owner
   - Responsibility for end-to-end consistency
   - Authority to resolve conflicts
```

### Correction Procedure

1. Identify all inconsistencies between outputs
2. Determine which output is correct
3. Trace back to master calculation
4. Correct erroneous outputs
5. File amendments where required
6. Implement integrated process for future periods

---

## Summary: Error Prevention Matrix

| Error | Frequency | Impact | Prevention Priority |
|-------|-----------|--------|---------------------|
| 1. CE Identification | High | High | Critical |
| 2. Ownership Percentage | High | High | Critical |
| 3. Excluded Entity | Medium | High | High |
| 4. GloBE Income | High | High | Critical |
| 5. Covered Taxes | High | High | Critical |
| 6. SBIE Data | Medium | Medium | Medium |
| 7. Intercompany | Medium | High | High |
| 8. Currency | Medium | Medium | Medium |
| 9. XML Schema | Low | Medium | Medium |
| 10. DFE Election | Medium | High | High |
| 11. Safe Harbour | Medium | High | High |
| 12. Filing Deadline | Low | High | High |
| 13. Amendment | Low | Medium | Medium |
| 14. Documentation | High | Medium | High |
| 15. Coordination | Medium | High | High |

---

## Practical Deliverable: GIR Quality Assurance Checklist

### Pre-Filing Quality Assurance Checklist

**Section A: Entity Completeness**

| Check | Verified | Reviewer |
|-------|----------|----------|
| All CEs reconciled to consolidation | □ | ___ |
| All CEs reconciled to legal entity register | □ | ___ |
| PEs identified and included | □ | ___ |
| Ownership percentages verified | □ | ___ |
| Excluded entities properly classified | □ | ___ |
| New acquisitions included | □ | ___ |
| Disposals removed | □ | ___ |

**Section B: Calculations**

| Check | Verified | Reviewer |
|-------|----------|----------|
| GloBE Income reconciled to FANIL | □ | ___ |
| All required adjustments applied | □ | ___ |
| Elections consistently applied | □ | ___ |
| Covered Taxes reconciled to tax provision | □ | ___ |
| SBIE calculated per transition rates | □ | ___ |
| Intercompany transactions eliminated | □ | ___ |
| Currency rates from approved source | □ | ___ |

**Section C: Safe Harbours**

| Check | Verified | Reviewer |
|-------|----------|----------|
| CbCR data matches filed return | □ | ___ |
| Correct transition rate applied | □ | ___ |
| "Once out" status verified | □ | ___ |
| QDMTT qualification confirmed | □ | ___ |
| Safe harbour documentation complete | □ | ___ |

**Section D: Technical Filing**

| Check | Verified | Reviewer |
|-------|----------|----------|
| XML validated against current schema | □ | ___ |
| All required fields populated | □ | ___ |
| Data types correct | □ | ___ |
| DFE elections in place | □ | ___ |
| Filing deadline confirmed | □ | ___ |

**Section E: Documentation**

| Check | Verified | Reviewer |
|-------|----------|----------|
| Calculation workpapers complete | □ | ___ |
| Source documents retained | □ | ___ |
| Election evidence filed | □ | ___ |
| Review sign-offs obtained | □ | ___ |
| Audit file structured | □ | ___ |

**Section F: Coordination**

| Check | Verified | Reviewer |
|-------|----------|----------|
| GIR reconciled to tax provision | □ | ___ |
| GIR reconciled to local returns | □ | ___ |
| CbCR alignment confirmed | □ | ___ |
| All outputs from single master | □ | ___ |

**Final Sign-Off:**

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Preparer | ___ | ___ | ___ |
| Reviewer | ___ | ___ | ___ |
| Approver | ___ | ___ | ___ |

---

## Key Takeaways

1. **Entity identification** and **GloBE Income calculations** are the highest-frequency, highest-impact error categories

2. The **"once out, always out"** rule for safe harbours creates significant risk from misapplication

3. **Documentation deficiencies** are pervasive and create long-term audit exposure

4. **Coordination failures** between GIR and other Pillar Two outputs generate authority scrutiny

5. **Transitional penalty relief** provides protection for good-faith errors, but requires demonstrable "reasonable measures"

6. **Process integration** - using a single master calculation for all outputs - is the most effective prevention strategy

7. **Pre-filing quality assurance** using structured checklists significantly reduces error rates

---

## Further Reading and Resources

- [IBFD: Tax Authorities Warn of Common Pillar Two Errors](https://www.ibfd.org/news/pillar-two-reporting-obligations-tax-authorities-warn-common-errors)
- [Wolters Kluwer: BEPS Practical Compliance Guidelines](https://www.wolterskluwer.com/en-au/expert-insights/beps-practical-guidance)
- [OECD: GloBE Information Return (January 2025)](https://www.oecd.org/en/publications/tax-challenges-arising-from-the-digitalisation-of-the-economy-globe-information-return-january-2025_a05ec99a-en.html)
- [oecdpillars.com: Identify Constituent and Excluded Entities](https://oecdpillars.com/pillar-tab/identify-constituent-and-excluded-entities/)
- [oecdpillars.com: Substance-Based Income Exclusion](https://oecdpillars.com/pillar-tab/substance-based-income-exclusion/)
- [KPMG: SBIE Mobile Employee Considerations](https://kpmg.com/kpmg-us/content/dam/kpmg/pdf/2024/beps-and-pillar-2-are-here-where-in-the-globe-are-your-employees-072224.pdf)

---

*End of Section 11.1*
