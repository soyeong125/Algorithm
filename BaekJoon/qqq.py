from copy import deepcopy
import queue
import sys
from collections import deque
sys.setrecursionlimit(100000)
sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline


if __name__ == "__main__":
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(n)]
    res = 10000

    dx= [1,-1,0,0]
    dy = [0,0,1,-1]

    def bfs(x,y,nn):
        global res
        q = deque()
        q.append([x,y,0])
        visited = [[0]*n for _ in range(n)]
        while q:
            xx,yy,cnt = q.popleft()
            visited[xx][yy]=1
            for k in range(4):
                xk = xx + dx[k]
                yk = yy + dy[k]
                if 0<=xk<n and 0<=yk<n and visited[xk][yk] == 0:
                    if arr[xk][yk] > 0 and arr[xk][yk] != nn:
                        res = min(res,cnt)
                        return
                    if arr[xk][yk] == 0:
                        visited[xk][yk]=1
                        q.append([xk,yk,cnt+1])

    #섬 구역짓기
    q = deque()
    visited = [[0]*n for _ in range(n)]
    num = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 1 and visited[i][j]==0 :
                num+=1
                visited[i][j]=1
                arr[i][j]=num
                q.append([i,j])
                while q:
                    x,y = q.popleft()
                    for k in range(4):
                        xx = x + dx[k]
                        yy = y + dy[k]
                        if 0<=xx<n and 0<=yy<n and arr[xx][yy]==1 and visited[xx][yy] == 0:
                            arr[xx][yy]=num
                            visited[xx][yy]=1
                            q.append([xx,yy])

    #다리 체크하기
    for i in range(n):
        for j in range(n):
            if arr[i][j] > 0:
                q = deque()
                q.append([i,j])
                for k in range(4):
                    xx = i + dx[k]
                    yy = j + dy[k]
                    if 0<=xx<n and 0<=yy<n and arr[xx][yy]==0:
                        bfs(i,j,arr[i][j])
                        break
    print(res)




