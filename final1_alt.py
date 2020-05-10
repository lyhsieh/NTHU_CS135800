import re
string = input()
for item in re.findall(r'[A-Z]\w+?\b', string):
    print(item)
