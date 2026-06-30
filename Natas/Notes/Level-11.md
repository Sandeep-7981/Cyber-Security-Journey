# Natas Level 11 → 12

## Objective

Retrieve the password for the next level by manipulating the encrypted cookie used by the application.

---

## Enumeration

* Reviewed the webpage source code.
* Identified that user preferences were stored inside a cookie named `data`.
* Observed that the application claimed the cookie was protected using XOR encryption.
* Analyzed how the cookie was encrypted and decrypted before being processed.

---

## Source Code Analysis

The application stores the following default data:

```php
$defaultdata = array(
    "showpassword"=>"no",
    "bgcolor"=>"#ffffff"
);
```

The cookie is encrypted using a repeating XOR key:

```php
function xor_encrypt($in) {
    $key = '<censored>';

    $outText = '';

    for($i = 0; $i < strlen($in); $i++) {
        $outText .= $in[$i] ^ $key[$i % strlen($key)];
    }

    return $outText;
}
```

Before being stored inside the browser, the data is processed as:

```
JSON
   ↓
XOR Encryption
   ↓
Base64 Encoding
   ↓
Cookie
```

During page loading, the reverse process occurs:

```
Cookie
   ↓
Base64 Decode
   ↓
XOR Decryption
   ↓
JSON Decode
```

The application reveals the next password only if:

```php
if($data["showpassword"] == "yes") {
    print "The password for natas12 is <censored>";
}
```

---

## Observation

Although the cookie is encrypted, it is **not authenticated**.

The application blindly trusts whatever is successfully decrypted from the cookie.

Since the cookie structure is known, recovering the repeating XOR key becomes possible using a **Known Plaintext Attack**.

---

## Vulnerability

### Insecure XOR Encryption (Known Plaintext Attack)

The application uses repeating-key XOR encryption without any integrity protection.

Given both:

* the encrypted cookie
* the expected plaintext structure

the XOR key can be recovered using:

```
Key = Ciphertext XOR Plaintext
```

Once the key is recovered, arbitrary cookies can be generated and accepted by the server.

---

## Cookie Analysis

### Original Cookie (URL Encoded)

```text
EGAgHwQ1IxYYMSQYGSZxTUksPFVHYDEQCC0%2FGBlgaVVIJDURDSQ1VRY%3D
```

### After URL Decoding

```text
EGAgHwQ1IxYYMSQYGSZxTUksPFVHYDEQCC0/GBlgaVVIJDURDSQ1VRY=
```

### Known Plaintext

```json
{
    "showpassword":"no",
    "bgcolor":"#ffffff"
}
```

### Modified Plaintext

```json
{
    "showpassword":"yes",
    "bgcolor":"#ffffff"
}
```

### Generated Cookie

```text
EGAgHwQ1IxYYMSQYGSZxTUk7NgRJbnEVDCE8GwQwcU1JYTURDSQ1EUk/
```

---

## Exploitation



### Step 1 - Retrieve the Cookie

Using the browser's Developer Tools, locate the `data` cookie.

**Cookie (URL Encoded)**

```text
EGAgHwQ1IxYYMSQYGSZxTUksPFVHYDEQCC0%2FGBlgaVVIJDURDSQ1VRY%3D
```

---

### Step 2 - URL Decode

The cookie is URL encoded before being stored.

**Input**

```text
EGAgHwQ1IxYYMSQYGSZxTUksPFVHYDEQCC0%2FGBlgaVVIJDURDSQ1VRY%3D
```

↓

**Output**

```text
EGAgHwQ1IxYYMSQYGSZxTUksPFVHYDEQCC0/GBlgaVVIJDURDSQ1VRY=
```

---

### Step 3 - Base64 Decode

Decode the cookie from Base64.

**Input**

```text
EGAgHwQ1IxYYMSQYGSZxTUksPFVHYDEQCC0/GBlgaVVIJDURDSQ1VRY=
```

↓

**Output**

Encrypted binary data.

Since XOR encryption is used, the decoded bytes are not human-readable.

---

### Step 4 - Recover the XOR Key

The expected plaintext is known:

```json
{
    "showpassword":"no",
    "bgcolor":"#ffffff"
}
```

Using

```
Ciphertext XOR Plaintext = Key
```

the repeating XOR key can be recovered.

**Recovered Key**

```text
<Recovered XOR Key>
```

---

### Step 5 - Decrypt the Cookie

Decrypt the encrypted bytes using the recovered XOR key.

**Input**

Encrypted binary data

↓

**Output**

```json
{
    "showpassword":"no",
    "bgcolor":"#ffffff"
}
```

---

### Step 6 - Modify the Cookie

Change

```json
{
    "showpassword":"no",
    "bgcolor":"#ffffff"
}
```

↓

to

```json
{
    "showpassword":"yes",
    "bgcolor":"#ffffff"
}
```

---

### Step 7 - Encrypt the Modified Cookie

Encrypt the modified JSON using the recovered XOR key.

↓

**Output**

Encrypted binary data

---

### Step 8 - Base64 Encode

Encode the encrypted bytes into Base64.

↓

**Generated Cookie**

```text
EGAgHwQ1IxYYMSQYGSZxTUk7NgRJbnEVDCE8GwQwcU1JYTURDSQ1EUk/
```

---

### Step 9 - Replace the Cookie

Replace the original `data` cookie with the generated value.

Refresh the page.

↓

The application now reads:

```json
{
    "showpassword":"yes",
    "bgcolor":"#ffffff"
}
```

↓

The following condition becomes true:

```php
if($data["showpassword"] == "yes")
```

↓

The password for **Natas12** is revealed.

---

## Attack Flow

```
Retrieve Cookie
        │
        ▼
URL Decode
        │
        ▼
Base64 Decode
        │
        ▼
Recover XOR Key
        │
        ▼
Decrypt Cookie
        │
        ▼
Modify JSON
        │
        ▼
Encrypt with XOR Key
        │
        ▼
Base64 Encode
        │
        ▼
Replace Cookie
        │
        ▼
Reveal Password
```

---

## Result

The password for **Natas Level 12** was successfully retrieved after forging a valid encrypted cookie with:

```json
{
    "showpassword":"yes",
    "bgcolor":"#ffffff"
}
```

---

## Prevention

* Never rely on reversible encryption alone to protect client-side data.
* Use authenticated encryption or sign cookies using HMAC.
* Store authorization-related values on the server instead of trusting client-controlled cookies.
* Never make authorization decisions based solely on client-side data.

---

## Key Takeaways

* Encryption does not guarantee integrity.
* Repeating-key XOR is vulnerable to Known Plaintext Attacks.
* Predictable plaintext can reveal the encryption key.
* Sensitive client-side data should always be authenticated.
* Cookie manipulation can lead directly to privilege escalation.

---

<details>
<summary><strong>🔑 Password (Spoiler)</strong></summary>

```text
Username: natas12
Password: EAGkE8uzFTxeoTT2mMst9Xy7PX6guEng
```

</details>