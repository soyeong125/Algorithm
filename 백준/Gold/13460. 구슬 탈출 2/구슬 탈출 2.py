import sys
from collections import deque

if __name__ == "__main__":
    n,m = map(int,input().split())
    board = [list(input().rstrip()) for _ in range(n)]

    res = -1
    #구슬의 위치 찾기
    rx,ry,bx,by = 0,0,0,0
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'R':
                rx,ry = i,j
            elif board[i][j] == 'B':
                bx,by = i,j

    q = deque()
    q.append([rx,ry,bx,by,0])
    visited = [[[[0] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]
    visited[rx][ry][bx][by] = 1

    dx = [1,-1,0,0]
    dy = [0,0,1,-1]

    def move(x,y,dxx,dyy):
        tmp_cnt = 0 #이동 횟수 체크

        while board[x+dxx][y+dyy] != '#' and board[x][y] != 'O': #벽이 아니고 현재 0이 아니면
                x += dxx
                y += dyy
                tmp_cnt +=1

        return x,y,tmp_cnt #최종 값 리턴

    flag = True
    while q:
        rx1,ry1,bx1,by1,cnt = q.popleft()

        if cnt >= 10: #움직인 횟수가 10번 이상이면 실패
            break

        for k in range(4):
            rx2,ry2,rcnt = move(rx1,ry1,dx[k],dy[k])
            bx2,by2,bcnt = move(bx1,by1,dx[k],dy[k])

            if board[bx2][by2] == 'O':  # 파란색이 먼저 구멍에 들어가면 실패
                continue
            if board[rx2][ry2] == 'O':  # 빨간 구술이 구멍에 들어가면 성공
                res = cnt + 1
                flag = False
                break

            #빨간 구슬하고 파란구슬하고 겹친다면 cnt가 더 많은 구슬을 하나 뒤로 빼준다
            if rx2 == bx2 and ry2 == by2:
                if rcnt > bcnt:
                    rx2 -= dx[k]
                    ry2 -= dy[k]
                else:
                    bx2 -= dx[k]
                    by2 -= dy[k]

            if not visited[rx2][ry2][bx2][by2]:
                q.append([rx2,ry2,bx2,by2,cnt+1])
                visited[rx2][ry2][bx2][by2] = 1
        if not flag:
            break
    print(res)