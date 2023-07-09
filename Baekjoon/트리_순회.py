# 실버1
# 트리 순회
# https://www.acmicpc.net/problem/1991
# 23.07.09

import sys

N = int(sys.stdin.readline())
lists = [list(sys.stdin.readline()) for _ in range(N)]

def pre(result): # 전위 순회

    return result