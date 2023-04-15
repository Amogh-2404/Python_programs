def merge(array,s,m,e):
    n1=m-s+1
    n2=e-m
    L = [0]*(n1)
    R = [0]*(n2)
    
    for i in range(0, n1):
        L[i] = array[s + i]
    for j in range(0, n2):
        R[j] = array[m + 1 + j]
    
    i=0
    j=0
    k=s
    
    while i<n1 and j<n2:
        if L[i]<=R[j]:
            array[k]=L[i]
            i+=1
        else:
            array[k]=R[j]
            j+=1
        k+=1
        
    while(i<n1):
        array[k]=L[i]
        k+=1
        i+=1
    while(j<n2):
        array=R[j]
        k+=1
        j+=1
    

def mergesort(array,s,e):
    if s<e:
        
        middle = s+(e-s)//2
        mergesort(array,s,middle)
        mergesort(array,middle+1,e)
        merge(array,s,middle,e)

l =[1,5,4,3,6,7,8,9,2,10,1,1,1,1,1]
mergesort(l,0,len(l)-1)
print(l)

