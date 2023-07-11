# 실버5
# 사과 담기 게임
# https://www.acmicpc.net/problem/2828
# 23.07.10

import sys

N, M = map(int, sys.stdin.readline().split())
J = int(sys.stdin.readline())
lists = list(int(sys.stdin.readline()) for _ in range(J))
cnt, start, end, index = 0, 1, M, 0

while J > 0:
    if start <= lists[index] <= end:
        index += 1
        J -= 1
        continue
    elif start > lists[index]:
        start -= 1
        end -= 1
    else:
        start += 1
        end += 1
    cnt += 1

print(cnt)

# 다른사람 풀이
n,m = map(int, input().split())
j = int(input())
 
left = 1
right = m
count = 0
 
for _ in range(j):
    position = int(input())
 
    if left <= position and right >= position:
        continue
    elif left > position:
        count += (left-position)
        right -= (left-position)
        left = position
    else:
        count += (position-right)
        left += (position-right)
        right = position
 
print(count)