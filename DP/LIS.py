import sys
from collections import deque
#sys.stdin=open("input.txt","rt")



if __name__ =='__main__':
    n=int(input())
    a=list(map(int,input().split()))
    res=[0]*(n)
    res[0]=1
    for i in range(1,n):
        max=0
        for j in range(i):
            if res[j]>max and a[j]<a[i]:
                     max=res[j]
        res[i]=max+1

    max=0
    for k in res:
        if k>max:
            max=k
    print(max)



    

