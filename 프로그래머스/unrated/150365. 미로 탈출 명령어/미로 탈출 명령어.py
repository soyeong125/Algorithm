from collections import deque
def solution(n, m, x, y, r, c, k):
    answer = 'impossible'
    #visited 체크 안해도됨 (해야됨 시간초과 어떻게 해결하지?)
    #bfs사용(x,y,cnt) cnt k이상이면 날려버리기
    #bfs 계속해서 cnt == k 이고 x,y가 r,c면 reslist에 넣기
    #reslist 갯수가 0 이면 임파서블 출력
    #reslist 정렬 0번째가 정답
    q = deque()
    q.append([x,y,0,''])
    dx = [1,0,0,-1]
    dy = [0,-1,1,0]
    dic = {0:'d',1:'l',2:'r',3:'u'}


    while q:
        xx,yy,cnt,arr = q.popleft()
        if cnt > k:
            continue
        if cnt == k:
            if (xx == r and yy == c):
                answer = arr
                break
        for s in range(4):
            sx = xx + dx[s]
            sy = yy + dy[s]
            if sx <= 0 or sx > n or sy <=0 or sy > m:
                continue
            if abs(sx - r) + abs(sy - c) + cnt + 1 > k:
                continue
            q.append([sx,sy,cnt+1,arr+dic[s]])
            break
                
                   
    return answer