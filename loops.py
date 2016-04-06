#1. Print each element of x on a seperate line
x = [1,2,3]
for i in x:
    print (i)

#2. Print each element of x on a seperate line
x = ['hello','this','is','a','test']
for i in x:
    print (i)

#3. Print each element of x on a seperate line
x = range(100)
for i in x:
    print (i)

#4. Print each element of x on a seperate lines, where n is the number of elements in x
x = ['This','is','a','test']
for i in range(len(x)) :
    print (i+1)

#5. For each element of x, print its index and its value
#EX:
#0 this
#1 is
#2 a
#3 test
x = ['This','is','a','test']
for i in range (len(x)):
    print (i,x[i])
