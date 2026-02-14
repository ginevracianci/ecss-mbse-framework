# Software Quality Assurance Checklist

**ECSS Standard**: ECSS-Q-ST-80C - Space product assurance - Software product assurance

**Version**: 1.0  
**Date**: [YYYY-MM-DD]  
**Project**: [Project Name]

---

## Document Information

| Field | Value |
|-------|-------|
| **Software Item** | [Software name/ID] |
| **Version** | [Version number] |
| **Audit Date** | [YYYY-MM-DD] |
| **Auditor** | [Name, Role] |
| **Development Team** | [Team name] |
| **QA Status** | [Pass / Conditional Pass / Fail] |

---

## 1. Software Management and Planning

### 1.1 Software Management Plan (SMP)

| ID | Check Item | Status | Comments | Evidence |
|----|-----------|--------|----------|----------|
| SMP-01 | Software Management Plan exists and is approved | ☐ Pass ☐ Fail ☐ N/A | | [Doc ID] |
| SMP-02 | Software development lifecycle defined | ☐ Pass ☐ Fail ☐ N/A | | |
| SMP-03 | Roles and responsibilities documented | ☐ Pass ☐ Fail ☐ N/A | | |
| SMP-04 | Development tools and environment specified | ☐ Pass ☐ Fail ☐ N/A | | |
| SMP-05 | Quality assurance activities planned | ☐ Pass ☐ Fail ☐ N/A | | |

### 1.2 Software Development Plan (SDP)

| ID | Check Item | Status | Comments | Evidence |
|----|-----------|--------|----------|----------|
| SDP-01 | Development phases and milestones defined | ☐ Pass ☐ Fail ☐ N/A | | [Doc ID] |
| SDP-02 | Deliverables for each phase identified | ☐ Pass ☐ Fail ☐ N/A | | |
| SDP-03 | Review and approval process established | ☐ Pass ☐ Fail ☐ N/A | | |
| SDP-04 | Risk management approach defined | ☐ Pass ☐ Fail ☐ N/A | | |

### 1.3 Software Configuration Management Plan (SCMP)

| ID | Check Item | Status | Comments | Evidence |
|----|-----------|--------|----------|----------|
| SCMP-01 | Configuration items identified | ☐ Pass ☐ Fail ☐ N/A | | [Doc ID] |
| SCMP-02 | Version control system established | ☐ Pass ☐ Fail ☐ N/A | | |
| SCMP-03 | Baseline management procedures defined | ☐ Pass ☐ Fail ☐ N/A | | |
| SCMP-04 | Change control process documented | ☐ Pass ☐ Fail ☐ N/A | | |
| SCMP-05 | Release management procedures established | ☐ Pass ☐ Fail ☐ N/A | | |

---

## 2. Software Requirements

### 2.1 Requirements Specification

| ID | Check Item | Status | Comments | Evidence |
|----|-----------|--------|----------|----------|
| REQ-01 | Software Requirements Specification (SRS) exists | ☐ Pass ☐ Fail ☐ N/A | | [Doc ID] |
| REQ-02 | Requirements have unique identifiers | ☐ Pass ☐ Fail ☐ N/A | | |
| REQ-03 | Requirements use "shall" for mandatory items | ☐ Pass ☐ Fail ☐ N/A | | |
| REQ-04 | Requirements are unambiguous and testable | ☐ Pass ☐ Fail ☐ N/A | | |
| REQ-05 | No TBD/TBC in baselined requirements | ☐ Pass ☐ Fail ☐ N/A | | |
| REQ-06 | Requirements traceability to system reqs | ☐ Pass ☐ Fail ☐ N/A | | |

### 2.2 Interface Requirements

| ID | Check Item | Status | Comments | Evidence |
|----|-----------|--------|----------|----------|
| ICD-01 | Interface Control Documents (ICDs) exist | ☐ Pass ☐ Fail ☐ N/A | | [Doc ID] |
| ICD-02 | All external interfaces documented | ☐ Pass ☐ Fail ☐ N/A | | |
| ICD-03 | Data formats and protocols specified | ☐ Pass ☐ Fail ☐ N/A | | |
| ICD-04 | Error handling at interfaces defined | ☐ Pass ☐ Fail ☐ N/A | | |

---

## 3. Software Design

### 3.1 Architecture Design

| ID | Check Item | Status | Comments | Evidence |
|----|-----------|--------|----------|----------|
| DES-01 | Software Design Document (SDD) exists | ☐ Pass ☐ Fail ☐ N/A | | [Doc ID] |
| DES-02 | Software architecture documented | ☐ Pass ☐ Fail ☐ N/A | | |
| DES-03 | Component decomposition defined | ☐ Pass ☐ Fail ☐ N/A | | |
| DES-04 | Design rationale documented | ☐ Pass ☐ Fail ☐ N/A | | |
| DES-05 | Design traceability to requirements | ☐ Pass ☐ Fail ☐ N/A | | |

