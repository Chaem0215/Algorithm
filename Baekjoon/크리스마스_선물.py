# 실버3
# 크리스마스 선물
# https://www.acmicpc.net/problem/14235
# 23.07.26

import sys
from queue import PriorityQueue

n = int(sys.stdin.readline())
lists = PriorityQueue()

for _ in range(n):
    a = list(map(int, sys.stdin.readline().split()))

    if a[0] == 0 and lists.empty(): # Queue에 원소없다면
        print(-1)
        continue
    elif a[0] > 0:
        for i in a[1:]: lists.put((-i, i)) # 역순으로 출력하기 위해
    else:
        print(lists.get()[1])


# heapq 를 써야하는 이유
# https://slowsure.tistory.com/130


# 다른 사람 풀이
# import heapq

# if __name__ == '__main__':
#     N = int(input())
#     pq = []  # 선물을 담을 리스트 ( 우선순위 큐 )
#     for _ in range(N):
#         input_value = input()
#         if input_value == '0':  # 인풋값이 0일 때
#             if pq:  # 선물이 있으면 선물
#                 print(-heapq.heappop(pq))
#             else:  # 선물이 없으면 -1
#                 print(-1)

#         else:
#             # 거점에서 선물 충전
#             present_list = list(map(int, input_value.split()))
#             for i in range(1, present_list[0] + 1):
#                 heapq.heappush(pq, -present_list[i])