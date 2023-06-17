# 실버4
# 수 찾기
# https://www.acmicpc.net/problem/1920
# 23.06.15

import sys

# 2. 이분탐색 시간 복잡도 O(logN)
N = int(sys.stdin.readline())
lists_N = sorted(list(map(int, sys.stdin.readline().split())))
M = int(sys.stdin.readline())
lists_M = list(map(int, sys.stdin.readline().split()))
result = []

def bisect(lists, i, start, end):
    if start > end: return 0
    mid = (start + end) // 2
    if i == lists[mid]: return 1
    elif i < lists[mid]: return bisect(lists, i, start, mid - 1)
    else: return bisect(lists, i, mid + 1, end)

for i in lists_M:
    start = 0
    end = N - 1
    print(bisect(lists_N, i, start, end))



# 3. 집합 자료형을 통한 포함 여부 확인
# from sys import stdin, stdout
# n = stdin.readline()
# N = set(stdin.readline().split())
# m = stdin.readline()
# M = stdin.readline().split()

# for l in M:
#     stdout.write('1\n') if l in N else stdout.write('0\n') # set, dictionary 의 in 시간 복잡도 O(1)



# 1. 시간초과
# import sys

# N = int(sys.stdin.readline())
# lists_N = list(map(int, sys.stdin.readline().split()))
# M = int(sys.stdin.readline())
# lists_M = list(map(int, sys.stdin.readline().split()))
# result = []

# for i in lists_M:
#     if i not in lists_N: result.append(0)
#     else: result.append(1)

# print(*result, sep='\n')