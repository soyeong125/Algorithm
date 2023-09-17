def solution(targets):
    answer = 1
    targets.sort(key = lambda x: (x[1],x[0]))
    E = targets[0][1]
    for s,e in targets:
        if s >= E :
            E = e
            answer +=1
    return answer
