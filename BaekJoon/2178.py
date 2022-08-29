import sys
import math
from collections import deque
sys.stdin = open("input.txt", 'r')
#input = sys.stdin.readline
if __name__ == "__main__":
    n,m = map(int,input().split())
    graph = [list(map(int,input())) for _ in range(n)]
    visited = [[0] * m for _ in range(n)]
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    q = deque()
    q.append([0, 0, 1])
    visited[0][0] = 1

    while q:
        x, y, c = q.popleft()
        if x == (n-1) and y == (m-1):
            print(c)
            break
        for k in range(4):
            xx = x + dx[k]
            yy = y + dy[k]
            if 0 <= xx < n and 0<=yy<m and graph[xx][yy] and not visited[xx][yy]:
                    q.append([xx, yy, c+1])
                    visited[xx][yy] = 1



