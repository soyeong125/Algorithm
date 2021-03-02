import sys

def solution(clothes):
    answer = 1
    dic={}
    for k in clothes:
             if k[1] not in dic:
                dic[k[1]]=1
             else:
                dic[k[1]]+=1
    for k in dic.values():
        answer*=(k+1)
    return answer-1

if __name__ == "__main__":
   print(solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]))
   