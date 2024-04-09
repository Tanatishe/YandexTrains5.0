matrix = []

with open('input.txt', 'r') as file:
    m, n = map(int, file.readline().split())
    for i in range(m):
        line = file.readline().strip('\n')
        matrix.append(list(line))

flag = 0
a = []
b = []
red_flag = False
green_flag = False


def check():
    flag = False
    for i in a:
        for j in i:
            if matrix[j[0]][j[1]] == 'b':
                flag = True
            if matrix[j[0]][j[1]] == 'a' and flag:
                return
    flag = False
    for i in b:
        for j in i:
            if matrix[j[0]][j[1]] == 'a':
                flag = True
            if matrix[j[0]][j[1]] == 'b' and flag:
                return
    global green_flag
    green_flag = True


def get_a(i, j, n, m):
    global a
    line = [[i, j]]
    if j < n - 1:
        for ind in range(j + 1, n):
            if matrix[i][ind] in '#b':
                line.append([i, ind])
            else:
                break
    if len(a) == 0 or len(line) == len(a[0]):
        a.append(line)
    else:
        pass
    if i < m - 1 and matrix[i + 1][a[0][0][1]] == '#':
        get_a(i + 1, a[0][0][1], a[0][-1][1] + 1, m)


def print_a():
    for i in a:
        for j in i:
            matrix[j[0]][j[1]] = 'a'


def get_b(i, j, n, m):
    global b
    line = [[i, j]]
    if j < n - 1:
        for ind in range(j + 1, n):
            if matrix[i][ind] in '#a':
                line.append([i, ind])
            else:
                break
    if len(b) == 0 or len(line) == len(b[0]):
        b.append(line)
    else:
        pass
    if i < m - 1 and matrix[i + 1][b[0][0][1]] == '#':
        get_b(i + 1, b[0][0][1], b[0][-1][1] + 1, m)


def alt_get_b(i, j, n, m):
    global b

    line = [[i, j]]
    if j < n - 1:
        for ind in range(j + 1, n):
            if matrix[i][ind] in '#':
                line.append([i, ind])
            elif matrix[i][ind] in 'a' and i < m - 1 and matrix[i + 1][line[0][1]] == '#':
                break
            elif matrix[i][ind] in 'a':
                line.append([i, ind])
            else:
                break
    if len(b) == 0 or len(line) == len(b[0]):
        b.append(line)
    else:
        pass
    if i < m - 1 and matrix[i + 1][b[0][0][1]] == '#':
        alt_get_b(i + 1, b[0][0][1], b[0][-1][1] + 1, m)


def print_b():
    for i in b:
        for j in i:
            matrix[j[0]][j[1]] = 'b'


for i in range(m):
    for j in range(n):
        if matrix[i][j] == '#':
            if flag == 0:
                flag = 'a'
                get_a(i, j, n, m)
                print_a()
            elif flag == 'a':
                flag = 'b'
                alt_get_b(i, j, n, m)
                print_b()
            else:
                red_flag = True
                break
    if red_flag:
        break

if len(b) == 0:
    if len(a) == 0 or len(a) == 1 and len(a[0]) == 1:
        red_flag = True
    if len(a) > 1:
        b.append(a[-1])
        print_b()
    else:
        for i in a:
            b.append([i[-1]])
        print_b()

if not red_flag:
    check()
    if not green_flag:
        print_a()
        check()

    if not green_flag:
        i = b[0][0][0]
        j = b[0][0][1]
        b = []
        get_b(i, j, n, m)
        print_a()
        print_b()
        check()

    if not green_flag:
        red_flag = True

if red_flag:
    print('NO')

if green_flag:
    print('YES')
    for i in matrix:
        print(*i, sep='')

