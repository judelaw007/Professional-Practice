# Section 3: Understanding the GIR Structure

## 3.3 GIR Section 2: Jurisdictional Safe Harbours and Exclusions

**Estimated Reading Time:** 25 minutes
**Pages:** 8-10

---

## Learning Objectives for This Section

By the end of this section, you will be able to:

- Evaluate whether each jurisdiction qualifies for the Transitional CbCR Safe Harbour
- Apply the three qualifying tests (De Minimis, Simplified ETR, Routine Profits)
- Understand the QDMTT Safe Harbour and its permanent application
- Apply the Transitional UTPR Safe Harbour where eligible
- Complete GIR Section 2 data elements correctly
- Avoid the "once out, always out" trap for transitional safe harbours
- Document safe harbour elections properly

---

## Overview of GIR Section 2

GIR Section 2 (Jurisdictional Safe Harbours and Exclusions) determines **where simplified reporting applies**. If a jurisdiction qualifies for a safe harbour, you can significantly reduce or eliminate Section 3 reporting requirements for that jurisdiction.

**Data Points:** Section 2 contains approximately **40 data points**, though the actual number varies based on:
- Number of jurisdictions where safe harbours are elected
- Types of safe harbours applied
- Whether exclusions apply

**Strategic Importance:** Proper application of safe harbours can dramatically reduce compliance burden and data collection requirements.

---

## Section 2 Structure

| Sub-Section | Content | Purpose |
|-------------|---------|---------|
| **2.1** | Jurisdictional Characteristics | Identify each jurisdiction's profile |
| **2.2** | Safe Harbour Elections | Document which safe harbours apply |
| **2.3** | Exclusion Documentation | Record jurisdictions excluded from full computation |

---

## 3.3.1 Safe Harbour Elections

### Available Safe Harbours

The GloBE framework provides three categories of safe harbours:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                        SAFE HARBOUR CATEGORIES                              │
└─────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────┐
│  TRANSITIONAL SAFE HARBOURS (Temporary)                                     │
│  ───────────────────────────────────────                                    │
│                                                                              │
│  1. Transitional CbCR Safe Harbour                                          │
│     • Three qualifying tests                                                 │
│     • Fiscal years beginning on or before Dec 31, 2026                      │
│     • "Once out, always out" rule applies                                   │
│                                                                              │
│  2. Transitional UTPR Safe Harbour                                          │
│     • UPE jurisdiction must have 20%+ nominal tax rate                      │
│     • Fiscal years beginning on or before Dec 31, 2025                      │
│     • Applies only to UPE jurisdiction                                      │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────┐
│  PERMANENT SAFE HARBOURS                                                    │
│  ───────────────────────────                                                │
│                                                                              │
│  3. QDMTT Safe Harbour                                                      │
│     • Jurisdiction must have Qualified QDMTT                                │
│     • Must meet Consistency, Accounting, and Administration standards       │
│     • Peer review process determines eligibility                            │
│     • Reduces IIR/UTPR top-up tax to nil                                    │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

### Transitional CbCR Safe Harbour

The Transitional CbCR Safe Harbour uses data from your Country-by-Country Report (CbCR) to provide compliance relief. If a jurisdiction meets **any one** of three tests, top-up tax is deemed to be **nil** for that jurisdiction.

#### The Three Qualifying Tests

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    TRANSITIONAL CbCR SAFE HARBOUR TESTS                     │
└─────────────────────────────────────────────────────────────────────────────┘

                    ┌──────────────────────────────────┐
                    │   For Each Tested Jurisdiction   │
                    └──────────────────┬───────────────┘
                                       │
              ┌────────────────────────┼────────────────────────┐
              │                        │                        │
              ▼                        ▼                        ▼
   ┌──────────────────┐     ┌──────────────────┐     ┌──────────────────┐
   │   TEST 1:        │     │   TEST 2:        │     │   TEST 3:        │
   │   DE MINIMIS     │     │   SIMPLIFIED ETR │     │   ROUTINE PROFITS│
   │                  │     │                  │     │                  │
   │ Revenue < €10M   │     │ Simplified ETR   │     │ Profit ≤ SBIE    │
   │      AND         │     │ ≥ Transition     │     │                  │
   │ Profit < €1M     │     │   Rate           │     │                  │
   └────────┬─────────┘     └────────┬─────────┘     └────────┬─────────┘
            │                        │                        │
            │         Pass ANY ONE test                       │
            └────────────────────────┼────────────────────────┘
                                     │
                                     ▼
                    ┌──────────────────────────────────┐
                    │   TOP-UP TAX = NIL               │
                    │   No Section 3 required for      │
                    │   this jurisdiction              │
                    └──────────────────────────────────┘
