# 🌐 IPv4 Addressing and Network Segmentation

---

# 📖 IPv4 Communication Types

Devices communicate in different ways depending on how many receivers should receive the data.

---

# 1️⃣ Unicast

## Definition

**Unicast** is **one-to-one communication**, where data is sent from one sender to one receiver.

```text
PC1  ─────────────►  PC2
```

### Examples

* Opening a website
* Sending an email
* SSH connection

### Characteristics

✔ One Sender

✔ One Receiver

✔ Most common communication type

---

# 2️⃣ Broadcast

## Definition

**Broadcast** sends data from one device to **every device** in the same network.

```text
               PC2
                ▲
                │
PC1 ────────────┼──────────► PC3
                │
                ▼
               PC4
```

### Examples

* ARP Request
* DHCP Discover Message

### Characteristics

✔ One Sender

✔ All Devices Receive

✔ Creates more network traffic

---

# 3️⃣ Multicast

## Definition

**Multicast** sends data from one sender to a selected group of receivers.

```text
             PC2
              ▲
              │
PC1 ──────────┼────────► PC3

(PC4 does not receive data)
```

### Examples

* Live Video Streaming
* IPTV
* Online Meetings

### Characteristics

✔ One Sender

✔ Selected Receivers

✔ Efficient bandwidth usage

---

# 📊 Communication Comparison

| Unicast     | Broadcast    | Multicast      |
| ----------- | ------------ | -------------- |
| One → One   | One → All    | One → Many     |
| Email       | ARP          | Live Streaming |
| Low Traffic | High Traffic | Efficient      |

---

# 📖 Types of IPv4 Addresses

---

# Public IP Address

Accessible over the Internet.

Assigned by an ISP.

Example

```text
8.8.8.8
```

---

# Private IP Address

Used inside local networks.

Cannot be accessed directly from the Internet.

### Private Address Ranges

| Class | Range                         |
| ----- | ----------------------------- |
| A     | 10.0.0.0 – 10.255.255.255     |
| B     | 172.16.0.0 – 172.31.255.255   |
| C     | 192.168.0.0 – 192.168.255.255 |

---

# Loopback Address

Used for testing the local device.

```text
127.0.0.1
```

Also called

**localhost**

---

# APIPA Address

Automatically assigned when DHCP is unavailable.

Range

```text
169.254.0.0/16
```

---

# Network Segmentation

## Definition

**Network Segmentation** is the process of dividing a large network into smaller networks (segments).

---

# Why Network Segmentation?

* Improves performance
* Reduces broadcast traffic
* Increases security
* Easier troubleshooting
* Better network management

---

# Example Without Segmentation

```text
                Switch

PC1  PC2  PC3  PC4  PC5  PC6  PC7  PC8

(All devices receive broadcast traffic)
```

---

# Example With Segmentation

```text
            Router

        /               \

Network A          Network B

PC1 PC2 PC3        PC4 PC5 PC6
```

Broadcast traffic stays inside each network.

---

# Network ID & Host ID

Every IPv4 address consists of

```text
+----------------+----------------+
| Network ID     | Host ID        |
+----------------+----------------+
```

### Network ID

Identifies the network.

### Host ID

Identifies a specific device.

---

# Default Gateway

## Definition

A **Default Gateway** is the router that forwards traffic from one network to another.

```text
Laptop

↓

Switch

↓

Router (Default Gateway)

↓

Internet
```

Without a default gateway, a device can communicate only within its own network.

---

# Broadcast Domain

A **Broadcast Domain** is a group of devices that receive the same broadcast message.

More devices

↓

More broadcasts

↓

More congestion

Segmentation reduces broadcast domains.

---

# Real-Life Example

```text
Office Network

                Router
             /            \
       HR Network      IT Network

     PC1  PC2          PC3  PC4
```

A broadcast from HR will not reach the IT network.

---

# 🧠 Remember This

```text
Unicast

One → One

Broadcast

One → Everyone

Multicast

One → Selected Group
```

Easy Formula

**U → B → M**

One → All → Many

---

# 🎤 Interview Q&A

### What is Unicast?

Unicast is one-to-one communication where data is sent from one sender to one receiver.

---

### What is Broadcast?

Broadcast is one-to-all communication where every device in the network receives the data.

---

### What is Multicast?

Multicast sends data to a selected group of devices instead of everyone.

---

### What is a Private IP Address?

A private IP address is used within local networks and is not directly accessible from the Internet.

---

### What is Network Segmentation?

Network segmentation divides a large network into smaller segments to improve performance and security.

---

### What is the purpose of a Default Gateway?

It allows devices to communicate with networks outside their local network.

---

### Why is Network Segmentation important?

It reduces broadcast traffic, improves security, and enhances network performance.

---

# ⚡ Quick Revision

```text
Communication

Unicast   → One → One

Broadcast → One → All

Multicast → One → Many

--------------------------

Private IP

10.x.x.x

172.16-31.x.x

192.168.x.x

--------------------------

Loopback

127.0.0.1

--------------------------

APIPA

169.254.x.x

--------------------------

Segmentation

Large Network

↓

Small Networks

↓

Better Performance
```

---

# 📌 Exam Tips

✅ Unicast = One Sender → One Receiver

✅ Broadcast = One Sender → All Devices

✅ Multicast = One Sender → Selected Devices

✅ Private IPs are not routable on the Internet.

✅ Loopback Address = 127.0.0.1

✅ APIPA Range = 169.254.0.0/16

✅ Default Gateway is usually the router.

✅ Network Segmentation improves security and reduces broadcast traffic.

---

**Related Topics:** IPv4 • Network ID • Host ID • Default Gateway • Broadcast Domains • Routing
