import sys
input = sys.stdin.readline
if __name__ == "__main__":
    n,c = map(int,input().split())
    home = [int(input()) for _ in range(n)]
    home.sort()

    #이분탐색이 공유기 사이 최대 거리를 이분탐색 하는거임
    start = 1
    end = home[-1] - home[0]
    res = 0

    while start <= end:
        mid = (start + end)//2
        cur = home[0]
        cnt = 1

        for i in range(1,len(home)):
            if home[i] >= cur + mid:
                cnt +=1
                cur = home[i]
        if cnt >= c:
            start = mid + 1
            res = mid
        else:
            end = mid - 1
    print(res)