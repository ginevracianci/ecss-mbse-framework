# Templates Guide

Detailed guide to using each template in the ECSS-MBSE Framework.

## 📚 Overview

This framework provides ready-to-use templates for:
1. Requirements Specification (ECSS-E-ST-10-02C)
2. Test Plan (ECSS-E-ST-10-03C)
3. Quality Assurance Checklist (ECSS-Q-ST-80C)

Each template is designed to be:
- ✅ ECSS-compliant out of the box
- ✅ Customizable to your project
- ✅ Usable immediately (copy and fill)
- ✅ Educational (with examples and guidance)

---

## 📋 1. Requirements Template

**File**: `templates/requirements/requirements_template.md`  
**Standard**: ECSS-E-ST-10-02C  
**Length**: 15+ pages

### When to Use

Use this template when you need to:
- Write system or subsystem requirements
- Prepare requirements for a design review
- Create baseline requirements documentation
- Comply with ECSS standards for ESA proposals

### Template Structure

| Section | Purpose | Required? |
|---------|---------|-----------|
| 1. Introduction | Context and scope | ✅ Yes |
| 2. Requirements | Actual requirements | ✅ Yes |
| 2.1 Functional | What the system does | ✅ Yes |
| 2.2 Performance | How well it performs | ✅ Yes |
| 2.3 Interface | How it interacts | If applicable |
| 2.4 Operational | How it's operated | If applicable |
| 2.5 Safety | Safety requirements | If safety-critical |
| 2.6 Constraints | Design limitations | If applicable |
| 3. Traceability | Requirements links | ✅ Yes |
| 4. Validation | Quality checks | ✅ Yes |

### How to Use

**Step 1: Copy Template**
```bash
cp templates/requirements/requirements_template.md your_project/requirements.md
```

**Step 2: Fill Document Information**
```markdown
| Field | Value |
|-------|-------|
| **Project Name** | Your Spacecraft Name |
| **Document ID** | REQ-001 |
| **Prepared by** | Your Name, Systems Engineer |
```

**Step 3: Write Requirements**

Use this format:
```markdown
| R-FUNC-001 | The system **shall** [action] [object] [condition] | [Why needed] | Test |
```

**Good Example:**
```markdown
| R-FUNC-001 | The GNC system shall compute trajectory at ≥10 Hz | Real-time control | Test |
```

**Bad Example:**
```markdown
| R-FUNC-001 | The system should be fast enough | Performance | TBD |
```

**Why bad:**
- Uses "should" instead of "shall"
- "Fast enough" is not quantified
- No verification method specified

**Step 4: Establish Traceability**

