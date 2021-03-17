from collections import deque

def DFS(L,total,numbers, target):
    global answer
    if L==len(numbers):
            if total==target:
                    answer+=1
                    return
            else:
                    return 
    DFS(L+1,total+numbers[L],numbers, target)
    DFS(L+1,total-numbers[L],numbers,target)
        
def solution(numbers, target): 
    global answer
    answer=0
    DFS(0,0,numbers, target)
    return answer

if __name__=="__main__":
    print(solution([1, 1, 1, 1, 1], 3))