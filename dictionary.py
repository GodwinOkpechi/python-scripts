#                           Dictionary
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