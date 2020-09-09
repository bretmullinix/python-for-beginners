# Working with Python:  Object Oriented Programming (OOP) Part 2

Last updated: 09.08.2020

## Purpose

The purpose of this tutorial is to further your knowledge in Object Oriented Programming (OOP).  You will
be introduced to concepts such as inheritance, polymorphism, encapsulation, and composition.  With knowledge in these
areas of OOP, you will develop a good foundation in OOP. 

## Prerequisites

You have finished the [t3-object-oriented-programming](../t3-object-oriented-programming/readme.md).  
This tutorial provides the necessary foundation you need to perform this tutorial.  If you already have a foundation
in using **OOP**, you may skip this prerequisite.

## Procedures

1. Open up your IntelliJ application. 

    ![tt3-object-oriented-programming](../images/t4-open-intellij.png)

    On the left part of the screen, you should see the **Project** window and the **first_application**
    folder should be visible. If the **first_application** folder is not open, go to the **File** menu,
    click on the **Open..** menu item, and navigate to the **first_application** folder.

1. Highlight the folder **first_application** in the **Project** window.
1. Right click on **first_application**, select the menu item **New** and the sub menu **Python File** to
create a new Python file as is shown below.

    ![t5-create-new-python-file](../images/t5-create-python-file-in-intellij.png)

1. Name the new file **oop-part2.py**.  Your screen should appear like the screenshot below.
   On the left **Project** window, your python file name is highlighted.  On the right window, your python file
   contents appear.  This is where you will enter your code for the tutorial.

    ![t3-a-little-oop-file-created](../images/t5-create-python-file-oop-part2.png)


### Creating the Mammal class
1. Create the class called **Mammal.py** in IntelliJ.
1. Add the following code to the **Mammal.py** class.

    ```python
    class Mammal:
        def __init__(self, number_of_legs_needed_to_walk = 4):
            self.__number_of_legs_needed_to_walk = number_of_legs_needed_to_walk
    
        def get_number_of_legs_needed_to_walk(self):
            return self.__number_of_legs_needed_to_walk
    
        def walk(self):
            class_name = self.__class__.__name__.lower()
            number_of_legs_needed_to_walk = self.get_number_of_legs_needed_to_walk()
            print ('The ' + class_name + ' walks on ' + str(number_of_legs_needed_to_walk) + ' legs.')
   ```

   Let's break down the code:
   
   1. The line `def __init__(self, number_of_legs_needed_to_walk = 4):` is the constructor for the class.  The method
      has the parameter **number_of_legs_needed_to_walk** and sets the default value to 4.  So as long as your mammal
      can walk on 4 legs, you can create an instance of the mammal class without passing in any arguments.
   
   1. The line `self.__number_of_legs_needed_to_walk = number_of_legs_needed_to_walk` assigns the parameter value of
      **number_of_legs_needed_to_walk** to the instance variable **\_\_number_of_legs_needed_to_walk**.  Instance
      variables beginning with **two underscores** are considered private variables.  Users have to explicitly type the
      **two underscores** before a variable name to access these private variables.  This discourages users from changing
      these variables which could impact the **state** of the instance.  A **state** of an instance is the combination of
      all the values of the instance variables.  For instance, if the **state** was modified by changing the
      **__number_of_legs_needed_to_walk** outside the class to 2, and the instance created was a dog, then the **state**
      would be put into an invalid state for a dog.  However, this is much more likely to happen if you have variables
      not prefixed with **two underscores**.  Users will think it is ok to modify the variable.
      
   1. The line ``def get_number_of_legs_needed_to_walk(self):`` is a method used to get the number of legs for a mammal
      instance.  We use the method to return the value of the private instance variable 
      **\_\_number_of_legs_needed_to_walk**.  This provides access to the value of the variable without allowing the
      variable to be modified.  The capability to make instance (object) variables private, not easily accessible
      outside the instance, and not easily modified outside the instance is called **encapsulation**.
    
   1. The line `def walk(self):` creates the object method **walk**.
   
   1. The line `class_name = self.__class__.__name__.lower()` obtains the class name in
      lower case using built in Python metadata on the class.
   
   1. The line `number_of_legs_needed_to_walk = self.get_number_of_legs_needed_to_walk()` assigns the
      result of calling the object method **self.get_number_of_legs_needed_to_walk()**.
      
   1. The line `print ('The ' + class_name + ' walks on ' + str(number_of_legs_needed_to_walk) + ' legs.')` prints
      out the resulting concatenated string "The mammal walks on 4 legs".
      
1. Add the following content to the **oop-part2.py** file and run the Python file.
   
   ```python
    # Create a mammal and call it's walk method
    from mammal import Mammal      
    mammal = Mammal()
    mammal.walk()
   ```

1. You should get the following output

![t5-output-mammal-walk](../images/t5-output-mammal-walk.png)
:construction:
  
Under construction, please continue to follow along as I build this tutorial.


We have finished our second tutorial on OOP.  To continue to learn more about Python, please proceed back to the main instructions.


[**<--Back to main instructions**](../readme.md)
