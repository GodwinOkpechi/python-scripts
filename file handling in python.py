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


#                    String formating in file handling
#String formating in file handling has to do with formating how the information in a file looks or is accepted.
#We have 2 ways or methods of formating in filehandling.
#1)the (f'''......''') method:   
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


# summary on file handling 
# There are 4 modes in File handling
# 1)Open
# 2)Read
# 3)closing
# 4)Deleting






