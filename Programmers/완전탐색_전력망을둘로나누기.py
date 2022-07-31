import math
from collections import defaultdict

def bfs(start,end,n,dic):
    visited = [False for i in range(n+1)]
    q = [start]
    visited[start] = True
    cnt = 0
    while q:
        cur = q.pop(0)
        for next in dic[cur]:
            if next == end: continue
            if visited[next]: continue
            visited[next] = True
            cnt+=1
            q.append(next)
    return cnt

def solution(n, wires):
    answer = 100000
    dic = defaultdict(set)

    #그래프를 딕셔너리에 정의
    for w in wires: 
        dic[w[0]].add(w[1])
        dic[w[1]].add(w[0])
    #그래프를 끊었을 때 최소값 찾기
    for w in wires:
        v1 = w[0]
        v2 = w[1]
        diff = abs(bfs(v1,v2,n,dic) - bfs(v2,v1,n,dic))
        answer = min(answer,diff)           
    return answer

if __name__ == "__main__" :
    # print(solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))
     print(solution(7, [[1, 2], [2, 7], [3, 7], [3, 4], [4, 5], [6, 7]]))