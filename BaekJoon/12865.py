import sys
sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline

if __name__ == "__main__":  
    n,k = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(n)]
    arr.sort(key=lambda x:(x[0],x[1]))
    minweight = arr[0][0]
    dp = [0] * 1000000

    for weight in range(minweight,k+1):
        curval = 0
        curweight = 0
        for w,v in arr:
            if w > weight:
                break
            if curweight + w > k:
                curval = max(curval,v)
            if w < weight and curweight + w <= k:
                curval += v
                curweight += w
        
        for i in range(minweight,weight//2+1):
            curval = max(curval,dp[i] + dp[weight - i])
        dp[weight] = curval
    print(dp[k])

    

    