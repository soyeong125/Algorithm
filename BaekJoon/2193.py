import sys
sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline

if __name__ == "__main__":  
        n = int(input())
        dp = [0] * (n+1)

        dp[1] = 1
        dp[2] = 1

        for i in range(3,n+1):
            dp[i] = dp[i-1] + dp[i-2]
        print(dp[n])