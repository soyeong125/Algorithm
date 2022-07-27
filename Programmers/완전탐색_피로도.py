answer = 0
n = 0
visited = []
def DFS(k,cnt,dungeons):
    global answer
    if cnt > answer:
        answer = cnt
    for i in range(n):
        if dungeons[i][0] <= k and not visited[i]:
            visited[i]=1
            DFS(k-dungeons[i][1] ,cnt+1,dungeons)
            visited[i]=0

def solution(k, dungeons):
    global n, visited
    n = len(dungeons)
    visited = [0] * n
    DFS(k,0,dungeons)
    
                    
    return answer
