import sys
sys.stdin = open("input.txt","rt")
from collections import deque

 
if __name__ =="__main__":
    m,n = map(int,input().split())
    grap=[list(input()) for _ in range(n)]
    ch=[[0]*m for _ in range(n)]
    W,B=0,0
    dx=[1,-1,0,0]
    dy=[0,0,1,-1]
    q=deque()
    for i in range(n):
        for j in range(m):
            tmp=1
            if ch[i][j]==0:
                ch[i][j]=1
                q.append((i,j,grap[i][j]))
                while q:
                    val  = q.popleft()
                    for k in range(4):
                        x=val[0]+dx[k]
                        y=val[1]+dy[k]
                        v=val[2]
                        if 0<=x<n and 0<=y<m and grap[x][y]==v and ch[x][y]==0:
                            q.append((x,y,v))
                            ch[x][y]=1
                            tmp+=1
                if grap[i][j]=='W':
                    W+=tmp*tmp
                else:
                    B+=tmp*tmp
    print(W,B)



