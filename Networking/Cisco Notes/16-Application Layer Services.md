# 🌐 16. Application Layer Services

## 📖 Definition

The **Application Layer** is the top layer of the network model that allows user applications to communicate over a network.

It provides services that users interact with directly.

**Simple:**  
Application Layer = Interface between users/apps and the network.

---

# 📌 Client-Server Relationship

## Client

A client is a device or software that requests a service.

Examples:
- Web browser
- Email application
- FTP client

## Server

A server provides resources or services to clients.

Examples:
- Web server
- Mail server
- DNS server
- File server


Example:

Browser (Client)
        |
        |
      Request
        |
        ↓
Web Server


---

# 🌍 Web Clients and Servers

Web communication mainly uses:

- HTTP
- HTTPS


## HTTP

Hyper Text Transfer Protocol

Port: 80

Used for transferring webpages.


## HTTPS

HTTP Secure

Port: 443

Uses encryption with SSL/TLS.

Protects:
- Passwords
- Payments
- Sensitive data


---

# 🌐 DNS (Domain Name System)

## Definition

DNS converts human-readable domain names into IP addresses.

Example:


google.com

        ↓ DNS

142.250.xxx.xxx


Humans remember names.  
Computers communicate using IP addresses.


---

## DNS Process

1. User enters website
2. Browser asks DNS server
3. DNS returns IP address
4. Browser connects to server


---

# 📂 FTP (File Transfer Protocol)

## Definition

FTP transfers files between computers over a network.


Ports:

20 → Data transfer  
21 → Control connection


Used for:
- Uploading files
- Downloading files


Security issue:

FTP sends data in plain text.

Secure alternatives:

- SFTP
- FTPS

---

# 💻 Virtual Terminals

Allows users to remotely access another computer.

Examples:

## Telnet

Port: 23

- Remote access protocol
- Not secure
- Sends data unencrypted


## SSH

Port: 22

Secure Shell

Features:
✔ Encrypted connection
✔ Secure remote login
✔ Server management


---

# 📧 Email Services

Email uses multiple protocols.

---

## SMTP

Simple Mail Transfer Protocol

Port: 25

Purpose:
Sending emails


---

## POP3

Post Office Protocol

Port: 110

Purpose:
Downloading emails from server


---

## IMAP

Internet Message Access Protocol

Port: 143

Purpose:
Accessing emails stored on server


---

# 🛡️ Cybersecurity Importance

Application services are common attack targets.

Security professionals analyze:

- Open services
- Vulnerable applications
- Misconfigurations
- Weak authentication


Examples:

Port scan:

nmap target.com


Finding services:

Port 22 open → SSH

Port 80 open → Web server


---

# ⚔️ Common Attacks

## DNS Spoofing

Attacker manipulates DNS responses.

Victim visits fake website.


---

## Brute Force Attack

Repeated login attempts against services.

Targets:

- SSH
- FTP
- Web login


---

## Man-in-the-Middle Attack

Attacker intercepts communication between client and server.


Protection:

Use HTTPS and encryption.


---

# 🔥 Important Ports

| Port | Service |
|-|-|
| 20/21 | FTP |
| 22 | SSH |
| 23 | Telnet |
| 25 | SMTP |
| 53 | DNS |
| 80 | HTTP |
| 110 | POP3 |
| 143 | IMAP |
| 443 | HTTPS |


---

# 🧠 Interview Questions

Q: What does DNS do?

DNS converts domain names into IP addresses.


Q: Difference between HTTP and HTTPS?

HTTPS encrypts communication using TLS.


Q: Why is Telnet insecure?

It transfers data without encryption.


Q: Why is SSH preferred?

SSH provides encrypted remote access.


---

# ⭐ Quick Summary

DNS → Names to IP  
HTTP/HTTPS → Websites  
FTP → File transfer  
SSH → Secure remote access  
SMTP/POP3/IMAP → Email  

Application Layer services are the main targets attackers test during reconnaissance.