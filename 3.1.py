filename = 'drake.txt'
f = open (filename,'w')
f.write ('You used to\n')
f.write ('call me on my\n')
f.write ('cellphone.\n')
f.close()

f = open (filename,'r')
string1 = f.readline()
string2 = f.readline()
print (string2)
f.close()









