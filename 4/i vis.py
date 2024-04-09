
import turtle

# Считывание данных из файла
with open("input.txt", "r") as file:
    D, N = map(int, file.readline().split())
    players = [list(map(int, file.readline().split())) for _ in range(N)]

# Создание окна
wn = turtle.Screen()
wn.bgcolor("white")

# Создание черепахи для рисования
t = turtle.Turtle()
t.speed(0)
t.color("blue")

# Коэффициент для увеличения изображения
scale = 0.5
time = 0.5
# Нарисовать окружность с центром 0,0 и точками по x D, -D
t.penup()
t.goto(-D * scale, 0)
t.pendown()
t.goto(D * scale, 0)
t.penup()
t.goto(0,-D * scale)
t.pendown()
t.circle(D*scale)

t.goto(0, 0)

# Нарисовать точку в центре
t.penup()
t.goto(0, 0)
t.dot(5)

# Нарисовать игроков
for player in players:
    t.color('red')
    x, y, v = player
    t.penup()
    t.goto(x * scale, y * scale)
    t.pendown()
    t.dot(scale*v*time)

# Закрытие окна при клике
wn.exitonclick()
