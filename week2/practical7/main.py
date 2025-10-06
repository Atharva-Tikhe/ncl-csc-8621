import unittest

from emp import Employee, SalesAssistant, Supervisor


class my_decorator(object):
    def __init__(self, original_function):
        self.original_function = original_function

    def __call__(self, *args, **kwargs):
        for arg in args:
            if arg == "atharva":
                return self.original_function(*args, **kwargs)
            else:
                return self.original_function(*args, **kwargs)


def decorator(original_function):

    def wrapper_function(*args, **kwargs):
        print(f"within wrapper function {original_function} ")
        return original_function(*args, **kwargs)

    return wrapper_function


class TestEmployeeClass(unittest.TestCase):
    def setUp(self):
        super_name = "Jordan"
        super_id = "12345"
        super_department = "Retail"
        super_title = "Supervisor"
        super_salary = 24000
        super_bonus = 2000

        self.supervisor = Supervisor(
            super_name,
            super_id,
            super_department,
            super_title,
            super_salary,
            super_bonus,
        )

    def test_salary(self):
        self.assertEqual(self.supervisor.salary, 24000)

    def test_object(self):
        self.assertIsInstance(self.supervisor, Supervisor)


def main():
    """
    e1 = Employee(1, "bob", "IT", "engineer")
    e2 = Employee(2, "alice", "R&D", "researcher")
    e3 = Employee(3, "john", "security", "officer")
    print(e1, e2, e3)
    e4 = SalesAssistant(3, "john", "security", "officer", "morning", "12")
    e4.shift_number = 2
    """
    super_name = "Jordan"
    super_id = "12345"
    super_department = "Retail"
    super_title = "Supervisor"
    super_salary = 24000
    super_bonus = 2000

    supervisor = Supervisor(
        super_name, super_id, super_department, super_title, super_salary, super_bonus
    )

    print(f"Supervisor information:")
    print(supervisor.id_number)
    print(supervisor.employee_name)
    print(supervisor.department)
    print(supervisor.salary)
    print(supervisor.title)

    print(supervisor.bonus)


unittest.main()
