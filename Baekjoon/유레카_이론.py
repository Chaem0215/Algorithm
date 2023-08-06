# 브론즈1
# 유레카 이론
# https://www.acmicpc.net/problem/10448
# 23.08.06


# 시간 968ms
import sys

T = int(sys.stdin.readline())
lists = list(i * (i + 1) // 2 for i in range(1, 45))
result = []

for i in lists:
   for j in lists:
      for k in lists:
         result.append(i + j + k)

for i in range(T):
   K = int(sys.stdin.readline())
   print(1 if result.count(K) else 0)



# 다른 사람 풀이 / 시간 : 228ms
# num = [i * (i + 1) // 2 for i in range(1, 46)]
# a = [0] * 1001

# for i in num:
#     for j in num:
#         for k in num:
#             n = i + j + k
#             if n <= 1000:
#                 a[n] = 1

# for i in range(int(input())):
#     print(a[int(input())])