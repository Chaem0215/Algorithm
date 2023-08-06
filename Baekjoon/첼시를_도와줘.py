# 브론즈2
# 첼시를 도와줘!
# https://www.acmicpc.net/problem/11098
# 23.08.04

import sys

n = int(sys.stdin.readline())

for _ in range(n):
    p = int(sys.stdin.readline())
    lists = [sys.stdin.readline().split() for _ in range(p)]
    player = [lists[0][0], lists[0][1]]
    for i in range(1, p):
        if int(player[0]) < int(lists[i][0]):
            player = [lists[i][0], lists[i][1]]
    print(player[1])