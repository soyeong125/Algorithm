import sys
from collections import deque

input = sys.stdin.readline

if __name__ == "__main__":
    n, l, r = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    union = deque([[i,j] for i in range(n) for j in range(i%2,n,2)])
    day = 0
    dx = [1,-1,0,0]
    dy = [0, 0,1,-1]


    def bfs(i, j):
        visited[i][j] = day #방문한 날짜
        total = arr[i][j] #총 인구수 체크
        stack = [[i,j]]

        for x,y in stack:
            for k in range(4):
                xx = x + dx[k]
                yy = y + dy[k]
                if 0 <= xx < n and 0 <= yy < n and visited[xx][yy] != day:
                    if abs(arr[x][y] - arr[xx][yy]) >= l and abs(arr[x][y] - arr[xx][yy]) <= r:
                        visited[xx][yy] = day
                        stack.append([xx, yy])
                        total += arr[xx][yy]  # 연합 국가 인구수 총합
        if len(stack) > 1:
            for x, y in stack:
                arr[x][y] = int(total // len(stack))  # 인구 이동 해주기
                union.append([x,y])


    visited = [[-1] * n for _ in range(n)]
    # 국경선이 열릴 수 있는 지 체크
    while union:

        for _ in range(len(union)):
            sx, sy = union.popleft()
            if visited[sx][sy] < day:
                bfs(sx,sy)
        day += 1  # 날짜 하루 추가

    print(day-1)
