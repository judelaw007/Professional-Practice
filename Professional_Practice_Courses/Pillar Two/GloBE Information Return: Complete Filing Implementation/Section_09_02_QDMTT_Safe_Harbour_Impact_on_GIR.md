# Section 9.2: QDMTT Safe Harbour Impact on GIR

## Learning Objectives

By the end of this section, you will be able to:

- Explain the purpose and operation of the QDMTT Safe Harbour
- Identify the three qualifying standards for QDMTT Safe Harbour eligibility
- Understand how the QDMTT Safe Harbour affects IIR and UTPR calculations
- Apply reduced GIR reporting requirements where the safe harbour applies
- Document QDMTT Safe Harbour positions for audit defence

---

## 9.2.1 Introduction to the QDMTT Safe Harbour

### What is a QDMTT?

A **Qualified Domestic Minimum Top-up Tax (QDMTT)** is a domestic minimum tax implemented by a jurisdiction that:

1. Calculates the Top-up Tax for Constituent Entities located in that jurisdiction
2. Uses GloBE-equivalent computational rules
3. Collects the Top-up Tax domestically before IIR or UTPR can apply

**Key Principle:** The QDMTT allows a jurisdiction to preserve its primary taxing right over profits derived from activities in its territory.

### QDMTT in the GloBE Rule Order

The GloBE Rules operate in a specific sequence:

```
GLOBE RULE ORDER
================

Step 1: QDMTT (Domestic jurisdiction collects first)
         │
         ▼
Step 2: IIR (Parent jurisdiction charges residual)
         │
         ▼
Step 3: UTPR (Backstop rule for remaining amounts)

Where QDMTT equals the full Top-up Tax amount,
IIR and UTPR have nothing further to collect.
```

### Purpose of the QDMTT Safe Harbour

The QDMTT Safe Harbour operates by **deeming the Top-up Tax to be zero** for GloBE IIR/UTPR purposes where a qualifying QDMTT has already been applied. This eliminates the need for MNE groups to perform duplicate calculations.

**Without QDMTT Safe Harbour:**
- MNE calculates QDMTT under local law
- MNE recalculates Top-up Tax under GloBE Rules
- Compare results; credit QDMTT against GloBE liability
- Risk of differences requiring reconciliation

**With QDMTT Safe Harbour:**
- MNE calculates QDMTT under local law
- Top-up Tax deemed to be zero for IIR/UTPR
- No duplicate GloBE calculation required
- Simplified compliance

---

## 9.2.2 The Three Qualifying Standards

For a jurisdiction's QDMTT to qualify for the QDMTT Safe Harbour, it must meet three standards assessed through a peer review process.

### Standard 1: QDMTT Accounting Standard

The QDMTT must be computed based on one of the following:

**Option A: UPE's Financial Accounting Standard**
- Uses the same accounting standard as the consolidated financial statements
- Ensures consistency with GloBE Income calculations

**Option B: Local Financial Accounting Standard**

Subject to conditions:
- All Constituent Entities in the jurisdiction use that local standard
- Entities are required to maintain such accounts under domestic law, OR
- Financial accounts are subject to external financial audit
- Fiscal year must align with consolidated financial statement year

```
ACCOUNTING STANDARD DECISION TREE
=================================

Does jurisdiction use UPE accounting standard?
     │
     ├── YES ──► Accounting Standard: SATISFIED
     │
     └── NO ──► Does jurisdiction use Local GAAP?
                    │
                    ├── YES ──► Are conditions met?
                    │              │
                    │              ├── All CEs use local standard? ──►
                    │              │   Required by law OR audited? ──►
                    │              │   FY aligns with group? ──►
                    │              │
                    │              └── All YES: SATISFIED
                    │                  Any NO: NOT SATISFIED
                    │
                    └── NO ──► Accounting Standard: NOT SATISFIED
```

### Standard 2: Consistency Standard

The QDMTT computations must be **substantially the same** as GloBE Rule calculations, with limited exceptions:

**Permitted Deviations:**

