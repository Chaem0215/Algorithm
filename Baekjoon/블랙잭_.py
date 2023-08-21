# 브론즈 2
# 블랙잭
# https://www.acmicpc.net/problem/2798
# 23.08.08

import sys, itertools

# 396ms
N, M = map(int, sys.stdin.readline().split())
lists = list(map(int, sys.stdin.readline().split()))
max_num = 0

for i in list(itertools.permutations(lists, 3)):
    total = sum(i)
    if M >= total and max_num < total: max_num = total

print(max_num)



# 다른 사람 풀이 // 124ms
# N, M = map(int, input().split())
# lst = list(map(int, input().split()))
# nlst = []
# for i in range(N):
#     for j in range(i+1, N):
#         for k in range(j+1, N):
#             three =  lst[i] + lst[j] + lst[k]
#             if three > M:
#                 continue
#             else:
#                 nlst.append(three)
# print(max(nlst))