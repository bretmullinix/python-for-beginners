# Working with Python

Last updated: 09.15.2020

## Purpose

The purpose of the repo is to provide simple tutorials 
for programming with **python**.

Python has been around since 1989. The language has evolved into one of the 
most powerful and feature rich languages.  The language is simple to pick up 
and allows people to automate tasks efficiently, eloquently, 
and in little time.

One example of a need for Python is while programming in Ansible.
Ansible is a great language that uses Python under the hoods.  While most tasks 
can be done in Ansible, Ansible sometimes needs new modules or filters for users
to complete their tasks and have maintainable Ansible.

One caveat to using Python is every programming language has
their pluses and minuses.  Python is no exception.  What can be done in Python, 
other languages might have better support, documentation, and other benefits 
that point to using the other languages.  Always evaluate what you need to do, 
create a matrix of plus and minuses of using the languages, and then make a 
well informed decision.  This comes from a developer that uses different languages 
based on evaluation.  No language is the best for everything.

## Prerequisites

Windows, Fedora, or Centos operating systems.

## Tutorials

The tutorials in this repo are as follows:

1. **Getting Started**

    Shows the user how to set up their environment
    and run adhoc **python** commands.  The tutorial is in the
    [**t1-getting-started**](./t1-getting-started) folder.

1. **Working with variables and data types**

    Shows the user how to work with different variables and data types.
    The tutorial is in the [**t2-variables-and-data-types**](./t2-variables-and-data-types) folder.

1. **Getting Started with Object Oriented Programming (OOP)**

   Shows the user how to work with Object Oriented Programming (OOP).  Object oriented programming uses
   real world objects (such as people, places, or things) to model your application(s).  The tutorial
   is in the [**t3-object-oriented-programming**](./t3-object-oriented-programming) folder.

1. **Working with collections**

   Shows the user how to work with collections.  A collection is used to hold a group of data types (like
   **string**, **int**, **long**, or **objects in a class** to name a few) so developers can perform
   actions using the collection.  For certain scenarios, working with collections gives developers
   several advantages compared to working with the individual data types.
   The tutorial is in the [**t4-working-with-collections**](./t4-working-with-collections) folder.

1. **Continue to work with Object Oriented Programming (OOP)**

   Builds on the first OOP tutorial.  Provides critical foundational skills in OOP.  You will learn
   about inheritance, polymorphism, encapsulation, and composition.  The examples used in the tutorial
   will focus on working with the real world **mammal** and **car** objects to explain the OOP concepts.
   The tutorial is in the [**t5-oop-part2**](./t5-oop-part2) folder.

1. **Working with Test Driven Design (TDD)**

   Test Driven Design (TDD) is a great practice that can take you from a beginner in
   software development to an experienced or even advanced software developer in
   a very short period.  TDD is based on the idea where you create your application
   or feature using pseudo code in a test, have the test fail, make changes to quickly
   get your application test to work, and then change your code to make your code
   maintainable and extensible.  The tutorial is in the [**t6-tdd**](./t6-tdd) folder.

1. **Incorporating Error/Exception Handling in your Code**

   Certain resources stay in memory longer than needed if they are not closed or disposed after they are used.
   If the resources stay around in memory and are not being used, your application can crawl to a halt or in
   some cases crash the computer.  An example we will use in this tutorial is working with **MongoDB**, a NoSQL
   Document database, hosted in a **Docker** container.  We will use exception handling to ensure no errors
   occur when connecting to the database, and we will show how to close your database connection to prevent
   memory leaks.
   The tutorial is in the [**t7-exception-handling**](./t7-exception-handling) folder.

:construction:
