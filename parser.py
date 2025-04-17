from colorama import Fore, Style
from collections import Counter
import re

def highlight_line(line):
    lowered = line.lower()
    if "error" in lowered:
        return Fore.RED + line + Style.RESET_ALL, "error"
    elif "warn" in lowered:
        return Fore.YELLOW + line + Style.RESET_ALL, "warning"
    elif "info" in lowered:
        return Fore.CYAN + line + Style.RESET_ALL, "info"
    else:
        return line, "other"

def extract_keywords(lines):
    words = []
    for line in lines:
        words += re.findall(r'\b[a-zA-Z]{4,}\b', line.lower())
    return Counter(words).most_common(5)
