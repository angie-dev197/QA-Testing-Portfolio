# QA Project — Demo Website (Manual + Automation)

QA portfolio project showcasing a realistic end-to-end testing workflow (planning → test design → execution → defect reporting → retest) on a **multi-page demo website**.  
It includes both manual testing and a lightweight automation suite built with **Python + Selenium + pytest**, designed around real resource constraints.  

## Project overview

**Application under test (AUT):** Demo multi-page informational website (static).  
**Pages:** Home, Services, Culture, Contact.  
**Tech stack:** HTML5, CSS3, JavaScript.  
**Test environment:** Self-built static website + custom Python automation framework.  

This repo is built to demonstrate:
- Manual testing skills (including structured + exploratory execution).
- Automation ROI: reduce repetitive cross-browser regression effort using Python/Selenium.
- Risk-based prioritization under time/device constraints.

## Objectives

- Verify critical functionality across multiple browsers/devices.
- Ensure responsive behavior from **320px to 1920px**.
- Validate the Contact form thoroughly (valid + invalid + edge-case inputs).
- Automate repetitive regression checks (navigation, form validation, breakpoints, cross-browser consistency).
- Document defects with reproducible steps and evidence.

## Scope

### In scope
- Functional testing: navigation, links, content rendering, images, UI consistency.
- Contact form: submission, required-field validation, email validation, sanitization (special characters, basic XSS/SQLi patterns).
- Cross-browser testing (defined below) and responsive design checks.
- Basic performance check: page load time target (P2).

### Out of scope (by design)
- Desktop Safari testing (no macOS device available).
- Native Android device testing (covered via DevTools simulation only).
- Backend/server-side testing (static site).
- Security/pentest, load/stress testing.
- Full accessibility compliance (only basic keyboard navigation checks).

## Test approach

### Manual testing
- Exploratory testing combined with structured test cases.
- Use DevTools for inspection, console debugging, and network analysis.
- Cross-device checks using a physical iPhone 11 plus responsive simulation in DevTools.
- Screenshot documentation for visual defects.

### Automated testing
**Framework:** Selenium WebDriver + pytest (Python).  
**Automated regression focus:**
- Navigation flow validation across pages.
- Contact form submission with valid/invalid data.
- Responsive breakpoint verification.
- Cross-browser consistency checks.

The automation is intended to significantly reduce repetitive manual execution time (documented efficiency gain in the test plan).

## Browsers & device matrix

**Hardware available:**
- Windows 11 PC (1920×1080).
- iPhone 11 (iOS 17).

**Browsers & coverage strategy:**
- Chrome (Windows 11): Full P1–P2 coverage.
- Firefox (Windows 11): Full P1–P2 coverage.
- Edge (Windows 11): Smoke coverage (P1 only).
- Safari (iOS 17 on iPhone 11): Full P1–P2 coverage.

Page coverage summary (from the test plan):
- Home / Services / Culture / Contact: Full on Chrome + Firefox + Safari iOS, Smoke on Edge.

## Test cases & prioritization

Risk-based prioritization with P1/P2 executed first.

**P1 (Critical — must execute) examples:**
- Main navigation links work on all pages (TC-NAV-001)
- Contact form submits with valid data (TC-FORM-001)
- Email validation rejects invalid formats (TC-FORM-002)
- Required field validation blocks empty fields (TC-FORM-003)
- Form sanitizes special characters / XSS attempts (TC-FORM-004)
- Responsive behavior (320px–1920px) (TC-RESP-001)
- Cross-browser layout consistency (TC-COMPAT-001)
- Mobile navigation menu works on iOS (TC-COMPAT-002)

**P2 (High priority) examples:**
- Page load time ≤ 3 seconds (TC-PERF-001)
- Hover effects display correctly (TC-UI-003)

**P3:** Documented for future execution (not executed due to constraints).

## Test data (high level)

Contact form inputs include:
- Valid: standard emails, names with accents (e.g., José, François), multiple phone formats.
- Invalid/edge: malformed emails, empty/whitespace-only fields, very long strings (255 chars), special characters, basic XSS/SQLi patterns.

## Execution workflow (as used in this project)

1. Execute P1 critical-path tests (manual + automated where applicable).
2. Execute P2 high-priority tests.
3. Exploratory testing on each page (~30 minutes per page).
4. Log defects with evidence (screenshots) and clear reproduction steps.
5. Fix defects and retest.
6. Run the automated regression suite.

## Entry / exit criteria

**Entry criteria**
- Website accessible via local server or file system.
- Browsers installed and configured.
- Test data prepared.
- Automation framework set up and working.
- Bug report template ready.

**Exit criteria**
- All P1 and P2 test cases executed.
- All P1 defects fixed and verified; P2 defects documented (fix if time allows).
- Automated suite passing on Chrome + Firefox.
- Test execution report completed.
- No critical blockers preventing portfolio demonstration.

## Defect management

Bug reports include:
- Summary, steps to reproduce, expected vs actual.
- Environment (browser/device/version).
- Severity/priority, status, retest result.
- Evidence (screenshots).

A sample defect in the test plan: contact form accepting an invalid email format (P2), fixed by updating the validation regex and verified by retest.

## Tools & technologies

- Selenium WebDriver (browser automation)
- Html + CSS + Javascript (demo website)
- Python + pytest (test framework)
- Chrome DevTools (debugging + responsive simulation)
- Git/GitHub (version control)
- VS Code (development)
- Markdown (documentation)

## Repo structure (recommended)

- `QA-portfolio/QA-Manual-Testing/test-plan.md/` — Manual Test Plan (this project’s main document)
- `QA-portfolio/QA-Manual-Testing/test-cases.xlsx/` — Test cases (xlsx/md)
- `QA-portfolio/QA-Manual-Testing/bug_reports/` — Bug reports + evidence (screenshots)
- `QA-portfolio/QA-Automated-Testing/automation/test_navigation.py` — Selenium + pytest code (regression suite)
- `QA-portfolio/QA-Manual-Testing/test_cases.xlsx/tab: Test Execution Summary` — Execution summaries / logs

## Deliverables included

Deliverables for this portfolio project include:
- Test Plan (Markdown)
- Test Cases (spreadsheet)
- Bug Reports (with screenshots)
- Test Execution Summary / results
- Automation code pushed to GitHub

## Notes on constraints (portfolio transparency)

This project intentionally mirrors real QA constraints:
- Limited hardware (1 Windows PC, 1 iPhone).
- Solo tester, no paid tools (free/open-source only).
- Time constraints requiring risk-based prioritization and selective coverage.

It demonstrates practical judgment: quality-over-quantity, clear communication of scope, and automation where it gives the best ROI.