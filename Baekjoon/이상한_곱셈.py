# 브론즈2
# 이상한 곱셈
# acmicpc.net/problem/1225
# 23.08.01

import sys
A, B = sys.stdin.readline().split()

A = list(map(int, A))
B = list(map(int, B))
print(sum(A) * sum(B))


# 1. 시간 초과
# import sys

# A, B = sys.stdin.readline().split()
# result = 0

# for i in A:
#     for j in B:
#         result += int(i) * int(j)
# print(result)