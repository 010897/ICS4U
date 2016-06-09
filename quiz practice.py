def sum(x):
    total=0
    for i in range (len(x)):
        total = total + x[i]
        return total

def min (x):
    lowest = x[0]
    for i in x:
        if i < lowest:
            lowest = i
            return lowest


