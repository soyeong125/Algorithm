import sys
import heapq
sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline
INF = sys.maxsize

if __name__ == "__main__":
    v,e = map(int,input().split())
    k = int(input())
    graph = [[] for _ in range(v+1)]
    for _ in range(e):
        s,e,w = map(int,input().split())
        graph[s].append((w,e)) #가중치 목적지 노드 형식으로 저장 > 우선순위 힙 사용하기 위해서
    dp = [INF] *(v+1) #가중치 테이블
    heap = []

    def dijkstra(start):
        dp[start] = 0
        heapq.heappush(heap,(0,start))

        while heap:
            w,cur = heapq.heappop(heap)
            if dp[cur] < w:
                continue
            for ww,vv in graph[cur]:
                next_w = w + ww
                if dp[vv] > next_w:
                    dp[vv] = next_w
                    heapq.heappush(heap,(next_w ,vv))   
    dijkstra(k)
    for i in range(1,v+1):
        print("INF" if dp[i]==INF else dp[i])

    