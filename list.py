
#                             Lists
#list is a collection of data types which are ordered and changeable.They allow update by a programmer or coder 
#They are denoted by square brackets []. e.g
fruits=['apple', 'banana', 'pear', 'grape']
print('the fruits are', fruits)

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

# to clear the items from a list we use the '.clear()' function. e.g
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