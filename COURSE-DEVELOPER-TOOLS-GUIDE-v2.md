# MojiTax Tools Platform - Course Developer Guide

## What is tools.mojitax.com?

**tools.mojitax.com** is a companion platform to MojiTax eBooks that provides **practical demo tools** for learners. When you build an eBook, you're not just creating written content—you're creating an integrated learning experience that includes hands-on practice.

Think of it as the "lab" component of a science course. The eBook teaches the theory; the tools provide the practice.

---

## The eBook + Tools Model

```
┌─────────────────────────────────────────────────────────────────────────┐
│                     INTEGRATED LEARNING EXPERIENCE                       │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│   eBOOK (mojitax.co.uk)                TOOLS (tools.mojitax.com)        │
│   ┌─────────────────────────────┐      ┌─────────────────────────────┐  │
│   │                             │      │                             │  │
│   │  📖 Chapter Content         │      │                             │  │
│   │  📋 Concepts & Explanations │  ──► │  🛠️ Practical Tools         │  │
│   │  📎 Appendices              │      │     (whatever form serves   │  │
│   │     (questions & data)      │      │      the learning best)     │  │
│   │                             │      │                             │  │
│   └─────────────────────────────┘      └─────────────────────────────┘  │
│                                                                          │
│   "Learn the concept"                  "Practice the skill"             │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## Why Think About Tools When Writing Your eBook?

Tools should be planned **at the eBook design stage**, not added as an afterthought:

| If you plan tools early... | If you add tools later... |
|---------------------------|---------------------------|
| Tools align with what you're teaching | Tools feel disconnected from content |
| Practice flows naturally from chapters | Exercises feel bolted on |
| The learner journey is coherent | Learners struggle to connect theory to practice |
| Development is coordinated | Development is rushed and fragmented |

---

## What Are Demo Tools?

Demo tools are **simplified, educational versions** of professional tax software. They're designed for learning, not production use.

### Key Characteristics

| Aspect | Description |
|--------|-------------|
| **Purpose** | Help learners practice concepts through hands-on use |
| **Complexity** | Simplified—focused on core functionality |
| **Data** | Sample/practice data provided in eBook Appendices |
| **Output** | Practice results—no feedback or assessment |
| **Liability** | Educational only—every tool carries a disclaimer |

### Important: Tools Are for Practice Only

**Tools do not provide feedback.** They are instruments for hands-on practice—like a calculator or a form. The learning happens through:
- Using the tool with the scenarios from your eBook
- Comparing results to expected outcomes in the Appendices
- Working through progressive case studies that build understanding

### The Disclaimer (On Every Tool)

> *"This is a demo tool for learning purposes only. Results are illustrative and should not be used for actual tax filings or professional advice. Always consult qualified tax professionals for real-world applications."*

---

## Tool Types: Whatever Works Best

Tools can take **any form that serves the learning objective**. There is no fixed template—design what's practical and valuable for your eBook.

Common forms include:
- Calculators
- Search/lookup tools
- Validators and format checkers
- Forms
- Document generators
- Compliance report tools
- Trackers and monitors
- Reference libraries
- Verification tools

**The key question is not "which template should I use?" but "what tool would genuinely help learners practice this skill?"**

---

## The Golden Rule: Fewer, Better Tools

### Quality Over Quantity

**Don't aim for many tools. Aim for the right tools.**

A single well-designed tool that directly supports your eBook content is worth more than five generic tools that don't quite fit.

### The Gate Question

Before requesting any tool, answer this:

> **"If this tool didn't exist, what would the learner miss?"**

If your answer is vague or uncertain, no tool is needed. If you can clearly articulate what practice opportunity would be lost, the tool may be worth building.

### Signs You've Got It Right

✅ Each tool has a clear purpose tied to specific chapters  
✅ Practice scenarios build naturally from the eBook content  
✅ Learners can immediately see how the tool applies to what they've read  
✅ The tool fills a gap that reading alone couldn't fill

### Signs You've Gone Wrong

❌ Tools exist because "we should have some tools"  
❌ Generic tools that could belong to any course  
❌ Many tools with little connection to the eBook narrative  
❌ Practice scenarios that feel like afterthoughts

---

## Where Do Questions and Data Live?

**Questions and associated data belong in the eBook Appendices.**

The structure:
- **eBook chapters**: Teach the concepts
- **eBook Appendices**: Contain practice questions, scenarios, sample data, and expected outcomes
- **Tools platform**: Provides the instruments for working through those scenarios

This keeps everything the learner needs in one place (the eBook) while the tools platform provides the hands-on practice environment.

---

## Planning Tools for Your eBook

### Step 1: Review Your Chapters

For each chapter, ask: **"What should learners be able to DO after reading this?"**

Not every chapter needs a tool. Some chapters are purely conceptual. Focus on chapters where hands-on practice would genuinely help.

### Step 2: Check the Tools Registry

**Before designing a new tool, check what already exists.**

Many tools are reusable across eBooks. Reusing existing tools means:
- No development time needed
- Learners who read multiple eBooks see familiar tools
- Consistency across the platform

### Step 3: Design Only What's Needed

If a tool doesn't exist and you genuinely need one, define it clearly:

```
TOOL NAME: [Name]
FORM: [What type of tool is this?]
CATEGORY: [Tax area]

