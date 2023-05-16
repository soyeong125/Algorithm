import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(n)] #상담에 걸리는 시간, 상담 비용
    dp = [0] * (n+1)

    for day in range(n-1,-1,-1):
        if day + arr[day][0] > n : #현재 날짜와 상담 날짜를 더해서 퇴사날이면 못함
            dp[day] = dp[day+1]
        else:
            dp[day] = max(dp[day+1],dp[day+arr[day][0]] + arr[day][1]) #상담을 했을 때 비용과 상담 안했을 때 지금까지 누적값중 더 큰 값으로 교체

    print(dp[0])