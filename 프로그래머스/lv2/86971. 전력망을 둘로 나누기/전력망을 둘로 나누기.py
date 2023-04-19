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

        visited = [False for _ in range(n+1)] # 방문한 노드 체크 할 리스트
        res = [0 for _ in range(n+1)] # 방문한 노드 root 노드 체크

        q = deque()
        node1 = wires[i][0]
        node2 = wires[i][1]
        q.append(node1) #자른 간선을 기준으로 체크
        q.append(node2) #자른 간선을 기준으로 체크
        visited[node1] = True # 시작 노드 방문 체크
        visited[node2] = True # 시작 노드 방문 체크
        res[node1] = node1
        res[node2] = node2

        while q:
            cur_node = q.popleft()
            for next_node in tree[cur_node]:
                if not visited[next_node]:
                    visited[next_node] = True
                    res[next_node] = res[cur_node]
                    q.append(next_node)
                    
        ans1 = res.count(node1)
        ans2 = res.count(node2)
        answer = min(answer,abs(ans1-ans2))

    return answer