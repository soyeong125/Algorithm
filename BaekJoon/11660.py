import sys
sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline


if __name__ == "__main__":  
    n = int(input())
    numbers = [list(map(int,input().split())) for _ in range(n)]
    dp = ([[0] *(n+1) for _ in range(n+1)])
    for i in range(n):
        for j in range(n):
            dp[i+1][j+1] += numbers[i][j]
    print(dp)