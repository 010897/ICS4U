
'''
Program:    a5.py
Name:Carla Carolina Perez Romero
Date:May
Desc:       
'''

import os

### PROGRAM YOUR FUNCTIONS HERE! ###


#1
'''
This funtion computes the power of x(n)
'''
def power (x,n):
    if n == 0:
        return 1
    else:
        #It returns the base raised to the exponent
        return x * power (x,n-1)
#2
'''
This function computes the power of x(n) more efficiently.
'''
def morePower (x,n):
    if n == 0:
        return 1
    elif (n % 2) == 0:
        return (x,n//2) * power (x,n//2)
    elif (n%2)==1:
        #Return the base raised to the esponent but more efficiently.
        return x * power (x,n//2) * power (x,n//2)
#3
'''
This function finds the greatest common factor of any two numbers. The GCF is the largest number that divides evenly into both numbers.
'''
def GCF (a,b):
    if b == 0:
        return a
    else:
        #Return the GCF of two numbers.
        return GCF (b,a%b)
#4
'''
This function checks whether a string is a palindrome (a word that is the same forwards and backwards.
'''
def isPalindrome(string):
    if string == "":
        return True
    elif string [0] == string [-1] and isPalindrome(string[1:-1]):
        #Returns True/False if the string is a palindrome
        return True

#5
'''
This function prints all files in a given folder, including files in all of its subfolders.
'''
def printFiles(root):

    #The root is the imput the folder to search

    initialFiles=os.listdir(root)

    for i in range (len(initialFiles)):
        tf=os.path.isdir(os.path.join(root,initialFiles[i]))
        if tf==True:
            path=os.path.join(root,initialFiles[i])
            printFiles(path)


        if tf==False:
            path=os.path.join(root,initialFiles[i])
            print(path)
            #There is no return but the output is all files in the given folder.











'''
files = os.listdir()
path = os.path.joim (path1,path2)
tf = os.path.isdir(path)
'''




if __name__=="__main__":
    ### PUT ANY EXTRA CODE (TESTING, ETC) HERE ###
    pass

    #print (power(5,3))
    #print (morePower(5,3))
    #print (GCF(36,20))
    print (printFiles("a5test"))

    '''
    a.txt
    b.txt
    folder1
    folder2
    none
    '''




