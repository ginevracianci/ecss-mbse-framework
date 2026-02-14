# MBSE Methodology Guide

How to apply Model-Based Systems Engineering (MBSE) for process engineering in space systems.

## 📚 Introduction

### What is MBSE?

**Model-Based Systems Engineering (MBSE)** is the formalized application of modeling to support system requirements, design, analysis, verification, and validation activities beginning in the conceptual design phase and continuing throughout development and later life cycle phases.

**Key difference from traditional SE:**
- Traditional: Document-centric (Word, Excel, PowerPoint)
- MBSE: Model-centric (integrated system model as single source of truth)

### Why MBSE for Process Engineering?

Most engineers use MBSE for **system design** (spacecraft architecture, subsystems, etc.).

This framework demonstrates using MBSE for **process engineering**:
- Requirements management processes
- Verification and validation workflows
- Configuration control procedures
- Quality assurance gates

**Benefits:**
- ✅ Processes are visualized and understood by all stakeholders
- ✅ Process changes are tracked and version-controlled
- ✅ Process compliance can be verified
- ✅ Training materials generated from models

---

## 🎯 MBSE for ECSS Processes

### Requirements Engineering Process

**SysML Diagrams Used:**
- Activity Diagrams: Show workflow steps
- Use Case Diagrams: Stakeholder interactions
- Requirements Diagrams: Traceability

**Example Process Model:**

```
[Stakeholder Needs]
    ↓
[Elicit Requirements]
    ↓
[Write Requirements] → [Review Requirements]
    ↓                        ↓
[Assign Verification] ← [Approved?] → YES → [Baseline]
    ↓                        ↓
[Requirements Database]     NO → [Revise]
```

**Artifacts Generated:**
- Requirements specification template
- Review checklist
- Traceability matrix structure

---

### Verification Process

**Process Flow (Activity Diagram):**

```
[Requirements Baseline]
    ↓
[Create Test Plan]
    ↓
[Develop Test Cases] → [Review Test Cases]
    ↓                        ↓
[Setup Test Environment] ← [Approved?] → NO → [Revise]
    ↓                        ↓
[Execute Tests]             YES
    ↓
[Document Results]
    ↓
[All Tests Pass?] → NO → [Defect Management] → [Retest]
    ↓ YES
[Verification Complete]
```

---

## 🛠️ MBSE Tools

### Recommended Tools

| Tool | Purpose | License |
|------|---------|---------|
| **Cameo Systems Modeler** | Full SysML modeling (used in this framework) | Commercial |
| **Papyrus** | Open-source SysML | Free |
| **Enterprise Architect** | UML/SysML modeling | Commercial |
| **Capella** | MBSE for systems architecture | Open-source |

### Tool Selection Criteria

For **process engineering MBSE**:
- Must support SysML (Activity, Use Case, Requirements diagrams)
- Ability to export diagrams as images
- Requirements management integration
- Version control support

---

## 📊 Creating Process Models

### Step 1: Identify Process

**Questions to ask:**
- What is the process input?
- What is the process output?
- Who are the actors/stakeholders?
- What are the decision points?
- What are the quality gates?

### Step 2: Choose Diagram Type

| Process Aspect | SysML Diagram |
|----------------|---------------|
| Workflow steps | Activity Diagram |
| Stakeholder interactions | Use Case Diagram |
| System states | State Machine Diagram |
| Requirements flow | Requirements Diagram |

### Step 3: Model the Process

**Example: Requirements Review Process**

**Activity Diagram Elements:**
- **Actions**: "Review Requirement", "Update Requirement"
- **Decision Nodes**: "Approved?", "Critical Issue?"
- **Flows**: Show sequence and branches
- **Swim Lanes**: Show responsible roles

### Step 4: Validate Model

**Validation checks:**
- [ ] All process steps included
- [ ] Decision points have all branches
- [ ] Responsible parties identified
- [ ] Inputs/outputs defined
- [ ] Exception handling included

