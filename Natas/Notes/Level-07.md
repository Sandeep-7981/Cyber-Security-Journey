# Natas Level 7 → 8

## Objective

Find the password for the next level.

---

## Enumeration

* Inspected the webpage source.
* Identified directory and file paths referenced within the HTML.
* Explored the referenced directories.
* Located the file containing the password.

---

## Observation

The page source revealed internal directory paths that were not directly visible through the webpage interface. Exploring these locations led to the password for the next level.

---

## Vulnerability

The application exposed internal file paths through its source code.

Although the directories were not linked on the webpage, they remained publicly accessible. This allowed an attacker to enumerate the application's structure and retrieve sensitive information.

---

## Exploitation

1. Viewed the page source.
2. Identified referenced directories and files.
3. Navigated to the exposed locations.
4. Retrieved the password.
5. Used it to authenticate to the next level.

---

## Prevention

* Avoid exposing unnecessary internal paths in client-side code.
* Restrict access to sensitive directories and files.
* Store confidential information outside the publicly accessible web root.
* Apply proper server-side authorization to protected resources.

---

## Key Takeaways

* Source code often reveals valuable information during reconnaissance.
* Always investigate referenced directories and files.
* Enumeration is a critical phase of web application security testing.
* Sensitive resources should never be publicly accessible simply because they are "hidden."

---

<details>
<summary><strong>🔑 Password (Spoiler)</strong></summary>

```text
ugXL95KQmUAJJj6bMezOlBNDyI9Imwkc
```

</details>
