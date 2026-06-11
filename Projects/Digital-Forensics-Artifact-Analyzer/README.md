# 🔐 Digital Forensics Artifact Analyzer

A beginner-friendly **Python-based Digital Forensics & Log Analysis tool** that parses Linux authentication logs (`auth.log`) and generates a concise security report.

This project was built as part of my **Cyber Security Journey** to strengthen Python programming, DFIR concepts, and Security Operations Center (SOC) fundamentals through hands-on projects.

---

## 📌 Features

### ✅ Authentication Log Parsing

- Extracts Timestamp
- Extracts Username
- Extracts IP Address
- Detects Login Status (Failed / Successful)

### ✅ Login Analysis

- Total Log Lines
- Total Failed Logins
- Total Successful Logins
- Unique Failed IP Count

### ✅ Threat Detection

- Top Failed IP Addresses
- Suspicious IP Detection using configurable threshold
- Failed Login Report

---

## 📂 Project Structure

```
Log_Analyzer/
│
├── main.py
│
├── parsers/
│   └── auth_parser.py
│
├── samples/
│   └── auth.log
│
└── README.md
```

---

## 🛠 Technologies Used

- Python 3
- Regular Expressions (`re`)
- Dictionaries
- Lists & Tuples
- Lambda Functions
- File Handling

---

## 🚀 How It Works

```
Authentication Log
        │
        ▼
Parse Log Entry
        │
        ▼
Extract:
• Timestamp
• Username
• IP Address
• Login Status
        │
        ▼
Generate Statistics
        │
        ├── Failed Login Report
        ├── Log Summary
        ├── Top Failed IPs
        └── Suspicious IP Detection
```

---

## 📊 Sample Output

```
========================================
DIGITAL FORENSICS ARTIFACT ANALYZER
========================================

Suspicious Failed Login Report

IP Address          Failed Attempts
-----------------------------------
192.168.1.10        18
172.16.5.2          2

-----------------------------------

========== Log Summary ==========

Total Lines : 28
Failed Logins : 20
Successful Logins : 8
Unique Failed IPs : 2

Top Failed Attempts :

192.168.1.10        -> 18
172.16.5.2          -> 2

Suspicious IPs (>= 5 Attempts)

192.168.1.10        -> 18

-----------------------------------
```

---

## ⚙ Configuration

The suspicious login threshold can be modified from:

```python
THRESHOLD = 5
```

Any IP with failed attempts greater than or equal to this value is flagged as suspicious.

---

## 🧠 Concepts Practiced

- Python File Handling
- Dictionaries
- Loops & Conditional Statements
- Functions
- Modular Programming
- Regular Expressions
- Sorting using `sorted()`
- Lambda Functions
- Tuple Unpacking
- Basic DFIR Log Analysis

---

## 🎯 Learning Objectives

This project was built to understand how Security Analysts and DFIR professionals process authentication logs to identify:

- Repeated failed login attempts
- Suspicious source IPs
- Brute-force indicators
- Authentication statistics

---

## 🔮 Future Enhancements

- [ ] Top Targeted Usernames
- [ ] Timestamp-based Brute Force Detection
- [ ] Export Report to TXT/CSV
- [ ] Command Line Arguments
- [ ] Support for Multiple Log Files
- [ ] Risk Scoring
- [ ] Interactive Dashboard

---

## 👨‍💻 Author

**Sandeep B**

Cyber Security | Cloud Security | DFIR Enthusiast

This project is part of my public **Cyber Security Journey**, where I document my progress by building practical security tools and learning through hands-on projects.

---

⭐ If you found this project useful or interesting, feel free to explore the repository and follow my cybersecurity journey!