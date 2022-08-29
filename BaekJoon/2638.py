import sys
from collections import deque
sys.stdin = open("input.txt", 'r')
sys.stdin = open("input.txt", 'r')

dx = [1,-1,0,0]
dy = [0,0,1,-1]
def bfs():
    q = deque()
    q.append([0,0])
    visited[0][0]=1
    while q:
        x,y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0<= nx < n and 0<= ny < m and visited[nx][ny] == 0:
                if ch[nx][ny] >= 1:
                    ch[nx][ny]+=1
                else:
                    q.append([nx,ny])
                    visited[nx][ny]=1




if __name__ == "__main__":
    n,m = map(int,input().split())
    ch = [list(map(int,input().split())) for _ in range(n)]
    time = 0
    
    while 1:
        flag = 0
        visited = [[0]*m for _ in range(n)]
        #bfs 돌리기
        bfs()
        #3인거 다 0으로 변경하기 시간 +=1
        for i in range(n):
            for j in range(m):
                if ch[i][j] >= 3:
                    ch[i][j] = 0
                    flag = 1
                elif ch[i][j] == 2:
                    ch[i][j] = 1
                    
        #변경된 부분 있으면 계속
        if flag == 0 :
            break
        else:
            time +=1

        #변경된 부분 없으면 while 나가기
        #시간 출력
    print(time)
#치즈를 기준으로 탐색을 하면 가장자리 기준점이 없어진다
#공기를 기준으로 탐색을 해야 된다 가장자리를 찾을 수 있다.