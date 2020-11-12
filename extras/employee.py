import datetime


class Employee:

    # class variables
    raise_amount = 1.04
    num_of_emps = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

        Employee.num_of_emps += 1

    def print_info(self):
        print(self.first)
        print(self.last)
        print(self.email)
        print(self.pay)

    @property
    def full_name(self):
        return f'{self.first} {self.last}'

    @full_name.setter
    def full_name(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @full_name.deleter
    def full_name(self):
        print('Delete Name!')
        self.first = None
        self.last = None

    @property
    def email(self):
        return f"{self.first}.{self.last}@company.com"

    def apply_raise(self):
        # class variable can be access as Employee.raise_amount
        # or self.raise_amount
        self.pay = int(self.pay * self.raise_amount)

    # class methods
    @classmethod
    def return_num_of_employees(cls):
        return cls.num_of_emps

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    # alternative constructor
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        # not related to the instance neither the class
        # it doesn't need a cls or self argument
        # if the method don't access the instance or the class
        # that could be an indicator of an instance method
        if day.weekday() in (5, 6):
            return False
        return True

    # dunders methods
    def __repr__(self):
        return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)

    def __str__(self):
        return '{} - {}'.format(self.full_name, self.email)

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.full_name)


if __name__ == "__main__":
    emp_1 = Employee('John', 'Doe', 6300)
    emp_2 = Employee('Michael', 'Jackson', 10000)

    emp_1.print_info()
    print("=============================")
    emp_2.print_info()
    print("=============================")
    print(emp_1.full_name)
    print(emp_2.full_name)
    # class method can be used through instances
    Employee.set_raise_amt(1.05)
    emp_1.apply_raise()
    print(emp_1.pay)
    # namespace of instance emp_1
    # print(emp_1.__dict__)
    # print(Employee.__dict__)
    print(Employee.return_num_of_employees())

    emp_str_3 = 'Jane-Perez-90000'
    emp_3 = Employee.from_string(emp_str_3)
    print("=============================")
    emp_3.print_info()

    my_date = datetime.date(2020, 11, 9)
    print(Employee.is_workday(my_date))

    # if __str__ is not defined it uses __repr__.
    print(emp_3)
    print(repr(emp_3))
    print(str(emp_3))
    print(emp_1 + emp_2)
    print(len(emp_1))
    emp_1.full_name = "John Doe"
    print(emp_1.full_name)
    del emp_1.full_name
