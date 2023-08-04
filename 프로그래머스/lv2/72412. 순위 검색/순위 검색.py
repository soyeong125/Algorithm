
import collections
def solution(info, query):
        infomap = collections.defaultdict(list)
        #하나의 info에서 나올 수 있는 16가지의 key를 만들어서 infomap[key]에 값을 추가해줍니다.
        for inf in info:
            i = inf.split()
            for a in [i[0],'-']:
                for b in [i[1], '-']:
                    for c in [i[2], '-']:
                        for d in [i[3],'-']:
                            infomap[(a,b,c,d)].append(int(i[4]))

        #이분탐색을 위해 infomap의 값들을 정렬합니다.
        for k in infomap:
            infomap[k].sort()

        # 이분탐색으로 point 이상의 값 개수를 구합니다.
        answers = []
        for q in query:
            l, _, p, _, c, _, f, point = q.split()
            key = infomap[(l, p, c, f)]

            l,r = 0,len(key)

            while l < r:
                mid = (l+r) //2
                if key[mid] >= int(point):
                    r = mid 
                else:
                    l = mid+1

            answers.append(len(key) - l)

        return(answers)