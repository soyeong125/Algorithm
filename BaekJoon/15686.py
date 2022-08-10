import sys
import math
from itertools import combinations
sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline
if __name__ == "__main__":
    n,m = map(int,input().split())
    cmap = [list(map(int,input().split())) for i in range(n)]
    chicken = []
    result = 10000000
    #치킨집 찾기
    for i in range(n):
        for j in range(n):
            if cmap[i][j]==2:
                chicken.append([i,j])
    #폐업안할 치킨집으로 최단거리 탐색
    for i in combinations(chicken,m):
        combi_result = 0
        for x in range(n):
            for y in range(n):         
                if cmap[x][y] == 1:
                    tmp_result = 1e9
                    for chick in i:
                        tmp_result = min(tmp_result,abs(chick[0]-x) + abs(chick[1]-y))
                else:
                    continue
                combi_result += tmp_result
        result = min(result,combi_result)
    print(result)



    
