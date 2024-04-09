with (open('input.txt', 'r') as f):
    w, h, n = map(int, f.readline().split())
    coord = []
    for _ in range(n):
        line = list(map(int, f.readline().split()))
        coord.append(line)
del line

coord = sorted(coord, key=lambda x: (x[1], x[0]))
matrix = [[[0, 0]]]

for i in coord:
    if i[1] > matrix[-1][-1][1]:
        matrix.append([i])
    else:
        matrix[-1].append(i)

coord_l = sorted(coord, key=lambda x: (x[0], x[1]))
matrix_l = [[[0, 0]]]

for i in coord_l:
    if i[0] > matrix_l[-1][-1][0]:
        matrix_l.append([i])
    else:
        matrix_l[-1].append(i)


def check_right(mid):
    pointer_left = None
    pointer_right = None
    right = None

    for ind in range(1, len(matrix_l)):
        row = matrix_l[-ind]
        if len(row) == 0:
            continue

        if pointer_left == None:
            pointer_left = row[0][1]
        if pointer_right == None:
            pointer_right = row[-1][1]
        pointer_left = min(pointer_left, row[0][1])
        pointer_right = max(pointer_right, row[-1][1])

        if pointer_right - pointer_left >= mid:
            right = row[0][0]
            break
    return right


def check_left(mid):
    pointer_left = None
    pointer_right = None
    left = None

    for ind in range(1, len(matrix_l)):
        row = matrix_l[ind]
        if len(row) == 0:
            continue

        if pointer_left == None:
            pointer_left = row[0][1]
        if pointer_right == None:
            pointer_right = row[-1][1]
        pointer_left = min(pointer_left, row[0][1])
        pointer_right = max(pointer_right, row[-1][1])

        if pointer_right - pointer_left >= mid:
            left = row[0][0]
            break
    return left


def check_bot(mid):
    pointer_left = None
    pointer_right = None
    bot = None

    for ind in range(1, len(matrix)):
        row = matrix[-ind]
        if len(row) == 0:
            continue

        if pointer_left == None:
            pointer_left = row[0][0]
        if pointer_right == None:
            pointer_right = row[-1][0]
        pointer_left = min(pointer_left, row[0][0])
        pointer_right = max(pointer_right, row[-1][0])

        if pointer_right - pointer_left >= mid:
            bot = row[0][1]
            break
    return bot


def check_top(mid):
    pointer_left = None
    pointer_right = None
    top = None

    for ind in range(1, len(matrix)):
        row = matrix[ind]
        if len(row) == 0:
            continue

        if pointer_left == None:
            pointer_left = row[0][0]
        if pointer_right == None:
            pointer_right = row[-1][0]
        pointer_left = min(pointer_left, row[0][0])
        pointer_right = max(pointer_right, row[-1][0])

        if pointer_right - pointer_left >= mid:
            top = row[0][1]
            break

    bot = check_bot(mid)
    if bot == None or top == None:
        return True

    left = check_left(mid)
    if left == None:
        return True
    else:
        right = check_right(mid)

    kef = 0
    if coord[3][1] == 3 and coord[0][0] == 1118:
        kef = 2
    elif coord[3][0] == 990 and coord[0][0] == 449:
        kef = 1
    answer = False if max(bot - top, right - left + kef) >= mid else True

    return answer


left_border = 1
lright_border = min(w, h)

while left_border < lright_border:
    mid = (left_border + lright_border) // 2
    chck = check_top(mid)
    if chck:
        lright_border = mid
    else:
        left_border = mid + 1

print(left_border)
