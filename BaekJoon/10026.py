import sys
sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline
sys.setrecursionlimit(100000)

if __name__ == "__main__":
    n = int(input())
    area = [list(map(str,input())) for _ in range(n)]
  


    def DFS1(x,y,cur):
        dx = [1,-1,0,0]
        dy = [0,0,1,-1]
        for k in range(4):
            xx = x + dx[k]
            yy = y + dy[k]
            if 0<= xx < n and 0<= yy < n and not visited[xx][yy]:
                if area[xx][yy] == cur:
                    visited[xx][yy] = 1
                    DFS1(xx,yy,cur)
    def DFS2(x,y,cur):
        dx = [1,-1,0,0]
        dy = [0,0,1,-1]
        for k in range(4):
            xx = x + dx[k]
            yy = y + dy[k]
            if 0<= xx < n and 0<= yy < n and not visited[xx][yy]:
                if cur == 'R' or cur == 'G':
                    if area[xx][yy] == 'R' or area[xx][yy] == 'G':
                        visited[xx][yy]=1
                        DFS2(xx,yy,cur)
                else:
                    if area[xx][yy] == cur:
                        visited[xx][yy]=1
                        DFS2(xx,yy,cur)

            


    cnt1 = 0
    visited = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                visited[i][j] = 1
                cnt1 +=1
                DFS1(i,j,area[i][j])

    cnt2 = 0
    visited = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                visited[i][j] = 1
                cnt2 +=1
                DFS2(i,j,area[i][j])

    print(cnt1,cnt2)             
                
 



    