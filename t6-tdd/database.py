class Database:
    def __init__(self, p_database_type):
        self.database_type = p_database_type

    def get_all_employees(self):
        return ["employee1", "employee2"]