# 실버4
# 제로
# https://www.acmicpc.net/problem/10773
# 23.07.10

import sys

K = int(sys.stdin.readline())
result = []

for _ in range(K):
    money = int(sys.stdin.readline())

    if money == 0: # 0이면 값을 꺼냄
        try: result.pop()
        except: continue # result에 값이 없다면 패스
    else: result.append(money) # 0이 아니면 값 집어넣음

print(sum(result))