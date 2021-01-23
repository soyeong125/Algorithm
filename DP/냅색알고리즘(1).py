import sys
from collections import deque
#sys.stdin=open("input.txt","rt")

n=int(input())
a=list(map(int,input().split()))
m=int(input())
res=[0]*(m+1)

for i in range(n):
    res[a[i]]=1
    for j in range(i,m+1):
        if res[j]>0:
           res[j]=min(res[j-a[i]]+res[a[i]],res[j])
        else:
           res[j]=res[j-a[i]]+res[a[i]]
print(res[m])