Link each requirement to:
- Parent requirement (where it came from)
- Design element (what implements it)
- Test case (how it's verified)

**Step 5: Validate Requirements**

Use the checklist in Section 5.1:
- [ ] Necessary
- [ ] Unambiguous
- [ ] Complete
- [ ] Verifiable
- [ ] Traceable

### Common Mistakes to Avoid

❌ **Bundling requirements**
```markdown
The system shall process data quickly and accurately
```
✅ **Split into separate requirements:**
```markdown
R-PERF-001: The system shall process data in ≤100 ms
R-PERF-002: The system shall achieve accuracy ≥99.5%
```

❌ **Using TBD/TBC in baseline**
```markdown
The sensor shall detect objects at TBD meters range
```
✅ **Resolve before baseline:**
```markdown
The sensor shall detect objects ≥0.5 m at ranges up to 100 m
```

---

## 🧪 2. Test Plan Template

**File**: `templates/verification/test_plan_template.md`  
**Standard**: ECSS-E-ST-10-03C  
**Length**: 12+ pages

### When to Use

Use this template when you need to:
- Plan verification activities
- Prepare for test campaigns
- Document test approach for reviews
- Comply with ECSS testing standards

### Template Structure

| Section | Purpose | Required? |
|---------|---------|-----------|
| 1. Introduction | Test scope and approach | ✅ Yes |
| 2. Test Strategy | How testing will be done | ✅ Yes |
| 3. Test Items | What will be tested | ✅ Yes |
| 4. Test Cases | Specific tests | ✅ Yes |
| 5. Test Matrix | Requirements coverage | ✅ Yes |
| 6. Schedule | When tests occur | ✅ Yes |
| 7. Organization | Who does what | ✅ Yes |
| 8. Environment | Test facilities | If applicable |
| 9. Data Management | Results storage | ✅ Yes |
| 10. Entry/Exit Criteria | When to start/stop | ✅ Yes |

### How to Use

**Step 1: Copy Template**
```bash
cp templates/verification/test_plan_template.md your_project/test_plan.md
```

**Step 2: Define Test Levels**

Decide which levels apply:
- [ ] Unit Testing (component level)
- [ ] Integration Testing (interface level)
- [ ] System Testing (end-to-end)
- [ ] Acceptance Testing (customer validation)

**Step 3: Create Test Cases**

For each requirement, define at least one test case:

```markdown
## TC-001: Trajectory Update Rate

**Requirement**: R-FUNC-001  
**Test Level**: System  
**Priority**: Critical

### Objective
Verify GNC computes trajectory at ≥10 Hz

### Test Procedure
1. Initialize GNC system
2. Start trajectory computation
3. Measure update rate for 60 seconds
4. Calculate average rate

### Success Criteria
- Average rate ≥ 10 Hz
- No missed updates
```

**Step 4: Build Test Matrix**

Map requirements to test cases:

| Requirement | Test Case | Method | Status |
|-------------|-----------|--------|--------|
| R-FUNC-001 | TC-001 | Test | Planned |
| R-FUNC-002 | TC-002, TC-003 | Test | Pass |

**Step 5: Set Entry/Exit Criteria**

**Entry Criteria** (before testing):
- [ ] Test plan approved
- [ ] Test environment ready
- [ ] Software baseline available

**Exit Criteria** (testing complete):
- [ ] All tests executed
- [ ] Pass rate ≥95%
- [ ] Critical defects resolved

### Test Case Quality

**Good test case:**
- Clear objective
- Detailed steps (reproducible)
- Quantified pass/fail criteria
- Links to requirements

**Poor test case:**
- Vague objective ("Test the system")
- Subjective criteria ("Works well")
- No requirement link

---

## ✅ 3. QA Checklist Template

**File**: `templates/quality_assurance/qa_checklist_ecss-q-80.md`  
**Standard**: ECSS-Q-ST-80C  
**Length**: 10+ pages

### When to Use

Use this template when you need to:
- Perform quality audits
- Prepare for formal reviews
- Verify ECSS compliance
- Document QA activities

### Template Structure

| Section | Purpose | Items |
|---------|---------|-------|
| 1. Software Management | Planning and organization | 10+ checks |
| 2. Requirements | Software requirements | 6+ checks |
| 3. Design | Architecture and detailed design | 10+ checks |
| 4. Implementation | Coding and review | 15+ checks |
| 5. Verification | Testing at all levels | 15+ checks |
| 6. Documentation | Technical docs | 5+ checks |
| 7. Configuration Mgmt | Baselines and changes | 8+ checks |
| 8. Risk & Safety | Hazards and risks | 5+ checks |

**Total**: 100+ checklist items

### How to Use

**Step 1: Copy Template**
```bash
cp templates/quality_assurance/qa_checklist_ecss-q-80.md your_project/qa_audit.md
```

**Step 2: Perform Audit**

Go through each section and mark:
- ☑ **Pass**: Requirement met
- ☐ **Fail**: Requirement not met
- ☐ **N/A**: Not applicable to this project

**Step 3: Document Findings**

For each failed item:
```markdown
| F-001 | Implementation | Major | Unit test coverage only 65% | Increase to 80% | Dev Team | 2026-02-15 |
```

**Step 4: Track to Closure**

Monitor findings until resolved:
- Critical: Must fix before release
- Major: Should fix before baseline
- Minor: Improvement opportunity

**Step 5: Overall Assessment**

Determine QA status:
- ✅ **PASS**: All critical items pass
- ⚠️ **CONDITIONAL**: Minor findings acceptable
- ❌ **FAIL**: Critical findings exist

### Customization

**For Small Projects:**
- Focus on Sections 2, 4, 5 (Requirements, Implementation, Verification)
- Mark irrelevant sections as N/A

**For Large Projects:**
- Use all sections
- Add project-specific checks
- Assign different auditors per section

---

## 🎯 Template Customization Guide

### General Principles

**DO customize:**
- ✅ Project-specific terminology
- ✅ Company/organization names
- ✅ Additional sections if needed
- ✅ Examples to match your domain

**DON'T remove:**
- ❌ ECSS compliance sections
- ❌ Required validation criteria
- ❌ Traceability mechanisms
- ❌ Quality checks

### Adaptation Process

**Step 1: Review Template**
- Read through entire template
- Understand each section's purpose
- Note sections that don't apply

**Step 2: Tailor to Project**
- Add project-specific sections
- Remove N/A sections (document why)
- Adjust examples to your domain

**Step 3: Validate Tailoring**
- Ensure ECSS compliance maintained
- Get stakeholder buy-in
- Document tailoring decisions

**Step 4: Use Consistently**
- Train team on template
- Use for all similar projects
- Collect lessons learned

---

## 💡 Tips & Tricks

### Requirements Template

**Tip 1**: Start simple
- Write 5-10 high-level requirements first
- Get reviewed
- Decompose into detailed requirements

**Tip 2**: Use examples
- Look at heritage missions
- Adapt successful patterns
- Cite sources for derived requirements

**Tip 3**: Maintain traceability from day 1
- Don't wait until later
- Use simple spreadsheet if needed
- Update as requirements evolve

### Test Plan Template

**Tip 1**: Test early and often
- Don't wait for complete implementation
- Use stubs and mocks
- Iterative testing approach

**Tip 2**: Automate where possible
- Unit tests automated
- Regression tests automated
- Manual tests for integration/system

**Tip 3**: Plan for failures
- Include off-nominal test cases
- Test error handling
- Document failure modes

### QA Checklist Template

**Tip 1**: Schedule regular audits
- Don't wait for problems
- Quarterly audits for long projects
- Track trends over time

**Tip 2**: Be objective
- Evidence-based assessment
- Don't skip difficult checks
- Document everything

**Tip 3**: Learn from findings
- Root cause analysis
- Process improvements
- Share lessons learned

---

## 🔗 Template Relationships

### How Templates Work Together

```
Requirements Template
    ↓ (defines what to verify)
Test Plan Template
    ↓ (executed and audited by)
QA Checklist Template
    ↓ (ensures compliance to)
ECSS Standards
```

**Example workflow:**
1. Write requirements using Requirements Template
2. Create test plan using Test Plan Template
3. Execute tests
4. Audit using QA Checklist Template
5. Document compliance

---

## 📚 Additional Resources

### Template Examples

See complete examples in:
- [GNC System Case Study](../examples/gnc_system/ECSS_COMPLIANCE_CASE_STUDY.md)
- [CubeSat Example](../examples/cubesat_mission/) *(coming soon)*

### Related Guides

- [ECSS Standards Guide]- Understand the standards
- [Quick Start] - Get started quickly
- [MBSE Methodology] - Use MBSE with templates

---

## ❓ FAQ

**Q: Can I use these templates for non-space projects?**  
A: Yes! ECSS principles apply to any complex system. Adapt terminology as needed.

**Q: Do I need to use all sections?**  
A: No. Mark irrelevant sections as "N/A" and document why.

**Q: Can I modify the templates?**  
A: Yes, but maintain ECSS compliance. Document any deviations.

**Q: How do I handle TBD items?**  
A: Track them in Open Items section. Resolve before baseline.

**Q: Can I combine templates?**  
A: Yes, for small projects. Keep requirements/testing separate for large projects.

---

**Need help?** Open an issue on GitHub or check the [Quick Start Guide].
