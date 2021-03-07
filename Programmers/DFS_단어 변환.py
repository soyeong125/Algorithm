import sys


def DFS(L,val,ch,begin,target, words):
    global answer
    if val==target:
        if answer> L:
            answer = L
            return
    else:
        for idx,k in enumerate(words):
            if ch[idx]==0:
                cnt=0
                for i in range(len(val)):
                        if val[i]==k[i]:
                            cnt+=1
                if len(val)-cnt ==1:
                        ch[idx]=1
                        DFS(L+1,k,ch,begin, target, words)
                        ch[idx]=0
                    
                
                
        
def solution(begin, target, words):
    global answer
    ch=[0]*len(words)
    if target in words:
       DFS(0,begin,ch, begin, target, words)
    else:
        answer = 0
    return answer

if __name__ == "__main__":
    answer = 2167000000

        
    #print(solution("hit","cog",["cog", "log", "lot", "dog", "dot", "hot"]))
    #print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"])) #4
    #print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"])) #0
    

    #print(solution("hit", "hot", ["hot", "dot", "dog", "lot", "log"])) #1
    #print(solution("1234567000", "1234567899", ["1234567800", "1234567890", "1234567899"])) #3
    print(solution("hit", "cog", ["cog", "log", "lot", "dog", "hot"])) #4
