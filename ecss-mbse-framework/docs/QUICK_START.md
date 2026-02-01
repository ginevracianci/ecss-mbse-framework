# Quick Start Guide

Get started with the ECSS-MBSE Framework in 10 minutes.

## 🎯 What You'll Learn

By the end of this guide, you'll be able to:
- ✅ Set up the framework for your project
- ✅ Use templates to create ECSS-compliant documentation
- ✅ Run automated compliance checks
- ✅ Generate requirements traceability matrices

---

## ⚡ 5-Minute Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/ginevracianci/ecss-mbse-framework.git
cd ecss-mbse-framework
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Use Your First Template

Copy the requirements template to your project:

```bash
# Create your project directory
mkdir my_space_project
cd my_space_project

# Copy requirements template
cp ../templates/requirements/requirements_template.md ./requirements.md
```

### 4. Fill in Your Requirements

Open `requirements.md` and start adding your project-specific requirements:

```markdown
## 2.1 Functional Requirements

| Requirement ID | Requirement Statement | Rationale | Verification Method |
|----------------|----------------------|-----------|---------------------|
| R-FUNC-001 | The system shall compute trajectory at ≥10 Hz | Real-time control | Test |
| R-FUNC-002 | The system shall detect obstacles at 100m range | Safety | Test |
```

### 5. Check Compliance

Run the automated compliance checker:

```bash
cd ..
python tools/compliance_checker.py my_space_project/
```

**Output:**
```
🔍 Checking ECSS compliance for: my_space_project
============================================================

📋 Checking Requirements (ECSS-E-ST-10-02C)...
  ✓ Checked requirements.md

🔗 Checking Requirements Traceability...
  ⚠️  No traceability matrix found

🧪 Checking Test Coverage (ECSS-E-ST-10-03C)...
  ⚠️  No test plan document found

============================================================
📊 COMPLIANCE CHECK SUMMARY
============================================================

🟡 MAJOR Issues: 2
  ⚠️  Traceability: No traceability matrix found
     ECSS: ECSS-E-ST-10-02C § 5.2.3
  ⚠️  Verification: No test plan document found
     ECSS: ECSS-E-ST-10-03C § 5.4.1

============================================================
⚠️  CONDITIONAL PASS - Major issues should be addressed
============================================================
```

---

## 📚 Complete Workflow

### Step 1: Requirements Phase

**1.1 Create Requirements Specification**

```bash
cp templates/requirements/requirements_template.md your_project/requirements.md
```

**1.2 Fill in Requirements**

Follow the template structure:
- Section 2.1: Functional Requirements
- Section 2.2: Performance Requirements
- Section 2.3: Interface Requirements
- Section 2.4: Operational Requirements
- Section 2.5: Safety Requirements

**Example:**
```markdown
| R-FUNC-001 | The GNC system shall compute trajectory corrections with update rate ≥ 10 Hz during rendezvous phase. | Real-time control needed | Test |
```

**1.3 Validate Requirements**

Use the validation checklist in the template (Section 5.1):
- [ ] Necessary
- [ ] Unambiguous
- [ ] Complete
- [ ] Consistent
- [ ] Verifiable
- [ ] Traceable
- [ ] Feasible

---

### Step 2: Verification Planning

**2.1 Create Test Plan**

```bash
cp templates/verification/test_plan_template.md your_project/test_plan.md
```

**2.2 Map Requirements to Tests**

Fill in the test matrix (Section 5.1):

```markdown
| Requirement ID | Requirement Description | Test Case(s) | Verification Method | Priority | Status |
|----------------|------------------------|--------------|---------------------|----------|--------|
| R-FUNC-001 | Trajectory update rate ≥10 Hz | TC-001 | Test | Critical | Planned |
```

**2.3 Define Test Cases**

Use the test case template (Section 4.2):

```markdown
## TC-001: Trajectory Update Rate Test

**Requirement**: R-FUNC-001  
**Test Level**: System  
**Priority**: Critical

### Objective
Verify GNC system computes trajectory updates at ≥10 Hz

### Test Procedure
1. Initialize GNC system
2. Start trajectory computation
3. Measure update rate over 60 seconds
4. Verify rate ≥ 10 Hz

### Success Criteria
- Update rate ≥ 10 Hz for 100% of measurement period
```

---

### Step 3: Quality Assurance

**3.1 Run QA Checklist**

```bash
cp templates/quality_assurance/qa_checklist_ecss-q-80.md your_project/qa_checklist.md
```

**3.2 Complete Checklist**

Go through each section and mark items:
- ☑ Pass
- ☐ Fail
- ☐ N/A

**3.3 Document Findings**

Record non-conformances in Section 10.2:

```markdown
| NC-001 | Unit test coverage only 65% (target: 80%) | 5.5.2 | Increase coverage | Open |
```

---

### Step 4: Automated Compliance

**4.1 Run Compliance Checker**

```bash
python tools/compliance_checker.py your_project/
```

**4.2 Generate Report**

```bash
python tools/compliance_checker.py your_project/ --report compliance_report.md
```

**4.3 Address Issues**

Review the report and fix identified issues:
- **Critical**: Must fix before release
- **Major**: Should fix before baseline
- **Minor**: Recommended improvements

---

## 🎓 Learning Path

### For Beginners

**Day 1: Understand Templates**
1. Read through requirements_template.md
2. Review examples in Appendix A
3. Look at good/bad requirements examples

