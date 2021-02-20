from collections import deque


def bfs(network,start,visited):
    if visited[start]:
        return 0
    visited[start]=1
    q=deque([start])
    
    while q:
        v=q.pop()
        for i in network[v]:
            if visited[i]==0:
                q.append(i)                
                visited[i]=1
    return 1


def solution(n, computers):
    answer=0
    network=[[] for _ in range(n)]
    visited=[0]*n
    for i in range(n):
        for j in range(n):
            if i==j:
                continue
            elif computers[i][j]==1:
                network[i].append(j)
    for i in range(n):
        answer+=bfs(network,i,visited)
           
    return answer

if __name__=="__main__":
    #computers=[[1, 0, 1, 1, 0, 0], [0, 1, 0, 0, 1, 1], [1, 0, 1, 1, 1, 1], [1, 0, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1]]
    computers=[[1, 1, 0], [1, 1, 0], [0, 0, 1]]
    print(solution(3,computers))