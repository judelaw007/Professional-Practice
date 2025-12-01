# Section 8.5: Local Filing Obligations Post-DFE

## Learning Objectives

By the end of this section, you will be able to:

- Identify which local filing obligations remain after DFE appointment
- Distinguish between GIR filing and local Top-up Tax return obligations
- Coordinate effectively between DFE and local entities
- Ensure local registration requirements are met in each jurisdiction

---

## 8.5.1 Understanding the DFE Filing Scope

### What DFE Filing Covers

The DFE files the **GloBE Information Return** on behalf of Constituent Entities. This covers:

- Section 1: Group-level information
- Section 2: Jurisdictional data for covered jurisdictions
- Section 3: Entity-level data for covered CEs

### What DFE Filing Does NOT Cover

Critically, the DFE appointment does **not** eliminate all local obligations:

| Obligation Type | DFE Covers? | Local Entity Responsibility |
|-----------------|-------------|----------------------------|
| GIR filing | Yes (for covered CEs) | None if covered by DFE |
| Local Top-up Tax returns | **No** | Local entity must file |
| QDMTT returns | **No** | Local entity must file |
| Local registration | **No** | Local entity must register |
| Top-up Tax payment | **No** | Liable entity must pay |

**Key Principle:** The DFE is an information reporting mechanism. It does not transfer substantive tax liabilities or local compliance obligations.

---

## 8.5.2 Local Filing Obligations by Type

### Type 1: Local Top-up Tax Returns

Many jurisdictions require separate returns for Top-up Tax liability, distinct from the GIR:

| Jurisdiction | Local Return Required | Filing Entity |
|--------------|----------------------|---------------|
| **UK** | MTT Self-Assessment Return | UK CE or responsible member |
| **Germany** | Mindeststeuer-Erklärung | German CE |
| **Netherlands** | Aangifte minimumbelasting | Dutch CE |
| **France** | Déclaration IMPT | French CE |
| **Australia** | CGDMTR schedules | Australian CE |

**Example - UK Structure:**

```
UK FILING OBLIGATIONS
=====================

1. GIR FILING (via DFE or locally)
   └── Information return only
   └── Can be filed by DFE

2. MTT SELF-ASSESSMENT RETURN
   └── Tax liability return
   └── Must be filed by UK entity
   └── Cannot be delegated to non-UK DFE

3. MTT PAYMENT
   └── Must be paid by UK liable entity
   └── Follows UK payment deadlines
```

### Type 2: QDMTT Returns

Jurisdictions with Qualified Domestic Minimum Top-up Tax require local QDMTT returns:

| Jurisdiction | QDMTT Return | Relationship to GIR |
|--------------|--------------|---------------------|
| **UK** | Part of MTT SA Return | Separate from GIR |
| **Germany** | Included in Mindeststeuer-Erklärung | Separate from GIR |
| **South Korea** | Local QDMTT return | Separate filing |
| **Japan** | QDMTT declaration | Separate filing |

**QDMTT vs GIR Distinction:**

```
GIR                              QDMTT RETURN
===                              ============
- Information reporting          - Tax liability reporting
- Filed via MCAA exchange        - Filed locally only
- No tax payment attached        - Tax payment required
- DFE can file                   - Local entity files
```

### Type 3: IIR/UTPR Top-up Tax Returns

Where IIR or UTPR applies, the charging jurisdiction requires its own return:

| Rule | Who Files | Where Filed |
|------|-----------|-------------|
| **IIR** | Parent entity in IIR jurisdiction | Parent's jurisdiction |
| **UTPR** | UTPR-liable entities | Each UTPR jurisdiction |

---

## 8.5.3 Coordination Between DFE and Local Entities

### Information Flow Requirements

Even with a DFE, local entities need information to complete local returns:

```
INFORMATION FLOW MODEL
======================

        ┌──────────────────┐
        │       DFE        │
        │  (Central GIR)   │
        └────────┬─────────┘
                 │
    ┌────────────┼────────────┐
    │            │            │
    ▼            ▼            ▼
┌───────┐   ┌───────┐   ┌───────┐
│ UK CE │   │ DE CE │   │ NL CE │
└───┬───┘   └───┬───┘   └───┬───┘
    │           │           │
    ▼           ▼           ▼
UK MTT SA   DE MinSt    NL Aangifte

Data needed:          Data needed:          Data needed:
- UK ETR              - DE ETR              - NL ETR
- UK Top-up Tax       - DE Top-up Tax       - NL Top-up Tax
- UK QDMTT            - DE QDMTT            - NL QDMTT
- Allocation basis    - Allocation basis    - Allocation basis
```

### Data Sharing Protocol

The DFE must provide local entities with data needed for local returns:

**Required Data Outputs from DFE:**

| Data Element | Purpose | Recipient |
|--------------|---------|-----------|
| Jurisdictional ETR | Local return completion | Local CE |
| Top-up Tax by jurisdiction | Local liability reporting | Local CE |
| QDMTT calculations | QDMTT return | Local CE |
| Allocation keys | Multi-entity jurisdictions | All local CEs |
| Safe harbour status | Local return elections | Local CE |

