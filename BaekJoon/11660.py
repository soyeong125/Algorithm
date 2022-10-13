import sys
sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline


if __name__ == "__main__":  
    n, m = map(int, input().split())
    dp = [[0] * (n+1) for _ in range(n+1)]
    s = [list(map(int,input().split())) for _ in range(n)]

    #누적합 받기
    for i in range(n):
        for j in range(n):
            dp[i+1][j+1] = dp[i][j+1] + dp[i+1][j] -dp[i][j] + s[i][j]
    
    #계산
    for i in range(m):
        a,b,c,d = map(int,input().split())
        print(dp[c][d] - dp[c][b-1]-dp[a-1][d] + dp[a-1][b-1])
    
