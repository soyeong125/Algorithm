import sys
sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline

if __name__ == "__main__":
    def solution(n,times):
        answer = 1000000000
        r = 1
        l = 1000000000
        times.sort()
        while r <= l :
            mid = (r + l)//2
            target = 0

            for i in times:
                target += ( mid // i )
            
            if target >= n :
                answer = min (answer, mid)
                l = mid - 1
            else:
                r = mid + 1          

        return answer
    
    print(solution(6,[7,10]))