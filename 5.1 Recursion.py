#1
def laugh (n):
    if n == (0):
        return ""
    return "HA " + laugh(n-1) #when you are in the step to a smaller journey you are suppose to do something with the function that will shrink make the smaller journey.

#2
def sum (numbers):
    if len (numbers) == 1:
        return numbers [0]
    elif numbers == []:
        return None
    else:
        return numbers [0] + sum(numbers[1:])
#3
def allEqual(x):
    if len (x) == 1:
        return True
    return x [0] == x[1] and allEqual(x[1:])

#4
def countDown (n):
    if n == 0:
        return None
    else:
        print (n)
        countDown(n-1)
#5
def countUp (n):
    if n == 0:
        return None
    else:
        countUp(n-1)
        print (n)




























#print (laugh(5))
#print (sum([1,50]))
#print (allEqual([2,2,2]))
print (countDown(5))
print (countUp(5))


