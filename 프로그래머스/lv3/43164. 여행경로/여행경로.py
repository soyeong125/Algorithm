import collections
def solution(tickets):
    answer = []
    dic = collections.defaultdict(list)
    for s,e in tickets:
        dic[s].append(e)
    
    for k,v in dic.items():
        v.sort()
    
    def dfs(start):
        if start in dic:
            while dic[start]:
                dfs(dic[start].pop(0))
        if start not in dic or len(dic[start]) == 0:
            answer.append(start)
            return
        
        answer.append(start)
    
    dfs('ICN')
    
    return answer[::-1]