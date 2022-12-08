#######################################################################################
# QUESTION 9 : Check Palindrome Number                                                #
#######################################################################################

# A palindrome number is a number that is same after reverse. For example 545, is the palindrome numbers

original_number=input()
print('original number',original_number,end='\n')

if str(original_number) ==str(original_number)[::-1]:

        print('Yes,It is a palindrome number')
        print('\n')

else:

        print('No, it is not a palindrome number.')


#WAY 2

# def palin(no):
#     print('original_number',no)
#     original_number=no

#     #reverse the given number
#     reverse_num=0
#     while no >0:
#         reminder=no%10
#         reverse_num=(reverse_num*10)+reminder
#         no//=10

#     #check with the original number
#     if original_number==reverse_num:
#         print("Yes")

#     else:
#         print("No")

# palin(121)
# palin(125)



