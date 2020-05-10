total = 0
credit_all = 0
cont = 'Y'
while(cont in {'Y', 'y'}):
    grade = input('Grade: ')
    gpa_dict = {'A+': 4.3, 'A': 4.0, 'A-': 3.7, \
            'B+': 3.3, 'B': 3.0, 'B-': 2.7, \
            'C+': 2.3, 'C': 2.0, 'C-': 1.7, 'D': 1.0, 'E': 0.0}
    temp_gpa = gpa_dict.get(grade, 'unknown grade')
    credit = int(input('credit: '))
    cont = input('Continue? ')
    total += temp_gpa * credit
    credit_all += credit
#try:
gpa = total / credit_all
print(f'GPA = {gpa:.2f}')
#except:
    #print('error in input')
