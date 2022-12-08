# Exercise 4: Count the occurrence of each element from a list

sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]
print("Original list ", sample_list)

count_dict = dict()
for item in sample_list:
    if item in count_dict:
        count_dict[item] += 1
    else:
        count_dict[item] = 1

print("Printing count of each item  ", count_dict)

#Exercise 5 : Create a Python set such that it shows the element from both lists in a pair

list1 = [2, 3, 4, 5, 6, 7, 8]
print("First List ", list1)

list2 = [4, 9, 16, 25, 36, 49, 64]
print("Second List ", list2)

result = zip(list1, list2)
result_set = set(result)
print(result_set)


# Exercise 6: Find the intersection (common) of two sets and remove those elements from the first set
set1={23, 42, 65, 57, 78, 83, 29}
set2={57, 83, 29, 67, 73, 43, 48}
print("Set1 :",set1)
print("Set2 :",set2)
intersection=set1.intersection(set2)
print("Intersection is:",intersection)
for i in intersection:
    set1.remove(i)

print(set1)


#Exercise 7: Checks if one set is a subset or superset of another set. If found, delete all elements from that set

set1 = {57, 83, 29}
set2 = {57, 83, 29, 67, 73, 43, 48}

print("First Set ", set1)
print("Second Set ", set2)

print("First set is subset of second set -", set1.issubset(set2))
print("Second set is subset of First set - ", set1.issubset(set2))

print("First set is Super set of second set - ", set1.issuperset(set2))
print("Second set is Super set of First set - ", set1.issuperset(set2))

if set1.issubset(set2):
    set1.clear()

if set2.issubset(set1):
    set2.clear()

print("First Set ", set1)
print("Second Set ", set2)


