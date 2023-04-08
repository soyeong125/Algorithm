import sys
sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline

if __name__ == "__main__":
    def solution(distance,rocks,n):
        answer = 0
        rocks.append(distance)
        rocks.sort()

        l,r= 0 , distance
        answer = distance

        while l <= r:
            min_dist = float('inf')
            mid = (l+r) // 2
            target = 0
            start = 0

            for rock in rocks:
                diff = rock - start
                if diff < mid:
                    target +=1
                else:
                    start = rock
                    min_dist = min(min_dist,diff)
            
            if target > n :
                r = mid -1
                
            else:
                l = mid + 1
                answer = min_dist

        return answer

    print(solution(25,[2, 14, 11, 21, 17],2))