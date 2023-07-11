# 브론즈2
# 공 바꾸기
# https://www.acmicpc.net/problem/10813
# 23.07.11

import sys

N, M = map(int, sys.stdin.readline().split())
lists = list(list(map(int, sys.stdin.readline().split())) for _ in range(M))
result = list(i + 1 for i in range(N))

for i, j in lists:
    result[j - 1], result[i - 1] = result[i - 1], result[j - 1]

print(*result)


# 다른 사람 풀이
N, M = map(int, sys.stdin.readline().split())

result = [i for i in range(1,N+1)]

for i in range(M):
    i, j = map(int, input().split())
    result[i - 1], result[j - 1] = result[j - 1], result[i - 1]

print(*result)