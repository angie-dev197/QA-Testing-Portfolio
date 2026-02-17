# Manual Test Plan - Demo Website

**Project:** QA Portfolio -  Demo Site  
**Prepared by:** Angelica Soete  
**Date:** February 16, 2026  
**Version:** 2.0

---

## 1. Introduction

### 1.1 Purpose
This document outlines the manual and automated testing strategy for the demo website created as part of my QA portfolio. The plan demonstrates realistic QA practices under resource constraints, focusing on risk-based prioritization and test automation efficiency.

### 1.2 Project Overview
**Application:** Multi-page informational website  
**Technology Stack:** HTML5, CSS3, JavaScript  
**Pages:** Home, Services, Culture, Contact  
**Test Environment:** Self-built static website with custom Python automation framework

### 1.3 Portfolio Context
This test plan demonstrates:
- **Manual testing expertise** from 2+ years LQA experience in gaming industry
- **Test automation skills** using Python/Selenium for efficiency gains
- **Full testing lifecycle** from planning → execution → reporting
- **Risk-based prioritization** under time and resource constraints

### 1.4 Objectives
- Verify all critical features work across multiple browsers and devices
- Ensure responsive design functions properly (320px - 1920px)
- Validate form functionality with comprehensive edge case testing
- Automate repetitive cross-browser regression tests using Python
- Document defects with reproducible steps and clear evidence
- Demonstrate practical QA skills applicable to real-world projects

---

## 2. Scope

### 2.1 In Scope
✅ Functional testing (navigation, forms, content rendering)  
✅ Cross-browser compatibility (Chrome, Firefox, Edge desktop + Safari iOS)  
✅ Responsive design testing (physical device + DevTools simulation)  
✅ Form validation and edge case testing  
✅ Basic performance testing (page load times)  
✅ Automated regression testing (Python/Selenium)

### 2.2 Out of Scope
❌ Desktop Safari (no macOS device available)  
❌ Native Android testing (using iOS + DevTools simulation)  
❌ Backend/server-side testing (static site)  
❌ Security/penetration testing  
❌ Load/stress testing  
❌ Accessibility compliance (WCAG) - basic keyboard nav only

### 2.3 Resource Constraints
**Available hardware:**
- Windows 11 PC (Intel i9, 8GB RAM, 1920×1080)
- iPhone 11 (iOS 17+)
- Browser DevTools for responsive simulation

**Time constraint:** TBD

---

## 3. Testing Approach & Tools

### 3.1 Manual Testing
**Tools & Methods:**
- Browser DevTools for inspection, console debugging, network analysis
- Exploratory testing combined with structured test cases
- Cross-device testing (physical iPhone 11 + DevTools responsive modes)
- Screenshot documentation for visual defects

**Coverage:**
- 12 priority test cases (P1/P2) executed in full
- Additional test scenarios documented but not executed

### 3.2 Automated Testing (Python/Selenium)
**Framework:** Selenium WebDriver + pytest  
**Coverage:** Cross-browser regression suite for critical user flows  
**Efficiency gain:** ~85% time reduction vs. manual execution  


**Automated test scenarios:**
- Navigation flow validation across all pages
- Form submission with valid/invalid data
- Responsive breakpoint verification
- Cross-browser consistency checks (Chrome, Firefox, Edge)

**Example code snippet:**
```python
def test_contact_form_validation():
    driver.get("http://localhost:8000/contact.html")

    # Test invalid email format
    email_field = driver.find_element(By.ID, "email")
    email_field.send_keys("invalid@")
    submit_btn = driver.find_element(By.ID, "submit")
    submit_btn.click()

    error_msg = driver.find_element(By.CLASS_NAME, "error-message")
    assert error_msg.is_displayed()
    assert "valid email" in error_msg.text.lower()
```

---

## 4. Test Environment

### 4.1 Browsers & Platforms

| Browser | Version | Platform | Test Coverage |
|---------|---------|----------|---------------|
| Chrome | 131+ | Windows 11 | Full (P1-P2 cases) |
| Firefox | 128+ | Windows 11 | Full (P1-P2 cases) |
| Edge | 130+ | Windows 11 | Smoke (P1 only) |
| Safari | iOS 17+ | iPhone 11 | Full (P1-P2 cases) |

**Testing strategy:**
- **Primary:** Chrome Desktop (most comprehensive + automation)
- **Secondary:** Firefox Desktop, Safari iOS (full functional testing)
- **Tertiary:** Edge Desktop (smoke testing - core functionality only)


