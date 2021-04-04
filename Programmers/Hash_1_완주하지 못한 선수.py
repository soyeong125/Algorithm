import sys
from collections import deque
sys.stdin = open("input.txt","rt")
#3:17 ~ 3:36
def solution(participant, completion):
    answer = ''
    p={}
    for i in participant:
        if i in p:
            p[i].append(0)
        else:
            p[i]=[0]

    for j in completion:
        if j in p:
            for h in range(len(p[j])):
                if p[j][h] ==0:
                    p[j][h]=1
                    break

    for k,v in p.items():
        if len(v)>1 and sum(v)<len(v):
            answer = k
            break
        else:
            if sum(v)==0:
                answer=k
                break

    return answer



if __name__ == "__main__":
    print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))
    print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))
    

    
