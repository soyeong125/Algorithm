import sys
from itertools import combinations

input = sys.stdin.readline

if __name__ == "__main__":

    n,m = map(int,input().split())
    INF = int(1e9)
    res = [[INF] * (n + 1) for _ in range(n + 1)]

    for _ in range(m):
        a,b = map(int,input().split())
        res[a][b] = 1
        res[b][a] = 1

    for i in range(1,n+1): #자기 자신은 0으로 초기화
        for j in range(1,n+1):
            if i == j:
                res[i][j] = 0

    #1. 모든 정점에서 모든 정점으로 가는 최소값 구하기 (플로이드 와샬)
    for k in range(1,n+1): # 경유 노드
        for i in range(1,n+1): # 출발 노드
            for j in range(1,n+1): # 도착 노드
                res[i][j] = min(res[i][j], res[i][k] + res[k][j]) #곧장 가는 값과 경유해서 가는 값 중 최소값으로 초기화

    #2. 노드 2개 정해서 가장 최소값을 찾기
    cases = list(combinations([i for i in range(1,n+1)],2))
    ans_sum = INF
    ans_node = [0,0]
    for case in cases:
        node1,node2 = case
        tmp_sum = 0
        for i in range(1,n+1):
            if i == node1 or i == node2:
                continue
            tmp_sum += min(res[node1][i], res[node2][i])

        if ans_sum > tmp_sum * 2:
            ans_sum = tmp_sum * 2
            ans_node[0] = node1
            ans_node[1] = node2

    print(ans_node[0],ans_node[1],ans_sum)









