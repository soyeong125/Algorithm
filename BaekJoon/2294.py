import sys
sys.stdin = open("input.txt", 'r')
from collections import deque
import copy
input = sys.stdin.readline
sys.setrecursionlimit(100000)

if __name__ == "__main__":  
    n,k = map(int,input().split())
    c = []
    for _ in range(n):
        c.append(int(input()))
    dp = [1000000] * (k+1)
    dp[0] = 0
    
    for i in c:
        for j in range(i,k+1):
            dp[j] = min(dp[j],dp[j-i]+1)
    print(dp[k])

   