**Day 2: Practice**
1. Create a simple project (e.g., "Coffee Machine Controller")
2. Write 5-10 requirements using the template
3. Run compliance checker

**Day 3: Expand**
1. Add test plan
2. Create test cases for your requirements
3. Run compliance checker again

### For Experienced Engineers

**Hour 1: Template Customization**
1. Review templates
2. Adapt to your project needs
3. Add project-specific sections

**Hour 2: Integration**
1. Integrate templates into existing project structure
2. Map existing documentation to ECSS structure
3. Run compliance checker to identify gaps

**Hour 3: Automation**
1. Set up automated compliance checking in CI/CD
2. Configure quality gates
3. Generate reports automatically

---

## 💡 Common Use Cases

### Use Case 1: New Space Project

**Scenario**: Starting a CubeSat mission from scratch

**Steps:**
1. Copy all templates to project folder
2. Fill in requirements based on mission objectives
3. Define verification approach in test plan
4. Set up QA checklist for reviews

**Timeline**: 2-3 days for initial documentation

---

### Use Case 2: Existing Project Compliance

**Scenario**: Need to make existing project ECSS-compliant

**Steps:**
1. Run compliance checker on existing docs
2. Review identified gaps
3. Use templates to fill missing documentation
4. Update existing docs to match ECSS structure

**Timeline**: 1-2 weeks depending on project size

---

### Use Case 3: Proposal Preparation

**Scenario**: Writing ESA proposal, need ECSS compliance

**Steps:**
1. Use requirements template for technical requirements section
2. Reference ECSS standards using provided clause numbers
3. Include test plan outline from template
4. Show QA approach using checklist

**Timeline**: 3-5 days for ECSS-compliant proposal sections

---

## 🔧 Tips & Best Practices

### Requirements Writing

**DO:**
- ✅ Use "shall" for mandatory requirements
- ✅ Include quantitative values with tolerances
- ✅ Make each requirement independently testable
- ✅ Assign unique IDs (e.g., R-FUNC-001)

**DON'T:**
- ❌ Use "should" or "will" for requirements
- ❌ Bundle multiple requirements in one statement
- ❌ Use vague terms like "fast enough" or "user-friendly"
- ❌ Leave TBD/TBC in baselined documents

### Test Planning

**DO:**
- ✅ Map every requirement to at least one test case
- ✅ Define clear pass/fail criteria
- ✅ Include both nominal and off-nominal scenarios
- ✅ Plan for regression testing

**DON'T:**
- ❌ Skip requirements coverage check
- ❌ Use subjective success criteria
- ❌ Forget to document test environment setup
- ❌ Ignore failed test cases

### Quality Assurance

**DO:**
- ✅ Perform regular QA reviews
- ✅ Document all findings
- ✅ Track non-conformances to closure
- ✅ Update checklist as project evolves

**DON'T:**
- ❌ Skip QA activities due to schedule pressure
- ❌ Accept critical findings without resolution
- ❌ Use checklist as simple checkbox exercise
- ❌ Ignore minor findings indefinitely

---

## 📊 Metrics to Track

Monitor these metrics for project health:

| Metric | Target | Tool |
|--------|--------|------|
| Requirements Coverage | 100% | Compliance checker |
| Requirements with TBD/TBC | 0 (at baseline) | Manual review |
| Test Pass Rate | ≥95% | Test execution |
| QA Checklist Completion | 100% | QA audit |
| Critical Findings Open | 0 | Issue tracker |

---

## 🚨 Troubleshooting

### "Compliance checker finds too many issues"

**Solution**: This is normal for first run. Address issues in order:
1. Critical issues first
2. Major issues next
3. Minor issues as time permits

### "Templates are too detailed for my project"

**Solution**: Templates are comprehensive - use what you need:
- Small projects: Focus on core sections
- Large projects: Use full template
- Adapt templates to your context

### "Don't understand ECSS clauses"

**Solution**: 
1. Read [ECSS Standards Guide](ECSS_STANDARDS_GUIDE.md)
2. Check ECSS website: https://ecss.nl/
3. Templates include examples for guidance

---

## 📖 Next Steps

After completing this quick start:

1. **Read detailed documentation**
   - [ECSS Standards Guide](ECSS_STANDARDS_GUIDE.md)
   - [MBSE Methodology](MBSE_METHODOLOGY.md)
   - [Templates Guide](ecss-mbse-framework/templates/TEMPLATES_GUIDE.md)

2. **Explore examples**
   - [CubeSat Mission Example](../examples/cubesat_mission/)
   - [GNC System Example](../examples/gnc_system/)

3. **Try advanced features**
   - MBSE process modeling
   - Requirements traceability automation
   - CI/CD integration

4. **Contribute**
   - Share your templates
   - Submit improvements
   - Report issues

---

## 🤝 Getting Help

- **GitHub Issues**: Report bugs or request features
- **Discussions**: Ask questions and share experiences
- **LinkedIn**: Connect with the community

---

## ✅ Checklist: You're Ready When...

- [ ] You can create a requirements specification from template
- [ ] You understand how to write ECSS-compliant requirements
- [ ] You can run the compliance checker
- [ ] You know how to interpret compliance reports
- [ ] You can create test cases for requirements
- [ ] You understand the QA checklist sections

---

**🎉 Congratulations!** You're now ready to apply ECSS standards using this framework.

For questions or support, open an issue on GitHub or connect on LinkedIn.

---

**Next recommended reading**: [ECSS Standards Guide](ECSS_STANDARDS_GUIDE.md)
