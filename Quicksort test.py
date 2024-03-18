import random
from matplotlib import pyplot as plt
def QuickSort(Array, p, r):
    if(p<r):
        (q,x)=Partition(Array,p,r)
        y=QuickSort(Array, p, q-1)
        z=QuickSort(Array,q+1,r)
        return x+y+z #+1
    else: return 0 #1

def Partition(Array, p, r):
    pivot_source=Array[r]
    pivot=pivot_source
    i=p-1
    for j in range (p,r):
        if(Array[j]<=pivot):
            i+=1
            Array[i],Array[j]=Array[j],Array[i]
    Array[i+1],Array[r]=Array[r],Array[i+1]
    return(i+1,r-p)


        
min=1
max=1000
step=10
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
    
    comparisons_random.append(QuickSort(array_random,0,size-1))
    comparisons_good.append(QuickSort(array_good,0,size-1))
    comparisons_bad.append(QuickSort(array_bad,0,size-1))

plt.title("Quick sort (ordinary)")
plt.xlabel("Size of array")
plt.ylabel("Number of comparisons")
plt.plot(sizes, comparisons_good, label="ordered array", color="green")
plt.plot(sizes, comparisons_bad, label="Reversed ordered array", color="red")
plt.plot(sizes, comparisons_random, label="Shuffled array", color="yellow")
plt.legend(["ordered array", "reversed ordered", "random array"])
plt.show()