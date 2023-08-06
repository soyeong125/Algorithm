
import collections
def solution(info, query):
        infomap = collections.defaultdict(list)
       #infomap[key]에 값을 추가해줍니다.
        for inf in info:
            a,b,c,d,p = inf.split()
            infomap[''.join([a,b,c,d])].append(int(p))
                

        #이분탐색을 위해 infomap의 값들을 정렬합니다.
        for k in infomap:
            infomap[k].sort()

        # 이분탐색으로 point 이상의 값 개수를 구합니다.(효율성)
        answers = []
        for q in query:
            l, _, p, _, c, _, f, point = q.split()
            key = infomap[''.join([l, p, c, f])]

            l,r = 0,len(key)

            while l < r:
                mid = (l+r) //2
                if key[mid] >= int(point):
                    r = mid-1
                else:
                    l = mid+1

            answers.append(len(key) - l)

        return(answers)
