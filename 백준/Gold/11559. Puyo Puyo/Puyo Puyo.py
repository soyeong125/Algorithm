from collections import deque
if __name__ == "__main__":
    puyo = [list(input().rstrip()) for _ in range(12)]
    res = 0

    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    flag = True
    while 1:
        flag = False
        visited = [[0]*6 for _ in range(12)]
        for i in range(12):
            for j in range(6):
                if puyo[i][j] != '.' and not visited[i][j]:
                    visited[i][j] = 1
                    tmp = []
                    q = deque()
                    q.append([i,j])
                    while q:
                        x,y = q.popleft()
                        tmp.append([x,y])
                        for k in range(4):
                            xx = x + dx[k]
                            yy = y + dy[k]
                            if 0<=xx<12 and 0<=yy<6 and not visited[xx][yy]:
                                if puyo[x][y] == puyo[xx][yy]:
                                    q.append([xx,yy])
                                    visited[xx][yy] = 1
                    #만약 4개 이상이면 터뜨릴 수 있음
                    if len(tmp) >= 4:
                        flag = True
                        for x,y in tmp:
                            puyo[x][y] = '.'


        if not flag:
            break

        for i in range(6):
            for j in range(10, -1, -1):
                for k in range(11, j, -1):
                    if puyo[j][i] != "." and puyo[k][i] == ".":
                        puyo[k][i] = puyo[j][i]
                        puyo[j][i] = "."
                        break

        res +=1

    print(res)