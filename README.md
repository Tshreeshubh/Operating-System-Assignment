# Operating Systems and Security (ST5004CEM)
## Individual Coursework Portfolio

**Student Name:** [Shreeshubh Thapa]
**Student ID:** [240213]
**Module Code:** ST5004CEM
**Submission Date:** 22nd January 2026

---

## 📖 Portfolio Overview
This repository contains the practical implementations for the **ST5004CEM** coursework. The work is divided into two main assignments:
1.  **Assignment 1:** Modern Operating Systems and Their Components (OS Services).
2.  **Assignment 2:** Network-Based Inter-Process Communication (IPC).

---

## 📂 Assignment Task 1: Modern OS Components
**Task Overview:** Design and implement small, practical programs that demonstrate the use of key Operating System services.

### Question 1.1: Process Control
> **Requirement:** Demonstrate process control concepts such as creating processes, forking, executing commands, and waiting for termination.

* **Solution File:** `assignment_1/process_control.py`
* **Description:** This script uses the `os` and `subprocess` modules to create child processes. It demonstrates `fork()` (or generic process creation), executes system commands, and uses `wait()` to ensure the parent process pauses until the child completes.

### Question 1.2: File Management
> **Requirement:** Demonstrate file management operations such as creating, reading, writing, and deleting files.

* **Solution File:** `assignment_1/file_management.py`
* **Description:** This script implements a CRUD (Create, Read, Update, Delete) system. It manages file permissions and demonstrates how the OS handles file I/O streams safely.

### Question 1.3: Threading and Synchronization
> **Requirement:** Demonstrate threading concepts and synchronization mechanisms (e.g., locks/mutexes) to manage concurrency.

* **Solution File:** `assignment_1/threading_sync.py`
* **Description:** This script creates multiple threads that access a shared resource. It implements a `Lock` (Mutex) to prevent race conditions, ensuring that only one thread can modify the resource at a time.

### Question 1.4: Memory Management
> **Requirement:** Simulate memory management concepts such as allocation, paging, or fragmentation.

* **Solution File:** `assignment_1/memory_manage.py`
* **Description:** This program simulates a memory block allocator. It visualizes how the OS allocates memory to processes and handles "fragmentation" when memory is freed and re-allocated.

### Question 1.5: Device Access
> **Requirement:** Demonstrate device access, such as listing mounted devices or reading system I/O.

* **Solution File:** `assignment_1/device_access.py`
* **Description:** This script interfaces with the OS to retrieve hardware information. It reads system stats (CPU/Disk) to demonstrate how the OS abstracts hardware devices for user programs.

---

## 🌐 Assignment Task 2: Network-Based IPC
**Task Overview:** Develop a portfolio demonstrating network-based Inter-Process Communication (IPC) techniques.

### Part 1: Theoretical Understanding
> **Requirement:** Define IPC, describe three network-based approaches (TCP, UDP, REST, Message Queues), and compare them.

* **Inter-Process Communication (IPC):** IPC allows separate processes to exchange data and synchronize actions. In distributed systems, this happens over a network rather than shared memory.
* **Comparison of Approaches:**
    1.  **TCP Sockets:** Reliable, connection-oriented. Best for applications needing guaranteed delivery (e.g., File Transfer).
    2.  **UDP Sockets:** Unreliable, connectionless, fast. Best for real-time applications (e.g., Video Streaming).
    3.  **Message Queues (RabbitMQ):** Asynchronous, decoupled. Best for complex microservices where the sender and receiver don't need to be active simultaneously.
    4.  **REST API:** HTTP-based, stateless. Standard for web services.

### Part 2: Practical Implementation
> **Requirement:** Implement two different IPC approaches showing code, comments, and input/output.

#### Implementation A: Reliable Communication (TCP / REST)
* **Selected Approach:** TCP Socket Communication
* **Solution Files:**
    * Server: `assignment_2/tcp_communication/tcp_server.py`
    * Client: `assignment_2/tcp_communication/tcp_client.py`
* **How it works:** The server binds to a port and listens. The client establishes a 3-way handshake connection. Data is transmitted reliably ensuring no packets are lost.

#### Implementation B: Message/Datagram Communication (UDP / Message Queue)
* **Selected Approach:** UDP Datagrams / Message Queue Simulation
* **Solution Files:**
    * Server: `assignment_2/udp_message/udp_server.py`
    * Client: `assignment_2/udp_message/udp_client.py`
* **How it works:** The client sends "datagrams" (messages) without establishing a permanent connection. This demonstrates a faster, "fire-and-forget" communication style often used in messaging or queues.

### Part 3: Reflection and Evaluation
> **Requirement:** Write a reflection comparing the methods implemented.

**Reflection:**
Comparing the TCP and UDP implementations in this portfolio:
1.  **Efficiency:** The UDP implementation was significantly faster to setup and execute because it avoids the overhead of establishing a connection (handshake).
2.  **Reliability:** The TCP implementation provided stability. In tests where I simulated high load, TCP ensured all data arrived correctly, whereas UDP prioritizes speed over completeness.
3.  **Scalability:** For a real-world enterprise system, I would prefer the **Message Queue** (or UDP broadcasting) approach for scalability, as it allows decoupling services, whereas direct TCP connections can become a bottleneck if one service hangs.

---

## 🚀 How to Run the Code

**Prerequisites:** Python 3.x

**1. Running Assignment 1 Tasks:**
Navigate to the root directory and run any specific task:
```bash
python assignment_1/process_control.py
python assignment_1/file_management.py
# etc...