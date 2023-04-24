import sys
input = sys.stdin.readline
if __name__ == "__main__":
    n,m = map(int,input().split())
    res = 0
    arr = [[0] * (n+1) for _ in range(n+1)]
    for _ in range(m):
        tall,short = map(int,input().split())
        arr[tall][short] = 1

    for k in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                if arr[i][j] == 1 or (arr[i][k] == 1 and arr[k][j] == 1):
                    arr[i][j] = 1 # i -> j 가 연결되었는지?
    for i in range(1,n+1):
        cnt = 0
        for j in range(1,n+1):
            cnt += (arr[i][j] + arr[j][i])
        if cnt == (n-1):
            res +=1
    print(res)