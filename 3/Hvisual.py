import turtle

with open('input.txt', 'r') as file:
    n = int(file.readline())
    massiv_A = []
    massiv_B = []
    for _ in range(n):
        line = list(map(int, file.readline().split()))
        massiv_A.append(((line[0], line[1]), (line[2], line[3])))
    for _ in range(n):
        line = list(map(int, file.readline().split()))
        massiv_B.append(((line[0], line[1]), (line[2], line[3])))

screen = turtle.Screen()
t = turtle.Turtle()

koef = 40
sdvig_x = 0
sdvig_y = 0
sdvig_x2 = 0
sdvig_y2 = 0
t.speed(0)

for fire in massiv_A:
    t.penup()
    t.goto(fire[0][0] * koef + sdvig_x2, fire[0][1] * koef + sdvig_y2)
    t.pendown()
    t.goto(fire[1][0] * koef + sdvig_x2, fire[1][1] * koef + sdvig_y2)
for fire in massiv_B:
    t.color('red')
    t.penup()
    t.goto(fire[0][0] * koef + sdvig_x, fire[0][1] * koef + sdvig_y)
    t.pendown()
    t.goto(fire[1][0] * koef + sdvig_x, fire[1][1] * koef + sdvig_y)

while True:
    pass
