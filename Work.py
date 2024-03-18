import os

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




path=(os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__))))
file_name=input("Write name of file: ")
files_possible=(os.listdir(path))
while(file_name not in files_possible):
    file_name=input("There is no file with that name in directory \nWrite name of file : ")
    files_possible=(os.listdir(path))

file=open(os.path.join(path,file_name))
number=file.readline()
number=int(number)

array=[]
for i in range(number):
    array.append(int(file.readline()))
array_second=list(array)
comparisons_second=QuickSortMedian(array_second,0,len(array)-1)
comparisons_first=QuickSort(array,0,len(array)-1)
to_file=''
to_file+=str(comparisons_first)+' '
to_file+=str(comparisons_second)
file=open(os.path.join(path,"is31_Panasenko_04_output.txt"),"w")
file.write(to_file)
file.close()