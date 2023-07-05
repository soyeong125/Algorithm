import sys
input = sys.stdin.readline
if __name__ == "__main__":
    n = int(input())
    dic = {}
    for _ in range(n):
        name = input().rstrip()
        if name[0] not in dic:
            dic[name[0]] = 1
        else:
            dic[name[0]] +=1
            
    res = []
    for k,v in dic.items():
        if v >= 5:
            res.append(k)
    if len(res) > 0:
        res.sort()
        print(''.join(res))
    else:
        print('PREDAJA')