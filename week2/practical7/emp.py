class Employee:
    def __init__(self, id_number, employee_name, department, title):
        self.__id_number = id_number
        self.__employee_name = employee_name
        self.__department = department
        self.__title = title
        print("new object created")

    def __str__(self):
        return f"Employee({self.__id_number}, {self.__employee_name}, {self.__department}, {self.__title})"

    @property
    def id_number(self):
        return self.__id_number

    @id_number.setter
    def id_number(self, id):
        self.__id_number = id

    @property
    def employee_name(self):
        return self.__employee_name

    @employee_name.setter
    def employee_name(self, name):
        self.__employee_name = name

    @property
    def department(self):
        return self.__department

    @department.setter
    def department(self, dept):
        self.__department = dept

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title):
        self.__title = title


class SalesAssistant(Employee):
    def __init__(
        self, id_number, employee_name, department, title, shift_number, pay_rate
    ):
        self.__id_number = id_number
        self.__employee_name = employee_name
        self.__department = department
        self.__title = title
        self._shift_number = shift_number
        self._pay_rate = pay_rate
        Employee.__init__(self, id_number, employee_name, department, title)

    @property
    def shift_number(self):
        return self._shift_number

    @shift_number.setter
    def shift_number(self, shift_no):
        self._shift_number = shift_no

    @property
    def pay_rate(self):
        return self._pay_rate

    @pay_rate.setter
    def pay_rate(self, rate):
        self._pay_rate = rate


class Supervisor(Employee):

    def __init__(self, id_number, employee_name, department, title, salary, bonus):
        self.__id_number = id_number
        self.__employee_name = employee_name
        self.__department = department
        self.__title = title
        self._salary = salary
        self._bonus = bonus
        Employee.__init__(self, id_number, employee_name, department, title)

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, salary):
        self._salary = salary

    @property
    def bonus(self):
        return self._bonus

    @bonus.setter
    def bonus(self, bonus):
        self._bonus = bonus
