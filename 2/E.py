import datetime
start = datetime.datetime.now()

berries = []

with open('input.txt', 'r') as file:
    n = int(file.readline())
    for i in range(n):
        line = list(map(int, file.readline().split()))
        line.append(i + 1)
        berries.append(line)

max_h = 0
posled = []
neplus = []

counter_plus = 0
counter_minus = 0
max_plus = -1
max_minus = -1
max_plus_ind = -1
max_minus_ind = -1

for value in berries:
    if value[0] - value[1] > 0:
        max_h += (value[0] - value[1])
        posled.append(value[2])
        if value[1] > max_plus:
            max_plus = value[1]
            max_plus_ind = counter_plus
        counter_plus += 1
    else:
        neplus.append(value[2])
        if value[0] > max_minus:
            max_minus = value[0]
            max_minus_ind = counter_minus
        counter_minus += 1

if counter_plus > 0:
    posled.append(posled.pop(max_plus_ind))
if counter_minus > 0:
    neplus = [neplus.pop(max_minus_ind)] + neplus
max_h += max(max_plus, max_minus)
posled += neplus

with open("output.txt", "w") as file:
    file.write(str(max_h) + '\n')
    for i in posled:
        file.write(str(i) + ' ')

finish = datetime.datetime.now()
print('Время работы: ' + str(finish - start))
