import sys
input = sys.stdin.readline

if __name__ == "__main__":
    slist = [input().rstrip() for _ in range(3)]
    n = len(slist[0])
    m = len(slist[1])
    k = len(slist[2])

    dp = [[[0] * (m + 1) for _ in range(n + 1)] for _ in range(k + 1)]

    for i in range(1,n+1):
        for j in range(1,m+1):
            for h in range(1,k+1):
                if slist[0][i-1] == slist[1][j-1] == slist[2][h-1]:
                    dp[h][i][j] = dp[h-1][i-1][j-1] + 1
                else:
                    dp[h][i][j] = max(dp[h-1][i][j],dp[h][i-1][j],dp[h][i][j-1])

    print(dp[k][n][m])