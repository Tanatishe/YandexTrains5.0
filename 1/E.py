answer = -1
flag = False
n, k, d = map(int, (input().split()))
prev = 1
while d > 0:
    d -= 1
    n = n * 10
    last = k - n % k
    if last == k:
        answer = n
        flag = True
        break
    if last <= 9:
        n += last
    else:
        break

else:
    answer = n


if flag:
    print(answer, end='')
    for i in range(d):
        print(0, end='')
else:
    print(answer)
