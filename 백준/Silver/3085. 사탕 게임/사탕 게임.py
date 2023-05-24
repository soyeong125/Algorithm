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

        for i in range(n):
            for j in range(n):
                if i+1 < n : #밑에 체크
                    bomboni[i][j], bomboni[i+1][j] = bomboni[i+1][j], bomboni[i][j]
                    tmp = check(bomboni)
                    if tmp > result:
                        result =tmp
                    bomboni[i][j], bomboni[i + 1][j] = bomboni[i + 1][j], bomboni[i][j]
                if j+1 < n:
                    bomboni[i][j], bomboni[i][j+1] = bomboni[i][j+1], bomboni[i][j]
                    tmp = check(bomboni)
                    if tmp > result:
                        result = tmp
                    bomboni[i][j], bomboni[i][j+1] = bomboni[i][j+1], bomboni[i][j]
        print(result)