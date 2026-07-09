# 🌐 15. TCP and UDP

## 📖 Definition

**TCP (Transmission Control Protocol)** and **UDP (User Datagram Protocol)** are transport layer protocols used for communication between devices over a network.

They define how data is transferred between applications.

**Simple:**
TCP focuses on reliability.  
UDP focuses on speed.

---

# 📌 Transport Layer

The transport layer is responsible for:

- End-to-end communication
- Dividing data into segments
- Managing application communication using ports
- Error checking and flow control

Examples:
- Browser connecting to website
- Video streaming
- Online gaming
- File transfers

---

# 🔵 TCP (Transmission Control Protocol)

## Definition

TCP is a connection-oriented protocol that ensures reliable delivery of data.

Before sending data, TCP establishes a connection.

This process is called the **Three-Way Handshake**.

---

## 🤝 TCP Three-Way Handshake

1. SYN
   - Client requests connection

2. SYN-ACK
   - Server accepts request

3. ACK
   - Client confirms connection


Client                Server

SYN ---------------->

<------------- SYN ACK

ACK ---------------->


Connection Established


---

## Features of TCP

✔ Reliable delivery  
✔ Error checking  
✔ Data arrives in order  
✔ Retransmits lost packets  
✔ Slower but accurate  

---

## TCP Examples

- HTTP / HTTPS
- SSH
- FTP
- Email

Used when accuracy matters.

---

# 🟢 UDP (User Datagram Protocol)

## Definition

UDP is a connectionless protocol that sends data without creating a connection first.

It does not guarantee delivery.

---

## Features of UDP

✔ Very fast  
✔ Low delay  
✔ Less overhead  

Limitations:

❌ No retransmission  
❌ No guarantee of delivery  
❌ Packets may arrive out of order  

---

## UDP Examples

- Online gaming
- Video calls
- Live streaming
- DNS queries

Used when speed matters.

---

# ⚔️ TCP vs UDP


| Feature | TCP | UDP |
|-|-|-|
| Connection | Required | Not required |
| Reliability | High | Low |
| Speed | Slower | Faster |
| Ordering | Maintained | Not guaranteed |
| Error Recovery | Yes | No |
| Header Size | Larger | Smaller |


---

# 🚪 Port Numbers

A port identifies which application/service should receive network traffic.

IP Address → Finds device  
Port Number → Finds application


Example:

192.168.1.10:443


IP = Device  
443 = HTTPS Service


---

# 📌 Common Ports

| Port | Protocol | Service |
|-|-|-|
| 20/21 | TCP | FTP |
| 22 | TCP | SSH |
| 25 | TCP | SMTP |
| 53 | TCP/UDP | DNS |
| 67/68 | UDP | DHCP |
| 80 | TCP | HTTP |
| 443 | TCP | HTTPS |
| 3389 | TCP | RDP |

---

# 🛡️ Cybersecurity Importance

Attackers and defenders analyze TCP/UDP traffic.

Used in:

- Port scanning
- Firewall rules
- Packet analysis
- Intrusion detection
- Network monitoring


Examples:

Nmap scan:
nmap -sS target.com

Checks open TCP ports.


UDP scan:
nmap -sU target.com


---

# 🔥 Security Concepts

## SYN Flood Attack

Attack abuses TCP handshake.

Many SYN requests are sent but never completed.

Result:
Server resources become exhausted.


---

## Open Ports

More open ports = larger attack surface.

Security practice:

- Close unused ports
- Restrict access
- Monitor traffic


---

# 🧠 Interview Points

Q: Difference between TCP and UDP?

TCP is reliable and connection-based, while UDP is faster and connectionless.


Q: Why does DNS use UDP?

UDP is faster and DNS queries are small.


Q: Why does HTTPS use TCP?

Because websites require reliable data transfer.

---

# ⭐ Quick Summary

TCP = Reliable + Ordered + Connection  
UDP = Fast + Lightweight + Connectionless  

Ports identify applications.

Understanding TCP/UDP is essential for cybersecurity, cloud security, and network defense.