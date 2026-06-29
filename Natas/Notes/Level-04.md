# Natas Level 4 → 5

## Objective

Find the password for the next level.

---

## Enumeration

* Read the message displayed on the webpage.
* Identified that access depended on the HTTP request headers.
* Intercepted the request using **Burp Suite**.
* Examined the request headers.

---

## Observation

The application checked the value of the **`Referer`** HTTP header before granting access.

Since HTTP headers are controlled by the client, the `Referer` value could be modified to satisfy the application's check.

---

## Vulnerability

The application trusted a client-controlled HTTP header for authentication or authorization.

HTTP headers such as `Referer` can be modified easily using tools like Burp Suite, making them unsuitable for enforcing security decisions.

---

## Exploitation

1. Intercepted the request with **Burp Suite**.
2. Modified the `Referer` header to the expected value.
3. Forwarded the modified request.
4. The server accepted the request and revealed the password.

---

## Prevention

* Never rely on the `Referer` header for authentication or authorization.
* Implement proper server-side access control.
* Treat all client-supplied headers as untrusted input.

---

## Key Takeaways

* HTTP headers can be modified by the client.
* The `Referer` header should never be trusted for security decisions.
* Burp Suite is a powerful tool for intercepting and modifying HTTP requests.
* Security must always be enforced on the server side.

---

<details>
<summary><strong>🔑 Password (Spoiler)</strong></summary>

```text
e4z2Noy3oqwPJUWzJH0dseN67Cn1sy2M
```

</details>
