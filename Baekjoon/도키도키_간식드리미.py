# 실버3
# 도키도키 간식드리미
# https://www.acmicpc.net/problem/12789
# 23.06.20

import sys

N = int(sys.stdin.readline())
lists = list(map(int, sys.stdin.readline().split()))
stack = []
cnt = 1

for i in lists:
    stack.append(i)
    while stack and stack[-1] == cnt:
        stack.pop()
        cnt += 1
        
print("Nice" if len(stack) == 0 else "Sad")


# 1. 코드 자체 틀림
# 문제 잘 읽기

# import sys

# N = int(sys.stdin.readline())
# lists = list(map(int, sys.stdin.readline().split()))
# stack = []
# cnt = 1
# index = 0
# result = 0

# while len(lists) > index:
#     if cnt == lists[index]:
#         cnt += 1
#     else :
#         if len(stack) == 0: stack.append(lists[index])
#         elif stack[-1] == cnt:
#             stack.pop()
#             cnt += 1
#         else: stack.append(lists[index])
#     index += 1

# print("Nice" if len(stack) == 0 else "Sad")