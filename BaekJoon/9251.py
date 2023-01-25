import sys
sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline
sys.setrecursionlimit(10**8)
input = sys.stdin.readline


if __name__ == "__main__":  
    a = '0' + input().rstrip() #마진 주기
    b = '0' +input().rstrip() #마진 주기

    #각 문자열의 길이 찾기
    len_a = len(a) 
    len_b = len(b) 

    #dp 저장소
    lcs = [[0] * (len_b) for _ in range(len_a)]

    #lcs 길이 탐구
    for i in range(1,len_a):
        for j in range(1,len_b):     
            if a[i] == b[j]:#문자가 같은 경우, 바로 위 대각선 lcs 값에 + 1
                lcs[i][j] = lcs[i-1][j-1] + 1
            else: #같지 않은 경우 위쪽의 최댓값과 왼쪽의 최댓값중 큰 값
                lcs[i][j] = max(lcs[i-1][j],lcs[i][j-1])
    
    print(lcs[len_a-1][len_b-1])
    res = ""
    i = len_a-1
    b = len_b-1
    #LCS 찾기
    while 1:
        if lcs[i][j] == 0:
            break
        if lcs[i][j] == lcs[i-1][j]:
            i = i-1
        elif lcs[i][j] == lcs[i][j-1]:
            j = j-1
        else:
            res += a[i]
            i = i-1
            j = j-1
    print(res[::-1])



    