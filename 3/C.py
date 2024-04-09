n = int(input())
massiv = list(map(int, input().split()))

massiv = list(sorted(massiv))

digit_list = [0] * (max(massiv)+1)


for i in massiv:
    digit_list[i] += 1

answer = digit_list[0] + digit_list[1]

for i in range(1, len(digit_list) - 1):
    temp = digit_list[i] + digit_list[i + 1]
    if temp > answer:
        answer = temp

answer = len(massiv) - answer

print(answer)
