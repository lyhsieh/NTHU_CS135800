import re
def dehtml(text):
    return re.split(r'\s+|<.*?>', text)
html_text = input()
print(' '.join(dehtml(html_text)))
