# Natas Level 0 → 1

## Objective

Find the password for the next level.

---

## Enumeration

* Logged into the challenge.
* Inspected the webpage.
* Opened the page source.

---

## Observation

The webpage itself did not display the password, but the HTML source contained additional information.

---

## Vulnerability

Sensitive information was exposed directly in the client-side HTML source.

Although hidden from normal page view, it was still delivered to the browser, making it accessible to anyone inspecting the source.

---

## Exploitation

1. Opened **View Page Source**.
2. Located the password within the HTML.
3. Used it to authenticate to the next level.

---

## Prevention

* Never store passwords or secrets in HTML.
* Sensitive data should remain on the server.
* Anything sent to the client should be considered public.

---

## Key Takeaways

* Always inspect the page source during enumeration.
* Client-side code should never contain confidential information.
* Hidden does **not** mean secure.

---

<details>
<summary><strong>🔑 Password (Spoiler)</strong></summary>

```text
scfWG6qNEIdzqVyfRwEGXyNUfFZkZeQ7
```

</details>
