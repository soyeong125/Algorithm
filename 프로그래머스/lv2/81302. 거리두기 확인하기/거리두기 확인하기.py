from collections import deque
def bfs(place):
    visited = [[0] * 5 for _ in range(5)]
    
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    
    for i in range(5):
        for j in range(5):
            if place[i][j] == 'P' and not visited[i][j]:
                visited[i][j] = 1
                q = deque()
                q.append([i,j,0])
                while q:
                    x,y,dist = q.popleft()
                    
                    if dist >= 2:
                        continue
                        
                    for k in range(4):
                        xx = x + dx[k]
                        yy = y + dy[k]
                        if 0<=xx<5 and 0<=yy<5 and not visited[xx][yy]:
                            if place[xx][yy] == 'O':
                                visited[xx][yy] = 1 
                                q.append([xx,yy,dist+1])
                            if place[xx][yy] == 'P' and dist <= 1:
                                return 0
    return 1
                     
             
def solution(places):
        answer = []
        for p in places:
            answer.append(bfs(p))
        return answer