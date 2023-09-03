import sys
import math

if __name__ == "__main__":
    n,n_atk = map(int,input().split())
    rooms = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

    max_hp = 0
    l , r = 1, int(1e18)

    while l <= r:
        mid = (l+r) // 2
        cur_hp = mid
        atk = n_atk

        for room in rooms:
            t, a, h = room[0], room[1], room[2]
            if t == 1:
                cur_hp -= (math.ceil(h / atk) - 1) * a
                if cur_hp <= 0:
                    break

            else:
                atk += a
                cur_hp = min(mid, cur_hp + h)

        if cur_hp <= 0:
            l = mid + 1
        else:
            r = mid - 1
            max_hp = mid

    print(max_hp)