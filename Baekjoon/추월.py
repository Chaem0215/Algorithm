# 실버1
# 추월
# https://www.acmicpc.net/problem/2002
# 23.05.18

import sys

N = int(sys.stdin.readline())
lists = [sys.stdin.readline().strip() for i in range(N * 2)]
count = 0

for i, v in enumerate(lists[:N]):
    if i > lists[N:].index(v):
        count += 1
print(count)