def solution(participant, completion):
    answer = ''
    dic={}
    for p in participant:
        if p in dic:
            dic[p]+=1
        else:
            dic[p] = 1
    for c in completion:
        if c in dic:
            dic[c] -= 1
    for k,v in dic.items():
        if v > 0:
            answer = k
            break
    return answer
    



if __name__ =='__main__':
    print(solution(["leo", "kiki", "eden"],["eden", "kiki"]))


