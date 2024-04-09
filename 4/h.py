from math import ceil
from copy import deepcopy

with (open('input.txt', 'r') as f):
    n = int(f.readline())
    spisok_nachal = []
    counter = 1
    for _ in range(n):
        line = (list(map(int, f.readline().split())))
        line.append(counter)
        spisok_nachal.append(line)
        counter += 1


spisok = list(sorted(spisok_nachal, key=lambda x: -x[0]))


answers = []
prefix = [0]
for i, v in enumerate(spisok[1:], 1):
    prefix.append(prefix[-1] + (spisok[i - 1][0]))


def find_index(test_sum):
    l = 1
    r = len(spisok) - 1
    while l < r:
        mid = (l + r) // 2
        if test_sum <= spisok[mid][0]:
            l = mid + 1
        else:
            r = mid
    return prefix[l], l


def check(m, party):
    pref, ind = find_index(m + party)
    ans = m + party > ceil((pref - m) / ind)
    ostatok = (pref - m) % ind
    return ans, ind, ostatok


def calc(party):
    l = 1
    r = 10 ** 7
    while l < r:
        m = (l + r) // 2
        ans, deep_index, ostatok = check(m, party)
        if ans:
            r = m
        else:
            l = m + 1
    return l, deep_index, ostatok

dc = {}
answers = []
for index, party in enumerate(spisok):
    if index == 0 and party[1] > 0:
        if len(spisok) > 1 and spisok[1][0] == party[0]:
            answers.append([party[1] + 1, party[2], party[1], index, 0, party[0], True, 0])
        else:
            answers.append([party[1], party[2], party[1], index, 0, party[0], False, 0])
        continue
    if party[1] < 0:
        continue
    if party[0] not in dc:
        dc[party[0]] = calc(party[0])
    ans, deep_index, ostatok = dc[party[0]]
    test_ostatok = ans - (prefix[deep_index] - (ans + party[0] - 1) * deep_index)
    answers.append([ans + party[1], party[2], party[1], index, deep_index, ans + party[0], False, test_ostatok])

answer = sorted(answers, key=lambda x: x[0])[0]

print(spisok)


if answer[6]:
    spisok[spisok[1][2] - 1][0] -= 1
else:
    for i in spisok[:answer[4]]:
        spisok_nachal[i[2] - 1] = answer[5] - 1
    spisok_nachal[spisok[0][2] - 1] -= answer[7]

print(spisok)

print(answer[0])
print(answer[1])
print(*spisok_nachal)
