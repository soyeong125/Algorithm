import sys
sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline


def combination(arr,r):
    for i in range(len(arr)):
        if r == 1:
            yield [arr[i]]
        else:
            for next in combination(arr[i:],r-1):
                yield [arr[i]] + next

if __name__ == "__main__":
    n,k = map(int,input().split())
    coin = [int(input()) for _ in range(n)]
    
