import sys
from collections import deque
sys.stdin = open("input.txt", 'r')

if __name__ == "__main__":
    n = int(input())
    res = 0
    sum = 0 

    for i in range(1, n+1):
        sum += i
        res +=1
        if sum > n :
            res -=1
            break
    print(res)
