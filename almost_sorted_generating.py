import random
def generare(j):
    x=[]
    k=random.randint(2,10)
    n=j*3//5
    for i in range(1,n):
        x.append(i)
    for i in range(j,n-1,-1):
        x.append(i)
    return x
