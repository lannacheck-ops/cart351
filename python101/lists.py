# fruits = ["oranges","bananas","melons","strawberries"]
# for el in fruits:
#     print(f"I love {el}")

# #Can iterate through a sentence because each character holds an index
# testString = "A wonderful sunshiny day"
# for ch in testString:
#     print(ch)

#empty list
# newItems = []
# newItems.append("first")
# #append using a for loop:
# for i in range(2,10):
#     #i is between 2 and 10
#     newItems.append(f"{i} is the next item")

# for el in newItems:
#     print(el)

# listF = ['cats','dogs','parrots','pies']
# listF.remove('dogs')
# listF.remove('pies')# will throw a Value Error and ends program
# print(listF)

#Sorting
# listToSort = ['water','question','apples','wander']
# listToSortBools = [True,True,False,True]
# listToSortNums = [2.5,6,7,43,102.6,1,1.2,0.8]

# #Sorts in alphabetical order
# listToSort.sort()
# print(listToSort)
# #Sorts from true to false
# listToSortBools.sort()
# print(listToSortBools)

# listToSortNums.sort()
# print(listToSortNums)
#Pop removes item at the end of an array
# el = listToSort.pop() # take out at end
# print(f"item removed: {el}")
# print(f"rev list: {listToSort}")

#Joining two elements
# element_list = ["hydrogen", "helium", "lithium", "beryllium", "boron"]
# glue = " "
# single_str = glue.join(element_list)
# print(single_str)
# # How to split a string
# slicer = " "
# seperate_str = single_str.split(slicer)
# print(seperate_str)

#List slicing
# aList = [1,2,3,4,5,'a','b','c','d','e'] 
# #Get items from a list starting at position 1 and ending at position 5 (exclusive)
# print(aList[1:5])
# # Get elements starting from index 2 to the end of the list
# bList = aList[2:] #specify start and leave end blank
# print(bList)

# # Get elements until from start until index 5 
# cList = aList[:5] #specify end and leave start blank
# print(cList)

# # Get every second element from the list, starting from the second element (use the step)
# stepA = aList[1::2]
# print(f"Second step: {stepA}")

# # Get every third element from the list, starting from index 1 to 8(exclusive)
# stepB = aList[1:8:3]
# print(stepB)

# rList = [1,2,3,4,5,'a','b','c','d','e'] 
# rList[0:2] = 'zz'   ## replace [1,2] with ['z','z'] 
# print(rList)

franken_chp1 = open("data/frankenstein.txt").read()
print(franken_chp1)