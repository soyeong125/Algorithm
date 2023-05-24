import sys
input = sys.stdin.readline

if __name__ == "__main__":
        n = int(input())
        bomboni = [list(input().rstrip()) for _ in range(n)]
        result = 0

        def check(param):
            total = 1
            for i in range(n):
                cnt = 1
                for j in range(1,n): #열 순회
                    if param[i][j] == param[i][j-1]:
                        cnt +=1
                    else:
                        cnt = 1
                    if cnt > total:
                        total = cnt
                cnt = 1
                for j in range(1,n): #행 순회
                    if param[j][i] == param[j-1][i]:
                        cnt +=1
                    else:
                        cnt = 1
                    if cnt > total:
                        total = cnt
            return total

        dx = [1,0]
        dy = [0,1]
        for i in range(n):
            for j in range(n):
                for k in range(2):
                    x = i + dx[k]
                    y = j + dy[k]
                    if 0<=x<n and 0<=y<n and bomboni[i][j] != bomboni[x][y]:
                        bomboni[i][j], bomboni[x][y] = bomboni[x][y], bomboni[i][j]
                        tmp = check(bomboni)
                        if tmp > result:
                            result = tmp
                        bomboni[i][j], bomboni[x][y] = bomboni[x][y], bomboni[i][j]

        print(result)