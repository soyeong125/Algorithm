import sys
import copy
from collections import deque
from itertools import combinations
input = sys.stdin.readline

if __name__ == "__main__":
        n, m = map(int, input().split())
        arr = [list(map(int, input().split())) for _ in range(n)]
        visited = [[0] * m for _ in range(n)]
        res = 0
        walls = []
        for i in range(n):
            for j in range(m):
                if not arr[i][j]:
                    walls.append((i,j))

        def spreadVirus(tmp_arr):
            dx = [1, -1, 0, 0]
            dy = [0, 0, 1, -1]
            # 바이러스 퍼뜨리기
            q = deque()
            for i in range(n):
                for j in range(m):
                    if tmp_arr[i][j] == 2:
                        q.append([i, j])
            while q:
                x, y = q.popleft()
                for k in range(4):
                    xx = x + dx[k]
                    yy = y + dy[k]
                    if 0 <= xx < n and 0 <= yy < m and not tmp_arr[xx][yy]:
                        tmp_arr[xx][yy] = 2
                        q.append([xx, yy])

            # 안전영역구하기
            safezone = 0
            for i in range(n):
                safezone += tmp_arr[i].count(0)
            return safezone

        for w in combinations(walls,3):
            tmp_arr = copy.deepcopy(arr)
            for x,y in w:
                tmp_arr[x][y] = 1
            res = max(res, spreadVirus(tmp_arr))
        print(res)