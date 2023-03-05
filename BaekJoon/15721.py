import sys
import math
sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline


if __name__ == "__main__":
    a = int(input())
    t = int(input())
    x = int(input())

    bundegi = []
    bun = degi = 1
    n = 0

    while 1:
        prebundegi = bun
        n +=1
        for _ in range(2):
            bundegi.append([bun,0])
            bun +=1
            bundegi.append([degi,1])
            degi +=1
        for _ in range(n+1):
            bundegi.append([bun,0])
            bun +=1
        for _ in range(n+1):
            bundegi.append([degi,1])
            degi +=1      
        if prebundegi < t <= bun:
            print(bundegi.index([t,x]) % a)
            break

