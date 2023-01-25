import sys
from collections import deque
sys.stdin = open("input.txt", 'r')
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

if __name__ == "__main__":  
    n,k = map(int,input().split())
    bag = [list(map(int,input().split())) for _ in range(n)]
    dp = [0] * (k+1)

    for i in range(n):
        for j in range(k,-1,-1):
            if bag[i][0] <= j:
                dp[j] = max(dp[j-bag[i][0]]+bag[i][1],dp[j])
    print(dp[k])
