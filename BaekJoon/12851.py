import sys
from collections import deque
sys.stdin = open("input.txt", 'r')
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

if __name__ == "__main__":  
    n,k = map(int,input().split())
    res = 0
    q = deque()
    visited = [[-1,0] for _ in range(100001)] #도달하는데 걸리는 시간, 경우의 수
    
    def bfs(val):
        q.append(val)
        visited[val][0] = 0
        visited[val][1] = 1

        while q:
            v = q.popleft()
            for i in [v-1,v+1,v*2]:
                if 0 <= i <= 100000:
                    if visited[i][0] == -1: #한번도 방문 안했으면
                        visited[i][0] = visited[v][0] + 1
                        visited[i][1] = visited[v][1]
                        q.append(i)
                    elif visited[i][0] == visited[v][0] + 1:
                        visited[i][1] += visited[v][1]
    bfs(n)
    print(visited[k][0])
    print(visited[k][1])
