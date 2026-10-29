# SIWES II Industrial Training Portfolio

Welcome to my official repository for the **Students Industrial Work Experience Scheme (SIWES) Phase II**. 

This repository serves as a practical logbook and codebase, demonstrating my transition from theoretical computer science concepts to real-world, production-level software engineering practices. The training focuses on advanced data structures, algorithmic complexity, system architecture, network protocols, and professional version control.

## 🛠️ Tech Stack & Tools
- **Language:** Python
- **Networking:** Python `socket` library, TCP/IP
- **Version Control:** Git & GitHub
- **Environment:** VS Code, Windows Terminal (Split-terminal testing)

## 📂 Training Breakdown

### Week 1: Environment Setup & Fundamentals
- Configured local development environment and IDE.
- Initialized Git version control and established remote repository synchronization.
- Reviewed object-oriented programming (OOP) principles and algorithmic logic.

### Week 2: Advanced Data Structures & Complexity Analysis
- **Binary Search Tree (BST):** Engineered a custom BST with recursive insertion, O(log n) searching, and in-order traversal.
- **Hash Maps:** Built a custom hash map from scratch, implementing a mathematical hash function and resolving memory index collisions via chaining.
- **Linked Lists:** Implemented a singly linked list demonstrating memory pointer manipulation for insertion, traversal, and deletion.
- **Graph Traversal:** Navigated a simulated campus network topology using Breadth-First Search (BFS) and Depth-First Search (DFS) algorithms.
- **Big-O Analysis:** Conducted time and space complexity evaluations (Best, Average, and Worst-case scenarios) for the implemented architectures.
- **System Design:** Proposed a dual-index hybrid architecture utilizing both Hash Maps and BSTs to optimize database retrieval speeds.

### Week 3: Network Architecture & Socket Programming
- **Networking Theory:** Analyzed the OSI Model (specifically Transport and Application layers), compared TCP vs. UDP protocols, and mapped the Client-Server model to real-world applications.
- **TCP Socket Programming:** Developed a TCP client-server architecture using Python sockets, managing IP binding, port listening, and handling network exceptions like `ConnectionRefusedError`.
- **Application-Layer Protocol Design:** Engineered a persistent, multi-message chat server for retail shop operations utilizing a `while True` loop. Enforced strict data validation rules requiring clients to format requests with specific structural syntax (e.g., `FUND:Request`, `TRANSFER:Details`, `CASHOUT:Details`).
- **Network Topology Design:** Architected a Hybrid Extended Star small office network with a static/dynamic Class C IPv4 addressing scheme.

#### Retail Office Network Topology Diagram
```mermaid
graph TD
    ISP((Internet / ISP)) <--> Router[Edge Router <br> 192.168.10.1]
    Router <--> Switch[24-Port Gigabit PoE Switch]
    
    Switch <--> S1[(Server 1: Financial <br> 192.168.10.10)]
    Switch <--> S2[(Server 2: Inventory <br> 192.168.10.11)]
    
    Switch <--> W1[Workstations 1-10 <br> 192.168.10.50 - 99]
    
    Switch <--> AP1((Wireless AP 1))
    Switch <--> AP2((Wireless AP 2))
    
    AP1 -.-> M1(Mobile Clients)
    AP2 -.-> M2(Mobile Clients)

## 🚀 How to Run the Code
To test any of the data structure implementations locally:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/SIWES-II-Training.git
   ```
2. Navigate to the specific week's folder:
   ```bash
   cd siwesII_trainning/week-2-tasks
   ```
3. Execute the Python scripts:
   ```bash
   python binary-tree.py
   python hashmap.py
   ```

---
*Documented and developed by Chinaza during the SIWES II Training Program.*