import sys
from collections import deque
import heapq
sys.stdin = open("input.txt","rt")
 


def solution(answers):
    answer = [0]*4
    students = [[1,2,3,4,5],[2,1,2,3,2,4,2,5],[3,3,1,1,2,2,4,4,5,5]]
    tmp=[]
    for j in range(3):
        for i in range(len(answers)):
            if answers[i] == students[j][i%len(students[j])]:
                answer[j+1]+=1
    maxx=max(answer)
    for i,j in enumerate(answer):
        if j == maxx:
            tmp.append(i)
    return tmp
              


  

if __name__ == "__main__":
    print(solution([1, 3, 2, 4, 2]))
    
