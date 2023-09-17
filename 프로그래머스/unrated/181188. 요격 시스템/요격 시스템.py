def solution(targets):
    answer = 0
    targets.sort(key = lambda x: (x[1],x[0]))
    E = 0
    
    for s,e in targets:
        if s >= E :
            E = e
            answer +=1
            
    return answer
