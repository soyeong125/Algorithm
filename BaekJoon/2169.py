import sys
sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


if __name__ == "__main__":  
    n,m = map(int,input().split())
    mm = [list(map(int,input().split())) for _ in range(n)]
    dp = [[0]*m for _ in range(n)]
    dx = [1,0,0]
    dy = [0,1,-1]
    result = 0

    def dfs(x,y):
        if dp[x][y] : return dp[x][y]
        
        for k in range(3):
            xx = x + dx[k]
            yy = y + dy[k]
            if 0<=xx<n and 0<=yy<m:
                dp[x][y] = max(dp[x][y],dfs(xx,yy)+mm[x][y])
        return dp[x][y]
    for i in range(n):
        for j in range(m):
            result = max(dfs(i,j),result)
    print(result)
        
    