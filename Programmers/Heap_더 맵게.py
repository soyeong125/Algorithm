import sys
from collections import deque
import heapq
sys.stdin = open("input.txt","rt")
 


def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)   

    while scoville[0] < K:
        val = heapq.heappop(scoville) + (heapq.heappop(scoville)*2)
        heapq.heappush(scoville,val)
        answer+=1

        if len(scoville)==1 and scoville[0] < K:
            return -1
     
    return answer
              


  

if __name__ == "__main__":
    print(solution([1,2,3,9,10,12],7))
    
print(solution([1, 1, 1], 4), 2)
print(solution([10, 10, 10, 10, 10], 100), 4)
print(solution([1, 2, 3, 9, 10, 12], 7), 2)
print(solution([0, 2, 3, 9, 10, 12], 7), 2)
print(solution([0, 0, 3, 9, 10, 12], 7), 3)
print(solution([0, 0, 0, 0], 7), -1)
print(solution([0, 0, 3, 9, 10, 12], 7000), -1)
print(solution([0, 0, 3, 9, 10, 12], 0), 0)
print(solution([0, 0, 3, 9, 10, 12], 1), 2)
print(solution([0, 0], 0), 0)
print(solution([0, 0], 1), -1)
print(solution([1, 0], 1), 1)