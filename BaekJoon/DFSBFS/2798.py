import sys
from itertools import combinations
sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline


if __name__ == "__main__":  
    n,m = list(map(int,input().split()))
    arr = list(map(int,input().split()))
    res = -1000000
    for t in combinations(arr,3):
        tmp = sum(t)
        if tmp > res and tmp <= m:
            res = tmp
    print(res)
