# Python Detection Lab

## Overview
A Python-based detection engineering lab that simulates brute force attacks against Azure AD accounts, parses sign-in logs, automatically flags suspicious behavior, and generates an incident report. Built as an extension of the Azure AD Sign-In Log Analyzer project.

## Detection Pipeline
```
Raw Logs → Parse → Detect → Report
```

## Scripts

### 01 - Brute Force Simulation
Simulates a brute force attack by generating failed login attempts against a target account. Mirrors the manual login simulation from the Azure AD lab — now automated with Python.

![Brute Force Simulation](screenshots/01-brute-force-simulation.png)

### 02 - Log Parser
Reads raw sign-in log data line by line, extracts structured fields, and counts total events, failures, and successes.

![Log Parser Output](screenshots/02-log-parser-output.png)

### 03 - Anomaly Detector
Applies a configurable threshold to flag accounts with excessive failed logins. Adjust `ALERT_THRESHOLD` to tune sensitivity and reduce false positives.

![Anomaly Alerts](screenshots/04-anomaly-alerts.png)

### 04 - Report Generator
Automatically generates a formatted incident report from the detection findings — including suspicious accounts, source IPs, failure counts, and recommended actions.

![Incident Report](screenshots/05-incident-report.png)

## Troubleshooting & Debugging
Real problem solving documented during the build — a syntax error caught and fixed during development.

![Syntax Error](screenshots/03-syntax-error.png)

## Git Workflow
![Staged Files](screenshots/06-staged-files.png)

## Skills Demonstrated
- Python scripting for security log analysis
- Detection logic with configurable thresholds
- Alert tuning to reduce false positives
- Automated incident report generation
- Debugging and troubleshooting Python scripts
- Professional Git workflow and documentation

## Related Project
This lab extends the [Azure AD Sign-In Log Analyzer](https://github.com/tdt1114/azure-ad-signin-analyzer)
