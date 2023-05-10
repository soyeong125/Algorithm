import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    schedule = []
    visited = [False for _ in range(n)]

    for _ in range(n):
        time, pay = map(int, input().split())
        schedule.append([time, pay])
    res = 0

    def dfs(today, total,lastdaypay):
        global res
        if today > n:
            res = max(res,total-lastdaypay)
            return
        elif today == n:
            res = max(res,total)
            return

        for i in range(today,n):
            if not visited[i]:
                visited[i] = True
                dfs(i + schedule[i][0], total + schedule[i][1],schedule[i][1])
                visited[i] = False

    dfs(0,0,0)
    print(res)