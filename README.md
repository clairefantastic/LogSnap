# 🪵 LogSnap

**LogSnap** is a Unix/Linux command-line tool that parses system log files, highlights warnings and errors with color, and summarizes key insights like log counts and top keywords.

Whether you're debugging a crash or just scanning logs, LogSnap gives you a quick, readable summary right from your terminal.

---

## ✨ Features

- 🔍 Parses any plain-text log file (e.g., `/var/log/syslog`)
- 🎨 Color-coded output:
  - 🔴 Errors
  - 🟡 Warnings
  - 🔵 Info
- 📊 Summary report:
  - Counts by severity
  - Top 5 keywords
- 🎛 Filter by severity with `--only` flag

---

## 🚀 Usage

### ▶️ Basic command

```bash
python logsnap.py --file /var/log/syslog
```

### 🎯 Filter only errors

```bash
python logsnap.py --file sample.log --only error
```

---

## 📂 Example Output

```bash
Apr 17 10:00:02 server kernel: warning: CPU temperature high
Apr 17 10:00:04 server nginx[789]: error: Connection timeout from 10.0.0.5

🔍 Log Summary
--------------
Info: 2
Warnings: 1
Errors: 2

🗂 Top Keywords
--------------
error: 2
connection: 1
timeout: 1
backup: 1
completed: 1
```

---

## 🧪 Try it out

You can test LogSnap with real logs or with our sample file:

### ✅ Sample log (small)

```bash
python logsnap.py --file sample.log
```

### ✅ Sample log (large)

Download the mock 1000-line log for stress testing:
[sample_big.log](./sample_big.log)

---

## 🛠 Installation

1. Clone this repo:

```bash
git clone https://github.com/yourusername/logsnap.git
cd logsnap
```

2. (Optional) Create a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 📁 Project Structure

```
logsnap/
├── logsnap.py         # Main CLI script
├── parser.py          # Parsing and highlighting logic
├── sample.log         # Sample test log
├── sample_big.log     # Large generated log for testing
├── requirements.txt
└── README.md
```

---

## 📌 Notes

- Works on Linux, macOS, and WSL (Windows Subsystem for Linux).
- Designed to be readable and fast. No external logging dependencies.
- Extendable — you can easily add real-time streaming, GPT summarization, etc.

---

## 🧑‍💻 Author

Made with ☕ and terminal love by Claire Chiou  
[GitHub](https://github.com/yourusername) | [LinkedIn](https://linkedin.com/in/yourprofile)

---

## 📜 License

MIT License
