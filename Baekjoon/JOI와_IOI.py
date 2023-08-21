# 브론즈 2
# JOI와 IOI
# https://www.acmicpc.net/problem/5586
# 23.08.20

lists = list(input())
JOI, IOI = 0, 0
for i in range(len(lists[:len(lists) - 2])):
    if "JOI" == lists[i] + lists[i + 1] + lists[i + 2]: #  if s[i : i + 3] == "JOI":
        JOI += 1
    elif "IOI" == lists[i] + lists[i + 1] + lists[i + 2]: #  elif s[i : i + 3] == "IOI":
        IOI += 1

print(JOI, IOI, sep="\n")