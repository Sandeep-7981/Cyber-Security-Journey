# Natas Level 8 → 9

## Objective

Find the password for the next level.

---

## Enumeration

* Inspected the webpage source code.
* Found the PHP function responsible for validating the submitted secret.
* Analyzed the encoding process used by the application.

---

## Observation

The application did not compare the secret directly. Instead, it encoded the user input using a series of functions and compared the result against a hardcoded encoded value.

By reversing the encoding process, the original secret could be recovered.

---

## Vulnerability

The application relied on reversible encoding to protect a secret.

Encoding is **not encryption**. If an attacker knows the encoding algorithm, they can reverse it and recover the original value.

---

## Exploitation

1. Reviewed the PHP source code.
2. Identified the encoding sequence:

   * `base64_encode()`
   * `strrev()`
   * `bin2hex()`
3. Reversed the operations in the opposite order:

   * Hex Decode
   * Reverse String
   * Base64 Decode
4. Recovered the original secret.
5. Submitted the secret to obtain the password for the next level.

---

## Prevention

* Do not rely on reversible encoding to protect sensitive values.
* Store secrets securely on the server.
* Use proper cryptographic techniques when confidentiality is required.
* Never expose validation logic or secrets in publicly accessible source code.

---

## Key Takeaways

* Encoding is designed for data representation, **not security**.
* Any reversible encoding can be undone if the algorithm is known.
* When reversing nested functions, apply the inverse operations in the reverse order.
* Source code disclosure can expose implementation details that completely bypass application logic.

---

<details>
<summary><strong>🔑 Password (Spoiler)</strong></summary>

```text
UdxmI27dTaXmnd1rxKQTfws6jihTdcQ9
```

</details>
