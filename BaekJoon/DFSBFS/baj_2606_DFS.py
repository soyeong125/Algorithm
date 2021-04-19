import sys
sys.stdin = open("input.txt","rt")
from collections import deque

def DFS(i):
    global cnt
    for j in range(n):
        if graph[i][j]==1 and visited[j]==0:
            cnt+=1
            visited[j]=1
            DFS(j)

if __name__ =="__main__":
    n=int(input())
    m=int(input())
    graph=[[0]*n for _ in range(n)]
    for _ in range(m):
        x,y=map(int,input().split())
        graph[x-1][y-1]=1
        graph[y-1][x-1]=1
    visited=[0]*n
    cnt=0
    visited[0]=1
    DFS(0)
    print(cnt)
    
        
    

