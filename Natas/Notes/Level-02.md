# Natas Level 2 → 3

## Objective

Find the password for the next level.

---

## Enumeration

* Inspected the webpage source.
* Found a reference to an image located inside the `/files` directory.
* Navigated directly to the `/files` directory.
* Explored the available files.

---

## Observation

The web server allowed directory browsing, making the contents of the `/files` directory publicly accessible. One of the files contained the password for the next level.

---

## Vulnerability

The application exposed a directory that allowed users to browse its contents.

Directory listing can unintentionally reveal sensitive files, configuration data, backups, credentials, or other information that should not be publicly accessible.

---

## Exploitation

1. Viewed the page source.
2. Identified a file path pointing to the `/files` directory.
3. Opened the directory in the browser.
4. Located the file containing the password.
5. Used the password to access the next level.

---

## Prevention

* Disable directory listing on the web server.
* Store sensitive files outside the web root.
* Restrict access to confidential resources using proper server-side permissions.
* Avoid exposing internal directory structures.

---

## Key Takeaways

* Always inspect resource paths referenced by a webpage.
* Directory enumeration is an important step during web application testing.
* Directory listing can expose sensitive information if left enabled.
* Never assume hidden directories are inaccessible.

---

<details>
<summary><strong>🔑 Password (Spoiler)</strong></summary>

```text
K30JrSRHzjxq3paUQuwozY4MNvmNFyhI
```

</details>
