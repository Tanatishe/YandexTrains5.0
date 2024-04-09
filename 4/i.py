import math


# Функция для вычисления расстояния между двумя точками
def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


# Функция для расчета времени до мяча для первого игрока
def first_player_time(x, y, players):
    min_time = float('inf')
    for player in players:
        dist = distance(x, y, player[0], player[1])
        time = dist / player[2]
        if time < min_time:
            min_time = time
    return min_time


def find_y(x, players, D):
    left = 0
    right = math.sqrt(D ** 2 - x ** 2)
    epsilon = 10 ** -4  # Точность для остановки поиска
    while right - left > epsilon:
        mid1 = left + (right - left) / 3
        mid2 = right - (right - left) / 3
        time1 = first_player_time(x, mid1, players)
        time2 = first_player_time(x, mid2, players)
        if time1 > time2:
            right = mid2
        else:
            left = mid1
    return left


# Загрузка данных из файла input.txt
with open('input.txt', 'r') as file:
    D, her = map(int, file.readline().split())
    players = []
    for line in file:
        x, y, v = map(float, line.split())
        players.append((x, y, v))

# Бинарный поиск для нахождения точки с минимальным временем для первого игрока
left = -D
right = D
epsilon = 10 ** -4  # Точность для остановки поиска
while right - left > epsilon:
    mid1 = left + (right - left) / 10
    mid2 = right - (right - left) / 10
    yy = find_y(mid1, players, D)
    time1 = first_player_time(mid1, yy, players)
    yy = find_y(mid2, players, D)
    time2 = first_player_time(mid2, yy, players)
    if time1 > time2:
        right = mid2
    else:
        left = mid1
best_shot = (left, yy)
best_time = first_player_time(left, yy, players)
answers = []
answers.append([best_time, best_shot])

left = -D
right = D
epsilon = 10 ** -4  # Точность для остановки поиска
while right - left > epsilon:
    mid1 = left + (right - left) / 3
    mid2 = right - (right - left) / 3
    time1 = first_player_time(mid1, 0, players)
    time2 = first_player_time(mid2, 0, players)
    if time1 > time2:
        right = mid2
    else:
        left = mid1
best_shot = (left, 0)
best_time = first_player_time(left, 0, players)

answers.append([best_time, best_shot])

answers = sorted(answers, key=lambda x: -x[0])
print(answers[0][0])
print(answers[0][1][0], answers[0][1][1])
