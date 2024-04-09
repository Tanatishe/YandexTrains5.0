n = int(input())
points = []
for i in range(n):
    points.append(list(map(int, input().split())))

xmax = points[0][0]
xmin = points[0][0]
ymax = points[0][1]
ymin = points[0][1]

for i, j in points:
    if i > xmax:
        xmax = i
    if j > ymax:
        ymax = j
    if i < xmin:
        xmin = i
    if j < ymin:
        ymin = j
print(xmin, ymin, xmax, ymax)
