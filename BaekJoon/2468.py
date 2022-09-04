import sys
from collections import deque
sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline


if __name__ == "__main__":
    n = int(input())
    area = [list(map(int,input().split())) for _ in range(n)]
    result = 1

    def dfs(x,y,r):
        dx = [1,-1,0,0]
        dy = [0,0,1,-1]
        for k in range(4):
            xx = dx[k] + x
            yy = dy[k] + y
            if 0<=xx<n and 0<=yy<n and area[xx][yy] > r and not visited[xx][yy]:
                visited[xx][yy] = 1
                dfs(xx,yy,r)



    for r in range(max(max(area))):
        visited = [[0]*n for _ in range(n)]
        count = 0
        for i in range(n):
            for j in range(n):
                if area[i][j] > r and not visited[i][j]:
                    visited[i][j] = 1
                    count +=1
                    dfs(i,j,r)
        result = max(result,count)

    print(result)

                


    
    

