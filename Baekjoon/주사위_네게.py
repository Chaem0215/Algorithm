# 브론즈 2
# 주사위 네개
# https://www.acmicpc.net/problem/2484
# 23.08.26

import sys
from collections import Counter

N = int(sys.stdin.readline())
lists = [list(sys.stdin.readline().split()) for _ in range(N)]
money = []

for i in lists:
    cnt = sorted(Counter(i).items(), key=lambda x: x[1], reverse=True)
    tmp, dup = 0, 0

    for key, val in cnt:
        if val == 4:
            tmp = 50000 + int(key) * 5000
        elif val == 3:
            tmp = 10000 + int(key) * 1000
        elif val == 2:
            tmp = 1000 + int(key) * 100
            dup = int(key)
        elif val == 2 and dup > 0:
            tmp = 2000 + dup * 500 + key * 500
        else:
            tmp = int(max(i)) * 100
    money.append(tmp)
print(max(money))
