import sys
from itertools import permutations
import math
sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline


if __name__ == "__main__":  
    n = int(input())
    array = list(map(int,input().split()))
    answer = 0
    for t in permutations(array,n):
        tmp = 0
        for i in range(n-1):
            tmp += abs(t[i]-t[i-1])
            answer = max(answer,tmp)
    print(answer)