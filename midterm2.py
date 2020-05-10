personal_data1 = input()
personal_data2 = input()
L1 = personal_data1.split(' ')
L2 = personal_data2.split(' ')
name1 = L1[0]
name2 = L2[0]
birthday1 = L1[1]
birthday2 = L2[1]
older = ''
younger = ''

birthday1_sep = birthday1.split('/')
birthday2_sep = birthday2.split('/')
year1 = int(birthday1_sep[0])
month1 = int(birthday1_sep[1])
day1 = int(birthday1_sep[2])
year2 = int(birthday2_sep[0])
month2 = int(birthday2_sep[1])
day2 = int(birthday2_sep[2])

if year1 > year2:
    older = name1
    younger = name2
elif year1 < year2:
    older = name2
    younger = name1
else:
    if month1 > month2:
        older = name1
        younger = name2
    elif month1 < month2:
        older = name2
        younger = name1
    else:
        if day1 > day2:
            older = name1
            younger = name2
        elif day1 < day2:
            older = name2
            younger = name1
        else:
            older = name1
            younger = name2

print(f'{younger} is older than {older}.')