### 3.2 Detailed Design

| ID | Check Item | Status | Comments | Evidence |
|----|-----------|--------|----------|----------|
| DD-01 | Detailed design for all modules | ☐ Pass ☐ Fail ☐ N/A | | |
| DD-02 | Algorithms documented | ☐ Pass ☐ Fail ☐ N/A | | |
| DD-03 | Data structures defined | ☐ Pass ☐ Fail ☐ N/A | | |
| DD-04 | Error handling approach specified | ☐ Pass ☐ Fail ☐ N/A | | |
| DD-05 | Design review conducted and closed | ☐ Pass ☐ Fail ☐ N/A | | |

---

## 4. Software Implementation

### 4.1 Coding Standards

| ID | Check Item | Status | Comments | Evidence |
|----|-----------|--------|----------|----------|
| CODE-01 | Coding standards document exists | ☐ Pass ☐ Fail ☐ N/A | | [Doc ID] |
| CODE-02 | Code follows naming conventions | ☐ Pass ☐ Fail ☐ N/A | | |
| CODE-03 | Code is properly commented | ☐ Pass ☐ Fail ☐ N/A | | |
| CODE-04 | File headers include required info | ☐ Pass ☐ Fail ☐ N/A | | |
| CODE-05 | No hard-coded values (use constants) | ☐ Pass ☐ Fail ☐ N/A | | |
| CODE-06 | Code complexity within limits | ☐ Pass ☐ Fail ☐ N/A | | |

### 4.2 Code Quality

| ID | Check Item | Status | Comments | Evidence |
|----|-----------|--------|----------|----------|
| CQ-01 | Static code analysis performed | ☐ Pass ☐ Fail ☐ N/A | | [Report ID] |
| CQ-02 | No critical violations remain | ☐ Pass ☐ Fail ☐ N/A | | |
| CQ-03 | Code coverage ≥ [X]% achieved | ☐ Pass ☐ Fail ☐ N/A | | |
| CQ-04 | Peer code review completed | ☐ Pass ☐ Fail ☐ N/A | | |
| CQ-05 | Code review findings addressed | ☐ Pass ☐ Fail ☐ N/A | | |

### 4.3 Version Control

| ID | Check Item | Status | Comments | Evidence |
|----|-----------|--------|----------|----------|
| VC-01 | All code under version control | ☐ Pass ☐ Fail ☐ N/A | | |
| VC-02 | Commit messages are descriptive | ☐ Pass ☐ Fail ☐ N/A | | |
| VC-03 | Branching strategy followed | ☐ Pass ☐ Fail ☐ N/A | | |
| VC-04 | No uncommitted changes in baseline | ☐ Pass ☐ Fail ☐ N/A | | |

---

## 5. Software Verification and Testing

### 5.1 Test Planning

| ID | Check Item | Status | Comments | Evidence |
|----|-----------|--------|----------|----------|
| TP-01 | Software Verification Plan (SVP) exists | ☐ Pass ☐ Fail ☐ N/A | | [Doc ID] |
| TP-02 | Test approach defined for each level | ☐ Pass ☐ Fail ☐ N/A | | |
| TP-03 | Test environment specified | ☐ Pass ☐ Fail ☐ N/A | | |
| TP-04 | Test schedule defined | ☐ Pass ☐ Fail ☐ N/A | | |

### 5.2 Unit Testing

| ID | Check Item | Status | Comments | Evidence |
|----|-----------|--------|----------|----------|
| UT-01 | Unit tests exist for all modules | ☐ Pass ☐ Fail ☐ N/A | | |
| UT-02 | Unit test coverage ≥ [X]% | ☐ Pass ☐ Fail ☐ N/A | | [Report] |
| UT-03 | All unit tests pass | ☐ Pass ☐ Fail ☐ N/A | | |
| UT-04 | Failed tests documented and tracked | ☐ Pass ☐ Fail ☐ N/A | | |

### 5.3 Integration Testing

| ID | Check Item | Status | Comments | Evidence |
|----|-----------|--------|----------|----------|
| IT-01 | Integration test cases defined | ☐ Pass ☐ Fail ☐ N/A | | |
| IT-02 | Interface testing completed | ☐ Pass ☐ Fail ☐ N/A | | |
| IT-03 | Integration test report available | ☐ Pass ☐ Fail ☐ N/A | | [Report ID] |
| IT-04 | Defects resolved or waived | ☐ Pass ☐ Fail ☐ N/A | | |

### 5.4 System Testing

