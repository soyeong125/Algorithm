if __name__ == "__main__":
    # 플로이드 와샬 구현하기
    # 2차원 배열 생성
    # 무한으로 초기화
    # 나 자신은 0
    n = int(input())
    INF = 100000000
    res = [[INF] * (n+1) for _ in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,n+1):
            if i == j:
                res[i][j] = 0

    # 각 정보를 입력받아 초기화 (양방향 아님 단반향이고 다름)
    m = int(input())
    for _ in range(m):
        a,b,c = map(int,input().split())
        res[a][b] = min(res[a][b],c)

    # 거쳐가는 경로를 기준으로 플로이드 와샬 알고리즘 구현
    for k in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                res[i][j] = min(res[i][j],res[i][k] + res[k][j])

    for i in range(1,n+1):
        for j in range(1,n+1):
            if res[i][j] >= INF:
                print(0,end = ' ')
            else:
                print(res[i][j],end = ' ')
        print()