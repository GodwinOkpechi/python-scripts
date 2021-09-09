#                                  If and Else statements
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