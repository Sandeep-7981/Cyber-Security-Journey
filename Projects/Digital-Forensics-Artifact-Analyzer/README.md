# 🔍 Digital Forensics Artifact Analyzer

> **A Python-based Digital Forensics & Incident Response (DFIR) tool for analyzing Linux SSH authentication logs, detecting suspicious login activity, and generating structured investigation reports.**

---

## 📖 Overview

Digital Forensics Artifact Analyzer automates the analysis of Linux SSH authentication logs to identify security threats such as brute-force attacks, username enumeration attempts, and potential account compromise events.

Instead of manually reviewing hundreds of log entries, the tool extracts relevant authentication events, correlates suspicious patterns, and generates an investigation report with actionable security recommendations.

This project demonstrates practical Python programming, log analysis, and Digital Forensics & Incident Response (DFIR) concepts.

---

# 🚀 Quick Start

## Clone the repository

```bash
git clone https://github.com/<your-username>/Digital-Forensics-Artifact-Analyzer.git
cd Digital-Forensics-Artifact-Analyzer
```

## Run the application

```bash
python main.py <log_file_path>
```

### Example

```bash
python main.py sample_logs/sample_auth.log
```

### Optional Arguments

| Argument      | Description                                                   |
| ------------- | ------------------------------------------------------------- |
| `--threshold` | Minimum failed login attempts to classify an IP as suspicious |
| `--top_n`     | Number of top failed IP addresses to display                  |
| `--savefile`  | Output path for the generated investigation report            |

### Example

```bash
python main.py sample_logs/sample_auth.log \
    --threshold 5 \
    --top_n 3 \
    --savefile reports/investigation_report.txt
```

---

# ✨ Features

## Authentication Analysis

* SSH Failed Login Detection
* SSH Successful Login Detection
* Configurable Suspicious IP Threshold

## Threat Detection

* Brute Force Attack Detection
* Username Enumeration Detection
* Success-after-Failure Correlation

## Investigation Support

* Structured Log Summary
* Top Failed Attempts Analysis
* Suspicious IP Identification
* Potential Account Compromise Alerts
* Recent Event Timeline (Latest 5 Events)
* Security Analyst Recommendations
* Automated Investigation Report Generation

---

# 📂 Project Structure

```text
Digital-Forensics-Artifact-Analyzer/

├── analyzers/
│   └── analyzer.py
│
├── parsers/
│   └── auth_parser.py
│
├── reports/
│
├── sample_logs/
│
├── report.py
├── main.py
├── README.md
└── requirements.txt
```

---

# 📊 Detection Capabilities

| Capability                       | Status |
| -------------------------------- | :----: |
| Failed Login Detection           |    ✅   |
| Successful Login Detection       |    ✅   |
| Suspicious IP Analysis           |    ✅   |
| Brute Force Detection            |    ✅   |
| Username Enumeration Detection   |    ✅   |
| Success-after-Failure Detection  |    ✅   |
| Event Timeline Reconstruction    |    ✅   |
| Investigation Report Generation  |    ✅   |
| Security Analyst Recommendations |    ✅   |

---

# 📋 Generated Report

The generated investigation report includes:

* Suspicious Failed Login Analysis
* Log Summary
* Top Failed Attempts
* Suspicious IP Analysis
* Potential Account Compromise Alerts
* Recent Event Timeline
* Security Analyst Recommendations

---

# 🛠 Technologies Used

* Python 3
* Regular Expressions (`re`)
* File Handling
* Dictionaries
* Sets
* Command-Line Arguments (`argparse`)
* Modular Programming

---

# 🎯 Skills Demonstrated

This project demonstrates practical experience with:

* Python Automation
* Digital Forensics Fundamentals
* Linux SSH Authentication Log Analysis
* Security Event Correlation
* Incident Investigation
* Threat Detection Logic
* Report Generation
* Modular Software Design


---

# 🔮 Future Enhancements

* Multi-parser architecture
* Sudo log parser
* CRON log parser
* Apache/Nginx log parser
* JSON/CSV/PDF report export
* IP reputation enrichment
* Interactive dashboard

---

# 🤝 Contributing

Contributions and suggestions are welcome. Feel free to fork the repository, improve the project, and submit a pull request.

---

# 📄 License

This project is released under the MIT License.

---

# 👨‍💻 Author

**Sandeep B**

Cybersecurity • Cloud Security • Digital Forensics Enthusiast

Developed as a portfolio project to demonstrate practical cybersecurity, Python automation, and Digital Forensics & Incident Response (DFIR) concepts.
