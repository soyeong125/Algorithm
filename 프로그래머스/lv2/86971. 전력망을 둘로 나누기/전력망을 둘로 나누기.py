def dfs(node, visited, tree, child):
    visited[node] = True
    
    for next in tree[node]:
        if not visited[next]:
            child[node] += dfs(next, visited, tree, child) + child[next]
        
    return 1

def solution(n, wires):
    tree = [[] for _ in range(n+1)]
    
    for v1, v2 in wires:
        tree[v1].append(v2)
        tree[v2].append(v1)
        
    visited = [False] * (n+1)
    child = [0] * (n+1) #각자의 자식 개수를 구하기 위한 리스트
    
    dfs(1, visited, tree, child)
    result = n
    
    for c in child:
        result = min(result, abs(n-2*(c+1)))
    
    return result
