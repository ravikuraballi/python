class Person:
    def __init__(self, name):
        self.name = name

    def show_name(self):
        print("name:",self.name)

class Student(Person):
    def study(self):
        print(self.name, "is studying")


s = Student("ravi")
s.show_name()
s.study()


#  Homework
# Create a Class:

# Write a class Mobile with attributes brand and price.
# Create two objects of the class and display their attributes using a method.
# Method Definition:

# Define a class Student with attributes name and marks.
# Write a method display_info() that prints the student's name and marks.
# Create multiple objects of the Student class and call the method on each.


class Mobile:
    def __init__(self,brand,price):
        self.brand = brand
        self.price = price

    def display_attributes(self):
        print("Brand:", self.brand)
        print("Price:", self.price)

# Create two objects of the Mobile class
mobile1 = Mobile("Apple", 999)
mobile2 = Mobile("Samsung", 799)

# Display their attributes
mobile1.display_attributes()
mobile2.display_attributes()


class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    def display_info(self):
        print("Student name:", self.name)
        print("marks:", self.marks)


s1 = Student("ravi", 85)
s2 = Student("ram", 90)
s3 = Student("raju", 95)

s1.display_info()
print()
s2.display_info()
print()
s3.display_info()
print()



# Homework
# Create a Class with a Constructor:

# Write a class Movie with attributes title and rating using the __init__() constructor.
# Define a method to display the movie’s title and rating.
# Add Default Parameters:

# Create a class Employee with attributes name, designation, and salary (default value of salary is 30,000).
# Write a method that displays the details of each employee.
# Create multiple Employee objects with different values for name and designation, and test the default salary behavior.

class Movie:
    def __init__(self, title, rating):
        self.title = title
        self.rating = rating

    def display(self):
        print("Movie Title:", self.title)
        print("Movie Rating:", self.rating)


# Create objects
m1 = Movie("KGF", 9.0)
m2 = Movie("Kantara", 8.5)

# Display movie details
m1.display()
print()
m2.display()



class Employee:
    def __init__(self, name, designation, salary=30000):
        self.name = name
        self.designation = designation
        self.salary = salary

    def display(self):
        print("Employee Name:", self.name)
        print("Designation:", self.designation)
        print("Salary:", self.salary)


# Create multiple objects
e1 = Employee("Ravi", "Software Developer")
e2 = Employee("Rahul", "Tester")
e3 = Employee("Arun", "Manager", 50000)

# Display employee details
e1.display()
print()
e2.display()
print()
e3.display()

#encapusulation
class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number
        self.__balance = balance

    def check_balance(self):
        print("Current Balance:", self.__balance)

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Amount deposited:", amount)
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount")
        elif amount <= self.__balance:
            self.__balance -= amount
            print("Amount withdrawn:", amount)
        else:
            print("Insufficient balance")


account = BankAccount("12345", 5000)

account.check_balance()
account.deposit(1000)
account.withdraw(2000)
account.check_balance()

# Try accessing private attribute
try:
    print(account.__balance)
except AttributeError:
    print("Cannot access __balance directly")                
