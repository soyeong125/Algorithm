from pickle import FALSE
import sys
from collections import deque
sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    sea = [list(map(int,input().split())) for _ in range(n)]
    shark = 2
    q = deque()
    
    for i in range(n):
        for j in range(n):
            if sea[i][j] == 9:
                q.append([i,j])
                break
    
    dx = [1,0,-1,0]
    dy = [0,-1,0,1]
    flag = False
    while True:
        visited = [[False] * n for _ in range(n)]
        while q:
            x,y = q.popleft()
            for k in range(4):
                xx = x + dx[k]
                yy = y + dy[k]
                if 0<=xx<n and 0<=yy<n and visited[xx][yy] == False:
                    if 0 < sea[xx][yy] < shark:
                        q.append([xx,yy])
                        visited[xx][yy] = True
                        shark +=1
                    elif sea[xx][yy] == shark or sea[xx][yy]==0:
                        q.append([xx,yy])
                        visited[xx][yy] = True
        if flag == False:
            break
                    
    print(shark)



   