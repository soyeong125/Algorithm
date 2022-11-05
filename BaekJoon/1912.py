import sys
sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline

if __name__ == "__main__":  
    n = int(input())
    arr = list(map(int,input().split()))
    res = -100000
    psum = 0
    for i in range(n):
        psum = max(psum,0) + arr[i]
        res = max(res,psum)

    print(res)