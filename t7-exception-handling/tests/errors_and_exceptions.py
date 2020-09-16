import unittest
from unittest.mock import patch
import pymongo

from exceptions.mongo_exception import MongoException


class TestErrorsAndExceptions(unittest.TestCase):

    mongo_client = None

    def print_mongodb_databases(self):
        self.assertIsNotNone(self.mongo_client)
        try:
            db_list = self.mongo_client.list_database_names()
            print('Your Mongo databases --->')
            for db in db_list:
                print('\t' + db)
        except Exception as exception:
            class_and_current_method = self.__class__.__name__ + '.' + \
                self.print_mongodb_databases.__name__
            custom_message = class_and_current_method + ':  ' +  \
                             "Couldn't retrieve the list of databases."
            raise MongoException(custom_message, exception)
        finally:
            if self.mongo_client is not None:
                self.mongo_client.close()

    def test_mongodb_connection_error(self):
        self.mongo_client = pymongo.MongoClient("mongodb://localhost:15000/")
        self.assertRaises(MongoException, self.print_mongodb_databases)

    def test_mongodb_connection(self):
        try:
            self.mongo_client = pymongo.MongoClient("mongodb://localhost:27017/")
            self.print_mongodb_databases()
        except Exception as exception:
            print(exception)
            self.fail("You had an error.")

if __name__ == '__main__':
    unittest.main()