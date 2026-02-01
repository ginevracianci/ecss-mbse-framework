#!/usr/bin/env python3
"""
ECSS Compliance Checker
Automated verification of ECSS standards compliance in project documentation

Based on:
- ECSS-E-ST-10-02C: System engineering general requirements
- ECSS-E-ST-10-03C: Testing
- ECSS-Q-ST-80C: Software product assurance

Author: Ginevra Cianci
License: MIT
"""

import re
import argparse
from pathlib import Path
from typing import Dict, List, Tuple
from dataclasses import dataclass
import sys

@dataclass
class ComplianceIssue:
    """Represents a compliance issue found during checking"""
    severity: str  # 'critical', 'major', 'minor'
    category: str
    description: str
    file_path: str
    line_number: int = 0
    ecss_clause: str = ""


class ECSSComplianceChecker:
    """
    Automated checker for ECSS standards compliance
    """
    
    def __init__(self, project_path: Path):
        self.project_path = project_path
        self.issues: List[ComplianceIssue] = []
        
    def check_all(self) -> Dict[str, int]:
        """
        Run all compliance checks
        
        Returns:
            Dict with counts of issues by severity
        """
        print(f"🔍 Checking ECSS compliance for: {self.project_path}")
        print("=" * 60)
        
        # Run checks
        self.check_requirements()
        self.check_traceability()
        self.check_test_coverage()
        self.check_documentation()
        
        # Summarize results
        return self.summarize_results()
    
    def check_requirements(self) -> None:
        """
        Check requirements compliance per ECSS-E-ST-10-02C
        """
        print("\n📋 Checking Requirements (ECSS-E-ST-10-02C)...")
        
        req_files = list(self.project_path.glob("**/*requirements*.md"))
        
        if not req_files:
            self.issues.append(ComplianceIssue(
                severity='critical',
                category='Requirements',
                description='No requirements specification found',
                file_path=str(self.project_path),
                ecss_clause='ECSS-E-ST-10-02C § 5.2.1'
            ))
            return
        
        for req_file in req_files:
            self._check_requirement_file(req_file)
    
    def _check_requirement_file(self, file_path: Path) -> None:
        """Check individual requirements file"""
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            lines = content.split('\n')
        
        # Check 1: Requirements should use "shall" for mandatory items
        should_count = len(re.findall(r'\bshould\b', content, re.IGNORECASE))
        if should_count > 0:
            self.issues.append(ComplianceIssue(
                severity='major',
                category='Requirements',
                description=f'Found {should_count} instances of "should" - use "shall" for mandatory requirements',
                file_path=str(file_path),
                ecss_clause='ECSS-E-ST-10-02C § 5.2.2'
            ))
        
        # Check 2: Requirements should have unique IDs
        req_pattern = r'R-[A-Z]+-\d+'
        req_ids = re.findall(req_pattern, content)
        if req_ids:
            if len(req_ids) != len(set(req_ids)):
                duplicates = [r for r in req_ids if req_ids.count(r) > 1]
                self.issues.append(ComplianceIssue(
                    severity='critical',
                    category='Requirements',
                    description=f'Duplicate requirement IDs found: {set(duplicates)}',
                    file_path=str(file_path),
                    ecss_clause='ECSS-E-ST-10-02C § 5.2.1'
                ))
        
        # Check 3: No TBD/TBC in baseline
        tbd_matches = [(i+1, line) for i, line in enumerate(lines) if 'TBD' in line or 'TBC' in line]
        if tbd_matches:
            self.issues.append(ComplianceIssue(
                severity='major',
                category='Requirements',
                description=f'Found {len(tbd_matches)} TBD/TBC items - should be resolved for baseline',
                file_path=str(file_path),
                line_number=tbd_matches[0][0],
                ecss_clause='ECSS-E-ST-10-02C § 5.2.2'
            ))
        
        # Check 4: Requirements should have verification methods
        verification_keywords = ['test', 'analysis', 'review', 'inspection']
        req_blocks = content.split('R-')
        unverified = 0
        for block in req_blocks[1:]:  # Skip first split (before any R-)
            has_verification = any(kw in block.lower() for kw in verification_keywords)
            if not has_verification:
                unverified += 1
        
        if unverified > 0:
            self.issues.append(ComplianceIssue(
                severity='major',
                category='Requirements',
                description=f'{unverified} requirements lack verification method specification',
                file_path=str(file_path),
                ecss_clause='ECSS-E-ST-10-02C § 6.2.1'
            ))
        
        print(f"  ✓ Checked {file_path.name}")
    
    def check_traceability(self) -> None:
        """
        Check requirements traceability
        """
        print("\n🔗 Checking Requirements Traceability...")
        
        # Look for traceability matrix files
        trace_files = list(self.project_path.glob("**/*trace*.xlsx")) + \
                     list(self.project_path.glob("**/*trace*.md"))
        
        if not trace_files:
            self.issues.append(ComplianceIssue(
                severity='major',
                category='Traceability',
                description='No traceability matrix found',
                file_path=str(self.project_path),
                ecss_clause='ECSS-E-ST-10-02C § 5.2.3'
            ))
        else:
            print(f"  ✓ Found traceability matrix: {trace_files[0].name}")
    
    def check_test_coverage(self) -> None:
        """
        Check test coverage per ECSS-E-ST-10-03C
        """
        print("\n🧪 Checking Test Coverage (ECSS-E-ST-10-03C)...")
        
        # Look for test plan
        test_plans = list(self.project_path.glob("**/*test*plan*.md"))
        
        if not test_plans:
            self.issues.append(ComplianceIssue(
                severity='critical',
                category='Verification',
                description='No test plan document found',
                file_path=str(self.project_path),
                ecss_clause='ECSS-E-ST-10-03C § 5.4.1'
            ))
        else:
            print(f"  ✓ Found test plan: {test_plans[0].name}")
            
        # Look for test cases
        test_files = list(self.project_path.glob("**/test*.py")) + \
                    list(self.project_path.glob("**/test*.md"))
        
        if len(test_files) < 5:
            self.issues.append(ComplianceIssue(
                severity='minor',
                category='Verification',
                description=f'Only {len(test_files)} test files found - may indicate insufficient coverage',
                file_path=str(self.project_path),
                ecss_clause='ECSS-E-ST-10-03C § 5.4.2'
            ))
    
    def check_documentation(self) -> None:
        """
        Check documentation completeness
        """
        print("\n📚 Checking Documentation Completeness...")
        
        required_docs = {
            'README.md': 'Project overview',
            'requirements': 'Requirements specification',
            'design': 'Design documentation',
            'test': 'Test documentation'
        }
        
        for doc_pattern, description in required_docs.items():
            matching_files = list(self.project_path.glob(f"**/*{doc_pattern}*"))
            if not matching_files:
                self.issues.append(ComplianceIssue(
                    severity='minor',
                    category='Documentation',
                    description=f'Missing {description}',
                    file_path=str(self.project_path),
                    ecss_clause='ECSS-Q-ST-80C § 5.7'
                ))
            else:
                print(f"  ✓ Found {description}")
    
    def summarize_results(self) -> Dict[str, int]:
        """
        Print summary of compliance check results
        
        Returns:
            Dict with counts of issues by severity
        """
        print("\n" + "=" * 60)
        print("📊 COMPLIANCE CHECK SUMMARY")
        print("=" * 60)
        
        severity_counts = {
            'critical': len([i for i in self.issues if i.severity == 'critical']),
            'major': len([i for i in self.issues if i.severity == 'major']),
            'minor': len([i for i in self.issues if i.severity == 'minor'])
        }
        
        # Print by severity
        if severity_counts['critical'] > 0:
            print(f"\n🔴 CRITICAL Issues: {severity_counts['critical']}")
            for issue in [i for i in self.issues if i.severity == 'critical']:
                print(f"  ❌ {issue.category}: {issue.description}")
                print(f"     File: {issue.file_path}")
                print(f"     ECSS: {issue.ecss_clause}")
        
        if severity_counts['major'] > 0:
            print(f"\n🟡 MAJOR Issues: {severity_counts['major']}")
            for issue in [i for i in self.issues if i.severity == 'major']:
                print(f"  ⚠️  {issue.category}: {issue.description}")
                print(f"     File: {issue.file_path}")
                print(f"     ECSS: {issue.ecss_clause}")
        
        if severity_counts['minor'] > 0:
            print(f"\n🔵 MINOR Issues: {severity_counts['minor']}")
            for issue in [i for i in self.issues if i.severity == 'minor']:
                print(f"  ℹ️  {issue.category}: {issue.description}")
                print(f"     ECSS: {issue.ecss_clause}")
        
        # Overall verdict
        print("\n" + "=" * 60)
        if severity_counts['critical'] == 0 and severity_counts['major'] == 0:
            print("✅ PASS - Project meets ECSS compliance requirements")
            print("(Minor issues are recommendations for improvement)")
            return_code = 0
        elif severity_counts['critical'] == 0:
            print("⚠️  CONDITIONAL PASS - Major issues should be addressed")
            return_code = 1
        else:
            print("❌ FAIL - Critical issues must be resolved")
            return_code = 2
        
        print("=" * 60)
        
        return severity_counts, return_code
    
    def generate_report(self, output_file: Path) -> None:
        """
        Generate detailed compliance report
        
        Args:
            output_file: Path to output markdown report
        """
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write("# ECSS Compliance Report\n\n")
            f.write(f"**Project**: {self.project_path.name}\n")
            f.write(f"**Generated**: {Path.cwd()}\n\n")
            
            f.write("## Summary\n\n")
            f.write("| Severity | Count |\n")
            f.write("|----------|-------|\n")
            
            severity_counts = {
                'critical': len([i for i in self.issues if i.severity == 'critical']),
                'major': len([i for i in self.issues if i.severity == 'major']),
                'minor': len([i for i in self.issues if i.severity == 'minor'])
            }
            
            f.write(f"| Critical | {severity_counts['critical']} |\n")
            f.write(f"| Major | {severity_counts['major']} |\n")
            f.write(f"| Minor | {severity_counts['minor']} |\n\n")
            
            f.write("## Findings\n\n")
            
            for severity in ['critical', 'major', 'minor']:
                issues = [i for i in self.issues if i.severity == severity]
                if issues:
                    f.write(f"### {severity.upper()} Issues\n\n")
                    for i, issue in enumerate(issues, 1):
                        f.write(f"{i}. **{issue.category}**: {issue.description}\n")
                        f.write(f"   - File: `{issue.file_path}`\n")
                        f.write(f"   - ECSS Reference: {issue.ecss_clause}\n\n")
        
        print(f"\n📄 Detailed report saved to: {output_file}")


