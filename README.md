# 🔍 Directory Integrity Scanner

A Python-based security tool that monitors directory integrity using SHA256 hashing and baseline comparison.

The system detects:

- New files
- Modified files
- Missing files

This project demonstrates the fundamental concepts behind File Integrity Monitoring (FIM) systems used in cybersecurity.

---

## 📌 Features

- SHA256 file hashing
- Directory scanning
- Baseline creation
- Integrity verification
- New file detection
- Modified file detection
- Missing file detection
- JSON-based baseline storage

---

## 🏗️ Project Workflow

```text
Scan Directory
      ↓
Generate SHA256 Hashes
      ↓
Create Baseline
      ↓
Store Baseline (JSON)
      ↓
Rescan Directory
      ↓
Compare Results
      ↓
Detect Changes
