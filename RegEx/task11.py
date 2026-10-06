# Flags (re.IGNORECASE, re.MULTILINE, etc.)

import re


text_case = "Python is great and PYTHON is powerful."

matches_case = re.findall(r"python", text_case, re.IGNORECASE)
print("re.IGNORECASE:", matches_case)


multiline_text = "First line\nSecond line\nThird line"

matches_multiline = re.findall(r"^S\w+", multiline_text, re.MULTILINE)
print("re.MULTILINE:", matches_multiline)


text_mixed = "Error: Invalid Code\nerror: failed to load"

matches_combined = re.findall(r"^error", text_mixed, re.IGNORECASE | re.MULTILINE)
print("Комбинированные флаги:", matches_combined)