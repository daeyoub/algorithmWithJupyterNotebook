# -*- coding: utf-8 -*-

# 기초 알고리즘
# 1. selectionSort (선택정렬)
# 2. bubbleSort    (버블정렬)
# 3. insertionSort (삽입정렬)

def theLargest(A, last):
    largest = 0;
    for i in range(1, last):
        if(A[i] >= A[largest]): #if(A[i] > A[largest]): 오류. why???
            largest = i;
    return largest 

def selectionSort(A, n):      
    for last in range(n-1, 0,-1):
        largest= theLargest(A, last)               
        A[largest], A[last] = A[last], A[largest]  
              
def bubbleSort(A, n):
    for last in range(n-1, 0,-1): # 1<= last <= n-1
        for i in range(0, last):  # 0 <= i <= last-1
            if A[i] > A[i+1]: 
                A[i], A[i+1]=A[i+1], A[i]        

def insertionSort(A,n):
    for i in range(1, n):
        loc     = i-1
        newItem = A[i]
        while loc >= 0 and newItem < A[loc]:
            A[loc+1]=A[loc]
            loc-=1
        A[loc+1]=newItem
        
#고급정렬알고리즘
#4. mergeSort    (병합정렬)
#5. quickSort    (퀵정렬)
#6. heapSort    (힙정렬)

def merge(A,p,q,r):
    i, j, t = p, q+1, 1
    temp=[]
    while i <= q and j <= r:
        if A[i] <= A[j] :
            temp.append(A[i])
            i+=1
        else:
            temp.append(A[j])
            j+=1
    while i <= q:
        temp.append(A[i])
        i+=1
    while j <= r:
        temp.append(A[j])
        j+=1
    i=p 
    t=0
    while i <= r:
        A[i]=temp[t] 
        i+=1
        t+=1

def mergeSort(A, p, r):
    if p < r :        
        q = int((p+r)/2)
        mergeSort(A, p, q)
        mergeSort(A, q+1,r)
        merge(A,p,q,r)
        
#고급정렬알고리즘
#5. quickSort    (퀵정렬)
#   A[p,...,r]을 정렬
def partition(A,p,r):
    x = A[r]
    i = p-1
    for j in range(p, r):  # p <= j <= r-1
        if __name__ == "__main__": print(j, r)
        if A[j] <= x: 
            i+=1
            A[i], A[j] = A[j], A[i] 
    i+=1
    A[i], A[r] = A[r], A[i] 
    return i

def quickSort(A,p,r):
    if p < r:
        q = partition(A, p, r)
        #print("q is %d"%q, A)
        quickSort(A, p, q-1)
        quickSort(A, q+1, r)

#고급정렬알고리즘
#6. heapSort    (힙정렬) 
def heapify(A, k, n): #To make a heap for a subtree which its subroot is A[k]
    leftChild   = 2*k 
    rightChild  = 2*k+1
    if rightChild <= n:
        if A[leftChild] < A[rightChild]:
            smaller = leftChild 
        else:
            smaller = rightChild 
    elif leftChild <= n:
        smaller = leftChild 
    else:
        return
    if A[smaller] < A[k]:
        A[k], A[smaller] = A[smaller], A[k]
        heapify(A, smaller, n)

def buildHeap(A, n):
    last = int(n/2)
    for i in range(last, -1, -1):  # n/2 >= i > 0
        heapify(A, i, n)
#        print("i is %d"%i, A)
        
def heapSort(A, n):
    buildHeap(A, n)
    for i in range(n, 0, -1):
        A[0], A[i] = A[i], A[0]
        heapify(A, 0, i-1)        
#        print(A)

#특수정렬
#7. radixSort (기수정렬)
from math import log
def radixSort_base16(A,n):
    base=16 #16진수 기준    
    
    digit = int(log(max(A), base) + 1)
    #print(digit)
    mask=0xF
    rightSift=0;    
       
    for x in range(0,digit):
        list = []
        for y in range(0, base-1):
            list.append([])        
        #for y in range(0, base-1):
        #    print(list[y])
        for i in range(0, n+1):
            y = A[i] & mask
        #    print("%d digit,i is %d"%(x,i), hex(A[i]),A[i], "is appended in list[%d]"%y)            
            y = y >> rightSift
            list[y].append(A[i])
        #   for y in range(0, base-1):
        #        print(y, list[y])        
        i=0
        for y in range(0, base-1):
            for k in range(0, list[y].__len__() ):                
                A[i]=list[y][k]
                i+=1
        rightSift +=4
        mask = mask << 4       

#특수정렬
#8. countSort (계수정렬): 0 보다 크거나 같은 양의 정수
def countSort(A, B, n):    
    
    for i in range(0, A.__len__()):
        B.append(0)
    
    k=max(A)
    C=[]
    for i in range(0, k+1):
        C.append(0)    
    
    for i in range(0, n+1):
        C[ A[i] ] +=1
        
    for i in range(1, k+1):
        C[i] += C[i-1]
            
    for i in range(0, n+1):        
        B[ C[ A[i]]-1 ] =A[i] # C[ A[i]]-1  : index가 0부터 시작하므로
        C[ A[i]] -=1
        print(A)
        print(B)

# 모듈 Test
if __name__ =='__main__':
    #A=[3,2,4,9,2,7,4,4,8]
    #A=[0x123,0x2154,0x222,0x4,0x283,0x1560,0x1061,0x2150,0x37]
    A=[3,4,2,39,29,33,31, 22, 11, 16]
    B=[]
    n=A.__len__()    
    firstIndex=0
    lastIndex=n-1
    print(A)
    #selectionSort(A,n)
    #bubbleSort(A,n)
    #insertionSort(A,n)
    #mergeSort(A,firstIndex,lastIndex)
    #quickSort(A,firstIndex,lastIndex)
    #buildHeap(A, lastIndex)
    #heapSort(A,lastIndex)
    #radixSort_base16(A,lastIndex)   
    countSort(A,B,lastIndex) 
    #print(A) 
    print(B)


            
        
