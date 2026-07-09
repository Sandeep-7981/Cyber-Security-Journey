# 🌐 The Internet Protocol (IPv4)

---

# 📖 Internet Protocol (IP)

## Definition

**Internet Protocol (IP)** is a set of rules used to identify devices and deliver data across networks.

Every device connected to a network must have a unique IP address.

**Simple:** IP Address = Address of a device on a network.

---

# 🌍 Why Do We Need an IP Address?

An IP address helps to

* Identify a device
* Locate a device
* Send and receive data
* Enable communication between different networks

Without an IP address, devices cannot communicate over the Internet.

---

# 📮 Real-Life Analogy

Just as a house needs a postal address to receive mail,

a computer needs an IP address to receive data.

```text
Person

↓

Home Address

↓

Letter Delivered

------------------------

Computer

↓

IP Address

↓

Data Delivered
```

---

# 📌 IPv4 Address

IPv4 (Internet Protocol Version 4) is the most widely used addressing system.

### Characteristics

* 32-bit address
* Four decimal numbers (octets)
* Range: 0 - 255

Example

```text
192.168.1.10
```

---

# 📦 IPv4 Structure

```text
192 . 168 . 1 . 10
 │      │     │    │
Octet Octet Octet Octet
```

Each octet contains **8 bits**.

```
8 bits × 4 octets = 32 bits
```

---

# 🔢 Binary Representation

Every decimal number is converted into binary.

Example

```text
Decimal

192.168.1.10

↓

Binary

11000000.10101000.00000001.00001010
```

---

# 📍 Network Portion & Host Portion

Every IPv4 address consists of

```text
+----------------+----------------+
| Network Part   | Host Part      |
+----------------+----------------+
```

### Network Part

Identifies the network.

### Host Part

Identifies the device within that network.

---

# 🏠 Private IPv4 Addresses

Used inside homes, schools, and offices.

These addresses are **not routable on the Internet**.

| Range                         | Class |
| ----------------------------- | ----- |
| 10.0.0.0 - 10.255.255.255     | A     |
| 172.16.0.0 - 172.31.255.255   | B     |
| 192.168.0.0 - 192.168.255.255 | C     |

---

# 🌍 Public IPv4 Addresses

Assigned by Internet Service Providers (ISPs).

Used for communication over the Internet.

Example

```text
8.8.8.8
```

(Google Public DNS)

---

# 📋 IPv4 Classes

| Class | Range     | Default Mask  |
| ----- | --------- | ------------- |
| A     | 1 - 126   | 255.0.0.0     |
| B     | 128 - 191 | 255.255.0.0   |
| C     | 192 - 223 | 255.255.255.0 |
| D     | 224 - 239 | Multicast     |
| E     | 240 - 255 | Experimental  |

---

# 🔄 Static vs Dynamic IP

## Static IP

Assigned manually.

Characteristics

* Fixed address
* Doesn't change
* Used for servers

---

## Dynamic IP

Assigned automatically by DHCP.

Characteristics

* Changes periodically
* Easy management
* Used in home networks

---

# 🌍 Loopback Address

Used to test the local network stack.

```text
127.0.0.1
```

Commonly called

**localhost**

---

# 📡 APIPA Address

Automatically assigned when DHCP is unavailable.

Range

```text
169.254.0.0/16
```

If you see this address, the device failed to obtain an IP from the DHCP server.

---

# 💡 Real-Life Example

```text
                Internet
                     │
                  Router
                     │
        -------------------------
        │           │           │
   192.168.1.2 192.168.1.3 192.168.1.4
      Laptop      Phone      Smart TV
```

Every device has a unique IPv4 address.

---

# 🧠 Remember This

```text
IP Address

↓

Network ID

+

Host ID

↓

Unique Device Identification
```

Easy Memory

**IP = Internet Passport**

---

# 🎤 Interview Q&A

### What is an IP address?

An IP address is a logical address used to uniquely identify a device on a network.

---

### Why is an IP address required?

It allows devices to identify each other and exchange data across networks.

---

### What is IPv4?

IPv4 is a 32-bit addressing system consisting of four octets separated by dots.

---

### Difference between Public and Private IP?

| Public IP           | Private IP              |
| ------------------- | ----------------------- |
| Internet Accessible | Local Network Only      |
| Assigned by ISP     | Assigned by Router/DHCP |

---

### What is the Loopback Address?

127.0.0.1, used for testing the local network stack.

---

### What is APIPA?

APIPA (169.254.x.x) is automatically assigned when a device cannot obtain an IP address from DHCP.

---

### Difference between Static and Dynamic IP?

| Static            | Dynamic              |
| ----------------- | -------------------- |
| Manual Assignment | Automatic Assignment |
| Fixed             | Changes              |
| Used for Servers  | Used for Clients     |

---

# ⚡ Quick Revision

```text
IPv4

32 Bits

↓

4 Octets

↓

Example

192.168.1.10

----------------------

Private IP

10.x.x.x

172.16-31.x.x

192.168.x.x

----------------------

Loopback

127.0.0.1

----------------------

APIPA

169.254.x.x

----------------------

Static → Manual

Dynamic → DHCP
```

---

# 📌 Exam Tips

✅ IPv4 = 32 bits

✅ 1 Octet = 8 bits

✅ Maximum value of an octet = 255

✅ Private IPs are not routable on the Internet

✅ Loopback Address = 127.0.0.1

✅ APIPA Range = 169.254.0.0/16

✅ Static IP = Manual

✅ Dynamic IP = DHCP Assigned

✅ Every device on a network must have a unique IP address

---

**Related Topics:** IPv4 • DHCP • DNS • Routing • Private vs Public IP • Network & Host ID
