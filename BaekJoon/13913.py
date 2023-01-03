import sys
sys.stdin = open("input.txt", 'r')
from collections import deque
input = sys.stdin.readline
if __name__ == "__main__":
    n, k = map(int, input().split())
    visited = [-1] * 100001
    idx = [0] * 100001
    visited[n] = 0
    q = deque()
    q.append(n)

    def check(k):
        res = [k]
        i = k
        for _ in range(visited[k]):
            res .append(idx[i])
            i = idx[i]
        print(' '.join(map(str,res[::-1])))


    while q:
        x = q.popleft()
        if x == k:
            print(visited[k])
            check(x)
            break
        for i in [x-1,x+1,x*2]:
            if 0 <= i < 100001:
                if visited[i] == -1:
                    visited[i] = visited[x] + 1
                    q.append(i)
                    idx[i] = x