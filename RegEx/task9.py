# re.sub() - Replace patterns

import re

text = "Телефон: 8-701-123-4567, факс: 8-777-987-6543"

masked_text = re.sub(r"\d", "#", text)
print("Замаскированный текст:", masked_text)


text_spaces = "один два три четыре пять"

limited_sub = re.sub(r"\s", "_", text_spaces, count=2)
print("Замена с count=2:", limited_sub)


date_str = "Сегодняшняя дата: 06.10.2026"
new_date_format = re.sub(r"(\d{2})\.(\d{2})\.(\d{4})", r"\3-\2-\1", date_str)
print("Дата в новом формате:", new_date_format)


bad_words = "Этот продукт полный блин ужас и кошмар!"
clean_text = re.sub(r"блин|ужас", "[ЦЕНЗУРА]", bad_words)
print("Очищенный текст:", clean_text)