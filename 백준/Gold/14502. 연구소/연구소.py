import sys
from collections import deque
import copy

input = sys.stdin.readline

if __name__ == "__main__":
    n,m = list(map(int,input().split()))
    arr = [list(map(int,input().split())) for _ in range(n)] # n 세로, m 가로
    res = 0

    def checksafe():
        global res
        q = deque()
        dx = [1,-1,0,0]
        dy = [0,0,1,-1]
        tmparr = copy.deepcopy(arr)

        for i in range(n):
            for j in range(m):
                if tmparr[i][j] == 2:
                    q.append([i,j])
        while q:
            x,y = q.popleft()
            for k in range(4):
                xx = x + dx[k]
                yy = y + dy[k]
                if 0<=xx<n and 0<=yy<m and tmparr[xx][yy] == 0:
                    tmparr[xx][yy] = 2
                    q.append([xx,yy])
        tmpcnt = 0
        for i in range(n):
            for j in range(m):
                if tmparr[i][j] == 0 :
                    tmpcnt +=1
        res = max(res,tmpcnt)


    def dfs(l):
        if l == 3:
            checksafe()
            return
        for i in range(n):
            for j in range(m):
                if arr[i][j] == 0 :
                    arr[i][j] = 1
                    dfs(l+1)
                    arr[i][j] = 0
    dfs(0)
    print(res)
                