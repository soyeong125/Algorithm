import sys
from collections import deque
sys.stdin = open("input.txt","rt")

    




n,m,v = map(int,input().split())
graph = [[0]*(n+1) for _ in range(n+1)]
visited_dfs =[0]*(n+1)
visited_bfs =[0]*(n+1)
   
for _ in range(m):
       x,y=map(int,input().split())
       graph[x][y]=1
       graph[y][x]=1

def DFS(v):
     print(v,end=' ')
     #if n == sum(visited_dfs):
     #   return

     for i in range(1,n+1):
             if graph[v][i] == 1 and visited_dfs[i] == 0:
                 visited_dfs[i] = 1
                 DFS(i)
def BFS(v):
    q = deque()
    q.append(v)

    while q:
        val = q.popleft()
        if visited_bfs[val]==0:
                visited_bfs[val] = 1
                print(val,end=' ')
                for i in range(1,n + 1):
                    if graph[val][i] == 1 and visited_bfs[i]==0:
                        q.append(i)

visited_dfs[v]=1
DFS(v)
print()
BFS(v)
        




