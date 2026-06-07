# Digital Forensics Artifact Analyzer

A Python-based Digital Forensics and Incident Response (DFIR) project that parses Linux authentication logs and extracts useful security information.

## Features

- Parse Linux auth.log entries
- Extract timestamps
- Extract usernames
- Extract IP addresses
- Detect login status (Failed/Accepted)
- Store parsed data in structured dictionaries

## Technologies

- Python
- Regular Expressions
- Dictionaries
- File Handling

## Example Output

```python
{
    "timestamp": "Jun 07 09:15:10",
    "status": "Failed",
    "username": "admin",
    "ip": "192.168.1.10"
}
```

## Future Features

- Failed login analysis
- Brute-force detection
- Report generation
- Timeline creation
- Multi-artifact support

## Author
B V V Sandeep