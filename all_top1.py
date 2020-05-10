input_text = input()
delimiter = input()
input_sep = input_text.split(delimiter)
d = dict()
for ch in input_sep:
    if ch in d:
        d[ch] += 1
    else:
        d[ch] = 1
M = max(d.values())
for ch, times in d.items():
    if times == M:
        print(ch)
