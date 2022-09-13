import sys
sys.stdin = open("input.txt", 'r')
from collections import deque
import copy
input = sys.stdin.readline
sys.setrecursionlimit(100000)

if __name__ == "__main__":  
    n, k = map(int,input().split())
    c = [int(input()) for _ in range(n)]
    dp = [ 10001 ] * (k+1)
    dp[0] = 0
    
    for i in c:
        for j in range(i,k+1):
            dp[j] = min(dp[j],dp[j-i]+1)
    if dp[k] == 10001:
        print(-1)
    else:
        print(dp[k])