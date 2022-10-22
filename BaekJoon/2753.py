import sys
from collections import deque
sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline

if __name__ == "__main__":  
    n = int(input())

    if n % 4 == 0:
        if not n%100 == 0 or n%400 == 0:
            print(1)
        else:
            print(0)
    else:
        print(0)