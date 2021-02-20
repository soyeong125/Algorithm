from collections import deque


def bfs(computers,visited,start):
    visited[start]=1
    for i in range(len(computers[start])):
        if visited[i]==0 and computers[start][i]==1:
            bfs(computers,visited,i)
    return 1


def solution(n, computers):
    answer=0
    visited=[0]*n
    for i in range(n):
        if visited[i]==0:
            answer+=bfs(computers,visited,i)

           
    return answer

if __name__=="__main__":
    computers=[[1, 0, 1, 1, 0, 0], [0, 1, 0, 0, 1, 1], [1, 0, 1, 1, 1, 1], [1, 0, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1]]
    #computers=[[1, 1, 0], [1, 1, 0], [0, 0, 1]]
    print(solution(6,computers))