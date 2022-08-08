import sys
import math
sys.stdin = open("input.txt", 'r')


def dfs(result,op_list):
    global visited
    global n
    global max_answer
    global min_answer
    global num
    if sum(op_list) == 0:
        max_answer = max(max_answer,result)
        min_answer = min(min_answer,result)
        return
    for i in range(1,n):
        if not visited[i]:
            visited[i]=1
            for j in range(4):
                if op_list[j] > 0:
                    tmp_list = op_list[:]
                    tmp_list[j]-=1
                    if j==0:
                        dfs(result+num[i],tmp_list)                            
                    elif j==1:
                        dfs(result-num[i],tmp_list)                                               
                    elif j==2:  
                        dfs(result*num[i] ,tmp_list)                                                 
                    else:
                        dfs(int(result/num[i]),tmp_list)                                                          
            visited[i]=0    


if __name__ == "__main__":
    n = int(sys.stdin.readline())
    num = list(map(int,input().split()))  
    op_list = list(map(int,input().split())) 
    visited = [0 for i in range(n)]
    max_answer = -1000000
    min_answer = 1000000

    visited[0]=1
    dfs(num[0],op_list)

    print(max_answer)
    print(min_answer)