```

#### Test 1: De Minimis Test

**Requirements:**

| Metric | Threshold | Source |
|--------|-----------|--------|
| Total Revenue | Less than €10 million | CbCR Table 1 |
| Profit (Loss) Before Income Tax | Less than €1 million | CbCR Table 1 |

**Both conditions must be met.**

**Example:**

```
JURISDICTION: Luxembourg (Holding Company)
─────────────────────────────────────────────────────────────────────────────

CbCR Data:
  Revenue:                    €2,500,000
  Profit Before Income Tax:   €750,000

De Minimis Test:
  Revenue < €10M?             YES (€2.5M < €10M)
  Profit < €1M?               YES (€750K < €1M)

Result: PASS - De Minimis Test met
        Top-up tax deemed nil for Luxembourg
```

---

#### Test 2: Simplified ETR Test

**Requirements:**

| Fiscal Year Beginning | Transition Rate (Threshold) |
|----------------------|----------------------------|
| 2023 or 2024 | 15% |
| 2025 | 16% |
| 2026 | 17% |

**Simplified ETR Calculation:**

```
                    Simplified Covered Taxes
Simplified ETR = ─────────────────────────────────
                 Profit Before Income Tax (CbCR)
```

**Simplified Covered Taxes =** Income tax expense from financial statements
- MINUS taxes that are not Covered Taxes
- MINUS taxes relating to uncertain tax positions

**Note:** No GloBE adjustments are required for this calculation. This is simpler than the full GloBE ETR calculation.

**Example:**

```
JURISDICTION: Germany
FISCAL YEAR: Beginning January 1, 2024
─────────────────────────────────────────────────────────────────────────────

Data:
  Profit Before Income Tax (CbCR):     €50,000,000
  Income Tax Expense (Fin. Statements): €9,000,000
  Non-Covered Taxes:                   €500,000
  Uncertain Tax Position Reserve:       €250,000

Simplified Covered Taxes:
  €9,000,000 - €500,000 - €250,000 = €8,250,000

Simplified ETR:
  €8,250,000 ÷ €50,000,000 = 16.5%

Transition Rate (2024): 15%

Result: PASS - Simplified ETR (16.5%) ≥ Transition Rate (15%)
        Top-up tax deemed nil for Germany
```

---

#### Test 3: Routine Profits Test

**Requirements:**

The jurisdiction's Profit (Loss) Before Income Tax (from CbCR) must be **equal to or less than** the Substance-Based Income Exclusion (SBIE) amount for that jurisdiction.

**SBIE Calculation Required:**

Unlike the other tests, the Routine Profits Test requires a full SBIE calculation using GloBE rules:

| Fiscal Year | Payroll Carve-Out Rate | Tangible Asset Carve-Out Rate |
|------------|------------------------|-------------------------------|
| 2024 | 9.8% | 7.8% |
| 2025 | 9.6% | 7.6% |
| 2026 | 9.4% | 7.4% |

**SBIE = (Eligible Payroll × Payroll Rate) + (Eligible Tangible Assets × Asset Rate)**

**Example:**

```
JURISDICTION: Singapore (Manufacturing)
FISCAL YEAR: 2024
─────────────────────────────────────────────────────────────────────────────

CbCR Data:
  Profit Before Income Tax:            €8,000,000

SBIE Calculation:
  Eligible Payroll Costs:              €30,000,000
  Eligible Tangible Assets:            €100,000,000

  Payroll Carve-Out (9.8%):            €30,000,000 × 9.8% = €2,940,000
  Asset Carve-Out (7.8%):              €100,000,000 × 7.8% = €7,800,000

  Total SBIE:                          €2,940,000 + €7,800,000 = €10,740,000

