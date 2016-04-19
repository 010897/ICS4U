'''
Program:a3.py
Name:Carla Carolina Perez Romero
Date: April 15th 2016
Desc:
'''



'''
This stores information in form of a list in a variable name database
'''
database = [
    ['ICS4U', 'Assignment 1', 'Luke Skywalker', '3+'],
    ['ICS4U', 'Assignment 1', 'Han Solo', '4-'],
    ['SPH3U', 'Unit 1 Test', 'Leia Organa', '4'],
    ['SPH3U', 'Unit 1 Test', 'Luke Skywalker', '3-'],
    ['SPH4U', 'Unit 1 Test', 'Yoda', '4+'],
    ['SPH4U', 'Unit 1 Test', 'Anakin Skywalker', '3'],
    ['MHF4U', 'Unit 1 Test', 'Boba Fett', '2+'],
    ['MHF4U', 'Unit 1 Test', 'Kylo Ren', '3'],
    ['MHF4U', 'Unit 1 Test', 'Chewbacca', '4']
    ]

string = 'ICS4U\tAssignment 1\tLuke Skywalker\t3+\nSPH4U\tUnit 1 Test\tYoda\t4+\n'


#1

'''
This function opens a file and writes the given string to the file, then closes the file.

'''

def writeString(filename,string):
    f = open (filename,'w')
    # This command is allowing the function to write a string.
    f.write (string)
    #It is a command use to close a file
    f.close()
#2
'''
This function opens a file and reads the ENTIRE file to a string, than it closes the file, and returns the string.
'''

def readString (filename):
    f = open (filename,'r')
    string = f.read()
    f.close()
    #It is returning a string containing the contents of the file
    return string
#3
'''
This function opens a file and writes the given number to the file, than it closes the file. it has no return.
'''
def writeNum (filename,number):
    f = open (filename,'w')
    #This command allows you to write a number using 'str'to a file. It is transforming a string into a number.
    f.write (str(number))
    f.close()
#4

'''
    This function opens,reads and closes a file, and returns the number contained in the file.
    If the number is a float then the function returns a float, otherwise it returns a string.
'''
def readNum (filename):
    f = open (filename,'r')
    number = f.read()
   #This if statement is allowing to find and allowe to recognize a string or a float.
    if '.' in number:
        return float (number)
    else:
        return int (number)
    f.close ()
    #It will return an integer or a float containing the contents of the file.
    return number


'''
    This is an extra function that will add a TSV into a single row.
'''
def row2TSV(row):
    string = '\t'.join(row)
    return string
#5
'''
This funciton turns a 2-dimensional array into a TSV string.
A TSV string has a tab between each 'column' of data, and a newline between each 'row' of data.
'''
def array2TSV(array):
    string = ""
    for i in range (len(array)):
        string = string + row2TSV(array[i]) + ('\n')
   #It return a string representation of the 2D array.
    return string
#6

'''
This function turs a TSV string into a 2D array.
'''
def TSV2array(string):
    #Creation of an empty list
    emptyList = []
    #the variable list is equal spliting and adding '\n'.
    list = string [:-1].split ('\n')
    #For loop to add a tab into the list.
    for i in range (len(list)):
        emptyList = emptyList + [list[i].split('\t')]
    #Returns a 2D array containing the data from the string.
    return emptyList


#7
'''
This function writes a 2D array to a file as a TSV string.
'''
def writeTSV(filename,array):
    #This variable will open the file and allows it to be written.
    f = open (filename,'w')
    #This will write arrayTSV into array.
    f.write (array2TSV(array))
    #It is important to always close a file after using.
    f.close()

#8

'''
This function reads a TSV file and returns its contents as a 2D array.
'''
def readTSV(filename):
    #Opens the file and allows for it to be read.
    f = open (filename,'r')
    #allows the TSVarray to be read.
    list = TSV2array(f.read())
    f.close()
    #It returns a 2D array containing the data from the file.
    return list
















#Function TESTER
#print (writeString('a3.txt','Hello beautiful'))
#print (readString('a3.txt'))
#print (writeNum('a3.txt',15))
# #print (readNum('a3.txt'))
#x = readNum('a3.txt')
#print(x*2)
#print (array2TSV(database))
#print (row2TSV(['This','is','a','string']))
#print (array2TSV(database))
#print (TSV2array(string))