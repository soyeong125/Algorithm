from collections import deque
def solution(n, m, x, y, r, c, k):
    answer = 'impossible'

    dd = ["d","l","r","u"]
    dx = [1,0,0,-1]
    dy = [0,-1,1,0]
    
    q = deque()
    q.append([x,y,0,""])
    
    while q:
        x1,y1,cnt,tmp = q.popleft()
        if (x1 == r and y1 == c) and cnt == k:
            answer = tmp
            break
            
        if cnt >= k:
            continue
            
        for kk in range(4):
            xx = x1 + dx[kk]
            yy = y1 + dy[kk]
            if 0<xx<=n and 0<yy<=m:
                if abs(xx-r) + abs(yy-c) + cnt + 1 <= k:
                    q.append([xx,yy,cnt+1,tmp+dd[kk]])
                    break
                               
    return answer


