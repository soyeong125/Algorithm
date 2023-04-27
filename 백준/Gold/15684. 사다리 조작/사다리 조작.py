import sys
input = sys.stdin.readline

if __name__ == "__main__":
    #시작점이 사다리를 타고 도착점에 도달했을 때 시작점과 동일한지 체크
    def chk():
        for i in range(1,n+1):
            idx = i
            for j in range(1,h+1):
                if graph[j][idx]:
                    idx +=1
                elif graph[j][idx-1]:
                    idx -=1
            if not idx == i:
                return False
        return True


    def dfs(cnt,x):
        global answer
        if cnt > 3:
            return
        if chk():
            if answer > 0:
                answer = min(cnt,answer)
            else:
                answer = cnt
            return
        # 연속되지 않는 가로선 그리기
        for i in range(x,h+1):
            for j in range(1,n):
                if not graph[i][j]:
                    if j-1 >= 0 and graph[i][j-1]:
                        continue
                    if j+1 < n and graph[i][j+1]:
                        continue
                    graph[i][j] = 1
                    dfs(cnt+1,i)
                    graph[i][j] = 0

    n,m,h = map(int,input().split())
    graph = [[0] * (n + 1) for _ in range(h + 1)]

    if not m: #입력되는 가로선이 없으면 바로 종료
        print(0)
        sys.exit()

    for _ in range(m):
        a,b = map(int,input().split())
        graph[a][b] = 1

    answer = -1

    dfs(0,1)

    print(answer)
