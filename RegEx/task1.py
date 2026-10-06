# RegEx Introduction

import re
text = "The rain in Spain stays mainly in the plain"

x = re.search(r"Spain", text)
if x:
    print("Совпадение найдено!")
    print(f"Начальная позиция: {x.start()}")
    print(f"Конечная позиция: {x.end()}")
    print(f"Найденный фрагмент: {x.group()}")
else:
    print("Совпадение не найдено")
all_matches = re.findall(r"ai", text)
print(f"Все найденные совпадения 'ai': {all_matches}")