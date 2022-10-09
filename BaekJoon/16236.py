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

   #상어 위치 저장 > 변수로 저장하기 (배열 쓰지 말기 무 조 건 간단하게가 포인트)
   sx,sy = 0,0
   #현재 상어 위치 찾기
   for i in range(n):
        for j in range(n):
            if sea[i][j] == 9:
                sx = i
                sy = j
                sea[i][j] = 0 #상어 위치 0 으로 리셋 해주기
                break
   
   size = 2
   move = 0 #상어 총 이동 전역변수로 하기
   eat = 0 #먹는 물고기 누적

   #상어 여행 시작
   while 1:      
        q= deque()
        q.append([sx,sy,0])
        tmp = [] #먹을 수 있는 물고기 저장 배열
        visited = [[0] * n for _ in range(n)] #바다 탐색 
        #먹을 수 있는 물고기 탐색
        while q:
            x,y,m = q.popleft()
            visited[x][y] = 1   
            for k in range(4):
                xx = x + dx[k]
                yy = y + dy[k]
                if 0<=xx<n and 0<=yy<n and sea[xx][yy] <= size and visited[xx][yy] == 0:
                    q.append([xx,yy,m+1]) #m+1은 그 전 칸에서 한칸 이동한거임
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
            sea[x][y] = 0 #물고기 먹은 곳 0 초기화 9로 할 필요 없음
            if eat == size:
                size += 1
                eat = 0 #상어 먹은 물고기 수 초기화 해줘야함 n의 크기일 때 n개를 먹어야 사이즈가 커진다 (문제 잘 읽기)
            #새로운 상어 위치로 다시 체크
            sx , sy = x, y #상어 위치 초기화

   print(move)
                    




