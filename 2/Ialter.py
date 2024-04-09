N = int(input())

matrix = [[0 for j in range(N)] for i in range(N)]

summa = 0

for _ in range(N):
    row, column = map(int, input().split())
    matrix[row - 1][column - 1] = 1
    summa += column - 1

srednee = round(summa / N)
next_free = [0, srednee]

for i in range(N):
    for j in range(N):
        pass


print(srednee)

print(*matrix, sep='\n')
