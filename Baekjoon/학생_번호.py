# 실버4
# 학생 번호
# https://www.acmicpc.net/problem/1235
# 23.07.17

import sys

def duplicate(result):
    return len(result) == len(set(result))

N = int(sys.stdin.readline())
lists = list(sys.stdin.readline().strip() for _ in range(N))
answer = 0

for i in range(1, len(lists[0]) + 1):
    result = []

    for j in lists:
        result.append(j[-i:])

    if duplicate(result):
        answer = len(result[0])
        break
print(answer if i != 0 else 1)




# 다른 사람 풀이

# import sys
# input = sys.stdin.readline
# N = int(input())
# numbers = [input().rstrip() for _ in range(N)]
# k = 1

# while True:
#     check = set()
#     for number in numbers:
#         check.add(number[-k:])
#     if len(check) == N:
#         break
#     k += 1
# print(k)