# Exercise 1: Print First 10 natural numbers using while loop

n=1
while n<=10:
    print(n)
    n+=1


# Exercise 2: Print the following pattern
# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5

for i in range(6):
    for j in range(i):
        print(j+1,end=' ')
    print('\n')


# Exercise 3: Calculate the sum of all numbers from 1 to a given number

print("Enter number :",end=' ')
n=int(input())
sum=0

for i in range(n+1):
    sum+=i
print("Sum is :",sum)

# Solution 2: Using the built-in function sum()

n = int(input("Enter number "))
# pass range of numbers to sum() function
x = sum(range(1, n + 1))
print('Sum is:', x)


# Exercise 4: Write a program to print multiplication table of a given number

val=int(input())

for i in range(1,11):
    print(i*val)




