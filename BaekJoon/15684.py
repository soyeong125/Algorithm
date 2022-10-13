import sys
from collections import deque
sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline


if __name__ == "__main__":
    n = int(input())
    location = [list(map(int,input().split())) for _ in range(n)]
      
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
  
    res = 0
    cnt = 0 

    maxval = 0
    for i in range(n):
        for j in range(n):
            maxval = max(maxval,location[i][j])

    
    for m in range(maxval):
        cnt = 0
        q = deque()
        visited = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if location[i][j] > m and visited[i][j] == 0:
                    q.append([i,j])
                    visited[i][j]=1
                    cnt+=1
                    while q:
                        x,y = q.popleft()
                        for k in range(4):
                            xx = x + dx[k]
                            yy = y + dy[k]
                            if 0<=xx<n and 0<=yy<n and location[xx][yy]>m and visited[xx][yy]==0:
                                q.append([xx,yy])
                                visited[xx][yy]=1
        res = max(res,cnt)
    print(1 if res==0 else res)


    