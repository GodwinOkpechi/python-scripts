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


#                    String formating in file handling
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