Routine Profits Test:
  Profit (€8,000,000) ≤ SBIE (€10,740,000)?  YES

Result: PASS - Routine Profits Test met
        Top-up tax deemed nil for Singapore
```

---

#### Transition Period for CbCR Safe Harbour

| Fiscal Year Start | Fiscal Year End | CbCR Safe Harbour Available? |
|-------------------|-----------------|------------------------------|
| Jan 1, 2024 | Dec 31, 2024 | YES |
| Jan 1, 2025 | Dec 31, 2025 | YES |
| Jan 1, 2026 | Dec 31, 2026 | YES |
| Jan 1, 2027 | Dec 31, 2027 | Only if ends before July 1, 2028 |
| Jan 1, 2027 | June 30, 2028 | YES (ends before July 1, 2028) |
| Jan 1, 2027 | July 1, 2028+ | NO |

**Key Rule:** The safe harbour applies to fiscal years beginning on or before December 31, 2026 but **not including** a fiscal year that ends after June 30, 2028.

---

#### Critical: "Once Out, Always Out" Rule

**This is the most important rule for the Transitional CbCR Safe Harbour.**

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                      "ONCE OUT, ALWAYS OUT" RULE                            │
└─────────────────────────────────────────────────────────────────────────────┘

If in ANY fiscal year:
─────────────────────

  • You FAIL to meet any of the three tests for a jurisdiction
                        OR
  • You CHOOSE not to apply the safe harbour (even if eligible)

                              ▼

  That jurisdiction is PERMANENTLY EXCLUDED from the Transitional CbCR
  Safe Harbour for all subsequent fiscal years within the transition period.

┌─────────────────────────────────────────────────────────────────────────────┐
│  EXCEPTION: First year of presence                                          │
│                                                                              │
│  If the current fiscal year is the FIRST fiscal year within the transition  │
│  period that the MNE Group has a Constituent Entity in the jurisdiction,    │
│  the safe harbour can still be elected.                                     │
└─────────────────────────────────────────────────────────────────────────────┘
```

**Practical Implications:**

| Scenario | Year 1 (2024) | Year 2 (2025) | Year 3 (2026) | Safe Harbour in 2025/2026? |
|----------|---------------|---------------|---------------|---------------------------|
| **A** | Elected | - | - | YES - continue to elect |
| **B** | Did not elect (chose not to) | - | - | NO - "once out, always out" |
| **C** | Failed tests | - | - | NO - "once out, always out" |
| **D** | Not in jurisdiction | Entered jurisdiction | - | YES - first year exception |

**Warning:** Even if you are eligible for the safe harbour, failing to elect it in the first year means you cannot use it in subsequent years.

---

### Transitional UTPR Safe Harbour

The Transitional UTPR Safe Harbour provides relief from UTPR top-up tax in the **UPE jurisdiction only** during the initial implementation period.

#### Requirements

| Requirement | Detail |
|-------------|--------|
| **UPE Jurisdiction** | Must have a nominal corporate income tax rate of **at least 20%** |
| **Combined Rate** | May include sub-national taxes if combined rate ≥ 20% |
| **Transition Period** | Fiscal years beginning on or before December 31, 2025 and ending before December 31, 2026 |

#### Eligible UPE Jurisdictions (Examples)

| Jurisdiction | Nominal Corporate Tax Rate | UTPR Safe Harbour Eligible? |
|-------------|---------------------------|----------------------------|
| United Kingdom | 25% | YES |
| United States | 21% (federal) + state | YES (combined ≥ 20%) |
| Germany | ~30% (combined) | YES |
| France | 25% | YES |
| Ireland | 12.5% | NO |
| Singapore | 17% | NO |
| Switzerland | Varies (8-24%) | Depends on canton |

#### Effect of the Safe Harbour

When the Transitional UTPR Safe Harbour applies:
- UTPR top-up tax in respect of the **UPE jurisdiction only** is reduced to **nil**
- Other jurisdictions' UTPR liability remains unaffected
- Full GloBE calculations may still be required for other purposes

