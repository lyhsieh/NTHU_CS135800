records = []

def write_record(expense, date = '2020/01/18', description = 'something'):
    records.append((expense, date, description))

def list_records():
    for items in records:
        print(f'${items[0]}, {items[1]}, {items[2]}')

def total_expense():
    total_expense = 0
    for items in records:
        total_expense += items[0]
    return total_expense

for i in range(4):
    calling_write_record = input()
    exec(calling_write_record)
list_records()
print(total_expense())
