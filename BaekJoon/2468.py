from copy import deepcopy
import sys
from collections import deque
sys.setrecursionlimit(100000)
sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline


if __name__ == "__main__":
   n = int(input())
   sea = [list(map(int,input().split())) for _ in range(n)]
   
   dx = [1,0,-1,0]
   dy = [0,1,0,-1]
   sx,sy = 0,0
   #현재 상어 위치 찾기
   for i in range(n):
        for j in range(n):
            if sea[i][j] == 9:
                sx = i
                sy = j
                sea[i][j] = 0
                break
   
   size = 2
   move = 0
   eat = 0 #먹는 물고기 누적
   while 1:      
        q= deque()
        q.append([sx,sy,0])
        tmp = [] #먹을 수 있는 물고기 저장 배열
        visited = [[0] * n for _ in range(n)] #바다 탐색 
        while q:
            x,y,m = q.popleft()
            # visited[x][y] = 1   
            for k in range(4):
                xx = x + dx[k]
                yy = y + dy[k]
                if 0<=xx<n and 0<=yy<n and sea[xx][yy] <= size and visited[xx][yy] == 0:
                    q.append([xx,yy,m+1])
                    visited[xx][yy] = 1
                    if 0 < sea[xx][yy] < size: #먹을 수 있는 물고기 수
                        tmp.append([xx,yy,m+1])
        #먹을 수 있는 물고기 없으면 끝 
        if len(tmp) == 0:
            break
        else:
            #먹을 수 있는 물고기 정렬 (움직임 > 위 >아래)
            tmp.sort(key = lambda x:([x[2],x[0],x[1]]))
            x,y,move2 = tmp[0][0],tmp[0][1],tmp[0][2]
            #움직임 누적
            move += move2
            #먹을 물고기 누적
            eat += 1
            sea[x][y] = 0
            if eat == size:
                size += 1
                eat = 0
            #새로운 상어 위치로 다시 체크
            sx , sy = x, y

   print(move)
                    




