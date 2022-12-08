
# Exercise 5: Display numbers from a list using loop
# Write a program to display only those numbers from a list that satisfy the following conditions
# The number must be divisible by five
# If the number is greater than 150, then skip it and move to the next number
# If the number is greater than 500, then stop the loop

# numbers = [12, 75, 150, 180, 145, 525, 50]
# # iterate each item of a list
# for i in numbers:
#     if i > 500:
#         break
#     elif i > 150:
#         continue
#     # check if number is divisible by 5
#     elif i % 5 == 0:
#         print(i)


# Exercise 6 : Write a program to count the total number of digits in a number using a while loop.
val=int(input())
cnt=0

while val!=0:
    val//=10        #to remove digits one by one from the last
    cnt+=1

print(cnt)