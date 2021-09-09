
'''
 the rat is very fast but i don't know why i am saying this, i just feel like saying it to test whether this stuff will work
'''
x,y,z= 'boy','girl','rat'
print(x)
print(y)
print(z)
                        #numbers in python
#to raise to power a number
x=5**2
y=pow(5,2)
print(x)
print(y)

#to get maximum of a set of numbers
x=(2,3,4,6,8,12,45,56)
y=(12,27,145,2,31)
print(max(x))
print(max(y))

#to get minimum value of a set of numbers
x=(2,3,4,6,8,12,45,56)
y=(12,27,145,2,31)
print(min(x))
print(min(y))

#to get the positive value of a negative number
x=-23
y=-1.234
print(abs(x))
print(abs(y))

#to approximate the value of float to an integer 
x=50.45342
print(round(x))

#to perform the following functions u must add this to the top of ur code editor
from math import *
#to approximate a float to the highest integer value
x=3.6
y=3.2
print(ceil(x))
print(ceil(y))

#to approximate a float to the lowest integer value
x=3.6
y=3.2
print(floor(x))
print(floor(y))

#to find the square root of a number
x=40
y=785
print(sqrt(x))
print(sqrt(y))

                        #strings in python
#to turn a string to uppercase
x='sarah'
print(x.upper())

#to turn a string to lowercase
x='SARAH'
print(x.lower())

#to turn the first letter of a string to a uppercase(capital letter)
x='sarah'
print(x.capitalize())

#to confirm if a string is in uppercase 
x='sarah'
y='SARAH'
print(x.isupper())
print(y.isupper())

#to confirm if a string is in lowercase
x='sarah'
y='SARAH'
print(x.islower())
print(y.islower())

#to replace a word or phrase in a string
x='my name is godwin'
print(x.replace('godwin','bolu'))
print(x.replace('my','his'))

#to get the length of a string
x='my name is godwin'
print(len(x))

#to get the index of a string  (make sure u ask him about this cause it was giving error when it was run)
x='my name is godwin'

from math import *
#to get the position of a character in a string   (also this one to)
x='my name is godwin'
print(x.index('g'))


                                #Operators
#operators are used to perform operations on variables and values 
#                     types of operators
# -arithmetic operators               -assignment operators
# -comparison operators               -logical operators
# -identity operators                 -membership operators
# -bitwise operators    