**Timing Coordination:**

| Milestone | DFE Action | Local Entity Action |
|-----------|------------|---------------------|
| T-8 weeks | Finalise jurisdiction calculations | - |
| T-6 weeks | Distribute local data packages | Receive and review |
| T-4 weeks | Respond to queries | Prepare local returns |
| T-2 weeks | Final confirmation | Finalise local returns |
| Deadline | File GIR | File local returns |

### Practical Coordination Checklist

```
DFE-LOCAL ENTITY COORDINATION CHECKLIST
=======================================

□ Local return requirements identified per jurisdiction
□ Data sharing templates prepared
□ Timeline aligned (GIR and local returns)
□ Responsible persons identified at local level
□ Query resolution process established
□ Sign-off protocol agreed

Per Jurisdiction:
□ [UK] MTT SA return preparer identified
□ [UK] Data package provided by DFE
□ [DE] Mindeststeuer return preparer identified
□ [DE] Data package provided by DFE
□ [NL] Aangifte preparer identified
□ [NL] Data package provided by DFE
[Continue for each jurisdiction]
```

---

## 8.5.4 Local Registration Requirements

### Registration Obligations Remain Local

DFE appointment does not satisfy local registration requirements:

| Jurisdiction | Registration Required | Who Must Register |
|--------------|----------------------|-------------------|
| **UK** | MTT registration | Each UK CE (or group representative) |
| **Germany** | MinStG notification | German group head entity |
| **Netherlands** | Minimumbelasting registration | Dutch CEs |
| **Singapore** | MTT registration | Singapore CEs |
| **Australia** | GMT/DMT registration | Australian CEs |

### UK Registration Example

```
UK MTT REGISTRATION REQUIREMENTS
================================

Even with non-UK DFE, UK entities must:

1. REGISTER with HMRC for Multinational Top-up Tax
   - Deadline: 6 months after FY end
   - Register via HMRC online services

2. APPOINT Responsible Member (if multiple UK CEs)
   - One UK entity acts as group representative
   - Files single UK MTT SA return

3. NOTIFY DFE arrangement
   - Inform HMRC that GIR filed via DFE
   - Provide DFE details

4. FILE UK MTT Self-Assessment
   - Regardless of DFE arrangement
   - UK-specific return for tax liability
```

### Germany Registration Example

```
GERMAN MinStG REGISTRATION
==========================

With non-German DFE:

1. GROUP HEAD NOTIFICATION still required
   - Meldung als Gruppenspitze
   - German entity notifies BZSt

2. DFE NOTIFICATION required
   - Inform BZSt of DFE arrangement
   - Provide DFE details and scope

3. LOCAL TAX RETURN remains
   - Mindeststeuer-Erklärung
   - Filed by German entity

4. GIR may be filed by DFE
   - Subject to MCAA exchange
   - Germany receives via automatic exchange
```

---

## 8.5.5 Common Coordination Scenarios

### Scenario 1: UK DFE for EU Subsidiaries

**Setup:** UK parent is DFE; subsidiaries in Germany, Netherlands, France

| Filing | Who Files | Where |
|--------|-----------|-------|
| GIR (all jurisdictions) | UK DFE | HMRC (exchanged via MCAA) |
| UK MTT SA Return | UK parent | HMRC |
| German Mindeststeuer | German sub | BZSt |
| Dutch Aangifte | Dutch sub | Belastingdienst |
| French IMPT declaration | French sub | DGFiP |

**Key Point:** DFE files GIR centrally; each local entity files local Top-up Tax return.

### Scenario 2: Non-Implementing Jurisdiction Parent (US)

**Setup:** US parent; UK subsidiary is DFE; operations in UK, Germany, Singapore

| Filing | Who Files | Where |
|--------|-----------|-------|
| GIR (all jurisdictions) | UK DFE | HMRC (exchanged via MCAA) |
| UK MTT SA Return | UK sub | HMRC |
| German Mindeststeuer | German sub | BZSt |
| Singapore MTT Return | Singapore sub | IRAS |
| US filing | None | US has no Pillar Two |

**Key Point:** US parent has no filing obligation; each implementing jurisdiction requires local return.

### Scenario 3: Multiple Low-Tax Jurisdictions

**Setup:** UK DFE; low-tax entities in Ireland and Luxembourg

| Filing | Who Files | Notes |
|--------|-----------|-------|
| GIR | UK DFE | Includes IE and LU data |
| UK MTT SA (IIR charge) | UK parent | Includes Top-up Tax on IE/LU |
| Irish return | Irish sub | May have QDMTT return |
| Luxembourg return | Lux sub | May have QDMTT return |

**Key Point:** IIR Top-up Tax charged in UK; local QDMTT returns still required where applicable.

---

## 8.5.6 Avoiding Common Pitfalls

### Pitfall 1: Assuming DFE Eliminates All Local Filings

**Mistake:** Believing that DFE appointment removes local return obligations

**Reality:** Local Top-up Tax returns remain required in most jurisdictions

**Solution:** Map all local filing obligations separately from GIR

### Pitfall 2: Missing Local Registration Deadlines

**Mistake:** Focusing only on GIR timeline; missing local registration deadlines

