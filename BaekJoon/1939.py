import sys
sys.stdin = open("input.txt", 'r')
from collections import deque
input = sys.stdin.readline


if __name__ == "__main__": 
    n,m = map(int,input().split())
    world = [[0] * n for _ in range(n)]
    adjust_list = [[] for _ in range(n+1)]
    for _ in range(m):
        s,e,v = map(int,input().split())
        adjust_list[s].append([e,v])
        adjust_list[e].append([s,v])
    v1,v2 = map(int,input().split())
    result = 0

    def bfs():
        q = deque()
        q.append(v1)
        visited = [False] * (n+1)
        visited[v1] = True

        while q:
            cur = q.popleft()
            for e,w in adjust_list[cur]:
                if not visited[e]:
                    visited[e] = True
                    q.append(e)
                    print(e)
        return True if visited[v2] else False

    if bfs():
        print("갈 수 있습니다.")
    else:
        print("갈 수 없습니다.") 



