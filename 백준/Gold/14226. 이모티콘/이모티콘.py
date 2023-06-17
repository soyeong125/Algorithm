import sys
from collections import deque
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    dp = [[-1] * (n+1) for _ in range(n+1)]
    dp[1][0] = 0
    q = deque()
    q.append([1,0])

    while q:
        s,c = q.popleft()
        if s > 0 and dp[s][s] == -1:
            q.append([s,s])
            dp[s][s] = dp[s][c] + 1
        if s+c <= n and dp[s+c][c] == -1:
            q.append([s+c,c])
            dp[s+c][c] = dp[s][c] + 1
        if s-1 >= 0 and dp[s-1][c] == -1:
            q.append([s-1,c])
            dp[s-1][c] = dp[s][c] + 1

    
    res = 1000000
    for i in dp[n]:
        if i != -1 and res > i:
            res = i
    print(res)
    