import sys
from collections import deque
sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline


if __name__ == "__main__":
    n,m = map(int,input().split())
    r,c,d = map(int,input().split())

    #탐색 방향 0 3 2 1
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]

    area = [list(map(int,input().split())) for _ in range(n)]
    visited = [ [0]*m for _ in range(n)]

    #현재 위치 청소
    visited[r][c] = 1
    res = 1

    while 1:
        flag = True
        #현재 위치에서 현재 방향을 기준으로 왼쪽부터 차례대로 탐색
        for i in range(4):
            nr = r + dx[(d+3)%4]
            nc = c + dy[(d+3)%4]
            d = (d+3)%4
            #청소 안했으면
            if 0<=nr<n and 0<=nc<m and area[nr][nc]==0 and visited[nr][nc]==0:
                #청소하고 전진하고 방향 바꾸고
                visited[nr][nc]=1
                res+=1
                r = nr
                c = nc
                #하나라도 청소했으면 후진 체크 안해도됨
                flag = False
                #청소하면 탐색 종료
                break
        #네 방향이 모두 청소가 되있는 경우엔        
        if flag:
            #후진했는데 벽이면?
            if area[r-dx[d]][c-dy[d]] == 1: #후진 현재 방향에서 - 해주면 후진
                print(res) #종료
                break
            else: #아니면 후진
                r = r-dx[d]
                c = c-dy[d]
            


   