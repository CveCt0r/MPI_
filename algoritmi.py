from gen import generare
def bubble(x):
    n=len(x)-1
    comp=0
    intersch=0
    for i in range(n):
        for j in range(1,n+1):
            comp+=1
            if x[i]>x[j]:
                intersch+=1
                x[i],x[j]=x[j],x[i]
    #print 'comparari= ',comp
    #print 'interschimbari= ', intersch
    #return intersch
def selection(x):
    comp=0
    inter=0
    for i in range(len(x)):
        k=i
        for j in range(i,len(x)):
            comp+=1
            if x[j]<x[k]:
                k=j
            if i!=k:
                inter+=1
                x[i],x[k]=x[k],x[i]

#    print 'comparari',comp,'interschibmari', inter
    return comp,inter
def insertion(x):
    comp=0
    inter=0
    for i in range(1,len(x)):
        aux=x[i]
        j=i-1
        while j>=0 and aux<x[j]:
            comp+=2
            x[j+1]=x[j]
            j-=1
        x[j+1]=aux
        inter+=1
#    print 'comparari',comp,'interschibmari', inter
    #return x
def quick(x,s,d):
    if s<d:
        q=partitie(x,s,d)
        x=quick(x,s,q)
        x=quick(x,q+1,d)
    return x
def partitie(x,s,d):
    v=x[s]
    i=s-1
    j=d+1
    while i<j:
        i+=1
        while x[i]<v:
            i+=1
        j-=1
        while x[j]>v:
            j-=1
        if i<j:
            x[i],x[j]=x[j],x[i]
    return j

def merge(x,s,d):
    comp=0
    inter=0
    if s<d:
        m=(s+d)//2
        x=merge(x,s,m)
        x=merge(x,m+1,d)
        x=interclasare(x,s,m,d)
    return x

def interclasare(x,s,m,d):
    c=[]
    i=s
    j=m+1
    while i<=m and j<=d:
        if x[i]<=x[j]:
            c.append(x[i])
            i+=1
        else:
            c.append(x[j])
            j+=1
        while i<=m:
            c.append(x[i])
            i+=1
        while j<=d:
            c.append(x[j])
            j+=1
        for i in range(len(c)):
            x[i+s]=c[i]
        return x

def countingsort(x,m):
    f=[0]*(m+2)
    n=len(x)
    y=[0]*(n+1)
    for i in range(0,n):
        f[x[i]]=f[x[i]]+1

    for i in range(2,m+1):
        f[i]=f[i-1]+f[i]

    for i in range(n-1,-1,-1):
        y[f[x[i]]]=x[i]
        f[x[i]]=f[x[i]]-1

    for i in range(0,n):
        x[i]=y[i+1]
    return x

x=[]
j=pow(10,9)
print 'numar elemente', j
#bubble(x)
#insertion(x)
#selection(x)
quick(generare(j),0,len(x)-1)
#merge(x,0,len(x)-1)
#countingsort(x,max(x))
