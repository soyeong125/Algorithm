import sys
sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline


if __name__ == "__main__":  
    n = int(input())
    arr = list(map(int,input().split()))
    dp = [1] * n
    max_value = 0
    result = []

    for i in range(n):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[j]+1,dp[i])
    max_value = max(dp)
    print(max_value)
    idx = dp.index(max_value)

    while idx >= 0:
        if dp[idx] == max_value:
            result.append(arr[idx])
            max_value-=1
        idx-=1
    for num in result[::-1]:
        print(num,end = ' ')
        
    



    