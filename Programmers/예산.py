import sys
input = sys.stdin.readline

if __name__ == "__main__":
    
    def solution(d, budget):
        d.sort()
        res = 0
        cnt = 0

        for i in d:
            res += i
            cnt += 1
            if res > budget:
                cnt -= 1
                break
        
        return cnt

    
    

    print(solution([1,3,2,5,4], 9))
    print(solution([2,2,3,3], 10))