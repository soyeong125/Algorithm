import sys
from collections import deque
from xml.dom.minidom import Childless
sys.stdin = open("input.txt", 'r')


if __name__ == "__main__":
    n,m = map(int,sys.stdin.readline().split())
    cheese = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
    cnt = 0
    q = deque()
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    visited = [[0]*m for _ in range(n)]
    
    for i in range(n):
        for j in range(m):
            if cheese[i][j] == 1:
                q.append([i,j])
                tmp_list = []
                visited[i][j] = 1
                while q:
                    x,y = q.popleft()            
                    air_cnt = 0
                    for k in range(4):
                        xx = x + dx[k]
                        yy = y + dy[k]
                        if 0<= xx < n and 0 <= yy < m and not visited[xx][yy]:
                            if cheese[xx][yy] == 0 :
                                air_cnt +=1
                            elif cheese[xx][yy] == 1:
                                q.append([xx,yy])
                                visited[xx][yy] = 1
                    if air_cnt >= 2:
                        cheese[x][y] = -1
                        tmp_list.append([x,y])
                visited = [[0]*m for _ in range(n)]     
                while tmp_list:
                    s,w = tmp_list.pop()
                    cheese[s][w]=0
                cnt +=1
    print(cnt)
                        


 

