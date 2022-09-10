import sys
sys.stdin = open("input.txt", 'r')
from collections import deque
import copy
input = sys.stdin.readline
sys.setrecursionlimit(100000)

if __name__ == "__main__":  
    n = int(input())
    area = [list(map(int,input().split())) for _ in range(n)]
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    q = deque()
    visited = [[0] * n for _ in range(n)]
    cnt = 1
    #섬 단지별로 나누기
    for i in range(n):
        for j in range(n):       
            if area[i][j] == 1 and not visited[i][j]:
                visited[i][j] = 1
                area[i][j] = cnt
                q.append([i,j])
                while q:
                    x,y = q.popleft()
                    for k in range(4):
                        xx = x + dx[k]
                        yy = y + dy[k]
                        if 0<= xx < n and 0<= yy < n and not visited[xx][yy]:
                            if area[xx][yy] == 1:
                                visited[xx][yy] = 1
                                area[xx][yy] = cnt
                                q.append([xx,yy])
                cnt +=1
    #섬 가장자리 체크
    for i in range(n):
        for j in range(n):
            flag = False
            if area[i][j] > 0:
                for k in range(4):
                    xx = i + dx[k]
                    yy = j + dy[k]
                    if 0<=xx<n and 0<=yy<n and area[xx][yy]==0:
                        flag = True
                        break
            if flag:
                q.append([i,j,area[i][j]])
    #가장자리에서 다른 섬으로 다리를 연결했을 때 가장 적은 수 찾기
    result = 1000000
    while q:
        sx,sy,inum = q.popleft()
        bridge = deque()
        bridge.append([sx,sy,0])
        visited = [[0]*n for _ in range(n)]
        while bridge:
            x,y,c = bridge.popleft()
            for k in range(4):
                xx = x + dx[k]
                yy = y + dy[k]
                if 0 > xx or n <= xx or 0 > yy or n <= yy or area[xx][yy] == inum or visited[xx][yy]:
                    continue
                if area[xx][yy] == 0 :
                    visited[xx][yy] = 1
                    bridge.append([xx,yy,c+1])
                elif area[xx][yy] != inum:
                    result = min(result,c)
                    break
    print(result)








    


 