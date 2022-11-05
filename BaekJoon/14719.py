import sys
from collections import deque
sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline

if __name__ == "__main__":
    h,w = map(int,input().split())
    arr = list(map(int,input().split()))
    total = 0
    for i in range(1,w-1):
        left_max = max(arr[:i])
        right_max = max(arr[i+1:])

        compare = min(left_max,right_max)

        if arr[i] < compare:
            total += compare - arr[i]
    print(total)




