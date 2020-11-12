from developer import Developer
from employee import Employee


class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_empl(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.full_name)


if __name__ == "__main__":
    dev_1 = Developer("John", "Doe", 80000, "Python")
    dev_2 = Developer("Jane", "Doe", 150000, "JavaScript")
    mgr_1 = Manager("Josefine", "Lopez", 200000, [dev_1])
    print(mgr_1.email)
    print("==================")
    mgr_1.add_empl(dev_2)
    mgr_1.print_emps()
    print("==================")
    mgr_1.remove_emp(dev_1)
    mgr_1.print_emps()
    print(isinstance(mgr_1, Employee))
    print(isinstance(dev_1, Employee))
    print(isinstance(mgr_1, Developer))
    print(issubclass(Manager, Employee))
