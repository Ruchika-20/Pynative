#######################################################################################
# QUESTION 8 : Print the following pattern                                            #
#######################################################################################

# 1 
# 2 2 
# 3 3 3 
# 4 4 4 4 
# 5 5 5 5 5


# for i in range(6):
#     for j in range(i):
#         print(i,end=' ')
    
#     print('\n')



# 1 1 1 1 1 
# 2 2 2 2 
# 3 3 3 
# 4 4 
# 5


for i in range(6):
    for j in range(6-i):
        print(i,end=' ')
    
    print('\n')



# 5
# 4 4
# 3 3 3
# 2 2 2 2
# 1 1 1 1 1

# for i in range(6):
#     for j in range(i):
#         print(6-i,end=' ')
#     print('\n')
