# Natas Level 5 → 6

## Objective

Find the password for the next level.

---

## Enumeration

* Inspected the webpage and its response.
* Used **Burp Suite** to intercept the HTTP request and response.
* Observed the cookies sent by the server.
* Identified a cookie controlling the application's access logic.

---

## Observation

The application stored the access state inside a client-side cookie. By modifying the cookie value and resending the request, the server granted access to the protected content.

---

## Vulnerability

The application trusted a client-controlled cookie to determine whether the user had the required access.

Since cookies are stored on the client, they can be viewed and modified using browser developer tools or proxy tools like Burp Suite.

---

## Exploitation

1. Intercepted the request using **Burp Suite**.
2. Examined the cookies sent with the request.
3. Modified the cookie value responsible for access control.
4. Forwarded the request.
5. The server accepted the modified cookie and revealed the password.

---

## Prevention

* Never rely on client-side cookies for authorization decisions.
* Store authorization state on the server.
* Validate user permissions using server-side session management.
* Sign or encrypt cookies if they contain important data, but avoid storing authorization flags directly in them.

---

## Key Takeaways

* Cookies are fully controlled by the client.
* Client-side cookies should never be trusted for authorization.
* Burp Suite makes it easy to inspect and modify cookies.
* Access control must always be enforced on the server.

---

<details>
<summary><strong>🔑 Password (Spoiler)</strong></summary>

```text
7mhjtShJAcld2NYbKHEadnhEwRn2P8VT
```

</details>
