# 🌐 Dynamic Addressing with DHCP

---

# 📖 DHCP (Dynamic Host Configuration Protocol)

## Definition

**DHCP** is a network protocol that automatically assigns IP addresses and other network settings to devices connected to a network.

**Simple:** DHCP acts like an automatic IP address manager.

Without DHCP, every device would need to be configured manually.

---

# 📍 Why DHCP?

Without DHCP

* Manual IP configuration
* More chances of duplicate IP addresses
* Difficult to manage large networks

With DHCP

✔ Automatic IP assignment

✔ Easy network management

✔ Reduces configuration errors

✔ Saves time

---

# 📌 Static Addressing

## Definition

A **Static IP Address** is manually assigned to a device and remains unchanged unless modified.

### Common Uses

* Servers
* Routers
* Printers
* Network Devices

### Advantages

* Permanent address
* Easy remote access
* Reliable for hosting services

### Disadvantages

* Manual configuration
* Difficult to manage in large networks

---

# 📌 Dynamic Addressing

## Definition

A **Dynamic IP Address** is automatically assigned by a DHCP server.

### Common Uses

* Laptops
* Mobile Phones
* Tablets
* Home Networks

### Advantages

* Automatic configuration
* No duplicate IP conflicts
* Easy management

### Disadvantages

* IP address may change
* Not ideal for servers

---

# 📊 Static vs Dynamic IP

| Static IP           | Dynamic IP           |
| ------------------- | -------------------- |
| Manual Assignment   | Automatic Assignment |
| Permanent           | Temporary            |
| Used for Servers    | Used for Clients     |
| More Administration | Easy Management      |

---

# 🖥️ DHCP Server

A **DHCP Server** is responsible for assigning IP addresses to devices.

It also provides

* Subnet Mask
* Default Gateway
* DNS Server Address
* Lease Time

---

# 🔄 DHCP Process (DORA)

The DHCP process consists of four steps.

```text
Client

↓

DHCP Discover

↓

DHCP Offer

↓

DHCP Request

↓

DHCP Acknowledgment (ACK)

↓

IP Address Assigned
```

---

## 1. DHCP Discover

The client broadcasts a request asking,

> "Is there any DHCP server available?"

---

## 2. DHCP Offer

The DHCP server replies with an available IP address.

---

## 3. DHCP Request

The client requests the offered IP address.

---

## 4. DHCP ACK (Acknowledgment)

The DHCP server confirms the assignment.

The client can now communicate on the network.

---

# 📦 DHCP Lease

## Definition

A **Lease** is the amount of time a client can use an assigned IP address.

Example

```
Lease Time

24 Hours

↓

Device renews IP before lease expires.
```

---

# 📋 Information Provided by DHCP

DHCP automatically provides

✔ IP Address

✔ Subnet Mask

✔ Default Gateway

✔ DNS Server

✔ Lease Duration

---

# 🌍 Real-Life Example

```text
                    Internet
                        │
                    Router
                  (DHCP Server)
                        │
        --------------------------------
        │              │              │
    Laptop         Mobile        Smart TV

192.168.1.2    192.168.1.3    192.168.1.4
```

Each device receives an IP address automatically.

---

# 🔍 APIPA (Automatic Private IP Addressing)

If a DHCP server is unavailable,

Windows automatically assigns an address from

```
169.254.0.0/16
```

This allows limited local communication.

---

# 🧠 Remember This

```
DORA

D → Discover

O → Offer

R → Request

A → Acknowledge
```

Easy Memory

**Client asks → Server offers → Client requests → Server confirms**

---

# 🎤 Interview Q&A

### What is DHCP?

DHCP (Dynamic Host Configuration Protocol) automatically assigns IP addresses and network configuration to devices.

---

### What is the purpose of DHCP?

To automate IP address assignment and reduce manual configuration.

---

### Difference between Static and Dynamic IP?

| Static    | Dynamic   |
| --------- | --------- |
| Manual    | Automatic |
| Permanent | Temporary |
| Server    | Client    |

---

### What is the DORA process?

DORA stands for

* Discover
* Offer
* Request
* Acknowledge

It is the process used by DHCP to assign an IP address.

---

### What information does DHCP provide?

* IP Address
* Subnet Mask
* Default Gateway
* DNS Server
* Lease Time

---

### What is a DHCP Lease?

A lease is the duration for which a client can use an assigned IP address.

---

### What happens if DHCP is unavailable?

The client may automatically assign itself an APIPA address (169.254.x.x).

---

# ⚡ Quick Revision

```
DHCP

↓

Automatic IP Assignment

----------------------

Static IP

Manual

Permanent

----------------------

Dynamic IP

Automatic

Temporary

----------------------

DORA

Discover

Offer

Request

Acknowledge

----------------------

APIPA

169.254.x.x
```

---

# 📌 Exam Tips

✅ DHCP = Dynamic Host Configuration Protocol

✅ Static IP = Manual Configuration

✅ Dynamic IP = Automatic Configuration

✅ DHCP Server assigns IP addresses

✅ DORA = Discover → Offer → Request → ACK

✅ DHCP also provides Gateway, DNS, and Subnet Mask

✅ APIPA Range = 169.254.0.0/16

✅ Dynamic IPs are commonly used in home and office networks

---

**Related Topics:** IPv4 • APIPA • DNS • Default Gateway • Static IP • Dynamic IP • DORA Process
