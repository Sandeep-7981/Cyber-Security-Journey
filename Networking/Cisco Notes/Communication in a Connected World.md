# 🌐 03. Network Components

## 📖 Definition

**Network Components** are the hardware devices and interfaces that work together to enable communication between devices in a network.

**Simple:** They are the building blocks of every computer network.

---

# 📌 Types of Network Components

Network components are mainly divided into:

1. End Devices
2. Intermediary Devices
3. Network Media

```text
                Network
                   │
     ┌─────────────┼─────────────┐
     │             │             │
End Devices   Intermediary   Network Media
```

---

# 💻 1. End Devices

End devices are the source or destination of data.

### Examples

* Desktop
* Laptop
* Mobile Phone
* Printer
* Server
* IP Camera

### Functions

* Send data
* Receive data
* Access network services

```text
Laptop ───── Switch ───── Server
```

---

# 🔀 2. Switch

## Definition

A **Switch** is a Layer 2 networking device that connects multiple devices within a Local Area Network (LAN) and forwards data using **MAC addresses**.

### Key Points

* Operates at OSI Layer 2
* Uses MAC Address Table
* Reduces collisions
* Intelligent forwarding

### Example

```text
          Switch
      ┌────┼────┐
      │    │    │
    PC1   PC2  PC3
```

### Advantages

* Fast communication
* Better performance
* Secure compared to hub

---

# 🌍 3. Router

## Definition

A **Router** connects different networks and forwards packets using **IP addresses**.

### Key Points

* Operates at OSI Layer 3
* Connects LAN to WAN
* Chooses the best path
* Provides Internet access

### Example

```text
Home Network
      │
   Router
      │
  Internet
```

### Real-Life Example

Your home Wi-Fi router connects your devices to the Internet.

---

# 📡 4. Hub

## Definition

A **Hub** is a basic networking device that broadcasts incoming data to every connected device.

### Key Points

* Operates at Physical Layer (Layer 1)
* No intelligence
* Broadcasts data to all ports

### Example

```text
         Hub
     ┌────┼────┐
     │    │    │
   PC1   PC2  PC3

(All devices receive the data)
```

### Disadvantages

* Slow
* More collisions
* Less secure

---

# 🌉 5. Bridge

## Definition

A **Bridge** connects two LAN segments and filters traffic using MAC addresses.

### Uses

* Reduces unnecessary traffic
* Improves network performance

```text
LAN A ─── Bridge ─── LAN B
```

---

# 🚪 6. Gateway

## Definition

A **Gateway** connects networks that use different communication protocols.

### Example

A company network communicating with a cloud service.

### Key Point

Acts as a translator between different networks.

---

# 📞 7. Modem

## Definition

A **Modem (Modulator-Demodulator)** converts digital signals into analog signals and vice versa.

### Functions

* Connects home network to ISP
* Enables Internet access

```text
Computer
     │
 Router
     │
 Modem
     │
 ISP
```

---

# 📶 8. Access Point (AP)

## Definition

An **Access Point** provides wireless connectivity to devices.

### Example

Office Wi-Fi

```text
        Access Point
         /    |    \
   Laptop  Phone  Tablet
```

### Advantages

* Wireless communication
* Easy mobility

---

# 💳 9. Network Interface Card (NIC)

## Definition

A **NIC** is a hardware component that enables a device to connect to a network.

### Types

* Wired NIC
* Wireless NIC

### Example

Ethernet Port in a Desktop Computer

---

# 🔥 10. Firewall

## Definition

A **Firewall** monitors and filters incoming and outgoing network traffic based on security rules.

### Functions

* Blocks unauthorized access
* Protects the network
* Filters malicious traffic

```text
Internet
    │
Firewall
    │
Office Network
```

---

# 📡 11. Server

## Definition

A **Server** is a computer that provides services or resources to other devices (clients).

### Examples

* Web Server
* File Server
* Mail Server
* Database Server

```text
           Server
        /    |    \
     PC1   PC2   PC3
```

---

# 📊 Component Comparison

| Device       | Layer       | Uses                         |
| ------------ | ----------- | ---------------------------- |
| Hub          | Layer 1     | Broadcast data               |
| Switch       | Layer 2     | Connects LAN devices         |
| Router       | Layer 3     | Connects different networks  |
| Bridge       | Layer 2     | Connects LAN segments        |
| Gateway      | Multiple    | Connects different protocols |
| Access Point | Layer 2     | Wireless connectivity        |
| Firewall     | Layer 3/4/7 | Network security             |

---

# 🧠 Memory Trick

```text
Hub       → Repeats Everything

Switch    → Thinks Before Sending

Router    → Finds Best Path

Firewall  → Security Guard

Gateway   → Translator

Access Point → Wi-Fi Provider

NIC        → Network Entry Ticket
```

---

# 🎤 Interview Q&A

### Q1. What is a Switch?

**Answer:**

A switch is a Layer 2 networking device that connects devices within a LAN and forwards data using MAC addresses.

---

### Q2. What is the difference between a Hub and a Switch?

| Hub             | Switch                         |
| --------------- | ------------------------------ |
| Broadcasts data | Sends data only to destination |
| Layer 1         | Layer 2                        |
| Slower          | Faster                         |
| Less secure     | More secure                    |

---

### Q3. What is a Router?

**Answer:**

A router is a Layer 3 device that connects different networks and forwards packets using IP addresses.

---

### Q4. What is a Firewall?

**Answer:**

A firewall is a security device that monitors and filters incoming and outgoing network traffic.

---

### Q5. What is an Access Point?

**Answer:**

An access point provides wireless connectivity to devices using Wi-Fi.

---

### Q6. What is the function of a NIC?

**Answer:**

A NIC enables a computer or device to connect to a network and communicate with other devices.

---

# ⚡ Quick Revision

```text
Hub         → Layer 1 → Broadcast

Switch      → Layer 2 → MAC Address

Router      → Layer 3 → IP Address

Bridge      → Connects LAN Segments

Gateway     → Connects Different Networks

Firewall    → Security

Access Point→ Wi-Fi

NIC         → Network Connection
```

---

# 📌 Exam Tips

✅ Switch uses **MAC Address**.

✅ Router uses **IP Address**.

✅ Hub broadcasts to every device.

✅ Firewall protects the network.

✅ NIC is required for network communication.

✅ Access Point provides wireless connectivity.