**Example:**

```
SCENARIO: UK-headquartered MNE with low-taxed subsidiary in Ireland
─────────────────────────────────────────────────────────────────────────────

UPE: GlobalCo plc (UK)
UK Corporate Tax Rate: 25%

Without UTPR Safe Harbour:
  Ireland subsidiary ETR: 10%
  Top-up tax (15% - 10%): 5%
  If no IIR/QDMTT collection: UTPR applies
  UTPR may be allocated to UK entities

With UTPR Safe Harbour (2024-2025):
  UK jurisdiction UTPR liability: NIL
  Reason: UK nominal rate (25%) ≥ 20% threshold

Result: UTPR Safe Harbour applies for UK in 2024 and 2025 fiscal years
```

---

### QDMTT Safe Harbour (Permanent)

The QDMTT Safe Harbour is a **permanent** safe harbour that applies when a jurisdiction has a **Qualified Domestic Minimum Top-up Tax (QDMTT)**.

#### How It Works

When the QDMTT Safe Harbour applies:
- Top-up tax under IIR or UTPR is deemed to be **nil** for that jurisdiction
- Only the QDMTT calculation is required
- Avoids duplication of calculations

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                     QDMTT SAFE HARBOUR EFFECT                               │
└─────────────────────────────────────────────────────────────────────────────┘

Without QDMTT Safe Harbour:          With QDMTT Safe Harbour:
──────────────────────────           ────────────────────────

┌──────────────────────┐             ┌──────────────────────┐
│ Calculate QDMTT      │             │ Calculate QDMTT      │
│ (if QDMTT applies)   │             │ (if QDMTT applies)   │
└──────────┬───────────┘             └──────────┬───────────┘
           │                                    │
           ▼                                    │
┌──────────────────────┐                        │
│ Calculate IIR        │                        │  NOT REQUIRED
│ (if IIR applies)     │                        │  IIR/UTPR = NIL
└──────────┬───────────┘                        │
           │                                    │
           ▼                                    │
