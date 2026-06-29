# Natas Level 3 → 4

## Objective

Find the password for the next level.

---

## Enumeration

* Inspected the webpage and page source.
* Explored common files that may reveal hidden content.
* Accessed the `robots.txt` file.
* Found a disallowed directory listed in `robots.txt`.
* Navigated to the discovered directory.

---

## Observation

The `robots.txt` file revealed the existence of a hidden directory. Inside that directory was a file containing the password for the next level.

---

## Vulnerability

The application relied on obscurity by hiding sensitive content in a directory referenced by `robots.txt`.

The `robots.txt` file is intended to guide search engine crawlers—not to protect sensitive resources. Anyone can access and read it.

---

## Exploitation

1. Opened the `robots.txt` file.
2. Identified a disallowed directory.
3. Visited the directory directly.
4. Located the password file.
5. Used the password to authenticate to the next level.

---

## Prevention

* Never store confidential information in publicly accessible directories.
* Do not rely on `robots.txt` to hide sensitive resources.
* Restrict access using proper authentication and authorization.
* Keep sensitive files outside the public web root whenever possible.

---

## Key Takeaways

* Always check `robots.txt` during web enumeration.
* "Disallow" does not mean "secure."
* Hidden paths can often be discovered through publicly accessible files.
* Security through obscurity is not an effective defense.

---

<details>
<summary><strong>🔑 Password (Spoiler)</strong></summary>

```text
JDrPnuZAKyl6MkiqQGFIddrqpvgOASth
```

</details>
