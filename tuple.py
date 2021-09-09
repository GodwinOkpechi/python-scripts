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