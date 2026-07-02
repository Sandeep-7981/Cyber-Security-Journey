# Google Search Operators (Google Dorking)

## What is Google Dorking?

When we search normally on Google, Google searches **billions of web pages** and shows the most relevant ones.

Example:

```
python regex
```

returns millions of results.

But what if you want to search:

- only inside GitHub?
- only PDF files?
- only pages containing "login"?
- only a particular company's website?

That's where **Google Search Operators** come in.

Search operators are special keywords that tell Google **how to search instead of what to search.**

Think of them as filters.

---

# Example Scenario

Suppose you're performing an authorized security assessment for a fictional company:

```
example.com
```

Instead of manually opening hundreds of pages, you can ask Google to search smarter.

---

# 1. site:

## Purpose

Search only inside one website.

### Syntax

```
site:domain keyword
```

Example:

```
site:example.com login
```

Google now ignores every other website and searches only inside **example.com**.

Without operator:

```
login
```

Results:

```
example.com
facebook.com
github.com
reddit.com
instagram.com
...
```

With operator:

```
site:example.com login
```

Results:

```
example.com/login

example.com/admin/login

example.com/help/login
```

Notice how Google completely ignores every other website.

---

## Practical Use

Imagine a company has thousands of pages.

Instead of navigating manually, you can search:

```
site:example.com internship
```

or

```
site:example.com careers
```

or

```
site:example.com cybersecurity
```

Much faster.

---

# 2. filetype:

## Purpose

Search only specific file types.

Google indexes many documents.

Examples include:

- PDF
- DOCX
- PPT
- XLSX

Suppose you only want PDF files.

```
filetype:pdf network security
```

Results might include:

```
Network Security Notes.pdf

Firewall Guide.pdf

CCNA Handbook.pdf
```

Google ignores HTML pages.

---

## Practical Example

Suppose you're preparing for an exam.

Instead of searching

```
network security
```

search

```
network security filetype:pdf
```

You'll mostly get books, notes and research papers.

---

# Combining Operators

Operators become much more powerful when combined.

Example:

```
site:gov.in filetype:pdf cyber security
```

Meaning:

```
Search only government websites

↓

Only PDF documents

↓

Containing cyber security
```

Google applies every filter together.

---

# 3. intitle:

Every webpage has a title.

Example:

```
Python Documentation

Linux Commands

Introduction to Networking
```

Google can search only titles.

Example:

```
intitle:"network security"
```

Now Google searches pages whose titles contain

```
Network Security
```

instead of searching the entire page.

---

## Practical Example

Suppose you're looking for tutorials.

```
intitle:"python regex"
```

Results:

```
Python Regex Tutorial

Python Regex Guide

Python Regex Explained
```

Much cleaner results.

---

# 4. inurl:

Every webpage has a URL.

Example:

```
example.com/login

example.com/admin

example.com/downloads

example.com/blog
```

Google can search URLs.

Example:

```
inurl:login
```

Results:

```
company.com/login

portal.example/login

student.edu/login
```

Only URLs containing

```
login
```

---

## Practical Example

Searching documentation.

```
site:python.org inurl:docs
```

returns documentation pages much faster.

---

# 5. intext:

Instead of title or URL,

Google searches the actual page content.

Example:

```
intext:"incident response"
```

Google returns pages where

```
Incident Response
```

appears in the article.

---

# 6. ""

Quotation Marks

Without quotes

```
network security
```

Google treats them as separate words.

It may show

```
network configuration

security cameras

computer networks
```

With quotes

```
"network security"
```

Google searches the exact phrase.

This makes searches much more accurate.

---

# 7. OR

Suppose you're interested in either Python or Bash.

```
Python OR Bash
```

Google returns pages containing either one.

Useful when multiple terms mean similar things.

---

# 8. -

The minus sign excludes words.

Example

```
python security -tutorial
```

Google removes pages containing

```
tutorial
```

Useful when unwanted results dominate your search.

---

# Real-World OSINT Examples

## Example 1

Find cybersecurity PDFs from universities.

```
site:edu filetype:pdf cybersecurity
```

Meaning:

```
Only educational websites

↓

Only PDFs

↓

Related to cybersecurity
```

---

## Example 2

Find Linux presentations.

```
filetype:ppt linux
```

---

## Example 3

Search only GitHub.

```
site:github.com python log parser
```

Instead of searching GitHub manually.

---

## Example 4

Find official AWS documentation.

```
site:aws.amazon.com IAM
```

---

## Example 5

Search documentation only.

```
site:docs.python.org regex
```

---

# Combining Everything

Example:

```
site:github.com filetype:md "SQL Injection"
```

Let's break it down.

```
site:github.com
```

↓

Only GitHub

```
filetype:md
```

↓

Only Markdown files

```
"SQL Injection"
```

↓

Containing the exact phrase "SQL Injection"

Final result:

Only GitHub Markdown files discussing SQL Injection.

---

# Tips

✔ Start with simple searches.

✔ Add one operator at a time.

✔ Combine operators only when necessary.

✔ Think of operators as filters.

✔ More filters = More specific results.

---

# Key Takeaways

- Search operators tell Google **how** to search.
- They reduce irrelevant results.
- Multiple operators can be combined.
- They are one of the most powerful tools in OSINT and reconnaissance.
- Always use them ethically and only for authorized research.