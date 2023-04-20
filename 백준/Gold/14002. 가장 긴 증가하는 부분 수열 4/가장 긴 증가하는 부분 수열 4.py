if __name__ == "__main__":
    n = int(input())
    arr = list(map(int,input().split()))
    dp = [0 for _ in range(n)]

    for i in range(n):
        for j in range(i):
            if arr[i] > arr[j] and dp[j] > dp[i]:
                dp[i] = dp[j]
        dp[i] +=1
    cur = max(dp)
    print(cur)
    res = []
    for i in range(n-1,-1,-1):
        if dp[i] == cur:
            res.append(arr[i])
            cur -=1
        if cur == 0:
            break
    for i in res[::-1]:
        print(i,end=' ')