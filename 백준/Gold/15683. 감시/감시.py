import sys
import itertools

if __name__ == "__main__":
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]

    # CCTV 개수 확인
    cctv_cnt = 0
    cctv = []
    wall = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] > 0 and arr[i][j] < 6:
                cctv_cnt += 1
                cctv.append([i, j])
            if arr[i][j] == 6:
                wall += 1


    cctv_list = list(itertools.product([i for i in range(4)], repeat=cctv_cnt))

    dx = [0,0,-1,1]
    dy = [1,-1,0,0]
    direction = {
        1 : [[0],[3],[1],[2]],
        2 : [[0,1],[2,3],[0,1],[2,3]],
        3 : [[0,2],[0,3],[1,3],[1,2]],
        4 : [[0,1,2],[0,2,3],[0,1,3],[1,2,3]],
        5 : [0,1,2,3]
    }
    # 행 열
    # 오른쪽 (0,1) 0
    # 왼쪽 (0,-1) 1
    # 위쪽 (-1,0) 2
    # 아래쪽 (1,0) 3


    res = int(1e9)
    for cl in cctv_list:
        visited = [[0] * m for _ in range(n)]

        for i in range(cctv_cnt):
            cctv_num = arr[cctv[i][0]][cctv[i][1]]
            if cctv_num == 5:
                cctv_dir = direction[cctv_num]
            else:
                cctv_dir = direction[cctv_num][cl[i]]

            for d in cctv_dir:
                x = cctv[i][0]
                y = cctv[i][1]
                xx = dx[d]
                yy = dy[d]
                while 0 <= x + xx < n and 0 <= y + yy < m:
                    if arr[x + xx][y + yy] == 6:
                        break
                    x += xx
                    y += yy
                    if visited[x][y] == 0 and arr[x][y] == 0:
                        visited[x][y] = 1

        v_cnt = 0
        for h in range(n):
            v_cnt += visited[h].count(1)
        tmp_res = max(0, (n * m) - wall - v_cnt - cctv_cnt)
        res = min(res, tmp_res)

    print(res)