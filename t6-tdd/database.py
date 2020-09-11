import time

class Database:
    def __init__(self, p_database_type):
        self.database_type = p_database_type

    def get_all_employees(self):
        # time.sleep( 60 ) # Uncomment this code for the exercise in similating a long database query....
        return ["employee1", "employee2"]