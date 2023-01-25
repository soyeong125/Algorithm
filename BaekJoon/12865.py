import sys
sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline


if __name__ == "__main__":  
    n,k = map(int,input().split())
    v = [0]*101
    w = [0]*101
    for i in range(1,n+1):
        w[i],v[i] = map(int,input().split())
    dp = [0] * (100001)

    for i in range(1,n+1):
        for j in range(k,0,-1):
            if w[i] <= j:
                dp[j] = max(dp[j],dp[j-w[i]]+v[i])
    print(dp[k])  

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
    