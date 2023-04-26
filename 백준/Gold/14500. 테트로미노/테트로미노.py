import sys
from itertools import combinations
input = sys.stdin.readline
if __name__ == "__main__":
    n,m = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(n)]
    answer = 0

    move = [[1,0],[-1,0],[0,1],[0,-1]] # 상,하,좌,우
    visited = [[0] * m for _ in range(n)]

    def dfs(l,x,y,tmp_sum):
        global answer
        if l == 4:
            answer = max(answer,tmp_sum)
            return
        for k in range(4):
            xx = x + move[k][0]
            yy = y + move[k][1]
            if 0 <= xx < n and 0 <= yy < m and not visited[xx][yy]:
                visited[xx][yy] = 1
                dfs(l+1,xx,yy,arr[xx][yy]+tmp_sum)
                visited[xx][yy] = 0

    def chk(x,y):
        global answer
        for ch in list(combinations([i for i in range(4)],3)):
            tmp = arr[x][y]
            for c in ch:
                xx = x + move[c][0]
                yy = y + move[c][1]
                if 0 <= xx < n and 0 <= yy < m:
                    tmp += arr[xx][yy]
                else:
                    tmp = 0
                    break
            answer = max(answer,tmp)

    for i in range(n):
        for j in range(m):
            visited[i][j] = 1
            dfs(1,i,j,arr[i][j])
            visited[i][j] = 0

            chk(i,j)
    print(answer)