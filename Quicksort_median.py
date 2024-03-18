import random
from matplotlib import pyplot as plt
def QuickSortMedian(Array, p, r):
    if(r-p>2):
        (q,x)=PartitionMedian(Array,p,r)
        y=QuickSortMedian(Array, p, q-1)
        z=QuickSortMedian(Array,q+1,r)
        return(x+y+z)
    elif(r-p<1):
        return 0
    elif(r-p==1):
        if(Array[p]>Array[r]):
            Array[p],Array[r]=Array[r],Array[p]
        return 1
    else:
        if(Array[p]>Array[p+1]): 
            Array[p],Array[p+1]=Array[p+1],Array[p]
        if(Array[p+2]>Array[p+1]):
            return 2
        else:
            Array[p+2],Array[p+1]=Array[p+1],Array[p+2]
            if(Array[p]>Array[p+1]):
                Array[p],Array[p+1]=Array[p+1],Array[p]
            return 3

def PartitionMedian(Array, p, r):
    a=Array[r]
    b=Array[p]
    c=Array[(r+p)//2]
    if(a>=b):
        if(b>=c):
            pivot=b
            index=p
        elif (a>=c): 
            pivot=c
            index=(r+p)//2
        else: 
            pivot=a
            index=r
    else: 
        if(a>=c):
            pivot=a
            index=r
        else:
            if(b>=c):
                pivot=c
                index=(r+p)//2
            else:
                pivot=b
                index=p
    Array[r],Array[index]=Array[index],Array[r]
    i=p-1
    for j in range (p,r):
        if(Array[j]<=pivot):
            i+=1
            Array[i],Array[j]=Array[j],Array[i]
    Array[i+1],Array[r]=Array[r],Array[i+1]
    return(i+1,r-p)    

        
min=1
max=50000
step=100
sizes=list(range(min,max+1,step))
comparisons_random=[]
comparisons_good=[]
comparisons_bad=[]

for size in sizes:
    array_random=list(range(size))
    array_good=list(array_random)
    array_bad=(list(array_good))
    array_bad.reverse()
    random.shuffle(array_random)
    
    comparisons_random.append(QuickSortMedian(array_random,0,size-1))
    comparisons_good.append(QuickSortMedian(array_good,0,size-1))
    comparisons_bad.append(QuickSortMedian(array_bad,0,size-1))

plt.title("Quick sort (median)")
plt.xlabel("Size of array")
plt.ylabel("Number of comparisons")
plt.plot(sizes, comparisons_good, label="ordered array", color="green")
plt.plot(sizes, comparisons_bad, label="Reversed ordered array", color="red")
plt.plot(sizes, comparisons_random, label="Shuffled array", color="yellow")
plt.legend(["ordered array", "reversed ordered", "random array"])
plt.show()