| Category | Description |
|----------|-------------|
| **Required departures** | Where QDMTT definition explicitly requires different treatment |
| **Approved variations** | Where Inclusive Framework has accepted an optional variation |
| **Transition rules** | Timing differences during implementation |

**Examples of Consistency Requirements:**

| GloBE Element | QDMTT Must |
|---------------|------------|
| GloBE Income | Use same adjustments to accounting income |
| Covered Taxes | Apply same inclusion/exclusion criteria |
| SBIE | Use same formula and percentages |
| ETR calculation | Apply same methodology |
| De minimis | Apply same thresholds |

**Not Permitted:**
- Lower minimum rate than 15%
- Narrower definition of Covered Taxes
- Broader SBIE calculation
- Exclusions not recognised under GloBE

### Standard 3: Administration Standard

The QDMTT jurisdiction must meet ongoing monitoring requirements:

**Requirements:**

1. **Information collection** consistent with GloBE requirements
2. **Reporting requirements** aligned with GIR approach
3. **Exchange of information** participation
4. **Ongoing compliance** with peer review process

**Peer Review Process:**

The OECD Inclusive Framework conducts peer reviews to determine whether a jurisdiction's QDMTT qualifies for the safe harbour. The outcome is recorded in a central register of qualified legislation.

---

## 9.2.3 Jurisdictions with QDMTT Safe Harbour Status

### Current Status (2024-2025)

The Inclusive Framework maintains a list of jurisdictions whose QDMTT legislation has been reviewed and granted qualified status.

**Jurisdictions with QDMTT (as of 2025):**

| Jurisdiction | QDMTT Enacted | Safe Harbour Status |
|--------------|---------------|---------------------|
| United Kingdom | Yes (2023) | Transitional qualified |
| Germany | Yes (2023) | Transitional qualified |
| Netherlands | Yes (2023) | Transitional qualified |
| France | Yes (2023) | Transitional qualified |
| South Korea | Yes (2023) | Transitional qualified |
| Japan | Yes (2024) | Transitional qualified |
| Ireland | Yes (2024) | Transitional qualified |
| Australia | Yes (2024) | Transitional qualified |
| Switzerland | Yes (2024) | Transitional qualified |
| Canada | Yes (2024) | Transitional qualified |

**Note:** "Transitional qualified" status applies during the initial implementation period. Full peer review for permanent status is ongoing.

### Checking Qualification Status

Before claiming QDMTT Safe Harbour, verify:

1. **Jurisdiction has enacted QDMTT** - Legislation in force for the fiscal year
2. **Safe harbour status granted** - Check OECD central register
3. **Effective date** - Status applies from a specific date
4. **No switch-off** - Status has not been revoked

---

## 9.2.4 Impact on IIR and UTPR

### How QDMTT Safe Harbour Affects IIR

When the QDMTT Safe Harbour applies:

```
IIR IMPACT OF QDMTT SAFE HARBOUR
================================

Scenario: Parent entity in IIR jurisdiction;
          Subsidiary in QDMTT Safe Harbour jurisdiction

Without Safe Harbour:
┌──────────────────────────────────────────────────┐
│ Subsidiary jurisdiction ETR: 10%                 │
│ GloBE Top-up Tax: 5% (to reach 15%)              │
│ QDMTT paid: 5%                                   │
│ IIR charge = 5% - 5% QDMTT credit = 0%           │
│                                                  │
│ Calculation required: YES (for QDMTT credit)     │
└──────────────────────────────────────────────────┘

With Safe Harbour:
┌──────────────────────────────────────────────────┐
│ QDMTT applies in subsidiary jurisdiction         │
│ Top-up Tax deemed to be: ZERO                    │
│ IIR charge: ZERO (automatic)                     │
│                                                  │
│ Calculation required: NO                         │
└──────────────────────────────────────────────────┘
```

### How QDMTT Safe Harbour Affects UTPR

The UTPR operates as the "backstop" rule. Where QDMTT Safe Harbour applies:

1. **Top-up Tax deemed zero** for that jurisdiction
2. **No UTPR allocation** arises for that jurisdiction
3. **UTPR jurisdictions** have no collection rights

**Practical Effect:**

| Without QDMTT Safe Harbour | With QDMTT Safe Harbour |
|---------------------------|-------------------------|
| Calculate UTPR top-up amount | UTPR amount is zero |
| Allocate to UTPR jurisdictions | No allocation required |
| Multiple jurisdictions may claim | No competing claims |
| Risk of double taxation/disputes | Eliminated |

### Transitional UTPR Safe Harbour (Related)

Separately, the **Transitional UTPR Safe Harbour** provides relief for UPE jurisdictions:

**Conditions:**
- UPE jurisdiction has statutory corporate tax rate ≥ 20%
- Applies to fiscal years beginning on or before 31 December 2025
- Fiscal year ends before 31 December 2026

**Effect:** UTPR does not apply to the UPE jurisdiction during the transitional period.

---

## 9.2.5 Impact on GIR Content

### Reduced Reporting for QDMTT Safe Harbour Jurisdictions

Where the QDMTT Safe Harbour applies, GIR reporting requirements are reduced:

**GIR Section 2 (Jurisdictional Data):**

| Data Element | Full Reporting | Safe Harbour Reporting |
|--------------|----------------|------------------------|
| Jurisdiction identifier | Required | Required |
| Safe harbour indicator | N/A | Required |
| GloBE Income details | Full calculation | Not required |
| Covered Taxes details | Full calculation | Not required |
| ETR calculation | Full breakdown | Not required |
| Top-up Tax | Calculated amount | Deemed zero |
| QDMTT reference | N/A | Required |

**GIR Section 3 (Entity Data):**

| Data Element | Full Reporting | Safe Harbour Reporting |
|--------------|----------------|------------------------|
| Entity identification | Required | Reduced |
| Ownership details | Required | Reduced |
| Financial data | Full GloBE data | Not required |
| Allocations | Full detail | Not required |

**Key Simplification:** Where a safe harbour reduces the Top-up Tax to zero for Constituent Entities, the filing entity **does not complete** the detailed tables in Section 3 for those entities.

### GIR Reporting Example

```
GIR SECTION 2 - JURISDICTION WITH QDMTT SAFE HARBOUR
====================================================

Jurisdiction: Germany
QDMTT Safe Harbour Applied: YES
QDMTT Legislation Reference: MinStG 2023
Safe Harbour Status: Transitional Qualified

Reporting:
┌─────────────────────────────────────────────────────┐
│ Field                          │ Value              │
├─────────────────────────────────────────────────────┤
│ Jurisdiction Code              │ DE                 │
│ Safe Harbour Election          │ QDMTT              │
│ Number of Constituent Entities │ 5                  │
│ GloBE Income                   │ [Not reported]     │
│ Covered Taxes                  │ [Not reported]     │
│ ETR                            │ [Not reported]     │
│ Top-up Tax                     │ 0 (deemed)         │
│ QDMTT Paid                     │ €2,500,000         │
└─────────────────────────────────────────────────────┘

GIR Section 3 for German entities: NOT REQUIRED
(Safe harbour applies - detailed entity tables omitted)
```

---

## 9.2.6 Documentation Requirements

### Supporting Documentation

Even with reduced GIR reporting, documentation must be maintained:

**Required Records:**

| Document | Purpose | Retention |
|----------|---------|-----------|
| QDMTT calculation | Evidence of domestic tax paid | 10 years |
| Safe harbour status confirmation | Eligibility verification | Per filing |
| Local QDMTT return | Filed return copy | 10 years |
| Payment evidence | Proof of tax payment | 10 years |
| Legislation reference | Qualifying QDMTT basis | Permanent |

### Audit Defence Considerations

Tax authorities may request verification that:

1. **QDMTT was actually paid** - Payment confirmation
2. **Jurisdiction qualifies** - Safe harbour status at time of filing
3. **Calculation was correct** - QDMTT computation under local law
4. **All CEs covered** - QDMTT applied to all entities in jurisdiction