┌──────────────────────┐                        │
│ Calculate UTPR       │                        │
│ (if UTPR applies)    │                        │
└──────────────────────┘                        │
```

#### Three Standards for QDMTT Safe Harbour Status

For a QDMTT to qualify for Safe Harbour status, it must meet three standards verified through OECD peer review:

| Standard | Requirement |
|----------|-------------|
| **1. Consistency Standard** | QDMTT computations must be the same as GloBE Rule computations (with permitted exceptions) |
| **2. Local Accounting Standard Restrictions** | Local accounting standard can only be used if all CEs in the jurisdiction use it and accounts are externally audited |
| **3. Administration Standard** | Jurisdiction must participate in ongoing OECD monitoring process |

#### Jurisdictions with QDMTT Safe Harbour Status

The OECD maintains a list of jurisdictions whose QDMTTs have achieved Safe Harbour status through peer review. Check the OECD Pillar Two portal for the current list.

**Common QDMTT Jurisdictions (Implementation Status):**

| Jurisdiction | QDMTT Effective | Safe Harbour Status |
|-------------|-----------------|---------------------|
| United Kingdom | 2024 | Subject to peer review |
| Germany | 2024 | Subject to peer review |
| South Korea | 2024 | Subject to peer review |
| Japan | 2026 | TBD |
| Australia | 2024 | Subject to peer review |
| Ireland | 2024 | Subject to peer review |

**Note:** Check current OECD guidance for confirmed Safe Harbour status as peer reviews are ongoing.

---

## 3.3.2 Jurisdictional Exclusions

When a safe harbour applies, the jurisdiction is **excluded** from full Section 3 computation. This exclusion must be documented in GIR Section 2.

### Types of Exclusions

| Exclusion Type | Basis | Effect on Section 3 |
|----------------|-------|---------------------|
| **Transitional CbCR Safe Harbour** | Passed one of three tests | No Section 3 required |
| **QDMTT Safe Harbour** | Qualified QDMTT with Safe Harbour status | Reduced Section 3 (QDMTT only) |
| **Transitional UTPR Safe Harbour** | UPE jurisdiction ≥ 20% rate | UTPR portion nil (other calculations may apply) |
| **De Minimis Exclusion** (Art. 5.5) | Revenue < €10M and Profit < €1M | May exclude from full computation |
| **Initial Phase Relief** | First year of international activity | Simplified requirements |

### Documentation Requirements

For each excluded jurisdiction, document:

| Element | What to Record |
|---------|----------------|
| **Jurisdiction** | 2-character country code |
| **Safe Harbour Type** | Which safe harbour applies |
| **Test Met** (for CbCR Safe Harbour) | De Minimis, Simplified ETR, or Routine Profits |
| **Fiscal Year** | Reporting period |
| **Election Confirmation** | Confirmation that safe harbour is elected |

---

## Section 2 Data Elements

### Section 2.1: Jurisdictional Characteristics

For each jurisdiction where the MNE has Constituent Entities:

| Field | Description | Format |
|-------|-------------|--------|
| **Jurisdiction** | Country code | ISO 3166-1 Alpha-2 |
| **Subgroup Type** | UPE, POPE, JV, etc. | Selection |
| **QDMTT in Force** | Whether jurisdiction has QDMTT | Yes/No |
| **IIR in Force** | Whether jurisdiction has IIR | Yes/No |
| **UTPR in Force** | Whether jurisdiction has UTPR | Yes/No |

### Section 2.2: Safe Harbour Elections

| Field | Description | Options |
|-------|-------------|---------|
| **Safe Harbour Election** | Which safe harbour applies | (a) Transitional CbCR Safe Harbour |
| | | (b) Transitional UTPR Safe Harbour |
| | | (c) QDMTT Safe Harbour |
| | | (d) None |
| **Test Met** (if CbCR) | Which test was passed | De Minimis / Simplified ETR / Routine Profits |
| **Switch-Off Applies** | Whether QDMTT switch-off applies | Yes/No |

### January 2025 Clarifications

The January 2025 OECD guidance provides important clarifications:

| Clarification | Detail |
|--------------|--------|
| **QDMTT Switch-Off** | Do not select QDMTT Safe Harbour option when the switch-off rule applies |
| **Discrepancy Reporting** | Report "Yes" if safe harbour eligibility differs between GIR and domestic law |
| **Incomplete Data** | If CbCR data unavailable, safe harbour cannot be elected |

---

## Safe Harbour Decision Flowchart

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    SAFE HARBOUR DECISION FLOWCHART                          │
└─────────────────────────────────────────────────────────────────────────────┘

For Each Jurisdiction Where MNE Has Constituent Entities:
─────────────────────────────────────────────────────────

                    ┌──────────────────────────────────┐
                    │  Is this the UPE jurisdiction?   │
                    └──────────────────┬───────────────┘
                                       │
                         ┌─────────────┴─────────────┐
                        YES                          NO
                         │                           │
                         ▼                           │
          ┌──────────────────────────────┐           │
          │ Does UPE jurisdiction have   │           │
          │ nominal tax rate ≥ 20%?      │           │
          └──────────────┬───────────────┘           │
                         │                           │
              ┌──────────┴──────────┐                │
             YES                    NO               │
              │                     │                │
              ▼                     │                │
   ┌──────────────────────┐         │                │
   │ Transitional UTPR    │         │                │
   │ Safe Harbour may     │         │                │
   │ apply (2024-2025)    │         │                │
   └──────────────────────┘         │                │
                                    │                │
                    ┌───────────────┴────────────────┘
                    │
                    ▼
          ┌──────────────────────────────┐
          │ Does jurisdiction have       │
          │ Qualified QDMTT with         │
          │ Safe Harbour status?         │
          └──────────────┬───────────────┘
                         │
              ┌──────────┴──────────┐
             YES                    NO
              │                     │
              ▼                     │
   ┌──────────────────────┐         │
   │ QDMTT Safe Harbour   │         │
   │ applies (permanent)  │         │
   │ IIR/UTPR = NIL       │         │
   └──────────────────────┘         │
                                    │
                    ┌───────────────┘
                    │
                    ▼
          ┌──────────────────────────────┐
          │ Is jurisdiction within       │
          │ Transitional CbCR period?    │
          │ (FY starting ≤ Dec 31, 2026) │
          └──────────────┬───────────────┘
                         │
              ┌──────────┴──────────┐
             YES                    NO
              │                     │
              ▼                     ▼
   ┌──────────────────────┐  ┌──────────────────────┐
   │ Has this jurisdiction│  │ Full Section 3       │
   │ been "out" in any    │  │ computation required │
   │ prior year?          │  └──────────────────────┘
   └──────────┬───────────┘
              │
     ┌────────┴────────┐
    YES               NO
     │                 │
     ▼                 ▼
┌──────────────┐  ┌──────────────────────────────┐
│ "Once out,   │  │ Apply Three Tests:           │
│ always out"  │  │ 1. De Minimis                │
│ Full Sec. 3  │  │ 2. Simplified ETR            │
│ required     │  │ 3. Routine Profits           │
└──────────────┘  └──────────────┬───────────────┘
                                 │
                      ┌──────────┴──────────┐
                   Pass ANY               Fail ALL
                      │                     │
                      ▼                     ▼
           ┌──────────────────┐  ┌──────────────────────┐
           │ Transitional CbCR│  │ Full Section 3       │
           │ Safe Harbour     │  │ computation required │
           │ applies          │  │ "Once out, always    │
           │ Top-up tax = NIL │  │ out" for future yrs  │
           └──────────────────┘  └──────────────────────┘
```

