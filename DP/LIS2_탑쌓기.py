import sys
from collections import deque
#sys.stdin=open("input.txt","rt")



if __name__ =='__main__':
    n=int(input())
    brick=[]
    for _ in range(n):
        a,b,c=map(int,input().split())
        brick.append([a,b,c])
    brick.sort(key = lambda x : -x[0])
    res=[0]*(n)
    res[0]=brick[0][1]
    tmp=0
    for i in range(1,n):
        max=0
        for j in range(i):
            if brick[j][2]>brick[i][2] and max<res[j]:
                max=res[j]
        res[i]=max+brick[i][1]
        
    for i in res:
        if tmp<i:
            tmp=i
    print(tmp)
    






    

