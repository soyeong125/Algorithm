import sys
import math
sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline


if __name__ == "__main__":
    a,b,c,m = map(int,input().split())
    cur = 0 
    work = 0
    for t in range(24):
        if cur + a <= m:
            work += b
            cur += a
        else:
            if cur - c >= 0:
                cur -= c
            else:
                cur = 0
    print(work)