**Rationale for exclusions:**
- Desktop Safari excluded due to lack of macOS device
- Android native testing excluded (compensated by iOS + DevTools Android simulation)

### 4.2 Test Data

**Valid inputs:**
- Email: `test@example.com`
- Name: Standard characters, accented characters (José, François)
- Phone: Various international formats

**Invalid/edge case inputs:**
- Email: `@example.com`, `test@`, `test@.com`, `test..double@example.com`
- XSS attempts: `<script>alert('test')</script>`
- SQL injection patterns: `'; DROP TABLE--`
- Very long strings (>255 chars)
- Special characters: `!@#$%^&*()`
- Empty fields, whitespace only

---

## 5. Browser/Device Test Matrix

| Page | Chrome Desktop | Firefox Desktop | Edge Desktop | Safari iOS |
|------|----------------|-----------------|--------------|------------|
| Home | ✅ Full | ✅ Full | ✅ Smoke | ✅ Full |
| Services | ✅ Full | ✅ Full | ✅ Smoke | ✅ Full |
| Culture | ✅ Full | ✅ Full | ✅ Smoke | ✅ Full |
| Contact | ✅ Full | ✅ Full | ✅ Smoke | ✅ Full |

**Legend:**
- **Full:** All test cases executed (P1 + P2)
- **Smoke:** Critical path only (P1 cases: navigation, page load, core features)

---

## 6. Test Cases & Prioritization

### 6.1 Test Case Summary

**Test cases executed:** 13  
**Test case categories:**

#### P1 - Critical (Must Execute)
- **TC-NAV-001:** Main navigation links work on all pages
- **TC-NAV-002:** Footer links navigate to correct destinations
- **TC-FORM-001:** Contact form submits with valid data
- **TC-FORM-002:** Email validation rejects invalid formats
- **TC-RESP-001:** Homepage responsive 320px - 1920px

*5 test cases*

#### P2 - High Priority
- **TC-FORM-003:** Required field validation (empty fields blocked)
- **TC-FORM-004:** Form sanitizes special characters/XSS attempts
- **TC-UI-001:** Images load correctly on all pages
- **TC-UI-002:** Typography renders consistently across browsers
- **TC-COMPAT-001:** Cross-browser layout consistency
- **TC-COMPAT-002:** Mobile navigation menu works on iOS

*6 test cases*

#### P3 - Medium (Documented, Not Executed)
- **TC-PERF-001:** Page load time <3 seconds
- **TC-UI-003:** Hover effects display correctly

*2 test cases (documented as future testing scenarios)*

### 6.2 Detailed Test Cases
Full test case documentation available in: `docs/test-cases.md`

---

## 7. Test Execution Strategy

### 7.1 Testing Approach
**Methodology:** Risk-based testing with exploratory + scripted approaches

**Test cycle:**
1. Execute P1 critical path tests (manual + automated)
2. Execute P2 high-priority functional tests
3. Perform exploratory testing on each page (30 min per page)
4. Document defects with screenshots and reproducible steps
5. Fix defects and retest
6. Run automated regression suite

### 7.2 Entry Criteria
- ✅ Website accessible via local server or file system
- ✅ All browsers installed and configured
- ✅ Test data prepared
- ✅ Automation framework set up and working
- ✅ Bug tracking template ready

### 7.3 Exit Criteria
- ✅ All P1 and P2 test cases executed
- ✅ All P1 defects fixed and verified
- ✅ P2 defects documented (fix if time permits)
- ✅ Automated test suite passing on Chrome/Firefox
- ✅ Test execution report completed
- ✅ No critical blockers preventing portfolio demonstration

---

## 9. Test Deliverables

### 9.1 Documentation
- ✅ Test Plan (this document)
- ✅ Test Cases Spreadsheet (`QA-Manual-Testing/test_cases.xlsx`)
- ✅ Bug Reports with screenshots (`QA-Manual-Testing/bug_reports`)
- ✅ Test Execution Summary (`QA-Automated-Testing/test_results`)
- ✅ Automation code on GitHub

### 9.2 Test Metrics (Example)

| Metric | Value |
|--------|-------|
| Total test cases | TBD |
| Test cases executed | TBD (100%) |
| Pass rate | x/y (100%) |
| Defects found | 0 |
| P1 defects | 0 |
| P2 defects | 0 |
| P3 defects | 0 |
| Defects fixed | 0/0 (100%) |
| Automated tests | 0 scenarios |
| Automation pass rate | 0/0 (100%) |

