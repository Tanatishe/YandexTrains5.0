n = int(input())
summ = 0
for i in range(n):
    number = int(input())
    ost = [0, 1, 2, 2][number % 4]
    summ += number // 4 + ost

print(summ)
