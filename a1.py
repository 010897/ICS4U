#1√
def helloWorld():
    print('Hello World')
#2√
def greet (name):
    print ('Hello',name,'!')


#3√
def greet2():
    name = input('What is your name?\n')
    print ('Hello,', name, '!')


#4√
def plus1(num):
   return num + 1
   plus1(num)


#5√
def max3(a,b,c):
    return max (a,b,c)
    max3(a,b,c)

#6
def printN(n):
    print (range (len (0,n)))



#7
def sumN(n):
   return range (len (1,n+1))
   sumN(n)
#8
def strFrirst(str):
    return str [:1]

#9
def strHalf(str):
    return str[:len(str)//2]


#10
def guessingGame(e):
  e = 8
  attempts = 0
  while True:
    guess = int (input('What is the number?\n'))
    attempts = attempts +1
    import time
    time.sleep (1)
    if guess==e :
        print ('That is correct, CONGRATULATIONS !')
        print ('You guessed in',attempts,'attempts')
        break


















#Testing Cases


#1
# helloWorld() √
#2
# greet('Bob') √
#3
# greet2() √
#4
#print (plus1(8))√
#5
#print (max3(6,9,8,))√
#6
#print (printN(4))-----
#7
#print (sumN(5))-----
#8
#print (strFrirst('Carla'))√
#9
#print (strHalf('Shetulun'))√
#10
#guessingGame(7)












