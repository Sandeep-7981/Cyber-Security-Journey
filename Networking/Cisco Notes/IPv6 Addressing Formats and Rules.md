# 🌐 IPv6 Addressing Formats and Rules

---

# 📖 Why IPv6?

IPv4 has been used for decades, but the rapid growth of the Internet has created a need for more IP addresses.

IPv6 was introduced to solve this problem.

---

# 🌍 IPv4 Issues

## 1. Address Exhaustion

IPv4 uses **32-bit addresses**, which provide approximately **4.3 billion unique addresses**.

With billions of smartphones, computers, IoT devices, and servers, IPv4 addresses are running out.

---

## 2. Large Number of Internet Devices

Examples

* Smartphones
* Smart TVs
* Laptops
* IoT Devices
* Smart Watches
* Security Cameras

Every device requires a unique IP address.

---

## 3. NAT Dependency

IPv4 often relies on **Network Address Translation (NAT)** to allow multiple devices to share a single public IP.

Although useful, NAT increases network complexity.

---

# 📖 IPv6

## Definition

**IPv6 (Internet Protocol Version 6)** is the latest version of the Internet Protocol designed to overcome IPv4 limitations.

### Characteristics

* 128-bit address
* Uses hexadecimal numbers
* Almost unlimited address space
* Improved security and efficiency

---

# 📌 IPv6 Address Structure

IPv6 consists of **8 groups**, each containing **4 hexadecimal digits**.

Example

```text
2001:0db8:85a3:0000:0000:8a2e:0370:7334
```

```text
2001 : 0db8 : 85a3 : 0000 : 0000 : 8a2e : 0370 : 7334
  │       │       │       │       │       │       │
 Group1 Group2 Group3 Group4 Group5 Group6 Group7 Group8
```

---

# 🔢 Hexadecimal System

IPv6 uses hexadecimal values.

```text
Decimal

0 1 2 3 4 5 6 7 8 9

↓

Hexadecimal

0 1 2 3 4 5 6 7 8 9 A B C D E F
```

---

# ✂️ Rule 1 : Omit Leading Zeros

Leading zeros in any group can be removed.

Example

```text
Original

2001:0db8:0000:0000:0000:ff00:0042:8329

↓

Compressed

2001:db8:0:0:0:ff00:42:8329
```

---

# ✂️ Rule 2 : Double Colon (::)

One or more consecutive groups containing only zeros can be replaced by **::**

This shortcut can be used **only once** in an IPv6 address.

Example

```text
Original

2001:0db8:0000:0000:0000:ff00:0042:8329

↓

Compressed

2001:db8::ff00:42:8329
```

---

# 📍 IPv6 Prefix Length

Instead of subnet masks, IPv6 uses **prefix length**.

Example

```text
2001:db8:acad:1::1/64
```

Meaning

* First 64 bits → Network Prefix
* Remaining 64 bits → Interface ID

---

# 📋 Types of IPv6 Addresses

## Global Unicast

Public IPv6 address.

Routable over the Internet.

Example

```text
2001:db8::1
```

---

## Link-Local

Used for communication within the same local network.

Automatically assigned.

Always begins with

```text
FE80::
```

Example

```text
FE80::1A2B:3C4D:5E6F:7890
```

---

## Multicast

Used to send data to multiple devices simultaneously.

Starts with

```text
FF00::
```

IPv6 does **not use Broadcast**.

---

## Loopback Address

Used for testing the local device.

```text
::1
```

Equivalent to IPv4

```text
127.0.0.1
```

---

## Unspecified Address

Represents the absence of an address.

```text
::
```

Equivalent to

0.0.0.0 in IPv4.

---

# 📊 IPv4 vs IPv6

| IPv4                   | IPv6                     |
| ---------------------- | ------------------------ |
| 32-bit                 | 128-bit                  |
| Decimal                | Hexadecimal              |
| ~4.3 Billion Addresses | Almost Unlimited         |
| Supports Broadcast     | No Broadcast             |
| Uses NAT Frequently    | NAT Usually Not Required |

---

# 💡 Real-Life Example

```text
Laptop

IPv4

192.168.1.10

↓

IPv6

2001:db8:acad:1::10
```

Modern operating systems usually support both IPv4 and IPv6.

---

# 🧠 Remember This

```text
IPv4

32 Bits

↓

4 Octets

↓

Decimal

---------------------

IPv6

128 Bits

↓

8 Groups

↓

Hexadecimal
```

Easy Memory

**IPv4 = Dots**

**IPv6 = Colons**

---

# 🎤 Interview Q&A

### Why was IPv6 introduced?

IPv6 was introduced to solve IPv4 address exhaustion and provide a much larger address space.

---

### What is the size of an IPv6 address?

An IPv6 address is **128 bits** long.

---

### What numbering system does IPv6 use?

IPv6 uses **hexadecimal (0-9 and A-F)**.

---

### What is the purpose of "::" in IPv6?

It compresses consecutive groups of zeros and can be used only once in an address.

---

### Does IPv6 support Broadcast?

No.

IPv6 replaces Broadcast with **Multicast**.

---

### What is the IPv6 Loopback Address?

```text
::1
```

---

### Difference between IPv4 and IPv6?

| IPv4                | IPv6               |
| ------------------- | ------------------ |
| 32-bit              | 128-bit            |
| Decimal             | Hexadecimal        |
| Broadcast Supported | No Broadcast       |
| Limited Addresses   | Huge Address Space |

---

# ⚡ Quick Revision

```text
IPv4

32 Bits

4 Octets

Decimal

127.0.0.1

----------------------

IPv6

128 Bits

8 Groups

Hexadecimal

::1

----------------------

Leading Zeros

Can be Removed

----------------------

Double Colon

::

Used Once

----------------------

Link Local

FE80::

----------------------

Multicast

FF00::
```

---

# 📌 Exam Tips

✅ IPv4 = 32 bits

✅ IPv6 = 128 bits

✅ IPv6 uses hexadecimal numbers

✅ Leading zeros can be omitted

✅ "::" can replace consecutive zero groups only once

✅ IPv6 does not support Broadcast

✅ Loopback Address = ::1

✅ Link-Local addresses begin with FE80::

✅ Multicast addresses begin with FF00::

---

**Related Topics:** IPv4 • IPv6 • Address Compression • Prefix Length • Link-Local • Global Unicast • Multicast
