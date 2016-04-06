#1
def printChars(string):
    print ('\n'.join(string))
#2
def emailDomain(string):
   a = string.find('@')
   return string [a+1:]
def emailDomain2(string):
    a = string.split ('@')
    return a[1]
#3
def printSorted(string1,string2):
    if string1 < string2:
        print (string1)
        print (string2)
    else:
        print(string2)
        print (string1)

def compareLenghth(string1,string2):
    return len (string1)==len(string2)

def compareNoCase(string1,string2):
    return string1.lower() == string2.lower()

def compareStrip(string1,string2):
    return string1.strip()==string2.strip()



#test
#1
#printChars('abcd')√
#2
#print (emailDomain("myname@hotmail.com  "))
print (compareNoCase('Luke Skywalker','luke skywalker'))
print (compareStrip('hello  ','hello'))
