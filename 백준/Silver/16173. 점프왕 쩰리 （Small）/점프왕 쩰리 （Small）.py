import sys
from collections import deque
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    jelly = [list(map(int,input().split())) for _ in range(n)]
    visited = [[0] * n for _ in range(n)]

    dx = [1,0]
    dy = [0,1]
    q = deque()
    q.append([0,0])
    visited[0][0] = 1
    res = False

    while q:
        x,y = q.popleft()
        if x==(n-1) and y==(n-1):
            res = True
            break
        for k in range(2):
            xx = x + (dx[k]*jelly[x][y])
            yy = y + (dy[k]*jelly[x][y])
            if 0<=xx<n and 0<=yy<n and not visited[xx][yy]:
                q.append([xx,yy])
                visited[xx][yy] = 1
    print("HaruHaru" if res else "Hing")