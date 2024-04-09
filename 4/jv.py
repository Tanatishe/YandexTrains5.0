import turtle

with open('input.txt', 'r') as file:
    n, h = file.readline().split()
    n = int(n)
    h = float(h)
    coords = []
    for i in range(n + 1):
        line = file.readline()
        line = line.replace('–', '-')
        line = list(map(int, line.split()))
        coords.append(line)

k = 20

wn = turtle.Screen()
wn.bgcolor("white")
coords.append([coords[0][0], 20000])
coords.sort(key=lambda x:(x[0], -x[1]))
coords.append([coords[-1][0], 20000])
turtle.penup()

turtle.penup()
turtle.speed(0)
for i, j in coords:
    turtle.setpos(i*k, j*k)
    turtle.pendown()


wn.exitonclick()
