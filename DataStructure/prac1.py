# Exercise 1: Create a list by picking an odd-index items from the first list and even index items from the second
# IT IS ODD  INDEXING AND NOT ODD ELEMENTS 
list1 = [3, 6, 9, 12, 15, 18, 21]
list2 = [4, 8, 12, 16, 20, 24, 28]
list3=[]

odd_elements=list1[1::2]
print(odd_elements)

even_elements=list2[0::2]
print(even_elements)

print("Final List is : ")
list3.extend(odd_elements)
list3.extend(even_elements) # Output of using append : Final List is : [[6, 12, 18], [4, 12, 20, 28]]
print(list3)



# Exercise 2 : Write a program to remove the item present at index 4 and add it to the 2nd position and at the end of the list.
# pop(index): Removes and returns the item at the given index from the list.
# insert(index, item): Add the item at the specified position(index) in the list
# append(item): Add item at the end of the list.


list1=[1,2,3,4,5,6,7,8]
ele=list1.pop(4)
list1.insert(2,ele)
list1.append(ele)
print(list1)



# Exercise 3: Slice list into 3 equal chunks and reverse each chunk
list = [11, 45, 8, 23, 14, 12, 78, 45, 89]
length=len(list)
chunk_size=int(length/3)
start=0
end=chunk_size

#run the loop 3 times
for i in range(3):
    indexes=slice(start,end)

# get chunk
list_chunk = list[indexes]
print("Chunk ", i, list_chunk)
    
# reverse chunk
print("After reversing it ", list(reversed(list_chunk)))
start = end
end += chunk_size