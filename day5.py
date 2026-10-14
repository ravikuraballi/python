#what is oops
#oop stands for object-oriented programming.
#oop is a programming method that organize code using classes and objectts.


#2.what is a class?
#a class is a blueprint for creating objects.

#class classname:
#variables and methods
 #pass

class Student:
    name = "ravi"
    age = 20

print(Student.name)
print(Student.age)    


#what is an object?
class Student:
    name = "ravi"

s1 = Student()

print(s1.name)

#the __init__()
#the __init__()method is a special method that is called when an object is created.

class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
s1 = Student("ravi",20)
s2 = Student("ram",21)

print(s1.name,s1.age)
print(s2.name,s2.age)



#methods in class
#a method is a function defined inside a class
class Student:
    def __init__(self,name):
        self.name = name
    def display(self):
        print("Student name:",self.name)

s1 = Student("ravi")
s1.display()

#inheritance
class Animal:
    def eat(self):
        print("Animal is eating")
class Dog(Animal):
    def bark(self):
        print("dog is barking")

d = Dog()
d.eat()
d.bark()
