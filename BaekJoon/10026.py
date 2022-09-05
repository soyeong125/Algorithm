import sys
from collections import deque
sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline
#BFS 풀이
if __name__ == "__main__":
    n = int(input())
    area = [list(map(str,input())) for _ in range(n)]
    q = deque()
    visited = [[0] * n for _ in range(n)]
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]

    cnt1 = 0
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                visited[i][j] = 1
                q.append([i,j])
                cnt1 += 1
                while q:
                    x,y = q.popleft()
                    cur = area[x][y]
                    for k in range(4):
                        xx = x + dx[k]
                        yy = y + dy[k]
                        if 0 <= xx < n and 0 <= yy < n and not visited[xx][yy]:
                            if area[xx][yy] == cur:
                                q.append([xx,yy])
                                visited[xx][yy]=1
    cnt2 = 0
    visited = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                visited[i][j] = 1
                q.append([i,j])
                cnt2 += 1
                while q:
                    x,y = q.popleft()
                    cur = area[x][y]
                    for k in range(4):
                        xx = x + dx[k]
                        yy = y + dy[k]
                        if 0 <= xx < n and 0 <= yy < n and not visited[xx][yy]:
                            if cur == 'R' or cur == 'G':
                                if area[xx][yy] == 'R' or area[xx][yy] == 'G':
                                    q.append([xx,yy])
                                    visited[xx][yy]=1 
                            else:
                                if area[xx][yy] == cur:
                                    q.append([xx,yy])
                                    visited[xx][yy]=1
    print(cnt1,cnt2)

    




    