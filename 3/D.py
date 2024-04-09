import datetime
start = datetime.datetime.now()

with open('input.txt', 'r') as file:
    n, k = map(int, file.readline().split())
    massiv = list(map(int, file.readline().split()))

answer = 'NO'
len_massiv = len(massiv)

sample_massv = []
for i in range(100):
    sample_massv.append([])

next_number = massiv[0]
sample_massv[next_number % 100].append(next_number)
counter = 0

for i in massiv[1:]:
    if i in sample_massv[i % 100]:
        answer = 'YES'
        break
    sample_massv[i % 100].append(i)
    counter += 1
    if counter >= k:
        sample_massv[massiv[counter - k] % 100].pop(0)

print(answer)

finish = datetime.datetime.now()
print('Время работы: ' + str(finish - start))
