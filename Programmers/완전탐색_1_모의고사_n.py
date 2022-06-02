import sys
sys.stdin = open("input.txt", 'r')

def solution(answers):
    answer = [0,0,0]
    supo = [[1,2,3,4,5],
            [2,1,2,3,2,4,2,5],
            [3,3,1,1,2,2,4,4,5,5]]
    rr = []
    for i in range(len(supo)):
        supo_answer = supo[i]
        for j in range(len(answers)):
            if(supo_answer[j%len(supo[i])] == answers[j]):
                answer[i] += 1
    for idx,value in enumerate(answers):
        if supo[0][idx%len(supo[0])] == value:
            answer[0] +=1
        if supo[1][idx%len(supo[1])] == value:
            answer[1] +=1
        if supo[2][idx%len(supo[2])] == value:
            answer[2] +=1

    for k in range(len(answer)):
        if answer[k] == max(answer):
            rr.append(k+1)
    return rr


def solution(answers):
    answer = [0,0,0]
    supo = [[1,2,3,4,5],
            [2,1,2,3,2,4,2,5],
            [3,3,1,1,2,2,4,4,5,5]]
    rr = []
    for idx,value in enumerate(answers): #개선사항 > 이중포문 해지, enumerate 사용
        if supo[0][idx%len(supo[0])] == value:
            answer[0] +=1
        if supo[1][idx%len(supo[1])] == value:
            answer[1] +=1
        if supo[2][idx%len(supo[2])] == value:
            answer[2] +=1

    for i, v in enumerate(answer):
        if max(answer) == v:
            rr.append(i+1)
    return rr