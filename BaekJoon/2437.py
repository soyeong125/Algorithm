import sys
sys.stdin=open("input.txt","rt")

n=int(sys.stdin.readline())
arr=sorted(list(map(int,sys.stdin.readline().split())))
target=1
for i in arr:
    if target < i:
        break
    target+=i
print(target)
