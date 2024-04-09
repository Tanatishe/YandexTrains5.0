t = int(input())
massiv = []
for i in range(t):
    input()
    massiv.append(list(map(int, input().split())))

answer = []

for line in massiv:
    max_len = line[0]
    counter = 0
    numbers = []
    for number in line:
        max_len = min(max_len, number)

        if max_len > counter:
            counter += 1
        else:
            numbers.append(counter)
            counter = 1
            max_len = number

    numbers.append(counter)
    answer.append(len(numbers))
    answer.append(numbers)

for i in range(0, len(answer), 2):
    print(answer[i])
    print(*answer[i + 1])
