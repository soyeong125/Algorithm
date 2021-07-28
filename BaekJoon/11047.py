import sys
sys.stdin=open("input.txt","rt")

n,k = map(int,input().split())
arr=[]
cnt=0
for _ in range(n):
    arr.append(int(input()))
for i in reversed(range(n)):
    if arr[i] > k :
        continue
    cnt += k // arr[i]
    k = k % arr[i]
print(cnt)
