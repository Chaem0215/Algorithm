# 실버 4
# 요세푸스 문제
# https://www.acmicpc.net/problem/1158
# 23.08.26

# import queue

# N, K = map(int, input().split())
# lists = [i for i in range(1, N + 1)]
# result = []
# point, cnt = 0, 1 # point : 현재 위치가 어디인지 표현

# while  len(lists) > 0:
#     if (cnt % K) == 0:
#         result.append(lists.pop(point))
#     else: point += 1
#     cnt += 1

#     if point >= len(lists): # lists를 넘어가면 안되서 처음으로 초기화
#         point = 0

# print("<" + ', '.join(str(i) for i in result) + ">")


# 유정
# 실패ㅎ

from sys import stdin

N, K = map(int, stdin.readline().split())

rear = 0    # start, 삽입
front = 0   # end, 삭제
size = N
# queue = [str(i) for i in range(1, size+1)]
queue = [0 for _ in range(size)]
delnum = []

# rear = (rear+1)% size
# front = (front+1)% size

for n in range(N):
    rear = (rear+1)% size
    queue[rear] = str(n + 1)
    
print(queue) # [7, 1, 2, 3, 4, 5, 6]

# for n in range(N):          # pop시켜서 리스트 크기가 줄어드는 만큼 n값도 줄여야 index에러가 안남
while len(queue) > 1:
    front = (front+K)% size
    queue.pop(front)
    delnum.append(queue[front])

result = ', '.join(delnum)
print("<", result, ">")

# [3, 6, 2, 5, 1, 4, 7]
# 정답 : <3, 6, 2, 7, 5, 1, 4>