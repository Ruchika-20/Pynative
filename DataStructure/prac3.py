#Exercise 8: Iterate a given list and check if a given element exists as a key’s value in a dictionary. If not, delete it from the list
# Given:
# roll_number = [47, 64, 69, 37, 76, 83, 95, 97]
# sample_dict = {'Jhon':47, 'Emma':69, 'Kelly':76, 'Jason':97}
# Expected Outcome:
# After removing unwanted elements from list [47, 69, 76, 97]

roll_number = [47, 64, 69, 37, 76, 83, 95, 97]
sample_dict = {'Jhon': 47, 'Emma': 69, 'Kelly': 76, 'Jason': 97}

print("List:", roll_number)
print("Dictionary:", sample_dict)

# create new list
roll_number[:] = [item for item in roll_number if item in sample_dict.values()]
print("after removing unwanted elements from list:", roll_number)



#Exercise 9: Get all values from the dictionary and add them to a list but don’t add duplicates
#Given:
# speed = {'jan': 47, 'feb': 52, 'march': 47, 'April': 44, 'May': 52, 'June': 53, 'july': 54, 'Aug': 44, 'Sept': 54}
# Expected Outcome:
# [47, 52, 44, 53, 54]


speed = {'jan': 47, 'feb': 52, 'march': 47, 'April': 44, 'May': 52, 'June': 53,
         'july': 54, 'Aug': 44, 'Sept': 54}

print("Dictionary's values - ", speed.values())

speed_list = list()

# iterate dict values
for val in speed.values():
    # check if value not present in a list
    if val not in speed_list:
        speed_list.append(val)
print("unique list", speed_list)


# Exercise 10: Remove duplicates from a list and create a tuple and find the minimum and maximum number
# Given:
#sample_list = [87, 45, 41, 65, 94, 41, 99, 94]
# Expected Outcome:
# unique items [87, 45, 41, 65, 99]
# tuple (87, 45, 41, 65, 99)
# min: 41
# max: 99

sample_list = [87, 52, 44, 53, 54, 87, 52, 53]

print("Original list", sample_list)

sample_list = list(set(sample_list))        #list is converted into set as it only contains unique elements
print("unique list", sample_list)

t = tuple(sample_list)
print("tuple ", t)

print("Minimum number is: ", min(t))
print("Maximum number is: ", max(t))