# 🧮 C-Powered Math Evaluator

A high-performance bridge project exploring the "handshake" between **Python** (UI) and **C** (Logic). This project implements the Shunting-Yard algorithm in native C to evaluate math expressions with maximum efficiency.

## 🚀 Quickstart
```bash
# 1. Install Dependencies
pip install -r requirements.txt

# 2. Build the Engine
# Run build.bat and select Option 1 (Release)

# 3. Launch the App
# Run run.bat
```
## 🏗️ The Bridge
This project demonstrates **Foreign Function Interface (FFI)** using `ctypes`:
* **The Brain (C):** Handles raw math logic and sequence validation (preventing syntax errors like `5++3` or `*9` before they process).
* **The Face (Python):** A retro-dark PyQt6 GUI that handles user input and displays real-time results.

## ✨ Features
| Feature | Description |
| :--- | :--- |
| **Performance** | High-speed evaluation using C-based Shunting-Yard logic. |
| **Security** | Dual-layer validation (Python Regex + C State Machine). |
| **UI/UX** | Retro-dark terminal powered by PyQt6. |
| **Inter-Op** | Direct memory-mapped communication via `ctypes`. |

## 📁 Structure
* **`main_connector.py`** — The "Glue" (Entry Point).
* **`src/`** — Modularized GUI and Engine Bridge code.
* **`main.c`** — The core C evaluator engine.
* **`build/`** — Destination for the compiled `.dll`.
* **`requirements.txt`** — Python package list.

## 🛠️ Requirements
* **Python 3.13+**
* **GCC Compiler** (MinGW-w64 or MSYS2 recommended)
* **PyQt6**

---
*Created as a study in cross-language communication and performance optimization.*