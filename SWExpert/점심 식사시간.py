import sys
sys.stdin=open("input.txt","rt")
from collections import deque

dx = [1,-1,0,0]
dy = [0,0,1,-1]

n = int(input())
mapp = [list(map(int,input().split())) for _ in range(n)]

sx, sy = 0, 0
for i in range(n):
    for j in range(n):
        if mapp[i][j]==9:
            mapp[i][j]=0
            sx, sy = i, j
            break
size = 2
move = 0
eat = 0

while True:
    q = deque()
    q.append((sx,sy,0))
    fish = []
    flag = 1e9
    visited = [[False] * n for _ in range(n)]
    while q:
        x, y, count = q.popleft()

        if flag < count :
            break
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if nx < 0 or nx >= n  or  ny < 0 or  ny >= n:
                continue
            if mapp[nx][ny] > size or visited[nx][ny]:
                continue
            if mapp[nx][ny] != 0 and mapp[nx][ny] < size:
                fish.append((nx,ny,count + 1))
                flag = count
            visited[nx][ny] = True
            q.append((nx,ny,count + 1))
    if len(fish) > 0:
        fish.sort()
        x,y,move2 = fish[0][0] , fish[0][1], fish[0][2]
        move += move2
        eat +=1
        mapp[x][y]=0
        if size == eat:
            size +=1
            eat = 0
        sx, sy = x, y 
    else:
        break
print(move)





                
        


    






    
        
        


















    