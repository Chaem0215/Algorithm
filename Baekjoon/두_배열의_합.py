# 골드3
# 두 배열의 합
# https://www.acmicpc.net/problem/2143
# 23.06.21

import sys
from bisect import bisect_left

T = int(sys.stdin.readline())
n = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
B = list(map(int, sys.stdin.readline().split()))

print(T, n, A, m, B)