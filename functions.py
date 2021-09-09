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

# note on Positional arguments and Named arguments
def do_something(num1,num2,num3):
    print('i love football')
    print(num1 + num2 * num3)
# the below function is a positional argument cause it's elements are derived from position.
do_something(30,40,50)
#     or
# the below function is a named argument cause it's elements are named or assigned to their units.
do_something(num3=50,num1=30,num2=40)