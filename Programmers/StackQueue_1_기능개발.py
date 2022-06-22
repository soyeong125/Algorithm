from collections import deque
def solution(progresses, speeds):
    answer = []
    deploy = deque()
    for i in range(len(progresses)):
        z = (100 -progresses[i])//speeds[i]
        x = (100 -progresses[i])%speeds[i]
        if x :
            deploy.append(z+1)
        else:
            deploy.append(z)
    while deploy:
        cur = deploy[0]
        a = 0
        while cur >= deploy[0] and deploy:
                deploy.popleft()
                a += 1
                if not deploy:
                    break
        answer.append(a)

        
    return answer