# Quantifiers ({n}, {n,}, {n,m})

import re

text1 = "a ab aab aaab aaaab"
print("Ровно 2 буквы 'a' ({2}):", re.findall(r"a{2}", text1))

text2 = "a ab aab aaab aaaab"
print("2 или более букв 'a' ({2,}):", re.findall(r"a{2,}", text2))

text3 = "a ab aab aaab aaaab"
print("От 2 до 4 букв 'a' ({2,4}):", re.findall(r"a{2,4}", text3))

text_numbers = "Codes: 12, 123, 1234, 12345"
print("От 3 до 4 цифр (\d{3,4}):", re.findall(r"\d{3,4}", text_numbers))