---

## 🎓 MBSE Best Practices

### For Process Engineering

**DO:**
- ✅ Keep models simple and readable
- ✅ Use consistent naming conventions
- ✅ Include all stakeholders in reviews
- ✅ Version control your models
- ✅ Export diagrams for documentation

**DON'T:**
- ❌ Over-complicate with too much detail
- ❌ Create models nobody will maintain
- ❌ Model for the sake of modeling
- ❌ Ignore feedback from process users

---

## 🔗 Integration with ECSS

### ECSS Process Requirements

ECSS standards define processes that **must** be followed.

**MBSE helps by:**
1. Modeling the process per ECSS requirements
2. Verifying all ECSS steps are included
3. Training teams using visual models
4. Auditing compliance to process

**Example: ECSS-E-ST-10-02C Requirements Process**

The standard requires:
- Requirements identification (§5.2.1)
- Requirements attributes (§5.2.2)
- Requirements validation (§5.3)
- Requirements verification (§6.2)

**MBSE model shows:**
- How these steps connect
- Who is responsible
- What artifacts are produced

---

## 📚 Learning MBSE

### Beginner Path

**Week 1: Learn SysML Basics**
- Study Activity Diagrams
- Study Use Case Diagrams
- Study Requirements Diagrams

**Week 2: Practice**
- Model a simple process (e.g., coffee making)
- Get feedback from peers
- Iterate

**Week 3: Apply to Real Process**
- Choose an ECSS process
- Create initial model
- Validate with stakeholders

### Resources

**Free Training:**
- OMG SysML Tutorial: https://www.omgsysml.org/
- NASA MBSE resources
- ESA MBSE Community

**Books:**
- *A Practical Guide to SysML* - Friedenthal et al.
- *Model-Based Systems Engineering Fundamentals* - Cloutier et al.

**Courses:**
- INCOSE MBSE courses
- ESA Academy MBSE training

---

## 💡 Quick Start Example

### Model Your First Process

**Process: Code Review**

1. **Open your MBSE tool**

2. **Create Activity Diagram**

3. **Add activities:**
   - Submit code for review
   - Assign reviewer
   - Perform review
   - Approve/Request changes
   - Update code
   - Final approval

4. **Add decision points:**
   - Code quality OK?
   - Changes needed?

5. **Add swim lanes:**
   - Developer
   - Reviewer
   - QA Manager

6. **Export diagram** and add to documentation

---

## 🔍 Advanced Topics

### Process Simulation

Use MBSE models to **simulate** process execution:
- Identify bottlenecks
- Optimize workflow
- Predict resource needs

### Requirements Traceability

Use SysML Requirements Diagrams to show:
- ECSS requirement → Process step
- Process step → Artifact produced
- Artifact → Verification method

### Integration with PLM

Connect MBSE models to Product Lifecycle Management (PLM) systems:
- Sync requirements
- Track changes
- Generate reports

---

## ✅ Success Criteria

You've successfully applied MBSE for process engineering when:

- [ ] Process is visualized and understood by all
- [ ] Process changes are tracked in model
- [ ] Process compliance can be verified
- [ ] New team members can learn process from model
- [ ] Process improvements are identified from model

---

## 📞 Getting Help

**Questions about MBSE methodology?**
- GitHub Discussions: Ask the community
- INCOSE MBSE Wiki: Best practices
- ESA MBSE Portal: European space context

---

## 🔗 Related Resources

- [ECSS Standards Guide](ECSS_STANDARDS_GUIDE.md) - How MBSE supports ECSS
- [Quick Start](QUICK_START.md) - Get started quickly
- [Case Studies](CASE_STUDIES.md) - See MBSE in action

---

**Note**: This framework focuses on **process engineering** MBSE. For system design MBSE, see ESA's SysML solution and NASA's MBSE resources.
