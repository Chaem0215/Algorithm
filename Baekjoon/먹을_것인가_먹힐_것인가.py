# 실버3
# 먹을 것인가 먹힐 것인가
# https://www.acmicpc.net/problem/7795
# 23.06.17

import sys

def toPointer(i, start, B):
    if start >= len(B): return len(B)
    if i <= B[start]: return len(B) - (len(B) - start)
    else: return toPointer(i, start + 1, B)

T = int(sys.stdin.readline())

for _ in range(T):
    result = 0
    N, M = map(int, sys.stdin.readline().split())
    A = sorted(list(map(int, sys.stdin.readline().split())))
    B = sorted(list(map(int, sys.stdin.readline().split())))

    for i in A:
        result += toPointer(i, 0, B)

    print(result)
    
    
# 1. 런타임 에러
# B의 길이는 최대 20,000개인데 파이썬 default 재귀 길이를 초과해서 런타임에러 뜬거같음.

# import sys

# def toPointer(i, start, B):
#     if start >= len(B): return len(B)
#     if i <= B[start]: return len(B) - (len(B) - start)
#     else: return toPointer(i, start + 1, B)

# T = int(sys.stdin.readline())

# for _ in range(T):
#     result = 0
#     N, M = map(int, sys.stdin.readline().split())
#     A = sorted(list(map(int, sys.stdin.readline().split())))
#     B = sorted(list(map(int, sys.stdin.readline().split())))

#     for i in A:
#         result += toPointer(i, 0, B)

#     print(result)