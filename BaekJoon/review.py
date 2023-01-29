import sys
from itertools import combinations, permutations
sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    team = [i for i in range(n)]
    arr = [list(map(int,input().split())) for _ in range(n)]
    res = 100000
    for _ in range(n//2):
        for p in combinations(team,n//2):
            team1 = set(p)
            team2 = set(team) - team1
            tmp_sum1,tmp_sum2 = 0,0
            for k in permutations(team1,2):
                tmp_sum1 += arr[k[0]][k[1]]
            for k in permutations(team2,2):
                tmp_sum2 += arr[k[0]][k[1]]
            res = min(res,abs(tmp_sum1-tmp_sum2))
    print(res)
        

  







  



        





    