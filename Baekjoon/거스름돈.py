# 실버5
# 거스름돈
# https://www.acmicpc.net/problem/14916
# 23.07.17

import sys

n = int(sys.stdin.readline())
cnt = [0] * (n + 1)

for i in range(2, n + 1):
    cnt[i] = cnt[i - 1] + 1
    if i % 5 == 0:
        cnt[i] = min(cnt[i], cnt[i // 5] + 1)
    elif i % 2 == 0:
        cnt[i] = min(cnt[i], cnt[i // 2] + 1)

print(cnt[n])