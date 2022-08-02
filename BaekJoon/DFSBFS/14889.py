import sys
from itertools import combinations, permutations
import math
sys.stdin = open("input.txt", 'r')
if __name__ == "__main__":
    n = int(sys.stdin.readline())
    player_value = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
    player = [i for i in range(n)]
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