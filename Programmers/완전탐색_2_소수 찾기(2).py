import itertools
import math

def solution(numbers):
    #1. 문자를 리스트화 해서 순열로 만든다
    answer = 0
    a = list(numbers)
    ap = list()
    for i in range(1,len(a)+1):
        ap.extend(list(itertools.permutations(a,i)))
    #2. 각 순열을 정수화하여 중복을 제거한다.  -> set 사용
    bp = set()
    s = ""     
    for i in ap:
        for j in i:
            s+=j
        bp.add(int(s))
        s=""
    #3. set 안에 정수들 중 소수 탐색
    for k in bp:
        check = True
        if k < 2 :
            continue
        for kk in range(2,int(math.sqrt(k) +1)):
            if k%kk==0:
                check = False
        if check : answer+=1
           
    return answer
