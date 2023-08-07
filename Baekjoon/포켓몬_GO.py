# 실버 5
# 포켓몬 GO
# https://www.acmicpc.net/problem/13717
# 23.08.07

import sys

N = int(sys.stdin.readline())
lists = []
dicts = dict()

def Evolution(P, K, M): # P: 포켓몬 이름, K: 진화에 필요한 사탕 수, M: 가지고 있는 총 사탕 수
    cnt = 0
    while M >= K:
        M -= K
        cnt += 1
        M += 2  # 진화가 된 후에는 2개의 사탕을 돌려받음
    dicts.update({P : cnt})

for i in range(N):
    lists.append([sys.stdin.readline().rstrip()])
    lists[i].append(list(map(int, sys.stdin.readline().rstrip().split())))

    for j in lists:
        Evolution(j[0], j[1][0], j[1][1]) # lists[0] : 포켓몬 이름, lists[1][0] : 진화에 필요한 사탕수, lists[1][1] : 가지고 있는 총 사탕 수

print(sum(dicts.values()), max(dicts, key=dicts.get), sep='\n') # 줄바꿔 출력




# 다른 사람 풀이 1
# def Evolution에서 while 문을 나머지 활용하여 함
    # while quot > 0:
    #     cur_cnt += quot
    #     r = candy % need  # 나머지
    #     candy = r + quot * 2
    #     quot = candy // need

# 다른 사람 풀이 2
# import sys
# input = sys.stdin.readline

# dict_pokemon = {}
# total_evolution = 0
# for n in range(int(input())):
#     pokemon = input().strip()
#     acquired, possessed = map(int, input().split())
#     unit_total_evolution = 0
#     while acquired <= possessed:
#         num_evolution = possessed // acquired
#         possessed = possessed % acquired + num_evolution * 2
#         unit_total_evolution += num_evolution
#     total_evolution += unit_total_evolution
#     dict_pokemon[pokemon] = (n, unit_total_evolution)
    
# pokemon_encyclopedia = sorted(list(dict_pokemon.items()), key=lambda x: (-x[1][1], x[1][0]))

# print(total_evolution)
# print(pokemon_encyclopedia[0][0])