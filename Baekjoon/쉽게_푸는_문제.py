# 브론즈1
# 쉽게 푸는 문제
# https://www.acmicpc.net/problem/1292
# 23.07.26

import sys

A, B = map(int, sys.stdin.readline().split())
lists = []
cnt = 0

while len(lists) <= B: # lists에 cnt 값을 담는 중인데 lists가 B를 넘으면 그 이후부터 필요 없으니 걸어줌.
    cnt += 1
    for i in range(cnt): lists.append(cnt)

print(sum(lists[A - 1 : B]))