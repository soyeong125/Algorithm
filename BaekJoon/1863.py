import sys
sys.stdin=open("input.txt","rt")

n = int(input())
stack = []
cnt = 0
for i in range(n):
    x,y = map(int,input().split())
    if stack:
        if stack[-1] > y:
            while not stack or stack[-1] > y:
                stack.pop()
            cnt+=1
    stack.append(y)
print(cnt+len(stack))

