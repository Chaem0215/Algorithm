# 실버 4
# 요세푸스 문제
# https://www.acmicpc.net/problem/1158
# 23.08.26

import queue

N, K = map(int, input().split())
lists = [i for i in range(1, N + 1)]
result = []
point, cnt = 0, 1 # point : 현재 위치가 어디인지 표현

while  len(lists) > 0:
    if (cnt % K) == 0:
        result.append(lists.pop(point))
    else: point += 1
    cnt += 1

    if point >= len(lists): # lists를 넘어가면 안되서 처음으로 초기화
        point = 0

print("<" + ', '.join(str(i) for i in result) + ">")