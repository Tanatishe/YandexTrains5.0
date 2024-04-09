with open('input.txt', 'r') as file:
    n = int(file.readline())

left = 1
righ = 1810000

while left <= righ:
    mid = (left + righ) // 2

    nex = mid + 1
    leng = 0
    for i in range(1, mid + 1):
        leng += i * nex
        nex -= 1

    leng = leng - 1

    if leng <= n:
        left = mid + 1
    else:
        righ = mid - 1

answer = left - 1

print(answer)
