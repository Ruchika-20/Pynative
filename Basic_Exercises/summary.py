from itertools import islice  #itertools used for handling iterators
# #islice('abcdef',3)            
# print(list(islice('abcdef',3)) )       #0,stop
# print(list(islice('abcdef',None,3)) )  #0,stop
# print(list(islice('abcdef',2,4))   )   #start,stop
# print(list(islice('abcdef',2,6,2)))    #start,stop,step

# from heapq import merge
# a = [1,4,7] 
# b = [4,9,12] 
# c = [33,76,99]
# it = merge(a,b,c)
# it1 = list(it)
# print(it1)
# print(list(islice(it1,3))  )
# print(it1)  #suppose you have google query responses to show, millions of results, use 'merge' with 'islice' to process only generators and showing content with islice as per as page limit and stuff...
# print(list(islice(it1,None))) #returns complete list


#work of intern function : references to same memory address which have same value to avoid double memory consumption
import sys
s = 'he'
t = 'llo'

u = sys.intern('hello')
v = sys.intern(s+t)
if(u is v):
    print(id(u),id(v))

#Inplace means it will make a change in the list but upon returning the value it will return as none
#For eg A=[1,2,3,4]
#       B=A.append(5)     //this will update the list A as 1,2,3,4,5 
#       print(B)          // this will print "None" that means it has changed the value in its place so inPlace=True
#       print(A)           // this will print the updated list.....this means the change is made in its place butupon assigning it to the other variable it does not get changed and so returns the value as NONE

#Example of inPlace=False
# C=A+B
# while using concatenation we are updating the whole value of A+B and so the change is made in C as well so here inPlace = False


basket = ['a','x','b','c','d','e','d']
basket.sort()
basket.reverse()
print("Reversing again :", basket[::-1]) #inplace=False with to slicing 
print("Reversed list   :", basket)


# $join
print("\nJoin operation")
sentence = '-'
print(sentence.join(['hi','my','name','is','Parth']))   #does not add before first and after last
print(' '.join(['hi','my','name','is','Parth']))

# $split, default split is by white space
'Hello there, how are you'.split()

# $List unpacking
print("\nList unpacking")
a,b,c,d,*other,d = [1,2,3,4,5,6,7,8,9]  # d is overwritten with value as 9
print(a)
print(b)
print(c)
print(d)
print(other)
print(d)  

#if we  want to insert the element keeping the sequence of the list as intact i.e sorted then for that purpose bisect is used.
import bisect
cuts = [20,40,60,80]
grades = 'EDCBA'
print(grades[bisect.bisect(cuts,50)])
print([grades[bisect.bisect(cuts,x)] for x in [10,30,50,80,100]])


print("\nDictionary")
dictionary = {
  'a': [1,2,3],
  123: 'hello integer',           #First key of all same keys will be selected as key and last updated value as the value for the first key
  123.0:'hello float',  
  123.12:'hello double',
  False: True
}
print(dictionary)
print(dictionary['a'])
print(dictionary.get('a',"default_value"))
print(dictionary[123])        #prints float value (if a similar float present) will therefore print hello float and not hello integer
print(dictionary[123.0])      #prints float value

#Another way of creating dictionary
dictionary2 = dict(a=[1,2,3], b="asd")    #a,b are taken as key in form as strings
print(dictionary2)
print(dictionary2['b'])


#List with the dictionary as shown below :
print("\nList with dictionary")
my_list = [
  {
  'a': [1,2,3],
  'b': 'hello',
  'c': True
  },
  {
  'a': [4,5,6],
  'b': 'world',
  'c': False
  }
]

print(my_list[1]['a'])  #since it starts with 0 it will go to 1 and print the value of a ie. 4,5,6

from collections import defaultdict
def def_value(): 
    return "Not Present"
      
# Defining the default dict 
d = defaultdict(def_value) #default value would be used when calling a key that is not present
d["a"] = 1
d["b"] = 2
  
print(d["a"]) 
print(d["b"]) 
print(d["c"])  



#Use of default dictionary
d = defaultdict(set)
d['starts_with_l']
d['starts_with_p'].add('parth')
d['starts_with_l'].add('lathiya')
d['starts_with_l'].add('lavjibhai')
d               #function is called



#####################################################################################################################################
#                                                    PYNATIVE QUIZZES                                                               #
#####################################################################################################################################

