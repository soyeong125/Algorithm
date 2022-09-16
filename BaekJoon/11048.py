import sys
from collections import deque
sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline

if __name__ == "__main__":  
    n,m = map(int,input().split())
    area = [list(map(int,input().split())) for _ in range(n)]
    dp = [[0] * (m+1) for _ in range(n+1)]

    for i in range(1,n+1):
        for j in range(1,m+1):
            dp[i][j] = area[i-1][j-1] + max(dp[i-1][j],dp[i-1][j-1],dp[i][j-1])
    print(dp[n][m])
    


    

    