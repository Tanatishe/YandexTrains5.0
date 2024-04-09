import copy

with open('input.txt', 'r') as file:
    n = int(file.readline())
    massiv_A = []
    massiv_B = []
    for _ in range(n):
        line = list(map(int, file.readline().split()))
        line = [[line[0], line[1]], [line[2], line[3]]]
        line = list(sorted(line, key=lambda x: (x[0], x[1])))
        massiv_A.append(line)

    for _ in range(n):
        line = list(map(int, file.readline().split()))
        line = [[line[0], line[1]], [line[2], line[3]]]
        line = list(sorted(line, key=lambda x: (x[0], x[1])))

        massiv_B.append(line)

answer = 0
sdvig_list = []
sdvig_dict = {}

hash_a = []
hash_b = []

nn = n
n = n if n > 10 else 10
for _ in range(n):
    hash_a.append([])
    hash_b.append([])

for i in massiv_A:
    sdvig_x_a = i[1][0] - i[0][0]
    sdvig_y_a = i[1][1] - i[0][1]
    sdvig_a = f'{sdvig_x_a} {sdvig_y_a}'
    for j in massiv_B:
        sdvig_x_b = j[1][0] - j[0][0]
        sdvig_y_b = j[1][1] - j[0][1]
        sdvig_b = f'{sdvig_x_b} {sdvig_y_b}'
        if sdvig_a == sdvig_b:

            test_sdvig_x = i[0][0] - j[0][0]
            test_sdvig_y = i[0][1] - j[0][1]

            keyw = f'{test_sdvig_x} {test_sdvig_y}'
            if keyw not in sdvig_dict:
                sdvig_dict[keyw] = 1
            else:
                sdvig_dict[keyw] += 1
            if sdvig_dict[keyw] > answer:
                answer = sdvig_dict[keyw]

print(nn - answer)
