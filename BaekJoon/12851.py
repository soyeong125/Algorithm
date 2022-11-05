import sys
from collections import deque
sys.stdin = open("input.txt", 'r')
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

#최단거리와, 최단거리를 만족하는 경우의 수를 구해야함 > 결과값을 담을 자료구조 2개 있어야함
if __name__ == "__main__":  
    n,k = map(int,input().split())
    visited = [[-1,0] for _ in range(100001)] #걸리는 시간, 경우의 수 
    q = deque()
    q.append(n) #n부터 시작
    visited[n][0] = 0 #n 일 때 0시간 ~ 
    visited[n][1] = 1 # 경우의 수 1가지 부터 시작

    while q:
        x  = q.popleft()
        for i in [x-1,x+1,x*2]:
            if 0 <= i < 100001:
                if visited[i][0] == -1: #방문 안한 경우
                    visited[i][0] = visited[x][0] + 1 #이전꺼에 +1 시간
                    visited[i][1] = visited[x][1] #동일한 경우의 수
                    q.append(i)                   
                elif visited[i][0] == visited[x][0] + 1: #걸리는 시간이 이전꺼에서 현재로 온거랑 지금이랑 같은 경우
                    visited[i][1] += visited[x][1] #경우의 수 더해주기, 그리고 더이상 탐색할 필요 없음;;

    print(visited[k][0])
    print(visited[k][1])
    
    