# Contributing to ECSS-MBSE Framework

Thank you for your interest in contributing to the ECSS-MBSE Framework! This document provides guidelines for contributing to make the process smooth and effective for everyone.

## 🎯 Ways to Contribute

There are many ways to contribute to this project:

### 1. **Share Your Templates** 📋
Have you created ECSS-compliant templates for other standards or domains?
- Project management templates
- Risk management templates
- Configuration management templates
- Domain-specific adaptations (CubeSats, launchers, etc.)

### 2. **Improve Existing Templates** ✏️
Found ways to make templates better?
- Add examples
- Clarify instructions
- Fix errors or inconsistencies
- Improve ECSS compliance

### 3. **Add Tools** 🛠️
Build automation tools to help the community:
- Requirements traceability tools
- Report generators
- Compliance checkers for other ECSS standards
- Integration with other tools (JIRA, GitHub, etc.)

### 4. **Submit Case Studies** 📚
Applied the framework to your project?
- Share your experience
- Document lessons learned
- Help others learn from your work
- Anonymize if needed for proprietary projects

### 5. **Improve Documentation** 📖
Help make the framework easier to use:
- Fix typos or unclear explanations
- Add tutorials or guides
- Translate documentation (coming soon)
- Create video tutorials

### 6. **Report Issues** 🐛
Found a problem?
- Template errors
- Tool bugs
- Documentation issues
- ECSS standard misinterpretations

### 7. **Suggest Features** 💡
Have ideas for improvements?
- New templates
- Tool enhancements
- Better workflows
- Integration possibilities

---

## 🚀 Getting Started

### Prerequisites

Before contributing, make sure you have:

- [ ] GitHub account
- [ ] Git installed locally
- [ ] Python 3.8+ (for tool development)
- [ ] Understanding of ECSS standards (or willingness to learn)
- [ ] Familiarity with Markdown for documentation

### Setting Up Your Environment

```bash
# Fork the repository on GitHub

# Clone your fork
git clone https://github.com/YOUR-USERNAME/ecss-mbse-framework.git
cd ecss-mbse-framework

# Add upstream remote
git remote add upstream https://github.com/ginevracianci/ecss-mbse-framework.git

# Create a branch for your contribution
git checkout -b feature/your-feature-name

# Install dependencies (for tool development)
pip install -r requirements.txt
```
### Dev setup

```bash
python -m pip install -r requirements.txt -r requirements-dev.txt -c constraints.txt
pre-commit install
```

### Run tests

```bash
python -m pytest -q
```

### CI workflow (brief)

The `python-tests` workflow runs on `pull_request` and on `push` to `main`.
It installs dependencies with `constraints.txt`, runs `pre-commit`, and then
executes `python -m pytest -q`.

---

## 📝 Contribution Guidelines

### Code of Conduct

This project follows a **be kind and professional** approach:

- ✅ Be respectful and constructive
- ✅ Welcome newcomers and help them learn
- ✅ Focus on improving the framework
- ✅ Give credit where credit is due
- ❌ No harassment, discrimination, or unprofessional behavior

### Git Workflow

**1. Keep your fork updated:**
```bash
git fetch upstream
git checkout main
git merge upstream/main
```

**2. Create feature branch:**
```bash
git checkout -b feature/descriptive-name
```

**3. Make your changes:**
- Follow existing style and structure
- Test your changes
- Document what you've added

**4. Commit with clear messages:**
```bash
git add .
git commit -m "Add: Brief description of what you added

Detailed explanation if needed:
- What changed
- Why it changed
- Any relevant context"
```

**5. Push to your fork:**
```bash
git push origin feature/descriptive-name
```

**6. Open Pull Request:**
- Go to GitHub
- Click "New Pull Request"
- Fill in the template (see below)
- Wait for review

---

## 📋 Pull Request Process

### PR Template

When submitting a PR, include:

```markdown
## Description
Brief description of what this PR does

## Type of Change
- [ ] New template
- [ ] Template improvement
- [ ] New tool
- [ ] Tool bug fix
- [ ] Documentation update
- [ ] Case study
- [ ] Other (specify)

## Changes Made
- Detailed list of changes
- What files were modified
- Any new dependencies

## Testing Done
- How you tested the changes
- What scenarios were covered
- Any edge cases considered

## ECSS Compliance
- [ ] Changes maintain ECSS compliance
- [ ] Relevant standard clauses referenced
- [ ] Template follows existing structure

## Checklist
- [ ] Code follows project style
- [ ] Documentation updated
- [ ] Examples provided (if applicable)
- [ ] Self-reviewed the changes
- [ ] Ready for review
```

### Review Process

1. **Maintainer review**: Usually within 3-5 days
2. **Feedback**: Address any requested changes
3. **Approval**: Maintainer approves PR
4. **Merge**: Changes merged to main branch
5. **Credit**: You'll be added to contributors list

---

## 🎨 Style Guidelines

### Templates

**Format:**
- Use Markdown (.md)
- Follow ECSS standard structure
- Include examples
- Provide clear instructions

**Structure:**
```markdown
# Template Title

**ECSS Standard**: ECSS-X-ST-XX-XXC
**Version**: 1.0
**Date**: YYYY-MM-DD

## Document Information
[Table with project details]

## 1. Introduction
[Purpose, scope, definitions]

## 2. Main Content
[Template-specific sections]

## Appendices
[Examples, references]
```

**Quality criteria:**
- Clear and unambiguous
- ECSS-compliant
- Includes examples
- Has validation checklist
- Professional formatting

### Tools

**Code style:**
- Follow PEP 8 for Python
- Use type hints
- Add docstrings
- Include error handling

