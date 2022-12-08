
#######################################################################################
# QUESTION 6 : Display numbers divisible by 5 from a list                             #
#######################################################################################
# Iterate the given list of numbers and print only those numbers which are divisible by 5

list1 = [ int(i) for i in input().split(" ")]

for i in list1:
    if i%5==0:
        print(i)
