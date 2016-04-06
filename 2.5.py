#1
def joinList(list1,list2):
    return list1 + list2
#2
def printList(x):
    for i in x:
        print (i)

#3
def makeList():
    x = []
    while True:
        ask = input ('What is your input?\n')
        if ask == 'none':
            break
        else:
            x.append(ask)
    return x

#4
def multiDim(list1,list2):
  return [list1,list2]

#5
def printMultiDim(x):
    for i in x:
        print (i)



#TEST
#1
#print (joinList([1,2,3],[4,5,6]))
#2
#print (printList([1,2,3,4]))
#3
print (makeList())
#4
#print (multiDim([10,20,30],[40,50,60]))
#5
#print (printMultiDim([[1,2,3],[4,5,6],[7,8,9]]))