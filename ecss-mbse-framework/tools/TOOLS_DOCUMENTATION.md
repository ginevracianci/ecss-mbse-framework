# Tools Documentation

Complete guide to using the automation tools in the ECSS-MBSE Framework.

## 🛠️ Available Tools

| Tool | Purpose | Language | Status |
|------|---------|----------|--------|
| **compliance_checker.py** | Automated ECSS compliance verification | Python | ✅ Available |
| **requirements_tracer.py** | Requirements traceability automation | Python | 🔄 Coming soon |
| **report_generator.py** | Documentation report generation | Python | 🔄 Coming soon |

---

## 1. ECSS Compliance Checker

**File**: `tools/compliance_checker.py`  
**Purpose**: Automated verification of ECSS standards compliance  
**Standards Checked**: ECSS-E-ST-10-02C, ECSS-E-ST-10-03C, ECSS-Q-ST-80C

### Installation

```bash
# Install dependencies
pip install -r requirements.txt

# Verify installation
python tools/compliance_checker.py --version
```

### Basic Usage

```bash
# Check current directory
python tools/compliance_checker.py .

# Check specific project
python tools/compliance_checker.py /path/to/project

# Generate detailed report
python tools/compliance_checker.py /path/to/project --report compliance_report.md
```

### What It Checks

#### Requirements Compliance (ECSS-E-ST-10-02C)

- ✅ Requirements specification exists
- ✅ Requirements use "shall" for mandatory items
- ✅ Requirements have unique IDs
- ✅ No TBD/TBC in baseline
- ✅ Verification methods specified

#### Test Coverage (ECSS-E-ST-10-03C)

- ✅ Test plan document exists
- ✅ Test cases defined
- ✅ Requirements-to-tests traceability

#### Documentation Completeness

- ✅ README exists
- ✅ Requirements documentation
- ✅ Design documentation
- ✅ Test documentation

### Output Format

```
🔍 Checking ECSS compliance for: my_project
============================================================

📋 Checking Requirements (ECSS-E-ST-10-02C)...
  ✓ Checked requirements.md

🔗 Checking Requirements Traceability...
  ⚠️  No traceability matrix found

============================================================
📊 COMPLIANCE CHECK SUMMARY
============================================================

🔴 CRITICAL Issues: 0
🟡 MAJOR Issues: 1
  ⚠️  Traceability: No traceability matrix found
     File: /path/to/project
     ECSS: ECSS-E-ST-10-02C § 5.2.3

🔵 MINOR Issues: 2

============================================================
⚠️  CONDITIONAL PASS - Major issues should be addressed
============================================================
```

### Issue Severity Levels

| Severity | Definition | Action Required |
|----------|------------|-----------------|
| **Critical** | Non-compliance with mandatory requirements | Must fix before release |
| **Major** | Significant gap, workaround possible | Should fix before baseline |
| **Minor** | Documentation or process improvement | Recommended enhancement |

### Example Use Cases

#### Use Case 1: Pre-Review Check

Before a design review:

```bash
python tools/compliance_checker.py . --report pre_review_compliance.md
```

Review the report and fix critical/major issues before the meeting.

#### Use Case 2: Continuous Integration

Add to CI/CD pipeline:

```yaml
# .github/workflows/ecss-compliance.yml
name: ECSS Compliance Check

on: [push, pull_request]

jobs:
  compliance:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Check ECSS Compliance
        run: python tools/compliance_checker.py .
```

#### Use Case 3: Regular Audits

Monthly compliance check:

```bash
python tools/compliance_checker.py . --report "compliance_$(date +%Y-%m).md"
```

Track compliance trends over time.

### Advanced Options

#### Filter by Severity

```python
# In Python script
checker = ECSSComplianceChecker(project_path)
results = checker.check_all()

# Only show critical issues
critical_issues = [i for i in checker.issues if i.severity == 'critical']
```

#### Custom Checks

