import os

PROJECT_ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

"""
The above line of code is very common within various Python projects. The definitions.py file itself needs to be in
the root folder of your project.

let's break dow th code piece by piece

PROJECT_ROOT_DIR ->  variable name and can be referred to as a constant due to caps

os.path.dirname() - dirname() is an object that is found in the os.path packages and it will return the directory
name of a file/directory that is given to it. So, it needs and argument of a string location given to it
info here ->   https://docs.python.org/3/library/os.path.html and the info is under dirname

to get the absolute path of our directory we need to give it a particular file name path which is where we use:

os.path.abspath(__file__) - abspath() will return the absolute path of a particular file given to it. Meaning no matter
which environment you're working on it will find the correct working path (Whether windows,linux or mac... it doesn't
matter)

__file__ ->  This is a variable that Python automatically creates for a Python module in the background. It's a variable
that you will be able to use which... very simply... gives you the name of the file.

So, in short, we use the abspath(__file__) to return the absolute path of our definitions file and use the dirname()
to give us our root path directory
"""
