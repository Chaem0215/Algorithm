# 실버3
# 프린터 큐
# https://www.acmicpc.net/problem/1966
# 23.07.12

import sys

T = int(sys.stdin.readline())

for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())
    lists = list(map(int, sys.stdin.readline().strip().split()))
    cnt = 1
    dicts = {k: i for k, i in enumerate(lists)}

    while True:
        k = list(dicts.copy().keys())[0]
        max_v = max(dicts, key = dicts.get)
        print(list(dicts.values())[0])
        if max_v == M:
            break
        elif (lists[M] <= list(dicts.values())[0]) and max_v != M:
            dicts.pop(k)
            cnt += 1
            #print("pop = ", dicts)
        else: 
            dicts.update({k : dicts.pop(k)})
            #print("update = ", dicts)
    print(cnt)

# 3
# 1 0
# 5  >>> 1
# 4 2
# 1 2 3 4  >>> 2
# 6 0
# 1 1 9 1 1 1 >>> 5
