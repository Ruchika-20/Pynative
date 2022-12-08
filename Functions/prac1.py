# Exercise 1: Create a function in Python
# Write a program to create a function that takes two arguments, name and age, and print their value.

def func(name,age):
    print(name,age)

func("ruhi",20)


# Exercise 2: Create a function with variable length of arguments
# Write a program to create function func1() to accept a variable length of arguments and print their value.

def func1(*args):
    for i in args:
        print(i)

func1(80,100,20)
func1(50,60)

# Exercise 3: Return multiple values from a function
# Write a program to create function calculation() such that it can accept two variables and calculate addition and subtraction. Also, it must return both addition and subtraction in a single return call.

def calculation(a, b):
    return a + b, a - b

# get result in tuple format
# unpack tuple
add, sub = calculation(40, 10)
print(add, sub)

#WAY 2

def calc(a,b):
    add=a+b
    sub=a-b
    return add,sub

res=calc(20,30)
print(res)


#If we use return we will have to afterwards print that also we can directly print the ans inside the function  definition as shown below:
def calc(a,b):
    add=a+b
    sub=a-b
    print(add,sub)

calc(20,30)

