'''
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

# Date---- 02/07/2021
# append 10 friends to a list
friend_1=input("enter first friend's name: ")
friend_2=input("enter second friend's name: ")
friend_3=input("enter third friend's name: ")
friend_4=input("enter fourth friend's name: ")
friend_5=input("enter fifth friend's name: ")
friend_6=input("enter sixth friend's name: ")
friend_7=input("enter seventh friend's name: ")
friend_8=input("enter eighth friend's name: ")
friend_9=input("enter ninth friend's name: ")
friend_10=input("enter tenth friend's name: ")
Friends=[]
Friends.append(friend_1)
Friends.append(friend_2)
Friends.append(friend_3)
Friends.append(friend_4)
Friends.append(friend_5)
Friends.append(friend_6)
Friends.append(friend_7)
Friends.append(friend_8)
Friends.append(friend_9)
Friends.append(friend_10)
print('These are ur 10 friends', Friends)

# write a program to collect 2 inputs from a user and compare using 'if statement'.
x=int(input('enter first amount: '))
y=int(input('enter second amount: '))
if x>y:
    print('First Amount is greater than Second Amount')
elif x==y:
    print('First Amount is equal to Second Amount')
else:
    print('Second Amount is greater than First Amount')   

Student grading system using inputs to derive score and if and else to derive grade
score=int(input('enter score of student: '))
if score>=70:
    print('A')
elif 70>score>=60:
    print('B')
elif 60>score>=50:
    print('C')
elif 50>score>=40:
    print('D')
elif 40>score>=30:
    print('E')
else:
    print('F- advised to withdraw ')

# Assignment: write a python program to print even numbers from 1-100
x=0
while x<=100:
    print (x)
    x=x+2

# Assignment: write a python program to print odd numbers from 1-100
x=1
while x<=100:
    print (x)
    x=x+2
'''
# # python program to collect a user's details and save them to a file.
# first_name=input('enter ur firstname: ')
# last_name=input('enter ur lastname: ')
# nationality=input('which country are u from: ')
# phone_number=input('enter ur phone number: ')
# address=input('enter ur address: ')
# user_details=f'''
# First Name: {first_name}
# Last Name: {last_name}
# Nationality: {nationality}
# Phone Number: {phone_number}
# Address: {address}
# '''
# x=open("user's details.txt","a")
# x.write("user's details")
# x.write(user_details)
'''
# Write a python program to implement 'MADLIBS'
compatriot=input('Another word for tout: ')
serve=input('Another word for receive: ')
love=input('Another word for dictate: ')
strength=input('Another word for corruption: ')
faith=input('Another word for Unrest: ')
hero=input('Another name for guardian: ')
heart=input('Another word for games: ')
might=input('Another word for falsehood: ')
freedom=input('Another word for tyranny: ')
peace=input('Another word for bribery: ')
unity=input('Another word for restrain: ')
print('------------------------------------------------------------------------------------------------')
print('Anthem for the Nigerian Politicians')
print('Arise O ',compatriot)
print("Nigeria's call obey to ",serve," our father's land with ",love,' and ',strength,' and ',faith)
print('The labour of our ',hero,"'s past shall never be in vain")
print('To serve with ',heart,' and ',might)
print('One nation bound in ',freedom,' and ',peace,' and ',unity)

'''
'''
#Write a python program to reverse a string without using any inbuilt function on python
name= 'godwin'
for x in name:
    print(name[-1])
    break
for x in name:
    print(name[-2])
    break
for x in name:
    print(name[-3])
    break
for x in name:
    print(name[-4])
    break
for x in name:
    print(name[-5])
    break
for x in name:
    print(name[-6])
    break
#        or
name='godwin'[::-1]
print(name)
def reversestr()

#   or
def reverse(string):
    if len(string)==0:
        return string
    else:
        return reverse(string[1:])+(string[0])
print(reverse('petroleum'))

#            or
name='james'
result=''
for x in name:
    result=x + result
print(result)
'''
def reverse(word):
    result=''
    for x in word:
        result=x+result
    return result
    
print(reverse('jango'))
'''
#Write a program to show 3 level inheritance in classes and objects
class Doctor:
    def __init__(self,name,age,hospital):
        self.name=name
        self.age=age
        self.hospital=hospital
    def treat_patients(self):
        print(self.name,' can treat patients.')

class Surgeon(Doctor):
    def __init__(self,name,age,hospital,):
        super().__init__(name,age,hospital)
    def surgery(self):
        print(self.name,' is performing a surgical operation.')

class Brain_Surgeon(Surgeon):
    def __init__(self,name,age,hospital):
        super().__init__(name,age,hospital)
    def brainsurgery(self):
        print(self.name,' can perform brain surgery.')
'''

#write a method in python to display the elements of a list thrice if it is a number and display the
#element terminated with '#' if it is not a number.
List=[19,0.63,'word']
for x in List:
    if x==int:
        print(f'{x}{x}{x}')                  #This is the code to perform the above program
    elif x==float:                           #nom we will put it in a condition.
        print(f'{x}{x}{x}')
    else:
        print(f'{x}#')

def determine():
    list=[19,0.63,'word']
for x in list:
    if x==int:
        print(f'{x}{x}{x}')                  
    elif x==float:                           
        print(f'{x}{x}{x}')
    else:
        print(f'{x}#')

#we can also create a function dat performs the same task but let's the user decide the values using input
#method.
def Determine():
    LIST=[]
    LIST.append(input('enter an example of a dataype: '))
    LIST.append(input('enter an example of another dataype: '))
    LIST.append(input('enter an example of another dataype: '))
    for x in LIST:
        if x==int:
            print(f'{x}{x}{x}')                  
        elif x==float:                           
            print(f'{x}{x}{x}')
        else:
            print(f'{x}#')
            
Determine()

#write a function 'is_vowel' that returns the value true if a given character is a vowel, otherwise return
#false.  
def is_vowel(x):
    if x=='a': 
        print('True, it is a vowel')
    elif x=='e':
        print('True, it is a vowel')
    elif x=='i':
        print('True, it is a vowel')
    elif x=='o':
        print('True, it is a vowel')
    elif x=='u':
        print('True, it is a vowel')
    else:
        print('False, it is not a vowel')
        
