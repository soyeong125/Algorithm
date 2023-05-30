import sys
from collections import deque
input = sys.stdin.readline

if __name__ == "__main__":
    n,k = map(int,input().split())
    check = [-1] * 100001

    q = deque()
    q.append(n)
    check[n] = 0

    while q:
        cur = q.popleft()
        for i in (cur-1,cur+1,cur*2):
            if 0 <= i <= 100000 and check[i] == -1:
                check[i] = check[cur] + 1
                q.append(i)

    print(check[k])