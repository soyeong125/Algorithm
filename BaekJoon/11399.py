import sys
from collections import deque
sys.stdin=open("input.txt","rt")

n = int(input())
arr=deque(sorted(list(map(int,input().split()))))

tmp=0
result=0

while arr:
    tmp+=arr.popleft()
    result+=tmp
print(result)
