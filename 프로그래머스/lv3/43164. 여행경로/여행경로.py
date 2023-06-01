def solution(tickets):
        answer = []
        dic = {}

        def dfs(start):
            if start in dic:
                while dic[start]:
                    dfs(dic[start].pop(0))

            if start not in dic or not dic[start]:
                answer.append(start)
                return


        for a, b in tickets:
            if a not in dic:
                dic[a] = [b]
            else:
                dic[a].append(b)
        for a in dic.keys():
            dic[a].sort()

        dfs("ICN")

        return answer[::-1]