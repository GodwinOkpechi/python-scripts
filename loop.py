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