**Documentation Checklist:**

```
QDMTT SAFE HARBOUR DOCUMENTATION
================================

□ QDMTT jurisdiction qualifies (OECD register check)
□ Local QDMTT legislation in force for fiscal year
□ QDMTT return filed with local authority
□ QDMTT calculation workpapers retained
□ QDMTT payment confirmation obtained
□ GIR safe harbour election marked
□ Section 3 exemption documented
□ Year-on-year consistency confirmed
```

---

## 9.2.7 Interaction with Transitional CbCR Safe Harbour

### Two Distinct Safe Harbours

The QDMTT Safe Harbour and Transitional CbCR Safe Harbour are separate mechanisms:

| Feature | Transitional CbCR Safe Harbour | QDMTT Safe Harbour |
|---------|-------------------------------|-------------------|
| **Purpose** | Ease early compliance burden | Avoid duplicate calculations |
| **Duration** | Transitional (ends FY 2026) | Permanent |
| **Basis** | CbCR data | QDMTT payment |
| **Tests** | De minimis, ETR, Routine Profits | Three standards met |
| **Jurisdiction dependency** | Any jurisdiction | Only QDMTT jurisdictions |

### Can Both Apply?

Yes, a jurisdiction may qualify under both safe harbours:

**Scenario A: Both available, choose one**
- Jurisdiction has qualifying QDMTT
- Jurisdiction also meets Transitional CbCR criteria
- MNE may apply either safe harbour
- QDMTT Safe Harbour preferred (permanent, simpler)

**Scenario B: Transitional only**
- Jurisdiction has no QDMTT
- Jurisdiction meets Transitional CbCR criteria
- Apply Transitional CbCR Safe Harbour

**Scenario C: QDMTT only**
- Jurisdiction has qualifying QDMTT
- Jurisdiction fails Transitional CbCR tests
- Apply QDMTT Safe Harbour

**Scenario D: Neither**
- No QDMTT in jurisdiction
- Fails Transitional CbCR tests
- Full GloBE calculation required

### Strategic Considerations

| Factor | Recommendation |
|--------|----------------|
| **QDMTT available** | Prefer QDMTT Safe Harbour (permanent) |
| **No QDMTT** | Use Transitional CbCR if eligible |
| **Transitional period ending** | Transition to QDMTT Safe Harbour where possible |
| **"Once out, always out" risk** | QDMTT Safe Harbour avoids this issue |

---

## 9.2.8 Jurisdictions Without QDMTT

### Implications for Non-QDMTT Jurisdictions

Where a jurisdiction has **not enacted QDMTT**:

1. **No QDMTT Safe Harbour available** - Must use Transitional CbCR or full calculation
2. **Top-up Tax may arise** - IIR or UTPR may apply
3. **Full GIR reporting** - Section 2 and Section 3 completion required

**Common Non-QDMTT Jurisdictions:**

| Jurisdiction | Pillar Two Status | Implication |
|--------------|-------------------|-------------|
| United States | No implementation | US profits may be subject to IIR/UTPR in other jurisdictions |
| China | Under consideration | May have future QDMTT |
| India | Under consideration | May have future QDMTT |
| Various tax havens | Limited implementation | Subject to IIR/UTPR charging |

### Planning Considerations

For operations in non-QDMTT jurisdictions:

1. **Monitor legislative developments** - QDMTT may be enacted
2. **Assess Transitional CbCR eligibility** - May provide temporary relief
3. **Model IIR/UTPR exposure** - Understand potential charges
4. **Consider substance** - SBIE may reduce Top-up Tax

---

## 9.2.9 Practical Application

### Case Study: Multi-Jurisdiction Group

**Scenario:**

UK-parented MNE group with subsidiaries in:
- Germany (QDMTT enacted)
- Singapore (QDMTT enacted)
- United States (no QDMTT)
- Ireland (QDMTT enacted)

**Analysis:**

