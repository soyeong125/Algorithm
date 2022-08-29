import sys
import math
from collections import deque
sys.stdin = open("input.txt", 'r')
#input = sys.stdin.readline
if __name__ == "__main__":
    n = int(input())
    house = [list(map(int,input())) for _ in range(n)]
    visited = [[0]*n for i in range(n)]
    q = deque()
    house_list = []
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    for i in range(n):
        for j in range(n):
            if house[i][j] and not visited[i][j]:
                q.append([i,j])
                visited[i][j]=1
                tmp_cnt = 1
                while q:
                    x,y = q.popleft()                   
                    for k in range(4):
                        xx = x + dx[k]
                        yy = y + dy[k]
                        if 0 <= xx < n and 0 <= yy < n and house[xx][yy]==1 and not visited[xx][yy]:
                            q.append([xx,yy])
                            visited[xx][yy]=1
                            tmp_cnt +=1
                house_list.append(tmp_cnt)
    print(len(house_list))
    for h in sorted(house_list):print(h,end='\n')




    
