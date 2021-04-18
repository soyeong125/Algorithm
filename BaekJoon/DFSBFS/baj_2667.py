import sys
sys.stdin = open("input.txt","rt")
from collections import deque
if __name__ =="__main__":
    n = int(input())
    apt = [list(map(int,input())) for _ in range(n)]
    visited=[[0]*n for _ in range(n)]
    result=[]
    q=deque()
    dx=[1,-1,0,0]
    dy=[0,0,1,-1]
    
    for i in range(n):
        for j in range(n):
            if apt[i][j]==1 and visited[i][j]==0:
                apt_cnt=1
                q.append((i,j))
                visited[i][j]=1
                while q:
                    x,y = q.popleft()
                    for k in range(4):
                        xx=x+dx[k]
                        yy=y+dy[k]
                        if 0<=xx<n and 0<=yy<n:
                            if  apt[xx][yy]==1 and visited[xx][yy]==0:
                                apt_cnt+=1
                                visited[xx][yy]=1
                                q.append((xx,yy))
                result.append(apt_cnt)
    print(len(result))
    result.sort()
    for i in result:
        print(i)



