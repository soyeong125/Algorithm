import itertools
import math

def solution(numbers):
    #1. ���ڸ� ����Ʈȭ �ؼ� ������ �����
    answer = 0
    a = list(numbers)
    ap = list()
    for i in range(1,len(a)+1):
        ap.extend(list(itertools.permutations(a,i)))
    #2. �� ������ ����ȭ�Ͽ� �ߺ��� �����Ѵ�.  -> set ���
    bp = set()
    s = ""     
    for i in ap:
        for j in i:
            s+=j
        bp.add(int(s))
        s=""
    #3. set �ȿ� ������ �� �Ҽ� Ž��
    for k in bp:
        check = True
        if k < 2 :
            continue
        for kk in range(2,int(math.sqrt(k) +1)):
            if k%kk==0:
                check = False
        if check : answer+=1
           
    return answer
