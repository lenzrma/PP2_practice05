import re

# 1. Write a Python program that matches a string that has an 'a' followed by zero or more 'b''s.
def task_1(text):
    pattern = r"ab*"
    return re.findall(pattern, text)

# 2. Write a Python program that matches a string that has an 'a' followed by two to three 'b'.
def task_2(text):
    pattern = r"ab{2,3}"
    return re.findall(pattern, text)

# 3. Write a Python program to find sequences of lowercase letters joined with a underscore.
def task_3(text):
    pattern = r"[a-z]+_[a-z]+"
    return re.findall(pattern, text)

# 4. Write a Python program to find the sequences of one upper case letter followed by lower case letters.
def task_4(text):
    pattern = r"[A-Z][a-z]+"
    return re.findall(pattern, text)

# 5. Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.
def task_5(text):
    pattern = r"a.*b"
    return re.findall(pattern, text)

# 6. Write a Python program to replace all occurrences of space, comma, or dot with a colon.
def task_6(text):
    return re.sub(r"[,\.\s]", ":", text)

# 7. Write a python program to convert snake case string to camel case string.
def task_7(text):
    parts = text.split('_')
    return parts[0] + ''.join(word.capitalize() for word in parts[1:])

# 8. Write a Python program to split a string at uppercase letters.
def task_8(text):
    return re.split(r"(?=[A-Z])", text)

# 9. Write a Python program to insert spaces between words starting with capital letters.
def task_9(text):
    return re.sub(r"(?<!^)(?=[A-Z])", " ", text)

# 10. Write a Python program to convert a given camel case string to snake case.
def task_10(text):
    s1 = re.sub(r"(.)([A-Z][a-z]+)", r"\1_\2", text)
    return re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", s1).lower()