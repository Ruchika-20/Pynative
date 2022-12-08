####################################################################################################
# QUESTION 11 : Write a Program to extract each digit from an integer in the reverse order.        #
####################################################################################################

# For example, If the given int is 7536, the output shall be “6 3 5 7“, with a space separating the digits.

int_value=int(input())

#Reversing a number
while int_value>0:
    last_digit=int_value%10
    int_value//=10      #removing the last digit and repeating the same process
    print(last_digit,end=' ')