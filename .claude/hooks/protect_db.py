import json
import sys
import re

data = json.load(sys.stdin)
command = data.get("tool_input", {}).get("command", "")

dangerous_patterns = [
    r"\brm\b.*(walmart\.db|\.db\b)",
    r"\bdel\b.*(walmart\.db|\.db\b)",
    r"Remove-Item.*(walmart\.db|\.db)",
    r"DROP\s+(TABLE|DATABASE)",
]

for pattern in dangerous_patterns:
    if re.search(pattern, command, re.IGNORECASE):
        print("BLOCKED: Attempted to delete a protected database file.")
        print("'data/walmart.db' is protected. Run setup.py to recreate it from the CSV.")
        sys.exit(2)

sys.exit(0)
