import sys
from collections import deque
sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline

dx = [1,-1,0,0]
dy = [0,0,1,-1]
if __name__ == "__main__":
    n = int(input())
    area = [list(map(int,input().split())) for _ in range(n)]
    maxvalue = 0
    minvalue = 1000000
    result = 0
    for i in range(n):
        for j in range(n):
            maxvalue = max(maxvalue,area[i][j])
            minvalue = min(minvalue,area[i][j])

    for r in range(minvalue,maxvalue+1):
        visited = [[0]*n for _ in range(n)]
        count = 0
        q = deque()
        for i in range(n):
            for j in range(n):
                if area[i][j] > r and not visited[i][j]:
                    q.append([i,j])
                    visited[i][j] = 1
                    count +=1
                    while q:
                        x,y = q.popleft()
                        for k in range(4):
                            xx = x + dx[k]
                            yy = y + dy[k]
                            if 0<=xx<n and 0<=yy<n and not visited[xx][yy]:
                                if area[xx][yy] > r :
                                    q.append([xx,yy])
                                    visited[xx][yy] = 1
        result = max(result,count)
    print(result)

                


    
    

