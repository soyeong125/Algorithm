if __name__ == "__main__":
    n,m = map(int,input().split())
    miro = [list(map(int,input().split())) for _ in range(n)]
    memo = [[0] * (m+1) for _ in range(n+1)]

    for i in range(n):
        for j in range(m):
            memo[i+1][j+1] = max(memo[i][j], memo[i+1][j], memo[i][j+1]) + miro[i][j]
    print(memo[n][m])