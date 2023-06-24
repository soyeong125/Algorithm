import sys
from collections import deque
if __name__ == "__main__":
    # 터질 수 있는 뿌요가 있는지 무한으로 체크한다 flag로 빠지기
    # bfs로 모든 뿌요 터트리기
    # 터트린 뿌요 좌표 담기
    # 터진 뿌요가 있으면 하나씩 떨어뜨려서 정리해주기
    n,m = 12,6
    puyo = [list(input().rstrip()) for _ in range(n)]

    flag = True
    res = 0
    def bfs(i,j):
        q = deque()
        q.append([i,j])
        visited[i][j] = 1

        boom = [[i,j]]

        dx = [1,-1,0,0]
        dy = [0,0,1,-1]

        while q:
            x,y = q.popleft()
            for k in range(4):
                xx = x + dx[k]
                yy = y + dy[k]
                if 0<=xx<n and 0<=yy<m and not visited[xx][yy]:
                    if puyo[x][y] == puyo[xx][yy]:
                        visited[xx][yy] = 1
                        q.append([xx,yy])
                        boom.append([xx,yy])
        if len(boom) >= 4:
            #제거하기
            for x,y in boom:
                puyo[x][y] = '.'
            #아래로 내리기
            for i in range(m):
                for j in range(n-1,-1,-1):
                    for k in range(j-1,-1,-1):
                        if puyo[j][i] == '.' and puyo[k][i] != '.':
                            puyo[j][i] = puyo[k][i]
                            puyo[k][i] = '.'
                            break
            return True
        return False


    while 1:
        flag = False
        visited = [[0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if not visited[i][j] and puyo[i][j] != '.':
                    if bfs(i,j):
                        flag = True

        if flag:
            res +=1
        else:
            break
    print(res)