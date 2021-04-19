import sys
sys.stdin = open("input.txt","rt")
from collections import deque

def Find(parent, x):
    if parent[x] != x:
        return Find(parent, parent[x])
    return parent[x]

def Union(parent,a,b):
    a=Find(parent,a)
    b=Find(parent,b)

    if a<b:
        parent[b]=a
    else:
        parent[a]=b

if __name__ =="__main__":
    n=int(input())
    m=int(input())
    parent=[i for i in range(n+1)]

    for _ in range(m):
        x,y=map(int,input().split())
        Union(parent,x,y)
    for i in range(1,n+1):
        parent[i]=Find(parent, i)

    cnt=0
    for i in parent:
        if i==1:
            cnt+=1
    print(cnt-1)
    print(parent)