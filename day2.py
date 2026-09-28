#7.Logical Operators
age = 21
marks = 80

#AND operator
print(age>=18 and marks>=35)

#OR operator
print(age>=18 or marks>=18)

#not operator
print(not(age>=18))

#8.practice program
age=int(input("enter your age:"))
if age>=18 and age<=60:
    print("you are an adult")
else:
    print("you are not int the adult age range")


#9.types of conditional statements
   #if statement
   #if condition:
age = 20
if age>=18:
    print("you are eligible to vote")

 #if-else statement
num = int(input("enter a number:"))
if num%2==0:
    print("the number is even")
else:
    print("the number is odd")   

#if-elif-else statement
marks = int(input("enter your marks:"))
if marks>=90:
    print("grade A")
elif marks>=80:
    print("grade B")
elif marks>=70:
    print("grade c")
elif marks>=60:
    print("grade D")
else:
    print("grade fail")


#10.nested if statement
username = input("enter your username:")
password = input("enter your password:")

if username=="admin":
    if password=="admin123":
        print("login successful")
    else:
        print("invalid password")
else:
    print("invalid username")

