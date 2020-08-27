# Working with Python

Last updated: 08.27.2020

## Purpose

The purpose of this document is to show how to install and work with python.

## Prerequisites

### Install Python 3 on Windows

1. Download the latest Python Windows Installer [here](https://www.python.org/downloads/release/python-385/).
1. Run the installer and make sure you check box "Add Python 3.8 to PATH"
1.  In the "Type to Search box", enter "cmd".
    This opens up an MSDOS terminal window.
1. Run `python --version` and you should see the version of Python you are running.

### Install Python 3 on Fedora or Centos

1. sudo dnf install python3
1. Run `python --version`
1. Your python version should be at least version 3.

## Procedures

1. Open up a terminal.
1. Create a Python virtual environment by typing the following:

    1. python -m venv my_first_virtual_environment
    
        1. On Windows, run the following:
        
              - Run `cd .\my_first_virtual_environment\Scripts`
              - Run `.\activate.bat`
              - Run `pip list`
              - You should only get a couple of installs, but not the **docker** library.
              - Run `pip install docker`
              - Run pip list
              - You should get **docker** and other new dependencies listed
              - Run `.\deactivate.bat`
              - cd \
              - Run `pip list`
              - You should not have **docker** installed.  The reason the **docker** library isn't installed is
                because when you run **activate.bat** in your virtual environment, the library installs 
                in your virtual_environment, not the system environment.  When you run **deactivate.bat**,
                python installs libraries in your system environment.  By having a virtual environment for different
                purposes, you avoid conflicts.  For example, one application requires one version of a library and
                another application requires another version of the same library in the same environment.
                Only one version of a library can be installed in an environment at once.

        1. On Fedora and Centos, run the following:        
              
              - Run `cd ./my_first_virtual_environment/bin
              - Run `source ./activate`
              - Run `pip list`
              - You should only get a couple of installs, but not the **docker** library.
              - Run `pip install docker`
              - Run pip list
              - You should get **docker** and other new dependencies listed
              - Run `deactivate`
              - cd /
              - Run `pip list`
              - You should not have **docker** installed.  The reason the **docker** library isn't installed is
                because when you run **source ./\[virtual env\]/bin/activate** in your virtual environment, 
                the library installs in your virtual_environment, not the system environment.  When you run **deactivate**,
                python installs libraries in your system environment.  By having a virtual environment for different
                purposes, you avoid the conflicts.  For example, one application requires one version of a library and
                another application requires another version of the same library in the same environment.
                Only one version of a library can be installed in an environment at once.
    
1. Activate your virtual environment as was shown above.
1. Run `python` 
1. Run the following commands to import libraries to display operating system information:

    1. import platform
    1. import os  

1. Run the following commands to display the operating system information.

    1. print(os.name)
    1. print(platform.system())
    1. print(platform.release())  
    1. print(platform.platform())

    The following image represents the Windows output:
    
    ![OS output for Windows](../images/python-adhoc-windows-10.png)
    
    The following image represents the Fedora output:
    
    ![OS output for Fedora](../images/python-adhoc-fedora.png)
 
[**<--Back to main instructions**](../readme.md)