    import sys
    from collections import deque
    sys.stdin = open("input.txt", 'r')
    sys.setrecursionlimit(10**8)
    input = sys.stdin.readline

    #최단거리와, 최단거리를 만족하는 경우의 수를 구해야함 > 결과값을 담을 자료구조 2개 있어야함
    if __name__ == "__main__":  
        n,k = map(int,input().split())
        visited = [[-1] for _ in range(100001)]
        visited[n] = 0
        q = deque()
        q.append(n)
        
        while q:
            x = q.popleft()

            for i in [x-1,x+1,x*2]:
                if 0 <= i < 100001:
                    if i == x*2:
                        if visited[i] == -1:
                            q.appendleft(i)
                            visited[i] = visited[x]
                    else:
                        if visited[i] == -1:
                            q.append(i)
                            visited[i] = visited[x] + 1
        print(visited[k])
        