def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(
        description='ECSS Compliance Checker - Automated verification of ECSS standards',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python compliance_checker.py /path/to/project
  python compliance_checker.py . --report compliance_report.md
  python compliance_checker.py ../my_project --version

ECSS Standards Checked:
  - ECSS-E-ST-10-02C: System engineering general requirements
  - ECSS-E-ST-10-03C: Testing
  - ECSS-Q-ST-80C: Software product assurance
        """
    )
    
    parser.add_argument(
        'project_path',
        nargs='?',
        default='.',
        help='Path to project directory (default: current directory)'
    )
    
    parser.add_argument(
        '--report',
        '-r',
        type=str,
        help='Generate detailed report to specified file'
    )
    
    parser.add_argument(
        '--version',
        '-v',
        action='version',
        version='ECSS Compliance Checker v1.0.0'
    )
    
    args = parser.parse_args()
    
    # Validate project path
    project_path = Path(args.project_path).resolve()
    if not project_path.exists():
        print(f"❌ Error: Project path does not exist: {project_path}")
        sys.exit(1)
    
    # Run compliance check
    checker = ECSSComplianceChecker(project_path)
    severity_counts, return_code = checker.check_all()
    
    # Generate report if requested
    if args.report:
        report_path = Path(args.report)
        checker.generate_report(report_path)
    
    sys.exit(return_code)


if __name__ == '__main__':
    main()
