import random
def generare(j):
    x=[]
    for i in range(1,j+1):
        x.append(random.randrange(10000000))
    return x
