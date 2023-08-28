import sys

if __name__ == "__main__":
    n = int(input())
    arr = [[0] * n for _ in range(n)]
    favorit = [[] for _ in range(n*n+1)]
    
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    
    for _ in range(n*n):
        i_list = list(map(int,input().split()))
        favorit[i_list[0]] += (i_list[1:])
        tmp_list = []

        for i in range(n):
            for j in range(n):
                if not arr[i][j]:
                    friend = 0
                    empty = 0
                    for k in range(4):
                        x = i + dx[k]
                        y = j + dy[k]
                        if 0<=x<n and 0<=y<n:
                            if arr[x][y] == 0 :
                                empty +=1
                            elif arr[x][y] in i_list[1:]:
                                friend +=1
                    tmp_list.append([friend,empty,i,j])

        tmp_list.sort(key = lambda x: (-x[0],-x[1],x[2],x[3]))

        arr[tmp_list[0][2]][tmp_list[0][3]] = i_list[0]

    res = 0
    for i in range(n):
        for j in range(n):
            tmp = 0
            for k in range(4):
                x = i + dx[k]
                y = j + dy[k]
                if 0<=x<n and 0<=y<n:
                    if arr[x][y] in favorit[arr[i][j]]:
                        tmp +=1
            if tmp > 0:
                res += 10 ** (tmp-1)
    print(res)