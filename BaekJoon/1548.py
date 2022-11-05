import sys
from itertools import combinations
sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    arr = list(map(int,input().split()))
    res = 0
    for k in combinations(arr,3):
        a,b,c = k[0],k[1],k[2]
        print(a,b,c)
    #     if a+b > c:
    #         res +=1
    # print(res)
    
