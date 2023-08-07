# 실버 3
# NBA 농구
# https://www.acmicpc.net/problem/2852
# 23.08.07

import sys

N = int(sys.stdin.readline())
lists = []
team_lists = [[00, 00], [00, 00]]

#def a():

for _ in range(N):
    team, time = sys.stdin.readline().rstrip().split()
    lists.append([team, list(map(int, time.split(':')))])



print(team_lists)