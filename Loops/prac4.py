# Exercise 12: Display Fibonacci series up to 10 terms

# first two numbers
n1, n2 = 0, 1

print("Fibonacci sequence:")
# run loop 10 times
for i in range(10):
    # print next number of a series
    print(n1, end="  ")
    # add last two numbers to get next number
    res = n1 + n2

    # update values
    n1 = n2
    n2 = res
