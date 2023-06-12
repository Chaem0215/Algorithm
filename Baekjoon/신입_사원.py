# 실버1
# 신입 사원
# https://www.acmicpc.net/problem/1946
# 23.06.12

import sys

N = int(sys.stdin.readline())

for _ in range(N):
    lists = []
    result = 1
    for _ in range(int(sys.stdin.readline())):
        lists.append(list(map(int, sys.stdin.readline().rstrip().split(' '))))

    lists = sorted(lists, key = lambda x: (x[0]))
    rank = lists[0][1]
    
    for i in range(1, len(lists)):
        if lists[i][1] < rank:
            result += 1
            rank = lists[i][1]
    
    print(result)