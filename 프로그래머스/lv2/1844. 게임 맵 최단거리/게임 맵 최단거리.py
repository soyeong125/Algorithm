from collections import deque
def solution(maps):
    n = len(maps)
    m = len(maps[0])
    
    visited = [[0] * (m) for _ in range(n)]
    
    q = deque()
    q.append([0,0,1])
    visited[0][0] = 1
    
    dx = [1,-1,0,0]
    dy =[0,0,1,-1]
    
    while q:
        x,y,cnt = q.popleft()
        if x == (n-1) and y == (m-1):
            return cnt

        for k in range(4):
            xx = x + dx[k]
            yy = y + dy[k]
            if 0<=xx<n and 0<=yy<m and maps[xx][yy]:
                if not visited[xx][yy]:
                    visited[xx][yy] = 1
                    q.append([xx,yy,cnt+1])

    return -1