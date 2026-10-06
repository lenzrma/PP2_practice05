# Sets and Character Classes

import re

text = "The rain in Spain"
print("Набор [arn]:", re.findall(r"[arn]", text))

print("Диапазон [a-m]:", re.findall(r"[a-m]", text))

print("Отрицание [^arn]:", re.findall(r"[^arn]", text))

text_digits = "Item costs 150 dollars in 2026."
print("Цифры от 2 до 5 [2-5]:", re.findall(r"[2-5]", text_digits))

print("Буквы от a до z или цифры [a-z0-9]:", re.findall(r"[a-z0-9]", text_digits))