import sys
input = sys.stdin.readline
if __name__ == "__main__":
    def check():
        for i in range(1,n+1):
            idx = i
            for j in range(1,h+1):
                if ladder[j][idx]:
                    idx +=1
                elif ladder[j][idx-1]:
                    idx -=1
            if not idx == i:
                return False
        return True


    def dfs(cnt,x):
        global answer

        if cnt > 3:
            return

        if check():
            if answer > 0 :
                answer = min(cnt, answer)
            else:
                answer = cnt
            return



        for i in range(x,h+1):
            for j in range(1,n):
                if not ladder[i][j]:
                    if j-1 >= 0 and ladder[i][j-1]:
                        continue
                    if j+1 < n and ladder[i][j+1]:
                        continue
                    ladder[i][j] = 1
                    dfs(cnt+1,i)
                    ladder[i][j] = 0

    n,m,h = map(int,input().split())
    ladder = [[0] * (n+1) for _ in range(h+1)]

    if not m :
        print(0)
        exit()

    for _ in range(m):
        a,b = map(int,input().split())
        ladder[a][b] = 1

    answer = -1

    dfs(0,1)

    print(answer)