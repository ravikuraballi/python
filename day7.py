#solid principles in python
class Student:
    def __init__(self,name):
        self.name = name

class StudentDatabase:
    def save(self,student):
        print(f"saving{student.name}to database...")

class ReportCard:
    def generate(self,student):
        print(f"generating report card for{student.name}...")

student = Student("ravi")

db = StudentDatabase()
db.save(student)

report = ReportCard()
report.generate(student)                        


# SRP Practice: Create a Book class that only stores details. Create another class that prints book details.
# OCP Practice: Build a billing system that calculates tax based on ProductType. Add Food, Electronics, etc., using subclasses.
# LSP Practice: Write a class Vehicle and subclasses like Bike, Boat. Avoid breaking behavior.
# DIP Practice: Make a HomeAppliance system where high-level class Remote works with abstract Appliance, and you can pass TV, AC, etc.

#1.SRP
class Book:
    def __init__(self,title,author,price):
        self.title = title
        self.author = author
        self.price = price

class BookPrinter:
    def print_details(self,book):
        print("Book Title:",book.title)
        print("Author:",book.author)
        print("price:",book.price)

book1 = Book("python Basics","ravi",350)

printer =BookPrinter()
printer.print_details(book1)

#2.ocp

from abc import ABC,abstractmethod

class Product(ABC):
    @abstractmethod
    def calculate_tax(self,price):
        pass

class Food(Product):
    def calculate_tax(self,price):
        return price *0.05

class Electronics(Product):
    def calculate_tax(self,price):
        return price *0.18

class Billing:
    def generate_bill(self,product,price):
        tax = product.calculate_tax(price)
        print("price:",price)
        print("Tax:",tax)
        print("Total:",price + tax)   

billing = Billing()

food = Food()
billing.generate_bill(food,1000)

electronics = Electronics()
billing.generate_bill(electronics,1000)

#dip

from abc import ABC, abstractmethod


class Appliance(ABC):
    @abstractmethod
    def turn_on(self):
        pass


class TV(Appliance):
    def turn_on(self):
        print("TV is turned ON")


class AC(Appliance):
    def turn_on(self):
        print("AC is turned ON")


class Remote:
    def __init__(self, appliance):
        self.appliance = appliance

    def press_power(self):
        self.appliance.turn_on()


tv = TV()
remote1 = Remote(tv)
remote1.press_power()

ac = AC()
remote2 = Remote(ac)
remote2.press_power()

