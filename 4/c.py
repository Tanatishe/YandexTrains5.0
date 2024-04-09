import datetime

start = datetime.datetime.now()

with open('input.txt', 'r') as file:
    n, m = map(int, file.readline().split())
    array = list(map(int, file.readline().split()))
    qerryes = []
    for i in range(m):
        qerryes.append(list(map(int, file.readline().split())))

file = open('output.txt', 'w')
answer = -1
prefix = [0]
summa = 0
lenka = len(array)

flag = False
if array[0] == array[-1]:
    flag = True
    sum_all = sum(array)
if flag:
    for querry in qerryes:
        left = 0
        righ = lenka - 1
        answer = 1 if sum_all >= querry[1] and querry[1] % array[0] == 0 else -1
        file.write(str(answer) + '\n')
else:
    for i in array:
        summa += i
        prefix.append(summa)

    for querry in qerryes:
        left = 0
        righ = lenka - querry[0]

        while left <= righ:
            mid = (left + righ) // 2

            amount = prefix[mid + querry[0]] - prefix[mid]

            if amount == querry[1]:
                left = mid + 1
                righ = mid
            elif amount < querry[1]:
                left = mid + 1
            else:
                righ = mid - 1

        answer = left if left > 0 and prefix[left - 1 + querry[0]] - prefix[left - 1] == querry[1] else -1

        file.write(str(answer) + '\n')

file.close()

finish = datetime.datetime.now()
print('Время работы: ' + str(finish - start))
