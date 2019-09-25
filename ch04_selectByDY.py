# -*- coding: utf-8 -*-

from ch03_sortByDY import *

#1. ��ռ��� ���� �˰���
#   �������� �̿��� ���� �˰���
#   A[p,....,r]���� i��° ���� ���Ҹ� ã�´�.
def selectUsingQsort(A, p, r, i):
    if p == r :
        return A[p]
    #if __name__ =="__main__": print("partition(A,%d,%d)"%(p,r))
    q = partition(A,p,r)
    k = q-p+1
    if i<k: 
        return selectUsingQsort(A,p, q-1, i)
    elif i==k:
        return A[q] 
    else:
        return selectUsingQsort(A, q+1, r, i-k)

#최약성능    
def selectLinear(A, p, r, i):
    length = A.__len__()
    pass
    
if __name__ == "__main__":
    A=[3,4,2,4,6,1,8, 9, 3, 2, 1]
    start =0
    end = A.__len__()-1
    for i in range(1, end+2):
        print(selectUsingQsort(A, start, end, i))
    quickSort(A, start, end)
    print(A)