# 실버4
# 주몽
# https://www.acmicpc.net/problem/1940
# 23.07.09

import sys
from bisect import bisect_right

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
lists = sorted(list(map(int, sys.stdin.readline().split())))
start, end, cnt = 0, N - 1, 0

while start < end:
    result = lists[start] + lists[end]
    if result < M: start += 1
    elif result > M: end -= 1
    else:
        start += 1
        end -= 1
        cnt += 1
print(cnt)


# 2. 런타임 에러
# import sys
# from bisect import bisect_right

# N = int(sys.stdin.readline())
# M = int(sys.stdin.readline())
# lists = list(map(int, sys.stdin.readline().split()))
# cnt = 0

# for i in lists:
#     if bisect_right(M - i, lists): cnt += 1

# print(cnt)



# 1. 시간초과
# import sys

# N = int(sys.stdin.readline())
# M = int(sys.stdin.readline())
# lists = list(map(int, sys.stdin.readline().split()))
# cnt = 0

# for i, v in enumerate(lists[:N-1]):
#     for j in lists[i+1:]:
#         if v + j == M: cnt += 1

# print(cnt)