**Reality:** Local deadlines often differ from GIR deadlines

**Solution:** Create consolidated calendar including all local deadlines

### Pitfall 3: Inadequate Data Sharing

**Mistake:** DFE completes GIR without sharing data with local entities

**Reality:** Local entities need DFE data to complete local returns

**Solution:** Establish formal data sharing protocol and timeline

### Pitfall 4: Inconsistent Positions

**Mistake:** DFE and local returns show different figures

**Reality:** Authorities may cross-check GIR against local returns

**Solution:** Reconciliation process before filing; consistent data source

---

## 8.5.7 Local Filing Obligations Summary Matrix

### Comprehensive Jurisdiction Reference

| Jurisdiction | GIR via DFE | Local Tax Return | Registration | QDMTT Return |
|--------------|-------------|------------------|--------------|--------------|
| **UK** | ✓ | MTT SA (local) | Required | Part of MTT SA |
| **Germany** | ✓ | Mindeststeuer (local) | Required | Included |
| **Netherlands** | ✓ | Aangifte (local) | Required | Included |
| **France** | ✓ | IMPT déclaration (local) | Required | Included |
| **Singapore** | ✓ | MTT Return (local) | Required | Separate |
| **Australia** | ✓ | CGDMTR (local) | Required | Included |
| **Ireland** | ✓ | Top-up Tax return (local) | Required | Separate |
| **Japan** | ✓ | Local return (local) | Required | Separate |
| **South Korea** | ✓ | Local return (local) | Required | Separate |
| **Canada** | ✓ | GMT return (local) | Required | Included |

**Legend:**
- ✓ = Can be filed via DFE
- (local) = Must be filed by local entity

---

## Deliverable: Post-DFE Local Obligations Checklist

```
POST-DFE LOCAL FILING OBLIGATIONS CHECKLIST
===========================================

Group: ______________________________________
DFE Entity: _________________________________
Fiscal Year: ________________________________
Prepared by: _____________ Date: ____________

PART A: LOCAL REGISTRATION STATUS

Jurisdiction      Registration    Reference No.    Expiry/Renewal
____________      ____________    _____________    ______________
UK                □ Complete      _____________    ______________
Germany           □ Complete      _____________    ______________
Netherlands       □ Complete      _____________    ______________
France            □ Complete      _____________    ______________
Singapore         □ Complete      _____________    ______________
Australia         □ Complete      _____________    ______________
[Other]           □ Complete      _____________    ______________

PART B: LOCAL RETURN REQUIREMENTS

Jurisdiction    Return Type         Preparer         Deadline
____________    ___________         ________         ________
UK              MTT SA              ___________      ________
Germany         Mindeststeuer       ___________      ________
Netherlands     Aangifte            ___________      ________
France          IMPT déclaration    ___________      ________
Singapore       MTT Return          ___________      ________
Australia       CGDMTR              ___________      ________
[Other]         ___________         ___________      ________

PART C: DATA SHARING FROM DFE

Data Package              Provided    Date       Confirmed
____________              ________    ____       _________
UK jurisdictional data    □           ____       □
Germany jurisdictional    □           ____       □
Netherlands jurisdictional□           ____       □
France jurisdictional     □           ____       □
Singapore jurisdictional  □           ____       □
Australia jurisdictional  □           ____       □
[Other]                   □           ____       □

PART D: FILING STATUS

Jurisdiction    Return Filed    Date Filed    Confirmation
____________    ____________    __________    ____________
UK              □               __________    ____________
Germany         □               __________    ____________
Netherlands     □               __________    ____________
France          □               __________    ____________
Singapore       □               __________    ____________
Australia       □               __________    ____________
[Other]         □               __________    ____________

PART E: RECONCILIATION

□ All local returns reconcile to GIR jurisdictional data
□ Any differences documented and explained
□ Consistent elections across GIR and local returns

SIGN-OFF

DFE Manager: _________________ Date: _________
Local Tax Lead: ______________ Date: _________
Group Tax Director: __________ Date: _________
```

---

## Section Summary

DFE appointment streamlines GIR filing but does not eliminate local compliance obligations:

1. **Local Top-up Tax returns** remain required in most jurisdictions
2. **Local registration** must be completed by local entities
3. **QDMTT returns** are filed locally, not via DFE
4. **Coordination** between DFE and local entities is essential
5. **Data sharing** protocols ensure consistent positions

Understanding the boundary between DFE-filed GIR and local obligations is critical to achieving full compliance.

---

## Key Takeaways

| Topic | Key Point |
|-------|-----------|
| **DFE Scope** | Covers GIR only; not local tax returns |
| **Local Returns** | Required in UK, Germany, Netherlands, etc. |
| **Registration** | Local entities must register locally |
| **QDMTT** | Filed locally, not through DFE |
| **Data Sharing** | DFE must provide data for local returns |
| **Consistency** | Reconcile GIR and local return figures |
| **Timeline** | Coordinate GIR and local deadlines |

---

*Section 8.5 Complete. This concludes Section 8: Designated Filing Entity Requirements. Proceed to Section 9: Simplified Reporting and Safe Harbours.*
