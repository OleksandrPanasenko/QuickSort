def QuickSort3Median(Array, p, r):
    if(r-p>2):
        (q1,q2,q3,v)=Partition3Median(Array,p,r)
        w=QuickSort3Median(Array, p, q1-1)
        x=QuickSort3Median(Array,q1+1,q2-1)
        y=QuickSort3Median(Array,q2+1,q3-1)
        z=QuickSort3Median(Array,q3+1,r)
        return(v+w+x+y+z)
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

def Partition3Median(Array, left, right):
    comparison=0
    a=b=left+2
    c=d=right-1
    p=Array[left]
    q=Array[left+1]
    r=Array[right]
    while b<=c:
        while Array[b]<q and b<=c:
            comparison+=1
            if Array[b]<p:
                Array[a],Array[b]=Array[b],Array[a]
                a+=1
            b+=1
        while Array[c]>q and b<=c:
            comparison+=1
            if Array[c]>r:
                Array[c],Array[d]=Array[d],Array[c]
                d-=1
            c-=1
        comparison+=1
        if b<=c:
            comparison+=1
            if Array[b]>r:
                comparison+=1
                if Array[c]<p:
                    Array[b],Array[a]=Array[a],Array[b]
                    Array[c],Array[a]=Array[a],Array[c]
                    a+=1
                else:
                    Array[b],Array[c]=Array[c],Array[b]
                Array[c],Array[d]=Array[d],Array[c]
                b+=1
                c-=1
                d-=1
            else:
                comparison+=1
                if Array[c]<p:
                    Array[b],Array[a]=Array[a],Array[b]
                    Array[c],Array[a]=Array[a],Array[c]
                    a+=1
                else:
                    Array[b],Array[c]=Array[c],Array[b]
                b+=1
                c-=1
    a-=1
    b-=1
    c+=1
    d+=1
    Array[left+1],Array[a]=Array[a],Array[left+1]
    Array[b],Array[a]=Array[a],Array[b]
    a-=1
    Array[left],Array[a]=Array[a],Array[left]
    return(a,b,d,comparison)