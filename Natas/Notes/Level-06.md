# Natas Level 6 → 7

## Objective

Find the password for the next level.

---

## Enumeration

* Inspected the webpage and reviewed its source code.
* Identified an external file included by the application.
* Opened the referenced file directly in the browser.
* Analyzed the source code to understand how the application validated user input.

---

## Observation

The application's source code was separated into multiple files. The included file contained a secret value used by the application for validation.

Although the secret was not displayed on the webpage, it was publicly accessible because the source file could be requested directly.

---

## Vulnerability

The application exposed sensitive information inside a publicly accessible source file.

Keeping secrets in files that are accessible from the web server allows attackers to retrieve them and bypass application logic.

---

## Exploitation

1. Viewed the page source.
2. Found a referenced source file.
3. Opened the file directly.
4. Retrieved the secret used by the application.
5. Submitted the secret to obtain the password for the next level.

---

## Prevention

* Never store secrets in publicly accessible files.
* Keep configuration files and sensitive data outside the web root.
* Restrict direct access to internal source files.
* Use server-side secret management for sensitive values.

---

## Key Takeaways

* Always inspect files referenced by a webpage.
* Included source files can reveal sensitive implementation details.
* Security through hidden files is ineffective if those files are publicly accessible.
* Source code disclosure can lead directly to compromise.

---

<details>
<summary><strong>🔑 Password (Spoiler)</strong></summary>

```text
B1szg95UcTnrzwnF3i3TzYHlyYh8iBV0
```

</details>
