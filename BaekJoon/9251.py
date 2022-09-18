import sys
sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline


if __name__ == "__main__":  
    a = "0"+ input().strip()
    b = "0" + input().strip()
    lena = len(a)
    lenb = len(b)
    LCS = [[0] * lenb for _ in range(lena)]

    for i in range(1,lena):
        for j in range(1,lenb):
            if a[i] == b[j]:
                 LCS[i][j] = LCS[i-1][j-1] + 1
            else:
               LCS[i][j] = max(LCS[i][j-1] ,LCS[i-1][j])
    
    print(LCS[lena-1][lenb-1])
    