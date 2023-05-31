import sys
from collections import deque
input = sys.stdin.readline

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n,m,b = map(int,input().split())
        arr = [[-1] * m for _ in range(n)]
        q = deque()
        for _ in range(b):
            x,y = map(int,input().split())
            arr[x][y] = 0
        dx = [1,-1,0,0]
        dy = [0,0,1,-1]
        cnt = 0
        for i in range(n):
            for j in range(m):
                if arr[i][j] == 0:
                    cnt +=1
                    q.append([i,j])
                    while q:
                        x,y = q.popleft()
                        for k in range(4):
                            xx = x + dx[k]
                            yy = y + dy[k]
                            if 0<=xx<n and 0<=yy<m and arr[xx][yy] == 0:
                                arr[xx][yy] = -1
                                q.append([xx,yy])
                    
        print(cnt)