import sys
import copy
from collections import deque
from itertools import combinations
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    area = [list(map(int,input().split())) for _ in range(n)]
    combi = [(r,c) for r in range(1,n-1) for c in range(1,n-1)]
    res = 10**8

    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    def check(c):
        global res
        cost = 0
        visited = [[0] * n for _ in range(n)]
        for x,y in c:
            visited[x][y] = 1
            cost += area[x][y]
            for k in range(4):
                xx = x + dx[k]
                yy = y + dy[k]
                if not visited[xx][yy]:
                    cost += area[xx][yy]
                    visited[xx][yy] = 1
                else:
                    return
        res = min(res,cost)

    for c in combinations(combi,3):
        check(c)
    print(res)