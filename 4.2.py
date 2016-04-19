def changeArray (array):
    array [0]=6

#Create a starting array
array = [1,2,3,4,5]
print (array)

changeArray(array)
print (array)


#THIS IS HOW WE VCAN MAKE SWAP WORK

#THIS CAN CAUSE SERIOUS PROBLEMS, ESPECIALLY WITH COPIES OF ARRAYS
array = [1,2,3,4,5]
array2 = array

print (array)
print (array2)

changeArray(array)
print (array)
print (array2)

#Lets try to stop this problem.

import copy
array = [1,2,3,4,5]
array2 = copy.deepcopy(array)
changeArray(array)
print (array)
print (array2)

#COMPLETELY SEPARATE TOPIC


#ONE WAY TO DELETE AN ITEM FROM ARRAY
del array [0]
print (array)
