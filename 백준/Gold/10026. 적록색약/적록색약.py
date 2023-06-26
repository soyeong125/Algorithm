import sys
from collections import deque
if __name__ == "__main__":
    if __name__ == "__main__":
        n = int(input())
        arr = [list(input().strip()) for _ in range(n)]

        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]

        def bfs(tmp,is_normal):
            cnt = 0
            visited = [[0] * n for _ in range(n)]
            for i in range(n):
                for j in range(n):
                    if not visited[i][j]:
                        cnt += 1
                        visited[i][j] = 1
                        q = deque()
                        q.append([i, j])
                        while q:
                            x, y = q.popleft()
                            for k in range(4):
                                xx = x + dx[k]
                                yy = y + dy[k]
                                if 0 <= xx < n and 0 <= yy < n and not visited[xx][yy]:
                                    if is_normal:
                                        if tmp[x][y] == tmp[xx][yy]:
                                            q.append([xx, yy])
                                            visited[xx][yy] = 1
                                    else:
                                        if (tmp[x][y] == 'R' or tmp[x][y] == 'G') and (tmp[xx][yy] == 'R' or tmp[xx][yy] == 'G'):
                                            q.append([xx,yy])
                                            visited[xx][yy] = 1
                                        elif tmp[x][y] == tmp[xx][yy]:
                                            q.append([xx,yy])
                                            visited[xx][yy] = 1

            return cnt


        print(bfs(arr,True))
        print(bfs(arr,False))