import sys
from itertools import combinations, permutations
import math
sys.stdin = open("input.txt", 'r')

if __name__ == "__main__":
    n = int(input())
    player = [i for i in range(n)]
    player_value = [list(map(int,input().split())) for _ in range(n)]
    answer = float('Inf')
    team1 = []
    
    for i in combinations(player,n//2):
        team1.append(list(i))
    
    for i in team1:
        team2 = []
        g1, g2 = 0, 0 
        for k in range(n):
            if k not in i:
                team2.append(k)
        for x in range(n//2):
            for y in range(x+1,n//2):
                g1 += player_value[i[x]][i[y]] + player_value[i[y]][i[x]]
        for x in range(n//2):
            for y in range(x+1,n//2):
                g2 += player_value[team2[x]][team2[y]] + player_value[team2[y]][team2[x]]
        answer = min(answer, abs(g1-g2))
    print(answer)

    # for i in combinations(player,n):
    #     g1,g2 = 0, 0
    #     for n1 in range(n//2):
    #         for n2 in range(n1,n//2):
    #             g1+= player_value[i[n1]][i[n2]]+player_value[i[n2]][i[n1]]
    #     for n1 in range(n//2,n):
    #         for n2 in range(n1,n):
    #             g2+= player_value[i[n1]][i[n2]]+player_value[i[n2]][i[n1]]
    #     answer = min(answer, abs(g1-g2))
    # print(answer)

#조합으로 가능한 팀 생성해주기
    # for team in list(combinations(members, N)):
    #     possible_team.append(team)
    # print(possible_team)
    # for team in list(permutations(members, N)):
    #     possible_team2.append(team)
    # print(possible_team2)
    # player = [i for i in range(n)]
    # answer = 1000000
    
    # for i in permutations(player,n):
    #     g1,g2 = 0, 0
    #     for n1 in range(n//2):
    #         for n2 in range(n1,n//2):
    #             g1+= player_value[i[n1]][i[n2]]+player_value[i[n2]][i[n1]]
    #     for n1 in range(n//2,n):
    #         for n2 in range(n1,n):
    #             g2+= player_value[i[n1]][i[n2]]+player_value[i[n2]][i[n1]]
    #     answer = min(answer, abs(g1-g2))
    # print(answer)

    # n = int(input())
    # player_value = [list(map(int,input().split())) for _ in range(n)]
    # answer = float('Inf')
    # visited = [0 for i in range(n)]
    # stack = []
    # def DFS(idx):
    #     global answer
    #     global visited
    #     global stack
    #     if idx == n//2:
    #         g1,g2 =0,0
    #         team1 = []
    #         team2 = []
    #         for i in range(n):
    #             if i in stack:
    #                 team1.append(i)
    #             else:
    #                 team2.append(i)
    #         for n1 in range(n//2):
    #             for n2 in range(n1+1,n//2):
    #                 g1 += player_value[team1[n1]][team1[n2]] + player_value[team1[n2]][team1[n1]]
    #                 g2 += player_value[team2[n1]][team1[n2]] + player_value[team2[n2]][team1[n1]]
    #         answer = min(answer, abs(g1-g2))
    #         return
    #     for i in range(n):
    #         if i in stack:continue
    #         if len(stack) > 0 and stack[-1] > i :continue
    #         stack.append(i)
    #         DFS(idx+1)
    #         stack.pop()
    # DFS(0)
    # print(answer)

            

 