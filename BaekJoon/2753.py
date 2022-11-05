import sys
from collections import deque
sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline

if __name__ == "__main__":  
    dic = {}
    dic[1] = 1
    dic[2] = 1
    dic[3] = [4,5]

    if 4 in dic[3]:
        print("yes")
    else:
        print("no")
    