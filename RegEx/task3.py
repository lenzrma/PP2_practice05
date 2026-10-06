# Special Sequences (\d, \w, \s, \D, \W, \S, \A, \Z)

import re

text = "Hello 123_world!"

print("\d:", re.findall(r"\d", text)) 

print("\w:", re.findall(r"\w", text)) 

text_space = "Hello world!"
print("\s:", re.findall(r"\s", text_space)) 

print("\D:", re.findall(r"\D", "A1")) 

print("\W:", re.findall(r"\W", text)) 

print("\S:", re.findall(r"\S", "Hi!")) 

print("\A (начало):", bool(re.search(r"\AHello", text))) 

print("\Z (конец):", bool(re.search(r"world!\Z", text)))  