import sys
from collections import deque
from xml.dom.minidom import Childless
sys.stdin = open("input.txt", 'r')

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def DFS(x,y):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False
    if apt[x][y]:
        global count
        count += 1
        apt[x][y]=0
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            DFS(nx,ny)
        return True
    return False

if __name__ == "__main__":
    n = int(input())
    apt = [list(map(int,input())) for i in range(n)]
    count = 0
    numlist = []
    result = 0

    for i in range(n):
        for j in range(n):
            if DFS(i,j) == True:
                numlist.append(count)
                result +=1
                count = 0
    numlist.sort()
    print(result)
    for i in range(result):
        print(numlist[i])
