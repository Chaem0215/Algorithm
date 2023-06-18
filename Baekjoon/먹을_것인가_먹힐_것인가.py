# 실버3
# 먹을 것인가 먹힐 것인가
# https://www.acmicpc.net/problem/7795
# 23.06.17

import sys

def toPointer(A, B, start, end):

    return result

T = int(sys.stdin.readline())

for _ in range(T):
    result = 0
    N, M = map(int, sys.stdin.readline().split())
    A = list(map(int, sys.stdin.readline().split()))
    B = list(map(int, sys.stdin.readline().split()))

    result = toPointer(A, B, 0, 0)

    print(result)