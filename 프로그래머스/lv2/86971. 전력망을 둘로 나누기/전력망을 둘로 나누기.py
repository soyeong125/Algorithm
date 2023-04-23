def dfs(tree,visited,connected,v):
    visited[v] = True
    cnt = 1

    for next_n in tree[v]:
        if not visited[next_n] and connected[v][next_n]: #방문하지 않았고 연결되어있다면
            cnt += dfs(tree,visited,connected,next_n)

    return cnt

def solution(n, wires):
    answer = float('inf')
    tree = [[] for _ in range(n + 1)]
    for n1,n2 in wires:
        tree[n1].append(n2)
        tree[n2].append(n1)
    connected = [[True] * (n+1) for _ in range(n+1)]

    for n1,n2 in wires:
        visited = [False for _ in range(n + 1)]  # 방문한 노드 체크 할 리스트
        visited[n1] = True
        visited[n2] = True
        ans = dfs(tree,visited,connected,n1)
        connected[n1][n2] = True

        answer = min(answer, abs(ans - (n-ans)))

    return answer