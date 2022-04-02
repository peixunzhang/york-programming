import re
from pathlib import Path

text = Path('week2/The_Raven.txt').read_text()

# Find the word ‘shrieked’
findS = re.search('shrieked', text)
if findS:
    print("match")
else:
    print("no match")

# Find the word ‘bleak’
findB = re.search('bleak', text)
if findB:
    print("match")
else:
    print("no match")

#Count the number of words that contain ‘pp’
pp = re.findall('pp', text)
count = len(pp)
print(count)

#Change all the exclamations marks (!) to hash symbols (#)

# def change(str):
#     result = []
#     for c in str:
#         if c == '!':
#             result.append('#')
#         else:
#             result.append(c)
#     return "".join(result)
# changeEx = change(text)
# print(changeEx)

print(text.replace('!', '#'))

#Identify all the words that start with a ‘t” but do not end with an ‘e’, case should be ignored here.
findTNoE = re.findall('\\bt\w*[^\We](?=\\b)', text)
print(findTNoE)
