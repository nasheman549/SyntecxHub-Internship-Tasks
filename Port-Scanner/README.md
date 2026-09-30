# Syntecxhub_Port_Scanner

A Python based TCP Port Scanner developed as part of **Syntecxhub Cyber Security Internship - Task 1 (Project 1)**.

This scanner can scan a single host or a range of hosts for open ports with fast multithreading.

### Features
- Single Host & IP Range Scanning (e.g., `192.168.1.1-192.168.1.10`)
- TCP Connect Scan using `socket` programming
- Service Name Detection (`socket.getservbyport`)
- Multithreading for faster scanning
- Thread-safe result storage using `threading.Lock()`
- Clean console output (only shows OPEN, TIMEOUT, ERROR)
- Saves all results to `scan_results.txt` with date & time

### Tech Stack
- Python 3
- Libraries: `socket`, `threading`, `datetime`

### ▶️ How to Run
1. Clone this repository:
```bash
git clone https://github.com/nasheman549/Syntecxhub_Port_Scanner.git
cd Syntecxhub_Port_Scanner