# arithmetic operators 
# i) addition(+)
x= 3 
y= 5 
print(x+y)
# ii)subtraction(-)
x=3
y=5
print(x-y)
# iii)multiplication(*)
x=3
y=5
print(x*y)
# iv)division(/)
x=12
y=4
print(x/y)
# v)modulus(%)
x=5
y=3
print(x%y)
# vi)exponentiation(**)
x=5
y=3
print(x**y)
# vii)floordivision(//)
x=22
y=4
print(x//y)
x=19
y=4
print(x//y)

# assignment operators
#i)=
x=5
print(x)
#ii)+=
x=5
x+=3
print(x)
#iii)-=
x=5
x-=3
print(x)
#iv)*=
x=5
x*=3
print(x)
#v)/=
x=5
x/=3
print(x)
#vi)%=
x=5
x%=3
print(x)
#vii)//=
x=5
x//=3
print(x)
#viii)**=
x=5
x**=3
print(x)
#ix)&= 
#x)!=
#xi)^= 
#xii)>>= 
#xiii)<<= 

# comparism operators
#i)equal to(==) 
x= 40==15   
print(x)
#ii)not-equal to(!=)
x= 40!=15   
print(x)
#iii)greather than(>)
x= 40>15   
print(x)
#iv)less than(<) 
x= 40<15   
print(x)
#v)greather than or equal to(>=)  
x=40>=15
print(x)
#vi)less than  or equal to(<=)
x=40<=15
print(x)

# logical operators
#i)AND(and): returns True only if both statements are true
x=3
print(x<5 and x<10)
print(x>5 and x<10)
print(x<5 and x>10)
print(x>5 and x>10)
#ii)OR(or): returns True if one of the statements is true
x=3
print(x<5 or x<10)
print(x>5 or x<10)
print(x<5 or x>10)
print(x>5 or x>10)
#iii)NOT(not): returns the reversal of the result, i.e returns False if the result is True
x=3
print(not(x<5 and x<10))
print(not(x>5 and x<10))
print(not(x<5 and x>10))
print(not(x>5 and x>10))

#                                     Type casting
# Type casting refers to the act of changing an element from one data type to another data type.                                
# types of Type casting
#i) Number(integer or float) to string
num=45    
num=str(45)
print(type(num))
#ii) String to number(integer and float): you cannot convert a string with letters to to number,e.g 'john';
# to convert these will not work so you can only convert from string with numbers to numbers(integer or float)
num='45'
num=int('45')       
print(type(num))

num='45'
num=float('45')
print(type(num))


#                                        Inputs
# input is used to collect and display information from a user's point of view(which is the terminal).
# the symbol is  input()
# Note: 
name=input('enter ur name: ')
print('ur name is',name)

# a program to display first name, last name and age with the use of inputs
first_name= input('enter ur first name: ')
last_name= input('enter ur last name: ')
age= input('how old are you: ')
print('------------------------------------------------------------------')
print('ur first name is ',first_name)
print('ur last name is ',last_name)
print('u are ',age,'yrs old')

# a program to calculate 2 numbers using inputs
num1= input('enter ur first number: ')
num2= input('enter ur second number: ')
sum= int(num1) + int(num2)
print('ur result is ',sum)

#a python program to collect a users details as required using inputs
full_name= input('write ur full name: ')
age= input('how old are u: ')
gender= input('what is ur gender: ')
marital_status= input('what is ur marital status: ')
state_of_origin= input('what is ur state of origin: ')
city= input('what is ur city of residence: ')
address= input('write ur address: ')
phone_number= input('what is ur phone number: ')
email= input('what is ur email address: ')
school= input('what was the name of ur secondary school: ')
comment= 'This was a nice experience and just had to add this to flex a little with the code.'
print('---------------------------------------------------------------------------------------')
print('Ur full name is ',full_name)
print('U are ',age,'yrs old')
print('Ur gender is ',gender)
print('Ur marital status is ',marital_status)
print('U are from ',state_of_origin,'state')
print('Ur city of residence is ',city)
print('U live at ',address)
print('Ur phone number is ',phone_number)
print('Ur email address is ',email)
print('The name of ur secondary school is ',school)
print('Thanks for using this.')
print(comment)


#                              Functions
# a function is a block of code that u can run  multiple times to perform a specific task. To use a function
# we must use:  def name of function():
#                   print('what u need to say')
#invoke the function by using:
#                name of function()

def greet():
    print('holla')
    print('hello, how are u ')
greet()

# to allow ur user send in input
def greeting():
    name=input('ur name: ')
    age=input('how old are u: ')
    print(name)
    print('hello, how are u ')
    print('u are', age,'yrs old')
greeting()

#to use functions to respond to inputted data
def greet2(name):
    print('hello' ,name, 'how are u ')
greet2('sarah')

# to add other parameters
def greet3(name, age):
    print('hello' ,name, 'how are u ')
    print('u are', age,'yrs old')
greet3('sarah', 26)

# Note:if u want use a function u must first declare it then use before going into a different function.

# to return data from a code for usage purpose
# Note: the return keyword must be the last thing used in ur code cause it serves as a end comment or limit for ur code.
def add_nums(num1,num2):
    sum= num1 + num2
    return sum 
def multiply_nums(num1,num2):
    multi= num1 * num2
    return multi
print(add_nums(20,5))
print(multiply_nums(20,5))
result= add_nums(30,21) + multiply_nums(3,4)
Result= add_nums(30,21) + add_nums(5,6)
result_2= add_nums(24,13)
print(result)
print(Result)
print(result_2)

#                          Python collections
# we have 4 types of python collections; they are 
# *List
# *Tuple
# *Set
# *Dictionary

#                             Lists
#list is a collection of data types which are ordered and changeable.They allow update by a programmer or coder 
#They are denoted by square brackets [] 
fruits=['apple', 'banana', 'pear', 'grape']
print(fruits)

#to access specific items or data from a list we make use of index value(we use our knowledge on index). e.g
fruits=['apple', 'banana', 'pear', 'grape']
print(fruits[0])
print(fruits[3])
# to access a list from the back we use negative index values. e.g
print(fruits[-1])
print(fruits[-3])
# we can also specify a range of items or data we want to display. to do so we use index values and ':' sign.e.g
fruits=['apple', 'banana', 'pear', 'grape']
print(fruits[0:])
print(fruits[1:])
# these will give u from the 0 index value to the end 
fruits=['apple', 'banana', 'pear', 'grape']
print(fruits[:1])
print(fruits[:3])
# these will give u the data up to the 1 index value(this serves as a end range value)

# so to use a complete range would be something like this
fruits=['apple', 'banana', 'pear', 'grape']
print(fruits[0:3])
print(fruits[1:3])

# to change items in a list we use the index number to assign the new item we want to assign.
# e.g i want to change some items in my fruits list 
fruits=['apple', 'banana', 'pear', 'grape']
fruits[1]= 'guava'
fruits[-1]= 'black currant'
print(fruits)

# to add an item to a list we use ".append()" function to execute that. e.g
fruits=['apple', 'banana', 'pear', 'grape']
fruits.append('tomato')
fruits.append('guava')
print(fruits)

# to add at a specific position we use index placing with the ".insert()" function to do that. e.g
fruits=['apple', 'banana', 'pear', 'grape']
fruits.insert(2,'tomato')
fruits.insert(4,'banana')
print(fruits)

# to remove an item from a list we use ".remove()" function to do that. e.g
fruits=['apple', 'banana', 'pear','guava', 'grape', 'tomato']
fruits.remove('tomato',)
fruits.remove('guava')
print(fruits)

#to remove a particular index value or item we use the '.pop()' function with the index position with it or. e.g 
fruits=['apple', 'banana', 'pear','guava', 'grape', 'tomato'] 
fruits.pop(3)
fruits.pop()
print(fruits)

# to clear the items from a list we use the 'clear()' function. e.g
fruits=['apple', 'banana', 'pear','guava', 'grape', 'tomato']
fruits.clear()
print(fruits)

# to copy a list we use the '.copy() function 
# Note: this can only be done if u want to refer or assign the list being copied to a variable. e.g
x=['apple', 'banana', 'pear','guava', 'grape', 'tomato']
fruits=x.copy()
print(fruits)

# to reverse the positions of items in a list we use the '.reverse()' function. e.g
fruits=['apple', 'banana', 'pear','guava', 'grape', 'tomato']
fruits.reverse()
print(fruits)

# to join 2 lists can be done in 2 ways
#i)we can use the '+' operator and variables. e.g
x=['apple', 'banana', 'pear']
y=['guava', 'grape', 'tomato']
print(x+y)
#ii)we use the '.extend()' function to add one list to the end of the other list. e.g
x=['apple', 'banana', 'pear']
y=['guava', 'grape', 'tomato']
x.extend(y)
print(x)
'''
Methods performed in a list:
i) .append() -adds an item to the end of a list.
ii) .clear() -removes all items in a list.
iii) .copy() -copy a list to a selected variable.
iv) len() -returns the number of items in a list.
v) .extend() -add the items of a list to the end of another list
vi) .index() -returns the index value of an item, when the index point is specified.
vii) .insert() -adds an item to a specified position.
viii) .remove() -removes the item to a specified value.
ix) .reverse() -reverse the order of a list.
'''

#                               Tuple
#Tuple is a collection that is ordered and unchangeable. i.e the items in a tuple cannot be changed after the
#tuple has been created. tuples are written with the '()' bracket.  e.g
x= ('apple', 'banana', 'cherry')
print(x)

# To access the items in a tuple, we use index number to locate them.  e.g
x= ('apple', 'banana', 'cherry')
print(x[2])
print(x[0])

# To specify the range of items we want to display we use the range symbol ':'.  e.g
x= ('apple', 'banana', 'cherry', 'orange', 'melon')
print(x[1:4])
 #Note: in any operation where we can perform indexing, we can also perform negative indexing and we can also
#      range its indexes(both positive and negative).
print(x[-4:-1]) 

# To change the value of a tuple
#tuples are unchangeable but we can change them by converting them to list, changing the item or value and 
#then converting them back to tuples.
#to convert to a list we the 'list()' method  and  to convert to a tuple we use the 'tuple()' method.  e.g
x=('apple', 'banana', 'cherry')
y=list(x)
y[-1]='kiwi'
y[1]='grape'
y[0]='orange'
x=tuple(y)
print(x)

# To check if an item is present in a tuple we use the 'in' keyword and the 'if and else' statement to check
# if an item is in a tuple.
x=('apple','banana','cherry')
if 'apple' in x:
    print('yes, it is present')
else:
    print('not available')

# to join two or more tuples we use the '+' operator. e.g
x=('apple','banana','cherry')
y=('a','b','c')
z=x+y
print(z)

#Note: tuple constructor -- tuple().

#                                 Sets
# A set is a collection which is unordered and unindexed. in python sets are written in curly brackets '{}'.
x={'apple','banana','cherry'}
print(x)

# To access items in a set we can use either the loop sequence to interate(print or display all the items one
# by one) the items or values in a set or by checking if an item exists in a set.
# Note: since a set is unordered and unindexed the item in the set have no index value or length.
#to access the items in a set
x={'apple','banana','cherry'}
for x in x:
    print(x) 
#        or
if 'apple' in x:
    print('yes')
else:
    print('no')

#Change items in a set: once a set is created, the items or elements cannot be changed.

#To add items to a set we use the '.add()' method to add a single item and the '.update()' to add multiple
#items to a set. e.g
y={'apple','banana','cherry'}
y.add('kiwi')
y.add('blackcurrant')
y.update(['a','b','c','mango','orange'])
print(y)

#we can also get the length of a set, to do that we use the 'len()' method. e.g
x={'cherry', 'blackcurrant', 'c', 'b', 'banana', 'orange', 'a', 'mango', 'kiwi', 'apple'}
print(len(x))

# To remove an item from a set we use the '.remove()' method or the '.discard()' method. e.g
x={'cherry', 'blackcurrant', 'c', 'b', 'banana', 'orange', 'a', 'mango', 'kiwi', 'apple'}
x.remove('blackcurrant')
x.discard('kiwi')
x.remove('orange')
x.discard('grape')
print(x)
#Note: if u use the '.remove()' method to remove an item that is not present in a set, it will raise an error
#but the '.discard()' method will not raise an error if it is used.

# To empty a set or remove all the items in a set at once we use the '.clear()' method. e.g
x={'cherry', 'blackcurrant', 'c', 'b', 'banana', 'orange', 'a', 'mango', 'kiwi', 'apple'}
x.clear()
print(x)

# To delete a set completely we use the 'del' keyword.
x={'cherry', 'blackcurrant', 'c', 'b', 'banana', 'orange', 'a', 'mango', 'kiwi', 'apple'}
del x 
print(x)
#note: this will raise an error cause the set 'x' does not exist anymore.

# To join 2 or more sets together we use either the 'union()' method or the 'update()' method.
#Note:'union()' method returns a new set with all the items of both sets while 'update()' method inserts the
#     items of 1 set into another set.  e.g
x={"a", "b" , "c"}
y={1, 2, 3}
z=x.union(y)
print(z) 
#         or
x={"a", "b" , "c"}
y={1, 2, 3}
x.update(y)
print(x)

# Set constructor----- 'set()'
'''
The following are some methods performed on sets
-.add()                             Adds an element to the set
-.clear()                           Removes all the elements from the set
-.copy()                            Returns a copy of the set
-.difference()                      Returns a set containing the difference between two or more sets
-.difference_update()               Removes the items in this set that are also included in another, specified set
-.discard()                         Remove the specified item
-.intersection()                    Returns a set, that is the intersection of two other sets
-.intersection_update()             Removes the items in this set that are not present in other, specified set(s)
-.isdisjoint()                      Returns whether two sets have a intersection or not
-.issubset()                        Returns whether another set contains this set or not
-.issuperset()                      Returns whether this set contains another set or not
-.pop()                             Removes an element from the set
-.remove()                          Removes the specified element
-.symmetric_difference()            Returns a set with the symmetric differences of two sets
-.symmetric_difference_update()     inserts the symmetric differences from this set and another
-.union()                           Return a set containing the union of sets
-.update()                          Update the set with the union of this set and others
'''

#                                  Dictionary
# A dictionary is a collection that is unordered, changeable and indexed. Dictionaries are written curly 
# brackets '{}' and they have index values. Dictionaries are used to write items that have subcontents or 
# subitems allocated to them. e.g
x={
    'cars': 'mustang',
    'fruits':'apple',
    'places':'beach',
}
print(x)

#To access items in a dictionary, we can refer to the name of the item in a square bracket'[]' or by using the
#'.get()' method to access the items in a dictionary. e.g
x={
    'cars': 'mustang',
    'fruits':'apple',
    'places':'beach',
}
y=x['cars']
print(y)
#      or
y=x.get('places')
print(y)

#To change the value of an item in a dictionary, u must specify the item in a '[]' bracket and outline what u 
#want it to say.
x={
    'cars': 'mustang',
    'fruits':'apple',
    'places':'beach',
}
x['cars']='bentley'
x['fruits']='banana'
x['places']='beach'
print(x)

# To check if a key exists, we use the 'in' keyword to do that. e.g
x={
    'cars': 'mustang',
    'fruits':'apple',
    'places':'beach',
}
if 'fruits' in x:
    print('yes')
else:
    print('no')

# to check the length of a dictionary we use the 'len()' method. the length being checked is the key-value
# pairred length.
x={
    'cars': 'mustang',
    'fruits':'apple',
    'places':'beach',
}
print(len(x))

# We can also add items to a dictionary by using a new index and assigning a value to it. e.g
x={
    'cars': 'mustang',
    'fruits':'apple',
    'places':'beach',
}
x['food']='rice'
x['day']='friday'
print(x)

# To remove an item or a key we use the '.pop()' method to do these. e.g
x={
    'cars': 'mustang',
    'fruits':'apple',
    'places':'beach',
}
x.pop('fruits')
print(x)

# To delete a dictionary we use the 'del' keyword. e.g
x={
    'cars': 'mustang',
    'fruits':'apple',
    'places':'beach',
}
del x
print(x)
#Note: this will give an error cause the dictionary has been deleted, it no longer exists.

# To empty a dictionary we use the '.clear()' method. 
x={
    'cars': 'mustang',
    'fruits':'apple',
    'places':'beach',
}
x.clear()
print(x)

# To create a copy of a dictionary we use the 'copy()' method.
x={
    'cars': 'mustang',
    'fruits':'apple',
    'places':'beach',
}
y=x.copy()
print(y)

#Nested Dictionaries: these are dictionaries inside dictionaries.
my_family = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

print(my_family)

# The dictionary constructor-- dict()

'''
The following are methods performed on dictionaries
*.clear()                Removes all the elements from the dictionary
*.copy()                 Returns a copy of the dictionary
*.fromkeys()             Returns a dictionary with the specified keys and values
*.get()                  Returns the value of the specified key
*.items()                Returns a list containing a tuple for each key value pair
*.keys()                 Returns a list containing the dictionary's keys
*.pop()                  Removes the element with the specified key
*.popitem()              Removes the last inserted key-value pair
*.setdefault()           Returns the value of the specified key. If the key does not exist: insert the key, 
                         with the specified value
*.update()               Updates the dictionary with the specified key-value pairs
*.values()               Returns a list of all the values in the dictionary
'''

#                  If and Else statements(conditional statements)
'''
If and Else statements are also called 'Conditional statements'. They support the usual logical conditions 
from mathematics:
i)Equal to:                              a==b
ii)Not equal:                            a!=b
iii)Less than:                           a<b
iv)Less than or equal to:                a<=b 
v)Greater than:                          a>b
vi)Greater than or equal to:             a>=b

Note: If statements use the 'If' keyword and every if statement must have an else statement with the 'Else'
       keyword to end the statement.
Note: When writing if and else statements indentation is very important. if indentation is not present the 
      code will display an error.
An example of  an if and else statement:
'''
a=50
b=100
if a>b:
    print('a is greater than b')
else:
    print('b is greater than a') 

#Elif:The 'elif' keyword is used to add a sub-condition or another condition to a conditional statement.
#Note: conditional statements are usually in 2 parts:'if' statement and the 'else' statement. so we use 'elif'
#      keyword to add more conditions to a conditional statement(so it won't dispaly an error). e.g
a=20
b=20
if a<b:
    print('a is less than b')
elif a==b:
    print('a is equal to b')
else:
    print('a is greater than b')

#Short hand if and else statement: if you have only one statement to execute, one for 'if' and one for 'else',
#you can put it all in the same line. e.g
a=2
b=10
print('a is greater than b') if a>b  else print('a is less than b')

#There are 2 logical operators that are commonly used in if and else statements.
#1)AND:The 'and' keyword is used to combine conditional statements. The and operator only displays 'True' if
# both conditional statements are true, else it displays 'False'. e.g
a=200
b=50
c=500
if a>b and c>a:
    print('True')
else:
    print('False')

if a>b and c<a:
    print('True')
else:
    print('False')

#2)OR:The 'or' keyword is used to join conditional statements. The or operator will display 'True' so far one
# of the conditional statements is true, it will dispaly 'False' only when both conditional statements are
# false.  e.g
a=200
b=50
c=500
if a>b or a>c:
    print('True')
else:
    print('False')

if a<b or a>c:
    print('True')
else:
    print('False')

#Nested if and else: this is an if and else statement that is inside another if statement. e.g
x=41
if x>10:
    print('x is above ten')
    if x>20:
        print('x is above twenty')
    else:
        print('x is not above twenty')
else:
    print('x is not above ten')


#                           Loop in python 
#Loop simply means for something, event or code to occur or execute in a repeated or continous state.
#comment: eat, sleep, repeat(life loop)
# python has 2 loop commands
#i) while loop
#ii) for loop

#i)       while loop
#while loop executes a set of instructions or code as long as the statements condition is true, but once it is 
#false the code breaks or ends. e.g
# the code ends. e.g:
x=1
while x<=10:
    print(x)
    x= x+1

#Note: for as long as a loops condition is true, it will continue to execute.That is why a break statement is 
#needed so it does not go into an infinite loop
#In the above code, the break statement is 'x=x+1', it is used to force the loop to stop by making the condition
#false at a moment.

#The break statement: this is the official break statement of loops. it halts or stops a loop even if the 
#statement is true. It is represented by the 'break' keyword. ee.g
x=1
while x<6:
    print(x)
    if x==3:
        break
    x=x+1
#Note: it will stop at 3 because the condition states break when x==3.

#The continue statement: What this statement does is that when a condition is given or assigned to it, it will
#skip the result and move to the next one. That is if i say when x==3 'continue', what it will do is dat when 
#x==3 it will skip and move to the next one. e.g
x=1
while x<6:
    x=x+1
    if x==3:
        continue
    print(x)

#The else statement: This is used to run a block of code once, when the condition is no longer true. i.e it will
#print a message once when the condition is false. e.g
x=1
while x<6:
    print(x)
    x=x+1
    x=x+1
else:
    print('x is no longer less than 6')

#                           For Loop
#For loop is used for iterating over a sequence or collection(list,tuple,set,dictionary ) or even a string.
#Iterate means to display the contents in a collection or container or to seperate in an orderly manner. The 
#for loop uses the 'for' keyword. e.g
fruits=['apple','banana','x','y',5] 
for x in fruits:
    print(x)
#Note: The 'x' in the code above is used to represent any value that is not in the collection. It is a random
#value that is used to set the loop in motion. That is we can basically put anything there in place of that 'x'

#We can also loop through a string. e.g 
for x in 'banana':
    print(x)

#The break statement: This is used to bring the loop to a stop at a desired position. e.g
fruits=['apple','banana','cherry']
for x in fruits:
    print(x)
    if x=='banana':
        break
#Note:We can also make a loop stop before a point.All we have to do is to put 'break' before the print 
#statement. e.g
fruits=['apple','banana','cherry']
for x in fruits:
    if x=='banana':
        break
    print(x)

#The continue statement: This is used to hoop over,cross over or pass over an assigned position in a loop. e.g
fruits=['apple','banana','cherry']
for x in fruits:
    if x=='banana':
        continue
    print(x)
#The range() function: This can be used to loop through a set of code a specified number of times.
#Note:If we want to do these all we need to do is attach the code to the print statement.

#We can also use the range() function to loop through a sequence or set of numbers. By default the range of 
#numbers starts from 0 and increases by 1 and ends at a specified number but we can specify where want it to
#start from,where it will end and the sequence of increase. The loop always stops before the specified number.
for x in range(6):
    print(x)
#setting the parameter: range(where it starts,where it ends,sequence of increase). e.g
for x in range(0,20,3):
    print(x)
#Note:In range() function above, the 1st no is where it starts, the 2nd no is where it ends and the 3rd no 
#is the sequence of increase.

#Else statement:The 'else' keyword in a for loop specifies a block of code that should execute when the loop is
#finished. e.g
for x in range(2,4):
    print(x)
else:
    print('finally done')

#Nested loops:A nested loop is a loop inside a loop. The content of the inner loop will be executed once for 
#each of the contents of the outer loop. e.g
colours=['blue','red']
fruits=['apple','banana']
for x in colours:
    for y in fruits:
        print(x,y)


#                           Date and Time in python 
# A date in Python is not a data type of its own, but we can import a module named 'datetime' to work with 
# dates as date objects.
#for us be able to use date and time as a module we must import(copy) it into the code
import datetime
today_date=datetime.datetime.now()
print(today_date) 

#To create a date, we can use the 'datetime()' class constructor of the datetime module.
# The datetime() class requires three parameters to create a date: year, month, day.
#  e.g ------date=datetime.datetime(year, month,day)
import datetime
date=datetime.datetime(2020,11,6)
print(date)

#The strftime() Method
#to change the format of the date and time to suit ur preference we use '.strftime()' function to perform dis
#'.strftime()' means string format time. to read up on more 'strftime' reference u can visit "python strftime
#  reference"
import datetime
Date=datetime.datetime(2021,11,6)
print(Date.strftime('%a'))

'''
The following are some '.strftime()' references 
*%a--Weekday, short version                                               result--Wed
*%A--Weekday, full version                                                result--Wednesday
*%w--Weekday as a number 0-6, 0 is Sunday                                 result--3
*%d--Day of month 01-31                                                   result--31
*%b--Month name, short version                                            result--Dec
*%B--Month name, full version                                             result--December
*%m--Month as a number 01-12                                              result--12
*%y--Year, short version, without century                                 result--18
*%Y--Year, full version                                                   result--2018
*%H--Hour 00-23                                                           result--17
*%I--Hour 00-12                                                           result--05
*%p--AM/PM                                                                result--PM
*%M--Minute 00-59                                                         result--41
*%S--Second 00-59                                                         result--08
*%f--Microsecond 000000-999999                                            result--548513
*%z--UTC offset                                                           result--+0100
*%Z--Timezone                                                             result--CST
*%j--Day number of year 001-366                                           result--365
*%U--Week number of year, Sunday as the first day of week, 00-53          result--52
*%W--Week number of year, Monday as the first day of week, 00-53          result--52
*%c--Local version of date and time                                       result--Mon Dec 31 17:41:00 2018
*%x--Local version of date                                                result--12/31/18
*%X--Local version of time                                                result--17:41:00
*%%--A % character                                                        result--%
'''


#                          String formating
#String formating is implemented when we want to make sure that a string will display as expected. To do this
#we use the '.format()' method. The '.format()' method allows you to format selected parts of a string, i.e
#add certain values to a part of a string.
#To control such values we add placeholders(curly brackets{}) in the text and run the values you want to place
#through the '.format()' method. e.g
price=50
x='The price of the bag is {} dollars.' 
print(x.format(price))

#formating multiple values: if u want to use more values, u just add more values to the '.format()' method
#and add more placeholders to the text or string. e.g
quantity=2
item_no=57
price=50
order='i want {} pieces of item no {} for {} dollars.'
print(order.format(quantity,item_no,price))

#Also we can refer to the index values of the holding variables inside the placeholders, to be sure the values
#are placed inside the appropriate placeholders. e.g
quantity=2
item_no=57
price=50
order='i want {0} pieces of item no {1} for {2} dollars.'
print(order.format(quantity,item_no,price))

#We can also use named indexes by entering a name(variable name) inside the curly brackets and then using the
#names when passing the parameter values. e.g
order='i have a {carname} car, it is a {model}.'
print(order.format(carname='Toyota',model='Camry'))



#                               Setting criteria for Password 
username=input('pls enter ur username: ')
password=input('enter ur password: ')
print('ur username:',username, 'ur password:',password)

# we can arrive at this in another way, called 'the string format method'
result='username:{} password:{}'.format(username,password)
print(result)

# we can also use another method called 'the string intercollation'
result2= f'username: {username}  password: {password}' 
print(result2)


# to run a test to dictate the criteria for a password
pass_len=len(password)
if pass_len !=5:
    print('password must be 5 characters only')
else:
    print('welcome')
#          or
pass_len=len(password)
if pass_len !=5:
    print('password must be 5 characters only')
else:
    first_five=username[0:5]
    if first_five==password:
        print('registration successfull')
    else:
        print('password must be first 5 characters of username')

# to run a test to dictate criteria for password and username length
pass_len=len(password)
user_len=len(username)
if pass_len !=5 or user_len <5:
    print('ERROR')
    print('username does not meet length criteria(5 characters)')
    print('password must be 5 characters only')
else:
    first_five=username[0:5]
    if first_five==password:
        print('registration successfull')
    else:
        print('password must be first 5 characters of username')

#Another format on achieving the above criteria
username = input("Enter your username: ")
password = input("Enter your password: ")


if len(password) == 5:
    usernameFirstFiveCharater = ""
    for x in username:
        usernameFirstFiveCharater = usernameFirstFiveCharater + x
        if username.index(x) == 4:
            break

    if password == usernameFirstFiveCharater:
        print("GOOD TO GO")
    else:
        print("Password must be the first five characters of username")

else:
    print("Password cannot be more than five charaters")


#                         File handling in python 
#File handling has to do with creating, reading, updating and deleting files. The key function used for working
#with files is the 'open()' method.
# 'Open()': This is used to open a file so as to work or perform tasks with or on it. we use the 'open()' method 
# when u want to use the open mode. The 'open()' method takes 2 parameters when opening a file: 
# the filename with extension,the mode of opening. e.g
#file=open('file name with extension','mode of opening')
file=open('muna.txt','r')
print(file)
# we have 4 different modes of opening files.
# i)'r': opens in read mode- for u to read only, not allowing you to edit or change any content of the file.
#'r'-read mode
file=open('muna.txt','r')
print(file.read())
# ii)'a': opens in append mode- for u to edit or add new content into a file.
#'a'-append mode
file=open('munachi.txt','a')
file.write('this is a new file that was just appended')
# iii)'w': opens in write mode- for u to overwrite the contents(clear the previous content) that are on a file 
# and place in new contents to replace them.
#'w'-write mode
file=open('munachi.txt','w')
file.write('i think it cleared the former text cause this would not have showed')

# iv)'x': opens in create new file mode- This creates a new automatically when the parameters are passed in.

#'Read()': To read a file we use the 'read()' method to read the contents of the file. e.g
x=open('record,txt','r')
print(x.read())
#Note:by default 'read()' method reads all the lines and contents of the file.
#But we can specify what we want to be read:
#i)We can select that by using the index no of the characters in your file
#e.g: this is to read the first 10 characters in the file
x=open('records,txt','r')
print(x.read(10))
#ii)We can use the 'readline() method to read one specific line in the content of your file.
#Note: By default 'readline() method reads the first line only, but you can indicate which line by passing
#the index value of the line into the 'readline()' method. e.g
x=open('record.txt','r')
print(x.readline())
print(x.readline(1))
#iii)We can use the 'readlines()' method to read all the the lines of content in the file. e.g
x=open('record.txt','r')
print(x.readlines())

#Closing Files: It is always good to close a file when you are done with using it. Sometimes changes made in a
#file will not show or display until it is closed.
x=open('record.txt','r')
print(x.readlines())
x.close() 


#                      String formating in file handling
#String formating in file handling has to do with formating how the information in a file looks or is accepted.
#We have 2 ways or methods of formating in filehandling.
#1)the (f'''......'''') method:   
#we can format multiple lines of values using the 'f' key with 3 pairs of hyphens covering the lines of string.
#This is mainly used when u want to format the way strings or information enter into a file. e.g
first_name=input('enter ur firstname: ')
last_name=input('enter ur lastname: ')
nationality=input('which country are u from: ')
phone_number=input('enter ur phone number: ')
address=input('enter ur address: ')
user_details=f'''
First Name: {first_name}
Last Name: {last_name}
Nationality: {nationality}
Phone Number: {phone_number}
Address: {address}
'''
print(user_details)
#    or if i want to put this information in a file i can do this
x=open("user's details.txt","a")
x.write("user's details")
x.write(user_details)

#2)Escape sequence method: these are a bunch of symbols or sequence oriented symbols dat control the output 
#display of the contents of a file. they control how the data put into a file is arranged inside the file.
# an example of escape sequence symbol: \n--- next line   \t------ tab.  e.g
name=input('enter name: ')
activation_code=input('enter activation code: ')
user_data=f'Name:{name}\nActivation code:{activation_code}'
print(user_data)
#      or if i want to put this information in a file i can do this
file=open('user360.txt','w')
file.write(user_data)


# to create and get information from a file
#to create the file
name=input('enter name: ')
activation_code=input('enter activation code: ')
user_data=f'Name:{name}\nActivation code:{activation_code}'
file=open('user360.txt','w')
file.write(user_data)

act_code='USER360_0007'
file=open('user360.txt','r')
user_data=file.readlines()
x=user_data[1]
a=x.split(':')
#    or 
#x=user_data[1].spilt(':')
if x==act_code:
    print('success')
else:
    print('invalid code')

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


#                          Classes and Objects in Python(OOP)
#OOP means Object Oriented Programming
#In OOP virtually everything in python is an object with it's properties and methods. 
#In OOP we have 2 main forms : class and objects
#A class is like an object constructor or a blueprint for creating objects. It is a detailed guideline for 
#creating objects

#creating a class: To create a class, we use the 'class' keyword followed by the name of the class. Then we 
#list the properties of the class below. e.g
# creating a simple class
class MyClass:
    x=5
#Note:'x=5' is a property of the 'MyClass' class, so therefore if we decide to create an object or objects
#under this class, they will all have this property 'x=5' assigned to them.

#creating an object: we are going to use the above class to create an object, in order to show how basically
#objects are created.First we name the object and assign it to our class 'MyClass' then we declare it 
#properties or assign values to it's properties. e.g 
#creating an object in the class above
object1= MyClass()
print(object1.x) 

object2= MyClass()
print(object2.x)
#Note:The above are simple classes and objects.
#We are going to be creating objects and classes that are related and useful to real life.

#The __init__() function:This is used as a class constructor, it is used to create the properties that are
#assigned to a class and to assign the values to the properties. e.g
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
#Note:The __init__() function is called up anytime an object is being created, in order to assign the values to
#their appropriate properties.

#Object Methods:These are functions or operations that are created for specific reasons, as conditional additional
#properties or functions that are assigned to an object so they can perform a particular thing. e.g
    def myfunc(self):
        print('hello my name is ',self.name)
    def myfunc2(self):
        print('i am ',self.age,' yrs old.')
#Note:For us to use this methods with objects we must first assign values to the properties of the class and 
#then call the functions and attach them to an object. e.g
Guy1=person('Godwin',22)
Guy1.myfunc()
Guy1.myfunc2()

#Self parameter:This is used to refer to the current instance of the class and is used to access properties 
#that belong to a class.
#Now that we have understood the functions used to create a class and the objects under it, we are going to
#create an elaborate class with objects under it.
#creating a class
class Human:
    def __init__(self,name,age,height):
        self.name=name 
        self.age=age
        self.height=height
    def talk(self):
        print(f"my name is {self.name}")
        print(f"i am {self.age} yrs old")
        print(f"i am {self.height}metres in height")
    def eat(self):
        print('i am eating my food; yum yum')
        print('i will ask for more if i am done')
  
person1= Human('yetunde',21,1.60)
print(person1.name)
print(person1.age)
print(person1.height)
person1.talk()
person1.eat()

person2= Human('CodeX',20,1.65)
print(person2.name)
print(person2.age)
print(person2.height)
person2.talk() 
person2.eat()

#a class on dogs
class Dog():
    def __init__(self,name,skin_colour,breed):
        self.name=name
        self.skin_colour=skin_colour
        self.breed=breed
    def bark(self):
        print(f'{self.name} is barking')
    def play(self):
        print(f'{self.name} is to fetch and bring the ball')
    def eat(self):
        print(f"{self.name} is eating it's food; yum yum yum")
        print(f'{self.name} is to lap for more when done')

Dog1= Dog('ricky','black with brown spots','bull mastif')
print(Dog1.name)
print(Dog1.skin_colour)
print(Dog1.breed)
Dog1.bark()
Dog1.play()
Dog1.eat()

# class that collects input from user.
class Humans:
    def __init__(self,name,age,height):
        self.name=name
        self.age=age
        self.height=height
    def talk(self):
        print(f'Hi, my name is {self.name}')
        print(f'i am {self.age}yrs old')
        print(f'i am {self.height}metres in height.')
    def eat(self):
        print('i am eating; yum yum ')
        print('i will ask for more when i am done')

person1= Humans(name=input('enter ur name: '),age=input('enter ur age: '),height=input('enter ur height: '))
print(person1.name) 
person1.talk()


#                         Inheritance
#Inheritance has to do with things or properties or even attitudes that are passed down from parents to their 
#children.Inheritance in python allows us to create classes that inherit or possess all the properties and 
#methods of another class.In inheritance we have 2 types of classes
#i)Parent class:This is the class being inherited from.it is also called Base class.
#ii)Child class:This is the class that inherits the properties and methods from another class.it is also called
#Derived class. 

#creating a parent class:Any class can be a parent class,whether it has properties and methods or not.
#Note:when a class does not have properties(i.e you do not use the class constructor  '__init__(self)' to
#construct properties) python automatically assigns an invisible class constructor that has the pass keyword 
#below it, which signifies that there are no available properties for this.(def __init__(self):)--invisible
#                                                                          (   pass            )   constructor
#e.g
class Cattle:                                             #(This is a class with properties)
    def __init__(self,name,no_of_legs):
        self.name=name
        self.no_of_legs=no_of_legs
    def animalsound(self):
        print('The animal makes a sound')
#               or
class Cattles:                                        #(this is a class without properties using the invisible)
    def animalsound(self):                         #(class constructor method                              )
        print('The animal makes a sound')

#creating a child class:To create a child class that inherits the properties and methods of another class, you
#must set the parent class as a parameter when creating the child class. e.g
class Cow(Cattle):                                    #class Cow(Cattle):
    def walk(self):                                   #     pass
        print('the cow moves around')
#Note:When you want to create a child class that inherits the properties of the parent class you have to use the
#'pass' keyword or the invisible class constructor method when creating the child class to be able to achieve 
#that.The 'pass' keyword is used to denote that no properties or methods are going to be passed. 
#we will now create a parent class and some child classes with it
class Animals:
    def __init__(self,name,no_legs):
        self.name=name
        self.no_legs=no_legs
    def animals_sound(self):
        print(self.name,' made a sound')

class Dogs(Animals):
    def eat(self):
        print(self.name,' is eating a bone')

class Monkeys(Animals):
        pass

class Cats(Animals):
        pass

dogs1=Dogs('bingo',4)
dogs1.animals_sound()
dogs1.eat()

monkeys1=Monkeys('chip',2)
monkeys1.animals_sound()

cats1=Cats('scratch',4)
cats1.animals_sound()
#Note:The above code us that when a child class is going to inherit only the properties of it's parents class
#then it cannot have it's own properties but it can have methods which only answer to it like the Dog class in
#our code.

#We can have child classes that have their own properties, what this does is that the child class properties
#will overwrite or override the properties of the parent class thereby making it's own properties what it 
#answers to.But it will still answer to the methods of the parent class and also it's own methods if it has.We
#use the class constructor in the child classes to achieve this.
#An example of this is the below classes.
 

#child classes over-riding parent properties.
class Animal:
    def animalsound(self):
        print('The animal makes a sound')

class Horse(Animal):
    def __init__(self,name):
        self.name=name
    def walk(self):
        print(self.name,' moves around')

class Cat(Animal):
    def __init__(self,name):
        self.name=name
    def walk(self):
        print(self.name,' moves around')

horse1=Horse('gringo')
print(horse1.name)
horse1.animalsound()
horse1.walk()
cat1=Cat('scratchy')
print(cat1.name)
cat1.walk()
cat1.animalsound()
#Note:In the above code the parent class did not have properties, but the properties of the child class was 
#used to override that and we saw that our objects had properties from the child classes.The objects had methods
#from both the child class and the parent class.
#Note:When u add the __init__() function to a child class, the child class will no longer inherit the parent's
#__init__() function(properties).

#We can create a child classes that can keep both their own properties and their parent classes properties to
#To achieve this there are 2 methods:

#i)We can call up the parent's properties or the __init__() function below the child's __init__() function and
#make sure that all the parameters that are in the parent's__init__() function are also in the child's__init__()
#function. e.g
class Person:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
    def printname(self):
        print(self.fname,self.lname)

class Student(Person):
    def __init__(self,fname,lname):
        Person.__init__(self,fname,lname)

#ii)We can use the 'super()' function.This makes the child class inherit all the methods and properties from the
#parent class.We will put the super() function below the child's __init__() function with the parameters of the
#parent class beside the super() function and also inside the child's __init__() function. e.g
class pErson:
    def __init__(self,fname,lname):
       self.fname=fname
       self.lname=lname
    def printname(self):
        print(self.fname,self.lname)

class sTudent(pErson):
    def __init__(self,fname,lname):
        super().__init__(fname,lname)
#Note:The main difference between the 2 methods is that the first one you put all parameters inside the 
#__init__() function of the parent class beside the name of the parent class while the second one, once you use
#the 'super()' function you don't need the name of the parent class and the parameter inside the __init__()func
#you just need the one's that are associated to the properties of the parent's class.
#A good example of a parent class and child classes that keep both their properties and their parent's properties
class ANIMAL:
    def __init__(self,name,no_legs):
        self.name=name
        self.no_legs=no_legs
    def animalsound(self):
        print(self.name,' makes a sound')

class DOG(ANIMAL):
    def __init__(self,name,no_legs,sound):
        ANIMAL.__init__(self,name,no_legs)
        self.sound=sound
    def eat(self):
        print(self.name,' is eating a bone')

class CAT(ANIMAL):
    def __init__(self,name,no_legs):
        super().__init__(name,no_legs)

dog2=DOG('Bingo',4,'Bark')
dog2.animalsound()
dog2.eat()
print(dog2.sound)
print(dog2.name)

cat2=CAT('Scratchy',4)
print(cat2.name)
print(cat2.no_legs)
cat2.animalsound()
#Note:In the above code, it shows us that we can add new methods and properties to a child class that is using
#both it's own properties and it's parent's properties.