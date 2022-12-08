# Write a program to use for loop to print the following reverse number pattern

# 5 4 3 2 1 
# 4 3 2 1 
# 3 2 1 
# 2 1 
# 1


# for i in range(5):
#     for j in range(5-i,0,-1):
#         print(j,end=' ')
#         j-=1
#     print('\n')


# Exercise 8: Print list in reverse order using a loop
# list1 = [10, 20, 30, 40, 50]
# # reverse list
# new_list = reversed(list1)
# # iterate reversed list
# for item in new_list:
#     print(item)


# list1 = [10, 20, 30, 40, 50]
# # get list size
# # len(list1) -1: because index start with 0
# # iterate list in reverse order
# # star from last item to first
# size = len(list1) - 1
# for i in range(size, -1, -1):
#     print(list1[i])


# Exercise 9: Display numbers from -10 to -1 using for loop

# for i in range(-10,0,1):
#     print(i)

# Exercise 10: Use else block to display a message “Done” after successful execution of for loop
# for i in range(5):
#         print(i)
# else:
#         print("Done!")


# Exercise 11: Write a program to display all prime numbers within a range
start = 25
end = 50
print("Prime numbers between", start, "and", end, "are:")

for num in range(start, end + 1):
    # all prime numbers are greater than 1
    # if number is less than or equal to 1, it is not prime
    if num > 1:
        for i in range(2, num):
            # check for factors
            if (num % i) == 0:
                # not a prime number so break inner loop and
                # look for next number
                break
        else:
            print(num)