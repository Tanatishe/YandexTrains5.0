# Создаем пустую доску
board = [[0] * 8 for _ in range(8)]

# Считываем количество выпиленных клеток
N = int(input())

# Отмечаем выпиленные клетки на доске
for _ in range(N):
    row, col = map(int, input().split())
    board[row - 1][col - 1] = 1

# Инициализируем периметр
perimeter = 0

# Проверяем каждую выпиленную клетку
for row in range(8):
    for col in range(8):
        if board[row][col] == 1:
            # Проверяем соседние клетки
            if row - 1 < 0 or board[row - 1][col] == 0:
                perimeter += 1
            if row + 1 == 8 or board[row + 1][col] == 0:
                perimeter += 1
            if col - 1 < 0 or board[row][col - 1] == 0:
                perimeter += 1
            if col + 1 == 8 or board[row][col + 1] == 0:
                perimeter += 1

# Выводим периметр
print(perimeter)
