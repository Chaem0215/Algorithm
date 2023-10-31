# 실버 1
# 회전 초밥
# https://www.acmicpc.net/problem/2531
# 23.10.31

import sys

def toPointer(start, end, mid):
    tmp = []
    if end >= N: 
        tmp = plates[start:] + plates[:mid]
    else: tmp = plates[start:end]

    return tmp


N, d, k, c = map(int, sys.stdin.readline().split()) # N: 접시의 수, d: 초밥 가짓수, k: 연속 접시 수, c: 쿠폰
plates = [int(sys.stdin.readline()) for _ in range(N)]
lists = list()

for i in range(N):
    tmp = set(toPointer(i, i + k, i + k - N))

    if c in tmp: lists.append(len(tmp))
    else: lists.append(len(tmp) + 1)

print(max(lists))



## 1. 런타임 에러 valueError
# import sys

# def toPointer(start, end, mid):
#     tmp = []
#     if end >= N: 
#         tmp = plates[start:] + plates[:mid]
#     else: tmp = plates[start:end]
#     return tmp

# N, d, k, c = map(int, sys.stdin.readline().split()) # N: 접시의 수, d: 초밥 가짓수, k: 연속 접시 수, c: 쿠폰
# plates = [int(sys.stdin.readline()) for _ in range(N)]
# lists = list()

# for i in range(N):
#     tmp = toPointer(i, i + k, i + k - N)
#     if len(set(tmp)) == k: lists.append(tmp)

# result = []
# for j in lists:
#     if c in j: result.append(len(j))
#     else: result.append(len(j) + 1)

# print(max(result))



## 다른 사람 풀이
# import sys
# input = sys.stdin.readline

# n, d, k, c = map(int, input().split())
# arr = [int(input()) for _ in range(n)]
# arr.extend(arr[:k])

# ans = 0
# for i in range(n):
#     ans = max(ans, len(set(arr[i:i+k])-set([c])))
# print(ans+1)



## 다른 사람 풀이 # 부르트포스 만으로 푼 것.
# import sys
# input = sys.stdin.readline

# N, d, k, c = map(int, input().rstrip().split())
# sushi = [int(input()) for _ in range(N)]
# max_number_of_type = 0
# for i in range(N):
#     if i+k > N:
#         number_of_type = len(set(sushi[i:N] + sushi[:(i+k)%N] + [c]))
#     else:
#         number_of_type = len(set(sushi[i:i+k] + [c]))
#     if max_number_of_type < number_of_type:
#         max_number_of_type = number_of_type
# print(max_number_of_type)