import sys
if __name__ == "__main__":
    n,k = map(int,input().split())
    convey = list(map(int,input().split()))
    robot = [0] * n
    res = 1

    while 1:
        #1 컨테이너 벨트 + 로봇 한바퀴 돌리기
        last = convey.pop()
        convey.insert(0,last)
        robot.pop()
        robot.insert(0, 0)
        if robot[n-1]:
            robot[n-1] = 0


        #2 로봇 회전
        for i in range(n-1,0,-1):
            if convey[i] > 0 and not robot[i] and robot[i-1]:
                robot[i] = 1
                robot[i-1] = 0
                convey[i] -=1

        if convey[0] > 0:
            convey[0] -=1
            robot[0] = 1

        if convey.count(0) >= k:
            break
        res +=1
    print(res)