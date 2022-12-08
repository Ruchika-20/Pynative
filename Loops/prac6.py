# Exercise 15: Use a loop to display elements from a given list present at odd index positions
lst=[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
for i in range(len(lst)):
    if i%2==1:
        print(lst[i])

#BETTER WAY
# my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# # stat from index 1 with step 2( means 1, 3, 5, an so on)
# for i in my_list[1::2]:
#     print(i, end=" ")


# Exercise 16: Calculate the cube of all numbers from 1 to a given number
print("input_number : ",end=' ')
val=int(input())

for i in range(1,val+1):
    print(i*i*i)

#WAY2
# input_number = 6
# for i in range(1, input_number + 1):
#     print("Current Number is :", i, " and the cube is", (i * i * i))


# Exercise 17: Find the sum of the series upto n terms
#For example, if n =5 the series will become 2 + 22 + 222 + 2222 + 22222 = 24690
n = 5
# first number of sequence
start = 2
sum = 0
# run loop n times
for i in range(0, n):
    print(start, end="+")
    sum += start
    # calculate the next term
    start = start * 10 + 2
print("\nSum of above series is:", sum)