| Jurisdiction | QDMTT Status | Safe Harbour Available | GIR Reporting |
|--------------|--------------|------------------------|---------------|
| UK (parent) | Yes | QDMTT Safe Harbour | Simplified |
| Germany | Yes | QDMTT Safe Harbour | Simplified |
| Singapore | Yes | QDMTT Safe Harbour | Simplified |
| United States | No | Transitional CbCR only | Full (if fails CbCR) |
| Ireland | Yes | QDMTT Safe Harbour | Simplified |

**GIR Completion:**

```
GIR COMPLETION SUMMARY
======================

Section 1: Group Information
  ► Complete in full (always required)

Section 2: Jurisdictional Data
  ► UK: QDMTT Safe Harbour - simplified reporting
  ► Germany: QDMTT Safe Harbour - simplified reporting
  ► Singapore: QDMTT Safe Harbour - simplified reporting
  ► US: Full calculation required (assess CbCR Safe Harbour)
  ► Ireland: QDMTT Safe Harbour - simplified reporting

Section 3: Entity Data
  ► UK entities: Not required (safe harbour)
  ► German entities: Not required (safe harbour)
  ► Singapore entities: Not required (safe harbour)
  ► US entities: Full detail required
  ► Irish entities: Not required (safe harbour)
```

### Workflow: Applying QDMTT Safe Harbour

```
QDMTT SAFE HARBOUR APPLICATION WORKFLOW
=======================================

STEP 1: Identify QDMTT Jurisdictions
        └── List jurisdictions with QDMTT legislation

STEP 2: Verify Safe Harbour Status
        └── Check OECD central register
        └── Confirm status is effective for fiscal year

STEP 3: Confirm QDMTT Compliance
        └── QDMTT return filed locally
        └── QDMTT payment made
        └── Documentation retained

STEP 4: Prepare GIR
        └── Mark QDMTT Safe Harbour in Section 2
        └── Enter deemed zero Top-up Tax
        └── Omit detailed Section 3 for those CEs

STEP 5: Document Position
        └── Maintain safe harbour eligibility evidence
        └── Retain QDMTT calculation and payment records
        └── File GIR with safe harbour election

STEP 6: Ongoing Monitoring
        └── Monitor for safe harbour status changes
        └── Track QDMTT payment each year
        └── Update documentation annually
```

---

## 9.2.10 Common Issues and Solutions

### Issue 1: Timing Mismatch

**Problem:** QDMTT return filed after GIR deadline

**Solution:**
- QDMTT Safe Harbour based on QDMTT **applying**, not filing date
- Document that QDMTT will be/has been filed
- Amend GIR if QDMTT calculation differs materially

### Issue 2: Partial QDMTT Coverage

**Problem:** QDMTT enacted mid-year or not covering all CEs

**Solution:**
- Safe harbour applies only to periods/entities covered by QDMTT
- Full calculation required for non-covered periods/entities
- Document the split clearly

### Issue 3: QDMTT Status Uncertainty

**Problem:** Peer review not complete; status unclear

**Solution:**
- Check for "transitional qualified" status
- Conservative approach: perform full calculation as backup
- Document reliance on published status

### Issue 4: Local vs GloBE Differences

**Problem:** QDMTT calculation differs from GloBE result

**Solution:**
- If QDMTT Safe Harbour applies, use QDMTT result
- No reconciliation to GloBE required
- Document that safe harbour was correctly applied

---

## Deliverable: QDMTT Safe Harbour Assessment Template

