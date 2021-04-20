import sys
sys.stdin = open("input.txt","rt")
from collections import deque
n,k = map(int,input().split())
visited=[0]*100001
q=deque()
q.append((n,0))
visited[n]=1
while q:
    val,idx = q.popleft()
    if val==k:
        print(idx)
        sys.exit()
    if 0<=val*2<=100000 and visited[val*2]==0:
        q.append((val*2,idx))
        visited[val*2]=1
    if 0<=val-1 and visited[val-1]==0:
        q.append((val-1,idx+1))
        visited[val-1]=1
    if 0<=val+1<=100000 and visited[val+1]==0:
        q.append((val+1,idx+1))
        visited[val+1]=1






    

