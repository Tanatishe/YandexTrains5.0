n = int(input())

cleft = 1
cright = 10 ** 10

while cleft < cright:
    mid = (cleft + cright) // 2
    celoe = (mid ** 2 + mid) * 5
    celoe = int(str(celoe)[:-1])

    if celoe < n:
        cleft = mid + 1
    else:
        cright = mid - 1

celoe = (cleft ** 2 + cleft) * 5
celoe = int(str(celoe)[:-1])

if celoe < n:
    pass
else:
    cleft -= 1
a = (cleft ** 2 + cleft) * 5
a = int(str(a)[:-1]) if a > 9 else 0

atop = cleft + 1
abot = 1
raznica = n - a - 1

list = [[atop, abot], [abot, atop]][not cleft % 2]

list[0] = [list[0] - raznica, list[0] + raznica][not cleft % 2]
list[1] = [list[1] + raznica, list[1] - raznica][not cleft % 2]

print(f'{list[0]}/{list[1]}')
