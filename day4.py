#why do we use functions?
print("hello world")
print("hello ravi")
print("hello ravi")

#using function
def say_hello():
    print("hello ravi")
say_hello()
say_hello() 

#function syntax
#def function_name():
   # statement
#function_name()

def add():
    a = 10
    b = 20
    print(a+b)

add() 

#function with parameters
def add(a,b):
    print(a+b)

add(10,20)
add(100,200)    

#function with return
def add(a,b):
    return a+b
result = add(10,20)
print(result)

#difference between print()and return:

def square(num):
    return num*num
x = square(5)
print(x)
print(x+10)

#difference types of function arguments
#A.positional arguments
def student(name,age):
    print(name,age)
student("ravi",20)    

#B.keyworld arguments
def student(name,age):
    print(name,age)
student(age=20,name="ravi")

#c.default arguments
def greet(name="Student"):
    print("hello",name)

greet()
greet("ravi")

#D.variable length arguments
def add_all(*numbers):
    print(sum(numbers))


add_all(10,20,30)
add_all(10,20,30,40,50)


#local and global variable
# a local variable is created inside a function is normally accessible only there

def show():
    x = 10
    print(x)
show()

#a global variable is created outside the function

x = 100

def show():
    print(x)
show()   

#lambda function
#lambda function is a small anonymous function

square = lambda x:x*x
print(square(5))
print(square(10))
