# re.findall() - Find all matches

import re

text = "Свяжитесь с нами по телефонам: +7-701-123-4567 или +7-777-987-6543."

all_numbers = re.findall(r"\d+", text)
print("Все найденные группы цифр:", all_numbers)

text_dates = "Даты встреч: 12.05.2025, 23.08.2026 и 01.01.2027"

parsed_dates = re.findall(r"(\d{2})\.(\d{2})\.(\d{4})", text_dates)
print("Найденные даты (кортежи день, месяц, год):", parsed_dates)


text_emails = "Пишите нам на support@example.com или admin@test.org."
emails = re.findall(r"[\w\.-]+@[\w\.-]+\.\w+", text_emails)
print("Найденные email-адреса:", emails)