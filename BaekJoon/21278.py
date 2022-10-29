import sys
from itertools import combinations
from collections import deque
sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline

if __name__ == "__main__": 
    n,m = map(int,input().split())
    tree = [[] for _ in range(n+1)]
    for _ in range(m):
        a,b = map(int,input().split())
        tree[a].append(b)
        tree[b].append(a)
    
    cases = list(combinations([i for i in range(1,n+1)],2))

    cases_score = []

    for case in cases:
        q = []
        visited = [False for _ in range(n+1)]
        node1 , node2 = case
        q.append([node1,0])
        q.append([node2,0])
        visited[node1] = True
        visited[node2] = True

        scores = [0 for _ in range(n+1)]
        while q:
            cur_node,depth = q.pop(0)
            if scores[cur_node] == 0:
                scores[cur_node] = depth * 2
            for next_node in tree[cur_node]:
                if not visited[next_node]:
                    visited[next_node] = True
                    q.append([next_node,depth + 1])
        cases_score.append([sum(scores),node1,node2])
    cases_score.sort()
    answer = f"{cases_score[0][1]} {cases_score[0][2]} {cases_score[0][0]}"
    print(answer)
    



    






    
