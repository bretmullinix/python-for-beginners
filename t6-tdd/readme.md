# Working with Python:  Test Driven Development (TDD)

Last updated: 09.10.2020

## Purpose

The purpose of this tutorial is to introduce Test Driven Development (TDD).  You will
be shown how to create an example application using TDD.

## Prerequisites

You have finished the [t5-oop-part2](../t5-oop-part2/readme.md).  This tutorial provides the necessary foundation you 
need to perform this tutorial.  If you already have a foundation in using **OOP**, you may skip this prerequisite.

## Procedures

1. Open up your IntelliJ application. 

    ![t6-test driven development](../images/t6-open-intellij.png)

    On the left part of the screen, you should see the **Project** window and the **first_application**
    folder should be visible. If the **first_application** folder is not open, go to the **File** menu,
    click on the **Open..** menu item, and navigate to the **first_application** folder.

1. The requirement for this example is **"List all the employees in our application."**.
   The requirement states we have an application.  In this case, we don't have one,
   but we will create our feature as if we did.

1. Let's setup Python testing

    1. Create the **tests** folder using the context menu as is shown below
    
        ![t6-tdd-new-directory-context-menu](../images/t6-tdd-new-directory-context-menu.png)
    
    1. Under the **tests** folder, let's create a python test file called
       **list_all_employees.py**.  After you create the file, you should
       see the following content.
       
        ![t6-tdd-list-all-employees](../images/t6-tdd-list-all-employees-empty-file.png)       

    1. Add the following code to the **list_all_employees.py** file.
    
        ```python  
        import unittest      
        class TestListAllEmployees(unittest.TestCase):
        
            def test_list_all_employees:
                database = Database("postgres")
                employees = database.get_all_employees()
                print("Your list of employees --->")
                for employee in employees:
                    print(employee)
        
        if __name__ == '__main__':
            unittest.main()
        ```   
     
        Let's explain the code:
        
        1. The line of code `import unittest` imports the **unittest** library.
           This library is used to create the tests and use their
           testing framework.
        

:construction:

The tutorial is currently under construction.  Please follow along as the tutorial
gets built over the next couple of weeks.




We have finished our tutorial on TDD.  To continue to learn more about Python, 
please proceed back to the main instructions.


[**<--Back to main instructions**](../readme.md)