---

## Section 2 Completion Checklist

Before proceeding to Section 3, verify the following for **each jurisdiction**:

### Safe Harbour Eligibility Check

- [ ] Identified all jurisdictions where MNE has Constituent Entities
- [ ] Determined if UPE jurisdiction qualifies for Transitional UTPR Safe Harbour (≥ 20% rate)
- [ ] Checked if jurisdiction has QDMTT with Safe Harbour status
- [ ] Verified jurisdiction is within Transitional CbCR period (if applicable)
- [ ] Confirmed no "once out, always out" disqualification for CbCR Safe Harbour

### Transitional CbCR Safe Harbour (If Applicable)

- [ ] CbCR data available and qualified
- [ ] De Minimis Test evaluated (Revenue < €10M AND Profit < €1M)
- [ ] Simplified ETR Test evaluated (ETR ≥ Transition Rate)
- [ ] Routine Profits Test evaluated (Profit ≤ SBIE) if other tests fail
- [ ] At least one test passed for jurisdictions where safe harbour elected
- [ ] Safe harbour election documented

### QDMTT Safe Harbour (If Applicable)

- [ ] Jurisdiction's QDMTT verified as "Qualified"
- [ ] Safe Harbour status confirmed through OECD peer review
- [ ] Switch-off rule checked (not applicable)
- [ ] QDMTT Safe Harbour elected in Section 2

### Documentation

- [ ] All safe harbour elections recorded in Section 2
- [ ] Tests met documented for CbCR Safe Harbour
- [ ] Exclusions properly noted
- [ ] Discrepancies between GIR and domestic law reported (if any)

---

## Common Errors in Section 2

| Error | Consequence | Prevention |
|-------|-------------|------------|
| **Electing CbCR Safe Harbour without qualifying data** | Invalid election, full computation required | Verify CbCR data before election |
| **Failing to elect in first year** | "Once out, always out" - lost benefit | Evaluate and elect from Year 1 |
| **Wrong Transition Rate threshold** | Incorrect Simplified ETR test | Use 15%/16%/17% per fiscal year start |
| **Assuming QDMTT = QDMTT Safe Harbour** | Safe Harbour requires peer review | Check OECD approved list |
| **Ignoring UTPR Safe Harbour** | Unnecessary UTPR calculations | Check UPE jurisdiction tax rate |
| **Inconsistent elections across jurisdictions** | Compliance risk | Document rationale for each election |

---

## Impact on Section 3 Reporting

The elections made in Section 2 directly determine Section 3 requirements:

