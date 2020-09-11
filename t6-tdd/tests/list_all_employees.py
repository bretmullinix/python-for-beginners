import unittest
from unittest.mock import patch

from database import Database


class TestListAllEmployees(unittest.TestCase):

    def test_list_all_employees(self):
        database = Database("postgres")
        employees = database.get_all_employees()
        print("Your list of employees --->")
        for employee in employees:
            print(employee)

    @patch('database.Database.get_all_employees')
    def test_list_all_employees_fast(self, mock_method_get_all_employees ):
        mock_method_get_all_employees.return_value =  ['employee4', 'employee5']
        database = Database("postgres")
        employees = database.get_all_employees()
        print("Your list of employees --->")
        for employee in employees:
            print(employee)

if __name__ == '__main__':
    unittest.main()