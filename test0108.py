s = input()
prohibit = input()
prohibit_list = prohibit.split(',')
for ch in s:
    if ch not in prohibit_list:
        print(ch, end = '')
