import sys
import heapq
sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline
INF = sys.maxsize

if __name__ == "__main__":
    n,e = map(int,input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(e):
        s,e,w = map(int,input().split())
        graph[s].append((w,e))
        graph[e].append((w,s))
    n1,n2 = map(int,input().split())
   
    def dijkstra(start):
        heap = []
        dp = [INF] * (n+1)
        dp[start] = 0 
        heapq.heappush(heap,(0,start))
        while heap:
            w,cur = heapq.heappop(heap)
            if dp[cur] < w:
                continue
            for ww,ee in graph[cur]:
                next_w = ww + w
                if dp[ee] > next_w:                 
                    dp[ee] = next_w
                    heapq.heappush(heap,[next_w,ee])
        return dp
    one = dijkstra(1)
    n1_ = dijkstra(n1)
    n2_ = dijkstra(n2)
    cnt = min(one[n1]+n1_[n2]+n2_[n],one[n2]+n2_[n1]+n1_[n])
    print(cnt if cnt < INF else -1)



