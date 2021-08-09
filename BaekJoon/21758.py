import sys
sys.stdin=open("input.txt","rt")

n=int(input())
arr=list(map(int,input().split()))
result=[]


for i in range(1,n):
    max=0
    tmp=0
    for j in range(i+1,n):
        tmp+=arr[i]
    if max < tmp:
        max=tmp
result.append(sum(arr)-arr[0]+max)
for i in range(n-2,0,-1):
    max=0
    tmp=0
    for j in range(i-1,0):
        tmp+=arr[i]
    if max < tmp:
        max=tmp
result.append(sum(arr)-arr[-1]+max)

print(result)

