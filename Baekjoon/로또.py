# 실버 2
# 로또
# https://www.acmicpc.net/problem/6603
# 23.09.07

from itertools import combinations

while True:
    lists = list(map(int, input().split()))
    if lists[0] == 0: break

    for i in combinations(lists[1:], 6): print(*i)
    print()