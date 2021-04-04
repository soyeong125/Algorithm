import sys
from collections import deque
import heapq
sys.stdin = open("input.txt","rt")
 


def solution(numbers):
    answer = 0
    valist=[]
    ch=[0]*len(numbers)
    def DFS(L,ch,valist):
        if L==len(numbers):
            tmp=[]
            val=0
            for j in range(len(ch)):
                if ch[j]==1:
                    tmp.append(numbers[j])
            for k in range(len(tmp)):
                val+=(10**(len(tmp)-k-1))*int(tmp[k])
            if val == 0 or val ==1:
                return
            if val not in valist:
                if val%10==2 or val%10==5 or val%10==7 or val%10==9:
                    valist.append(val)
        else:
            for i in range(len(numbers)):
                if ch[i]==0:
                    ch[i]=1
                    DFS(L+1,ch,valist)
                    ch[i]=0
                    DFS(L+1,ch,valist)

    for i in range(len(numbers)):
            DFS(0,ch,valist)

    answer = len(valist)
    return answer
              


  

if __name__ == "__main__":
    print(solution("17"))
    
