# 실버3
# 스파이
# https://www.acmicpc.net/problem/28075
# 23.07.09

import sys

N, M = map(int, sys.stdin.readline().split())
collect_list = list(map(int, sys.stdin.readline().split()))
watch_list = list(map(int, sys.stdin.readline().split()))

# 부르트포스 알고리즘

def slove(day, sum, place):
    if day == N: return
    