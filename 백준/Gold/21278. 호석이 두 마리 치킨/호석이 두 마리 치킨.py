import sys
from itertools import combinations
from collections import deque
input = sys.stdin.readline
if __name__ == "__main__":
    n,m = map(int,input().split())
    tree = [[] for _ in range(n+1)]
    for _ in range(m):
        a,b = map(int,input().split())
        tree[a].append(b)
        tree[b].append(a)

    cases = list(combinations([i for i in range(1,n+1)],2))

    res = [10**6,0,0] #결과, node1, node2

    for case in cases:
        node1,node2 = case
        visited = [False for _ in range(n+1)]
        visited[node1] = True
        visited[node2] = True
        q = deque()
        q.append([node1,0])
        q.append([node2,0])
        tmp_res = 0
        while q:
            cur_node, cnt = q.popleft()
            for next_node in tree[cur_node]:
                if not visited[next_node]:
                    visited[next_node] = True
                    tmp_res += cnt + 1
                    q.append([next_node,cnt+1])

        if tmp_res * 2 < res[0]:
            res[0] = tmp_res * 2
            res[1] = node1
            res[2] = node2
    print(f"{res[1]} {res[2]} {res[0]}")