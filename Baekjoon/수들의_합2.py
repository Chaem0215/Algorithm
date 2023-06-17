# 실버4
# 수들의 합 2
# https://www.acmicpc.net/problem/2003
# 23.06.12

#2. 투 포인터 : 두 지점을 통해 구간의 부분합 도출
import sys

N, M = map(int, sys.stdin.readline().split())
lists = list(map(int, sys.stdin.readline().split()))
cnt = 0
left = 0
right = 1
sum = lists[0]

while right <= N and left <= right: # 포인터를 이용하여 중복 덧셈 연산을 제외시켜줌
    if sum == M:
        cnt += 1
        sum -= lists[left]
        left += 1
    elif sum < M:
        if right == N:
            break
        sum += lists[right]
        right += 1
    else:
        sum -= lists[left]
        left += 1
print(cnt)


# 1. 시간 초과
# import sys

# N, M = map(int, sys.stdin.readline().split())
# lists = list(map(int, sys.stdin.readline().split()))
# cnt = 0

# for i, v in enumerate(lists):
#     sum = 0
#     for j in lists[i:]:
#         sum += j
#         if M < sum: break
#         elif M == sum:
#             cnt += 1
#             break
        

# print(cnt)