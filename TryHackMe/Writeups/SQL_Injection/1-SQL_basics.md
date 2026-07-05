# SQL Injection Basics

## Introduction

SQL Injection (SQLi) is a web security vulnerability where an attacker can manipulate SQL queries executed by an application.

It happens when user input is directly added into database queries without proper validation.

A successful SQL Injection attack can allow an attacker to:

- Access sensitive data
- Bypass authentication
- Modify database records
- Delete information

---

# What is SQL?

SQL (Structured Query Language) is used to communicate with databases.

Web applications use SQL to:

- Store user information
- Retrieve data
- Update records
- Delete records

Example:

A website login system may store:

| id | username | password |
|---|---|---|
|1|admin|admin123|
|2|user|pass123|

---

# Basic SQL Commands

## SELECT

Used to retrieve data from a database.

Example:

```sql
SELECT username
FROM users;
```

Returns all usernames from the users table.

---

Selecting everything:

```sql
SELECT *
FROM users;
```

`*` means all columns.

---

## WHERE Clause

Used to filter results.

Example:

```sql
SELECT *
FROM users
WHERE username='admin';
```

Only returns rows where:

```text
username = admin
```

---

# SQL in Web Applications

A normal login system may execute:

```sql
SELECT *
FROM users
WHERE username='admin'
AND password='admin123';
```

If the database finds a matching user:

```text
Login Successful
```

If no record matches:

```text
Invalid Credentials
```

---

# What Causes SQL Injection?

SQL Injection happens when user input becomes part of the SQL command.

Example vulnerable query:

```sql
SELECT *
FROM users
WHERE username='$input';
```

The application trusts the user input.

---

# Authentication Bypass Example

Normal input:

Username:

```text
admin
```

Password:

```text
hello123
```

Query:

```sql
SELECT *
FROM users
WHERE username='admin'
AND password='hello123';
```

If the password is wrong:

```text
Login Failed
```

---

## Injected Input

Username:

```sql
admin'--
```

The query becomes:

```sql
SELECT *
FROM users
WHERE username='admin'--
AND password='hello123';
```

---

The symbols:

```sql
--
```

start a comment in SQL.

Everything after it is ignored.

So the database only checks:

```sql
username='admin'
```

The password check is removed.

Authentication can be bypassed.

---

# Always True Conditions

Another common payload:

```sql
' OR '1'='1
```

Original query:

```sql
SELECT *
FROM users
WHERE username=''
OR '1'='1';
```

The condition:

```sql
1=1
```

is always TRUE.

Therefore the database returns results.

---

# SQL Comments

Comments are used to ignore the remaining SQL query.

Common comment styles:

```sql
--
```

```sql
#
```

```sql
/*
comment
*/
```

Example:

```sql
admin'--
```

The remaining query is ignored.

---

# Types of SQL Injection

Common SQL Injection categories:

## 1. In-Band SQL Injection

The attacker uses the same request to:

- Send the attack
- Receive the result

Examples:

- Error-Based SQL Injection
- UNION-Based SQL Injection

---

## 2. Blind SQL Injection

The database does not directly show output.

Information is extracted using:

- TRUE/FALSE responses
- Time delays

Examples:

- Boolean-Based SQL Injection
- Time-Based SQL Injection

---

## 3. Out-of-Band SQL Injection

The attacker receives data through a different channel.

Examples:

- DNS requests
- HTTP callbacks

---

# Why SQL Injection is Dangerous

SQL Injection can lead to:

- Data leaks
- Account takeover
- Authentication bypass
- Database modification
- Complete system compromise

---

# Prevention

## Prepared Statements

The best defense is using parameterized queries.

Unsafe:

```sql
"SELECT * FROM users WHERE username='" + input + "'"
```

Safe:

```sql
SELECT *
FROM users
WHERE username=?;
```

The database treats input as data, not executable SQL.

---

Other protections:

- Validate user input
- Limit database permissions
- Avoid showing database errors
- Use secure coding practices

---

# Key Takeaways

- SQL is used by applications to communicate with databases.
- SQL Injection happens when input changes the intended query.
- Attackers can bypass authentication using manipulated queries.
- Comments can remove unwanted parts of SQL statements.
- SQL Injection can expose sensitive information.
- Prepared statements prevent SQL Injection.

---

## Practice

Completed:

- TryHackMe SQL Injection Introduction
- SQL Basics
- Authentication Bypass Concepts