#************************************
#          1) Beginner Quiz         #
#************************************

# 1) What is the Output of the following code?
# for x in range(0.5, 5.5, 0.5):
#   print(x)

# [0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5]
# [0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5]
# The Program executed with errors -->true

# Explanation
# We cannot use float numbers in range() function.




# 2) What is the output of the following code?
# def calculate (num1, num2=4):
#   res = num1 * num2
#   print(res)
# calculate(5, 6)

# 20
# The program executed with errors
# 30 --->true

# Explanation
# In Python, we can set default values for arguments. If the function is called without the argument, the default value is used.




# 3) Can we use the “else” block for for loop?
# for i in range(1, 5):
#     print(i)
# else:
#     print("this is else block statement" )
# No
# Yes --> true

# Explanation
# We can use the else block after the end of for loop and while loop. The else block is used to check the successful execution of a loop. If the loop executed successfully without any issues, the else block executes.




# 4) What is the output of the following code?
# var= "James Bond"
# print(var[2::-1])
# Jam
# dno
# maJ ---> true
# dnoB semaJ

# Explanation:
# Pick a range of items starting in the reverse direction starting from index 2 with step 1.




# 5) What is the output of the following code?
# sampleSet = {"Jodi", "Eric", "Garry"}
# sampleSet.add(1, "Vicki")
# print(sampleSet)

# {‘Vicki’, ‘Jodi’, ‘Garry’, ‘Eric’}
# {‘Jodi’, ‘Vicki’, ‘Garry’, ‘Eric’}
# The program executed with error --->true

# Explanation:
# The set is an unordered data structure. Therefore, we cannot access/add/remove its elements by index number.




# 6) What is the output of the following code?
# sampleList = ["Jon", "Kelly", "Jessa"]
# sampleList.append(2, "Scott")
# print(sampleList)

# The program executed with errors -->true
# [‘Jon’, ‘Kelly’, ‘Scott’, ‘Jessa’]
# [‘Jon’, ‘Kelly’, ‘Jessa’, ‘Scott’]
# [‘Jon’, ‘Scott’, ‘Kelly’, ‘Jessa’]

# Explanation:
# The append() method appends an item to the end of the list. Therefore, we cannot pass the index number to it.




# 7) What is the output of the following code?
# var1 = 1
# var2 = 2
# var3 = "3"
# print(var1 + var2 + var3)

# 6
# 33
# 123
# Error. Mixing operators between numbers and strings are not supported ---> true

# Explanation
# We cannot add strings and numbers together using the + operator. Either we can use the + operator to concatenate strings or add numbers.




# 8) What is the output of the following code?
# p, q, r = 10, 20 ,30
# print(p, q, r)

# 10 20
# 10 20 30 ---> true
# Error: invalid syntax

# Explanation
# In Python, We can do simultaneous assignments to more than one variable.







#*********************************************************
#          2) INPUT/OUTPUT QUIZZES                       #
#*********************************************************

# https://pynative.com/python/file-handling/

# 1) What is the output of the following print() function
# print(sep='--', 'Ben', 25, 'California')

# Syntax Error
# Ben–25–California
# Ben 25 California
# Ben–25 California

# Explanation:
# sep is keyword argument Any keyword arguments passed to print() function must come at the end, after the objects to display. Otherwise, you will get a Syntax Error positional argument that follows the keyword argument.
# The correct way is print('Ben', 25, 'California', sep='--')




# 2) What will be displayed as an output on the screen
# x = float('NaN')
# print('%f, %e, %F, %E' % (x, x, x, x))

# nan, nan, NAN, NAN
# nan, NaN, nan, NaN
# NaN, NaN, NaN, NaN,

# Explanation:
# %f, %e produces lowercase output, and %F, %E produces uppercase output.




# 3) Which of the following is incorrect file handling mode in Python
# wb+
# ab
# xr ---> true
# ab+




# 4)  What is the output of print('[%c]' % 65)
# 65
# A
# [A] ---> true
# Syntax Error

# Explanation:
# The c conversion type supports character conversion from ASCII code to the character. It also works for the Unicode




# 5) Which of the following is incorrect file handling mode in Python.
# r
# x
# t+ --->true
# b




# 6)  What is true for file mode x
# create a file if the specified file does not exist
# Create a file, returns an error if the file exists ---->true
# Create a file if it doesn’t exists else Truncate the existed file