#######################################################################################
# QUESTION 5 : Check if the first and last number of a list is the same               #
#######################################################################################
# Write a function to return True if the first and last number of a given list is same. If numbers are different then return False.

# Given list: [10, 20, 30, 40, 10]
# result is True

# numbers_y = [75, 65, 35, 75, 30]
# result is False

list1=input()
list=list1.split()

if list[0]==list[-1]:
    print("True")

else:
    print("False")

# WAY 2
# def first_last_same(numberList):
#     print("Given list:", numberList)
    
#     first_num = numberList[0]
#     last_num = numberList[-1]
    
#     if first_num == last_num:
#         return True
#     else:
#         return False

# numbers_x = [10, 20, 30, 40, 10]
# print("result is", first_last_same(numbers_x))

# numbers_y = [75, 65, 35, 75, 30]
# print("result is", first_last_same(numbers_y))
