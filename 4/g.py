with (open('input.txt', 'r') as f):
    n, m = map(int, f.readline().split())
    matrix = []
    for _ in range(n):
        line = list(f.readline().strip())
        matrix.append(line)

del f
del line

for i in range(n):
    counter = 0
    for j in range(m):
        if matrix[i][j] == '#':
            counter += 1
        else:
            counter = 0
        matrix[i][j] = counter

hash = []
for i in matrix:
    hash.append(max(i))


def check(mid):

    for i in range(mid, n - 2 * mid + 1):
        if mid > hash[i]:
            continue
        for j in range(mid * 3 - 1, m):
            for ind in range(mid):
                if matrix[i + ind][j] < (mid * 3):
                    break
                if matrix[i + ind + mid][j - mid] < (mid):
                    break
                if matrix[i - ind - 1][j - mid] < (mid):
                    break
            else:
                return True
    return False


u_l = 1
u_r = min(m, n) // 3 + 1

while u_l < u_r:
    mid = (u_l + u_r) // 2 + 1
    ans = check(mid)
    if ans:
        u_l = mid
    else:
        u_r = mid - 1
print(u_l)