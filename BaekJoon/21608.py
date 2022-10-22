import sys
from collections import deque
sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    students = [list(map(int,input().split())) for _ in range(n*n)]
    res = [[0] * n for _ in range(n)]
    
    dx = [1,-1,0,0]
    dy =[0,0,1,-1]
    for idx in range(n*n):
        student = students[idx]
        tmp = []
        for i in range(n):
            for j in range(n):
                if res[i][j] == 0:                   
                    friend = 0
                    empty = 0
                    for k in range(4):
                        x = i + dx[k]
                        y = j + dy[k]
                        if 0<=x<n and 0<=y<n:
                            if res[x][y] in student[1:]:
                                friend +=1
                            if res[x][y] == 0:
                                empty +=1
                    tmp.append([friend,empty,i,j])
        tmp.sort(key = lambda x: (-x[0],-x[1],x[2],x[3]))
        res[tmp[0][2]][tmp[0][3]] = student[0]
    
    total = 0
    students.sort(key = lambda x: x[0])
    for i in range(n):
        for j in range(n):
            cnt = 0
            for k in range(4):
                x = i + dx[k]
                y = j + dy[k]
                if 0<=x<n and 0<=y<n:
                    if res[x][y] in students[res[i][j]-1][1:]:
                        cnt +=1
            if cnt != 0:
                total += 10 ** (cnt -1)

    print(total)