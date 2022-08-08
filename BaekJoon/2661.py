import sys

sys.stdin = open("input.txt", 'r')


def dfs(depth,total,pluse,minus,multiply,divide):
    global max_answer
    global min_answer
    if depth == n:
        max_answer = max(max_answer,total)
        min_answer = min(min_answer,total)
        return
    if pluse:
        dfs(depth+1,total+num[depth],pluse-1,minus,multiply,divide)
    if minus:
        dfs(depth+1,total-num[depth],pluse,minus-1,multiply,divide)
    if multiply:
        dfs(depth+1,total*num[depth],pluse,minus,multiply-1,divide)
    if divide:
        dfs(depth+1,int(total/num[depth]),pluse,minus,multiply,divide-1)       


if __name__ == "__main__":
    n = int(sys.stdin.readline())
    num = list(map(int,input().split()))  
    op_list = list(map(int,input().split())) 
    visited = [0 for i in range(n)]
    max_answer = -1e9
    min_answer = 1e9

    dfs(1,num[0],op_list[0],op_list[1],op_list[2],op_list[3])

    print(max_answer)
    print(min_answer)
