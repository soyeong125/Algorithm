import sys
sys.stdin = open("input.txt","rt")
from collections import deque

def DFS(L,val,goal):
    if val==goal:
        print(L+1)
        sys.exit()
    if val>goal:
        return
    DFS(L+1,val*2,goal)
    DFS(L+1,(val*10)+1,goal)

A,B = map(int,input().split())
DFS(0,A,B)
print(-1)
    

