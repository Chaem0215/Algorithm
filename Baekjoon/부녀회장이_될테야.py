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
