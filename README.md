# 🪵 LogSnap

**LogSnap** is a Unix/Linux command-line tool that parses system log files, highlights warnings and errors with color, and summarizes key insights like log counts, top keywords, and — optionally — a GPT-generated summary using the OpenAI API.

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
- 🤖 Optional GPT summary with `--gpt-summary` (OpenAI)
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

### 🤖 Generate a one-line GPT summary

```bash
export OPENAI_API_KEY=your-key-here
python logsnap.py --file sample.log --gpt-summary
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

🧠 GPT Summary
--------------
System logs indicate frequent failed connections and a high CPU temperature warning.
```

---

## 🧪 Try it out

### ✅ Sample log (small)

```bash
python logsnap.py --file sample.log
```

### ✅ Sample log (large)

Download: [sample_big.log](./sample_big.log)

---

## 🛠 Installation

1. Clone this repo:

```bash
git clone https://github.com/clairefantastic/logsnap.git
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

## 🧠 OpenAI Setup

To use GPT summaries, you need an OpenAI API key:

1. Get your key from: https://platform.openai.com/account/api-keys
2. Set it in your terminal:

```bash
export OPENAI_API_KEY=sk-xxxx
```

3. Then run with:

```bash
python logsnap.py --file sample.log --gpt-summary
```

---

## 📁 Project Structure

```
logsnap/
├── logsnap.py         # Main CLI script
├── parser.py          # Parsing and highlighting logic
├── ai.py              # GPT summary logic
├── sample.log         # Sample test log
├── sample_big.log     # Large generated log for testing
├── requirements.txt
└── README.md
```

---

## 📌 Notes

- Works on Linux, macOS, and WSL.
- You can disable GPT features by omitting `--gpt-summary`.
- Extendable — you can add real-time streaming, `.env` loading, etc.

---

## 🧑‍💻 Author

Made with ☕ and terminal love by Claire Chiou  
[GitHub](https://github.com/clairefantastic) | [LinkedIn](https://linkedin.com/in/yun-ting-chiou)

---

## 📜 License

MIT License
