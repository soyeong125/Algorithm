import sys
from collections import deque
#sys.stdin=open("input.txt","rt")


def DFS(x,y):
    if dy[x][y]>0:
        return dy[x][y]
    if x==0 and y==0:
        return d[0][0]
    else:
        if x==0:
            dy[x][y]=DFS(x,y-1)+d[x][y]
        elif y==0:
            dy[x][y]=DFS(x-1,y)+d[x][y]
        else:
             dy[x][y]=min(DFS(x-1,y),DFS(x,y-1))+d[x][y]
        return dy[x][y]


if __name__ =='__main__':
    n=int(input())
    d=[list(map(int,input().split())) for _ in range(n)]
    dy=[[0]*n for _ in range(n)]
    dy[0][0]=d[0][0]
    DFS(n-1,n-1)
    print(dy[n-1][n-1])






    

