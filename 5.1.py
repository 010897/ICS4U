def isOdd (list):
    if list == []:
        #If the list is empty, there's no odd numbers.
        return False
    ##This will check if the first number is odd or even. with mod if there is remainder is odd.Here you already check the 1st value.
    elif (list [0] % 2)== 1: #if the remainder is == '1' is odd.
        return True
    else:
        return isOdd(list[1:])

def factorial (x):
    #Step 1: Knowing when to stop
    if x  == 0:
        return 1
    if x < 0: #There is NO FACTORIAL for a negative number because it goes on forever.
        return None
    #Step 2 - 3: Take one step step and a smaller journey.
    return x * factorial (x-1) #5! = 5*4!
                               #4! = 4*3!

def loafLength(loaf):
     #1.- Know when to stop
     if loaf == []:
         return 0
     #2-3: Take one step and a smaller journey:
     loaf.pop() #cutting a slice, poping off one slice putting on a side.
     return 1 + loafLength(loaf)





#print (isOdd([4,12,14,20,1])) #Return false when there is NO odd numbers.Return TRUE when there is an odd number.
#print (loafLength([1,1,1,1,1,1,1,1]))
#print (factorial(-1))


#1 Know when to stop.
#2 Decide how to take one (small) step.
#3 Break the journey down into that step plus a smaller journey.

#three pieces
#1.-Exit condition
#2.-Small step
#3.-Calling the funtion again (recursively)

import os
root = '/Users/CarlaCpro/Desktop/FIELDSTONE GR 12/ICS4U'
files = os.listdir(root)


print (files)
print (files[0])

filePath = os.path.join(root, files [1])
print (filePath)

print (os.path.isdir(filePath))

