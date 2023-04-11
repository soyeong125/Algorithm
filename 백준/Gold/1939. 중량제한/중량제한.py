import sys

sys.setrecursionlimit(1000000)
input = sys.stdin.readline

# start -> end까지 weight 무게로 통과가능한지
# DFS 재귀함수로 구현
def check(cur, weight):
    global end
    if cur == end:
        return True

    for node, bridgeW in graph[cur]:
        if bridgeW >= weight and not visited[node]:  # 중량이 넘지 않는다면
            visited[node] = True
            if check(node, weight):
                return True
            # visited[node] = False -> ✅ 이부분 때문에 자꾸 시간초과남

    return False


if __name__ == "__main__":
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))
        graph[b].append((a, c))

    start, end = map(int, input().split())

    left = 1
    right = 1000000000
    while left <= right:
        mid = (left + right) // 2
        visited = [False] * (n + 1)
        visited[start] = True

        if check(start, mid):
            left = mid + 1
        else:
            right = mid - 1

    print(right)