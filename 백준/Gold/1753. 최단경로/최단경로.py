import heapq
import sys
input = sys.stdin.readline
INF = sys.maxsize

if __name__ == "__main__":
    #노드 갯수, 간선 갯수 입력 받기
    v,e = map(int,input().split())
    #시작 노드 입력 받기
    k = int(input())
    #각 노드에 연결된 노드 정보 인접 리스트 생성
    graph = [[] for _ in range(v+1)]
    #최단 거리 테이블 초기화
    distance = [INF] * (v + 1)
    # 간선 정보 입력 받기
    for _ in range(e):
        s,e,w = map(int,input().split())
        graph[s].append((e,w)) # s노드에서 e노드로 가는 비용이 w

    def dijkstra(start):
        heap = []
        heapq.heappush(heap,(0,start)) #가중치로 최소힙을 만들기
        distance[start] = 0 #시작 노드는 0으로 초기화

        while heap:
            w,cur = heapq.heappop(heap) #가중치가 가장 짧은 노드 정보 꺼내기
            if distance[cur] < w: #이미 처리된 노드는 무시
                continue
            for vv,ww in graph[cur]: #현재 노드와 연결된 인접한 노드 확인
                next_w = w + ww
                if distance[vv] > next_w: #현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
                    distance[vv] = next_w
                    heapq.heappush(heap,(next_w,vv))
    dijkstra(k)
    for i in range(1,v+1):
        print('INF' if distance[i] == INF else distance[i])