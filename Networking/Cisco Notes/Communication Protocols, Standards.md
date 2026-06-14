# 🌐 Communication Protocols, Standards, and Models

---

# 📖 Communication Protocols

## Definition

A **communication protocol** is a set of rules that defines how devices exchange data over a network.

**Simple:** Protocols are the language that computers use to communicate.

---

# 📌 Why Protocols are Important

* Enable communication between different devices
* Ensure reliable data transfer
* Standardize data exchange
* Detect and recover from errors

---

# 📚 Common Communication Protocols

## HTTP (HyperText Transfer Protocol)

Used to access websites.

**Default Port:** 80

Example

```text
http://example.com
```

Not encrypted.

---

## HTTPS (HyperText Transfer Protocol Secure)

Secure version of HTTP.

**Default Port:** 443

Uses SSL/TLS encryption.

Example

```text
https://github.com
```

---

## FTP (File Transfer Protocol)

Used to transfer files between computers.

**Ports:** 20 & 21

Example

Uploading website files.

---

## SSH (Secure Shell)

Used for secure remote access.

**Port:** 22

Commonly used by Linux administrators.

---

## DNS (Domain Name System)

Converts domain names into IP addresses.

```text
google.com

↓

142.250.xxx.xxx
```

**Port:** 53

---

## DHCP (Dynamic Host Configuration Protocol)

Automatically assigns IP addresses to devices.

**Ports:** 67 & 68

---

# 🏛️ Communication Standards

## Definition

Communication standards ensure that networking devices from different manufacturers work together correctly.

Without standards, interoperability would not be possible.

---

# 📌 Standard Organizations

## IEEE

Develops LAN and Wireless standards.

Examples

* IEEE 802.3 → Ethernet
* IEEE 802.11 → Wi-Fi

---

## IETF

Develops Internet protocols.

Examples

* TCP/IP
* IPv4
* IPv6

---

## ISO

Created the OSI Reference Model.

---

## ICANN

Responsible for

* Domain Names
* IP Address Allocation

---

# 🌐 Network Communication Models

Models provide a structured way to understand how data moves through a network.

---

# OSI Model (7 Layers)

```text
Application
Presentation
Session
Transport
Network
Data Link
Physical
```

### Easy Memory

**All People Seem To Need Data Processing**

---

## Layer Functions

| Layer        | Function                     |
| ------------ | ---------------------------- |
| Application  | User Services                |
| Presentation | Data Formatting & Encryption |
| Session      | Session Management           |
| Transport    | Reliable Delivery            |
| Network      | Routing (IP Address)         |
| Data Link    | MAC Address & Frames         |
| Physical     | Bits & Transmission Media    |

---

# TCP/IP Model

```text
Application

Transport

Internet

Network Access
```

Used by the Internet.

---

# OSI vs TCP/IP

| OSI              | TCP/IP                |
| ---------------- | --------------------- |
| 7 Layers         | 4 Layers              |
| Reference Model  | Practical Model       |
| Developed by ISO | Developed by DoD/IETF |

---

# 📦 Data Encapsulation

As data travels through the network, each layer adds its own header.

```text
Application Data

↓

Segment

↓

Packet

↓

Frame

↓

Bits
```

At the receiver, headers are removed in reverse order (Decapsulation).

---

# 🔄 Communication Process

Example: Opening GitHub

```text
User

↓

HTTPS Request

↓

DNS resolves Domain

↓

TCP establishes Connection

↓

IP routes Packet

↓

Ethernet/Wi-Fi sends Bits

↓

GitHub Server

↓

Response Returned
```

---

# 📋 Common Protocols & Ports

| Protocol | Port  | Purpose             |
| -------- | ----- | ------------------- |
| HTTP     | 80    | Web                 |
| HTTPS    | 443   | Secure Web          |
| FTP      | 20/21 | File Transfer       |
| SSH      | 22    | Secure Remote Login |
| DNS      | 53    | Domain Resolution   |
| DHCP     | 67/68 | IP Assignment       |

---

# 💡 Real-Life Example

Typing

```text
https://github.com
```

Steps

1. DNS finds the IP address.
2. TCP establishes a reliable connection.
3. HTTPS encrypts communication.
4. Data travels through OSI/TCP-IP layers.
5. Webpage is displayed.

---

# 🧠 Remember This

```text
Protocol

↓

Rules

↓

Standard

↓

Compatibility

↓

Model

↓

How Communication Happens
```

---

# 🎤 Interview Q&A

### What is a communication protocol?

A communication protocol is a set of rules that enables devices to exchange data over a network.

---

### What is the difference between HTTP and HTTPS?

HTTP transfers data without encryption, whereas HTTPS encrypts communication using SSL/TLS.

---

### Which organization developed Ethernet standards?

IEEE developed Ethernet (802.3) and Wi-Fi (802.11) standards.

---

### Which organization developed the OSI Model?

ISO (International Organization for Standardization).

---

### Difference between OSI and TCP/IP Models?

| OSI             | TCP/IP                   |
| --------------- | ------------------------ |
| 7 Layers        | 4 Layers                 |
| Reference Model | Practical Internet Model |

---

### Which protocol converts domain names into IP addresses?

DNS (Domain Name System).

---

### Which protocol automatically assigns IP addresses?

DHCP (Dynamic Host Configuration Protocol).

---

### What is encapsulation?

Encapsulation is the process of adding protocol headers to data as it moves down the networking layers before transmission.

---

# ⚡ Quick Revision

```text
Protocols

HTTP  → 80

HTTPS → 443

FTP   → 20/21

SSH   → 22

DNS   → 53

DHCP  → 67/68

----------------------------

Standards

IEEE → Ethernet & Wi-Fi

ISO → OSI Model

IETF → Internet Protocols

ICANN → Domain Names

----------------------------

Models

OSI → 7 Layers

TCP/IP → 4 Layers
```

---

# 📌 Exam Tips

✅ Protocol = Rules of communication

✅ Standard = Ensures compatibility

✅ Model = Explains communication process

✅ OSI has 7 layers

✅ TCP/IP has 4 layers

✅ HTTP is not encrypted

✅ HTTPS uses SSL/TLS

✅ DNS converts Domain → IP

✅ DHCP automatically assigns IP addresses

✅ Encapsulation: Data → Segment → Packet → Frame → Bits

---

**Related Topics:** OSI Model • TCP/IP Model • Common Ports • Network Protocols • Encapsulation
