# 실버 5
# 막대기
# https://www.acmicpc.net/problem/1094
# 23.08.29

X = int(input())
result, cnt, bar = 0, 0, 64

while result != X:
    helf = bar // 2

    if helf > X: 
        bar = helf
    elif bar == X: 
        result += bar
        cnt += 1
    elif helf <= X:
        result += helf
        cnt += 1

print(cnt)