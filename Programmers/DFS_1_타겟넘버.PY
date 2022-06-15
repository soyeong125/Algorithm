import math
sys.stdin = open("input.txt", 'r')

def DFS(sum, i,numbers,target):
     answer = 0
     if i == len(numbers):
         if sum == target:
             return 1
         else:
              return 0
     answer += DFS(sum + numbers[i],i+1,numbers,target)
     answer += DFS(sum - numbers[i],i+1,numbers,target)
   
def solution(numbers, target):    
    answer = DFS(0, 0,numbers,target)
    return answer
  

  
if __name__ =='__main__':
    print(solution([1, 1, 1, 1, 1],3))