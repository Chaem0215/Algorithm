# 실버2
# 나무 자르기
# https://www.acmicpc.net/problem/2805
# 23.07.09

import sys

N, M = map(int, sys.stdin.readline().split())
lists = list(map(int, sys.stdin.readline().split()))
start, end = 1, max(lists)
# 이분탐색

while start <= end:
    mid = (start + end) // 2
    result = 0
    for i in lists: 
        if i >= mid: result += i - mid

    if result >= M: start = mid + 1
    else: end = mid - 1

print(end)