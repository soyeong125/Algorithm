import sys
sys.stdin=open("input.txt","rt")

n=int(input())
arr=list(input())
result=[arr[0]]*n
cnt=1

i=0
while i<n:
    if arr[i]==result[i]:
        i+=1
        continue
    while arr[i]!=result[i]:
        result[i]=arr[i]
        i+=1
        if i==n:
            break
    cnt+=1
print(cnt)
        



