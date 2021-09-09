'''
#program to calculate amount after discount
Sch_fee=4535
discount_percent=50
discount_amount=(discount_percent*Sch_fee)/100
discounted_amount=Sch_fee - discount_amount
print('fee after discount is', discounted_amount)



#program to convert from kilometre to mile
km=564
mile= km*0.621
print('mile =', mile)   

# program to get the multiplication of 2 numbers without using *
a=5
b=3
sum=a+a+b+(a-b)
print(sum)


#program to dictate that password is first five characters of username
username=input('ur username: ')
password=input('ur password: ')
pass_len=len(password)
first_five=username[0:5]
if pass_len==5:
    if password==first_five:
        print('welcome to our site.')
    else:
        print('password must be first five characters of username.')
else:
    print('password must be 5 characters.')

# to create and get information from a file
#to create the file
name=input('enter name: ')
activation_code=input('enter activation code: ')
user_data=f'Name:{name}\nActivation code:{activation_code}'
file=open('user360.txt','w')
file.write(user_data)

act_code='USER360_0007'
file=open('user360.txt','r')
user_data=file.readlines()
x=user_data[1]
a=x.split(':')
#    or 
#x=user_data[1].spilt(':')
if x==act_code:
    print('success')
else:
    print('invalid code')
'''
# class that collects input from user.
class Human:
    def __init__(self,name,age,height):
        self.name=name
        self.age=age
        self.height=height
    def talk(self):
        print(f'Hi, my name is {self.name}')
        print(f'i am {self.age}yrs old')
        print(f'i am {self.height}metres in height.')
    def eat(self):
        print('i am eating; yum yum ')
        print('i will ask for more when i am done')

person1= Human(name=input('enter ur name: '),age=input('enter ur age: '),height=input('enter ur height: '))
print(person1.name) 
person1.talk()