
'''
Program:    a5.py
Name:Carla Carolina Perez Romero
Date:May
Desc:       
'''

import os

### PROGRAM YOUR FUNCTIONS HERE! ###

def power (x,n):
    if n == 0:
        return 1
    else:
        return x * power (x,n-1)

def morePower (x,n):
    if n == 0:
        return 1
    elif (n % 2) == 0:
        return (x,n//2) * power (x,n//2)
    elif (n%2)==1:
        return x * power (x,n//2) * power (x,n//2)

def GCF (a,b):
    if b == 0:
        return a
    else:
        return GCF (b,a%b)

def isPalindrome(string):
    if string == "":
        return True
    elif string [0] == string [-1] and isPalindrome(string[1:-1]):
        return True

def printFiles (root):
    files = os.listdir(root)
    if files == "":
        return None
    filePath = os.path.join(root,files[0])
    if os.path.isdir(filePath) == False:

        for i in range (len(files)):
            print (files [i] +str(1))


    '''
    elif os.path.isdir(filePath) == True:
        return printFiles(root)
        for i in range (files [i] +str (1)):
             print (files [0])
    '''












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
    print (printFiles('a5test'))




