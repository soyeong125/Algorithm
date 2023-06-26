import sys
from collections import deque

input = sys.stdin.readline

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def bfs(sy, sx):
    population = lst[sy][sx]  # 시작 나라의 인구수
    union = [(sy, sx)]  # 연합에 속한 나라의 좌표
    visit[sy][sx] = True  # 방문 여부 표시
    queue = deque([(sy, sx)])  # BFS를 위한 큐
    while queue:
        y, x = queue.popleft()
        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]
            if ny < 0 or nx < 0 or ny >= N or nx >= N:
                continue
            if visit[ny][nx]:
                continue
            diff = abs(lst[y][x] - lst[ny][nx])
            if diff < L or diff > R:
                continue
            visit[ny][nx] = True
            population += lst[ny][nx]
            union.append((ny, nx))
            queue.append((ny, nx))
    
    if len(union) > 1:
        avg = population // len(union)  # 연합의 평균 인구수
        for y, x in union:
            lst[y][x] = avg  # 연합의 인구수 갱신
    return len(union) > 1

N, L, R = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]

day = 0  # 인구 이동이 발생하는 일수
while True:
    visit = [[False] * N for _ in range(N)]  # 방문 여부 초기화
    moved = False  # 인구 이동이 발생했는지 여부
    for y in range(N):
        for x in range(N):
            if not visit[y][x]:
                if bfs(y, x):
                    moved = True
    if not moved:  # 인구 이동이 더 이상 발생하지 않으면 종료
        break
    day += 1

print(day)