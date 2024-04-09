import datetime

start = datetime.datetime.now()

with open('input.txt', 'r') as file:
    n = int(file.readline())
    massiv = []
    hash_l = n * 11
    hash_x = []
    for i in range(hash_l):
        hash_x.append([])

    for _ in range(n):
        line = list(map(int, file.readline().split()))
        hash_x[line[0] % hash_l].append(line)
        massiv.append(line)

answer = [1, 2, 3, 4]

for i in range(n - 1):
    for j in range(i + 1, n):
        now = massiv[i]
        next = massiv[j]

        cor_x = now[1] - next[1]
        cor_y = now[0] - next[0]

        check_list = [[now[0] + cor_x, now[1] - cor_y], [next[0] + cor_x, next[1] - cor_y]]
        if check_list[0] in hash_x[check_list[0][0] % hash_l]:
            del check_list[0]
            if check_list[0] in hash_x[check_list[0][0] % hash_l]:
                del check_list[0]
        elif check_list[1] in hash_x[check_list[1][0] % hash_l]:
            del check_list[1]
        if len(check_list) < len(answer):
            answer = check_list

        check_list = [[now[0] - cor_x, now[1] + cor_y], [next[0] - cor_x, next[1] + cor_y]]
        if check_list[0] in hash_x[check_list[0][0] % hash_l]:
            del check_list[0]
            if check_list[0] in hash_x[check_list[0][0] % hash_l]:
                del check_list[0]
        elif check_list[1] in hash_x[check_list[1][0] % hash_l]:
            del check_list[1]
        if len(check_list) < len(answer):
            answer = check_list

print(len(answer))
if len(answer) > 0:
    for i in answer:
        print(*i)

finish = datetime.datetime.now()
print('Время работы: ' + str(finish - start))
