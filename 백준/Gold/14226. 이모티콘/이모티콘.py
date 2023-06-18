import sys
from collections import deque
if __name__ == "__main__":
    n = int(input())
    dp = [[-1] * (n+1) for _ in range(n+1)]
    dp[1][0] = 0

    q = deque()
    q.append([1,0])
    res = -1
    while q:
        view,clip = q.popleft()
        if view == n:
            res = dp[view][clip]
            break

        if view > 0 and dp[view][view] == -1:
            q.append([view,view])
            dp[view][view] = dp[view][clip] + 1
        if view + clip <= n and dp[view + clip][clip] == -1:
            q.append([view+clip,clip])
            dp[view+clip][clip] = dp[view][clip] + 1
        if view > 0 and dp[view -1][clip] == -1:
            q.append([view-1,clip])
            dp[view-1][clip] = dp[view][clip] + 1

    print(res)