| ID | Check Item | Status | Comments | Evidence |
|----|-----------|--------|----------|----------|
| ST-01 | System test cases cover all requirements | ☐ Pass ☐ Fail ☐ N/A | | |
| ST-02 | Requirements traceability matrix complete | ☐ Pass ☐ Fail ☐ N/A | | |
| ST-03 | All critical requirements verified | ☐ Pass ☐ Fail ☐ N/A | | |
| ST-04 | System test report approved | ☐ Pass ☐ Fail ☐ N/A | | [Report ID] |

### 5.5 Regression Testing

| ID | Check Item | Status | Comments | Evidence |
|----|-----------|--------|----------|----------|
| RT-01 | Regression test suite defined | ☐ Pass ☐ Fail ☐ N/A | | |
| RT-02 | Regression tests executed after changes | ☐ Pass ☐ Fail ☐ N/A | | |
| RT-03 | No new defects introduced | ☐ Pass ☐ Fail ☐ N/A | | |

---

## 6. Software Documentation

### 6.1 Technical Documentation

| ID | Check Item | Status | Comments | Evidence |
|----|-----------|--------|----------|----------|
| DOC-01 | User Manual exists and is current | ☐ Pass ☐ Fail ☐ N/A | | [Doc ID] |
| DOC-02 | Installation Guide available | ☐ Pass ☐ Fail ☐ N/A | | [Doc ID] |
| DOC-03 | API documentation complete | ☐ Pass ☐ Fail ☐ N/A | | |
| DOC-04 | Technical specifications up-to-date | ☐ Pass ☐ Fail ☐ N/A | | |

### 6.2 Process Documentation

| ID | Check Item | Status | Comments | Evidence |
|----|-----------|--------|----------|----------|
| PROC-01 | Build procedures documented | ☐ Pass ☐ Fail ☐ N/A | | |
| PROC-02 | Deployment procedures documented | ☐ Pass ☐ Fail ☐ N/A | | |
| PROC-03 | Maintenance procedures documented | ☐ Pass ☐ Fail ☐ N/A | | |

---

## 7. Configuration Management

### 7.1 Baseline Management

| ID | Check Item | Status | Comments | Evidence |
|----|-----------|--------|----------|----------|
| CM-01 | Software baseline identified | ☐ Pass ☐ Fail ☐ N/A | | [Baseline ID] |
| CM-02 | Baseline under configuration control | ☐ Pass ☐ Fail ☐ N/A | | |
| CM-03 | Build procedure repeatable | ☐ Pass ☐ Fail ☐ N/A | | |
| CM-04 | Build artifacts archived | ☐ Pass ☐ Fail ☐ N/A | | |

### 7.2 Change Management

| ID | Check Item | Status | Comments | Evidence |
|----|-----------|--------|----------|----------|
| CHG-01 | Change control process followed | ☐ Pass ☐ Fail ☐ N/A | | |
| CHG-02 | All changes have approved change requests | ☐ Pass ☐ Fail ☐ N/A | | |
| CHG-03 | Impact analysis performed for changes | ☐ Pass ☐ Fail ☐ N/A | | |
| CHG-04 | Change log maintained | ☐ Pass ☐ Fail ☐ N/A | | |

---

## 8. Risk and Safety

### 8.1 Software Safety

| ID | Check Item | Status | Comments | Evidence |
|----|-----------|--------|----------|----------|
| SAF-01 | Hazard analysis performed | ☐ Pass ☐ Fail ☐ N/A | | [Report ID] |
| SAF-02 | Safety-critical functions identified | ☐ Pass ☐ Fail ☐ N/A | | |
| SAF-03 | Safety requirements verified | ☐ Pass ☐ Fail ☐ N/A | | |
| SAF-04 | Fault tolerance mechanisms tested | ☐ Pass ☐ Fail ☐ N/A | | |

### 8.2 Risk Management

| ID | Check Item | Status | Comments | Evidence |
|----|-----------|--------|----------|----------|
| RISK-01 | Software risks identified | ☐ Pass ☐ Fail ☐ N/A | | [Risk register] |
| RISK-02 | Mitigation plans in place | ☐ Pass ☐ Fail ☐ N/A | | |
| RISK-03 | Risks reviewed regularly | ☐ Pass ☐ Fail ☐ N/A | | |

---

## 9. Quality Metrics

### 9.1 Code Metrics

| Metric | Target | Actual | Status |
|--------|--------|--------|--------|
| Code Coverage | ≥ 80% | [%] | ☐ Pass ☐ Fail |
| Cyclomatic Complexity | ≤ 15 | [value] | ☐ Pass ☐ Fail |
| Lines of Code per Function | ≤ 200 | [value] | ☐ Pass ☐ Fail |
| Comment Density | ≥ 20% | [%] | ☐ Pass ☐ Fail |

### 9.2 Test Metrics

