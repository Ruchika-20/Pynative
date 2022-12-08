#Exercise 13: Find the factorial of a given number
fact=1
val=int(input())        #6! = 6*5*4*3*2*1
for i in range(1,val+1):
    fact*=i

print(fact)

#OTHER WAY
# num = 5
# factorial = 1
# if num < 0:
#     print("Factorial does not exist for negative numbers")
# elif num == 0:
#     print("The factorial of 0 is 1")
# else:
#     # run loop 5 times
#     for i in range(1, num + 1):
#         # multiply factorial by current number
#         factorial = factorial * i
#     print("The factorial of", num, "is", factorial)



# Exercise 14: Reverse a given integer number
num = 76542
reverse_number = 0
print("Given Number ", num)
while num > 0:
    reminder = num % 10
    reverse_number = (reverse_number * 10) + reminder
    num = num // 10
print("Revere Number ", reverse_number)