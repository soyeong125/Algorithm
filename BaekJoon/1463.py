import sys
sys.stdin = open("input.txt", 'r')
from collections import deque
import copy
input = sys.stdin.readline
sys.setrecursionlimit(100000)

if __name__ == "__main__":  
    n, k = map(int,input().split())
    c = [int(input()) for _ in range(n)]
    dp = [0 for _ in range(k+1)]
    dp[0] = 1

    for i in c:
        for j in range(i,k+1):
                dp[j] += dp[j-i]
    print(dp[k])

