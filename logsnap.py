import argparse
from collections import defaultdict
from parser import highlight_line, extract_keywords
from ai import generate_summary

def main():
    parser = argparse.ArgumentParser(description="LogSnap: Highlight and summarize Linux logs.")
    parser.add_argument("--file", required=True, help="Path to log file (e.g., /var/log/syslog)")
    parser.add_argument("--only", choices=["info", "warning", "error"], help="Filter by log level")
    parser.add_argument("--gpt-summary", action="store_true", help="Generate AI summary of logs")
    args = parser.parse_args()

    counts = defaultdict(int)
    all_lines = []

    try:
        with open(args.file, "r") as f:
            for line in f:
                stripped = line.strip()
                all_lines.append(stripped)
                colored, level = highlight_line(stripped)
                if args.only is None or args.only == level:
                    print(colored)
                counts[level] += 1
    except FileNotFoundError:
        print(f"❌ File not found: {args.file}")
        return

    print("\n🔍 Log Summary")
    print("--------------")
    for level in ["info", "warning", "error", "other"]:
        print(f"{level.capitalize()}: {counts[level]}")

    print("\n🗂 Top Keywords")
    print("--------------")
    for word, freq in extract_keywords(all_lines):
        print(f"{word}: {freq}")

    if args.gpt_summary:
        print("\n🧠 GPT Summary")
        print("--------------")
        print(generate_summary(all_lines))

if __name__ == "__main__":
    main()
