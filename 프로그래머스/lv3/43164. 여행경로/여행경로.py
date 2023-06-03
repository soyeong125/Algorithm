import collections
def solution(tickets):
        answer = []
        dic = collections.defaultdict(list)
        visited = collections.defaultdict(list)

        for s, e in tickets:
            dic[s].append(e)
            visited[s].append(0)
        for k, v in dic.items():
            dic[k].sort()

        def dfs(l,start,tmp):
            if l == len(tickets):
                answer.append(tmp)
                return
            if l >= len(tickets):
                return

            for i in range(len(dic[start])):
                if not visited[start][i]:
                    visited[start][i] = 1
                    dfs(l+1,dic[start][i],tmp+[dic[start][i]])
                    visited[start][i] = 0

        dfs(0,'ICN',['ICN'])

        return answer[0]