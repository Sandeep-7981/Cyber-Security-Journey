# Out-of-Band SQL Injection and Prevention

## Introduction

Out-of-Band SQL Injection (OOB SQLi) is a type of SQL Injection where the attacker does not receive the database response through the same web request.

Instead, the database sends information through another communication channel.

Examples:

- DNS requests
- HTTP requests

---

# Why Out-of-Band SQL Injection?

Sometimes normal SQL Injection techniques do not work.

Examples:

- Database errors are hidden
- Application responses do not change
- Time delays are unreliable

In these situations, attackers try to make the database communicate externally.

---

# How Normal SQL Injection Works

In-Band:

```text
Attacker
    |
    v
Website
    |
    v
Database
    |
    v
Result displayed on website
```

The same channel is used.

---

# How Out-of-Band SQL Injection Works

OOB:

```text
Attacker
      |
      v
Application
      |
      v
Database
      |
      v
External Server
      |
      v
Attacker receives data
```

The response comes through a different channel.

---

# Example Scenario

An attacker injects a payload that makes the database perform a DNS lookup.

Example idea:

```text
Send database version to attacker.com
```

The attacker monitors:

```text
attacker.com
```

for incoming requests.

---

# DNS Based Exfiltration

DNS is commonly used because many networks allow DNS traffic.

Example flow:

```text
1. SQL payload executes

2. Database retrieves sensitive data

3. Database creates DNS request

4. Attacker receives request
```

Example leaked request:

```text
adminpassword.attacker.com
```

The attacker extracts:

```text
adminpassword
```

from the DNS logs.

---

# When is OOB SQLi Possible?

Out-of-Band SQL Injection depends on:

- Database features
- Network permissions
- External connections allowed

Not every database environment supports it.

---

# SQL Injection Prevention

The best defense is preventing user input from changing SQL commands.

---

# Prepared Statements

Prepared statements separate:

```text
SQL Code

from

User Data
```

---

## Vulnerable Query

Example:

```sql
SELECT *
FROM users
WHERE username='$username';
```

If input is:

```sql
admin' OR '1'='1
```

The SQL logic changes.

---

## Secure Query

Parameterized query:

```sql
SELECT *
FROM users
WHERE username=?;
```

The input is treated only as data.

It cannot modify the SQL structure.

---

# Input Validation

Validate what users provide.

Example:

If expecting a number:

Allowed:

```text
123
```

Block:

```text
123 OR 1=1
```

---

# Least Privilege Principle

Applications should use database accounts with minimum required permissions.

Bad:

```text
Web App User

Permissions:
READ
WRITE
DELETE
DROP DATABASE
```

---

Better:

```text
Web App User

Permissions:
READ required tables only
```

---

# Error Handling

Do not expose database errors.

Bad:

```text
MySQL Error:

SELECT failed near line 5
table users_passwords
```

This leaks information.

---

Good:

```text
Something went wrong.
Please try again.
```

---

# Web Application Firewall (WAF)

A WAF can detect and block common attack patterns.

Examples:

```sql
OR 1=1

UNION SELECT
```

However:

```text
WAF is an additional layer,
not a replacement for secure coding.
```

---

# Secure Development Checklist

Use:

- Prepared statements
- Input validation
- Least privilege accounts
- Secure error handling
- Regular security testing
- Updated database software

---

# SQL Injection Comparison

| Type | How Data is Retrieved |
|-|-|
| In-Band SQLi | Directly visible response |
| Blind Boolean SQLi | TRUE/FALSE behavior |
| Time-Based SQLi | Response delay |
| Out-of-Band SQLi | External communication |

---

# Attack vs Defense

Attack:

```text
User Input
      |
      v
Changes SQL Query
      |
      v
Database Compromise
```

Defense:

```text
User Input
      |
      v
Parameterized Query
      |
      v
Treated as Data
      |
      v
Safe Execution
```

---

# Key Takeaways

- Out-of-Band SQLi uses a separate channel to retrieve data.
- DNS and HTTP requests are commonly used for OOB attacks.
- OOB depends on database and network configuration.
- Prepared statements are the strongest SQLi prevention.
- Never directly concatenate user input into SQL queries.
- Restrict database permissions.
- Do not reveal database errors.

---

## Practice

Completed:

TryHackMe SQL Injection Introduction

Covered:

- Out-of-Band SQL Injection
- SQL Injection Prevention
- Secure Coding Practices