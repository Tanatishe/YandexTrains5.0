l, x1, v1, x2, v2 = map(int, input().split())


def calcul(l, x1, v1, x2, v2):
    range = l / 2

    if x1 >= range:
        x1 = l - x1
        v1 *= -1
    if x2 >= range:
        x2 = l - x2
        v2 *= -1

    flag = x2 > x1
    start1 = [x1, x2][flag]
    start2 = [x2, x1][flag]
    speed1 = [v1, v2][flag]
    speed2 = [v2, v1][flag]

    if start1 == start2:
        answer = ('YES', float(0))
    elif speed1 == 0 and speed2 == 0:
        answer = ('NO',)
    elif speed2 >= 0 and (speed1 == 0 or
                          (speed2 > speed1 and (start1 - start2) / (speed2 - speed1) <= (range - start1) / speed1) or
                          speed1 < 0):
        answer = ('YES', float((start1 - start2) / (speed2 - speed1)))
    elif speed2 >= 0:
        time_to_turn = (range - start1) / speed1
        answer = ('YES', float(time_to_turn + (range - start2 - speed2 * time_to_turn) / (speed1 + speed2)))
    elif speed2 < 0 and (speed1 == 0 or
                         (speed1 < 0 and (abs(speed2) == abs(speed1) or (
                                 start2 / abs(speed2) < (start1 - start2) / (abs(speed2) - abs(speed1)))))):
        answer = (
            'YES', (start2 + start1) / (abs(speed2) + abs(speed1)))
    elif speed2 < 0 and speed1 < 0:
        answer = ('YES', (start1 - start2) / (abs(speed1) - abs(speed2)))
    elif speed2 < 0 and speed1 > 0 and abs(speed2) > speed1 and start2 / abs(speed2) < (range - start1) / speed1 and (
            start2 / abs(speed2) + (start1 + speed1 * (start2 / abs(speed2))) / (abs(speed2) - speed1)) < (
            range - start1) / speed1:
        answer = (
            'YES', float(start2 / abs(speed2) + (start1 + speed1 * (start2 / abs(speed2))) / (abs(speed2) - speed1)))
    elif speed2 < 0 and speed1 > 0 and abs(speed2) < speed1 and (
            ((range - start1) / speed1) + ((range - start2) + ((range - start1) / speed1) * abs(speed2)) / (
            speed1 - abs(speed2))) < start2 / abs(speed2):
        answer = (
            'YES', (((range - start1) / speed1) + ((range - start2) + ((range - start1) / speed1) * abs(speed2)) / (
                    speed1 - abs(speed2))))
    else:
        answer = ('YES', (range + start2 + (range - start1)) / (abs(speed2) + speed1))

    return answer


answer = calcul(l, x1, v1, x2, v2)
print(*answer, sep='\n')
