matrix = []
for i in range(8):
    matrix.append(list(input().strip()))

count = 0


def process_rook(ii, jj):
    ii = i - 1
    jj = j
    while ii in range(8) and jj in range(8):
        if matrix[ii][jj] == '*':
            matrix[ii][jj] = 'r'
        elif matrix[ii][jj] in 'BR':
            break
        ii -= 1

    ii = i + 1
    jj = j
    while ii in range(8) and jj in range(8):
        if matrix[ii][jj] == '*':
            matrix[ii][jj] = 'r'
        elif matrix[ii][jj] in 'BR':
            break
        ii += 1

    ii = i
    jj = j + 1
    while ii in range(8) and jj in range(8):
        if matrix[ii][jj] == '*':
            matrix[ii][jj] = 'r'
        elif matrix[ii][jj] in 'BR':
            break
        jj += 1

    ii = i
    jj = j - 1
    while ii in range(8) and jj in range(8):
        if matrix[ii][jj] == '*':
            matrix[ii][jj] = 'r'
        elif matrix[ii][jj] in 'BR':
            break
        jj -= 1


def process_bish(i, j):
    ii = i - 1
    jj = j - 1
    while ii in range(8) and jj in range(8):
        if matrix[ii][jj] == '*':
            matrix[ii][jj] = 'b'
        elif matrix[ii][jj] in 'BR':
            break
        ii -= 1
        jj -= 1
    ii = i + 1
    jj = j - 1
    while ii in range(8) and jj in range(8):
        if matrix[ii][jj] == '*':
            matrix[ii][jj] = 'b'
        elif matrix[ii][jj] in 'BR':
            break
        ii += 1
        jj -= 1
    ii = i - 1
    jj = j + 1
    while ii in range(8) and jj in range(8):
        if matrix[ii][jj] == '*':
            matrix[ii][jj] = 'b'
        elif matrix[ii][jj] in 'BR':
            break
        ii -= 1
        jj += 1
    ii = i + 1
    jj = j + 1
    while ii in range(8) and jj in range(8):
        if matrix[ii][jj] == '*':
            matrix[ii][jj] = 'b'
        elif matrix[ii][jj] in 'BR':
            break
        ii += 1
        jj += 1


for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == 'R':
            process_rook(i, j)
        elif matrix[i][j] == 'B':
            process_bish(i, j)

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == '*':
            count += 1

print(count)