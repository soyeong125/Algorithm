import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n,m = map(int,input().split())
    dna = [input() for _ in range(n)]
    res = []
    resnum = 0
    for i in range(m):
        nucle = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
        for j in range(n):
            nucle[dna[j][i]]+=1
        maxval = nucle['A']
        resval = 'A'
        for k,y in nucle.items():
            if y > maxval:
                maxval = y
                resval = k
        res.append(resval)
        resnum += (n - maxval)
    print("".join(res))
    print(resnum)