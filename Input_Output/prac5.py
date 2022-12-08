############################################################################
# QUESTION 5 : Accept a list of 5 float numbers as an input from the user  #
############################################################################

#https://pynative.com/python-accept-list-input-from-user/

numbers = []

# 5 is the list size
# run loop 5 times
for i in range(0, 5):
    print("Enter number at location", i, ":")
    # accept float number from user
    item = float(input())
    # add it to the list
    numbers.append(item)

print("User List:", numbers)