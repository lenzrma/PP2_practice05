# re.split() - Split strings

import re


text = "Hello, world! How are you today?"

split_result = re.split(r"[\s,\.!?]+", text)
print("Результат разделения (очищенный от знаков и пробелов):", [item for item in split_result if item])


text_dates = "2026-10-06-12-30"
limited_split = re.split(r"-", text_dates, maxsplit=2)
print("Разделение с maxsplit=2:", limited_split)


text_with_separators = "apple1banana2orange3grape"
split_with_delims = re.split(r"(\d)", text_with_separators)
print("Разделение с сохранением разделителей (цифр):", split_with_delims)