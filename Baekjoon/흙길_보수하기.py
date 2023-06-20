# 실버1
# 흙길 보수하기
# https://www.acmicpc.net/problem/1911
# 23.06.17

import sys

N, L = map(int, sys.stdin.readline().split())
lists = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
result = 0
end = 0

lists.sort()
print(lists)
for i in lists:
    if end > i[0]: i[0] = end
    
    if (i[1] - i[0]) % L == 0: result += (i[1] - i[0]) % 2
    else:
         result += (i[1] - i[0]) % 2 + 1
         end = i[1] - ((i[1] - i[0]) % 2) + L

print(result)



# 1. 시간 초과

# import sys

# N, L = map(int, sys.stdin.readline().split())
# lists = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# result = 0
# end = 0

# lists.sort()

# for i in lists:
#     if end > i[0]:
#         i[0] = end
#     while i[0] < i[1]:
#         result += 1
#         i[0] += L
#         end = i[0]

# print(result)