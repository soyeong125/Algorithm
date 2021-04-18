import sys
sys.stdin = open("input.txt","rt")
from collections import deque
if __name__ =="__main__":
    n,m,k=map(int,input().split())
    graph=[[0]*m for _ in range(n)]
    visited=[[0]*m for _ in range(n)]
    for _ in range(k):
        x,y=map(int,input().split())
        graph[x-1][y-1]=1
    q=deque()
    dx=[0,0,1,-1]
    dy=[1,-1,0,0]
    maxx=-2167000000
    for i in range(n):
        for j in range(m):
            if graph[i][j]==1 and visited[i][j]==0:
                visited[i][j]=1
                q.append((i,j))
                cnt=1
                while q:
                    x,y = q.popleft()
                    for k in range(4):
                        xx=x+dx[k]
                        yy=y+dy[k]
                        if 0<=xx<n and 0<=yy<m:
                            if graph[xx][yy]==1 and visited[xx][yy]==0:
                                visited[xx][yy]=1
                                q.append((xx,yy))
                                cnt+=1
                if maxx<cnt:
                    maxx=cnt
    print(maxx)


