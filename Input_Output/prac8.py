############################################################################
# QUESTION 8 : Format variables using a string.format() method.            #
############################################################################

totalMoney = 1000
quantity = 3
price = 450
statement1 = "I have {1} dollars so I can buy {0} football for {2:.2f} dollars."
print(statement1.format(quantity, totalMoney, price))
