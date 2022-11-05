import sys
from collections import deque
sys.stdin = open("input.txt", 'r')
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

if __name__ == "__main__":  
    n,m = map(int,input().split())

    arr = [list(map(int,input().split())) for _ in range(n)]
    arr.insert(0,[0 for _ in range(m+1)])
    for i in range(1,n+1):
        arr[i].insert(0,0)

    dx = [-1,0,-1]
    dy = [0,-1,-1]

    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
    
    for i in range(1,n+1):
        for j in range(1,m+1):
            dp[i][j] = max(dp[i-1][j],dp[i-1][j-1],dp[i][j-1]) + arr[i][j]
    print(dp[n][m])


    
    
    






        