# 실버4
# 카드
# https://www.acmicpc.net/problem/11652
# 23.06.06

import sys
from collections import Counter

N = int(sys.stdin.readline())
lists = [int(sys.stdin.readline().rstrip()) for i in range(N)]
sort_lists = sorted(Counter(lists).most_common(), key=lambda x: (-x[1], x[0]))
print(sort_lists)
print(sort_lists[0][0])