# 🌐 The Access Layer

---

# 📖 Access Layer

## Definition

The **Access Layer** is the lowest layer of a network where end devices connect to the network and gain access to communication services.

**Simple:** It is the layer where your laptop, mobile, printer, or PC connects to the network.

---

# 🎯 Functions of the Access Layer

* Connects end devices
* Provides network access
* Uses MAC addresses for communication
* Encapsulates data into Ethernet frames
* Detects transmission errors

---

# 📦 Encapsulation

## Definition

**Encapsulation** is the process of adding protocol information (headers and trailers) to data before transmission.

Every network layer adds its own information.

---

## Encapsulation Process

```text
Application Data
        │
        ▼
Transport Layer
(Segment)
        │
        ▼
Network Layer
(Packet)
        │
        ▼
Access Layer
(Frame)
        │
        ▼
Physical Layer
(Bits)
```

At the destination, the reverse process is called **Decapsulation**.

---

# 📨 Ethernet Frame

## Definition

An **Ethernet Frame** is the data unit used at the Access Layer for communication within a LAN.

It contains addressing information and error-checking fields.

---

# Ethernet Frame Format

```text
+------------------------------------------------------+
| Destination | Source | Type | Data | FCS |
| MAC Address | MAC Address |      |      |     |
+------------------------------------------------------+
```

---

## Frame Fields

### Destination MAC Address

Identifies the receiving device.

Example

```
00:1A:2B:3C:4D:5E
```

---

### Source MAC Address

Identifies the sending device.

Every NIC has a unique MAC address.

---

### Type Field

Specifies which protocol is carried inside the frame.

Examples

* IPv4
* IPv6
* ARP

---

### Data Field

Contains the actual user information.

Examples

* Webpage
* Image
* Email
* Video

---

### Frame Check Sequence (FCS)

Used for error detection.

If errors are detected, the frame is discarded.

---

# 🏷️ MAC Address

## Definition

A **MAC (Media Access Control) Address** is a unique physical address assigned to a network interface card (NIC).

Length

**48 bits (6 Bytes)**

Example

```
3C:52:82:AF:10:7D
```

---

# MAC Address Characteristics

✔ Unique for every device

✔ Assigned by manufacturer

✔ Used inside Local Area Networks

✔ Works at Data Link Layer

---

# 🖥️ Network Interface Card (NIC)

A NIC allows a device to connect to a network.

Functions

* Stores MAC Address
* Sends Frames
* Receives Frames

Examples

* Ethernet Port
* Wireless Adapter

---

# 🔀 Switch and the Access Layer

A switch forwards Ethernet frames using MAC addresses.

```text
          Switch
      ┌────┼────┐
      │    │    │
    PC1   PC2  PC3
```

The switch learns MAC addresses and stores them in a MAC Address Table.

---

# 📋 MAC Address Table

| MAC Address       | Port  |
| ----------------- | ----- |
| 00:AA:11:22:33:44 | Fa0/1 |
| 00:BB:55:66:77:88 | Fa0/2 |

This allows the switch to send frames only to the correct destination.

---

# 🌍 Frame Forwarding

Example

```text
Laptop

↓

Frame Created

↓

Switch

↓

Reads Destination MAC

↓

Forwards to Correct Port

↓

Desktop
```

---

# 📊 Frame vs Packet

| Frame            | Packet                |
| ---------------- | --------------------- |
| Access Layer     | Network Layer         |
| Uses MAC Address | Uses IP Address       |
| Used inside LAN  | Used between Networks |

---

# 💡 Real-Life Example

Sending a file from one laptop to another in the same Wi-Fi network.

```text
Laptop A

↓

Ethernet Frame

↓

Wi-Fi Router / Switch

↓

Laptop B
```

Communication happens using MAC addresses.

---

# 🧠 Remember This

```text
Application

↓

Segment

↓

Packet

↓

Frame

↓

Bits
```

Easy Memory

**Data → Segment → Packet → Frame → Bits**

---

# 🎤 Interview Q&A

### What is the Access Layer?

The Access Layer is the layer where end devices connect to the network and communicate using Ethernet frames and MAC addresses.

---

### What is Encapsulation?

Encapsulation is the process of adding protocol headers and trailers to data before transmission.

---

### What is an Ethernet Frame?

An Ethernet frame is the data unit used at the Access Layer for communication in a Local Area Network.

---

### What is a MAC Address?

A MAC address is a unique 48-bit physical address assigned to a network interface card.

---

### What is the purpose of the Frame Check Sequence (FCS)?

FCS is used for error detection during data transmission.

---

### Difference between Frame and Packet?

| Frame            | Packet          |
| ---------------- | --------------- |
| Uses MAC Address | Uses IP Address |
| Access Layer     | Network Layer   |

---

### What device forwards Ethernet frames?

A **Switch** forwards Ethernet frames based on MAC addresses.

---

# ⚡ Quick Revision

```text
Access Layer

↓

Ethernet Frame

↓

MAC Address

↓

Switch

↓

Destination Device

-------------------------

Encapsulation

Data

↓

Segment

↓

Packet

↓

Frame

↓

Bits
```

---

# 📌 Exam Tips

✅ Access Layer is responsible for LAN communication.

✅ Ethernet uses Frames.

✅ MAC Address = Physical Address.

✅ IP Address = Logical Address.

✅ Switch forwards Frames using MAC addresses.

✅ NIC stores the MAC Address.

✅ FCS detects transmission errors.

✅ Encapsulation adds headers at every layer.

---

**Related Topics:** Ethernet • MAC Address • Switch • Encapsulation • OSI Data Link Layer
