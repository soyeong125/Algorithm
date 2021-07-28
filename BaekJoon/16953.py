import sys
sys.stdin=open("input.txt","rt")

def solution(n, lost, reserve):
    ch_lost=[1]*len(lost)
    ch_reserve=[0]*(len(reserve))
    
    for i in range(len(lost)):
        for j in range(len(reserve)):
            if lost[i]==reserve[j] and ch_reserve[j]==0:
                ch_reserve[j]=1
                ch_lost[i]=0
                break


    for i in range(len(lost)):
        if ch_lost[i]==1:
             for j in range(len(reserve)):
                    if (reserve[j]==lost[i]-1 or reserve[j]==lost[i]+1) and ch_reserve[j]==0 :
                            ch_lost[i]=0
                            ch_reserve[j]=1

    return n - sum(ch_lost)