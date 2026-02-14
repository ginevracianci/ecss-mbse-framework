# ECSS-MBSE Application Framework

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![ECSS](https://img.shields.io/badge/Standards-ECSS-red.svg)]()
[![MBSE](https://img.shields.io/badge/Methodology-MBSE-orange.svg)]()
[![SysML](https://img.shields.io/badge/Language-SysML-blue.svg)]()
[![Release](https://img.shields.io/github/v/release/ginevracianci/ecss-mbse-framework)](https://github.com/ginevracianci/ecss-mbse-framework/releases)  
[![Python Tests](https://github.com/ginevracianci/ecss-mbse-framework/actions/workflows/python-tests.yml/badge.svg)](https://github.com/ginevracianci/ecss-mbse-framework/actions/workflows/python-tests.yml)

> **Practical framework for applying ECSS standards using Model-Based Systems Engineering (MBSE) methodology**

A comprehensive collection of ready-to-use templates, process models, and automation tools for aerospace systems engineering following European Cooperation for Space Standardization (ECSS) guidelines.

![Framework Overview](ecss-mbse-framework/docs/images/framework_overview.png)

## 🎯 What Is This?

This framework helps aerospace engineers apply ECSS standards in real projects by providing:

- **📋 Ready-to-Use Templates** - ECSS-compliant templates for requirements, testing, QA, and project management
- **🎨 MBSE Process Models** - SysML diagrams for engineering processes (not just system design)
- **🛠️ Automation Tools** - Python scripts for compliance checking and traceability management
- **📚 Practical Examples** - Real case studies showing complete ECSS application 

## 🌟 Why This Framework?

**The Problem:**
ECSS standards are comprehensive but often difficult to apply in practice. Engineers know *what* the standards require but struggle with *how* to implement them efficiently.

**The Solution:**
This framework bridges the gap between ECSS theory and practice by providing:
- Practical templates you can use immediately
- Process automation to reduce manual work
- MBSE methodology to manage complexity
- Real examples from space missions

## 🚀 Quick Start

### For Requirements Management
```bash
# 1. Copy the requirements template
cp templates/requirements/requirements_template.md your_project/

# 2. Fill in your requirements following ECSS-E-ST-10-02C structure

# 3. Use the traceability tool
python tools/requirements_tracer.py your_project/requirements.md
```

### For Test Planning
```bash
# 1. Copy the test plan template
cp templates/verification/test_plan_template.md your_project/

# 2. Define test cases following ECSS-E-ST-10-03C

# 3. Generate verification matrix
python tools/report_generator.py --verification your_project/
```

### For Quality Assurance
```bash
# 1. Use the QA checklist
cp templates/quality_assurance/qa_checklist_ecss-q-80.md your_project/

# 2. Run compliance checker
python tools/compliance_checker.py your_project/
```

## 📦 What's Included

### 1. Templates Library

| Category | Template | ECSS Standard | Description |
|----------|----------|---------------|-------------|
| **Requirements** | Requirements Specification | ECSS-E-ST-10-02C | Complete requirements template with traceability |
| | Requirements Traceability Matrix | ECSS-E-ST-10-02C | Excel template for tracking requirements |
| | Requirements Review Checklist | ECSS-E-ST-10-02C | Peer review checklist |
| **Verification** | Test Plan | ECSS-E-ST-10-03C | Comprehensive test planning template |
| | Verification Matrix | ECSS-E-ST-10-03C | Map requirements to test cases |
| | Test Procedure | ECSS-E-ST-10-03C | Detailed test execution template |
| **Quality** | QA Checklist | ECSS-Q-ST-80C | Software product assurance checklist |
| | Code Review Template | ECSS-Q-ST-80C | Structured code review form |
| | Audit Report | ECSS-Q-ST-80C | Quality audit documentation |
| **Project Mgmt** | Project Plan | ECSS-M-ST-10C | Project planning and implementation |
| | Risk Register | ECSS-M-ST-10C | Risk management tracking |
| | Milestone Tracker | ECSS-M-ST-10C | Project milestone management |

### 2. MBSE Process Models

Process engineering using SysML for:

- **Requirements Engineering Process** - Complete workflow from stakeholder needs to verified requirements
- **Verification & Validation Flow** - Test planning, execution, and reporting process
- **Configuration Control Process** - Change management and baseline control
- **Quality Assurance Gates** - QA checkpoints throughout project lifecycle

**Methodology**: All process models follow ESA's MBSE adoption guidelines and use ECSS-compliant terminology.

### 3. Automation Tools

| Tool | Purpose | Input | Output |
|------|---------|-------|--------|
| `compliance_checker.py` | Verify ECSS compliance | Project files | Compliance report |
| `requirements_tracer.py` | Check requirements traceability | Requirements docs | Traceability matrix |
| `report_generator.py` | Auto-generate documentation | Project data | PDF/Excel reports |

### 4. Case Studies

| Project | Domain | Standards Applied | Status |
|---------|--------|-------------------|--------|
| **CubeSat Mission** | Small satellite | ECSS-E-ST-10-02C, 10-03C | ✅ Complete |
| **GNC System** | Asteroid exploration | ECSS-E-ST-60-30C, Q-ST-80C | ✅ Complete |
| **More coming...** | Various | Multiple standards | 🔄 In progress |

## 🎓 Background

This framework was developed based on:

- **ECSS Training Course** at ESA ESTEC (September-October 2023)
- **Research collaboration** with ISAE-SUPAERO Space Advanced Concepts Laboratory (SaCLaB)
- **Practical application** in asteroid exploration GNC system development
- **ISO 9001:2015 Lead Auditor** certification principles

The methodology combines:
- European space industry best practices (ECSS)
- Model-Based Systems Engineering (MBSE) with SysML
- Quality management systems (ISO 9001:2015)
- Lessons learned from heritage missions (Hayabusa2, OSIRIS-REx)

## 📚 Documentation

- **[Quick Start Guide](ecss-mbse-framework/docs/QUICK_START.md)** - Get started in 10 minutes
- **[ECSS Standards Guide](ecss-mbse-framework/docs/ECSS_STANDARDS_GUIDE.md)** - Overview of key ECSS standards
- **[MBSE Methodology](ecss-mbse-framework/docs/MBSE_METHODOLOGY.md)** - How to use MBSE for process engineering
- **[Templates Guide](ecss-mbse-framework/templates/TEMPLATES_GUIDE.md)** - Detailed explanation of each template
- **[Tools Documentation](ecss-mbse-framework/tools/TOOLS_DOCUMENTATION.md)** - How to use automation tools
- **[Case Studies](ecss-mbse-framework/examples/CASE_STUDIES.md)** - Real-world applications

## 🛠️ Installation

### Prerequisites
```bash
python >= 3.8
pandas >= 1.3.0
openpyxl >= 3.0.0
markdown >= 3.3.0
```

### Setup
```bash
# Clone the repository
git clone https://github.com/ginevracianci/ecss-mbse-framework.git
cd ecss-mbse-framework

# Install dependencies
pip install -r requirements.txt

# Verify installation
python tools/compliance_checker.py --version
```

## Testing

### Install dev dependencies
```bash
python -m pip install -r requirements.txt -r requirements-dev.txt -c constraints.txt
```

### Run tests
```bash
python -m pytest -q
```

### CI workflow

The `python-tests` workflow runs on:
- `pull_request` (all branches)
- `push` to `main`

It uses a Python matrix (3.8, 3.10, 3.11, 3.12), installs dependencies with
`constraints.txt`, runs `pre-commit`, and then executes:

```bash
python -m pytest -q
```

## 💡 How to Use This Framework

### For Your Space Project

1. **Start with templates** - Copy relevant templates to your project
2. **Customize for your needs** - Adapt templates to your specific mission
3. **Use MBSE models** - Reference process models for workflow design
4. **Automate compliance** - Run tools to verify ECSS compliance
5. **Document everything** - Generate reports using automation tools

### For Learning ECSS

1. **Study the examples** - Review complete case studies
2. **Understand process models** - See how ECSS processes work in MBSE
3. **Practice with templates** - Use templates for practice projects
4. **Check compliance** - Use tools to verify your understanding

## 🎯 Key Features

### ✅ ECSS Standards Coverage

- **ECSS-E-ST-10-02C**: Space systems engineering - System engineering general requirements
- **ECSS-E-ST-10-03C**: Space systems engineering - Testing
- **ECSS-E-ST-60-30C**: Space engineering - GNC verification
- **ECSS-Q-ST-80C**: Space product assurance - Software product assurance
- **ECSS-M-ST-10C**: Space project management - Project planning and implementation

### ✅ MBSE Integration

- SysML process models for all major engineering activities
- Requirements traceability using SysML relationships
- Activity diagrams for workflow automation
- State machines for process control

### ✅ Practical Focus

- Templates are **ready to use** (not just examples)
- Tools provide **immediate value** (not just demonstrations)
- Examples show **complete application** (not just fragments)
- Documentation is **action-oriented** (not just reference)

## 🤝 Contributing

Contributions are welcome! This framework grows stronger with community input.

### How to Contribute

1. **Share your templates** - Submit ECSS-compliant templates you've created
2. **Add process models** - Contribute SysML models for new processes
3. **Improve tools** - Enhance automation scripts or add new ones
4. **Submit case studies** - Share how you applied the framework
5. **Report issues** - Help identify gaps or improvements

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

## 📖 Related Resources

### ECSS Standards
- [ECSS Official Website](https://ecss.nl/)
- [ECSS Standards Library](https://ecss.nl/standards/)
- [ESA Requirements & Standards Division](https://www.esa.int/Our_Activities/Space_Engineering_Technology/ECSS_Requirements_and_Standards)

### MBSE Resources
- [INCOSE MBSE Initiative](https://www.incose.org/products-and-publications/mbse-initiative)
- [SysML Specifications](https://www.omg.org/spec/SysML/)
- [ESA MBSE Portal](https://www.esa.int/Our_Activities/Space_Engineering_Technology/MBSE)

### Heritage Missions
- [Hayabusa2 Mission](https://www.hayabusa2.jaxa.jp/en/)
- [OSIRIS-REx](https://www.asteroidmission.org/)
- [ESA Science Missions](https://www.esa.int/Science_Exploration)

## 🏆 Acknowledgments

- **ESA ECSS Training Programme** for foundational knowledge
- **ISAE-SUPAERO SaCLaB** for research collaboration
- **ECSS community** for developing comprehensive standards
- **INCOSE MBSE community** for methodology guidance

## 📧 Contact

**Ginevra Cianci**
- LinkedIn: [linkedin.com/in/ginevracianci](https://linkedin.com/in/ginevracianci)
- GitHub: [github.com/ginevracianci](https://github.com/ginevracianci)
- Email: ginevra.cianci@gmail.com

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

You are free to:
- ✅ Use templates in commercial projects
- ✅ Modify and adapt for your needs
- ✅ Share with your team
- ✅ Build upon this work

---

## ⭐ Star This Repository

If you find this framework useful, please star this repository! It helps others discover these resources.

---

**Made with 🚀 by aerospace engineers, for aerospace engineers**
