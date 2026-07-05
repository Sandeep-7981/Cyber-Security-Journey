# 🌐 Networking Cheatsheet for Cyber Security

> Quick reference notes for networking concepts, commands, protocols, ports, and security fundamentals.

---

# 1. Networking Basics

## What is a Network?

A network is a group of devices connected together to share data and resources.

Examples:

* Home WiFi network
* College LAN
* Internet

---

# 2. Important Network Devices

## Router

* Connects different networks
* Finds the best path for data
* Works mainly at Layer 3 (Network Layer)

Example:
Home network → Router → Internet

## Switch

* Connects devices inside the same network
* Uses MAC addresses
* Works mainly at Layer 2 (Data Link Layer)

## Firewall

* Monitors and filters network traffic
* Allows or blocks packets based on security rules

## Access Point

* Provides wireless connectivity (WiFi)

---

# 3. OSI Model (Must Know)

| Layer | Name         | Purpose                    | Example       |
| ----- | ------------ | -------------------------- | ------------- |
| 7     | Application  | User services              | HTTP, DNS     |
| 6     | Presentation | Data formatting/encryption | SSL/TLS       |
| 5     | Session      | Connection management      | Sessions      |
| 4     | Transport    | End-to-end communication   | TCP, UDP      |
| 3     | Network      | Routing                    | IP, ICMP      |
| 2     | Data Link    | Local communication        | MAC, Ethernet |
| 1     | Physical     | Hardware signals           | Cables        |

Remember:
**Please Do Not Throw Sausage Pizza Away**

---

# 4. TCP/IP Model

| Layer          | Protocols             |
| -------------- | --------------------- |
| Application    | HTTP, HTTPS, DNS, SSH |
| Transport      | TCP, UDP              |
| Internet       | IP, ICMP              |
| Network Access | Ethernet, WiFi        |

---

# 5. IP Address

IP = Unique address of a device on a network.

Example:

```
192.168.1.10
```

## IPv4 Classes

| Class | Range     |
| ----- | --------- |
| A     | 1-126     |
| B     | 128-191   |
| C     | 192-223   |
| D     | Multicast |
| E     | Research  |

---

# 6. Private IP Ranges

Used inside local networks.

```
10.0.0.0/8

172.16.0.0 - 172.31.255.255

192.168.0.0/16
```

---

# 7. Subnetting Basics

CIDR Examples:

```
/24 = 255.255.255.0
/16 = 255.255.0.0
/8  = 255.0.0.0
```

Example:

192.168.1.0/24

Network:
192.168.1.0

Usable hosts:
192.168.1.1 - 192.168.1.254

Broadcast:
192.168.1.255

---

# 8. MAC Address

* Physical address of network interface
* Layer 2 identifier

Example:

```
00:1A:2B:3C:4D:5E
```

Used by switches.

---

# 9. TCP vs UDP

## TCP

Reliable connection

Features:

* Connection based
* Error checking
* Slower

Examples:

* HTTP
* HTTPS
* SSH

## UDP

Fast communication

Features:

* Connectionless
* Less reliable

Examples:

* DNS
* Streaming
* VoIP

---

# 10. TCP Three Way Handshake

Used to create TCP connection.

```
Client → SYN → Server

Client ← SYN ACK ← Server

Client → ACK → Server
```

---

# 11. Common Ports

| Port  | Service    |
| ----- | ---------- |
| 20/21 | FTP        |
| 22    | SSH        |
| 23    | Telnet     |
| 25    | SMTP       |
| 53    | DNS        |
| 67/68 | DHCP       |
| 80    | HTTP       |
| 110   | POP3       |
| 123   | NTP        |
| 143   | IMAP       |
| 161   | SNMP       |
| 389   | LDAP       |
| 443   | HTTPS      |
| 445   | SMB        |
| 3306  | MySQL      |
| 3389  | RDP        |
| 5432  | PostgreSQL |

---

# 12. DNS (Domain Name System)

Converts:

