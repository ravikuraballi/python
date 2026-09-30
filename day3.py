#10.for loop
#syntax
#for variable in sequence:
for i in range(1, 6):
    print(i)

#for loop with a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)  

#11.while loop
i = 1
while i <= 5:
    print(i)
    i +=1   
#12.range
for i in range(1, 11):
    print(i)  

#13.break
for i in range(1,10):
    if i==5:
        break
    print(i)    

#continue
for i in range(1,10):
    if i==5:
        continue
    print(i)

#14.what is list?
fruits = ["apple", "banana", "cherry"]
print(fruits) 

#15.indexing in list
fruits = ["apple", "banana", "cherry","orange"]
print(fruits[0])
print(fruits[1])
print(fruits[2])
print(fruits[3])

#negative indexing
fruits = ["apple", "babana", "cherry","orange"]
print(fruits[-1])
print(fruits[-2])

#changing a list value
fruits = ["apple", "banana", "cherry"]
fruits[1] = "kiwi"
print(fruits)

#slicing
numbers = [10,20,30,40,50]

print(numbers[1:4])

#more examples
numbers = [10,20,30,40,50]

print(numbers[:3])
print(numbers[2:])
print(numbers[:])

#append
fruits = ["apple", "banana"]
fruits.append("cherry")
print(fruits)

#insert
fruits = ["apple", "banana"]
fruits.insert(1, "kiwi")
print(fruits)

#remove
fruits = ['apple', 'banana', 'cherry']
fruits.remove("banana")
print(fruits)

#pop
fruits = ['apple', 'banana', 'cherry']
fruits.pop(1)
print(fruits)

#sort()
numbers = [50,10,40,20,30]
numbers.sort()
print(numbers)

#revese()
numbers = [10,20,30,40,50]
numbers.reverse()
print(numbers)

#len()
fruits = ["apple", "banana", "cherry"]
print(len(fruits))
