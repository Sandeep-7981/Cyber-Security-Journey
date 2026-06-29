# Natas Level 1 → 2

## Objective

Find the password for the next level.

---

## Enumeration

* Attempted to inspect the page using the right-click menu.
* Noticed that right-click was disabled.
* Used the keyboard shortcut **Ctrl + U** to view the page source.

---

## Observation

The webpage prevented users from opening the context menu, but this restriction only affected the user interface. The page source remained accessible through browser shortcuts, revealing the password.

---

## Vulnerability

The application relied on a client-side restriction (disabling right-click) to protect sensitive information.

Since browser shortcuts and developer tools cannot be effectively blocked this way, the password was still exposed in the HTML source.

---

## Exploitation

1. Pressed **Ctrl + U** to open the page source.
2. Searched the HTML for sensitive information.
3. Retrieved the password.
4. Used it to authenticate to the next level.

---

## Prevention

* Never rely on client-side restrictions for security.
* Avoid storing secrets in HTML or JavaScript.
* Implement access control and secret management on the server side.

---

## Key Takeaways

* Client-side protections are easily bypassed.
* Browser shortcuts such as **Ctrl + U** can still reveal page source.
* Sensitive data should never be delivered to the client unless absolutely necessary.

---

<details>
<summary><strong>🔑 Password (Spoiler)</strong></summary>

```text
vsDOxoXyq3wckCP1ZmTZ71ngIA606odB
```

</details>
