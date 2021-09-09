'''
#  a python program to collect the age of a user then check if the age is greater than 18
age=int(input('how old are u:' )) 
if age >= 18:
    print('welcome to our site, u met the age requirement')
else:
    print("pls we are redirecting u to our other site, u haven't met the age requirement")    






numbers=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
for x in numbers:
    print(x)

nums=range(0,20)
for y in nums:
    print(x) 

number=0
while number<=20:
    print (number)
    number=number+1
'''

#Write a program to show inheritance in classes and objects
class Chefs:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def cookrice(self):
        print(f'{self.name} is cooking rice')
    def bakecake(self):
        print(f'{self.name} is baking cake.')
class NigerianChefs:
    def __init__(self,name,age,state_of_origin):
        super().__init__(name,age)
        self.state_of_origin=state_of_origin
    def cookjollof(self):
        print(f'{self.name} is cooking jollof rice.')

name=input('enter ur name: ')
age=input('how old are u: ')
state_of_origin= input('which state are u from: ')

chef1=NigerianChefs(name,age,state_of_origin)
print(chef1.name)
chef1.cookjollof()
chef1.bakecake()
chef1.cookrice
    