| Section 2 Election | Section 3 Requirement |
|-------------------|----------------------|
| **Transitional CbCR Safe Harbour** (any test passed) | No Section 3 for this jurisdiction |
| **QDMTT Safe Harbour** | QDMTT computation only; IIR/UTPR = nil |
| **Transitional UTPR Safe Harbour** | UTPR portion = nil; other computations may apply |
| **No safe harbour** | Full Section 3 computation required |

---

## Summary: Safe Harbour Comparison

| Safe Harbour | Type | Period | Key Test | Effect |
|-------------|------|--------|----------|--------|
| **Transitional CbCR** | Transitional | FY ≤ Dec 31, 2026 | De Minimis / ETR / Routine Profits | Top-up tax = nil |
| **Transitional UTPR** | Transitional | FY ≤ Dec 31, 2025 | UPE jurisdiction ≥ 20% rate | UTPR in UPE jurisdiction = nil |
| **QDMTT** | Permanent | Ongoing | Qualified QDMTT + peer review | IIR/UTPR = nil |

---

## Next Steps

You now understand how to evaluate and elect safe harbours in GIR Section 2. The next subsection will cover the detailed GloBE computations required for jurisdictions that do not qualify for safe harbour treatment.

---

## Sources and References

This section incorporates information from:

- [OECD Safe Harbours and Penalty Relief: Global Anti-Base Erosion Rules (Pillar Two)](https://www.oecd.org/content/dam/oecd/en/topics/policy-sub-issues/global-minimum-tax/safe-harbours-and-penalty-relief-global-anti-base-erosion-rules-pillar-two.pdf)
- [oecdpillars.com - Transitional CbCR Safe Harbour](https://oecdpillars.com/pillar-tab/transitional-cbcr-safe-harbour/)
- [oecdpillars.com - QDMTT Safe Harbour](https://oecdpillars.com/pillar-tab/qdmtt-safe-harbour/)
- [oecdpillars.com - A Review of Changes in the OECD's Updated January 2025 GloBE Information Return](https://oecdpillars.com/a-review-of-changes-in-the-oecds-updated-january-2025-globe-information-return/)
- [EY - Pillar Two: what is the importance of the Country-by-Country Safe Harbors?](https://www.ey.com/en_be/insights/tax/pillar-two-what-is-the-importance-of-the-country-by-country-safe-harbors)
- [PwC UK - Pillar 2 safe harbours: how your country-by-country report will be central to compliance](https://www.pwc.co.uk/services/tax/insights/pillar-2-safe-harbours.html)
- [PwC US - Transfer Pricing and the Pillar Two Transitional CbCR Safe Harbor](https://www.pwc.com/us/en/services/tax/library/transfer-pricing-pillar-two-cbcr-safe-harbor-rule.html)
- [RSM - Transitional Pillar Two safe harbor](https://rsmus.com/insights/tax-alerts/2023/transitional-pillar-two-safe-harbor.html)
- [Macfarlanes - Unpacking Pillar Two: a period of transition - the safe harbour explained](https://www.macfarlanes.com/what-we-think/2023/unpacking-pillar-two-a-period-of-transition-safe-harbour-explained/)
- [Forvis Mazars Ireland - Pillar 2 – How to avail of transitional safe harbours and exclusions](https://www.forvismazars.com/ie/en/insights/news-opinions/pillar-2-transitional-safe-harbours-exclusions)
- [HMRC MTT Manual - QDMTT Safe Harbour Overview](https://www.gov.uk/hmrc-internal-manuals/multinational-top-up-tax-and-domestic-top-up-tax/mtt15110)
- [ATO - Transitional CBC reporting safe harbour](https://www.ato.gov.au/businesses-and-organisations/international-tax-for-business/in-detail/multinationals/global-and-domestic-minimum-tax/transitional-cbc-reporting-safe-harbour)
- [Grant Thornton - OECD offers new UTPR safe harbor, favorable credit rules](https://www.grantthornton.com/insights/newsletters/tax/2023/hot-topics/aug-01/oecd-offers-new-utpr-safe-harbor-favorable-credit-rules)

---

*End of Section 3.3*
