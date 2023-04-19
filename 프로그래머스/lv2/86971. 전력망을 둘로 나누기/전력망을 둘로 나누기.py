from collections import deque
import math

def solution(n, wires):
    answer = 101
    wires.sort()
    for i in range(n-1):
        tree = [[] for _ in range(n + 1)]
        for j in range(n-1): # 트리 만들기
            if i == j : # 간선 하나 자르기
                continue
            node1 = wires[j][0]
            node2 = wires[j][1]
            tree[node1].append(node2)
            tree[node2].append(node1)
        visited = [False for _ in range(n+1)]
        res = [0 for _ in range(n+1)]
        q = deque()
        q.append([wires[i][0],1]) #자른 간선을 기준으로 체크
        q.append([wires[i][1],2]) #자른 간선을 기준으로 체크
        visited[wires[i][0]] = True # 시작 노드 방문 체크
        visited[wires[i][1]] = True # 시작 노드 방문 체크
        res[wires[i][0]] = 1
        res[wires[i][1]] = 2

        while q:
            node,idx = q.popleft()

            for next_node in tree[node]:
                if not visited[next_node]:
                    visited[next_node] = True
                    res[next_node] = idx
                    q.append([next_node,idx])
        ans1,ans2 = 0 , 0
        ans1 = res.count(1)
        ans2 = res.count(2)
        answer = min(answer,abs(ans1-ans2))

    return answer