import sys
from collections import deque
sys.stdin = open("input.txt", 'r')
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

if __name__ == "__main__":  
    n,k = map(int,input().split())
    res = 0
    q = deque()
    visited = [-1 for _ in range(100001)] 
    
    q = deque()
    q.append([n,0])
    visited[n] = 1

    while q:
        x,cnt = q.popleft()
        if x == k:
            res = cnt
            break
        for i in [x-1,x+1,x*2]:
            if 0 <= i < 100001:
                if i == x*2:
                    if visited[i] == -1:
                        visited[i] = cnt
                        q.append([i,cnt])
                    else:
                        visited[i] = min(visited[i],cnt)




    print(res)           