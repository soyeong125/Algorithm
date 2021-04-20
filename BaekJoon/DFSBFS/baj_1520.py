#시간초과 해결:sys.setrecursionlimit(10000)  
#Top-Down 방식 (x,y)가 있을 때 (x,y)에서 (0,0)까지 가는 경로의 수
#도달하면 1을 리턴
#-1로 체크리스트 세팅: 아직 가지 않은 경우
#0 한번이라도 방문한 노드
#조건이 맞으면 DFS를 이용하여 경로를 더해준다.
#return visited[x][y]는 visited[0][0] 해서 최종 결과를 출력


import sys
sys.stdin = open("input.txt","rt")
from collections import deque
sys.setrecursionlimit(10000)
dx=[1,-1,0,0]
dy=[0,0,1,-1]
def DFS(x,y):
    if x==(m-1) and y==(n-1):
        return 1
    if visited[x][y] != -1:
        return visited[x][y]
    visited[x][y]=0
    for i in range(4):
            xx = x+dx[i]
            yy = y+dy[i]
            if 0<=xx<m and 0<=yy<n and mapp[x][y]>mapp[xx][yy]:
                        visited[x][y]+=DFS(xx,yy)
    return visited[x][y]


if __name__ == "__main__":
    m, n = map(int,input().split())
    mapp = [list(map(int,input().split())) for _ in range(m)]
    visited = [[-1]*n for _ in range(m)]
    print(DFS(0,0))

    

