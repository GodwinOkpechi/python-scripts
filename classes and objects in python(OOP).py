'''
#                          Classes and Objects in Python(OOP)
#OOP means Object Oriented Programming
#In OOP virtually everything in python is an object with it's properties and methods. 
#In OOP we have 2 main forms : class and objects
#A class is like an object constructor or a blueprint for creating objects. It is a detailed guideline for 
#creating objects

#creating a class: To create a class, we use the 'class' keyword followed by the name of the class. Then we 
#list the properties of the class below. e.g
# creating a simple class
class MyClass:
    x=5
#Note:'x=5' is a property of the 'MyClass' class, so therefore if we decide to create an object or objects
#under this class, they will all have this property 'x=5' assigned to them.

#creating an object: we are going to use the above class to create an object, in order to show how basically
#objects are created.First we name the object and assign it to our class 'MyClass' then we declare it 
#properties or assign values to it's properties. e.g 
#creating an object in the class above
object1= MyClass()
print(object1.x) 

object2= MyClass()
print(object2.x)
#Note:The above are simple classes and objects.
#We are going to be creating objects and classes that are related and useful to real life.

#The __init__() function:This is used as a class constructor, it is used to create the properties that are
#assigned to a class and to assign the values to the properties. e.g
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
#Note:The __init__() function is called up anytime an object is being created, in order to assign the values to
#their appropriate properties.

#Object Methods:These are functions or operations that are created for specific reasons, as conditional additional
#properties or functions that are assigned to an object so they can perform a particular thing. e.g
    def myfunc(self):
        print('hello my name is ',self.name)
    def myfunc2(self):
        print('i am ',self.age,' yrs old.')
#Note:For us to use this methods with objects we must first assign values to the properties of the class and 
#then call the functions and attach them to an object. e.g
Guy1=person('Godwin',22)
Guy1.myfunc()
Guy1.myfunc2()

#Self parameter:This is used to refer to the current instance of the class and is used to access properties 
#that belong to a class.
#Now that we have understood the functions used to create a class and the objects under it, we are going to
#create an elaborate class with objects under it.
#creating a class
class Human:
    def __init__(self,name,age,height):
        self.name=name 
        self.age=age
        self.height=height
    def talk(self):
        print(f"my name is {self.name}")
        print(f"i am {self.age} yrs old")
        print(f"i am {self.height}metres in height")
    def eat(self):
        print('i am eating my food; yum yum')
        print('i will ask for more if i am done')
  
person1= Human('yetunde',21,1.60)
print(person1.name)
print(person1.age)
print(person1.height)
person1.talk()
person1.eat()

person2= Human('CodeX',20,1.65)
print(person2.name)
print(person2.age)
print(person2.height)
person2.talk() 
person2.eat()

#a class on dogs
class Dog():
    def __init__(self,name,skin_colour,breed):
        self.name=name
        self.skin_colour=skin_colour
        self.breed=breed
    def bark(self):
        print(f'{self.name} is barking')
    def play(self):
        print(f'{self.name} is to fetch and bring the ball')
    def eat(self):
        print(f"{self.name} is eating it's food; yum yum yum")
        print(f'{self.name} is to lap for more when done')

Dog1= Dog('ricky','black with brown spots','bull mastif')
print(Dog1.name)
print(Dog1.skin_colour)
print(Dog1.breed)
Dog1.bark()
Dog1.play()
Dog1.eat()

# class that collects input from user.
class Humans:
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

person1= Humans(name=input('enter ur name: '),age=input('enter ur age: '),height=input('enter ur height: '))
print(person1.name) 
person1.talk()


#                         Inheritance
#Inheritance has to do with things or properties or even attitudes that are passed down from parents to their 
#children.Inheritance in python allows us to create classes that inherit or possess all the properties and 
#methods of another class.In inheritance we have 2 types of classes
#i)Parent class:This is the class being inherited from.it is also called Base class.
#ii)Child class:This is the class that inherits the properties and methods from another class.it is also called
#Derived class. 

#creating a parent class:Any class can be a parent class,whether it has properties and methods or not.
#Note:when a class does not have properties(i.e you do not use the class constructor  '__init__(self)' to
#construct properties) python automatically assigns an invisible class constructor that has the pass keyword 
#below it, which signifies that there are no available properties for this.(def __init__(self):)--invisible
#                                                                          (   pass            )   constructor
#e.g
class Cattle:                                             #(This is a class with properties)
    def __init__(self,name,no_of_legs):
        self.name=name
        self.no_of_legs=no_of_legs
    def animalsound(self):
        print('The animal makes a sound')
#               or
class Cattles:                                        #(this is a class without properties using the invisible)
    def animalsound(self):                         #(class constructor method                              )
        print('The animal makes a sound')

#creating a child class:To create a child class that inherits the properties and methods of another class, you
#must set the parent class as a parameter when creating the child class. e.g
class Cow(Cattle):                                    #class Cow(Cattle):
    def walk(self):                                   #     pass
        print('the cow moves around')
#Note:When you want to create a child class that inherits the properties of the parent class you have to use the
#'pass' keyword or the invisible class constructor method when creating the child class to be able to achieve 
#that.The 'pass' keyword is used to denote that no properties or methods are going to be passed. 
#we will now create a parent class and some child classes with it
class Animals:
    def __init__(self,name,no_legs):
        self.name=name
        self.no_legs=no_legs
    def animals_sound(self):
        print(self.name,' made a sound')

class Dogs(Animals):
    def eat(self):
        print(self.name,' is eating a bone')

class Monkeys(Animals):
        pass

class Cats(Animals):
        pass

dogs1=Dogs('bingo',4)
dogs1.animals_sound()
dogs1.eat()

monkeys1=Monkeys('chip',2)
monkeys1.animals_sound()

cats1=Cats('scratch',4)
cats1.animals_sound()
#Note:The above code us that when a child class is going to inherit only the properties of it's parents class
#then it cannot have it's own properties but it can have methods which only answer to it like the Dog class in
#our code.

#We can have child classes that have their own properties, what this does is that the child class properties
#will overwrite or override the properties of the parent class thereby making it's own properties what it 
#answers to.But it will still answer to the methods of the parent class and also it's own methods if it has.We
#use the class constructor in the child classes to achieve this.
#An example of this is the below classes.
 

#child classes over-riding parent properties.
class Animal:
    def animalsound(self):
        print('The animal makes a sound')

class Horse(Animal):
    def __init__(self,name):
        self.name=name
    def walk(self):
        print(self.name,' moves around')

class Cat(Animal):
    def __init__(self,name):
        self.name=name
    def walk(self):
        print(self.name,' moves around')

horse1=Horse('gringo')
print(horse1.name)
horse1.animalsound()
horse1.walk()
cat1=Cat('scratchy')
print(cat1.name)
cat1.walk()
cat1.animalsound()
#Note:In the above code the parent class did not have properties, but the properties of the child class was 
#used to override that and we saw that our objects had properties from the child classes.The objects had methods
#from both the child class and the parent class.
#Note:When u add the __init__() function to a child class, the child class will no longer inherit the parent's
#__init__() function(properties).

#We can create a child classes that can keep both their own properties and their parent classes properties to
#To achieve this there are 2 methods:

#i)We can call up the parent's properties or the __init__() function below the child's __init__() function and
#make sure that all the parameters that are in the parent's__init__() function are also in the child's__init__()
#function. e.g
class Person:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
    def printname(self):
        print(self.fname,self.lname)

class Student(Person):
    def __init__(self,fname,lname):
        Person.__init__(self,fname,lname)

#ii)We can use the 'super()' function.This makes the child class inherit all the methods and properties from the
#parent class.We will put the super() function below the child's __init__() function with the parameters of the
#parent class beside the super() function and also inside the child's __init__() function. e.g
class pErson:
    def __init__(self,fname,lname):
       self.fname=fname
       self.lname=lname
    def printname(self):
        print(self.fname,self.lname)

class sTudent(pErson):
    def __init__(self,fname,lname):
        super().__init__(fname,lname)
#Note:The main difference between the 2 methods is that the first one you put all parameters inside the 
#__init__() function of the parent class beside the name of the parent class while the second one, once you use
#the 'super()' function you don't need the name of the parent class and the parameter inside the __init__()func
#you just need the one's that are associated to the properties of the parent's class.
#A good example of a parent class and child classes that keep both their properties and their parent's properties
class ANIMAL:
    def __init__(self,name,no_legs):
        self.name=name
        self.no_legs=no_legs
    def animalsound(self):
        print(self.name,' makes a sound')

class DOG(ANIMAL):
    def __init__(self,name,no_legs,sound):
        ANIMAL.__init__(self,name,no_legs)
        self.sound=sound
    def eat(self):
        print(self.name,' is eating a bone')

class CAT(ANIMAL):
    def __init__(self,name,no_legs):
        super().__init__(name,no_legs)

dog2=DOG('Bingo',4,'Bark')
dog2.animalsound()
dog2.eat()
print(dog2.sound)
print(dog2.name)

cat2=CAT('Scratchy',4)
print(cat2.name)
print(cat2.no_legs)
cat2.animalsound()
#Note:In the above code, it shows us that we can add new methods and properties to a child class that is using
#both it's own properties and it's parent's properties.
'''
'''
from math import sqrt
class calculator:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def add(self):
        return self.num1 + self.num2
    def subtract(self):
        return self.num1 - self.num2

calc=calculator(25,64)
print(calc.add())
print(calc.subtract())
print(sqrt(25))
#    or if u want to collect input
num1=int(input('enter ur first number: '))
num2=int(input('enter ur second number: '))
calc=calculator(num1,num2)
'''
'''
#            class-work
class Chefs:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def cookrice(self):
        print(self.name,' is cooking rice.')
    def bakecake(self):
        print(self.name,'is baking cake.')

class NigerianChefs(Chefs):
    def __init__(self,name,age,state_of_origin):
        super().__init__(name,age)
        self.state_of_origin=state_of_origin
    def cookjollof(self):
        print(self.name,' is cooking jollof rice.')

name=input('enter ur name: ')
age=input('how old are u: ')
state_of_origin=input('which state are u from: ')

chef1=NigerianChefs(name,age,state_of_origin)
print(chef1.name)
chef1.cookrice()
chef1.cookjollof()
chef1.bakecake()


'''

'''
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
'''

name='godwin'[::-1]
print(name)