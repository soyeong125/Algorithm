def solution(stones, k):
        l,r = 1,200000000
        answer = 0
        while l <= r:
            mid = (l+r)//2
            tmp_cnt = 0
            for s in stones:
                if s - mid <= 0 :
                    tmp_cnt +=1
                else:
                    tmp_cnt = 0
                if tmp_cnt >= k:
                    break
            if tmp_cnt >= k:
                r = mid -1
            else:
                l =mid + 1 

        answer = l
        return answer