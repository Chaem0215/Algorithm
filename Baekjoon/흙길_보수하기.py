# 실버1
# 흙길 보수하기
# https://www.acmicpc.net/problem/1911
# 23.06.17

import sys

N, L = map(int, sys.stdin.readline().split())
result = 0

for _ in range(N):
    i, j = map(int, sys.stdin.readline().split())
    result += (j - i)

print((result // L) + 1 if result % L > 0 else result // L)