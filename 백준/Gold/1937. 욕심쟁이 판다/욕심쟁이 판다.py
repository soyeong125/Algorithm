import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

if __name__ == "__main__":  
    n = int(input())
    mm = [list(map(int,input().split())) for _ in range(n)]
    dp = [[0] * n for _ in range(n)]
    result = 0
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]

    def dfs(x,y):
        if dp[x][y] : return dp[x][y]
        dp[x][y] = 1
        for k in range(4):
            xx = x + dx[k]
            yy = y + dy[k]
            if 0<= xx < n and 0<= yy < n and mm[xx][yy] > mm[x][y]:
                dp[x][y] = max(dp[x][y],dfs(xx,yy) + 1)

        return dp[x][y]

    for i in range(n):
        for j in range(n):
            result = max(dfs(i,j),result)
    print(result)
