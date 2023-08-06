# 브론즈 1
# 팀 이름 정하기
# https://www.acmicpc.net/problem/1296
# 23.07.31

import sys

name = sys.stdin.readline().rstrip()
N = int(sys.stdin.readline())
dicts = dict()

for _ in range(N):
    team = sys.stdin.readline().rstrip()
    L = name.count('L') + team.count('L')
    O = name.count('O') + team.count('O')
    V = name.count('V') + team.count('V')
    E = name.count('E') + team.count('E')

    result = ((L + O) * (L + V) * (L + E) * (O + V) * (O + E) * (V + E)) % 100
    dicts.update({team : result})

dicts = dict(sorted(dicts.items()))
print(max(dicts, key=dicts.get))



# 문제 잘 못 이해

# import sys
# from functools import reduce

# name = sys.stdin.readline().rstrip()
# N = int(sys.stdin.readline())
# dicts = dict()
# set_name = list(set(name))

# for _ in range(N):
#     team = sys.stdin.readline().rstrip()
#     lists = []
#     result = 1
#     for i, j in enumerate(set_name[:len(set_name) - 1]):
#         for k in set_name[i + 1:]:
#             sum = (team.count(j) + name.count(j)) + (team.count(k) + name.count(k))
#             lists.append(sum)
    
#     dicts.update({team: reduce(lambda x, y: x * y, lists) % 100})

# dicts = dict(sorted(dicts.items()))
# print(dicts)
# print(max(dicts, key=dicts.get))