# 실버 2
# 주차장
# https://www.acmicpc.net/problem/5464
# 23.11.09

# https://chaewonkong.github.io/posts/python-deque.html

import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
lists = [0] * N
N_lists = [int(sys.stdin.readline().rstrip()) for _ in range(N)]  # 자리에 대한 무게
M_lists = [int(sys.stdin.readline().rstrip()) for _ in range(M)]  # 차 번호에 대한 가격
que = deque()
total = 0

def cost(idx, i): # idx = 0 -> 1
    k = N_lists[idx]
    s = M_lists[i - 1]

    return k * s

def fullCarLists():
    try: return lists.index(0)
    except: return -1

for _ in range(M * 2): # find : 문자열에서만 사용, index : 딕셔너리만 불가
    i = int(sys.stdin.readline().rstrip())

    if i > 0: # 주차 차량
        idx = fullCarLists() # 주차장이 만차인지, 아닌지 확인
        if idx >= 0:
            lists[idx] = i
        else: # 만차라면 큐에 넣음
            que.append(i)
    else: # 출차 차량
        idx = lists.index(abs(i))
        total += cost(idx, abs(i))
        lists[idx] = 0
        if len(que): lists[idx] = que.popleft() # 출차 후 큐에 대기중인 차가 있다면 주차
print(total)
