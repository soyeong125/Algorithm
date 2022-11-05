import sys
from collections import deque
sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline
if __name__ == "__main__":
    n, k = map(int, input().split())
    idx = [0] * 100001
    q = deque()
    q.append([n,0])

    def check(k,cnt):
        res = [k]
        i = k
        for _ in range(cnt):
            res .append(idx[i])
            i = idx[i]
        print(' '.join(map(str,res[::-1])))


    while q:
        x,cnt = q.popleft()
        if x == k:
            print(cnt)
            check(x,cnt)
            break
        for i in [x-1,x+1,x*2]:
            if 0 <= i < 100001:
                if idx[i] == 0:
                    q.append([i,cnt+1])
                    idx[i] = x