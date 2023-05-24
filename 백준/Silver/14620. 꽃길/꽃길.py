import sys
import copy
input = sys.stdin.readline

if __name__ == "__main__":
        n = int(input())
        res = 10**8
        arr = [list(map(int,input().split())) for _ in range(n)]
        visited = [[0] * n for _ in range(n)]

        def check():
            tmp_arr = copy.deepcopy(visited)
            seed = []
            cnt = 0
            dx = [1,-1,0,0]
            dy = [0,0,1,-1]

            for i in range(1,n-1):
                for j in range(1,n-1):
                    if tmp_arr[i][j]:
                        seed.append([i,j])
                        cnt += arr[i][j]
            for x,y in seed:
                for k in range(4):
                    xx = x + dx[k]
                    yy = y + dy[k]
                    if not tmp_arr[xx][yy]:
                        tmp_arr[xx][yy] = 1
                        cnt += arr[xx][yy]
                    else:
                        return -1
            return cnt
        def dfs(l):
            global res
            if l == 3:
                tmp = check()
                if tmp >= 0:
                    res = min(res,tmp)
                return
            for i in range(1,n-1):
                for j in range(1,n-1):
                    if not visited[i][j] and not visited[i-1][j] and not visited[i][j-1] and not visited[i+1][j] and not visited[i][j+1]:
                        visited[i][j] = 1
                        dfs(l+1)
                        visited[i][j] = 0
        dfs(0)
        print(res)