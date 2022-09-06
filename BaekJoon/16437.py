from asyncio.windows_events import NULL
import sys
from collections import deque
sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline
sys.setrecursionlimit(100000)

if __name__ == "__main__":
    n = int(input())
    area = [[]] * (n+2)
    s = deque()
    result = 0

    def DFS(cur,cnt,connect):
        global result
        if cnt <= 0 :
            return
        if cur == 1:
            result += cnt
            return
        if area[connect][0] == 'W': #늑대인 경우         
            cnt = cnt - area[connect][1]
            DFS(connect,cnt,area[connect][2])
        if area[connect][0] == 'S': #양인 경우         
            DFS(connect,cnt,area[connect][2])            
    area[1] = ['S',0,1]
    for i in range(n-1):
        x = list(input().split())
        if x[0] == 'S':
            s.append([i+2,int(x[1]),int(x[2])])
            area[i+2] = ['S',int(x[1]),int(x[2])]
        if x[0] == 'W':
            area[i+2] = ['W',int(x[1]),int(x[2])]
    while s:
        cur,cnt,connect = s.pop()
        DFS(cur,cnt,connect) 
    print(result)       


        
