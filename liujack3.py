from collections import Counter

cnt = Counter()

s1 = input()
delimit = input()
s1 = s1.split(delimit)
ans = set()
order = {}

for item in s1:
    cnt[item] += 1
    if order.get(item) == None:
        order[item] = s1.index(item)

L = cnt.most_common()
most_freq = L[0][1]

ans.update(L[0][0])

for item in L:
    if item[1] < most_freq:
        break
    elif item[1] == most_freq:
        ans.update(item[0])

ans = list(ans)
ans.sort(key=lambda x: order[x])
ans = '\n'.join(ans)
print(ans)
