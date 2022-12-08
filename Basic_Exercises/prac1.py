
############################################################################
# QUESTION 1 : Calculate the multiplication and sum of two numbers         #
############################################################################

#WAY 1
# num_1=input()
# num_2= input()
# product = int(num_1)*int(num_2)
# sum=int(num_1) + int(num_2)    # We cannot simply write product = num1 * num2 else data type error will occur because num1 & num2 are bydeafult string data types also product and sum is of type string and so the number must be converted into integer to avoid the error because we are dealing with number 

# if product<=1000:
#     print(product)

# else:   
#     print(sum)

#WAY 2
def product_or_sum(num1 , num2):
    product = num1 * num2
    sum = num1 + num2

    if product<=1000:
        return product

    else:
        return sum

n1,n2=(input("enter number: ")).split()         #split is used for spacing
num1=int(n2)
num2=int(n1)
result=product_or_sum(num1,num2)
print(result)





