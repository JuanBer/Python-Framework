from employee import Employee


class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


if __name__ == "__main__":
    dev = Developer("Juan", "Perez", 2000, "Python")
    dev.apply_raise()
    dev.print_info()
    print(Employee.return_num_of_employees())
