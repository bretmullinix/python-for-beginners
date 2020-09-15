# Working with Python:  Exception Handling

Last updated: 09.15.2020

## Purpose

The purpose of this tutorial is to work with exception handling.  With exception handling,
you will be able to catch errors and exceptions that occur and gracefully recover from them.
Also, with the exception handling, you will see how to clean up resources to prevent
memory leaks, even if a failure occurs.

## Prerequisites

You have finished the [t6-tdd](../t6-tdd/readme.md).  This tutorial provides the necessary foundation
you need to perform this tutorial.  If you already have a foundation
in using **TDD**, you may skip this prerequisite.


## Procedures

1. Open up your IntelliJ application. 

    ![t3-object-oriented-programming](../images/t7-open-intellij.png)

    On the left part of the screen, you should see the **Project** window and the **first_application**
    folder should be visible. If the **first_application** folder is not open, go to the **File** menu,
    click on the **Open..** menu item, and navigate to the **first_application** folder.

1. Highlight the folder **first_application** in the **Project** window.

### Catching your First Error

1. Under the **tests** folder, create the class called **errors_and_exceptions.py** in IntelliJ.
1. Open up a terminal as is shown below.

    ![p7-open-terminal-window](../images/p7-open-terminal-window.png)
    
1. At the terminal, install the Python MongoDB library using the following command `pip install pymongo`

    ![p7-install-pymongo-terminal](../images/p7-install-pymongo-terminal.png)

1. Add the following code to the **errors_and_exceptions.py** class.

    ```python
    import unittest
    from unittest.mock import patch
    import pymongo
    
    
    
    class TestErrorsAndExceptions(unittest.TestCase):
    
        def test_mongodb_connection(self):  
            mongo_client = pymongo.MongoClient("mongodb://localhost:27017/")
            db_list = mongo_client.list_database_names()
            print('Your Mongo databases --->')
            for db in db_list:
               print('\t' + db)
            mongo_client.close()
    
    
    
    if __name__ == '__main__':
        unittest.main()
   ```

   Let's break down the code:
   
   1. The line `import pymongo` imports the Mongo library needed to interact with a Mongo database server
      in Python.
   
   1. The line `mongo_client = pymongo.MongoClient("mongodb://localhost:27017/")` creates a MongoDB
      client for the Mongo database server located on **localhost** and listening on port **27017**.
      The word **localhost** is always a reference to your computer.
      
   1. The line `db_list = mongo_client.list_database_names()` retrieves a list of databases from
      the **MongoDB** server.
      
   1. The rest of the code just prints out the Mongo database names.

1. Run the test.  You should get a failure similar to the output below.  The test fails because we don't
   have a MongoDB server running on our machine at port 27017 (or if you do, stop MongoDB and re-run the test).

    ![p7-mongodb-no-exception-handling](../images/p7-mongodb-no-exception-handling.png)
    

### Install the MongoDB Server

1. Install **Docker** by following the installation instructions for your operating system
   [here](https://docs.docker.com/get-docker/).  Please read the instructions on **Getting Started**.
   Otherwise, you might have trouble running the **MongoDB** server container below.
   
1. Open up a terminal

1. Run the **MongoDB** docker container by running the following command:

    `docker run -d -p 27017-27019:27017-27019 --name mongodb mongo:4.0.4`
      
      The command says to run the Docker image called **mongo** with the image version of
      **4.0.4**.  The **-d** option says to run the container in the background so 
      you can still use your terminal.  The **-p** option maps your host ports
      **27017-27019** to the container ports **27017-27019**.  The **-name** option
      gives the container the name **mongodb**.
      
1. Open up the **errors_and_exceptions.py** and re-run the test.  The test should be successful and
   you should see results similar to the image below.
   
    ![p7-mongodb-no-exception-handling-success](../images/p7-mongodb-no-exception-handling-success.png)
    
    As you can see, you have some pre-configured databases listed when you install the MongoDB server.  The
    code is not quality code.  You have no exception handling if something goes wrong, and if something does
    go wrong, you are not cleaning up your MongoDB connection.
    
###  Add Exception Handling and Clean up the MongoDB Connection

Let's add some exception handling, and if an exception does occur, let's clean up the MongoDB connection.

     
:construction:

Currently, this tutorial is under construction.  The tutorial should be finished by the end of the week.


We have finished our second tutorial on OOP.  To continue to learn more about Python, 
please proceed back to the main instructions.


[**<--Back to main instructions**](../readme.md)
