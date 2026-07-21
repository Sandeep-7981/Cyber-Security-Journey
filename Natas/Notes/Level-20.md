# Natas Level 20 → 21

## Objective

Retrieve the password for the next level by exploiting a Session Injection vulnerability.

The application stores user-controlled session data using a custom session handler without properly sanitizing user input.

The goal is to inject a new session variable and obtain administrator privileges.

---

## Enumeration

- Reviewed the webpage functionality.
- Found a form allowing users to set their name.
- Submitted normal input and observed that the name persisted across requests.
- Reviewed the source code.
- Identified a custom PHP session handler.
- Observed that session data is written and parsed using a custom text format.
- Identified a possible Session Injection vulnerability.

---

# Source Code Analysis

The application stores the submitted name inside the session.

```php
if(array_key_exists("name", $_REQUEST)) {
    $_SESSION["name"] = $_REQUEST["name"];
}
```

Whenever a session is saved, the custom session handler writes every session variable into a file.

```php
foreach($_SESSION as $key => $value) {
    $data .= "$key $value\n";
}
```

The resulting session file follows the format:

```text
key value
key value
key value
```

Example:

```text
name Sandeep
```

---

## Reading Session Data

When the session is loaded, each line of the session file is processed individually.

```php
foreach(explode("\n", $data) as $line) {
    $parts = explode(" ", $line, 2);

    if($parts[0] != "")
        $_SESSION[$parts[0]] = $parts[1];
}
```

Each line becomes a session variable.

Example:

```text
name Sandeep
admin 1
```

becomes

```php
$_SESSION["name"] = "Sandeep";
$_SESSION["admin"] = "1";
```

---

## Administrator Check

Administrator access depends entirely on the following condition.

```php
if($_SESSION and
   array_key_exists("admin", $_SESSION) and
   $_SESSION["admin"] == 1)
```

If the session contains

```php
$_SESSION["admin"] = 1;
```

the application displays the credentials for the next level.

---

# Vulnerability

## Session Injection

The application directly writes user-controlled input into the session file.

```php
$data .= "$key $value\n";
```

No filtering or escaping is performed on the value.

If the submitted name contains a newline character, the newline becomes a new entry inside the session file.

Instead of storing

```text
name Sandeep
```

an attacker can cause the session file to become

```text
name Sandeep
admin 1
```

When the application later reloads the session, both entries are interpreted as legitimate session variables.

---

# Why Normal Input Doesn't Work

Suppose the submitted name is

```text
Sandeep
```

The session file becomes

```text
name Sandeep
```

When loaded,

```php
$_SESSION["name"] = "Sandeep";
```

No administrator variable exists.

Therefore,

```php
$_SESSION["admin"] == 1
```

evaluates to false.

---

# Exploitation Strategy

Instead of modifying cookies or guessing session IDs, inject an additional session variable.

The session file uses one line per variable.

Therefore, inserting a newline inside the submitted value creates another session entry.

Payload concept:

```text
Sandeep
admin 1
```

The server writes

```text
name Sandeep
admin 1
```

When the session is read back, the parser creates

```php
$_SESSION["name"] = "Sandeep";
$_SESSION["admin"] = "1";
```

The administrator check now succeeds.

---

## Sending a Newline

A newline can be transmitted using URL encoding.

Example:

```text
%0A
```

Example payload:

```text
Sandeep%0Aadmin%201
```

After URL decoding, the application receives

```text
Sandeep
admin 1
```

which becomes two separate session entries.

---

# Attack Flow

```
Open Name Form
        |
        v
Review Source Code
        |
        v
Identify Custom Session Handler
        |
        v
Observe Session File Format
        |
        v
Notice Missing Input Sanitization
        |
        v
Inject Newline Character
        |
        v
Create admin Session Variable
        |
        v
Reload Session
        |
        v
Gain Administrator Access
        |
        v
Retrieve Next Password
```
---

# Challenges Faced

Initially, it appeared that simply modifying the `PHPSESSID` cookie or brute-forcing session IDs would solve the challenge, similar to Natas18 and Natas19.

However, after reviewing the source code, it became clear that the application used a completely different approach for storing session data.

The session handler writes every session variable into a text file and reconstructs the session by reading each line individually.

The challenge was identifying that user input could introduce additional lines into the session file.

Once the custom session format was understood, the vulnerability became straightforward to exploit.

---

# Result

The administrator account was successfully obtained by injecting a new session variable into the session file.

Instead of stealing another user's session, the exploit modified the attacker's own session so that it contained:

```php
$_SESSION["admin"] = "1";
```

The application then treated the current user as an administrator and revealed the credentials for the next level.

---

# Prevention

The vulnerability exists because user-controlled values are written directly into the session file without sanitization.

To prevent this type of attack:

- Never create custom session storage formats unless absolutely necessary.
- Use PHP's built-in session handling instead of implementing custom parsers.
- Validate and sanitize all user input before storing it.
- Escape newline and control characters before writing data to files.
- Store session data using structured formats rather than manually concatenated strings.

For example, instead of

```php
$data .= "$key $value\n";
```

store the session using PHP's built-in serialization or another structured format.

Additionally, reject control characters such as:

```text
\n
\r
\t
```

before storing user input.

---

# Key Takeaways

- PHP sessions can be customized using session handlers.
- Improperly designed session formats can introduce security vulnerabilities.
- User-controlled input should never be written directly into session files.
- Newline characters can be abused to inject additional session variables.
- Session Injection allows privilege escalation without guessing or stealing session IDs.
- Always use PHP's built-in session management whenever possible.

---

<details>
<summary><strong>🔑 Password (Spoiler)</strong></summary>

```text
Username : natas21
Password : 7meHZ1l2zPoK2v1qfTUxq4Ydfja4UlmU
```

</details>