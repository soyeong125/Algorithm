import heapq
import sys
input = sys.stdin.readline
INF = sys.maxsize

if __name__ == "__main__":
    v,e = map(int,input().split())
    graph = [[] for _ in range(v+1)]
    for _ in range(e):
        s,e,w = map(int,input().split())
        graph[s].append((e,w))
        graph[e].append((s,w))
    p1,p2 = map(int,input().split())

    def dijkstra(start):
        heap = []
        heapq.heappush(heap,(0,start))
        distance = [INF] * (v+1)
        distance[start] = 0

        while heap:
            ww,cur = heapq.heappop(heap)

            if distance[cur] < ww:
                continue

            for next_v , next_w in graph[cur]:
                cost = next_w + ww
                if distance[next_v] > cost :
                    distance[next_v] = cost
                    heapq.heappush(heap,(cost,next_v))
        return distance


    start_one = dijkstra(1)
    start_p1 = dijkstra(p1)
    start_p2 = dijkstra(p2)

    path_start_p1 = start_one[p1] + start_p1[p2] + start_p2[v]
    path_start_p2 = start_one[p2] + start_p2[p1] + start_p1[v]

    res = min(path_start_p1,path_start_p2)

    print(res if res < INF else -1)


