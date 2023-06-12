# 실버3
# 모든 순열
# https://www.acmicpc.net/problem/10974
# 23.06.12

import sys
from itertools import permutations

N = int(sys.stdin.readline())
lists = []
for i in range(N):
    lists.append(i+1)

for j in permutations(lists, N):
    print(*j) # Unpacking 사용 (묶인 값 풀어주는)
    

# 다른 사람 풀이
from itertools import permutations
n = int(input())
for i in permutations(list(range(1, n+1)), n):print(*i)