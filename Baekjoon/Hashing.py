# 브론즈2
# Hashing
# https://www.acmicpc.net/problem/15829
# 23.07.09

import sys

L = int(sys.stdin.readline())
string = sys.stdin.readline()
result = 0

for i in range(L):
    result += (ord(string[i]) - 96) * (31 ** i)

print(result % 1234567891)