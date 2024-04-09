n = int(input())
numbers = list(map(int, input().split()))

norm = numbers[0] % 2
answer = ''

for i in range(1, n):
    if numbers[i] % 2 and norm:
        answer += 'x'
    elif numbers[i] % 2 and not norm:
        answer += '+'
        norm = not norm
    else:
        answer += '+'
print(answer)
