# 실버 2
# 아카라카
# https://www.acmicpc.net/problem/23304
# 23.11.02

import sys
sys.setrecursionlimit(10**5)

def stringCompare (s):
    if s != s[::-1]: return False
    if len(s) <= 1: return True
    return stringCompare(s[:len(s) // 2])


S = input()
print("AKARAKA" if stringCompare(S[:len(S) // 2]) else "IPSELENTI") 



# 메모리 초과
# 재귀함수를 바로 리턴할 수 있도록 수정하기
# import sys
# sys.setrecursionlimit(10**5)

# def stringCompare (s):
#     idx = len(s) - 1

#     if idx <= 1: return True
#     elif s[0] != s[idx]: return False
#     return stringCompare(s[1:idx])


# S = input()
# point = len(S) // 2 if len(S) % 2 == 0 else (len(S) // 2) + 1
# first = stringCompare(S[:len(S) // 2])
# second = stringCompare(S[point:])
# print("AKARAKA" if first and second else "IPSELENTI")