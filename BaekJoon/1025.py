import sys
sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline

if __name__ == "__main__":  
    n,m = map(int,input().split())
    arr = []
    s = set()
    for _ in range(n):
        arr.append(list(input().rstrip()))

    def issquare(n):
        return int(n**0.5)**2 == n

    #행 선택하기
    for i in range(n):
        for j in range(m):           
            for k in range(1,m):
                jj = j
                tmp = ""
                while 1:
                    if jj >= m:
                        break
                    tmp += arr[i][jj]
                    jj += k
                s.add(tmp)
                s.add(tmp[::-1])
    #열 선택하기
    for i in range(m):
        for j in range(n):        
            for k in range(1,n):
                jj = j
                tmp = ""
                while 1:
                    if jj >= n:
                        break
                    tmp += arr[jj][i]
                    jj += k 
                s.add(tmp)
                s.add(tmp[::-1])
    #가운데 선택하기
    for i in range(n):
        for j in range(m):
            tmp = ""
            kk = 1
            while 1:
                k = kk
                while 1:
                    if 0<=(i+k)<n and 0<=(j+k)<m:
                        tmp += arr[i+k][j+k]
                        k+=1
                    s.add(tmp)
                    s.add(tmp[::-1])
                kk+=1
                if i+kk >= n or j+kk >= m:
                    break
    print(s)




   