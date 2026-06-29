# Natas Level 9 → 10

## Objective

Find the password for the next level.

---

## Enumeration

* Inspected the webpage and tested the search functionality.
* Viewed the page source.
* Observed that user input was passed to a PHP function executing a shell command.
* Noticed there was no input sanitization or filtering before execution.

---

## Source Code Analysis

The application executed a command similar to:

```php
passthru("grep -i $key dictionary.txt");
```

Here, `$key` is directly taken from user input.

Since the input is concatenated into the command without validation or escaping, arbitrary shell commands can be executed.

---

## Observation

The application was vulnerable to **OS Command Injection** because user input was directly incorporated into a shell command.

Instead of only searching the dictionary, I could instruct the shell to execute additional commands.

---

## Vulnerability

### OS Command Injection

Command Injection occurs when an application executes operating system commands using unsanitized user input.

Since the shell interprets special characters, an attacker can inject additional commands and execute them with the permissions of the web server.

---

## Exploitation

### Payload Used

```text
; cat /etc/natas_webpass/natas10
```

### Why This Payload Works

The original command executed by the application is similar to:

```bash
grep -i <user_input> dictionary.txt
```

After supplying the payload, the command effectively becomes:

```bash
grep -i ; cat /etc/natas_webpass/natas10 dictionary.txt
```

The semicolon (`;`) tells the shell:

1. Finish executing the current command.
2. Execute the next command.

The injected command:

```bash
cat /etc/natas_webpass/natas10
```

prints the contents of the password file, which the server returns in the HTTP response.

---

## Result

The password for **Natas Level 10** was successfully retrieved from:

```text
/etc/natas_webpass/natas10
```

and used to authenticate to the next level.

---

## Prevention

* Never concatenate user input into shell commands.
* Validate and sanitize all user input.
* Use parameterized APIs or built-in language functions instead of shell commands whenever possible.
* Escape shell arguments if command execution is unavoidable.
* Apply the principle of least privilege to the web server process.

---

## Key Takeaways

* User input should never be trusted.
* Shell metacharacters such as `;`, `&&`, and `|` can alter command execution.
* Reading the source code often reveals how an application processes input.
* Command Injection is one of the most critical web vulnerabilities because it can lead to arbitrary command execution on the server.

---

<details>
<summary><strong>🔑 Password (Spoiler)</strong></summary>

```text
EgjlkzB6E8LJyf2Obt4q7q4ewt5ZWSNv
```

</details>
