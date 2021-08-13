import sys
from collections import deque
sys.stdin=open("input.txt","rt")

n = int(sys.stdin.readline())
arr=sorted(list(map(int,sys.stdin.readline().split())),reverse=True)
summ=arr[0]
for i in range(1,n):
    summ+=arr[i]/2
print(summ)

    