```
QDMTT SAFE HARBOUR ASSESSMENT
=============================

PART A: GROUP AND YEAR IDENTIFICATION

MNE Group Name: _____________________________________
UPE Jurisdiction: ___________________________________
Fiscal Year End: ____________________________________
Prepared by: __________________ Date: _______________

PART B: JURISDICTION ANALYSIS

For each jurisdiction with Constituent Entities:

JURISDICTION 1: _______________________

1. QDMTT Enacted?
   □ Yes  □ No
   If No → QDMTT Safe Harbour NOT available

2. QDMTT Safe Harbour Status (check OECD register):
   □ Qualified
   □ Transitional Qualified
   □ Not Qualified / Pending
   □ Not Listed

   Status effective from: _______________

3. QDMTT Compliance:
   □ QDMTT return filed with local authority
   □ QDMTT payment made
   □ QDMTT calculation retained

4. QDMTT Safe Harbour Claimed?
   □ Yes  □ No

5. GIR Reporting Approach:
   □ Simplified (safe harbour)
   □ Full calculation

QDMTT Amount Paid: €_________________

[Repeat for each jurisdiction]

PART C: SUMMARY TABLE

| Jurisdiction | QDMTT? | SH Status | Claimed? | Top-up Tax |
|--------------|--------|-----------|----------|------------|
| ____________ | Y / N  | _______   | Y / N    | €_________ |
| ____________ | Y / N  | _______   | Y / N    | €_________ |
| ____________ | Y / N  | _______   | Y / N    | €_________ |
| ____________ | Y / N  | _______   | Y / N    | €_________ |
| ____________ | Y / N  | _______   | Y / N    | €_________ |

PART D: DOCUMENTATION CHECKLIST

Per QDMTT Safe Harbour Jurisdiction:

□ OECD register status confirmation (screenshot/printout)
□ Local QDMTT legislation reference
□ QDMTT return (filed copy)
□ QDMTT calculation workpapers
□ QDMTT payment confirmation
□ GIR safe harbour election documentation

PART E: SIGN-OFF

I confirm that the QDMTT Safe Harbour assessment has been completed
accurately and that supporting documentation is retained.

Prepared by: _____________________ Date: ____________
Reviewed by: _____________________ Date: ____________
Approved by: _____________________ Date: ____________
```

---

## Section Summary

The QDMTT Safe Harbour provides **permanent** simplification for MNE groups operating in jurisdictions with qualifying QDMTT legislation:

1. **Eliminates duplicate calculations** - No need to recalculate GloBE Top-up Tax
2. **Deems Top-up Tax to zero** - Automatic for IIR and UTPR purposes
3. **Reduces GIR reporting** - Simplified Section 2; no Section 3 entity detail
4. **Requires three standards** - Accounting, Consistency, Administration
5. **Subject to peer review** - Check OECD register for qualification status

Unlike the Transitional CbCR Safe Harbour, the QDMTT Safe Harbour is **permanent** and does not have the "once out, always out" limitation.

---

## Key Takeaways

| Topic | Key Point |
|-------|-----------|
| **Purpose** | Avoid duplicate GloBE calculations where QDMTT paid |
| **Three Standards** | Accounting, Consistency, Administration |
| **Effect** | Top-up Tax deemed zero for IIR/UTPR |
| **Duration** | Permanent (not transitional) |
| **GIR Impact** | Simplified Section 2; omit Section 3 for CEs |
| **Peer Review** | Check OECD register for jurisdiction status |
| **Documentation** | Retain QDMTT returns, payments, status evidence |
| **vs. CbCR Safe Harbour** | Separate mechanisms; can apply both where eligible |

---

## Sources

Key references for this section include:

- [OECD Safe Harbours and Penalty Relief Guidance](https://www.oecd.org/tax/beps/safe-harbours-and-penalty-relief-global-anti-base-erosion-rules-pillar-two.pdf)
- [QDMTT Safe Harbour - OECD Pillars](https://oecdpillars.com/pillar-tab/qdmtt-safe-harbour/)
- [PwC - OECD Releases Pillar Two GloBE Rules Guidance](https://www.pwc.com/gx/en/tax/newsletters/tax-policy-bulletin/assets/pwc-oecd-releases-p2-globe-rules-guidance-and-information-return.pdf)
- [KPMG - Understanding QDMTT and Safe Harbor](https://kpmg.com/ch/en/insights/taxes/beps-2/financial-disclosure-requirements-qdmtt-safe-harbour.html)

---

*Section 9.2 Complete. Proceed to Section 9.3: Simplified Reporting Elections.*
