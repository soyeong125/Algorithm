import bisect, itertools, collections
def solution(info, query):
        infomap = collections.defaultdict(list)
        binarys = list(itertools.product((True, False), repeat=4))

        #하나의 info에서 나올 수 있는 16가지의 key를 만들어서 infomap[key]에 값을 추가해줍니다.
        for inf in info:
            inf = inf.split()
            for binary in binarys:
                key = ''.join([inf[i] if binary[i] else '-' for i in range(4)])
                infomap[key].append(int(inf[4]))
        #이분탐색을 위해 infomap의 값들을 정렬합니다.
        for k in infomap.keys():
            infomap[k].sort()

        #query의 값을 key로 만들고 이분탐색으로 point 이상의 값 개수를 구합니다.
        answers = []
        for q in query:
            l, _, p, _, c, _, f, point = q.split()
            key = ''.join([l, p, c, f])
            i = bisect.bisect_left(infomap[key], int(point))
            answers.append(len(infomap[key]) - i)

        return(answers)