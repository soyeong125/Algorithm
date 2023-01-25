import sys
from itertools import permutations
sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    arr = list(map(int,input().split()))
    res = -100000
    for p in permutations(arr,n):
        tmp = 0
        for i in range(n-1):
            tmp += abs(p[i]-p[i+1]) 
        res = max(res,tmp)
    print(res)
        

  







  



        





    