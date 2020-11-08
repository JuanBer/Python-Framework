class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f"{first}.{last}@company.com"

    def print_info(self):
        print(self.first)
        print(self.last)
        print(self.email)
        print(self.pay)

    def full_name(self):
        return f'{self.first} {self.last}'


emp_1 = Employee('John', 'Doe', 6300)
emp_2 = Employee('Michael', 'Jackson', 10000)

emp_1.print_info()
print("=============================")
emp_2.print_info()
print("=============================")
print(emp_1.full_name())
print(emp_2.full_name())
# Another way to do it
print(Employee.full_name(emp_2))
