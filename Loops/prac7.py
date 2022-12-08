# Exercise 18: Print the following pattern
# Write a program to print the following start pattern using the for loop

# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# * * * * 
# * * * 
# * * 
# *

for i in range(6):
    for j in range(i):
        print("*",end=' ')
    print('\n')

for i in range(4):
    for j in range(4-i):
        print("*",end=' ')
    print('\n')


# WAY 2
#     rows = 5
# for i in range(0, rows):
#     for j in range(0, i + 1):
#         print("*", end=' ')
#     print("\r")

# for i in range(rows, 0, -1):
#     for j in range(0, i - 1):
#         print("*", end=' ')
#     print("\r")
