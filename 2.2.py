
#1

def exer1():
    x = input ('Give me an number,please.\n')
    return float(x)


#3

def exer3(x):
    print ('$',round(x,2),sep="")


#2
def encode (str):
    y = ('')
    for i in range (len(str)):
        y = y+chr(ord(str[i])+1)
    return y

#3

def decode (str):
    x = ('')
    for i in range (len(str)):
        x = x + chr (ord(str[i])-1)
    return x



#Test Cases

#exer1
print ('Hello','This','is','my','program','2.2 Data Types', sep = '\n')
x = exer1()
print (x)

#exer3
print (exer3(5.1112345))

#exer4

print (encode ('cheese'))

#exer5

print (decode('difftf'))