PURPOSE:
What specific skill does this tool help learners practice?

RELATED CHAPTERS:
Which chapters in your eBook will reference this tool?

WHY THIS TOOL ADDS VALUE:
Why is hands-on practice with this tool better than just reading about it?
```

---

## Designing Practice Scenarios

### One eBook, One Storyline

Rather than thinking "which tools do I need?", start with a different question:

> **"What's the one fictional company or scenario that will carry through this entire eBook?"**

The storyline comes first. Tools serve it.

When you anchor your eBook to a single evolving scenario, practice becomes natural. Learners follow a company through challenges, apply what they've learned at each stage, and see how concepts connect across chapters.

### Progressive Scenarios

The best practice scenarios **build on each other**, developing the learner as they progress through your eBook.

**Don't create isolated, disconnected exercises.** Build on your storyline:

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    PROGRESSIVE PRACTICE STORYLINE                        │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  Chapter 2 Scenario: "You've just joined the tax team at GlobalCo..."   │
│                ↓                                                        │
│  Chapter 4 Scenario: "Three months later, GlobalCo acquires a           │
│                       subsidiary. Using what you've learned..."         │
│                ↓                                                        │
│  Chapter 6 Scenario: "The tax authority has now raised questions        │
│                       about GlobalCo's structure. You need to..."       │
│                ↓                                                        │
│  Final Scenario: "It's year-end at GlobalCo. Pulling together           │
│                   everything you've practiced..."                       │
│                                                                          │
│  The learner grows alongside the fictional scenario.                    │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

### Why Progressive Storylines Work

| Disconnected Exercises | Progressive Storyline |
|------------------------|----------------------|
| Each exercise starts fresh | Learner builds on previous work |
| No sense of development | Clear sense of growth |
| Exercises feel like tests | Exercises feel like real work |
| Easy to skip | Engaging—learners want to see what happens next |

### Scenario Structure (for Appendices)

Each scenario in your Appendices should include:

```
SCENARIO: [Title that connects to the storyline]
CHAPTER: [Which chapter this follows]
TOOL: [Which tool to use]

CONTEXT:
[How does this connect to the previous scenario? What's new?]

TASK:
[What should the learner do?]

DATA PROVIDED:
[The specific inputs they'll need]

EXPECTED OUTCOME:
[What results should they get?]

LEARNING POINT:
[What should they take away from this?]
```

---

## Workflow: eBook Developer + App Developer

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    COORDINATED DEVELOPMENT                               │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  eBOOK DEVELOPER                       APP DEVELOPER                     │
│  ─────────────────                     ─────────────────                 │
│                                                                          │
│  1. Plans eBook outline                (waits)                           │
│     ↓                                                                    │
│  2. Identifies where practice          (waits)                           │
│     would add real value                                                 │
│     ↓                                                                    │
│  3. Checks Tools Registry              (waits)                           │
│     ↓                                                                    │
│  4. Specifies any new tools       ───► Receives specifications          │
│     (only if truly needed)              ↓                                │
│     ↓                                  5. Develops tools                 │
│  6. Writes eBook content                ↓                                │
│     ↓                                  7. Tools ready                    │
│  7. Creates Appendices with        ◄───                                  │
│     progressive scenarios                                                │
│     ↓                                                                    │
│  8. Tests complete flow                                                  │
│     ↓                                                                    │
│  9. eBook + Tools launch together                                        │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## Adding Tool References in Your eBook

### In Chapter Content

> "Now let's see how this works in practice. In the tools platform, you'll find [Tool Name]. Head to the Appendices for Scenario 3, which walks you through applying what we've just covered."

### In Appendices

The Appendices should contain:
1. **All practice scenarios** in progressive order
2. **Sample data** for each scenario
3. **Expected outcomes** so learners can check their work
4. **Discussion points** for deeper understanding

---

## Summary: Your Checklist

When developing an eBook, ensure you:

- [ ] Review chapters and identify where practice adds real value (not everywhere)
- [ ] Check the Tools Registry before requesting new tools
- [ ] Request new tools only if they're genuinely needed and valuable
- [ ] Design a progressive storyline for practice scenarios
- [ ] Create Appendices with scenarios, data, and expected outcomes
- [ ] Reference tools naturally within chapter content
- [ ] Test the complete learner journey (chapter → Appendix scenario → tool)
- [ ] Update the Tools Registry with any new tools

---

*Guide Version: 2.0*  
*Last Updated: December 2024*