Extend the checker with project-specific checks:

```python
class CustomComplianceChecker(ECSSComplianceChecker):
    def check_project_specific(self):
        # Your custom checks
        if not Path('project_plan.md').exists():
            self.issues.append(ComplianceIssue(
                severity='major',
                category='Documentation',
                description='Project plan missing',
                file_path=str(self.project_path)
            ))
```

### Troubleshooting

**Issue**: "No requirements found"
- **Solution**: Ensure requirements file matches pattern `*requirements*.md`

**Issue**: "Permission denied"
- **Solution**: Check file permissions, run with appropriate user

**Issue**: "Module not found"
- **Solution**: Install dependencies: `pip install -r requirements.txt`

---

## 2. Requirements Tracer *(Coming Soon)*

**Status**: Under development  
**Expected**: March 2025

### Planned Features

- Automatic traceability matrix generation
- Bidirectional requirement tracing
- Coverage analysis
- Export to Excel/CSV

### Preview Usage

```bash
python tools/requirements_tracer.py requirements.md --output trace_matrix.xlsx
```

---

## 3. Report Generator *(Coming Soon)*

**Status**: Under development  
**Expected**: April 2025

### Planned Features

- Automated documentation generation
- PDF/HTML report output
- Template-based formatting
- Metrics dashboard

### Preview Usage

```bash
python tools/report_generator.py --project . --output verification_report.pdf
```

---

## 🔧 Tool Development

### Contributing Tools

Want to add a new tool? Follow these guidelines:

**1. Tool Structure**
```python
#!/usr/bin/env python3
"""
Tool Name - Brief description

Author: Your Name
License: MIT
"""

import argparse
from pathlib import Path

def main():
    parser = argparse.ArgumentParser(description='Tool description')
    # Add arguments
    args = parser.parse_args()
    # Tool logic
    
if __name__ == '__main__':
    main()
```

**2. Documentation**
- Docstrings for all functions
- Usage examples in header
- README update

**3. Testing**
- Unit tests in `tests/`
- Example usage in `examples/`

**4. Integration**
- Add to `requirements.txt`
- Update this documentation
- Add to main README

---

## 📊 Tool Roadmap

### Short Term (Q1 2025)
- ✅ Compliance Checker v1.0
- 🔄 Requirements Tracer v1.0
- 🔄 Report Generator v1.0

### Medium Term (Q2 2025)
- 📋 Verification Matrix Generator
- 📋 MBSE Model Validator
- 📋 Metrics Dashboard

### Long Term (Q3+ 2025)
- 📋 AI-powered requirement quality checker
- 📋 Automated test case generation
- 📋 Integration with JIRA/GitHub Issues

---

## 🎓 Best Practices

### Tool Usage

**DO:**
- ✅ Run compliance checker before commits
- ✅ Integrate tools in CI/CD
- ✅ Review tool outputs, don't blindly trust
- ✅ Use reports for process improvement

**DON'T:**
- ❌ Ignore tool warnings
- ❌ Bypass checks to save time
- ❌ Modify tool output to look better
- ❌ Use tools as replacement for reviews

### Tool Maintenance

**Keep tools updated:**
```bash
# Pull latest version
git pull origin main

# Update dependencies
pip install -r requirements.txt --upgrade
```

**Report issues:**
- GitHub Issues for bugs
- Feature requests welcome
- Contribute fixes via PR

---

## 🔗 Related Documentation

- [Quick Start Guide] - Get started with tools
- [Templates Guide] - What tools check against
- [ECSS Standards Guide] - Standards background

---

## 📞 Support

**Questions about tools?**
- Check existing GitHub Issues
- Open new issue with [Tool] prefix
- Include error messages and context

**Want to contribute?**
- See [CONTRIBUTING.md](../CONTRIBUTING.md)
- Fork repository
- Submit pull request

---

**Last Updated**: February 2026  
**Version**: 1.0.0
