if __name__ == "__main__":
    n, m = map(int, input().split())
    arr = [int(input()) for _ in range(n)]

    con = [[0] + [-float('inf')] * (m) for _ in range(n)]
    notcon = [[0] + [-float('inf')] * (m) for _ in range(n)]
    #행 : 인덱스
    #열 : 구간
    #con[i][j] = 현재 인덱스를 기준으로, 현재 인덱스를 포함해서 j개의 구간의 최댓값 -> 1. 내 앞에 있는 인덱스를 포함해서 j구간일 때 최대값(나 자신도 구간에 넣어짐), 2.내 앞에 인덱스 포함 안함 구간도 -1 내가 구간+1이니까
    #

    con[0][1] = arr[0] #예외 열 인덱스를 포함하지 않아야 하지만 이건 포함해야함

    for i in range(1,n): #포함할지 말지 정하는 인덱스
        for j in range(1,min(m,(i+2)//2) + 1): #구간
            notcon[i][j] = max(con[i-1][j],notcon[i-1][j])
            con[i][j] = max(con[i-1][j], notcon[i-1][j-1]) + arr[i]

    print(max(con[n-1][m],notcon[n-1][m]))