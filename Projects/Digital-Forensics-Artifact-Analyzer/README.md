# 🔍 Digital Forensics Artifact Analyzer

A modular Python command-line tool that parses authentication logs, analyzes login activity, identifies suspicious IP addresses, and generates structured forensic reports.

Built to demonstrate practical Python programming and cybersecurity automation concepts through a real-world Digital Forensics & Incident Response (DFIR) use case.

---

## ✨ Features

- 📄 Parse authentication log files
- 🚨 Detect and count failed login attempts
- ✅ Track successful login attempts
- 📊 Generate authentication statistics
- 🏆 Display Top-N IP addresses with the highest failed login attempts
- ⚠️ Identify suspicious IPs using configurable thresholds
- 📝 Generate formatted forensic reports
- 🖥️ Command-line interface with customizable options
- 📁 Automatically creates the report directory if it does not exist

---

## 📂 Project Structure

```
Digital-Forensics-Artifact-Analyzer/
│
├── main.py
├── analyzer.py
├── report_generator.py
│
├── parsers/
│   └── auth_parser.py
│
├── sample_logs/
│   └── auth.log
│
├── reports/
│   └── report.txt
│
├── README.md
├── requirements.txt
└── LICENSE
```

---

## 🛠️ Technologies Used

- Python 3
- argparse
- File Handling
- Dictionaries & Lists
- Sorting Algorithms
- Modular Programming

---

## 🚀 Getting Started

### Clone the repository

```bash
git clone https://github.com/<your-username>/Digital-Forensics-Artifact-Analyzer.git

cd Digital-Forensics-Artifact-Analyzer
```

### Run the analyzer

```bash
python main.py sample_logs/auth.log
```

---

## ⚙️ Command-Line Options

| Option | Description | Default |
|------------|------------------------------|-----------|
| `logfile` | Path to authentication log file | Required |
| `--threshold` | Minimum failed attempts to mark an IP as suspicious | `5` |
| `--top_n` | Number of top failed IPs to display | `3` |
| `--savefile` | Output report file location | `reports/report.txt` |

---

## 💻 Example Usage

Basic execution

```bash
python main.py sample_logs/auth.log
```

Display Top 5 failed IPs

```bash
python main.py sample_logs/auth.log --top_n 5
```

Set suspicious threshold

```bash
python main.py sample_logs/auth.log --threshold 10
```

Save report to a custom location

```bash
python main.py sample_logs/auth.log --savefile reports/custom_report.txt
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
192.168.1.10        8
10.0.0.5            4
172.16.0.2          2

========== Log Summary ==========

Total Lines : 250
Failed Logins : 14
Successful Logins : 236
Unique Failed IPs : 3

Top Failed Attempts :

192.168.1.10      -> 8
10.0.0.5          -> 4
172.16.0.2        -> 2

Suspicious IPs (>= 5 Attempts)

192.168.1.10      -> 8
```

---

## 🎯 Skills Demonstrated

This project showcases practical experience with:

- Python Programming
- Command-Line Interface (CLI) Development
- Log Parsing
- Data Analysis
- File Handling
- Modular Software Design
- Exception Handling
- Digital Forensics Fundamentals
- Cybersecurity Automation

---

## 🔮 Future Enhancements

- JSON report export
- CSV report export
- Support for Windows Event Logs
- Apache/Nginx log analysis
- Timeline reconstruction
- Interactive dashboard
- IP geolocation enrichment
- Risk scoring for suspicious activity

---

## 💡 Use Cases

- Authentication log analysis
- Brute-force attack detection
- Digital forensics practice
- Security monitoring
- Python cybersecurity portfolio project

---

## 🤝 Contributing

Contributions and suggestions are welcome.

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Open a Pull Request

---

## 📜 License

This project is licensed under the MIT License.

---

## ⭐ Why This Project?

This project was developed as part of a hands-on cybersecurity learning journey to strengthen practical skills in Python automation, log analysis, and Digital Forensics & Incident Response (DFIR).

It emphasizes clean code organization, modular design, and real-world security use cases while serving as a foundation for future forensic analysis tools.