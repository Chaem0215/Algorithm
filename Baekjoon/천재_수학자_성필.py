# 실버 3
# 천재 수학자 성필
# https://www.acmicpc.net/problem/15815
# 23.10.19

N = list(input())
tmp, result = [], 0

for i in N:
        if(i == '+' or i == '-' or i == '*' or i == '/'):
            a = tmp.pop()
            b = tmp.pop()
            if i == '+': tmp.append(a + b)
            elif i == '-': tmp.append(b - a)
            elif i == '*': tmp.append(a * b)
            elif i == '/': tmp.append(b // a)
        else: tmp.append(int(i))
print(*tmp)


# 1. 런타임 에러 eval(result) 쓰면 
# N = list(input())
# sign, result = N[(len(N) // 2) + 1:], ''

# for i, v in enumerate(N[:(len(N) // 2) + 1]):
#     if len(sign) > i: result += (v + sign[i - 1])
#     else: result += v

# print(eval(result))

# 2. 런타임 에러
# N = list(input())
# stand = (len(N) // 2) + 1
# lists, sing = list(map(int, N[:stand])), N[stand:]
# result = lists.pop()

# for i in sing:
#     tmp = lists.pop()
#     if i == '+': result += tmp
#     elif i == '-': result -= tmp
#     elif i == '*': result *= tmp
#     else: result // tmp

# print(result)