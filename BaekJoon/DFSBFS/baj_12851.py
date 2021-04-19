import sys
sys.stdin = open("input.txt","rt")
from collections import deque

n,k = map(int,input().split())
visited=list()
visited.append(n)
q=deque()
q.append((n,0))
minn=2167000000
cnt=0
while q:
    now = q.popleft()
    if now[1]>minn:
        continue
    if now[0] == k:
        if minn>=now[1]:
            minn=min(minn,now[1])
            cnt+=1
            

    visited.append(now[0])
    if (now[0]-1 < 0 and now[0]-1 >100000) and (now[0]+1 < 0 and now[0]+1 >100000) and (now[0]*2 < 0 and now[0]*2 >100000):
            continue
    if not now[0]-1 in visited and (0<=now[0]-1<100000):
        q.append((now[0]-1,now[1]+1))

    if not now[0]+1 in visited and (0<=now[0]+1<100000):
        q.append((now[0]+1,now[1]+1))

    if not now[0]*2 in visited and (0<=now[0]*2<100000):
        q.append((now[0]*2,now[1]+1))



print(minn)
print(cnt)
