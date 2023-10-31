# 골드5
# 강의실 배정
# https://www.acmicpc.net/problem/11000
# 23.09.24

import sys

N = int(sys.stdin.readline())
lists = sorted([list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)], key=lambda x: x[0])

print(lists)