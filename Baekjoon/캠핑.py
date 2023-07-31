# 브론즈 1
# 캠핑
# https://www.acmicpc.net/problem/4796
# 23.07.31

import sys
cnt = 0

while True:
    L, P, V = map(int, sys.stdin.readline().split())
    cnt += 1
    if L == 0 and P == 0 and V == 0:
        break

    print("Case {0}: {1}".format(cnt, V // P * L + ( L if V % P > L else V % P)))
