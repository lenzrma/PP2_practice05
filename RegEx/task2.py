# RegEx Syntax and Metacharacters (., *, +, ?, ^, $, [], |, (), \)

import re

text1 = "cat, cot, cut"
print(re.findall(r"c.t", text1))  

text2 = "ac, abc, abbc, abbbc"
print(re.findall(r"ab*c", text2))  

text3 = "ac, abc, abbc"
print(re.findall(r"ab+c", text3)) 

text4 = "color, colour"
print(re.findall(r"colou?r", text4))  

text5 = "Hello world"
print(bool(re.search(r"^Hello", text5)))  

text6 = "Hello world"
print(bool(re.search(r"world$", text6))) 

text7 = "The rain in Spain"
print(re.findall(r"[rns]", text7))  

text8 = "The rain in Spain falls mainly"
print(re.findall(r"rain|fall", text8)) 

text9 = "banana, bandanas"
print(re.findall(r"(ban)+", text9))  

text10 = "Price is 20$."
print(re.findall(r"\$", text10))  