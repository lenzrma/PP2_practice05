# re.search() - Find first match

import re

text = "The rain in Spain stays mainly in the plain"

match = re.search(r"\bS\w+", text)

if match:
    print("Совпадение найдено!")
    print(f"Найденный фрагмент: {match.group()}") 
    print(f"Начальная позиция: {match.start()}")  
    print(f"Конечная позиция: {match.end()}")     
    print(f"Диапазон (span): {match.span()}")     
else:
    print("Совпадение не найдено")

print("Поиск слова 'Spain' в середине текста:", bool(re.search(r"Spain", text)))  