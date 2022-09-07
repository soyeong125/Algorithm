import sys
sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline
sys.setrecursionlimit(100000)
#dfs
if __name__ == "__main__":
    R,C = map(int,input().split())
    area = [list(map(str,input())) for _ in range(R)]
    arr = [0] * 26
    result = 0
    
    def DFS(cnt,x,y):          
        global result  
        result = max(cnt,result)
        dx = [1,-1,0,0]
        dy = [0,0,1,-1]
        for k in range(4):
            xx = dx[k] + x
            yy = dy[k] + y
            if 0<=xx<R and 0<=yy<C and not arr[ord(area[xx][yy])-65]:
                    arr[ord(area[xx][yy])-65] = 1 
                    DFS(cnt+1,xx,yy)
                    arr[ord(area[xx][yy])-65] = 0
                    
    arr[ord(area[0][0])-65] = 1
    DFS(1,0,0)
    print(result)

#bfs    
import sys
from collections import deque
sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

if __name__ == "__main__":
    r,c = map(int,input().split())
    area = [list(input()) for _ in range(r)]
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    result = 0

    def bfs():
        global result
        q = set([(0,0,area[0][0])])
        while q:
            x,y,z = q.pop()
            result = max(result,len(z))
            for k in range(4):
                xx = x + dx[k]
                yy = y + dy[k]
                if 0<=xx<r and 0<=yy<c and area[xx][yy] not in z:
                    q.add((xx,yy,z+area[xx][yy]))
                    
   
    bfs()
    print(result)


  



    