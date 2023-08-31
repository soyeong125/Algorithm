import sys
from collections import deque

if __name__ == "__main__":
    n,m = map(int,input().split())
    arr = [list(input().rstrip()) for _ in range(n)]
    res = -1

    rx,ry,bx,by = 0,0,0,0

    for i in range(n):
        for j in range(m):
            if arr[i][j] == 'R':
                rx , ry = i ,j
            elif arr[i][j] == 'B':
                bx,by = i, j

    qq = deque()
    qq.append([rx,ry,bx,by,0])

    visited = [[[[0] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]
    visited[rx][ry][bx][by] = 1

    dx = [1,-1,0,0] #아래 위 오 왼
    dy = [0,0,1,-1]

    def move(x,y,k):
        tmp_cnt = 0

        while arr[x+dx[k]][y+dy[k]] != '#' and arr[x][y] != 'O': #다음에 갈 수 있고 & 현재 구멍이 아니면 계속 이동
            x += dx[k]
            y += dy[k]
            tmp_cnt +=1

        return [x,y,tmp_cnt]


    while qq:
        rx,ry,bx,by,cnt = qq.popleft()
        if cnt >= 10:
            continue
        for k in range(4):
            #빨간 구슬 움직이기
            rxx,ryy,r_cnt = move(rx,ry,k)
            #파란 구슬 움직이기
            bxx,byy,b_cnt = move(bx,by,k)

            #파란색이 빠졌으면 fail
            if arr[bxx][byy] == 'O':
                continue
            #빨간색이 빠졌으면 cnt + 1 리턴하고 끝
            if arr[rxx][ryy] == 'O':
                res = cnt + 1
                break

            #둘이 동일한 위치라면 더 많이 움직인 쪽이 한칸 뒤로 가기
            if rxx == bxx and ryy == byy:
                if r_cnt > b_cnt:
                    rxx -= dx[k]
                    ryy -= dy[k]
                else:
                    bxx -= dx[k]
                    byy -= dy[k]

            #신규 위치 q에 넣기
            if visited[rxx][ryy][bxx][byy] == 0:
                visited[rxx][ryy][bxx][byy] = 1
                qq.append([rxx,ryy,bxx,byy,cnt+1])
        if res > 0 :
            break
    print(res)