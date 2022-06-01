import sys
from collections import deque
sys.stdin=open("input.txt","rt")

dx = [1,-1,0,0]
dy = [0,0,1,-1]

n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]

sx, sy = 0 , 0
for i in range(n):
    for j in range(n):
        if arr[i][j]==9:
            sx, sy = i, j
            arr[i][j]=0
            break
size = 2
eat = 0
move = 0
while True:
    q = deque()
    q.append([sx,sy,0])
    flag = 1e9
    visited = [[False] * n for _ in range(n)]
    fish = []
    while q:
        x,y,count = q.popleft()
        if count > flag:
            break
        for k in range(4):
            nx = dx[k] + x
            ny = dy[k] + y
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if arr[nx][ny] > size or visited[nx][ny] :
                continue
            if arr[nx][ny] < size and arr[nx][ny] != 0:
                fish.append([nx,ny,count+1])
                flag = count
            visited[nx][ny] = True
            q.append([nx,ny,count + 1])
    if len(fish) > 0 :
        fish.sort()
        x,y,move2 = fish[0][0], fish[0][1],fish[0][2]
        move += move2
        eat +=1

        if size == eat:
            size+=1
            eat = 0
        sx, sy = x, y
    else:
        break
print(move)


