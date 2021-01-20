import sys
from collections import deque
#sys.stdin=open("input.txt","rt")

if __name__ =='__main__':
    n=int(input())
    d=[]
    dy=[[0]*n for _ in range(n)]
    for _ in range(n):
        d.append(list(map(int,input().split())))
    dy[0][0]=d[0][0]
    for i in range(1,n):
        dy[0][i]=dy[0][i-1]+d[0][i]
        dy[i][0]=dy[i-1][0]+d[i][0]
    for j in range(1,n):
        for k in range(1,n):
            dy[j][k]=min(dy[j-1][k],dy[j][k-1])+d[j][k]
    print(dy[n-1][n-1])
            






    

