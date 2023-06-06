import sys
from collections import deque
input = sys.stdin.readline
if __name__ == "__main__":
    #8421:남동북서 (아래 오른쪽 위 왼쪽) 0이면 갈 수 있음
    m,n = map(int,input().split())
    room_input = [list(map(int,input().split())) for _ in range(n)]
    room_2 = [[] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            changeVal = bin(room_input[i][j])[2:]
            room_2[i].append(list(map(int,'0'*(4-len(changeVal))+changeVal)))

    def bfs():
        visited = [[0] * m for _ in range(n)]
        res = []
        cnt1,cnt2 =0,0 #방의 갯수, 방의 넓이
        dx = [1,0,-1,0]
        dy = [0,1,0,-1]
        for i in range(n):
            for j in range(m):
                if not visited[i][j]:
                    visited[i][j] = 1
                    q = deque()
                    q.append([i,j])
                    cnt1 +=1
                    cnt2 = 1
                    while q:
                        x,y = q.popleft()
                        for kk in range(4):
                            if not room_2[x][y][kk]:
                                xx = x + dx[kk]
                                yy = y + dy[kk]
                                if 0<=xx<n and 0<=yy<m and not visited[xx][yy]:
                                    q.append([xx,yy])
                                    visited[xx][yy] = 1
                                    cnt2 +=1
                    res.append([cnt1,cnt2])
        return res
    tmp1 = bfs()
    tmp1.sort(key = lambda x:-x[1])
    maxRoomSpace = 0

    for i in range(n):
        for j in range(m):
            for k in range(2):
                if room_2[i][j][k]:
                    room_2[i][j][k] = 0
                    tmp = bfs()
                    tmp.sort(key = lambda x:-x[1])
                    maxRoomSpace = max(maxRoomSpace, tmp[0][1])
                    room_2[i][j][k] = 1

    print(len(tmp1))
    print(tmp1[0][1])
    print(maxRoomSpace)