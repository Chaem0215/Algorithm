# 실버4
# 제로
# https://www.acmicpc.net/problem/10773
# 23.07.10

import sys

K = int(sys.stdin.readline())
result = []

for _ in range(K):
    money = int(sys.stdin.readline())

    if money == 0: 
        try: result.pop()
        except: continue
    else: result.append(money)

print(sum(result))