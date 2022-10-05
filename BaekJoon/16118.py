import sys
import heapq
sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline
INF = sys.maxsize

if __name__ == "__main__":
    n,e = map(int,input().split())
    graph = [[] for _ in range(n+1)]
    for i in range(n):
        s,e,w = map(int,input().split())
        graph[s].append((e,w))
        graph[e].append((s,w))
      
    def foxDijkstra(start):
        heap = []
        dp = [INF] * (n+1)
        for vv,ww in graph[start]:
                next_w = ww
                if dp[vv] > next_w:
                    dp[vv] = next_w
                    heapq.heappush(heap,(next_w,vv))     

        while heap:
            w,cur = heapq.heappop(heap)
            if w > dp[cur]:
                continue
            for vv,ww in graph[cur]:
                next_w = ww + w
                if dp[vv] > next_w:
                    dp[vv] = next_w
                    heapq.heappush(heap,(next_w,vv))
        return dp

    def wolfDijkstra(start):
        heap = []
        dp = [INF] * (n+1)
        for vv,ww in graph[start]:
                next_w = ww
                if dp[vv] > next_w:
                    dp[vv] = next_w
                    heapq.heappush(heap,(next_w,vv))       

        while heap:
            w,cur = heapq.heappop(heap)
            for vv,ww in graph[cur]:
                next_w = 2*w + ww//2
                if dp[vv] > next_w:
                    dp[vv] = next_w
                    heapq.heappush(heap,(next_w,vv))
        return dp
    fox = foxDijkstra(1)
    wolf = wolfDijkstra(1)
    print(fox)
    print(wolf)
    
    result = 0
    for i in range(1,n+1):
        if fox[i] > wolf [i]:
            result +=1
    print(result)

