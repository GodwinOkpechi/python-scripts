#                                 Modules in python
#A module is a file that contains a set of functions or codes that u want to add or include in ur code or 
#project. A module is basically a code or set of codes which are written and saved in a file to aid other 
#programmers by making their work less stressful.

#Note:In python the directory for storing modules in ur editor is the library directory.
#The directory for downloading new modules for python is 'PIP'. It is an online database for python modules.
#U can go there to download modules and upload modules for others to download and use.
 
#To download a module for python
#STEP1--U to the site for 'PIP' where all the modules are stored, www.pip.org, and download the module u want
#STEP2--U can ur command prompt terminal or the terminal in ur text editor(vs code) to type 'PIP install'
#STEP3--in the terminal, it will give ur a search pop-up window, from there u locate the downloaded module and
#       press enter for it to install.
#STEP4--When it is done installing the meter-guage for the downloading would be filled and ur terminal will 
#       display download successful.
#Note:The downloading and installing of the module is online. The downloading of the module is basically 
#     copying the codes or script from the site and pasting in a new file(python file).

#To use a module, we use the 'import' keyword followed by the name of the module. e.g
#  import math         (using dis allow access to all the functions or methods in a function)
#         or
#  from math import *   (using this is when we want to choose a or some specific methods or functions from a
#                        module. Note: wherever u see '*', dis means 'all or everything, so it can be used to
#                        access all the functions.)
#how to use a module in ur code
import humanize
import datetime
# or from humanize import * (to import all the available method in the module)
x=1000000
print(humanize.intcomma(x))
print(humanize.intword(x))

#to humanize current date
date= datetime.datetime.now()
print(date)
print(humanize.naturaldate(date))
print(humanize.naturaltime(date))
#to humanize date and time dat have past
print(humanize.naturalday(date - datetime.timedelta(days=3)))
print(humanize.naturaltime(date - datetime.timedelta(days=3)))

#how to create a module
#a module is a simple python file. it has a normal python extension '.py' like any other python file
#we can create our own modules, all we have to do is to define the codes as functions and save them to a 
#python file, so anytime we want to use them all we need to do is to call on them by their function name.
#Note: u can only call a module if it is present in the same folder as the code file that u want to implement
#the module in.
#first u must define the module like how u define a function
# def TurnToUpper(word):
#     newword=word.upper()
#     return newword

# def calculator(num1,num2):
#     return num1 +  num2

#Then i save my functions in a file named 'mymodule.py' so if i want to use it i can use it. 

import mymodule
x=mymodule.calculator(50,43)
print(x)
y=mymodule.TurnToUpper('potato')
print(y)