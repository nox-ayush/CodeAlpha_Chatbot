# 🤖 AlphaBot — Rule-Based Terminal Chatbot

[![Python Version](https://img.shields.io/badge/Python-3.x-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Internship Project](https://img.shields.io/badge/CodeAlpha-Task%202-orange.svg)](https://www.codealpha.tech/)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-Yes-green.svg)](#)

An interactive, terminal-based **Rule-Based Conversational Chatbot** built with pure Python. Developed as **Task 2** for the **CodeAlpha Python Programming Internship**.

---

## 📌 Project Overview
AlphaBot is a lightweight command-line assistant engineered using structured conditional branching, persistent session tracking, and loop architectures. It processes user prompts and returns contextual responses without relying on any external APIs or third-party dependencies.

---

## ✨ Key Features
- 👤 **Session Personalization:** Captures and remembers your name dynamically to address you throughout the conversation.
- ⏰ **Real-Time System Data:** Dynamically retrieves live system time and date on request.
- 🎭 **Interactive Humor & Facts:** Curated library of randomized tech humor and trivia facts.
- 🧭 **In-Console Command Menu:** Type `help` to inspect all supported interaction patterns instantly.
- 🛡️ **Robust Input Handling:**
  - Gracefully handles empty inputs and unrecognized phrases.
  - Supports clean session exits via keywords (`bye`, `exit`, `quit`).
  - Safely traps terminal interruptions (`Ctrl + C`) without traceback crashes.
- 🧩 **Zero External Dependencies:** Built entirely using Python standard library components.

---

## 🛠️ Tech Stack
- **Language:** Python 3
- **Libraries Used:** Standard `datetime`, `random` modules

---

## 🚀 Getting Started

### Prerequisites
Make sure Python 3 is installed on your system:
```bash
python --version