# 🌐 Gateways to Other Networks

---

# 📖 Network Boundaries

## Definition

A **Network Boundary** is the point where one network ends and another network begins.

Devices inside the same network communicate directly, while communication with another network requires a router (gateway).

---

# 🌍 Same Network Communication

Devices in the same network exchange data directly using MAC addresses.

```text
PC1 (192.168.1.10)
        │
     Switch
        │
PC2 (192.168.1.20)
```

No router is required.

---

# 🌍 Different Network Communication

If devices belong to different networks, data must pass through a router.

```text
Network A                  Network B

PC1
 │
Switch
 │
Router
 │
Switch
 │
PC2
```

The router acts as a gateway between the two networks.

---

# 📌 Default Gateway

## Definition

A **Default Gateway** is the router interface that forwards traffic from the local network to other networks.

Simply,

> "The exit door of a network."

---

## Example

```text
Laptop

IP Address : 192.168.1.10

Gateway : 192.168.1.1

↓

Internet
```

Whenever the destination is outside the local network, the device sends packets to the default gateway.

---

# 📦 Packet Journey

Suppose Laptop A wants to access a website.

```text
Laptop

↓

Switch

↓

Default Gateway (Router)

↓

ISP

↓

Internet

↓

Web Server
```

The reply follows the reverse path.

---

# 🌐 Router

## Definition

A **Router** is a Layer 3 device that connects different networks and forwards packets based on IP addresses.

### Functions

* Connect different networks
* Forward packets
* Choose best path
* Act as default gateway

---

# 📖 Network Address Translation (NAT)

## Definition

**NAT (Network Address Translation)** converts private IP addresses into public IP addresses and vice versa.

It allows multiple devices to share a single public IP address.

---

# Why NAT?

IPv4 addresses are limited.

Instead of assigning a public IP to every device,

one public IP can be shared by many devices.

---

# NAT Example

```text
Private Network

Laptop      192.168.1.10

Phone       192.168.1.20

Smart TV    192.168.1.30

        │

      Router
      (NAT)

        │

Public IP

49.204.xx.xx

        │

Internet
```

To the Internet, every device appears to use the same public IP.

---

# 📌 Advantages of NAT

✔ Conserves IPv4 addresses

✔ Improves security

✔ Allows multiple devices to share one public IP

✔ Hides internal network structure

---

# 📌 Private vs Public IP

| Private IP            | Public IP         |
| --------------------- | ----------------- |
| Used inside LAN       | Used on Internet  |
| Not Internet Routable | Internet Routable |
| Assigned by Router    | Assigned by ISP   |

---

# 🌍 Home Network Example

```text
                 Internet
                      │
              Public IP Address
                      │
                  ISP Router
               (NAT Enabled)
                      │
        -----------------------------
        │             │             │
 Laptop         Mobile        Smart TV

192.168.1.2   192.168.1.3   192.168.1.4
```

---

# 📋 Packet Flow with NAT

```text
Laptop

↓

Private IP

192.168.1.2

↓

Router

↓

NAT Translation

↓

Public IP

↓

Internet

↓

Server

↓

Response

↓

Router

↓

Laptop
```

---

# 🧠 Remember This

```text
Same Network

↓

Switch

----------------

Different Network

↓

Router

----------------

Private IP

↓

NAT

↓

Public IP

↓

Internet
```

Easy Formula

**Switch → Local**

**Router → Global**

---

# 🎤 Interview Q&A

### What is a Default Gateway?

A default gateway is a router that forwards traffic from a local network to other networks.

---

### What is a Router?

A router is a Layer 3 networking device that connects different networks and forwards packets using IP addresses.

---

### What is NAT?

Network Address Translation (NAT) converts private IP addresses into public IP addresses and vice versa.

---

### Why is NAT used?

NAT conserves IPv4 addresses, improves security, and allows multiple devices to share one public IP address.

---

### Difference between Switch and Router?

| Switch                           | Router                      |
| -------------------------------- | --------------------------- |
| Connects devices in same network | Connects different networks |
| Uses MAC Address                 | Uses IP Address             |
| Layer 2                          | Layer 3                     |

---

### When is the Default Gateway used?

Whenever a device wants to communicate with another network or access the Internet.

---

# ⚡ Quick Revision

```text
Network Communication

Same Network

↓

Switch

↓

MAC Address

------------------------

Different Network

↓

Router

↓

IP Address

------------------------

Private IP

↓

NAT

↓

Public IP

↓

Internet

------------------------

Default Gateway

↓

Exit Point of Network
```

---

# 📌 Exam Tips

✅ Devices in the same network communicate through a Switch.

✅ Devices in different networks communicate through a Router.

✅ Default Gateway is usually the router's IP address.

✅ NAT = Network Address Translation.

✅ NAT converts Private IP ↔ Public IP.

✅ NAT helps conserve IPv4 addresses.

✅ Router operates at OSI Layer 3.

✅ Switch uses MAC addresses, Router uses IP addresses.

---

**Related Topics:** Router • NAT • Default Gateway • IPv4 • Private vs Public IP • Network Communication