| Metric | Target | Actual | Status |
|--------|--------|--------|--------|
| Requirements Coverage | 100% | [%] | ☐ Pass ☐ Fail |
| Test Pass Rate | ≥ 95% | [%] | ☐ Pass ☐ Fail |
| Defect Density | ≤ 0.5/KLOC | [value] | ☐ Pass ☐ Fail |
| Critical Defects Open | 0 | [number] | ☐ Pass ☐ Fail |

### 9.3 Process Metrics

| Metric | Target | Actual | Status |
|--------|--------|--------|--------|
| Peer Review Coverage | 100% | [%] | ☐ Pass ☐ Fail |
| Review Defect Density | [value] | [value] | ☐ Pass ☐ Fail |
| Change Request Closure Rate | ≥ 90% | [%] | ☐ Pass ☐ Fail |

---

## 10. Audit Summary

### 10.1 Findings

| Finding ID | Category | Severity | Description | Action Required | Owner | Due Date |
|-----------|----------|----------|-------------|-----------------|-------|----------|
| F-001 | [Category] | [Critical/Major/Minor] | [Description] | [Action] | [Name] | [Date] |

**Severity Definitions:**
- **Critical**: Non-compliance with mandatory requirements, blocks release
- **Major**: Significant gap, workaround possible
- **Minor**: Documentation or process improvement needed

### 10.2 Non-Conformances (NCs)

| NC ID | Description | ECSS Clause | Resolution | Status |
|-------|-------------|-------------|------------|--------|
| NC-001 | [Description] | [Clause] | [Resolution plan] | [Open/Closed] |

### 10.3 Observations

| OBS ID | Description | Recommendation |
|--------|-------------|----------------|
| OBS-001 | [Observation] | [Recommendation] |

---

## 11. Overall Assessment

### 11.1 Summary

| Area | Pass | Fail | N/A | Total | Pass Rate |
|------|------|------|-----|-------|-----------|
| Software Management | [N] | [N] | [N] | [N] | [%] |
| Requirements | [N] | [N] | [N] | [N] | [%] |
| Design | [N] | [N] | [N] | [N] | [%] |
| Implementation | [N] | [N] | [N] | [N] | [%] |
| Verification | [N] | [N] | [N] | [N] | [%] |
| Documentation | [N] | [N] | [N] | [N] | [%] |
| Configuration Mgmt | [N] | [N] | [N] | [N] | [%] |
| Risk & Safety | [N] | [N] | [N] | [N] | [%] |
| **TOTAL** | **[N]** | **[N]** | **[N]** | **[N]** | **[%]** |

### 11.2 QA Decision

☐ **PASS** - Software meets all ECSS-Q-ST-80C requirements  
☐ **CONDITIONAL PASS** - Minor findings, can proceed with conditions  
☐ **FAIL** - Critical findings, cannot proceed until resolved

**Conditions (if applicable):**
1. [Condition/Finding to be resolved]
2. [Condition/Finding to be resolved]

**Justification:**
[Provide rationale for QA decision]

---

## 12. Sign-Off

### 12.1 Auditor

**Name**: [QA Auditor Name]  
**Signature**: ___________________  
**Date**: [YYYY-MM-DD]

**ISO 9001:2015 Lead Auditor**: ☐ Yes ☐ No  
**ECSS Training**: ☐ Yes ☐ No

### 12.2 Development Team

**Name**: [Development Lead]  
**Signature**: ___________________  
**Date**: [YYYY-MM-DD]

**Acknowledgment**: I acknowledge the findings and commit to addressing identified issues.

### 12.3 QA Manager

**Name**: [QA Manager]  
**Signature**: ___________________  
**Date**: [YYYY-MM-DD]

**Approval**: ☐ Approved ☐ Conditional ☐ Rejected

---

## Appendix A: Reference Documents

| ID | Document | Version |
|----|----------|---------|
| [1] | ECSS-Q-ST-80C Rev. 1 | Rev 1 |
| [2] | ISO/IEC 12207:2017 | 2017 |
| [3] | ISO 9001:2015 | 2015 |
| [4] | Project Software Management Plan | [Version] |

---

## Appendix B: ECSS-Q-ST-80C Compliance Matrix

| ECSS Clause | Title | Section | Status |
|-------------|-------|---------|--------|
| 5.1 | Software management | 1.1 | ✅ |
| 5.2 | Software requirements | 2.1 | ✅ |
| 5.3 | Software design | 3.1 | ✅ |
| 5.4 | Software implementation | 4.1 | ✅ |
| 5.5 | Software verification | 5.1 | ✅ |
| 5.6 | Software configuration management | 7.1 | ✅ |

---

**Document prepared using ECSS-MBSE Framework**  
Repository: https://github.com/ginevracianci/ecss-mbse-framework
