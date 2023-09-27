import sys
if __name__ == "__main__":
    n,m,x,y,k = map(int,input().split())
    board = []
    bottom = 0
    ans = []

    for _ in range(n):
        board.append(list(map(int, input().split())))

    move = list(map(int,input().split()))

    dice = [[[0,0],0],[[-1,0],0],[[1,0],0],[[0,-1],0],[[0,1],0],[[0,2],0]]


    def switch(s):
        if s == 1: # 동쪽으로 굴리기 (0,0) -> (-1,0) (-1,0) -> (0,2) (1,0) -> (0,0) (0,2) -> (1,0)
            for j in range(6):
                if dice[j][0] == [0,0]:
                    dice[j][0] = [-1,0]
                elif dice[j][0] == [-1,0]:
                    dice[j][0] = [0,2]
                elif dice[j][0] == [1,0]:
                    dice[j][0] = [0,0]
                elif dice[j][0] == [0,2]:
                    dice[j][0] = [1,0]
        elif s == 2: # 서쪽으로 굴리기 (-1,0) -> (0,0) (1,0) ->(0,2) (0,0) -> (1,0) (0,2) -> (-1,0)
            for j in range(6):
                if dice[j][0] == [-1,0]:
                    dice[j][0] = [0,0]
                elif dice[j][0] == [1,0]:
                    dice[j][0] = [0,2]
                elif dice[j][0] == [0,0]:
                    dice[j][0] = [1,0]
                elif dice[j][0] == [0,2]:
                    dice[j][0] = [-1,0]
        elif s == 3: # 북쪽으로 굴리기 x = 0 인 것들 y-1씩 -2이면 2로 강등
            for j in range(6):
                if dice[j][0][0] == 0:
                    dice[j][0][1] += 1
                    if dice[j][0][1] == 3:
                        dice[j][0][1] = -1
        elif s == 4: # 남쪽으로 굴리기 x = 0 인 것들 y+1씩 3되면 -1로 강등
            # (0,-1)-> (0,2) (0,0) -> (0,-1),(0,1) -> (
            for j in range(6):
                if dice[j][0][0] == 0:
                    dice[j][0][1] -= 1
                    if dice[j][0][1] == -2:
                        dice[j][0][1] = 2



    i = 0
    flag = True

    dx = [0,0,0,-1,1]
    dy = [0,1,-1,0,0]

    while i < k:
        d = move[i]

        if 0<= x + dx[d] < n and 0<= y + dy[d] <m:
            x += dx[d]
            y += dy[d]
            switch(d)
            flag = True
        else:
            flag = False

        if flag:
            up,down = 0,0
            for j in range(6):
                if dice[j][0] == [0,2]:
                    up = j
                elif dice[j][0] == [0,0]:
                    down = j
            if board[x][y] == 0:
                board[x][y] = dice[down][1]
            else:
                dice[down][1] = board[x][y]
                board[x][y] = 0

            print(dice[up][1])
        i +=1