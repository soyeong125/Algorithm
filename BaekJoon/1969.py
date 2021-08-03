import sys
sys.stdin=open("input.txt","rt")

n,m = map(int,input().split())
arr=sorted([input() for _ in range(n)])
result=[]
cnt=0
for i in range(m):
    rna={'T':0,'A':0,'G':0,'C':0}
    for j in range(n):
        rna[arr[j][i]]+=1
    tmp = sorted(rna.items(),key=lambda x:(-x[1],x[0]))
    result.append(tmp[0][0])
    cnt+=(n-tmp[0][1])
print("".join(result))
print(cnt)




