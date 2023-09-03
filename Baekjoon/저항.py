# 브론즈 2
# 저항
# https://www.acmicpc.net/problem/1076
# 23.09.02

color_dict = {
    "black" : [0, 1],
    "brown" : [1, 10],
    "red" : [2, 100],
    "orange" : [3, 1000],
    "yellow" : [4, 10000],
    "green" : [5, 100000],
    "blue" : [6, 1000000],
    "violet" : [7, 10000000],
    "grey" : [8, 100000000],
    "white" : [9, 1000000000],
}
result = ""

for i in range(3):
    color = input()
    if i < 2: result += str(color_dict.get(color)[0])
    else: print(int(result) * color_dict.get(color)[1])



# 다른 사람 풀이
# color = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']

# a = str(color.index(input())) # color.index(input())
# b = str(color.index(input())) # color.index(input())
# c = str(10 ** color.index(input())) # color.index(input())

# print(int(a + b + c[1:])) # int(str(a) + str(b)) * (10 ** c)