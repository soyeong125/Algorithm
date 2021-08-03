import sys
sys.stdin=open("input.txt","rt")

n,m = map(int,input().split())
arr=sorted([input() for _ in range(n)])
result=""
minn=2176000000
for i in range(n):
    cnt=0
    for j in range(n):
        if i==j:
            continue
        for k in range(m):
            if arr[i][k] != arr[j][k]:
                cnt+=1
    if cnt < minn:
        minn = cnt
        result = arr[i]
print(result)
print(minn)