**Example:**
```python
#!/usr/bin/env python3
"""
Tool Name - Brief description

Based on ECSS-X-ST-XX-XXC standard

Author: Your Name
License: MIT
"""

from pathlib import Path
from typing import List, Dict

def function_name(param: str) -> Dict[str, str]:
    """
    Brief description of function
    
    Args:
        param: Description of parameter
        
    Returns:
        Description of return value
        
    Raises:
        ValueError: When something goes wrong
    """
    # Implementation
    pass
```

**Testing:**
- Unit tests for all functions
- Test both success and failure cases
- Use pytest
- Aim for >80% coverage

### Documentation

**Markdown style:**
- Use headers hierarchically (h1 → h2 → h3)
- Include code examples
- Add links to related docs
- Use tables for structured data
- Include emojis sparingly for visual clarity

**Example structure:**
```markdown
# Main Title

Brief introduction

## Section 1

Content with examples

### Subsection

Details

## Section 2

More content
```

---

## 🧪 Testing Contributions

### Template Testing

Before submitting template changes:

1. **Fill out the template** completely
2. **Run compliance checker** if applicable
3. **Peer review** with colleague
4. **Verify ECSS compliance** against standard
5. **Test usability** - can someone else use it?

### Tool Testing

Before submitting tool changes:

1. **Run existing tests:**
```bash
python -m pytest -q
```

2. **Add new tests** for your changes

3. **Test manually** with example projects

4. **Check for edge cases**

5. **Verify error handling**

### Documentation Testing

Before submitting documentation:

1. **Check all links** are valid
2. **Verify code examples** work
3. **Read from user perspective** - is it clear?
4. **Check formatting** renders correctly
5. **Spell check**

---

## 📚 Specific Contribution Types

### Adding a New Template

**Process:**

1. **Research the ECSS standard** thoroughly
2. **Create template file** in appropriate directory:
   ```
   templates/[category]/[standard_name]_template.md
   ```
3. **Follow existing template structure**
4. **Include at least 3 examples**
5. **Add to Templates Guide** documentation
6. **Update main README** with template reference
7. **Create example usage** in examples/

**Required sections:**
- Document Information
- Introduction
- Main content per ECSS standard
- Validation criteria
- ECSS compliance matrix

### Adding a New Tool

**Process:**

1. **Define tool purpose** clearly
2. **Create tool file:**
   ```
   tools/[tool_name].py
   ```
3. **Add command-line interface** with argparse
4. **Include help text** and examples
5. **Add tests** in tests/
6. **Update TOOLS_DOCUMENTATION.md**
7. **Add to requirements.txt** if dependencies needed

**Required features:**
- Command-line arguments
- Help text (--help)
- Error handling
- Progress indication
- Output formatting

### Adding a Case Study

**Process:**

1. **Get approval** (open issue first to discuss)
2. **Anonymize** if needed (company names, etc.)
3. **Create case study file:**
   ```
   examples/[project_name]/CASE_STUDY.md
   ```
4. **Follow case study template**
5. **Include metrics** and results
6. **Share lessons learned**
7. **Update CASE_STUDIES.md** index

**Required content:**
- Project overview
- ECSS standards applied
- Challenges and solutions
- Results/metrics
- Lessons learned
- Artifacts (templates used, reports, etc.)

---

## 🏆 Recognition

### Contributors

All contributors are recognized in:
- **README.md** contributors section
- **Release notes** for their contributions
- **GitHub contributors** page

### Significant Contributions

Major contributions may result in:
- Co-author credit on specific documents
- Feature announcements
- LinkedIn mentions (with permission)

---

## 📞 Getting Help

### Questions?

- **GitHub Discussions**: For general questions
- **GitHub Issues**: For specific problems
- **Email**: ginevra.cianci@gmail.it (maintainer)

### Learning ECSS

New to ECSS standards?

- Read [ECSS Standards Guide](docs/ECSS_STANDARDS_GUIDE.md)
- Check [Quick Start Guide](docs/QUICK_START.md)
- Review existing templates
- Ask questions in Discussions

---

## 🔄 Review Timeline

What to expect:

| Action | Typical Timeline |
|--------|-----------------|
| Issue response | 1-3 days |
| PR initial review | 3-5 days |
| PR approval/merge | 5-10 days |
| Feature discussion | Ongoing |

**Note**: These are estimates. Complex contributions may take longer.

---

## 📜 License

By contributing, you agree that your contributions will be licensed under the MIT License.

All contributions must be:
- ✅ Your original work
- ✅ Compatible with MIT License
- ✅ Free of proprietary/confidential information
- ✅ Free of third-party copyrights

---

## 🎯 Contribution Ideas

Not sure where to start? Try these:

### Quick Contributions (< 1 hour)
- Fix typos in documentation
- Improve examples in templates
- Add ECSS clause references
- Update links

### Medium Contributions (1-5 hours)
- Add template for new ECSS standard
- Improve compliance checker
- Write tutorial or guide
- Create case study

### Large Contributions (5+ hours)
- Build new automation tool
- Comprehensive template suite
- MBSE process model library
- Multi-language documentation

---

## ✅ Final Checklist

Before submitting your contribution:

- [ ] Changes follow project style
- [ ] ECSS compliance maintained
- [ ] Documentation updated
- [ ] Tests added/passing
- [ ] Examples provided
- [ ] PR template filled
- [ ] Self-reviewed
- [ ] Commit messages clear

---

## 🙏 Thank You!

Your contributions help the aerospace community apply ECSS standards more effectively. Every contribution, no matter how small, makes a difference.

**Questions about contributing?** Open an issue or discussion - we're here to help!

---

**Maintained by**: Ginevra Cianci  
**Contact**: ginevra.cianci@gmail.it  
**GitHub**: [@ginevracianci](https://github.com/ginevracianci)
