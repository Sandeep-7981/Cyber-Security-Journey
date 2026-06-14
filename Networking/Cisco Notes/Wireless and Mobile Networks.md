# 🌐 04. Data Transmission

## 📖 Definition

**Data Transmission** is the process of transferring data from one device to another through a communication medium (wired or wireless).

**Simple:** It is the movement of data from a sender to a receiver.

---

# 📌 Basic Communication Process

```text
Sender
   │
   ▼
Transmission Medium
   │
   ▼
Receiver
```

Example:

```text
Laptop ───── Wi-Fi Router ───── Internet ───── Server
```

---

# 📌 Components of Data Transmission

### 1. Sender

The device that sends data.

**Examples**

* Laptop
* Mobile
* Server

---

### 2. Receiver

The device that receives data.

**Examples**

* Computer
* Printer
* Mobile

---

### 3. Transmission Medium

The path through which data travels.

Examples

* Ethernet Cable
* Fiber Optic Cable
* Wi-Fi

---

### 4. Message

The actual information being transmitted.

Examples

* Email
* Image
* Video
* File

---

# 📌 Transmission Modes

## 1. Simplex

Communication happens in **only one direction**.

```text
Keyboard  ─────────► Computer
```

### Examples

* Keyboard
* Mouse
* Television Broadcast
* Radio

### Characteristics

✔ One-way communication

✔ No response from receiver

---

## 2. Half Duplex

Communication happens in **both directions but not at the same time**.

```text
Person A ◄────► Person B

(One speaks at a time)
```

### Examples

* Walkie-Talkie
* CB Radio

### Characteristics

✔ Two-way communication

✔ Only one device transmits at a time

---

## 3. Full Duplex

Communication happens in **both directions simultaneously**.

```text
Person A ◄════════► Person B

(Both can speak together)
```

### Examples

* Mobile Calls
* Video Calls
* Telephone

### Characteristics

✔ Fast communication

✔ Simultaneous transmission

✔ Most efficient mode

---

# 📌 Data Delivery Methods

## Unicast

Data is sent from **one sender to one receiver**.

```text
PC1 ─────────► PC2
```

Example:

Sending an email to one person.

---

## Broadcast

Data is sent from **one sender to all devices** in the network.

```text
          PC2
         ▲
         │
PC1 ─────┼────► PC3
         │
         ▼
        PC4
```

Example:

ARP Request

---

## Multicast

Data is sent from **one sender to a selected group of receivers**.

```text
          PC2
         ▲
         │
PC1 ─────┼────► PC3

(PC4 does not receive data)
```

Example:

Online live classes

Video conferencing

Streaming services

---

# 📌 Transmission Media

Transmission media are the paths through which data travels.

They are divided into:

### Guided Media (Wired)

* Twisted Pair Cable
* Coaxial Cable
* Fiber Optic Cable

---

### Unguided Media (Wireless)

* Wi-Fi
* Bluetooth
* Infrared
* Satellite
* Radio Waves

---

# 📌 Wired Media

## Twisted Pair Cable

Most common networking cable.

### Types

* UTP (Unshielded Twisted Pair)
* STP (Shielded Twisted Pair)

### Uses

* LAN
* Ethernet

Advantages

✔ Cheap

✔ Easy installation

Disadvantages

✘ Limited distance

✘ Electromagnetic interference

---

## Coaxial Cable

Contains a central conductor surrounded by insulation.

Uses

* Cable TV
* Broadband Internet

Advantages

✔ Better shielding

✔ Longer distance than UTP

---

## Fiber Optic Cable

Uses light signals instead of electrical signals.

Advantages

✔ Very high speed

✔ Long distance

✔ Immune to electromagnetic interference

Disadvantages

✘ Expensive

✘ Difficult installation

---

# 📌 Wireless Media

## Wi-Fi

Uses radio waves for communication.

Examples

* Home Wi-Fi
* Office Wi-Fi

---

## Bluetooth

Short-range wireless communication.

Examples

* Earbuds
* Smartwatch
* Wireless Keyboard

---

## Infrared

Uses light waves.

Requires line-of-sight communication.

Examples

* TV Remote

---

# 📊 Comparison Table

| Mode        | Direction            | Example       |
| ----------- | -------------------- | ------------- |
| Simplex     | One-way              | Keyboard      |
| Half Duplex | Both (one at a time) | Walkie-Talkie |
| Full Duplex | Both simultaneously  | Phone Call    |

---

# 📊 Transmission Media Comparison

| Media        | Speed     | Distance | Cost   |
| ------------ | --------- | -------- | ------ |
| Twisted Pair | Medium    | Short    | Low    |
| Coaxial      | High      | Medium   | Medium |
| Fiber Optic  | Very High | Long     | High   |

---

# 🧠 Memory Trick

### Transmission Modes

```text
Simplex

Only Send
↓

Half Duplex

Send OR Receive

↓

Full Duplex

Send AND Receive
```

Easy Formula:

**S → H → F**

One Way → One at a Time → Both Together

---

# 🎤 Interview Q&A

### Q1. What is Data Transmission?

**Answer**

Data transmission is the process of transferring data from one device to another through a communication medium.

---

### Q2. Differentiate between Simplex, Half Duplex, and Full Duplex.

| Simplex  | Half Duplex             | Full Duplex            |
| -------- | ----------------------- | ---------------------- |
| One-way  | Two-way (one at a time) | Two-way simultaneously |
| Keyboard | Walkie-Talkie           | Mobile Call            |

---

### Q3. What is Unicast?

**Answer**

Unicast is one-to-one communication where data is sent from one sender to one receiver.

---

### Q4. Difference between Broadcast and Multicast?

| Broadcast           | Multicast              |
| ------------------- | ---------------------- |
| Sent to all devices | Sent to selected group |
| More traffic        | Less traffic           |

---

### Q5. Which transmission medium provides the highest speed?

**Answer**

Fiber Optic Cable provides the highest speed and supports long-distance communication.

---

### Q6. Why is Fiber Optic preferred over Copper Cable?

**Answer**

* Higher speed
* Longer distance
* No electromagnetic interference
* Better reliability

---

# ⚡ Quick Revision

```text
Data Transmission
│
├── Simplex
├── Half Duplex
└── Full Duplex

Communication
│
├── Unicast
├── Broadcast
└── Multicast

Transmission Media
│
├── Wired
│   ├── UTP
│   ├── Coaxial
│   └── Fiber
│
└── Wireless
    ├── Wi-Fi
    ├── Bluetooth
    └── Infrared
```

---

# 📌 Exam Tips

✅ Keyboard → Simplex

✅ Walkie-Talkie → Half Duplex

✅ Mobile Call → Full Duplex

✅ Email → Unicast

✅ ARP Request → Broadcast

✅ Online Live Class → Multicast

✅ Fiber Optic = Fastest + Longest Distance


