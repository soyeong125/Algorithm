from collections import deque
def bfs(p):
        dx = [1,-1,0,0]
        dy = [0,0,1,-1]
        visited = [[0] * 5 for _ in range(5)]
        for i in range(5):
            for j in range(5):
                if p[i][j] == 'P':
                    q = deque()
                    q.append([i,j,0])
                    
                    visited[i][j] = 1
                    while q:
                        x,y,d = q.popleft()
                        if d > 2:
                            continue
                        for k in range(4):
                            xx = x + dx[k]
                            yy = y + dy[k]
                            if 0<=xx<5 and 0<=yy<5 and not visited[xx][yy]:
                                if p[xx][yy] == 'O':
                                    q.append([xx,yy,d+1])
                                    visited[xx][yy] = 1
                                if p[xx][yy] == 'P' and d <= 1:
                                    return 0
        return 1



def solution(places):
        answer = []
        for i in places:
            answer.append(bfs(i))
        return answer