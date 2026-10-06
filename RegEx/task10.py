# re.match() - Match at beginning

import re


text = "Hello world from Python"


match_start = re.match(r"Hello", text)
if match_start:
    print("Найдено в начале:", match_start.group())
else:
    print("Не найдено в начале")


match_middle = re.match(r"world", text)
if match_middle:
    print("Найдено в начале:", match_middle.group())
else:
    print("Совпадение не найдено (так как 'world' находится не в самом начале строки)")

date_str = "12-05-2026 - start date"
match_date = re.match(r"(\d{2})-(\d{2})-(\d{4})", date_str)

if match_date:
    print("Полное совпадение даты в начале:", match_date.group(0))
    print("День:", match_date.group(1))
    print("Месяц:", match_date.group(2))
    print("Год:", match_date.group(3))