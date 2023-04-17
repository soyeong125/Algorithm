if __name__ == "__main__":
    a = '0' + input().rstrip()
    b = '0' + input().rstrip()

    len_a = len(a)
    len_b = len(b)

    LCS = [[0] * len_b for _ in range(len_a)]

    for i in range(1,len_a):
        for j in range(1,len_b):
            if a[i] == b[j]:
                LCS[i][j] = LCS[i-1][j-1] + 1
            else:
                LCS[i][j] = max(LCS[i-1][j],LCS[i][j-1])
    print(LCS[len_a-1][len_b-1])