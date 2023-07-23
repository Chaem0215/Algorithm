# 실버3
# 1로 만들기
# https://www.acmicpc.net/problem/1463
# 23.07.11

import sys

X = int(sys.stdin.readline())
result = [0] * (X + 1)

#result[1] = 0

for  i in range(2, X + 1):
    print('i: ', i)
    result[i] = result[i - 1] + 1
    print(result)
    if i % 2 == 0:
        result[i] = min(result[i], result[i // 2] + 1)
    if i % 3 == 0:
        result[i] = min(result[i], result[i // 3] + 1)

print(result[X])



#10 : 9 -> 3 -> 1
#10 : 5 -> 4 -> 2 -> 1

#11 : 10 -> 9 -> 3 -> 1
#11 : 10 -> 5 -> 4 -> 2 -> 1

#12 : 4 -> 2 -> 1

#13 : 12 -> 4 -> 2 -> 1

#14 : 7 -> 6 -> 2 -> 1

#15 : 5 -> 4 -> 2 -> 1

#16 : 8 -> 4 -> 2 -> 1
#16 : 15 -> 5 -> 4 -> 2 -> 1
