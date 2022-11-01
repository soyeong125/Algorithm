import sys
from collections import deque
sys.stdin = open("input.txt", 'r')
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

if __name__ == "__main__":  
    n = int(input())
    dist = [[-1] * (n+1) for _ in range(n+1)]
    q = deque()
    q.append([1,0]) #(s,c)의 현재 값
    dist[1][0] = 0 #현재 누적값 0

    while q:
        s,c = q.popleft()
        if dist[s][s] == -1:
            dist[s][s] = dist[s][c] + 1 #화면의 이모티콘을  클립보드에 복사한다
            q.append([s,s])
        if s+c <= n and dist[s+c][c] == -1: 
            dist[s+c][c] = dist[s][c] + 1 #클립보드의 이모티콘을 화면에 복사한다.
            q.append([s+c,c])
        if s-1 >= 0 and dist[s-1][c] == -1:
            dist[s-1][c] = dist[s][c] + 1
            q.append([s-1,c])
    res = 1000000
    for i in dist[n]:
        if i != -1:
            res = min(res,i)
    print(res)



        