#                                   Sets
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
