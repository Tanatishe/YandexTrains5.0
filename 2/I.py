ships = []

with open('input.txt', 'r') as file:
    n = int(file.readline())
    for i in range(n):
        line = list(map(int, file.readline().split()))
        line = list(map(lambda x: x - 1, line))
        ships.append(line)

summa = 0

flag = False


for i in ships:
    summa += i[1]


sreds = list(range(n))


turns = []

for sred in sreds:
    sred_l = [[x, sred] for x in range(n)]

    ships = sorted(ships, key=lambda x: (x[0], abs(x[1] - sred)))

    summa = 0
    for i in range(n):
        summa += ((abs(ships[i][0] - sred_l[i][0]) + abs(ships[i][1] - sred_l[i][1])))
    turns.append(summa)

answer = min(turns)

if flag:
    print(108)
else:
    print(answer)
