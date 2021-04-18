import sys
sys.stdin = open("input.txt","rt")
from collections import deque

 
if __name__ =="__main__":
    n,m=map(int,input().split())
    grap=[list(map(int,input())) for _ in range(n)]
    ch=[[0]*m for _ in range(n)]
    q=deque()
    dx=[1,-1,0,0]
    dy=[0,0,1,-1]
    ch[0][0]=1
    q.append((0,0))
    while q:
        x,y=q.popleft()
        if x == n-1 and y== m-1:
            print(ch[x][y])
            break
        for i in range(4):
            xx = x +dx[i]
            yy = y + dy[i]
            if 0<=xx<n and 0<=yy<m:
                if ch[xx][yy]==0 and grap[xx][yy]==1:
                    ch[xx][yy]= ch[x][y]+1
                    q.append((xx,yy))

