class Employee:

    def __init__(self, first, last, salary):
        self.first = first
        self.last = last
        self.salary = salary
        self.email = first + '.' + last + '@test.com'

    def test(self, name):
        print(name)

emp1 = Employee('Simran', 'Raina', 100000)
emp1.test("Shriti")
emp2 = Employee('Test', 'Last', 200000)

print(emp1.email)
print(emp2.email)
print('{} {}'. format(emp1.first, emp1.last))

class Employee2:
    def __init__(self, first, last, salary):
        self.first = first
        self.last = last
        self.salary = salary
        self.email = first + '.' + last + '@test.com'

    def full_name(self):
        return '{} {}'. format(self.first, self.last)


emp3 = Employee2('Sim', 'Raina', 100000)
emp4 = Employee2('Test', 'Last', 200000)

print(emp4.full_name())
