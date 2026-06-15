# 🌐 Network Components, Types, and Connections

---

# 📖 Clients and Servers

## Client

A **client** is a device or software that requests services or resources from another device.

### Examples

* Web Browser
* Mobile App
* Laptop
* Desktop

```
Client ───── Request ─────► Server
```

---

## Server

A **server** is a device or software that provides services, data, or resources to clients.

### Examples

* Web Server
* File Server
* Mail Server
* Database Server

```
             Server
          /     |     \
      Client1 Client2 Client3
```

---

## Client-Server Model

A centralized architecture where multiple clients communicate with a dedicated server.

### Advantages

* Centralized management
* Better security
* Easy backup
* Scalable

### Disadvantages

* Server failure affects all clients
* Higher setup cost

---

# 📡 Peer-to-Peer (P2P)

In a Peer-to-Peer network, every device can act as both a client and a server.

```
PC1 -------- PC2
 |             |
 |             |
PC3 -------- PC4
```

### Advantages

* Easy setup
* Low cost
* No dedicated server

### Disadvantages

* Less secure
* Difficult management
* Not suitable for large networks

---

# 🖥️ Network Components

## End Devices

Devices that send or receive data.

Examples

* Laptop
* Mobile
* Printer
* IP Phone
* Server

---

## Intermediary Devices

Devices that forward and manage network traffic.

Examples

* Router
* Switch
* Firewall
* Wireless Access Point

---

## Network Media

Path used to transfer data.

### Wired

* UTP Cable
* Fiber Optic Cable
* Coaxial Cable

### Wireless

* Wi-Fi
* Bluetooth
* Cellular Network

---

# 🌍 ISP (Internet Service Provider)

An ISP provides Internet connectivity to homes, businesses, and organizations.

Examples

* Airtel
* Jio
* BSNL

---

# 📶 ISP Connectivity Options

## DSL

Uses telephone lines for Internet access.

✔ Affordable

✘ Lower speed

---

## Cable

Uses coaxial cable.

✔ Faster than DSL

✔ Common in residential areas

---

## Fiber

Uses optical fiber.

✔ Very high speed

✔ Low latency

✔ Most reliable

---

## Cellular

Uses mobile networks (4G / 5G).

Examples

* Mobile Hotspot
* SIM Router

---

## Satellite

Uses satellites for Internet connectivity.

Useful in remote locations.

✘ Higher latency

---

# 📊 ISP Comparison

| Type      | Speed     | Cost   | Example        |
| --------- | --------- | ------ | -------------- |
| DSL       | Medium    | Low    | Telephone Line |
| Cable     | High      | Medium | Cable TV       |
| Fiber     | Very High | High   | FTTH           |
| Cellular  | Medium    | Medium | 4G / 5G        |
| Satellite | Medium    | High   | Remote Areas   |

---

# 💡 Real-Life Example

```
          Internet
               │
             ISP
               │
            Router
        ┌──────┼──────┐
        │      │      │
    Laptop   Phone   Smart TV
```

Every home network connects to the Internet through an ISP.

---

# 🧠 Remember This

```
Client

Requests Data

↓

Server

Provides Data

↓

ISP

Provides Internet

↓

Router

Distributes Internet

↓

Devices
```

---

# 🎤 Interview Q&A

### What is a client?

A client is a device or software that requests services from a server.

---

### What is a server?

A server is a computer or software that provides resources or services to clients.

---

### Difference between Client-Server and Peer-to-Peer?

| Client-Server       | Peer-to-Peer           |
| ------------------- | ---------------------- |
| Dedicated server    | No dedicated server    |
| Better security     | Less secure            |
| Centralized         | Decentralized          |
| Used in enterprises | Used in small networks |

---

### What is an ISP?

An Internet Service Provider (ISP) is an organization that provides Internet connectivity to users.

---

### Which ISP connection provides the highest speed?

Fiber Optic Internet provides the highest speed and lowest latency.

---

# ⚡ Quick Revision

```
Client → Requests Service

Server → Provides Service

Router → Connects Networks

Switch → Connects Devices

ISP → Provides Internet

Fiber → Fastest Internet Connection
```

---

# 📌 Exam Tips

✅ Browser = Client

✅ Web Server = Server

✅ Client-Server is the most common architecture on the Internet.

✅ ISP stands for Internet Service Provider.

✅ Fiber is faster than DSL and Cable.

✅ Peer-to-Peer networks are suitable only for small environments.
