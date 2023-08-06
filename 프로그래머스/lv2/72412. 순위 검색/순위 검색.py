
import collections
def solution(info, query):
        #infomap[key]에 값을 추가해줍니다.
        infomap = collections.defaultdict(list)     
        
        # for inf in info:
        #     a,b,c,d,p = inf.split()
        #     infomap[''.join([a,b,c,d])].append(int(p))
        # 지원자의 정보로 가능한 모든 조합의 키를 생성해야 한다.
        for inf in info:
            a, b, c, d, p = inf.split()
        # 가능한 모든 조합 생성
            for l in [a, '-']:
                for m in [b, '-']:
                    for n in [c, '-']:
                        for o in [d, '-']:
                            infomap[l+m+n+o].append(int(p))        

        #이분탐색을 위해 infomap의 값들을 정렬합니다.
        for k in infomap:
            infomap[k].sort()

        # 이분탐색으로 point 이상의 값 개수를 구합니다.(효율성)
        answers = []
        for q in query:
            l, _, p, _, c, _, f, point = q.split()
            score_list = infomap[l + p + c + f]

            l,r = 0,len(score_list)

            while l < r:
                mid = (l+r) //2
                if score_list[mid] >= int(point):
                    r = mid
                else:
                    l = mid+1

            answers.append(len(score_list) - l)

        return(answers)
