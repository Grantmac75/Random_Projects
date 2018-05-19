class Employee:

    num_of_emps = 0
    raise_amt = 1.03

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    def get_amount(self):
        return self.amount

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    # Alternative Constructor for String Parsing
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    # Stand Alone Method within Class to check if it's workday
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


class Developer(Employee):
    raise_amt = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
            print('You removed employee: {}'.format(emp.fullname()))

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())
        return

# Prints for Class/Static Methods Tutorial
# emp1 = Employee('Test', 'Employee', 85000)
# print(emp1.email)
# print(emp1.pay)
#
# emp_str_1 = 'John-Doe-72000'
# new_emp_1 = Employee.from_string(emp_str_1)
# print(new_emp_1.email)
# print(new_emp_1.pay)
#
# import datetime
# my_date = datetime.date(2017, 3, 11)
# print(Employee.is_workday(my_date))


# Prints for Class Inheritance Tutorial
# print(help(Developer)) prints method resolution order

dev1 = Developer('Some','Guy', 50000, 'Python')
dev2 = Developer('Another', 'Girl', 55000, 'Java')
# print(dev1.pay)
# dev1.apply_raise()
# print(dev1.pay)
# print(dev1.email)
# print(dev1.prog_lang)
#
mgr_1 = Manager('Sue', 'Smith', 90000, [dev1])
# print(mgr_1.email)
# mgr_1.add_emp(dev2)
# mgr_1.print_emps()
#
# print(mgr_1.email)
# mgr_1.remove_emp(dev1)
# mgr_1.print_emps()

print(isinstance(mgr_1, Manager)) # Prints True
print(issubclass(Manager, Employee)) # Prints True
print(issubclass(Manager, Developer)) # Prints False