```
google.com → IP Address
```

Important records:

| Record | Purpose                    |
| ------ | -------------------------- |
| A      | Domain to IPv4             |
| AAAA   | Domain to IPv6             |
| MX     | Mail server                |
| TXT    | Verification/security info |
| CNAME  | Alias                      |
| NS     | Name server                |

---

# 13. DHCP

Automatically provides:

* IP Address
* Gateway
* DNS server

Process:

```
Discover
Offer
Request
Acknowledge
```

(DORA)

---

# 14. NAT (Network Address Translation)

Converts private IP ↔ public IP.

Example:

Private:
192.168.1.5

Public:
49.x.x.x

Allows many devices to share one public IP.

---

# 15. HTTP vs HTTPS

HTTP:

* Port 80
* Plain text

HTTPS:

* Port 443
* Encrypted using TLS

---

# 16. Important Networking Commands

## Windows

Show IP:

```
ipconfig
```

Detailed:

```
ipconfig /all
```

Check connection:

```
ping google.com
```

Trace route:

```
tracert google.com
```

DNS lookup:

```
nslookup google.com
```

Network connections:

```
netstat -ano
```

---

## Linux

Show interfaces:

```
ip addr
```

Routing:

```
ip route
```

Ping:

```
ping google.com
```

DNS lookup:

```
dig google.com
```

Open connections:

```
ss -tulnp
```

Trace route:

```
traceroute google.com
```

---

# 17. Cyber Security Tools

## Nmap

Host discovery:

```
nmap 192.168.1.1
```

Service detection:

```
nmap -sV target.com
```

OS detection:

```
nmap -O target.com
```

Aggressive scan:

```
nmap -A target.com
```

All ports:

```
nmap -p- target.com
```

---

# 18. Network Security Concepts

## CIA Triad

Confidentiality:
Protect data from unauthorized access

Integrity:
Prevent unauthorized modification

Availability:
Keep systems accessible

---

# 19. Common Network Attacks

## Port Scanning

Finding open ports/services.

Tool:
Nmap

---

## Packet Sniffing

Capturing network traffic.

Tools:

* Wireshark
* tcpdump

---

## Man In The Middle (MITM)

Attacker intercepts communication.

Protection:

* HTTPS
* VPN
* Encryption

---

## DNS Spoofing

Fake DNS responses redirect users.

Protection:

* DNSSEC
* Secure DNS

---

## ARP Spoofing

Fake MAC address mapping inside LAN.

Protection:

* Static ARP
* Switch security

---

## DDoS Attack

Overwhelming a server with traffic.

Protection:

* Rate limiting
* Firewalls
* CDN

---

# 20. Wireshark Filters

HTTP traffic:

```
http
```

Specific IP:

```
ip.addr == 192.168.1.5
```

TCP:

```
tcp
```

DNS:

```
dns
```

Port filter:

```
tcp.port == 443
```

---

# 21. Important Security Protocols

| Protocol  | Purpose                 |
| --------- | ----------------------- |
| SSH       | Secure remote login     |
| HTTPS     | Secure web traffic      |
| TLS       | Encryption              |
| IPSec     | Secure IP communication |
| WPA2/WPA3 | WiFi security           |

---

# 22. Cloud Networking Basics

## VPC

Private network inside cloud.

## Subnet

Small section of a network.

## Security Group

Firewall rules for cloud resources.

## Load Balancer

Distributes traffic between servers.

---

# 23. Quick Troubleshooting Flow

1. Check physical connection

2. Check IP

```
ip addr
```

3. Test connectivity

```
ping IP
```

4. Test DNS

```
nslookup domain.com
```

5. Check ports

```
nmap target
```

6. Analyze packets

```
Wireshark
```

---

# Final Notes

Networking is the foundation of:

* Ethical Hacking
* Cloud Security
* Digital Forensics
* SOC Analysis
* Bug Bounty
* Malware Analysis

Strong networking = strong cybersecurity foundation.
