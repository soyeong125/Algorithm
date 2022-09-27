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


  