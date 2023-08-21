# 실버 5
# 생일
# https://www.acmicpc.net/problem/5635
# 23.08.07

import sys

n = int(sys.stdin.readline())
dicts = {}

for _ in range(n):
    tmp = list(sys.stdin.readline().rstrip().split())
    dicts.update({tmp[0] : int(tmp[3] + tmp[2].zfill(2) + tmp[1].zfill(2))})

print(max(dicts, key=dicts.get), min(dicts, key=dicts.get), sep="\n")