import sys
import math
from itertools import combinations
sys.stdin = open("input.txt", 'r')
sys.setrecursionlimit(10**6) 
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    start_team = list(i for i in range(n))
    arr = [list(map(int,input().split())) for _ in range(n)]
    res = 10**6



    for i in range(1,int(n/2 + 1)):
        mem_dive = combinations(start_team,i)
        for x in mem_dive:
            start_list = list(x)
            link_list = list(set(start_team) - set(start_list))
            start_p , link_p = 0, 0
            for j in range(n-1):
                for k in range(n-1):
                    try :
                            start_p += arr[start_list[j]][start_list[k]]
                    except IndexError:
                            start_p +=0
                    try :
                            link_p += arr[link_list[j]][link_list[k]]
                    except IndexError:
                            link_p +=0
            res = min(res,abs(start_p - link_p))
        
    print(res)


