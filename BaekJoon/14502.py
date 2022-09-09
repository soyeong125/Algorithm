import sys
sys.stdin = open("input.txt", 'r')
from collections import deque
import copy
input = sys.stdin.readline
sys.setrecursionlimit(100000)
#dfs
if __name__ == "__main__":
    n,m = list(map(int,input().split()))
    area = [list(map(int,input().split())) for _ in range(n)]
    
    def virus():
        dx = [1,-1,0,0]
        dy = [0,0,1,-1]
        tmp_area = copy.deepcopy(area)
        
        q = deque()

        for i in range(n):
            for j in range(m):
                if tmp_area[i][j] == 2:
                    q.append([i,j])
        while q:
            x,y = q.popleft()
            for k in range(4):
                xx = x + dx[k]
                yy = y + dy[k]
                if 0<=xx<n and 0<=yy<m and tmp_area[xx][yy]==0:
                      q.append([xx,yy])
                      tmp_area[xx][yy] = 2
        global result
        cnt = 0
        for i in range(n):
            cnt += tmp_area[i].count(0)
        result = max(cnt,result)


    def bfs(l):
        if l == 3:
            virus()
            return 
        
        for i in range(n):
            for j in range(m):
                if area[i][j]==0:
                    area[i][j] = 1
                    bfs(l+1)
                    area[i][j] = 0
    
    result = 0
    bfs(0)                
    print(result)
                




    