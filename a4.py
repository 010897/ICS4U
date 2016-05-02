'''
Program:a4.py
Name: Carla Carolina Perez Romero
Date: April 15th 2016.
Desc:
'''

# Import required libraries.
import copy, random, timeit

def funcTimer(func):
    '''
    Time the specified function, running it 100 times with a random array.
    '''
    
    # Create the strings to be run.
    arrayStr = 'array = [random.randint(0,1000) for i in range(200)]'
    funcStr = '{}; a4.{}(array)'.format(arrayStr, func.__name__)

    # Run the test and return the result.
    return timeit.timeit(funcStr, setup='import random, a4', number=100)
#1
'''
 This function takes an array and swaps the elements at index a and b.
 It has no return- it changes the input array, which changes the value of array in the calling funtion.
'''
def swap(array,a,b):
    '''

    There is no return - this function modifies the input array directly.
    '''
    #This variable will store the original value of the element a in the array.
    aOriginal = array [a]
    #Element a is equal element b.
    array [a] = array [b]
    #Element b in array is equal to the original value of a.
    array [b] = aOriginal

    return array
#2
def findMin(array):
    '''
    This funtion takes an array and returns the index of the smallest element in array.
    '''
    #Returns the index of the smallest element in array.
    return array.index(min(array))


def sort(array):
    '''
    This function takes an unsorted array and sorts it in increasing order, according to the algorythm assigned, which in this case is simple sort.
    '''

    # Make a copy of array, so that the input array isn't modified.
    array = copy.deepcopy(array)

    #Empty list of sorted numbers.
    emptyList = []
    #For loop to compare all the unsorted numbers.
    for i in range (len(array)):
        #Selecting the smallest number in array and storing it in a variable named min.
        min = findMin(array)
        #Adding/Copying the smallest number in array to the end of the list.
        emptyList.append(array[min])
        #Removes the smallest number from the unsorted list.
        del array [min]
    #Returns the sorted array.
    return emptyList




    # Return the sorted array.
    return

if __name__=="__main__":
    ### PUT ANY EXTRA CODE (TESTING, ETC) HERE ###
    # Create an array of random numbers.
    array = [random.randint(0,100) for i in range(10)]

    # Print the array, the sorted array, and the elapsed time for 100 tests.
    print(array)
    print(sort(array))
    print(funcTimer(sort))
    #print (findMin([9,2,3,4]))
