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

#������ 

def isPrime (number):
    if number <= 1:
        return False
    for i in range(2,int(math.sqrt(number)+1)):
        if number % i ==0:
            return False
    return True


def solution(numbers):
    answer = 0
    #1. ���ڸ� ����Ʈȭ �ؼ� ������ ����� => list(numbers) ���̽��� ����
    #2. �� ������ ����ȭ�Ͽ� �ߺ��� �����Ѵ�.  -> set ���
    a = set()
    for i in range(1,len(numbers)+1):
            a |= set(map(int, map("".join,itertools.permutations(list(numbers),i))))
    #3. set �ȿ� ������ �� �Ҽ� Ž��
    for k in a:
        if isPrime (k):
            answer+=1
           
    return answer
