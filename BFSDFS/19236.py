import sys
sys.stdin=open("input.txt","rt")


a=[[1,2,3],[1]]
b = a[:1]
b.append(4)
print(a)
print(b)
k = a is b
a[0].append(5)
print(a)
print(b)

#dx = [-1, -1, 0, 1, 1, 1, 0, -1]
#dy = [0, -1, -1, -1, 0, 1, 1, 1]


#def food(array, x, y): 
#    positions = []
#    direction = array[x][y][1]
#    for i in range(1, 4):
#        nx, ny = x + dx[direction], y + dy[direction]
#        if 0 <= nx < 4 and 0 <= ny < 4 and 1 <= array[nx][ny][0] <= 16:
#            positions.append([nx, ny])
#        x, y = nx, ny
#    return positions



#def find_fish(array, index):
#    for i in range(4):
#        for j in range(4):
#            if array[i][j][0] == index:
#                return (i, j)
#    return None


#def move_fish(array, now_x, now_y):  
#    flag = False
#    position = []
#    for i in range(1, 17):
#        position = find_fish(array, i)
#        if position is None:
#            continue
#        x, y = position[0], position[1]
#        dir = array[x][y][1] 
#        for j in range(8):
#            nx, ny = x + dx[dir], y + dy[dir]
#            if 0 <= nx < 4 and 0 <= ny < 4:
#                if not (nx == now_x and ny == now_y): 
#                    array[x][y][0], array[nx][ny][0] = array[nx][ny][0], array[x][y][0]
#                    array[x][y][1], array[nx][ny][1] = array[nx][ny][1], dir
#                    break
#            dir = (dir + 1) % 8


#def dfs(array, x, y, total):
#    global answer
#    array = copy.deepcopy(array)

#    number = array[x][y][0]
#    array[x][y][0] = -1

#    move_fish(array, x, y)

#    result = food(array, x, y)

#    answer = max(answer, total + number)
#    for next_x, next_y in result:
#        dfs(array, next_x, next_y, total + number)


#if __name__ == "__main__":
#    temp = [list(map(int, input().split())) for _ in range(4)]
#    array = [[None] * 4 for _ in range(4)]
#    for i in range(4):
#        for j in range(4):
#            array[i][j] = [temp[i][j * 2], temp[i][j * 2 + 1] - 1]

#    answer = 0
#    dfs(array, 0, 0, 0)
#    print(answer)


#for i in range(4):
#	f =[]
#	for j in range(4):
#		f.append([arr[i][2*j], arr[i][2*j +1]])
#	fish.append(f)

#sx , sy = 0, 0
#ss = fish[0][0][1]
#eat = fish[0][0][0]

#fish[0][0][0] = 0
#fish[0][0][1] = 0

#while True:
#	for k in range(1,17):
#		for i in range(4):
#			for j in range(4):
#				if fish[i][j][0] == k:
#					nx =  dx[fish[i][j][1]] + i 
#					ny = dy[fish[i][j][1]] + j
#					flag = True
#					if  (nx < 0 or nx >= 4 or ny < 0 or ny >= 4) or (nx == sx and ny == sy):
#						flag = False
#						kk = 0
#						for k in range(1,9):
#							if dx[(fish[i][j][1]+k) % 9] == 0 and dy[(fish[i][j][1]+k) % 9] == 0: continue
#							xx = dx[(fish[i][j][1]+k) % 9] + i
#							yy = dy[(fish[i][j][1]+k) % 9] + j 
#							kk = (fish[i][j][1]+k) % 9
#							if xx >= 0 and xx < 4 and 0 <= yy and yy < 4 and (xx != sx) and (yy != sy):
#								nx = xx
#								ny = yy
#								fish[i][j][1] = kk
#								flag = True
#								break
#					if flag:
#						fish[nx][ny][0] = fish[i][j][0]
#						fish[nx][ny][1] = fish[i][j][1]

#						if fish[nx][ny][0] == 0:
#							fish[i][j][0] = 0
#							fish[i][j][1] = 0
#						else:
#							fish[i][j][0] = fish[nx][ny][0]
#							fish[i][j][1] = fish[nx][ny][1]

#	sh =[]
#	for i in range(4):
#		sx = sx + dx[ss]
#		sy = sy + dy[ss]
#		if sx < 0 or sx >=4 or sy < 0 or sy >= 4:
#			continue
#		if fish[sx][sy][0] != 0:
#			sh.append((fish[sx][sy][0],sx,sy))
#	if len(sh) > 0:
#		sh.sort()
#		sx,sy  = sh[-1][1], sh[-1][2]
#		eat += fish[sx][sy][0]
#		ss = fish[sx][sy][1]
#		fish[sx][sy][0] , fish[sx][sy][1] = 0, 0 
#	else:
#		break
#print(eat)
			


		