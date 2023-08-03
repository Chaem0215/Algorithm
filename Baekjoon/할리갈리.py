# 브론즈2
# 할리갈리
# https://www.acmicpc.net/problem/27160
# 23.08.01

import sys
#from collections import Counter # 데이터 처리를 위한 유용한 객체가 많음
# dict를 쓴 이유 : dict는 키를 중복으로 받지 않는다. 이미 있는키면 거기에 추가 가능
N = int(sys.stdin.readline())
dicts = dict()
result = 'NO'

for _ in range(N):
    S, X = sys.stdin.readline().split()

    try: dicts[S] += int(X) # 키가 있다면 키만 추가
    except: dicts.update({S : int(X)}) # 키가 없다면 키를 추가

for S, X in dicts.items(): # dict 에서 반복문 사용하는 방법
    if X == 5: result = 'YES'

print(result)



# 다른 사람 풀이
# N = int(input())
# cards = {
#     'STRAWBERRY' : 0,
#     'BANANA' : 0,
#     'LIME' : 0,
#     'PLUM' : 0
# }

# for i in range(N) :
#     fruit, count = input().split()
#     cards[fruit] += int(count)

# check = 5 in cards.values()	# 5개 있는지 확인

# if check : print('YES')
# else : print('NO')