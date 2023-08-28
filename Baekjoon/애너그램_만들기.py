# 브론즈 1
# 애너그램 만들기
# https://www.acmicpc.net/problem/1919
# 23.08.26

first_word = list(input())
second_word = list(input())
idx = 0

while idx < len(first_word):
    if first_word[idx] in second_word:
        second_word.remove(second_word[idx])
        first_word.remove(first_word[idx])
        idx -= 1
    idx += 1

print(len(first_word) + len(second_word))