---

## 10. Defect Management

### 10.1 Bug Report Example

**BUG-001: Contact form accepts invalid email format**

**Severity:** P2 (High)  
**Status:** Fixed  
**Found in:** Chrome 131, Firefox 128  
**Environment:** Windows 11 Desktop

**Steps to reproduce:**
1. Navigate to Contact page
2. Enter email: `@example.com`
3. Fill other required fields with valid data
4. Click Submit button

**Expected result:** Form should display error "Please enter a valid email address"  
**Actual result:** Form accepts invalid email and displays success message

**Root cause:** Email validation regex didn't check for characters before @ symbol  
**Fix:** Updated regex pattern to `/^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/`  
**Retest result:** ✅ Pass - Invalid emails now properly rejected

**Screenshot:** `bug-reports/BUG-001-screenshot.png`

### 10.2 Defect Workflow
1. **New** → Defect discovered during testing
2. **Open** → Confirmed and documented
3. **In Progress** → Fix being implemented
4. **Fixed** → Code updated, ready for retest
5. **Closed** → Verified fixed, no regression

---

## 11. Risks & Mitigation

| Risk | Impact | Mitigation |
|------|--------|------------|
| Browser updates break compatibility | Medium | Test on stable releases; document versions |
| Limited device access | Medium | Use DevTools simulation; prioritize available hardware |
| Time constraints affect coverage | High | Focus on P1/P2; document untested scenarios |
| Automation maintenance overhead | Low | Keep scripts simple; use stable selectors |

---

## 12. Portfolio Note: Resource Constraints & Decisions

### 12.1 Real-World Context
This portfolio project was completed under realistic constraints that mirror actual QA work:

**Available resources:**
- 1 Windows PC + 1 iPhone 11
- Solo tester (no team collaboration)
- No dedicated QA tools (free/open-source only)

**Strategic decisions made:**
- ✅ Executed 12 of 15 planned test cases (80% coverage, 100% of P1/P2)
- ✅ Focused on 4 browsers representing 85% market share
- ✅ Used DevTools for Android simulation (no physical device)
- ✅ Built custom automation framework to maximize efficiency
- ✅ Documented all test scenarios; executed highest priority

### 12.2 What This Demonstrates
- **Risk-based prioritization:** Understanding what matters most
- **Resource management:** Delivering quality within constraints
- **Practical automation:** Using Python to solve real QA challenges
- **Transparent communication:** Clear about scope and limitations
- **Professional judgment:** Quality over quantity approach
- **LQA transferable skills:** Attention to detail, edge case thinking, systematic testing

This approach reflects real QA work where testers must balance:
- Comprehensive testing vs. time/budget constraints
- Manual verification vs. automation ROI
- Ideal coverage vs. available resources
- Documented thoroughness vs. executed depth

---

## 13. Tools & Technologies

| Tool | Purpose |
|------|---------|
| **Selenium WebDriver** | Browser automation |
| **Python + pytest** | Test automation framework |
| **Html** | static demo-website |
| **Chrome DevTools** | Debugging, network analysis, responsive testing |
| **Git/GitHub** | Version control, code repository |
| **Visual Studio Code** | Test script development |
| **Markdown** | Documentation |

---


## Appendix A: Testing Checklist

**Manual Testing:**
- [x] All navigation links tested (4 browsers)
- [x] Contact form validation tested (valid + invalid inputs)
- [x] Responsive breakpoints verified (320px, 768px, 1024px, 1920px)
- [x] Cross-browser compatibility confirmed
- [x] All defects documented with screenshots
- [x] P1/P2 defects fixed and retested

**Automated Testing:**
- [x] Selenium framework set up
- [x] Cross-browser tests created (Chrome, Firefox, Edge)
- [x] Form validation automated
- [x] Navigation flow automated
- [x] Regression suite passing
- [x] Code pushed to GitHub

**Documentation:**
- [x] Test plan completed
- [x] Test cases documented
- [x] Bug reports written
- [x] Test summary with metrics
- [x] Portfolio context explained

---

## Appendix B: References

- **Test Cases:** `QA-Manual-Testing/test_cases.xlsx`
- **Bug Reports:** `QA-Manual-Testing/bug_reports/bug_report_log.xlsx`
- **Automation Code:** `QA-Automated-Testing/test_navigation.py`
- **GitHub Repository:** [Link to project]

---

**End of Test Plan**
