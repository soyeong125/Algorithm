import sys
sys.stdin=open("input.txt","rt")

k = int(input())
arr=sorted([int(input()) for _ in range(k)])
max=0
for i in range(k,0,-1):
    if arr[k-i]*i > max:
        max = arr[k-i]*i
print(max)



