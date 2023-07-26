# 브론즈1
# 부녀회장이 될테야
# https://www.acmicpc.net/problem/2775
# 23.07.25

import sys

T = int(sys.stdin.readline())

for _ in range(T):
    k = int(sys.stdin.readline()) # k층
    n = int(sys.stdin.readline()) # n호
    lists = [[i + 1 for i in range(n)]] # 0층 n호 거주민

    for i in range(k):
        tmp = []
        for j in range(n):
            tmp.append(sum(lists[i][:j + 1]))
        lists.append(tmp)
    
    print(lists[k][n - 1])


# 다른 사람 풀이
# t = int(input())

# for _ in range(t):  
#     floor = int(input())  # 층
#     num = int(input())  # 호
#     f0 = [x for x in range(1, num+1)]  # 0층 리스트
#     for k in range(floor):  # 층 수 만큼 반복
#         for i in range(1, num):  # 1 ~ n-1까지 (인덱스로 사용)
#             f0[i] += f0[i-1]  # 층별 각 호실의 사람 수를 변경
#     print(f0[-1])  # 가장 마지막 수 출력