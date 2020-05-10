class Person:
    def __init__(self, name, origin_money):
        self._name = name
        self._money = origin_money
    def lend_to(self, person, amount):
        person._money += amount
        self._money -= amount
    def borrow_from(self, person, amount):
        person._money -= amount
        self._money += amount
    @property
    def money(self):
        return self._money



for i in range(3):
    instantiate_statement = input()
    exec(instantiate_statement)

for i in range(3):
    function_call = input()
    exec(function_call)

for i in range(3):
    print_statement = input()
    exec(print_statement)
