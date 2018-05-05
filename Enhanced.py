from almost_sorted_generating import generare
import time
import datetime
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
    return comp,inter

def insertion(x):
    for i in range(1,len(x)):
        aux=x[i]
        j=i-1
        while j>=0 and aux<x[j]:
            x[j+1]=x[j]
            j-=1
        x[j+1]=aux
    return x

def quick1(x,s,d):
    if len(x)<500:
        return insertion(x)
    if s<d:
        q=partitie(x,s,d)
        x=quick1(x,s,q)
        x=quick1(x,q+1,d)
    return x

def quick2(x,s,d):
    if s<d:
        q=partitie(x,s,d)
        x=quick2(x,s,q)
        x=quick2(x,q+1,d)
    return x




def partitie(x,s,d):
    v=x[(s+d)/2]
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

j=pow(10,5)
x=generare(j)
print 'numar elemente', j
#bubble(x)
#insertion(x)
start=int(round(time.time()*100000))
quick2(x,0,len(x)-1)
end=int(round(time.time()*100000))
print "----------timpul de executie quick2------------   %s " %(end-start)
#selection(x)
start=int(round(time.time()*100000))
quick1(x,0,len(x)-1)
end=int(round(time.time()*100000))
print "----------timpul de executie quick1------------   %s " %(end-start)

#merge(x,0,len(x)-1)
#countingsort(x,max(x))
end=time.time()
