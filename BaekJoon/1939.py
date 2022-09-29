import sys
sys.stdin = open("input.txt", 'r')
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

if __name__ == "__main__": 
    n,m = map(int,input().split())
    adjust_list = [[] for _ in range(n+1)]
    for _ in range(m):
        s,e,v = map(int,input().split())
        adjust_list[s].append([e,v])
        adjust_list[e].append([s,v])
    v1,v2 = map(int,input().split())

    def bfs(c):
        q = deque()
        q.append(v1)
        visited = [False] * (n+1)
        visited[v1] = True

        while q:
            cur = q.popleft()
            if cur == v2:
                return True
            for e,w in adjust_list[cur]:
                if not visited[e] and w >= c:
                    visited[e] = True
                    q.append(e)

        return False

    def dfs(start,c):
        if start == v2:
            return True
        for y,w in adjust_list[start]:
            if not visited[y] and w >= c:
                visited[y] = True
                if dfs(y,c):
                    return True 
        return False

    
    l,r = 1,1000000000 #l값을 0으로 해서 탐색하면 메모리 초과
    ans = 0
    while l <= r:
        visited = [False] * (n+1)
        visited[v1] = True
        mid = (l+r)//2
        if dfs(v1,mid):
            l = mid + 1
            ans = mid
        else:
            r = mid -1
    print(ans)





