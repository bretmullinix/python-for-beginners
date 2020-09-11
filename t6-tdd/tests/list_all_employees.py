import unittest

from database import Database


class TestListAllEmployees(unittest.TestCase):

    def test_list_all_employees(self):
        database = Database("postgres")
        employees = database.get_all_employees()
        print("Your list of employees --->")
        for employee in employees:
            print(employee)

if __name__ == '__main__':
    unittest.main()