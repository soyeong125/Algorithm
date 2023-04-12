if __name__ == "__main__":
    n = int(input())
    dp = [1] * (n+1)
    for i in range(3,n+1):
        dp[i] = dp[i-2] + dp[i-1]
    print(dp[n])